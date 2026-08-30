const aulasService = require('../modules/aulas/aulas.service');
const alertasService = require('../modules/alertas/alertas.service');
const { registrarAccion } = require('../modules/bitacora/bitacora.service');
const { UMBRAL_TEMPERATURA, UMBRAL_HUMEDAD, SIMULATOR_INTERVAL_MS } = require('../config/thresholds');

const SISTEMA = { id: null, nombre: 'Sistema', rol: 'Sistema' };

function clamp(valor, min, max) {
  return Math.min(max, Math.max(min, valor));
}

function pesoAleatorio(opciones) {
  const total = Object.values(opciones).reduce((a, b) => a + b, 0);
  let r = Math.random() * total;
  for (const [valor, peso] of Object.entries(opciones)) {
    if (r < peso) return valor;
    r -= peso;
  }
  return Object.keys(opciones)[0];
}

function siguienteLectura(estadoPrevio) {
  const ocupacion = Math.random() < 0.2
    ? (estadoPrevio.ocupacion === 'Ocupada' ? 'Vacía' : 'Ocupada')
    : estadoPrevio.ocupacion;

  const temperatura = Number(clamp(estadoPrevio.temperatura + (Math.random() * 3 - 1.5), 16, 34).toFixed(1));
  const humedad = Number(clamp(estadoPrevio.humedad + (Math.random() * 6 - 3), 35, 78).toFixed(0));

  const proyector = ocupacion === 'Ocupada'
    ? pesoAleatorio({ Encendido: 0.75, Apagado: 0.15, 'Sin señal HDMI': 0.10 })
    : pesoAleatorio({ Apagado: 0.85, Encendido: 0.15 });

  const climatizacion = ocupacion === 'Ocupada'
    ? pesoAleatorio({ Activo: 0.85, Apagado: 0.15 })
    : pesoAleatorio({ Apagado: 0.8, Activo: 0.2 });

  const conectividad = pesoAleatorio({ 'En línea': 0.9, Alerta: 0.1 });

  return { ocupacion, temperatura, humedad, proyector, climatizacion, conectividad };
}

function evaluarUmbrales(aula, lectura) {
  const alertasCreadas = [];

  const registrar = (tipoAnomalia, descripcion, lecturaAsociada, prioridad, responsable) => {
    const alerta = alertasService.crearSiNoExiste({
      aulaId: aula.id,
      tipoAnomalia,
      descripcion,
      lecturaAsociada,
      prioridad,
      responsable
    });
    if (alerta) alertasCreadas.push(alerta);
  };

  if (lectura.temperatura > UMBRAL_TEMPERATURA) {
    registrar(
      'Temperatura elevada',
      'Temperatura elevada.',
      `Lectura de ${lectura.temperatura}°C, por encima del umbral de ${UMBRAL_TEMPERATURA}°C.`,
      'Alta',
      'Mantenimiento'
    );
  }

  if (lectura.humedad > UMBRAL_HUMEDAD) {
    registrar(
      'Humedad elevada',
      'Humedad elevada.',
      `Lectura de ${lectura.humedad}%, por encima del umbral de ${UMBRAL_HUMEDAD}%.`,
      'Media',
      'Mantenimiento'
    );
  }

  if (lectura.proyector === 'Sin señal HDMI') {
    registrar(
      'Proyector sin señal HDMI',
      'Proyector sin señal HDMI.',
      'Equipo encendido, sin señal de entrada.',
      'Alta',
      'TI'
    );
  }

  if (lectura.climatizacion === 'Activo' && lectura.ocupacion === 'Vacía') {
    // RF-13/RF-16: apagado automático por ahorro energético en aula desocupada.
    // El sistema no solo detecta la anomalía, la corrige: apaga la climatización
    // antes de persistir la lectura y deja constancia (alerta ya Cerrada + bitácora).
    lectura.climatizacion = 'Apagado';

    const alerta = alertasService.registrarAutoResuelta({
      aulaId: aula.id,
      tipoAnomalia: 'Apagado automático por aula desocupada',
      descripcion: 'Climatización apagada automáticamente por ahorro energético.',
      lecturaAsociada: 'Aula vacía con climatización en estado Activo: el sistema la apagó de forma automática, sin intervención humana.',
      prioridad: 'Media',
      responsable: 'Sistema'
    });
    if (alerta) {
      alertasCreadas.push(alerta);
      registrarAccion(SISTEMA, 'Apagado automático', `Climatización de ${aula.nombre} apagada automáticamente (aula desocupada). Alerta ${alerta.codigo}.`);
    }
  }

  if (lectura.conectividad === 'Alerta') {
    registrar(
      'Aula sin conectividad estable',
      'Red IoT del aula reporta intermitencia.',
      'Pérdida de paquetes detectada en el enlace del aula.',
      'Media',
      'TI'
    );
  }

  return alertasCreadas;
}

function tick(io) {
  const aulas = aulasService.listarConEstado();
  const nuevasAlertas = [];

  for (const aula of aulas) {
    const lectura = siguienteLectura(aula);
    // evaluarUmbrales puede corregir lectura (p. ej. apagado automático) antes
    // de que se persista, para que el Panel y el historial reflejen el estado
    // ya corregido, no el estado anómalo transitorio.
    const alertasDeAula = evaluarUmbrales(aula, lectura);
    aulasService.guardarLectura({
      aulaId: aula.id,
      ...lectura,
      creadoEn: new Date().toISOString(),
      actualizadoEn: new Date().toISOString()
    });
    nuevasAlertas.push(...alertasDeAula);
  }

  const panel = {
    aulas: aulasService.listarConEstado(),
    resumen: aulasService.resumenPanel()
  };
  io.emit('panel:actualizado', panel);

  if (nuevasAlertas.length > 0) {
    io.emit('alertas:nuevas', nuevasAlertas);
    io.emit('alertas:resumen', alertasService.resumen());
  }
}

function start(io) {
  tick(io);
  const handle = setInterval(() => tick(io), SIMULATOR_INTERVAL_MS);
  return () => clearInterval(handle);
}

module.exports = { start };

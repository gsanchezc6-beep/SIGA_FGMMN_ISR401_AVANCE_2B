const { db } = require('../../db/database');

// Consumo simulado: cada lectura con proyector Encendido suma 0.6 kWh y cada
// lectura con climatizacion Activo suma 1.2 kWh (no hay medidor real, es MVP).
const KWH_PROYECTOR = 0.6;
const KWH_CLIMATIZACION = 1.2;

function condicionesLecturas({ aula, fechaInicio, fechaFin }) {
  const condiciones = [];
  const params = [];

  if (aula) {
    condiciones.push('aulas.nombre LIKE ?');
    params.push(`%${aula}%`);
  }
  if (fechaInicio) {
    condiciones.push('date(lecturas.creado_en) >= date(?)');
    params.push(fechaInicio);
  }
  if (fechaFin) {
    condiciones.push('date(lecturas.creado_en) <= date(?)');
    params.push(fechaFin);
  }

  return { where: condiciones.length ? `WHERE ${condiciones.join(' AND ')}` : '', params };
}

function generar(filtros = {}) {
  const { where, params } = condicionesLecturas(filtros);

  const lecturas = db.prepare(`
    SELECT lecturas.*, aulas.nombre AS aula_nombre
    FROM lecturas
    JOIN aulas ON aulas.id = lecturas.aula_id
    ${where}
  `).all(...params);

  const porAula = new Map();
  for (const l of lecturas) {
    if (!porAula.has(l.aula_nombre)) {
      porAula.set(l.aula_nombre, { lecturas: 0, ocupadas: 0, consumo: 0 });
    }
    const acc = porAula.get(l.aula_nombre);
    acc.lecturas += 1;
    if (l.ocupacion === 'Ocupada') acc.ocupadas += 1;
    if (l.proyector === 'Encendido') acc.consumo += KWH_PROYECTOR;
    if (l.climatizacion === 'Activo') acc.consumo += KWH_CLIMATIZACION;
  }

  const alertasCondiciones = [];
  const alertasParams = [];
  if (filtros.aula) {
    alertasCondiciones.push('aulas.nombre LIKE ?');
    alertasParams.push(`%${filtros.aula}%`);
  }
  if (filtros.fechaInicio) {
    alertasCondiciones.push('date(alertas.fecha_hora) >= date(?)');
    alertasParams.push(filtros.fechaInicio);
  }
  if (filtros.fechaFin) {
    alertasCondiciones.push('date(alertas.fecha_hora) <= date(?)');
    alertasParams.push(filtros.fechaFin);
  }
  const alertasWhere = alertasCondiciones.length ? `WHERE ${alertasCondiciones.join(' AND ')}` : '';

  const alertas = db.prepare(`
    SELECT alertas.*, aulas.nombre AS aula_nombre
    FROM alertas
    JOIN aulas ON aulas.id = alertas.aula_id
    ${alertasWhere}
  `).all(...alertasParams);

  const fallasPorAula = new Map();
  for (const a of alertas) {
    fallasPorAula.set(a.aula_nombre, (fallasPorAula.get(a.aula_nombre) || 0) + 1);
  }

  const tabla = [...porAula.entries()].map(([aulaNombre, acc]) => {
    const uso = acc.lecturas > 0 ? Math.round((acc.ocupadas / acc.lecturas) * 100) : 0;
    const fallas = fallasPorAula.get(aulaNombre) || 0;
    return {
      aula: aulaNombre,
      uso,
      consumo: Math.round(acc.consumo),
      fallas,
      estado: fallas > 2 ? 'Revisión' : 'Normal'
    };
  }).sort((a, b) => a.aula.localeCompare(b.aula));

  const totalLecturas = lecturas.length;
  const totalOcupadas = lecturas.filter((l) => l.ocupacion === 'Ocupada').length;
  const ocupacionPromedio = totalLecturas > 0 ? Math.round((totalOcupadas / totalLecturas) * 100) : 0;
  const consumoEstimado = Math.round(tabla.reduce((acc, fila) => acc + fila.consumo, 0));
  const ticketsTotal = db.prepare('SELECT COUNT(*) AS n FROM tickets').get().n;

  return {
    kpis: {
      ocupacionPromedio,
      consumoEstimado,
      incidenciasRegistradas: alertas.length + ticketsTotal
    },
    grafico: tabla.map((fila) => ({ aula: fila.aula, uso: fila.uso })),
    tabla
  };
}

module.exports = { generar };

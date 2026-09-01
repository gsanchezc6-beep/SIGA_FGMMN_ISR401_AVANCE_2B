const bcrypt = require('bcryptjs');
const { db } = require('./database');

const AULAS = [
  { nombre: 'Aula-101', tipo: 'Aula' },
  { nombre: 'Aula-102', tipo: 'Aula' },
  { nombre: 'Lab-201', tipo: 'Laboratorio' },
  { nombre: 'Aula-103', tipo: 'Aula' },
  { nombre: 'Aula-104', tipo: 'Aula' }
];

// Estado inicial calcado del mockup "Panel de control" para que la demo
// arranque con la misma foto que se disenio.
const ESTADO_INICIAL = {
  'Aula-101': { ocupacion: 'Ocupada', temperatura: 24, humedad: 58, proyector: 'Encendido', climatizacion: 'Activo', conectividad: 'En línea' },
  'Aula-102': { ocupacion: 'Vacía', temperatura: 22, humedad: 60, proyector: 'Apagado', climatizacion: 'Apagado', conectividad: 'En línea' },
  'Lab-201': { ocupacion: 'Ocupada', temperatura: 25, humedad: 55, proyector: 'Sin señal HDMI', climatizacion: 'Activo', conectividad: 'Alerta' },
  'Aula-103': { ocupacion: 'Vacía', temperatura: 28, humedad: 62, proyector: 'Apagado', climatizacion: 'Activo', conectividad: 'En línea' },
  'Aula-104': { ocupacion: 'Vacía', temperatura: 24, humedad: 58, proyector: 'Apagado', climatizacion: 'Activo', conectividad: 'En línea' }
};

function isoMinutesAgo(minutes) {
  return new Date(Date.now() - minutes * 60 * 1000).toISOString();
}

function seedIfEmpty() {
  const { count } = db.prepare('SELECT COUNT(*) AS count FROM usuarios').get();
  if (count > 0) {
    return false;
  }

  const insertUsuario = db.prepare(
    'INSERT INTO usuarios (nombre, usuario, password_hash, rol) VALUES (?, ?, ?, ?)'
  );
  insertUsuario.run('Admin SIGA', 'admin', bcrypt.hashSync('admin123', 10), 'Administrador');
  insertUsuario.run('Técnico TI', 'tecnico', bcrypt.hashSync('tecnico123', 10), 'Tecnico');

  const insertAula = db.prepare('INSERT INTO aulas (nombre, tipo) VALUES (?, ?)');
  const insertEstado = db.prepare(`
    INSERT INTO aula_estado (aula_id, ocupacion, temperatura, humedad, proyector, climatizacion, conectividad, actualizado_en)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  `);

  const aulaIds = {};
  for (const aula of AULAS) {
    const result = insertAula.run(aula.nombre, aula.tipo);
    aulaIds[aula.nombre] = Number(result.lastInsertRowid);
  }

  for (const [nombre, estado] of Object.entries(ESTADO_INICIAL)) {
    insertEstado.run(
      aulaIds[nombre],
      estado.ocupacion,
      estado.temperatura,
      estado.humedad,
      estado.proyector,
      estado.climatizacion,
      estado.conectividad,
      isoMinutesAgo(0)
    );
  }

  // Historial de lecturas de las ultimas horas para que Reportes tenga datos
  // desde el primer arranque, sin depender de que el simulador ya haya corrido.
  const insertLectura = db.prepare(`
    INSERT INTO lecturas (aula_id, ocupacion, temperatura, humedad, proyector, climatizacion, conectividad, creado_en)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  `);
  for (const [nombre, estado] of Object.entries(ESTADO_INICIAL)) {
    for (let i = 12; i >= 1; i--) {
      insertLectura.run(
        aulaIds[nombre],
        estado.ocupacion,
        estado.temperatura + (Math.random() * 2 - 1),
        estado.humedad + (Math.random() * 4 - 2),
        estado.proyector,
        estado.climatizacion,
        estado.conectividad,
        isoMinutesAgo(i * 20)
      );
    }
  }

  const insertAlerta = db.prepare(`
    INSERT INTO alertas (codigo, aula_id, tipo_anomalia, descripcion, lectura_asociada, prioridad, fecha_hora, estado, responsable)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);
  insertAlerta.run(
    'AL-001',
    aulaIds['Lab-201'],
    'Proyector sin señal HDMI',
    'Proyector sin señal HDMI.',
    'Equipo encendido, sin señal de entrada.',
    'Alta',
    isoMinutesAgo(95),
    'Pendiente',
    'TI'
  );
  insertAlerta.run(
    'AL-002',
    aulaIds['Aula-103'],
    'Climatización activa fuera de horario',
    'Climatización activa fuera de horario.',
    'Aula vacía con climatización en estado Activo.',
    'Media',
    isoMinutesAgo(55),
    'En proceso',
    'Mantenimiento'
  );

  const insertTicket = db.prepare(`
    INSERT INTO tickets (codigo, aula_id, equipo, tipo_incidencia, prioridad, descripcion, estado, alerta_id, creado_por, creado_en, actualizado_en)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `);
  const alertaLab201 = db.prepare('SELECT id FROM alertas WHERE codigo = ?').get('AL-001');
  const alertaAula103 = db.prepare('SELECT id FROM alertas WHERE codigo = ?').get('AL-002');

  insertTicket.run('TK-001', aulaIds['Lab-201'], 'Proyector', 'HDMI', 'Alta', 'Proyector sin señal HDMI en Lab-201.', 'Abierto', alertaLab201.id, 'Admin SIGA', isoMinutesAgo(90), isoMinutesAgo(90));
  insertTicket.run('TK-002', aulaIds['Aula-103'], 'Climatización', 'Aire', 'Media', 'Climatización activa fuera de horario en Aula-103.', 'En proceso', alertaAula103.id, 'Técnico TI', isoMinutesAgo(50), isoMinutesAgo(20));
  insertTicket.run('TK-003', aulaIds['Aula-102'], 'Sensor', 'Sensor', 'Media', 'Sensor de ocupación con lecturas intermitentes en Aula-102.', 'Abierto', null, 'Técnico TI', isoMinutesAgo(180), isoMinutesAgo(180));
  insertTicket.run('TK-004', aulaIds['Aula-101'], 'Climatización', 'Temperatura', 'Baja', 'Temperatura ambiente por debajo de confort en Aula-101.', 'Cerrado', null, 'Admin SIGA', isoMinutesAgo(400), isoMinutesAgo(200));

  const insertHistorial = db.prepare(`
    INSERT INTO ticket_historial (ticket_id, fecha, accion, usuario, observacion, estado_anterior, estado_nuevo)
    VALUES (?, ?, ?, ?, ?, ?, ?)
  `);
  const tk002 = db.prepare('SELECT id FROM tickets WHERE codigo = ?').get('TK-002');
  const tk004 = db.prepare('SELECT id FROM tickets WHERE codigo = ?').get('TK-004');
  insertHistorial.run(tk002.id, isoMinutesAgo(50), 'Creación de ticket', 'Técnico TI', 'Generado desde alerta AL-002.', null, 'Abierto');
  insertHistorial.run(tk002.id, isoMinutesAgo(20), 'Cambio de estado', 'Técnico TI', 'Se envió cuadrilla de mantenimiento.', 'Abierto', 'En proceso');
  insertHistorial.run(tk004.id, isoMinutesAgo(400), 'Creación de ticket', 'Admin SIGA', 'Reporte manual de docente.', null, 'Abierto');
  insertHistorial.run(tk004.id, isoMinutesAgo(200), 'Cambio de estado', 'Admin SIGA', 'Sensor recalibrado, incidencia resuelta.', 'Abierto', 'Cerrado');

  const insertBitacora = db.prepare(`
    INSERT INTO bitacora (usuario_id, usuario_nombre, rol, accion, detalle, fecha_hora)
    VALUES (?, ?, ?, ?, ?, ?)
  `);
  insertBitacora.run(1, 'Admin SIGA', 'Administrador', 'Inicio de sesión', 'Acceso al sistema SIGA.', isoMinutesAgo(400));
  insertBitacora.run(1, 'Admin SIGA', 'Administrador', 'Creación de ticket', 'Ticket TK-004 registrado para Aula-101.', isoMinutesAgo(400));
  insertBitacora.run(2, 'Técnico TI', 'Tecnico', 'Inicio de sesión', 'Acceso al sistema SIGA.', isoMinutesAgo(200));
  insertBitacora.run(2, 'Técnico TI', 'Tecnico', 'Cambio de estado de ticket', 'Ticket TK-004 pasó de Abierto a Cerrado.', isoMinutesAgo(200));
  insertBitacora.run(2, 'Técnico TI', 'Tecnico', 'Cambio de estado de ticket', 'Ticket TK-002 pasó de Abierto a En proceso.', isoMinutesAgo(20));

  return true;
}

if (require.main === module) {
  const seeded = seedIfEmpty();
  console.log(seeded ? 'Base de datos poblada con datos de ejemplo.' : 'La base de datos ya tenia datos, no se modifico nada.');
}

module.exports = { seedIfEmpty };

const { db } = require('../../db/database');

function siguienteCodigo() {
  const { total } = db.prepare('SELECT COUNT(*) AS total FROM tickets').get();
  return `TK-${String(total + 1).padStart(3, '0')}`;
}

function baseQuery() {
  return `
    SELECT tickets.*, aulas.nombre AS aula_nombre
    FROM tickets
    JOIN aulas ON aulas.id = tickets.aula_id
  `;
}

function listar() {
  return db.prepare(`${baseQuery()} ORDER BY tickets.creado_en DESC`).all();
}

function obtener(id) {
  return db.prepare(`${baseQuery()} WHERE tickets.id = ?`).get(id);
}

function obtenerPorCodigo(codigo) {
  return db.prepare(`${baseQuery()} WHERE tickets.codigo = ?`).get(codigo);
}

const insertTicket = db.prepare(`
  INSERT INTO tickets (codigo, aula_id, equipo, tipo_incidencia, prioridad, descripcion, estado, alerta_id, creado_por, creado_en, actualizado_en)
  VALUES (?, ?, ?, ?, ?, ?, 'Abierto', ?, ?, ?, ?)
`);

const insertHistorial = db.prepare(`
  INSERT INTO ticket_historial (ticket_id, fecha, accion, usuario, observacion, estado_anterior, estado_nuevo)
  VALUES (?, ?, ?, ?, ?, ?, ?)
`);

function crear({ aulaId, equipo, tipoIncidencia, prioridad, descripcion, alertaId = null }, usuario) {
  const ahora = new Date().toISOString();
  const codigo = siguienteCodigo();
  const result = insertTicket.run(codigo, aulaId, equipo, tipoIncidencia, prioridad, descripcion, alertaId, usuario.nombre, ahora, ahora);
  const ticketId = Number(result.lastInsertRowid);

  insertHistorial.run(
    ticketId,
    ahora,
    'Creación de ticket',
    usuario.nombre,
    alertaId ? 'Generado a partir de una alerta.' : 'Solicitud registrada manualmente.',
    null,
    'Abierto'
  );

  return obtener(ticketId);
}

function cambiarEstado(id, nuevoEstado, usuario, observacion = '') {
  const ticket = obtener(id);
  if (!ticket) return null;

  const ahora = new Date().toISOString();
  db.prepare('UPDATE tickets SET estado = ?, actualizado_en = ? WHERE id = ?').run(nuevoEstado, ahora, id);
  insertHistorial.run(id, ahora, 'Cambio de estado', usuario.nombre, observacion, ticket.estado, nuevoEstado);

  return obtener(id);
}

function historial(ticketId) {
  return db.prepare('SELECT * FROM ticket_historial WHERE ticket_id = ? ORDER BY fecha ASC').all(ticketId);
}

function resumen() {
  const total = db.prepare('SELECT COUNT(*) AS n FROM tickets').get().n;
  const abiertos = db.prepare("SELECT COUNT(*) AS n FROM tickets WHERE estado != 'Cerrado'").get().n;
  return { total, abiertos };
}

module.exports = { listar, obtener, obtenerPorCodigo, crear, cambiarEstado, historial, resumen };

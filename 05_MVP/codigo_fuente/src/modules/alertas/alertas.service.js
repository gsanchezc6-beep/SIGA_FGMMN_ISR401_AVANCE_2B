const { db } = require('../../db/database');

function siguienteCodigo() {
  const { total } = db.prepare('SELECT COUNT(*) AS total FROM alertas').get();
  return `AL-${String(total + 1).padStart(3, '0')}`;
}

const insertAlerta = db.prepare(`
  INSERT INTO alertas (codigo, aula_id, tipo_anomalia, descripcion, lectura_asociada, prioridad, fecha_hora, estado, responsable)
  VALUES (?, ?, ?, ?, ?, ?, ?, 'Pendiente', ?)
`);

const alertaAbiertaExistente = db.prepare(`
  SELECT id FROM alertas
  WHERE aula_id = ? AND tipo_anomalia = ? AND estado IN ('Pendiente', 'En proceso')
`);

// Evita inundar la demo con alertas duplicadas: si ya hay una abierta del
// mismo tipo para la misma aula, no se crea otra hasta que se cierre.
function crearSiNoExiste({ aulaId, tipoAnomalia, descripcion, lecturaAsociada, prioridad, responsable }) {
  const existente = alertaAbiertaExistente.get(aulaId, tipoAnomalia);
  if (existente) return null;

  const codigo = siguienteCodigo();
  const result = insertAlerta.run(
    codigo,
    aulaId,
    tipoAnomalia,
    descripcion,
    lecturaAsociada,
    prioridad,
    new Date().toISOString(),
    responsable
  );
  return obtener(Number(result.lastInsertRowid));
}

const insertAlertaResuelta = db.prepare(`
  INSERT INTO alertas (codigo, aula_id, tipo_anomalia, descripcion, lectura_asociada, prioridad, fecha_hora, estado, responsable)
  VALUES (?, ?, ?, ?, ?, ?, ?, 'Cerrada', ?)
`);

// Para acciones que el propio sistema resuelve en el momento (p. ej. apagado
// automático): queda registrada como alerta ya Cerrada, no como pendiente de
// atender, porque no requiere que un humano actúe sobre ella.
function registrarAutoResuelta({ aulaId, tipoAnomalia, descripcion, lecturaAsociada, prioridad, responsable }) {
  const codigo = siguienteCodigo();
  const result = insertAlertaResuelta.run(
    codigo,
    aulaId,
    tipoAnomalia,
    descripcion,
    lecturaAsociada,
    prioridad,
    new Date().toISOString(),
    responsable
  );
  return obtener(Number(result.lastInsertRowid));
}

function baseQuery() {
  return `
    SELECT alertas.*, aulas.nombre AS aula_nombre
    FROM alertas
    JOIN aulas ON aulas.id = alertas.aula_id
  `;
}

function listar({ aula, prioridad, estado, fecha } = {}) {
  const condiciones = [];
  const params = [];

  if (aula) {
    condiciones.push('aulas.nombre LIKE ?');
    params.push(`%${aula}%`);
  }
  if (prioridad) {
    condiciones.push('alertas.prioridad = ?');
    params.push(prioridad);
  }
  if (estado) {
    condiciones.push('alertas.estado = ?');
    params.push(estado);
  }
  if (fecha) {
    condiciones.push("date(alertas.fecha_hora) = date(?)");
    params.push(fecha);
  }

  const where = condiciones.length ? `WHERE ${condiciones.join(' AND ')}` : '';
  const sql = `${baseQuery()} ${where} ORDER BY alertas.fecha_hora DESC`;
  return db.prepare(sql).all(...params);
}

function obtener(id) {
  return db.prepare(`${baseQuery()} WHERE alertas.id = ?`).get(id);
}

function cambiarEstado(id, estado) {
  db.prepare('UPDATE alertas SET estado = ? WHERE id = ?').run(estado, id);
  return obtener(id);
}

function asignarResponsable(id, responsable) {
  db.prepare('UPDATE alertas SET responsable = ? WHERE id = ?').run(responsable, id);
  return obtener(id);
}

function resumen() {
  const criticas = db.prepare("SELECT COUNT(*) AS n FROM alertas WHERE prioridad = 'Alta' AND estado != 'Cerrada'").get().n;
  const pendientes = db.prepare("SELECT COUNT(*) AS n FROM alertas WHERE estado = 'Pendiente'").get().n;
  const atendidasHoy = db.prepare(`
    SELECT COUNT(*) AS n FROM alertas
    WHERE estado = 'Cerrada' AND date(fecha_hora) = date('now')
  `).get().n;
  return { criticas, pendientes, atendidasHoy };
}

module.exports = { crearSiNoExiste, registrarAutoResuelta, listar, obtener, cambiarEstado, asignarResponsable, resumen };

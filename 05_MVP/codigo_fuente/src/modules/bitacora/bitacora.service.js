const { db } = require('../../db/database');

const insertStmt = db.prepare(`
  INSERT INTO bitacora (usuario_id, usuario_nombre, rol, accion, detalle, fecha_hora)
  VALUES (?, ?, ?, ?, ?, ?)
`);

function registrarAccion(usuario, accion, detalle = '') {
  insertStmt.run(
    usuario.id,
    usuario.nombre,
    usuario.rol,
    accion,
    detalle,
    new Date().toISOString()
  );
}

function listarAcciones() {
  return db.prepare('SELECT * FROM bitacora ORDER BY fecha_hora DESC').all();
}

module.exports = { registrarAccion, listarAcciones };

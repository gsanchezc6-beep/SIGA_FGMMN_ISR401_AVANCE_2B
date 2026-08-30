const bcrypt = require('bcryptjs');
const { db } = require('../../db/database');

const findByUsuario = db.prepare('SELECT * FROM usuarios WHERE usuario = ?');

function verificarCredenciales(usuario, password) {
  const registro = findByUsuario.get(usuario);
  if (!registro) return null;
  if (!bcrypt.compareSync(password, registro.password_hash)) return null;
  return { id: registro.id, nombre: registro.nombre, usuario: registro.usuario, rol: registro.rol };
}

module.exports = { verificarCredenciales };

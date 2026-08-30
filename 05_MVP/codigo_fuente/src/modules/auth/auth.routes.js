const express = require('express');
const { verificarCredenciales } = require('./auth.service');
const { registrarAccion } = require('../bitacora/bitacora.service');
const { requireAuth } = require('../../middleware/auth');

const router = express.Router();

router.post('/login', (req, res) => {
  const { usuario, password } = req.body || {};
  if (!usuario || !password) {
    return res.status(400).json({ error: 'Usuario y contraseña son obligatorios.' });
  }

  const cuenta = verificarCredenciales(usuario, password);
  if (!cuenta) {
    return res.status(401).json({ error: 'Usuario o contraseña incorrectos.' });
  }

  req.session.usuario = cuenta;
  registrarAccion(cuenta, 'Inicio de sesión', 'Acceso al sistema SIGA.');
  res.json({ usuario: cuenta });
});

router.post('/logout', requireAuth, (req, res) => {
  const cuenta = req.session.usuario;
  registrarAccion(cuenta, 'Cierre de sesión', 'Salida del sistema SIGA.');
  req.session.destroy(() => {
    res.clearCookie('connect.sid');
    res.json({ ok: true });
  });
});

router.get('/me', (req, res) => {
  res.json({ usuario: req.session.usuario || null });
});

module.exports = router;

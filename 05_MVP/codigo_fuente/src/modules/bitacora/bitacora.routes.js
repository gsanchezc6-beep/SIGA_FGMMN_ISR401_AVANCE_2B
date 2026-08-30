const express = require('express');
const bitacoraService = require('./bitacora.service');
const { requireAuth, requireRole } = require('../../middleware/auth');

const router = express.Router();

router.get('/', requireAuth, requireRole('Administrador'), (req, res) => {
  res.json({ registros: bitacoraService.listarAcciones() });
});

module.exports = router;

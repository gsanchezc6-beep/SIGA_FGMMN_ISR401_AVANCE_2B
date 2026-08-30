const express = require('express');
const reportesService = require('./reportes.service');
const { requireAuth, requireRole } = require('../../middleware/auth');

const router = express.Router();

router.get('/', requireAuth, requireRole('Administrador'), (req, res) => {
  const { aula, fechaInicio, fechaFin, tipo } = req.query;
  res.json(reportesService.generar({ aula, fechaInicio, fechaFin, tipo }));
});

module.exports = router;

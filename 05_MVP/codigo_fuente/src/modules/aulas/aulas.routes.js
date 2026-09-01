const express = require('express');
const aulasService = require('./aulas.service');
const { requireAuth } = require('../../middleware/auth');

const router = express.Router();

router.get('/', requireAuth, (req, res) => {
  res.json({
    aulas: aulasService.listarConEstado(),
    resumen: aulasService.resumenPanel()
  });
});

router.get('/:id', requireAuth, (req, res) => {
  const aula = aulasService.obtenerConEstado(Number(req.params.id));
  if (!aula) return res.status(404).json({ error: 'Aula no encontrada.' });
  res.json({ aula });
});

module.exports = router;

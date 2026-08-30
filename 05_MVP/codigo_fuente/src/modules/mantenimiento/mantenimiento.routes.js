const express = require('express');
const mantenimientoService = require('./mantenimiento.service');
const aulasService = require('../aulas/aulas.service');
const { registrarAccion } = require('../bitacora/bitacora.service');
const { requireAuth } = require('../../middleware/auth');

function crearRouter(io) {
  const router = express.Router();

  router.get('/', requireAuth, (req, res) => {
    res.json({ tickets: mantenimientoService.listar(), resumen: mantenimientoService.resumen() });
  });

  router.get('/:id/historial', requireAuth, (req, res) => {
    const ticket = mantenimientoService.obtener(Number(req.params.id));
    if (!ticket) return res.status(404).json({ error: 'Ticket no encontrado.' });
    res.json({ ticket, historial: mantenimientoService.historial(ticket.id) });
  });

  router.post('/', requireAuth, (req, res) => {
    const { aulaId, equipo, tipoIncidencia, prioridad, descripcion } = req.body || {};
    if (!aulaId || !equipo || !tipoIncidencia || !prioridad || !descripcion) {
      return res.status(400).json({ error: 'Todos los campos de la solicitud son obligatorios.' });
    }

    const aula = aulasService.obtenerConEstado(Number(aulaId));
    if (!aula) return res.status(400).json({ error: 'Aula no válida.' });

    const ticket = mantenimientoService.crear(
      { aulaId: Number(aulaId), equipo, tipoIncidencia, prioridad, descripcion },
      req.session.usuario
    );

    registrarAccion(req.session.usuario, 'Creación de ticket', `Ticket ${ticket.codigo} registrado para ${aula.nombre}.`);
    io.emit('tickets:actualizado', { tickets: mantenimientoService.listar(), resumen: mantenimientoService.resumen() });
    res.status(201).json({ ticket });
  });

  router.patch('/:id/estado', requireAuth, (req, res) => {
    const { estado, observacion } = req.body || {};
    const permitido = ['Abierto', 'En proceso', 'Cerrado'];
    if (!permitido.includes(estado)) {
      return res.status(400).json({ error: 'Estado no válido.' });
    }

    const ticket = mantenimientoService.cambiarEstado(Number(req.params.id), estado, req.session.usuario, observacion || '');
    if (!ticket) return res.status(404).json({ error: 'Ticket no encontrado.' });

    registrarAccion(req.session.usuario, 'Cambio de estado de ticket', `Ticket ${ticket.codigo} pasó a estado ${estado}.`);
    io.emit('tickets:actualizado', { tickets: mantenimientoService.listar(), resumen: mantenimientoService.resumen() });
    res.json({ ticket });
  });

  return router;
}

module.exports = crearRouter;

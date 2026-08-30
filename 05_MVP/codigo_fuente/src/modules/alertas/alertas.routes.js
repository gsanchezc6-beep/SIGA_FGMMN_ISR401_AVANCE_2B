const express = require('express');
const alertasService = require('./alertas.service');
const mantenimientoService = require('../mantenimiento/mantenimiento.service');
const { registrarAccion } = require('../bitacora/bitacora.service');
const { requireAuth } = require('../../middleware/auth');

function crearRouter(io) {
  const router = express.Router();

  router.get('/', requireAuth, (req, res) => {
    const { aula, prioridad, estado, fecha } = req.query;
    res.json({
      alertas: alertasService.listar({ aula, prioridad, estado, fecha }),
      resumen: alertasService.resumen()
    });
  });

  router.get('/:id', requireAuth, (req, res) => {
    const alerta = alertasService.obtener(Number(req.params.id));
    if (!alerta) return res.status(404).json({ error: 'Alerta no encontrada.' });
    res.json({ alerta });
  });

  router.patch('/:id/estado', requireAuth, (req, res) => {
    const { estado } = req.body || {};
    const permitido = ['Pendiente', 'En proceso', 'Cerrada'];
    if (!permitido.includes(estado)) {
      return res.status(400).json({ error: 'Estado no válido.' });
    }

    const alerta = alertasService.cambiarEstado(Number(req.params.id), estado);
    if (!alerta) return res.status(404).json({ error: 'Alerta no encontrada.' });

    registrarAccion(req.session.usuario, 'Cambio de estado de alerta', `Alerta ${alerta.codigo} (${alerta.aula_nombre}) pasó a estado ${estado}.`);
    io.emit('alertas:resumen', alertasService.resumen());
    res.json({ alerta });
  });

  router.patch('/:id/responsable', requireAuth, (req, res) => {
    const { responsable } = req.body || {};
    if (!responsable) return res.status(400).json({ error: 'Responsable es obligatorio.' });

    const alerta = alertasService.asignarResponsable(Number(req.params.id), responsable);
    if (!alerta) return res.status(404).json({ error: 'Alerta no encontrada.' });

    registrarAccion(req.session.usuario, 'Notificación de responsable', `Alerta ${alerta.codigo} (${alerta.aula_nombre}) notificada a ${responsable}.`);
    res.json({ alerta });
  });

  router.post('/:id/ticket', requireAuth, (req, res) => {
    const alerta = alertasService.obtener(Number(req.params.id));
    if (!alerta) return res.status(404).json({ error: 'Alerta no encontrada.' });

    const ticket = mantenimientoService.crear({
      aulaId: alerta.aula_id,
      equipo: alerta.tipo_anomalia,
      tipoIncidencia: alerta.tipo_anomalia,
      prioridad: alerta.prioridad,
      descripcion: alerta.descripcion,
      alertaId: alerta.id
    }, req.session.usuario);

    alertasService.cambiarEstado(alerta.id, 'En proceso');

    registrarAccion(req.session.usuario, 'Creación de ticket desde alerta', `Ticket ${ticket.codigo} generado a partir de la alerta ${alerta.codigo}.`);
    io.emit('tickets:actualizado', { tickets: mantenimientoService.listar(), resumen: mantenimientoService.resumen() });
    io.emit('alertas:resumen', alertasService.resumen());
    res.status(201).json({ ticket, alerta: alertasService.obtener(alerta.id) });
  });

  return router;
}

module.exports = crearRouter;

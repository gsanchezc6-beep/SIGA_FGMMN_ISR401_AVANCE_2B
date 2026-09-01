function badgeEstadoTicket(valor) {
  if (valor === 'Abierto') return `<span class="badge yellow">Abierto</span>`;
  if (valor === 'En proceso') return `<span class="badge green">En proceso</span>`;
  return `<span class="badge gray">Cerrado</span>`;
}

let ticketSeleccionado = null;
let aulasCache = [];

async function cargarVista(usuario) {
  const [aulasDatos, ticketsDatos] = await Promise.all([
    api('/api/aulas'),
    api('/api/tickets')
  ]);
  aulasCache = aulasDatos.aulas;
  renderMantenimiento(usuario, ticketsDatos.tickets);
}

function renderMantenimiento(usuario, tickets) {
  const filas = tickets.map((t) => `
    <tr data-id="${t.id}" style="cursor:pointer;${ticketSeleccionado === t.id ? 'background:#f3f6ff;' : ''}">
      <td>${t.codigo}</td>
      <td>${t.aula_nombre}</td>
      <td>${t.tipo_incidencia}</td>
      <td>${badgeEstadoTicket(t.estado)}</td>
    </tr>
  `).join('');

  const opcionesAula = aulasCache.map((a) => `<option value="${a.id}">${a.nombre}</option>`).join('');

  document.getElementById('main-content').innerHTML = `
    <h2>Gestión de solicitudes de mantenimiento</h2>
    <div class="two-col">
      <div class="detail-box">
        <h3>Registrar solicitud</h3>
        <form id="ticket-form">
          <div class="field" style="margin-bottom:14px;">
            <label for="t-aula">Aula</label>
            <select id="t-aula" required>
              <option value="">Seleccione el aula</option>
              ${opcionesAula}
            </select>
          </div>
          <div class="field" style="margin-bottom:14px;">
            <label for="t-equipo">Equipo afectado</label>
            <select id="t-equipo" required>
              <option value="">Proyector / Climatización / Sensor / Conectividad</option>
              <option value="Proyector">Proyector</option>
              <option value="Climatización">Climatización</option>
              <option value="Sensor">Sensor</option>
              <option value="Conectividad">Conectividad</option>
            </select>
          </div>
          <div class="field" style="margin-bottom:14px;">
            <label for="t-tipo">Tipo de incidencia</label>
            <select id="t-tipo" required>
              <option value="">Seleccione el tipo</option>
              <option value="HDMI">HDMI</option>
              <option value="Aire">Aire</option>
              <option value="Sensor">Sensor</option>
              <option value="Temperatura">Temperatura</option>
              <option value="Conectividad">Conectividad</option>
              <option value="Otro">Otro</option>
            </select>
          </div>
          <div class="field" style="margin-bottom:14px;">
            <label for="t-prioridad">Prioridad</label>
            <select id="t-prioridad" required>
              <option value="">Baja / Media / Alta</option>
              <option value="Baja">Baja</option>
              <option value="Media">Media</option>
              <option value="Alta">Alta</option>
            </select>
          </div>
          <div class="field" style="margin-bottom:16px;">
            <label for="t-descripcion">Descripción</label>
            <textarea id="t-descripcion" placeholder="Detalle de la incidencia observada." required></textarea>
          </div>
          <div class="action-buttons">
            <button class="btn primary" type="submit">Guardar solicitud</button>
            <button class="btn" type="button" id="t-cancelar">Cancelar</button>
          </div>
        </form>
      </div>

      <div class="detail-box">
        <h3>Seguimiento de tickets</h3>
        <table>
          <thead><tr><th>Ticket</th><th>Aula</th><th>Incidencia</th><th>Estado</th></tr></thead>
          <tbody>${filas || `<tr><td colspan="4" class="empty-state">Sin tickets registrados.</td></tr>`}</tbody>
        </table>
        <h3 style="margin-top:22px;">Historial del ticket seleccionado</h3>
        <div id="historial-ticket" class="empty-state" style="padding:12px 0;">Selecciona un ticket para ver su historial.</div>
      </div>
    </div>
  `;

  document.getElementById('t-cancelar').addEventListener('click', () => document.getElementById('ticket-form').reset());

  document.getElementById('ticket-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
      await api('/api/tickets', {
        method: 'POST',
        body: {
          aulaId: Number(document.getElementById('t-aula').value),
          equipo: document.getElementById('t-equipo').value,
          tipoIncidencia: document.getElementById('t-tipo').value,
          prioridad: document.getElementById('t-prioridad').value,
          descripcion: document.getElementById('t-descripcion').value
        }
      });
      showToast('Solicitud registrada correctamente.');
      await cargarVista(usuario);
    } catch (err) {
      showToast(err.message);
    }
  });

  document.querySelectorAll('tbody tr[data-id]').forEach((tr) => {
    tr.addEventListener('click', () => {
      ticketSeleccionado = Number(tr.dataset.id);
      mostrarHistorial(usuario, ticketSeleccionado, tickets);
    });
  });

  if (ticketSeleccionado) {
    mostrarHistorial(usuario, ticketSeleccionado, tickets);
  }
}

async function mostrarHistorial(usuario, ticketId, tickets) {
  const { ticket, historial } = await api(`/api/tickets/${ticketId}/historial`);

  const filasHistorial = historial.map((h) => `
    <tr>
      <td>${formatFecha(h.fecha)}</td>
      <td>${h.accion}</td>
      <td>${h.usuario}</td>
      <td>${h.observacion || '-'}</td>
      <td>${h.estado_anterior || '-'}</td>
      <td>${h.estado_nuevo}</td>
    </tr>
  `).join('');

  const opciones = ['Abierto', 'En proceso', 'Cerrado']
    .map((v) => `<option value="${v}" ${v === ticket.estado ? 'selected' : ''}>${v}</option>`)
    .join('');

  document.getElementById('historial-ticket').outerHTML = `
    <div id="historial-ticket">
      <div style="display:flex;gap:10px;align-items:center;margin-bottom:12px;">
        <strong>${ticket.codigo}</strong> · ${ticket.aula_nombre}
        <select id="cambio-estado-ticket">${opciones}</select>
        <button class="btn action" id="guardar-estado-ticket">Cambiar estado</button>
      </div>
      <table>
        <thead><tr><th>Fecha</th><th>Acción</th><th>Usuario</th><th>Observación</th><th>Estado anterior</th><th>Estado nuevo</th></tr></thead>
        <tbody>${filasHistorial || `<tr><td colspan="6" class="empty-state">Sin movimientos registrados.</td></tr>`}</tbody>
      </table>
    </div>
  `;

  document.getElementById('guardar-estado-ticket').addEventListener('click', async () => {
    const estado = document.getElementById('cambio-estado-ticket').value;
    await api(`/api/tickets/${ticketId}/estado`, { method: 'PATCH', body: { estado, observacion: `Cambio manual a ${estado}.` } });
    showToast('Estado del ticket actualizado.');
    await cargarVista(usuario);
  });
}

(async () => {
  const usuario = await initPage({ title: 'Mantenimiento', activeKey: 'mantenimiento' });
  await cargarVista(usuario);

  const socket = conectarSocket();
  socket.on('tickets:actualizado', () => cargarVista(usuario));
})();

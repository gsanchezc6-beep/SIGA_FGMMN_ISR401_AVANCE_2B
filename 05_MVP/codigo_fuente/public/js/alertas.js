function badgePrioridad(valor) {
  if (valor === 'Alta') return `<span class="badge red">Alta</span>`;
  if (valor === 'Media') return `<span class="badge yellow">Media</span>`;
  return `<span class="badge green">Baja</span>`;
}

function badgeEstadoAlerta(valor) {
  if (valor === 'Pendiente') return `<span class="badge yellow">Pendiente</span>`;
  if (valor === 'En proceso') return `<span class="badge green">En proceso</span>`;
  return `<span class="badge gray">Cerrada</span>`;
}

let alertaSeleccionada = null;
let ultimosFiltros = {};

function leerFiltrosDeUrl() {
  const params = new URLSearchParams(window.location.search);
  return { aula: params.get('aula') || '' };
}

async function cargarAlertas(usuario, filtros = {}) {
  ultimosFiltros = filtros;
  const query = new URLSearchParams(filtros);
  const datos = await api(`/api/alertas?${query.toString()}`);
  renderAlertas(usuario, datos);
}

function renderAlertas(usuario, datos) {
  const { alertas, resumen } = datos;

  const filas = alertas.map((a) => `
    <tr data-id="${a.id}" style="cursor:pointer;${alertaSeleccionada === a.id ? 'background:#f3f6ff;' : ''}">
      <td>${a.codigo}</td>
      <td>${a.aula_nombre}</td>
      <td>${a.tipo_anomalia}</td>
      <td>${badgePrioridad(a.prioridad)}</td>
      <td>${formatFecha(a.fecha_hora)}</td>
      <td>${badgeEstadoAlerta(a.estado)}</td>
      <td>${a.responsable}</td>
    </tr>
  `).join('');

  document.getElementById('main-content').innerHTML = `
    <h2>Alertas generadas por el sistema</h2>
    <div class="kpi-row">
      <div class="kpi-card"><div class="label">Alertas críticas</div><div class="value">${resumen.criticas}</div></div>
      <div class="kpi-card"><div class="label">Pendientes</div><div class="value">${resumen.pendientes}</div></div>
      <div class="kpi-card"><div class="label">Atendidas hoy</div><div class="value">${resumen.atendidasHoy}</div></div>
    </div>

    <div class="filters-bar">
      <input id="f-aula" placeholder="Aula" value="${ultimosFiltros.aula || ''}" />
      <select id="f-prioridad">
        <option value="">Criticidad</option>
        <option value="Alta">Alta</option>
        <option value="Media">Media</option>
        <option value="Baja">Baja</option>
      </select>
      <input id="f-fecha" type="date" />
      <select id="f-estado">
        <option value="">Estado</option>
        <option value="Pendiente">Pendiente</option>
        <option value="En proceso">En proceso</option>
        <option value="Cerrada">Cerrada</option>
      </select>
      <div class="spacer"></div>
      <button class="btn primary" id="aplicar-filtros">Aplicar filtros</button>
    </div>

    <div class="panel-card">
      <div class="panel-title">Panel consolidado de aulas</div>
      <table>
        <thead>
          <tr><th>ID</th><th>Aula</th><th>Tipo de anomalía</th><th>Prioridad</th><th>Fecha/hora</th><th>Estado</th><th>Responsable</th></tr>
        </thead>
        <tbody>${filas || `<tr><td colspan="7" class="empty-state">No hay alertas para los filtros aplicados.</td></tr>`}</tbody>
      </table>
    </div>

    <div class="two-col">
      <div class="detail-box" id="detalle-alerta">
        <h3>Detalle de alerta seleccionada</h3>
        <p class="empty-state" style="padding:0;">Selecciona una alerta de la tabla para ver el detalle.</p>
      </div>
      <div class="detail-box">
        <h3>Acciones</h3>
        <div class="action-buttons">
          <button class="btn action" id="btn-cambiar-estado" disabled>Cambiar estado</button>
          <button class="btn action" id="btn-notificar" disabled>Notificar responsable</button>
          <button class="btn action" id="btn-crear-ticket" disabled>Crear ticket</button>
        </div>
      </div>
    </div>

    <dialog id="estado-dialog" style="border-radius:14px;border:2px solid #111;padding:22px;min-width:280px;">
      <h3 style="margin-top:0;">Cambiar estado de la alerta</h3>
      <div class="field">
        <select id="nuevo-estado">
          <option value="Pendiente">Pendiente</option>
          <option value="En proceso">En proceso</option>
          <option value="Cerrada">Cerrada</option>
        </select>
      </div>
      <div style="text-align:right;display:flex;gap:10px;justify-content:flex-end;">
        <button class="btn" id="cancelar-estado" type="button">Cancelar</button>
        <button class="btn primary" id="guardar-estado" type="button">Guardar</button>
      </div>
    </dialog>

    <dialog id="responsable-dialog" style="border-radius:14px;border:2px solid #111;padding:22px;min-width:280px;">
      <h3 style="margin-top:0;">Notificar responsable</h3>
      <div class="field">
        <select id="nuevo-responsable">
          <option value="TI">TI</option>
          <option value="Mantenimiento">Mantenimiento</option>
          <option value="Docencia">Docencia</option>
        </select>
      </div>
      <div style="text-align:right;display:flex;gap:10px;justify-content:flex-end;">
        <button class="btn" id="cancelar-responsable" type="button">Cancelar</button>
        <button class="btn primary" id="guardar-responsable" type="button">Guardar</button>
      </div>
    </dialog>
  `;

  document.getElementById('f-aula').value = ultimosFiltros.aula || '';
  document.getElementById('f-prioridad').value = ultimosFiltros.prioridad || '';
  document.getElementById('f-fecha').value = ultimosFiltros.fecha || '';
  document.getElementById('f-estado').value = ultimosFiltros.estado || '';

  document.getElementById('aplicar-filtros').addEventListener('click', () => {
    cargarAlertas(usuario, {
      aula: document.getElementById('f-aula').value.trim(),
      prioridad: document.getElementById('f-prioridad').value,
      fecha: document.getElementById('f-fecha').value,
      estado: document.getElementById('f-estado').value
    });
  });

  document.querySelectorAll('tbody tr[data-id]').forEach((tr) => {
    tr.addEventListener('click', () => {
      alertaSeleccionada = Number(tr.dataset.id);
      const alerta = alertas.find((a) => a.id === alertaSeleccionada);
      seleccionarAlerta(usuario, alerta);
    });
  });

  if (alertaSeleccionada) {
    const alerta = alertas.find((a) => a.id === alertaSeleccionada);
    if (alerta) seleccionarAlerta(usuario, alerta);
  }
}

function seleccionarAlerta(usuario, alerta) {
  document.getElementById('detalle-alerta').innerHTML = `
    <h3>Detalle de alerta seleccionada</h3>
    <dl>
      <dt>Aula</dt><dd>${alerta.aula_nombre}</dd>
      <dt>Descripción</dt><dd>${alerta.descripcion}</dd>
      <dt>Lectura asociada</dt><dd>${alerta.lectura_asociada}</dd>
      <dt>Estado</dt><dd>${badgeEstadoAlerta(alerta.estado)}</dd>
      <dt>Responsable</dt><dd>${alerta.responsable}</dd>
    </dl>
  `;

  const btnEstado = document.getElementById('btn-cambiar-estado');
  const btnNotificar = document.getElementById('btn-notificar');
  const btnTicket = document.getElementById('btn-crear-ticket');
  btnEstado.disabled = false;
  btnNotificar.disabled = false;
  btnTicket.disabled = false;

  btnEstado.onclick = () => {
    document.getElementById('nuevo-estado').value = alerta.estado;
    document.getElementById('estado-dialog').showModal();
  };
  document.getElementById('cancelar-estado').onclick = () => document.getElementById('estado-dialog').close();
  document.getElementById('guardar-estado').onclick = async () => {
    const estado = document.getElementById('nuevo-estado').value;
    await api(`/api/alertas/${alerta.id}/estado`, { method: 'PATCH', body: { estado } });
    document.getElementById('estado-dialog').close();
    showToast('Estado de la alerta actualizado.');
    await cargarAlertas(usuario, ultimosFiltros);
  };

  btnNotificar.onclick = () => {
    document.getElementById('nuevo-responsable').value = ['TI', 'Mantenimiento', 'Docencia'].includes(alerta.responsable) ? alerta.responsable : 'TI';
    document.getElementById('responsable-dialog').showModal();
  };
  document.getElementById('cancelar-responsable').onclick = () => document.getElementById('responsable-dialog').close();
  document.getElementById('guardar-responsable').onclick = async () => {
    const responsable = document.getElementById('nuevo-responsable').value;
    await api(`/api/alertas/${alerta.id}/responsable`, { method: 'PATCH', body: { responsable } });
    document.getElementById('responsable-dialog').close();
    showToast('Responsable notificado.');
    await cargarAlertas(usuario, ultimosFiltros);
  };

  btnTicket.onclick = async () => {
    const { ticket } = await api(`/api/alertas/${alerta.id}/ticket`, { method: 'POST' });
    showToast(`Ticket ${ticket.codigo} creado.`);
    await cargarAlertas(usuario, ultimosFiltros);
  };
}

(async () => {
  const usuario = await initPage({ title: 'Alertas', activeKey: 'alertas' });
  await cargarAlertas(usuario, leerFiltrosDeUrl());

  const socket = conectarSocket();
  socket.on('alertas:nuevas', () => {
    showToast('Nueva alerta generada por el sistema.');
    cargarAlertas(usuario, ultimosFiltros);
  });
  socket.on('alertas:resumen', () => {
    cargarAlertas(usuario, ultimosFiltros);
  });
})();

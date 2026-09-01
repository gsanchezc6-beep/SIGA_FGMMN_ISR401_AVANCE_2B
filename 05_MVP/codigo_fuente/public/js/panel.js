function badgeOcupacion(valor) {
  return valor === 'Ocupada'
    ? `<span class="badge green">Ocupada</span>`
    : `<span class="badge gray">Vacía</span>`;
}

function badgeProyector(valor) {
  if (valor === 'Encendido') return `<span class="badge green">Encendido</span>`;
  if (valor === 'Sin señal HDMI') return `<span class="badge yellow">Sin señal HDMI</span>`;
  return `<span class="badge red">Apagado</span>`;
}

function badgeConectividad(valor) {
  return valor === 'En línea'
    ? `<span class="badge green">En línea</span>`
    : `<span class="badge red">Alerta</span>`;
}

function necesitaAtencion(aula) {
  return aula.proyector === 'Sin señal HDMI' || aula.conectividad === 'Alerta' || aula.temperatura > 28;
}

function renderPanel(usuario, datos) {
  const { aulas, resumen } = datos;

  const filas = aulas.map((aula) => `
    <tr>
      <td>${aula.nombre}</td>
      <td>${badgeOcupacion(aula.ocupacion)}</td>
      <td>${aula.temperatura}°C</td>
      <td>${aula.humedad}%</td>
      <td>${badgeProyector(aula.proyector)}</td>
      <td>${aula.climatizacion}</td>
      <td>${badgeConectividad(aula.conectividad)}</td>
      <td>
        ${necesitaAtencion(aula)
          ? `<button class="btn action" data-atender="${aula.nombre}">Atender</button>`
          : `<button class="btn" data-detalle="${aula.id}">Ver detalle</button>`}
      </td>
    </tr>
  `).join('');

  document.getElementById('main-content').innerHTML = `
    <h2>Estado de aulas en tiempo real</h2>
    <div class="kpi-row">
      <div class="kpi-card"><div class="label">Aulas monitoreadas</div><div class="value">${resumen.aulasMonitoreadas}</div></div>
      <div class="kpi-card"><div class="label">Alertas activas</div><div class="value">${resumen.alertasActivas}</div></div>
      <div class="kpi-card"><div class="label">Equipos encendidos</div><div class="value">${resumen.equiposEncendidos}</div></div>
      <div class="kpi-card"><div class="label">Red IoT</div><div class="value">${resumen.redIot}</div></div>
    </div>
    <div class="panel-card">
      <div class="panel-title">Panel consolidado de aulas</div>
      <table>
        <thead>
          <tr>
            <th>Aula</th><th>Ocupación</th><th>Temperatura</th><th>Humedad</th>
            <th>Proyector</th><th>Climatización</th><th>Conectividad</th><th>Acción</th>
          </tr>
        </thead>
        <tbody>${filas || `<tr><td colspan="8" class="empty-state">Sin aulas registradas.</td></tr>`}</tbody>
      </table>
    </div>
    <dialog id="detalle-dialog" style="border-radius:14px;border:2px solid #111;padding:0;min-width:320px;">
      <div class="detail-box" id="detalle-contenido"></div>
      <div style="padding:0 22px 20px;text-align:right;">
        <button class="btn" id="cerrar-detalle">Cerrar</button>
      </div>
    </dialog>
  `;

  document.querySelectorAll('[data-detalle]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const aula = aulas.find((a) => String(a.id) === btn.dataset.detalle);
      mostrarDetalle(aula);
    });
  });

  document.querySelectorAll('[data-atender]').forEach((btn) => {
    btn.addEventListener('click', () => {
      window.location.href = `/alertas.html?aula=${encodeURIComponent(btn.dataset.atender)}`;
    });
  });
}

function mostrarDetalle(aula) {
  const dialog = document.getElementById('detalle-dialog');
  document.getElementById('detalle-contenido').innerHTML = `
    <h3>${aula.nombre}</h3>
    <dl>
      <dt>Ocupación</dt><dd>${aula.ocupacion}</dd>
      <dt>Temperatura</dt><dd>${aula.temperatura}°C</dd>
      <dt>Humedad</dt><dd>${aula.humedad}%</dd>
      <dt>Proyector</dt><dd>${aula.proyector}</dd>
      <dt>Climatización</dt><dd>${aula.climatizacion}</dd>
      <dt>Conectividad</dt><dd>${aula.conectividad}</dd>
      <dt>Última actualización</dt><dd>${formatFecha(aula.actualizado_en)}</dd>
    </dl>
  `;
  dialog.showModal();
  document.getElementById('cerrar-detalle').onclick = () => dialog.close();
}

(async () => {
  const usuario = await initPage({ title: 'Panel de control', activeKey: 'aulas' });
  const datos = await api('/api/aulas');
  renderPanel(usuario, datos);

  const socket = conectarSocket();
  socket.on('panel:actualizado', (payload) => {
    renderPanel(usuario, payload);
    showToast('Panel actualizado con nuevas lecturas.');
  });
})();

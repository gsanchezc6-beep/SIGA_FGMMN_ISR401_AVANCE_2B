let ultimoReporte = null;
let ultimosFiltrosReporte = {};

function renderReportes(usuario, datos) {
  const { kpis, grafico, tabla } = datos;
  ultimoReporte = datos;

  const maxUso = Math.max(1, ...grafico.map((g) => g.uso));
  const barras = grafico.map((g) => `
    <div class="bar-col">
      <div class="bar" style="height:${Math.max(6, (g.uso / maxUso) * 170)}px;">${g.uso}%</div>
      <div class="bar-label">${g.aula.replace('Aula-', '').replace('Lab-', '')}</div>
    </div>
  `).join('');

  const filasTabla = tabla.map((f) => `
    <tr>
      <td>${f.aula}</td>
      <td>${f.uso}%</td>
      <td>${f.consumo} kWh</td>
      <td>${f.fallas}</td>
      <td>${f.estado === 'Normal' ? '<span class="badge green">Normal</span>' : '<span class="badge yellow">Revisión</span>'}</td>
    </tr>
  `).join('');

  document.getElementById('main-content').innerHTML = `
    <h2>Generación de reportes</h2>
    <div class="filters-bar">
      <select id="r-aula">
        <option value="">Aula</option>
        ${['Aula-101', 'Aula-102', 'Lab-201', 'Aula-103', 'Aula-104'].map((a) => `<option value="${a}">${a}</option>`).join('')}
      </select>
      <input id="r-inicio" type="date" title="Fecha inicio" />
      <input id="r-fin" type="date" title="Fecha fin" />
      <select id="r-tipo">
        <option value="">Tipo de reporte</option>
        <option value="general">General</option>
        <option value="ocupacion">Ocupación</option>
        <option value="consumo">Consumo</option>
        <option value="mantenimiento">Mantenimiento</option>
      </select>
      <div class="spacer"></div>
      <button class="btn primary" id="generar-reporte">Generar</button>
    </div>

    <div class="kpi-row">
      <div class="kpi-card"><div class="label">Ocupación promedio</div><div class="value">${kpis.ocupacionPromedio} %</div></div>
      <div class="kpi-card"><div class="label">Consumo estimado</div><div class="value">${kpis.consumoEstimado} kWh</div></div>
      <div class="kpi-card"><div class="label">Incidencias registradas</div><div class="value">${kpis.incidenciasRegistradas}</div></div>
    </div>

    <div class="two-col">
      <div class="bar-chart">${barras || '<div class="empty-state">Sin datos para graficar.</div>'}</div>
      <div class="panel-card">
        <div class="panel-title">Seguimiento de tickets</div>
        <table>
          <thead><tr><th>Aula</th><th>Uso</th><th>Consumo</th><th>Fallas</th><th>Estado</th></tr></thead>
          <tbody>${filasTabla || `<tr><td colspan="5" class="empty-state">Sin datos.</td></tr>`}</tbody>
        </table>
      </div>
    </div>

    <div class="action-buttons" style="margin-top:18px;">
      <button class="btn" id="exportar-pdf">Exportar PDF</button>
      <button class="btn" id="exportar-excel">Exportar Excel</button>
    </div>
  `;

  document.getElementById('r-aula').value = ultimosFiltrosReporte.aula || '';
  document.getElementById('r-inicio').value = ultimosFiltrosReporte.fechaInicio || '';
  document.getElementById('r-fin').value = ultimosFiltrosReporte.fechaFin || '';
  document.getElementById('r-tipo').value = ultimosFiltrosReporte.tipo || '';

  document.getElementById('generar-reporte').addEventListener('click', () => {
    cargarReporte(usuario, {
      aula: document.getElementById('r-aula').value,
      fechaInicio: document.getElementById('r-inicio').value,
      fechaFin: document.getElementById('r-fin').value,
      tipo: document.getElementById('r-tipo').value
    });
  });

  document.getElementById('exportar-pdf').addEventListener('click', () => window.print());
  document.getElementById('exportar-excel').addEventListener('click', () => exportarExcel(tabla));
}

function exportarExcel(tabla) {
  const encabezado = 'Aula,Uso (%),Consumo (kWh),Fallas,Estado\n';
  const filas = tabla.map((f) => `${f.aula},${f.uso},${f.consumo},${f.fallas},${f.estado}`).join('\n');
  const blob = new Blob([encabezado + filas], { type: 'text/csv;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'siga-reporte.csv';
  a.click();
  URL.revokeObjectURL(url);
}

async function cargarReporte(usuario, filtros) {
  ultimosFiltrosReporte = filtros;
  const query = new URLSearchParams(Object.fromEntries(Object.entries(filtros).filter(([, v]) => v)));
  const datos = await api(`/api/reportes?${query.toString()}`);
  renderReportes(usuario, datos);
}

(async () => {
  const usuario = await initPage({ title: 'Reportes administrativos', activeKey: 'reportes', requiredRole: 'Administrador' });
  await cargarReporte(usuario, {});
})();

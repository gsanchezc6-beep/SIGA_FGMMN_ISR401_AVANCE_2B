(async () => {
  const usuario = await initPage({ title: 'Bitácora de acciones', activeKey: 'bitacora', requiredRole: 'Administrador' });
  const { registros } = await api('/api/bitacora');

  const filas = registros.map((r) => `
    <tr>
      <td>${formatFecha(r.fecha_hora)}</td>
      <td>${r.usuario_nombre}</td>
      <td>${r.rol === 'Administrador' ? 'Administrador' : 'Técnico de Infraestructura'}</td>
      <td>${r.accion}</td>
      <td>${r.detalle || '-'}</td>
    </tr>
  `).join('');

  document.getElementById('main-content').innerHTML = `
    <h2>Bitácora de acciones</h2>
    <div class="panel-card">
      <div class="panel-title">Registro de actividad del sistema</div>
      <table>
        <thead><tr><th>Fecha/hora</th><th>Usuario</th><th>Rol</th><th>Acción</th><th>Detalle</th></tr></thead>
        <tbody>${filas || `<tr><td colspan="5" class="empty-state">Sin registros de actividad.</td></tr>`}</tbody>
      </table>
    </div>
  `;
})();

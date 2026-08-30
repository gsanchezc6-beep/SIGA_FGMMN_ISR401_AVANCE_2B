const MENU_ITEMS = [
  { key: 'aulas', label: 'Aulas', href: '/panel.html' },
  { key: 'alertas', label: 'Alertas', href: '/alertas.html' },
  { key: 'mantenimiento', label: 'Mantenimiento', href: '/mantenimiento.html' },
  { key: 'reportes', label: 'Reportes', href: '/reportes.html', soloAdmin: true },
  { key: 'bitacora', label: 'Bitácora', href: '/bitacora.html', soloAdmin: true },
  { key: 'configuracion', label: 'Configuración', href: '/configuracion.html' }
];

async function requireSession() {
  const data = await api('/api/auth/me');
  if (!data.usuario) {
    window.location.href = '/login.html';
    throw new Error('sin sesión');
  }
  return data.usuario;
}

function renderShell({ title, activeKey, usuario }) {
  const esAdmin = usuario.rol === 'Administrador';
  const items = MENU_ITEMS.filter((item) => !item.soloAdmin || esAdmin);

  const nav = items.map((item) => `
    <a class="nav-link${item.key === activeKey ? ' active' : ''}" href="${item.href}">${item.label}</a>
  `).join('');

  const iniciales = usuario.nombre.split(' ').map((p) => p[0]).slice(0, 2).join('').toUpperCase();

  document.body.innerHTML = `
    <div class="app-shell">
      <header class="app-header">
        <h1>SIGA | ${title}</h1>
      </header>
      <div class="app-body">
        <nav class="sidebar">
          <h2>Menú principal</h2>
          ${nav}
          <div class="sidebar-footer">
            <div class="avatar">${iniciales}</div>
            <div class="who">
              <span>${usuario.nombre}</span>
              <span class="rol">${usuario.rol === 'Administrador' ? 'Administrador' : 'Técnico de Infraestructura'}</span>
            </div>
            <a class="logout-link" id="logout-link">Salir</a>
          </div>
        </nav>
        <main class="main" id="main-content"></main>
      </div>
    </div>
  `;

  document.getElementById('logout-link').addEventListener('click', async () => {
    await api('/api/auth/logout', { method: 'POST' });
    window.location.href = '/login.html';
  });
}

async function initPage({ title, activeKey, requiredRole }) {
  const usuario = await requireSession();
  if (requiredRole && usuario.rol !== requiredRole) {
    window.location.href = '/panel.html';
    throw new Error('sin permiso');
  }
  renderShell({ title, activeKey, usuario });
  return usuario;
}

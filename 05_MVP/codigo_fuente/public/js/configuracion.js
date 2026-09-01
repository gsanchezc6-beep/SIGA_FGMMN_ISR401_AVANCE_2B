function renderConfiguracion() {
  const actual = siga_obtenerPaleta();

  const swatches = SIGA_PALETTES.map((p) => `
    <button class="swatch-btn" data-id="${p.id}" type="button" title="${p.label}">
      <span class="swatch-circle${p.id === actual.id ? ' selected' : ''}" style="background:${p.accent};"></span>
      <span class="swatch-label">${p.label}</span>
    </button>
  `).join('');

  document.getElementById('main-content').innerHTML = `
    <h2>Configuración de interfaz</h2>
    <div class="detail-box">
      <h3>Paleta de color</h3>
      <p class="settings-intro">
        Elige el color de acento de la interfaz (menú activo, botones principales, avatar).
        Los colores de estado de las alertas y tickets (verde, rojo, amarillo) no cambian,
        para mantener su significado. El cambio se aplica al instante y se guarda en este
        navegador.
      </p>
      <div class="swatch-row" id="swatch-row">${swatches}</div>

      <div class="settings-preview">
        <span class="nav-link active" style="cursor:default;">Vista previa de menú activo</span>
        <button class="btn primary" type="button" style="cursor:default;">Botón principal</button>
      </div>
    </div>
  `;

  document.querySelectorAll('.swatch-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const id = btn.dataset.id;
      siga_guardarPaleta(id);
      const paleta = siga_aplicarPaleta(id);
      document.querySelectorAll('.swatch-circle').forEach((c) => c.classList.remove('selected'));
      btn.querySelector('.swatch-circle').classList.add('selected');
      showToast(`Paleta "${paleta.label}" aplicada.`);
    });
  });
}

(async () => {
  await initPage({ title: 'Configuración', activeKey: 'configuracion' });
  renderConfiguracion();
})();

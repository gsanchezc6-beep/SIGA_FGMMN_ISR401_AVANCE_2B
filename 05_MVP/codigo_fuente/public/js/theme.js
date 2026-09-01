// Paletas de acento (estilo selector de tema de Gmail/Calendar). Solo cambian
// el color de acento (menú activo, botones principales); no tocan los colores
// semánticos de estado (verde/rojo/amarillo de los badges).
const SIGA_PALETTES = [
  { id: 'azul', label: 'Azul', accent: '#1a73e8', accentLight: '#e8f0fe' },
  { id: 'verde', label: 'Verde', accent: '#188038', accentLight: '#e6f4ea' },
  { id: 'morado', label: 'Morado', accent: '#8430ce', accentLight: '#f3e8fd' },
  { id: 'rojo', label: 'Rojo', accent: '#c5221f', accentLight: '#fce8e6' },
  { id: 'naranja', label: 'Naranja', accent: '#e8710a', accentLight: '#fef0e6' },
  { id: 'gris', label: 'Gris pizarra', accent: '#3c4043', accentLight: '#eceef0' }
];

const SIGA_PALETA_KEY = 'siga-paleta';
const SIGA_PALETA_DEFAULT = 'azul';

function siga_obtenerPaleta() {
  const guardada = localStorage.getItem(SIGA_PALETA_KEY);
  return SIGA_PALETTES.find((p) => p.id === guardada) || SIGA_PALETTES.find((p) => p.id === SIGA_PALETA_DEFAULT);
}

function siga_aplicarPaleta(id) {
  const paleta = SIGA_PALETTES.find((p) => p.id === id) || SIGA_PALETTES[0];
  document.documentElement.style.setProperty('--accent', paleta.accent);
  document.documentElement.style.setProperty('--accent-light', paleta.accentLight);
  return paleta;
}

function siga_guardarPaleta(id) {
  localStorage.setItem(SIGA_PALETA_KEY, id);
}

// Se aplica de inmediato al cargar el <script>, antes de pintar el <body>,
// para evitar el parpadeo del color por defecto.
siga_aplicarPaleta(siga_obtenerPaleta().id);

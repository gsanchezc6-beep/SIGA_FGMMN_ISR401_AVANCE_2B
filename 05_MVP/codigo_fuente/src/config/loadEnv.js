// Cargador de .env minimalista para no depender del paquete dotenv.
const fs = require('node:fs');
const path = require('node:path');

const envPath = path.join(__dirname, '..', '..', '.env');
if (fs.existsSync(envPath)) {
  const contenido = fs.readFileSync(envPath, 'utf8');
  for (const linea of contenido.split(/\r?\n/)) {
    const limpia = linea.trim();
    if (!limpia || limpia.startsWith('#')) continue;
    const igual = limpia.indexOf('=');
    if (igual === -1) continue;
    const clave = limpia.slice(0, igual).trim();
    const valor = limpia.slice(igual + 1).trim();
    if (!(clave in process.env)) {
      process.env[clave] = valor;
    }
  }
}

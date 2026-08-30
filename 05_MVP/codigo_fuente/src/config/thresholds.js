module.exports = {
  UMBRAL_TEMPERATURA: Number(process.env.UMBRAL_TEMPERATURA) || 28,
  UMBRAL_HUMEDAD: Number(process.env.UMBRAL_HUMEDAD) || 65,
  SIMULATOR_INTERVAL_MS: Number(process.env.SIMULATOR_INTERVAL_MS) || 15000
};

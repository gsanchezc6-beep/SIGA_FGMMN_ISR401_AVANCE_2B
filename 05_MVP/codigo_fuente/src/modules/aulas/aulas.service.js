const { db } = require('../../db/database');

function listarConEstado() {
  return db.prepare(`
    SELECT aulas.id, aulas.nombre, aulas.tipo,
           aula_estado.ocupacion, aula_estado.temperatura, aula_estado.humedad,
           aula_estado.proyector, aula_estado.climatizacion, aula_estado.conectividad,
           aula_estado.actualizado_en
    FROM aulas
    JOIN aula_estado ON aula_estado.aula_id = aulas.id
    ORDER BY aulas.nombre
  `).all();
}

function obtenerConEstado(id) {
  return db.prepare(`
    SELECT aulas.id, aulas.nombre, aulas.tipo,
           aula_estado.ocupacion, aula_estado.temperatura, aula_estado.humedad,
           aula_estado.proyector, aula_estado.climatizacion, aula_estado.conectividad,
           aula_estado.actualizado_en
    FROM aulas
    JOIN aula_estado ON aula_estado.aula_id = aulas.id
    WHERE aulas.id = ?
  `).get(id);
}

function listarTodas() {
  return db.prepare('SELECT * FROM aulas ORDER BY nombre').all();
}

function resumenPanel() {
  const aulasMonitoreadas = db.prepare('SELECT COUNT(*) AS n FROM aulas').get().n;
  const alertasActivas = db.prepare("SELECT COUNT(*) AS n FROM alertas WHERE estado != 'Cerrada'").get().n;
  const equiposEncendidos = db.prepare(`
    SELECT COUNT(*) AS n FROM aula_estado
    WHERE proyector = 'Encendido' OR climatizacion = 'Activo'
  `).get().n;
  const redAlerta = db.prepare("SELECT COUNT(*) AS n FROM aula_estado WHERE conectividad = 'Alerta'").get().n;
  return {
    aulasMonitoreadas,
    alertasActivas,
    equiposEncendidos,
    redIot: redAlerta > 0 ? 'ALERTA' : 'OK'
  };
}

const upsertEstado = db.prepare(`
  INSERT INTO aula_estado (aula_id, ocupacion, temperatura, humedad, proyector, climatizacion, conectividad, actualizado_en)
  VALUES (@aulaId, @ocupacion, @temperatura, @humedad, @proyector, @climatizacion, @conectividad, @actualizadoEn)
  ON CONFLICT(aula_id) DO UPDATE SET
    ocupacion = excluded.ocupacion,
    temperatura = excluded.temperatura,
    humedad = excluded.humedad,
    proyector = excluded.proyector,
    climatizacion = excluded.climatizacion,
    conectividad = excluded.conectividad,
    actualizado_en = excluded.actualizado_en
`);

const insertLectura = db.prepare(`
  INSERT INTO lecturas (aula_id, ocupacion, temperatura, humedad, proyector, climatizacion, conectividad, creado_en)
  VALUES (@aulaId, @ocupacion, @temperatura, @humedad, @proyector, @climatizacion, @conectividad, @creadoEn)
`);

function guardarLectura(lectura) {
  const { aulaId, ocupacion, temperatura, humedad, proyector, climatizacion, conectividad, creadoEn, actualizadoEn } = lectura;
  upsertEstado.run({ aulaId, ocupacion, temperatura, humedad, proyector, climatizacion, conectividad, actualizadoEn });
  insertLectura.run({ aulaId, ocupacion, temperatura, humedad, proyector, climatizacion, conectividad, creadoEn });
}

module.exports = { listarConEstado, obtenerConEstado, listarTodas, resumenPanel, guardarLectura };

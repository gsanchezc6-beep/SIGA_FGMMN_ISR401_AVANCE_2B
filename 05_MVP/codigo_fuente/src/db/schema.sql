-- SIGA MVP - esquema SQLite

CREATE TABLE IF NOT EXISTS usuarios (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL,
  usuario TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  rol TEXT NOT NULL CHECK (rol IN ('Administrador', 'Tecnico'))
);

CREATE TABLE IF NOT EXISTS aulas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre TEXT NOT NULL UNIQUE,
  tipo TEXT NOT NULL DEFAULT 'Aula'
);

-- Estado "en vivo" de cada aula (lo que pinta el Panel de control).
-- Se sobreescribe en cada tick del simulador de sensores.
CREATE TABLE IF NOT EXISTS aula_estado (
  aula_id INTEGER PRIMARY KEY REFERENCES aulas(id),
  ocupacion TEXT NOT NULL CHECK (ocupacion IN ('Ocupada', 'Vacía')),
  temperatura REAL NOT NULL,
  humedad REAL NOT NULL,
  proyector TEXT NOT NULL CHECK (proyector IN ('Encendido', 'Apagado', 'Sin señal HDMI')),
  climatizacion TEXT NOT NULL CHECK (climatizacion IN ('Activo', 'Apagado')),
  conectividad TEXT NOT NULL CHECK (conectividad IN ('En línea', 'Alerta')),
  actualizado_en TEXT NOT NULL
);

-- Historial de lecturas simuladas, usado para Reportes.
CREATE TABLE IF NOT EXISTS lecturas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  aula_id INTEGER NOT NULL REFERENCES aulas(id),
  ocupacion TEXT NOT NULL,
  temperatura REAL NOT NULL,
  humedad REAL NOT NULL,
  proyector TEXT NOT NULL,
  climatizacion TEXT NOT NULL,
  conectividad TEXT NOT NULL,
  creado_en TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_lecturas_aula ON lecturas(aula_id, creado_en);

CREATE TABLE IF NOT EXISTS alertas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo TEXT NOT NULL UNIQUE,
  aula_id INTEGER NOT NULL REFERENCES aulas(id),
  tipo_anomalia TEXT NOT NULL,
  descripcion TEXT NOT NULL,
  lectura_asociada TEXT NOT NULL,
  prioridad TEXT NOT NULL CHECK (prioridad IN ('Alta', 'Media', 'Baja')),
  fecha_hora TEXT NOT NULL,
  estado TEXT NOT NULL CHECK (estado IN ('Pendiente', 'En proceso', 'Cerrada')) DEFAULT 'Pendiente',
  responsable TEXT NOT NULL DEFAULT 'Sin asignar'
);

CREATE TABLE IF NOT EXISTS tickets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  codigo TEXT NOT NULL UNIQUE,
  aula_id INTEGER NOT NULL REFERENCES aulas(id),
  equipo TEXT NOT NULL,
  tipo_incidencia TEXT NOT NULL,
  prioridad TEXT NOT NULL CHECK (prioridad IN ('Alta', 'Media', 'Baja')),
  descripcion TEXT NOT NULL,
  estado TEXT NOT NULL CHECK (estado IN ('Abierto', 'En proceso', 'Cerrado')) DEFAULT 'Abierto',
  alerta_id INTEGER REFERENCES alertas(id),
  creado_por TEXT NOT NULL,
  creado_en TEXT NOT NULL,
  actualizado_en TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ticket_historial (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER NOT NULL REFERENCES tickets(id),
  fecha TEXT NOT NULL,
  accion TEXT NOT NULL,
  usuario TEXT NOT NULL,
  observacion TEXT NOT NULL DEFAULT '',
  estado_anterior TEXT,
  estado_nuevo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bitacora (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  usuario_id INTEGER,
  usuario_nombre TEXT NOT NULL,
  rol TEXT NOT NULL,
  accion TEXT NOT NULL,
  detalle TEXT NOT NULL DEFAULT '',
  fecha_hora TEXT NOT NULL
);

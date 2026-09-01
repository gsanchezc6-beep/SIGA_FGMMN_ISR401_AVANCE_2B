require('./config/loadEnv');

const path = require('node:path');
const express = require('express');
const session = require('express-session');
const http = require('node:http');
const { Server } = require('socket.io');

const { seedIfEmpty } = require('./db/seed');
const authRoutes = require('./modules/auth/auth.routes');
const aulasRoutes = require('./modules/aulas/aulas.routes');
const crearAlertasRouter = require('./modules/alertas/alertas.routes');
const crearMantenimientoRouter = require('./modules/mantenimiento/mantenimiento.routes');
const reportesRoutes = require('./modules/reportes/reportes.routes');
const bitacoraRoutes = require('./modules/bitacora/bitacora.routes');
const sensorSimulator = require('./simulator/sensorSimulator');

seedIfEmpty();

const app = express();
const server = http.createServer(app);
const io = new Server(server);

const PORT = process.env.PORT || 3000;
const sessionMiddleware = session({
  secret: process.env.SESSION_SECRET || 'siga-mvp-secret',
  resave: false,
  saveUninitialized: false,
  cookie: { maxAge: 1000 * 60 * 60 * 8 }
});

app.use(express.json());
app.use(sessionMiddleware);
app.use(express.static(path.join(__dirname, '..', 'public')));

app.use('/api/auth', authRoutes);
app.use('/api/aulas', aulasRoutes);
app.use('/api/alertas', crearAlertasRouter(io));
app.use('/api/tickets', crearMantenimientoRouter(io));
app.use('/api/reportes', reportesRoutes);
app.use('/api/bitacora', bitacoraRoutes);

io.engine.use(sessionMiddleware);

io.on('connection', (socket) => {
  const usuario = socket.request.session && socket.request.session.usuario;
  if (!usuario) {
    socket.disconnect(true);
  }
});

sensorSimulator.start(io);

server.listen(PORT, () => {
  console.log(`SIGA MVP escuchando en http://localhost:${PORT}`);
});

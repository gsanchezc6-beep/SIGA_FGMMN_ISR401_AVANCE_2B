# SIGA — Sistema Inteligente de Gestión de Aulas (MVP)

MVP académico de Ingeniería de Requerimientos. Simula un sistema de gestión de aulas
universitarias con sensores IoT: no hay hardware real, las lecturas de temperatura,
humedad, ocupación y estado de equipos las genera el propio backend cada cierto
intervalo.

## Stack

- **Backend:** Node.js + Express + Socket.io.
- **Base de datos:** SQLite, mediante el módulo nativo `node:sqlite` de Node.js —
  **no requiere ningún paquete nativo ni compilación** (nada de `better-sqlite3`,
  Python o Visual Studio Build Tools). Un solo archivo `data/siga.db`.
- **Frontend:** HTML/CSS/JS plano, sin build step ni framework. Multipágina, una
  vista por módulo, actualizada en vivo vía Socket.io.
- **Sesiones:** `express-session` (cookie de sesión, en memoria — suficiente para
  una demo local).

Esta combinación se eligió para que el proyecto corra en cualquier laptop del
equipo con un solo comando, sin dependencias nativas que puedan fallar al instalar.

## Requisitos

- Node.js **22.5 o superior** (probado en Node 25). El proyecto usa el módulo
  `node:sqlite`; en versiones de Node anteriores a la 23.4 este módulo requiere el
  flag `--experimental-sqlite`, por lo que los scripts de `npm` ya lo incluyen —
  no necesitas hacer nada adicional.

## Despliegue local

```bash
npm install
npm start
```

Abre `http://localhost:3000`. Al iniciar por primera vez, el servidor crea
`data/siga.db` y lo puebla automáticamente con datos de ejemplo (usuarios, aulas,
alertas y tickets semilla) — no hace falta ningún paso manual de seed.

Si por algún motivo quieres re-sembrar la base de datos manualmente:

```bash
npm run seed
```

(Solo agrega datos si la base está vacía; no duplica registros.)

## Cuentas de demo

| Usuario   | Contraseña  | Rol                          |
|-----------|-------------|-------------------------------|
| `admin`   | `admin123`  | Administrador                 |
| `tecnico` | `tecnico123`| Técnico de Infraestructura    |

El **Administrador** ve los 6 módulos (Aulas, Alertas, Mantenimiento, Reportes,
Bitácora, Configuración). El **Técnico de Infraestructura** ve Aulas, Alertas,
Mantenimiento y Configuración (sin Reportes ni Bitácora), conforme a RF-19.

## Simulador de sensores

`src/simulator/sensorSimulator.js` corre en el mismo proceso del servidor y cada
`SIMULATOR_INTERVAL_MS` (por defecto 15 segundos, configurable en `.env`) genera
una nueva lectura para cada aula: ocupación, temperatura, humedad, estado del
proyector, climatización y conectividad. Cada lectura:

1. Se guarda como el estado "en vivo" del aula (lo que ve el Panel de control) y
   se agrega al historial (`lecturas`), usado por Reportes.
2. Se emite por Socket.io (`panel:actualizado`) para refrescar el Panel sin
   recargar la página.
3. Se evalúa contra los umbrales configurados. Si excede alguno, se crea una
   alerta automáticamente (evitando duplicar alertas abiertas del mismo tipo
   para la misma aula) y se emite `alertas:nuevas`.

Umbrales por defecto (ajustables en `.env`, ver `.env.example`):

- Temperatura > 28 °C → alerta "Temperatura elevada" (Alta).
- Humedad > 65 % → alerta "Humedad elevada" (Media).
- Proyector en estado "Sin señal HDMI" → alerta (Alta).
- Climatización "Activo" con aula "Vacía" → el sistema la **apaga
  automáticamente** (ahorro energético, RF-13/RF-16) y deja un registro ya
  Cerrado ("Apagado automático por aula desocupada", Media) con responsable
  "Sistema", más una entrada en Bitácora.
- Conectividad en estado "Alerta" → alerta "Aula sin conectividad estable"
  (Media).

Durante una demo de ~3 minutos, con el intervalo por defecto (15 s), es normal
ver aparecer 1-3 alertas nuevas sin ninguna interacción manual.

## Cobertura de Requisitos Funcionales (RF) "Must"

El proyecto define **17 RF "Must"**. Este MVP cubre **11 de 17 (64.7%)**,
verificado contra el código real (no contra lo documentado). La tabla incluye
el archivo/función exacto que implementa cada uno, para que sea auditable:

| RF | Descripción | Evidencia en código |
|----|---|---|
| RF-01 | Recopilación de datos ambientales (sensores IoT simulados) | [`sensorSimulator.js`](src/simulator/sensorSimulator.js) `siguienteLectura()` — genera temperatura/humedad/ocupación cada tick |
| RF-03 | Detección automática de ocupación de aula | Mismo `siguienteLectura()`, campo `ocupacion` recalculado sin intervención humana |
| RF-07 | Panel de control centralizado | [`aulas.routes.js`](src/modules/aulas/aulas.routes.js) + `panel.js` — vista consolidada de todas las aulas con KPIs |
| RF-08 | Generación y envío de alertas por anomalías | `sensorSimulator.js` `evaluarUmbrales()` + [`alertas.service.js`](src/modules/alertas/alertas.service.js) `crearSiNoExiste()`; envío = push inmediato por Socket.io (`alertas:nuevas`) |
| RF-10 | Registro histórico de fallas y mantenimientos | Tabla `alertas` (nunca se borra, filtrable por fecha/estado/aula) + tabla `ticket_historial` en [`mantenimiento.service.js`](src/modules/mantenimiento/mantenimiento.service.js) |
| RF-12 | Gestión de solicitudes de mantenimiento | `mantenimiento.service.js` — crear, listar, cambiar estado, historial |
| RF-13 | Control automático de apagado energético | `sensorSimulator.js` `evaluarUmbrales()` — apaga climatización automáticamente cuando detecta la condición, antes de persistir la lectura |
| RF-16 | Apagado automático por aula desocupada | Misma regla que RF-13, caso específico: `ocupacion === 'Vacía' && climatizacion === 'Activo'` |
| RF-19 | Gestión de acceso diferenciado por roles | [`middleware/auth.js`](src/middleware/auth.js) `requireRole()` — verificado con 403 real en la API, menús distintos por rol |
| RF-22 | Monitoreo de conectividad de red IoT | `aulas.service.js` `resumenPanel()` (KPI "Red IoT") + alerta "Aula sin conectividad estable" |
| RF-23 | Registro de bitácora de acciones de usuario | [`bitacora.service.js`](src/modules/bitacora/bitacora.service.js) `registrarAccion()` — login/logout, cambios de estado, apagados automáticos del sistema |

**RF Must no cubiertos o solo parcialmente cubiertos por este MVP** (no cuentan
en el 64.7%; se documentan para que quede claro qué falta, no para inflar el
número):

| RF | Estado | Qué falta |
|----|---|---|
| RF-04 | Parcial | Se monitorea el proyector (estado, alerta de señal HDMI), pero no existe control remoto (encender/apagar) |
| RF-05 | Parcial | Se monitorea la climatización, pero no hay ajuste remoto manual (solo el apagado automático de RF-13/16) |
| RF-11 | Parcial | Las alertas se entregan en tiempo real vía Socket.io, pero no hay diferenciación especial para "críticas" — mismo evento y mismo aviso que cualquier alerta |
| RF-21 | Parcial | La regla de "equipo encendido fuera de horario" solo existe para climatización; no hay una equivalente para proyector |
| RF-02 | No cubierto | No existe ningún control remoto simulado de dispositivos |
| RF-15 | No cubierto | No existe ningún concepto de horario/programación en el modelo de datos ni en el código |

RF-17 (Reportes con estadísticas agregadas) **sí está implementado**, pero es
prioridad "Should" en el proyecto, no "Must" — se documenta aparte y no cuenta
para el 64.7% de cobertura Must.

## Personalización de interfaz (Configuración)

Además de los 6 módulos de RF, el menú incluye un ítem **Configuración**
(visible para ambos roles) con un selector de paleta de color de acento, al
estilo del selector de tema de Gmail/Calendar. Es una mejora de experiencia de
usuario, no un RF del proyecto:

- Cambia únicamente el color de acento (menú activo, botones principales,
  avatar). Los colores semánticos de estado (verde/rojo/amarillo de badges de
  alertas y tickets) **no cambian**, para no alterar su significado.
- La preferencia se guarda por navegador (`localStorage`), no requiere backend
  ni base de datos.
- Lógica en `public/js/theme.js`; interfaz en `public/configuracion.html` /
  `public/js/configuracion.js`.

## Estructura del proyecto

```
SIGA/
├── src/
│   ├── server.js              # entry point: express + socket.io + arranque del simulador
│   ├── config/                 # umbrales, carga de .env
│   ├── db/                     # schema.sql, conexión node:sqlite, seed
│   ├── middleware/              # requireAuth / requireRole
│   ├── modules/
│   │   ├── auth/                # RF-19
│   │   ├── aulas/                # RF-01, RF-03, RF-07, RF-22
│   │   ├── alertas/               # RF-08, RF-13, RF-16, RF-22
│   │   ├── mantenimiento/          # RF-12, RF-10
│   │   ├── reportes/               # RF-17 (Should, no cuenta para el 64.7%)
│   │   └── bitacora/                # RF-23
│   └── simulator/                # RF-01, RF-03 (genera lecturas) + RF-08/RF-13/RF-16/RF-22 (evalúa umbrales y ejecuta el apagado automático)
├── public/                     # frontend estático (HTML/CSS/JS, sin build step)
├── data/                       # siga.db (se crea al iniciar, no versionado)
└── package.json
```

## Notas para la demo

- La primera carga ya trae datos de ejemplo: 5 aulas, 2 alertas y 4 tickets, para
  que ninguna pantalla se vea vacía.
- El Panel de control y las Alertas se actualizan solos vía Socket.io; no hace
  falta recargar el navegador durante la demo.
- Para provocar una alerta a demanda sin esperar al simulador, basta con bajar
  temporalmente `UMBRAL_TEMPERATURA` en `.env` (por ejemplo a `20`) antes de
  arrancar, o esperar un ciclo del simulador (15 s por defecto).

## Licencia

Apache License 2.0 — ver [LICENSE](LICENSE).

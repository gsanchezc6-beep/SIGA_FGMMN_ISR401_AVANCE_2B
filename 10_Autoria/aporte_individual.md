# Declaracion de aporte individual

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Elemento **A10** de la evidencia de autoria. Declara que hizo cada integrante, sobre que
artefactos y con que confirmaciones del historial se acredita.

Este documento **no se escribe a mano**: se genera con `04_Trazabilidad/generar_aporte_individual.py`
desde el propio historial. El detalle confirmacion por confirmacion esta en [`../04_Trazabilidad/aporte_individual.csv`](../04_Trazabilidad/aporte_individual.csv).

---

## Resumen

| Integrante | Correo institucional | Commits | Primera | Ultima |
|---|---|---|---|---|
| Gary Alberto Sanchez Cornejo | gsanchezc6@uteq.edu.ec | **81** | 2026-08-30 | 2026-09-04 |
| Yeranick Esther Munoz Quinonez | ymunozq@uteq.edu.ec | **69** | 2026-08-30 | 2026-09-04 |
| Winston Damian Cedeno Avila | wcedenoa2@uteq.edu.ec | **4** | 2026-09-04 | 2026-09-04 |

Comprobable con `git shortlog -sne main`. El total de esta tabla es una confirmacion
menor que el historial completo, porque la declaracion no puede incluir el commit que la deposita.

---

## Gary Alberto Sanchez Cornejo

**Rol:** Analista lider; especificacion, componente empirico e integracion

**Confirmaciones: 81**, de 2026-08-30 a 2026-09-04.

### Areas sobre las que trabajo

| Area | Archivos tocados |
|---|---|
| Modelado UML e i* | 132 |
| Manuscrito y deposito | 66 |
| Documentos de raiz | 63 |
| Componente empirico | 63 |
| Paquete de datos | 55 |
| Producto minimo viable | 53 |
| Especificacion de requisitos | 40 |
| Evidencia de campo y etica | 26 |
| Evidencia de autoria | 24 |
| Defensa | 21 |
| Trazabilidad | 17 |
| Otros | 8 |

### Confirmaciones

| Commit | Fecha | Aporte |
|---|---|---|
| `a939f6d` | 2026-08-30 | docs: agrega los archivos raiz obligatorios y la licencia dual |
| `4f85748` | 2026-08-30 | docs: agrega el reporte del estudio con su estructura y bibliografia |
| `d713c55` | 2026-08-30 | docs: agrega la ERS/SRS v2.0 compilada con sus figuras |
| `f3fa45d` | 2026-08-30 | feat: agrega la auditoria de calidad de la especificacion con sus conteos base |
| `36cd4f3` | 2026-08-30 | feat: agrega la ficha del componente de IA y su clasificacion de riesgo |
| `aada199` | 2026-08-30 | feat: agrega el diagrama de contexto y el modelado organizacional iStar |
| `59a779c` | 2026-08-30 | feat: agrega el diagrama general de casos de uso y el de clases refinado |
| `c1b4201` | 2026-08-30 | feat: agrega los diagramas de secuencia de los casos de uso obligatorios |
| `60868be` | 2026-08-30 | feat: agrega los diagramas de actividad de los flujos principales |
| `d938f4c` | 2026-08-30 | feat: agrega las maquinas de estado y los diagramas de componentes y despliegue |
| `2c5e510` | 2026-08-30 | feat: agrega los prototipos de interfaz de las pantallas obligatorias |
| `eac1c93` | 2026-08-30 | feat: agrega la matriz de trazabilidad y la priorizacion MoSCoW y Kano |
| `6928f8a` | 2026-08-30 | docs: agrega el protocolo experimental y su registro previo con desviaciones |
| `c986ab8` | 2026-08-30 | feat: agrega los instrumentos de evaluacion ciega y las consignas del modelo |
| `7e63cab` | 2026-08-30 | feat: agrega el pipeline de analisis reproducible con una sola orden |
| `42b53db` | 2026-08-30 | feat: agrega las salidas estadisticas del componente empirico |
| `bc8426a` | 2026-08-30 | data: agrega los datos crudos y procesados del paquete de replicacion |
| `698366a` | 2026-08-30 | data: agrega el diccionario de datos y la correspondencia de salidas del reporte |
| `bb4b3fd` | 2026-08-30 | feat: agrega el codigo fuente del prototipo organizado por modulos |
| `ffe701b` | 2026-08-30 | docs: agrega el despliegue del prototipo y su cobertura de requisitos |
| `33732bb` | 2026-08-30 | feat: agrega el video de demostracion del recorrido funcional |
| `6803847` | 2026-08-30 | docs: agrega el guion de la defensa individual y el banco de preguntas |
| `8e0334e` | 2026-08-30 | docs: declara el aporte individual con los identificadores de commit que lo respaldan |
| `4ecc5b1` | 2026-08-30 | docs: completa la declaracion de aporte y regenera el manifiesto de integridad |
| `bb53c76` | 2026-08-30 | fix: evita que el manifiesto de sumas se normalice a CRLF en Windows |
| `d7962ac` | 2026-08-30 | fix: impide que los archivos del manifiesto se normalicen al clonar |
| `baa8fce` | 2026-08-30 | docs: redacta el cuerpo completo del reporte del estudio |
| `b9cc55d` | 2026-08-30 | fix: el script de potencia emitia un alfa literal que rompia la compilacion |
| `bd6f017` | 2026-08-30 | docs(ers): identifica la especificacion como Entrega Final 2B en su version 4.0 |
| `e2ff989` | 2026-08-30 | build(ers): recompila la especificacion consolidada |
| `9132cb1` | 2026-08-30 | docs(reporte): referencia en el texto cada figura y cada tabla del estudio |
| `982df1b` | 2026-08-30 | build(reporte): recompila el reporte con las referencias cruzadas resueltas |
| `8c03f2b` | 2026-08-30 | docs(ers): declara version, fecha y commit base en la caratula |
| `3edde5a` | 2026-08-30 | docs(reporte): sincroniza la tabla de metricas con la auditoria y explica los cambios |
| `282133d` | 2026-08-30 | build: recompila ambos documentos y regenera el manifiesto de sumas |
| `05c2a39` | 2026-08-31 | docs(ers): corrige el commit base declarado en la caratula |
| `1375eb2` | 2026-08-31 | docs(ers): incorpora los requisitos del componente de IA a la especificacion |
| `f86f54d` | 2026-08-31 | docs(ers): anade el resumen bilingue que exige el criterio C1 |
| `2174d54` | 2026-08-31 | build(ers): recompila la especificacion y regenera el manifiesto |
| `e383c23` | 2026-08-31 | docs(ers): eleva la especificacion a la version 4.1 |
| `065b9c5` | 2026-08-31 | build(ers): recompila la version 4.1 y regenera el manifiesto |
| `28ab805` | 2026-08-31 | fix(ers): etiqueta los criterios de aceptacion y anade las historias que faltaban |
| `cf362f9` | 2026-08-31 | docs(ers): eleva la especificacion a la version 4.2 |
| `db6c5fe` | 2026-08-31 | build(ers): recompila la version 4.2 |
| `0bc376d` | 2026-08-31 | docs(ers): aplica las decisiones del comite CCB-01 y declara las dependencias |
| `ae7f654` | 2026-08-31 | build(ers): recompila la especificacion en su version 4.3 |
| `d4e5c8d` | 2026-08-31 | docs(etica): declara la reduccion de la muestra a diez entrevistas |
| `e1489e2` | 2026-09-01 | feat(publicacion): incorpora el manuscrito final y su paquete de deposito |
| `cfbda80` | 2026-09-01 | feat(experimento): anade el analisis de sensibilidad por item y reubica el pipeline |
| `bcc3149` | 2026-09-01 | feat(mvp): anade el despliegue del prototipo en contenedor |
| `a2ce2c6` | 2026-09-01 | docs(defensa): corrige los materiales a la modalidad individual |
| `4bd0a30` | 2026-09-01 | build(ers): deja la caratula con los dos integrantes reales y recompila |
| `ea7c616` | 2026-09-01 | docs(readme): declara los identificadores persistentes y el arbol vigente |
| `ae2cd78` | 2026-09-01 | fix(ers): deja la tabla de roles del anexo A.1 con los dos integrantes |
| `268837f` | 2026-09-01 | fix(reporte): corrige el umbral de trazabilidad y declara el cierre de cadenas |
| `dd91d88` | 2026-09-01 | docs(protocolo): anade notas de actualizacion sin reescribir lo registrado |
| `91ad3ca` | 2026-09-01 | fix(publicacion): apunta al registro OSF y al deposito Zenodo vigentes |
| `2048ebc` | 2026-09-01 | feat(evidencias): deposita la sesion de member checking MC-01 |
| `7b058eb` | 2026-09-01 | feat(etica): deposita el acta de constancia N=10 y el comprobante del correo |
| `9d3fc7c` | 2026-09-01 | fix(defensa): corrige la presentacion y actualiza el banco de preguntas |
| `d86291d` | 2026-09-01 | fix(modelado): reconstruye el diagrama i* SR |
| `94f0c19` | 2026-09-01 | feat(defensa): deposita la exposicion grabada y declara que no es la defensa |
| `0e69071` | 2026-09-01 | docs(trazabilidad): pone al dia la declaracion de aporte |
| `b1a2b94` | 2026-09-02 | docs(entrega): atiende las observaciones del informe de la 2B |
| `042732e` | 2026-09-03 | feat(datos): restituye 07_Datos como paquete de datos verificable |
| `69b3008` | 2026-09-03 | docs(equipo): declara la composicion de tres y el origen del historial |
| `e7c7b7e` | 2026-09-03 | feat(autoria): crea 10_Autoria con la evidencia que no depende de terceros |
| `2f9ef3d` | 2026-09-03 | feat(ers): especifica el componente inteligente como requisitos verificables |
| `930b580` | 2026-09-03 | feat(trazabilidad): define los casos de prueba que la matriz citaba sin respaldo |
| `4ae79d4` | 2026-09-03 | docs(autoria): pone al dia el aporte individual y deposita el elemento A10 |
| `6fc1216` | 2026-09-03 | feat(autoria): ejecuta la lista de verificacion previa de la seccion 11 |
| `fdb1c2c` | 2026-09-03 | feat(etica): registra el alcance del consentimiento de cada participante |
| `4dd22aa` | 2026-09-03 | fix(etica): corrige la asignacion de la ronda terminal a seis docentes |
| `81cc69e` | 2026-09-03 | docs(autoria): incorpora los ORCID y precisa quien rindio la defensa |
| `adfc44f` | 2026-09-04 | fix(publicacion): las tablas del manuscrito caben y estan en ingles |
| `898c973` | 2026-09-04 | fix(experimento): orden determinista de la curva e incorporacion del corpus |
| `5a47632` | 2026-09-04 | docs: el corpus son dieciseis entrevistas, y la documentacion lo dice |
| `bc8f312` | 2026-09-04 | feat(autoria): A6 y A11 completos, y el perfil tecnico declarado |
| `d6c1615` | 2026-09-04 | fix(evidencias): la causa del perfil tecnico es de calendario, no de plantilla |
| `e630d8c` | 2026-09-04 | fix(evidencias): el cargo de TIC-01 se toma del consentimiento firmado |
| `d1a02a1` | 2026-09-04 | feat(evidencias): sesion de validacion WT-08 con usuario tecnico |

---

## Yeranick Esther Munoz Quinonez

**Rol:** Documentacion, trazabilidad, auditoria de calidad y gestion de evidencias

**Confirmaciones: 69**, de 2026-08-30 a 2026-09-04.

### Areas sobre las que trabajo

| Area | Archivos tocados |
|---|---|
| Evidencia de campo y etica | 189 |
| Evidencia de autoria | 54 |
| Producto minimo viable | 43 |
| Documentos de raiz | 42 |
| Otros | 25 |
| Componente empirico | 19 |
| Trazabilidad | 14 |
| Manuscrito y deposito | 11 |
| Especificacion de requisitos | 10 |
| Modelado UML e i* | 7 |
| Paquete de datos | 1 |

### Confirmaciones

| Commit | Fecha | Aporte |
|---|---|---|
| `1499dd9` | 2026-08-30 | data: agrega las transcripciones anonimizadas de las diez entrevistas |
| `ef5cf3d` | 2026-08-30 | data: agrega los diez registros de audio de entrevista en MP3 a 128 kbps |
| `4d88a4d` | 2026-08-30 | data: agrega los videos de entrevista de la primera ronda de campo |
| `e99b1ab` | 2026-08-30 | data: agrega los videos de entrevista de la segunda ronda de campo |
| `0a2ccd3` | 2026-08-30 | data: agrega los diez consentimientos informados enmascarados |
| `507c475` | 2026-08-30 | data: agrega la ficha tecnica de la evidencia audiovisual con sus hashes |
| `0f1b8af` | 2026-08-30 | data: agrega el cuestionario aplicado con sus sesenta respuestas |
| `ab0a112` | 2026-08-30 | data: agrega las fotografias del entorno operativo del cliente |
| `4cf6593` | 2026-08-30 | data: agrega los documentos originales de la organizacion cliente |
| `cdf3346` | 2026-08-30 | data: agrega la codificacion tematica de las transcripciones |
| `cd15418` | 2026-08-30 | feat: agrega el guion de validacion para participante no tecnico |
| `6379b69` | 2026-08-30 | data: agrega las actas de las sesiones de validacion enmascaradas |
| `e440b67` | 2026-08-30 | docs: agrega el paquete de anexos eticos del proyecto |
| `e35c9fe` | 2026-08-30 | docs: agrega los anexos de categoria B y la declaracion de uso de IA |
| `6603e61` | 2026-08-30 | fix(ers): unifica los identificadores en RNF- y delimita RF-13 frente a RF-16 |
| `2d9c602` | 2026-08-30 | feat(replicacion): anade replicar.py, el pipeline en una orden sin GNU Make |
| `0fe13ae` | 2026-08-30 | docs(citacion): declara el identificador persistente del deposito en CITATION.cff |
| `7dae4d5` | 2026-08-30 | docs(readme): retira del arbol las carpetas sin contenido y declara su ausencia |
| `82b102d` | 2026-08-30 | chore(integridad): regenera el manifiesto de sumas sobre las 248 entradas |
| `4ffb70a` | 2026-08-30 | docs(changelog): registra la consolidacion 2B-1.1.0 |
| `5851996` | 2026-08-30 | fix(ers): hace comprobable el criterio de aceptacion de RF-14 |
| `d87bc43` | 2026-08-30 | docs(auditoria): recalcula completitud, verificabilidad y consistencia |
| `06ce54e` | 2026-08-31 | fix(experimento): traslada y renombra la tabla de desciego de items |
| `e6cea7e` | 2026-08-31 | docs(experimento): documenta la desviacion de la clave de desciego |
| `b33e130` | 2026-08-31 | docs(readme): declara la tabla de desciego en su nueva ubicacion |
| `012ba1e` | 2026-08-31 | chore(integridad): regenera el manifiesto tras el traslado de la clave |
| `a663650` | 2026-08-31 | docs(changelog): registra las correcciones 2B-1.2.0 |
| `5800f35` | 2026-08-31 | docs(experimento): deposita el comprobante del registro previo en PDF |
| `afc0930` | 2026-08-31 | data(experimento): deposita la evidencia verificable del registro previo |
| `2ef0e9b` | 2026-08-31 | docs(experimento): corrige el estado del registro previo |
| `d214866` | 2026-08-31 | chore(integridad): extiende el manifiesto de sumas a los archivos zip |
| `dc1978b` | 2026-08-31 | docs(changelog): registra la version 2B-1.3.0 |
| `b4faffe` | 2026-08-31 | chore(integridad): extiende el manifiesto de sumas a los archivos xml |
| `1e68dda` | 2026-08-31 | fix(trazabilidad): corrige los enlaces rotos de la matriz y completa su cadena |
| `5804479` | 2026-08-31 | docs(trazabilidad): lista los huerfanos y las cadenas rotas con causa y accion |
| `dd1d07e` | 2026-08-31 | docs(auditoria): recalcula la trazabilidad tras completar la matriz |
| `49fc9ad` | 2026-08-31 | docs(aporte): rehace la declaracion de aporte sobre el historial real |
| `b32ef2d` | 2026-08-31 | docs(experimento): cierra las dos comprobaciones sobre el repositorio 2A |
| `ab6977d` | 2026-08-31 | chore(integridad): regenera el manifiesto tras completar la trazabilidad |
| `dd4abe4` | 2026-08-31 | docs(changelog): registra la version 2B-1.4.0 |
| `d42ba84` | 2026-09-01 | feat(evidencias): deposita once fotografias de entorno con su inventario |
| `5a60692` | 2026-09-01 | refactor(evidencias): pasa las transcripciones a Markdown estructurado |
| `5ca4257` | 2026-09-01 | refactor(evidencias): reubica etica, validacion y codificacion tematica |
| `c1b217d` | 2026-09-01 | docs(trazabilidad): declara la composicion real del equipo y rehace el aporte |
| `1518546` | 2026-09-01 | docs(auditoria): publica el par de valores antes y despues de las seis metricas |
| `96999d9` | 2026-09-01 | chore(integridad): cierra el deposito FAIR y regenera el manifiesto |
| `572513f` | 2026-09-01 | docs(changelog): registra las versiones 2B-1.5.0 y 2B-1.6.0 |
| `27e8adf` | 2026-09-01 | docs(trazabilidad): actualiza la declaracion de aporte al historial completo |
| `3e3de2b` | 2026-09-01 | feat(modelado): deposita los diagramas de flujo de datos de nivel 0 y 1 |
| `9619d02` | 2026-09-01 | docs(evidencias): documenta las carpetas declaradas y su estado real |
| `f4e63e0` | 2026-09-01 | docs(readme): corrige la fila de los DFD, que ya estan depositados |
| `023f745` | 2026-09-01 | fix(integridad): entrega los archivos de texto sin normalizar el fin de linea |
| `c76db09` | 2026-09-01 | chore(integridad): regenera el manifiesto sobre el arbol completo |
| `bbe5c87` | 2026-09-01 | fix(integridad): extiende la regla de no normalizar a todo el arbol |
| `84921aa` | 2026-09-01 | docs(trazabilidad): actualiza la declaracion de aporte al historial vigente |
| `998ab45` | 2026-09-03 | feat(evidencias): sustituye las fotografias de entorno sin metadato verificable |
| `88bb1fd` | 2026-09-03 | feat(evidencias): deposita los seis consentimientos de la ronda terminal |
| `076b392` | 2026-09-03 | feat(autoria): deposita la correspondencia de coordinacion, elemento A8 |
| `f889afc` | 2026-09-04 | feat(autoria): deposita las dos grabaciones de sesion, elemento A4 |
| `328499a` | 2026-09-04 | feat(autoria): deposita las notas de campo y la primera tanda de capturas |
| `f3fa233` | 2026-09-04 | feat(autoria): manifiesto por script, acuerdo de A7 y declaracion al dia |
| `14436bc` | 2026-09-04 | docs(trazabilidad): el recuento por autor deja de declarar cero para el tercero |
| `b92bc5d` | 2026-09-04 | docs(evidencias): declara las doce grabaciones de la ronda terminal |
| `be0dc83` | 2026-09-04 | fix(autoria): el instructivo de A2 pedia usuarios de Git que no existen |
| `4010c12` | 2026-09-04 | feat(autoria): A7 completo, con las dos codificaciones y su acuerdo |
| `c4c695a` | 2026-09-04 | feat(autoria): A2 completo, tres capturas por cada integrante |
| `17ceb08` | 2026-09-04 | feat(evidencias): dos documentos mas de la organizacion; se pasa de cuatro a seis |
| `c13ac7f` | 2026-09-04 | feat(evidencias): las dos actas que faltaban, firmadas; ocho sesiones en total |
| `2fded58` | 2026-09-04 | docs(autoria): la lista de verificacion previa, reejecutada sobre clon limpio |

---

## Winston Damian Cedeno Avila

**Rol:** Transcripcion y anonimizacion del corpus de entrevistas

**Confirmaciones: 4**, de 2026-09-04 a 2026-09-04.

### Areas sobre las que trabajo

| Area | Archivos tocados |
|---|---|
| Evidencia de campo y etica | 15 |
| Evidencia de autoria | 4 |
| Documentos de raiz | 3 |

### Confirmaciones

| Commit | Fecha | Aporte |
|---|---|---|
| `ea08aba` | 2026-09-04 | feat(evidencias): transcribe y anonimiza EV-20 y EV-21 con control de calidad |
| `d79c879` | 2026-09-04 | feat(evidencias): completa las seis transcripciones de la ronda terminal |
| `d0a3138` | 2026-09-04 | feat(evidencias): validacion e incorporacion de la codificacion tematica |
| `cf79792` | 2026-09-04 | feat(autoria): cuatro capturas mas de A2; dos integrantes llegan al minimo |

---

## Firmas

Cada integrante firma declarando que el aporte que consta arriba a su nombre es suyo,
y que no reclama trabajo de otra persona.


**Gary Alberto Sanchez Cornejo**

Firma: ______________________________    Fecha: ______________


**Yeranick Esther Munoz Quinonez**

Firma: ______________________________    Fecha: ______________


**Winston Damian Cedeno Avila**

Firma: ______________________________    Fecha: ______________

---

Generado el 2026-09-04 desde el historial del repositorio.

# Registro de cambios — SIGA (Sistema Inteligente de Gestion de Aulas)

Formato basado en Keep a Changelog. Versionado segun las entregas del Proyecto Fin de
Curso ISR-401, Universidad Tecnica Estatal de Quevedo, periodo 2026–2027.

Cada version registra lo anadido, lo cambiado y lo corregido. Solo se listan artefactos
que existen en el arbol del repositorio en el commit correspondiente.

---

## [2B-1.6.0] - 2026-09-01

Analisis de sensibilidad, despliegue en contenedor y cierre de la verificacion documental.

### Anadido

- `06_Experimento/scripts_analisis/analisis_por_item.py` - analisis de sensibilidad que toma
  el requisito como unidad en lugar del juez. La potencia para un efecto mediano sube de
  **0,084 a 0,417**, y los tamanos de efecto pasan a tener intervalos interpretables. Las dos
  aproximaciones coinciden: ninguna dimension resulta significativa tras Holm-Bonferroni.
- `06_Experimento/registro_previo/desviacion_analisis_por_item.md` - la desviacion declarada,
  con lo que decia el plan preregistrado, que problema aparecio y que se hizo.
- `07_Publicacion/verificacion_referencias.md` - registro de la verificacion de las 40
  referencias: 35 con DOI que resuelve al trabajo citado y 5 sin DOI por no tener uno
  asignado, cada una con su motivo.
- `05_MVP/docker-compose.yml` - despliegue del prototipo con una sola orden.
- `02_Evidencias/Fotos_Entorno/` - once fotografias nuevas (ENT-16 a ENT-26) con su
  inventario, entre ellas la camara Dahua identificable y un aula vacia con las luminarias
  encendidas a plena luz de dia.
- `02_Evidencias/Codificacion_Tematica/` - la curva de saturacion y la tabla por entrevista,
  que la guia situa en esta carpeta.
- `08_Defensa/README.md` - declara que la defensa fue individual y que no existe grabacion.

### Cambiado

- Las diez transcripciones pasan de texto plano a **Markdown estructurado**, con la cabecera
  como tabla y cada intervencion marcada. El contenido se conserva literal.
- `protocolo.pdf`, `osf_registration.pdf` y `osf_deviations.pdf` se ven ya al nivel de
  `06_Experimento/`, como fija el arbol de la seccion 9.1.
- `08_Defensa/guion.md` y `guion_reparto_exposicion.md` - reescritos para defensa individual.
- El manuscrito incorpora la subseccion del analisis de sensibilidad y pasa a 13 paginas.

### Corregido

- Cuatro referencias cruzadas del manuscrito apuntaban a etiquetas inexistentes
  (`tab:desc` y `tab:power`) e imprimian interrogantes en el PDF.
- La respuesta G2 del banco de preguntas afirmaba que el historial estaba concentrado en una
  persona; el recuento real es 47 y 40.

---

## [2B-1.5.0] - 2026-09-01

Cierre del deposito FAIR, incorporacion del manuscrito y reorganizacion del arbol segun
la seccion 9.1 de la guia.

### Anadido

- `07_Publicacion/manuscrito_final.tex` y su PDF - manuscrito en plantilla Springer LNCS
  (`llncs.cls`), 12 paginas, compilado sin errores y sin citas sin resolver.
- `07_Publicacion/referencias.bib` - 40 entradas, 35 con DOI verificado uno a uno
  resolviendo al trabajo citado. Las cinco restantes son una norma ISO, el SWEBOK, un
  libro, una ley y un informe tecnico: ninguno tiene DOI asignado.
- `07_Publicacion/analisis_revistas.md` - eleccion de REFSQ 2027, track Research, como
  objetivo primario, coherente con la plantilla empleada.
- `07_Publicacion/dataset_zenodo/` - paquete efectivamente depositado en Zenodo.
- `06_Experimento/osf_deviations.pdf` - desviaciones declaradas respecto del protocolo.
- `fair_assessment.pdf` - autoevaluacion FAIR con F-UJI: 21 de 26 indicadores, 80,8 %.
- `04_Trazabilidad/composicion_equipo.md` - integrantes del equipo con el recuento por
  autor del historial que lo respalda.
- `08_Defensa/folleto_una_hoja.pdf` y `presentacion.pdf`.

### Cambiado

- **Reorganizacion del arbol.** `07_Datos/` se disuelve: los datos crudos, los procesados
  y los scripts pasan a `06_Experimento/`, y las figuras y tablas a `07_Publicacion/`.
  `09_Defensa/` pasa a `08_Defensa/`, `08_Etica/` a `02_Evidencias/Etica/` y
  `02_Evidencias/Validacion/` a `02_Evidencias/Validacion_Walkthrough/`. Los traslados se
  hicieron con `git mv`, de modo que el historial sigue a cada archivo.
- `06_Experimento/replicar.py` y `Makefile` - rutas actualizadas. El pipeline se ejecuto
  completo despues del traslado y regenera todas las tablas y figuras.
- `CITATION.cff` - el DOI principal pasa a ser el del deposito de datos en Zenodo; se
  anaden el registro OSF y el identificador de Software Heritage como identificadores
  relacionados.
- `README.md` - nueva seccion con los identificadores persistentes y la cita recomendada;
  arbol actualizado.
- Equipo declarado en la caratula del ERS, el README, el reporte, el manuscrito y
  `CITATION.cff`: dos integrantes, que son los dos autores del historial.
- `04_Trazabilidad/aporte_individual.csv` - regenerado desde `git log`: 87 filas, una por
  commit, todas con identificador que resuelve.
- `checksums.sha256` - regenerado sobre el arbol reorganizado: 290 entradas, comprobadas
  sin error.

### Corregido

- El manuscrito ya no contiene marcadores de plantilla: se sustituyeron el correo de
  contacto, el DOI de Zenodo y el identificador de Software Heritage por sus valores
  reales.
- `07_Publicacion/tablas/tabla_power_calculation.tex` - un caracter griego sin escapar
  impedia la compilacion.
- Se retiro `04_Trazabilidad/acreditacion_aporte.md`, que acreditaba a personas ajenas al
  equipo actual.

---

## [2B-1.4.0] - 2026-08-31

Cierre de la trazabilidad y acreditacion del aporte individual.

### Anadido

- `04_Trazabilidad/huerfanos_y_cadenas_rotas.md` - huerfanos y cadenas rotas listados con
  causa y accion, como exige la guia.
- `04_Trazabilidad/acreditacion_aporte.md` - responde a las dos observaciones del docente
  sobre el historial: el trabajo anterior al 30 de agosto y el aporte de los integrantes
  sin commits en este repositorio.
- `01_ERS/` - historias HU-18, HU-19 y HU-20 para RF-20, RF-24 y RF-25, con sus criterios
  CA-18, CA-19 y CA-20. Los diecisiete escenarios Gherkin existentes quedan etiquetados
  como CA-01 a CA-17.
- `04_Trazabilidad/matriz_trazabilidad.csv` - columnas de clase, proceso, caso de prueba y
  estado de la traza.

### Corregido

- Ocho identificadores de historia de la matriz no resolvian contra el ERS, y ningun
  criterio de aceptacion resolvia porque el ERS no los etiquetaba. Corregido en ambos
  extremos.
- La declaracion de aporte individual subestimaba el trabajo de tres integrantes. Rehecha
  sobre el historial real de los dos repositorios: 183 commits, uno por fila.
- Tres filas de la matriz arrastraban una coma de mas.

### Medido

- Trazabilidad, cadena adelante completa: de **48,0 % a 92,0 %**, por encima del 90 % de
  referencia.
- Celdas vacias en la matriz: de **308 a 0**.
- `checksums.sha256`: 254 entradas, con los archivos xml ya cubiertos.

---

## [2B-1.3.0] - 2026-08-31

Comprobante del registro previo y ampliacion del manifiesto de integridad.

### Anadido

- `06_Experimento/registro_previo/osf_registration.pdf` - exportacion de 15 paginas de la
  pagina publica del registro, con DOI, fecha de registro, contribuyentes y formulario.
- `06_Experimento/registro_previo/osf_internet_archive.pdf` - ficha del item archivado por
  el Center for Open Science, con su fecha propia.
- `06_Experimento/registro_previo/osf_registration_api.json`,
  `osf_contributors_api.json`, `osf_internet_archive_bag.zip` y
  `osf_internet_archive_meta.xml` - la misma evidencia en formato verificable con dos
  ordenes `curl`, sin credenciales.

### Cambiado

- `06_Experimento/registro_previo/registro_osf.md` - se corrige el estado: el registro ya
  constaba como retrospectivo en la propia OSF desde el 2026-08-27. G9 sigue incumplido,
  pero la declaracion esta hecha en la fuente y con fecha.
- `checksums.sha256` - de 248 a 253 entradas; el manifiesto cubre ahora los archivos zip.
- `.gitattributes` - `*.zip binary`, para que el hash del paquete archivado cuadre sobre
  un clon limpio.

---

## [2B-1.2.0] — 2026-08-31

Correcciones derivadas de la revision docente de la Entrega Final.

### Anadido

- `06_Experimento/registro_previo/desviacion_clave_desciego.md` — desviacion del
  protocolo documentada: que es la tabla de desciego, por que debe ser publica para que el
  paquete de replicacion funcione, y que amenaza a la validez queda declarada y pendiente
  de verificar.
- `01_ERS/` — subseccion 3.3.2, requisitos del componente de inteligencia artificial:
  rendimiento, equidad con su regla de no despliegue, explicabilidad, datos de
  entrenamiento con sus sesgos declarados, plan de monitoreo y clasificacion de riesgo.
- `01_ERS/` — resumen bilingue, Resumen y Abstract con sus palabras clave.

### Cambiado

- La tabla de desciego pasa de `07_Datos/datos_crudos/CLAVE_RESPUESTAS_no_compartir_con_jueces.csv`
  a `06_Experimento/clave_desciego_items.csv`. Es artefacto de diseno experimental, no dato
  crudo de campo, y su nombre anterior afirmaba una restriccion que el repositorio no
  cumplia. El contenido es identico y las diez salidas del pipeline no cambian.
- `07_Datos/scripts/analizar_resultados.py` — ruta por defecto de la tabla de desciego.
- `checksums.sha256` — regenerado.

---

## [2B-1.1.0] — 2026-08-30

Consolidacion de la especificacion y cierre de las declaraciones del repositorio.

### Anadido

- `06_Experimento/replicar.py` — el pipeline completo en una sola orden, sin depender de
  GNU Make. Ejecuta las nueve etapas con los mismos parametros y la misma semilla que el
  Makefile, y produce las mismas tablas y figuras byte a byte. Incluye `--verificar`,
  que sondea el codec y la duracion del material audiovisual y comprueba el manifiesto
  de sumas sin necesidad de `sha256sum`.
- `06_Experimento/resultados/entorno_python.txt` — version de Python y de cada
  dependencia con la que se produjeron los resultados publicados.
- `CITATION.cff` — identificador persistente del deposito: DOI `10.17605/OSF.IO/7PQ3H`,
  con su bloque `identifiers`.
- `README.md` — apartado «Elementos aun no depositados», que declara de forma explicita
  los cinco elementos que el repositorio todavia no contiene y en que estado esta cada
  uno.
- `reporte.tex` — etiquetas de las tres tablas de anexo que no las tenian:
  `tab:metricas`, `tab:retrospectiva` y `tab:correspondencia`.

### Cambiado

- `01_ERS/` — la especificacion pasa a version 4.0 y se identifica como Entrega Final
  (2B) en la caratula, en el repositorio declarado y en el historial de versiones. Las
  referencias a la Entrega 3 (2A) que describen hechos pasados se conservan intactas:
  son historia del documento, no una identidad equivocada.
- `01_ERS/secciones_generadas.tex` — las conclusiones dejan de anunciar como pendiente
  lo que esta entrega ya cierra, y declaran lo que sigue abierto: los umbrales de RNF-07,
  RNF-09, RNF-10, RNF-12, RNF-13 y RNF-15 sin verificacion de campo, y la cadena de
  trazabilidad hacia clase, proceso y caso de prueba.
- `reporte.tex` — cada figura y cada tabla se referencia ahora desde el cuerpo del texto.
  Antes ninguna de las cinco tablas generadas por el pipeline se citaba en la prosa.
- `README.md` — la orden unica de reproduccion se documenta por las dos vias, con GNU
  Make declarado como opcional.
- `checksums.sha256` — regenerado sobre las 248 entradas del manifiesto. Comprueba sin
  error.

### Corregido

- **Identificadores de requisito no funcional duplicados.** El prefijo aparecia como
  `NFR-` en las tablas del ERS y como `RNF-` en la prosa y en la matriz de trazabilidad,
  lo que rompia la resolucion automatica de identificadores. Se unifica en `RNF-`, que
  es el que ya usaban la matriz y la columna de tipo. 49 sustituciones en siete
  archivos.
- **Solapamiento funcional entre RF-13 y RF-16**, unico conflicto abierto que arrojaba
  la auditoria de consistencia. Ambos se disparaban ante la misma condicion y con el
  mismo umbral. Se delimitan por causa conforme a la solicitud de cambio SC-01: RF-13
  actua por consumo sostenido sin actividad, con independencia del horario; RF-16 actua
  al concluir la ultima franja asignada, con independencia del consumo. Se anade regla
  de precedencia y registro en bitacora de que regla ordeno el apagado. Se alinean las
  historias HU-11 y HU-13 y sus escenarios.
- **Carpetas declaradas y vacias.** El arbol del README describia cinco carpetas sin
  contenido en el repositorio. Se retiran del arbol y su ausencia se declara en el
  apartado nuevo, de modo que el repositorio no nombra nada que no exista.
- `README.md` — la descripcion de `04_Trazabilidad/` prometia tablas de huerfanos y un
  tablero que la carpeta no contiene; se ajusta a lo que hay.

---

## [2B-1.0.0] — 2026-08-29

Reconstruccion del repositorio de la Entrega Final sobre la estructura de la seccion 9
de la guia vigente.

### Anadido

- Arbol de carpetas de la seccion 9: `01_ERS/`, `02_Evidencias/` con sus subcarpetas de
  consentimientos, video, audio, transcripciones, guiones, cuestionario, fotografias del
  entorno, documentos de la organizacion, notas de campo, codificacion tematica y
  validacion; `03_Modelado/`, `04_Trazabilidad/`, `05_MVP/`, `06_Experimento/` y
  `07_Datos/`.
- `04_Trazabilidad/aporte_individual.csv` — una fila por aporte, cada una con el
  identificador del commit que la respalda y el repositorio donde se puede verificar.
- `07_Datos/diccionario_datos.csv` — significado, tipo y rango de cada variable de los
  datos crudos, procesados y de resultados.
- `07_Datos/correspondencia_salidas.csv` — cada tabla y cada figura del reporte
  emparejada con el script que la produce y la etapa del Makefile que la invoca.
- `08_Etica/declaracion_uso_ia.md` — declaracion por seccion, con herramienta, tipo de
  asistencia y metodo de validacion aplicado.
- `reporte.tex` — documento entregado, con las secciones y el orden que fija la
  seccion 10 de la guia.
- Tres registros de audio de entrevista recuperados del historial del repositorio de la
  Entrega 2A: DOC-02, COORD-03 y DOC-04.

### Cambiado

- Nomenclatura de archivos normalizada a ASCII sin acentos ni espacios, con guion bajo
  como separador. Afecta a las quince fotografias del entorno, a los cuatro prototipos
  de interfaz, al diagrama de contexto, al libro de respuestas del cuestionario y al
  horario academico.
- Los diez consentimientos y las cinco actas de sesion de validacion pasan a la
  convencion `AAAA-MM-DD_TipoParticipante_Codigo_Tecnica.ext`.
- El paquete de replicacion se traslada a `07_Datos/`, que es la carpeta que nombra la
  seccion 9. Los datos crudos, los datos procesados y los scripts quedan bajo esa raiz.
- Los diagramas UML se reorganizan por tipo de modelo, cada uno con su archivo fuente
  nativo junto a las exportaciones.

### Corregido

- Se retiran las referencias a artefactos de la guia anterior que no forman parte de
  esta entrega: autoevaluacion FAIR, identificador de Software Heritage y deposito
  externo con identificador persistente.
- Se eliminan los marcadores de plantilla y las instrucciones dirigidas al equipo de
  los archivos raiz. Ningun campo queda escrito como pendiente: los valores que no se
  pueden afirmar se omiten.
- Se elimina de la documentacion toda mencion a archivos que no existen en el arbol.

---

## [2A-1.0.0] — 2026-08-02 (Entrega 3, repositorio `SIGA_FGMMN_ISR401_AVANCE_2A`)

Version de la que procede la evidencia de campo migrada: transcripciones, consentimientos,
fotografias, documentos de la organizacion, modelado UML e i*, prototipos de interfaz y
registros de audio.

---

## [1B] y [1A] — 2026

Entregas iniciales del Proyecto Fin de Curso: elicitacion preliminar, primera version de
la especificacion y modelado de contexto.

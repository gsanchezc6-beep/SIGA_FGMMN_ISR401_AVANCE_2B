# Registro de cambios — SIGA (Sistema Inteligente de Gestion de Aulas)

Formato basado en Keep a Changelog. Versionado segun las entregas del Proyecto Fin de
Curso ISR-401, Universidad Tecnica Estatal de Quevedo, periodo 2026–2027.

Cada version registra lo anadido, lo cambiado y lo corregido. Solo se listan artefactos
que existen en el arbol del repositorio en el commit correspondiente.

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

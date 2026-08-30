# Declaracion de uso de inteligencia artificial

Proyecto SIGA — Entrega Final (2B) — ISR-401 — Equipo FGMMN
Ultima actualizacion: 2026-08-29

Esta declaracion cubre, seccion por seccion, la herramienta empleada, el tipo de
asistencia recibida y el metodo concreto con el que el equipo valido el contenido
resultante. Cubre las secciones que existen a la fecha de esta actualizacion; se
extiende conforme se incorporan las restantes.

---

## 1. Los modelos de lenguaje como objeto de estudio

El Conjunto A de Requisitos Funcionales del componente empirico fue **generado por un
modelo grande de lenguaje**, deliberadamente y como variable independiente del
cuasi-experimento. No es asistencia de redaccion: es el material que el estudio compara.

La consigna literal, el modelo, sus parametros y el material fuente estan en
[`06_Experimento/consignas/`](../06_Experimento/consignas/). Las limitaciones
metodologicas de esa generacion —incluida la exposicion previa parcial del modelo al
Conjunto B en la misma sesion de chat— se declaran en
`06_Experimento/consignas/prompt_llm_conjunto_A.md` y se recogen como amenaza a la
validez de constructo en el reporte.

---

## 2. Asistencia recibida en la elaboracion del entregable

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Estructura del repositorio | Claude (Anthropic) | Reorganizacion del arbol de carpetas contra la seccion 9 de la guia y normalizacion de nombres de archivo a ASCII sin espacios | El equipo recorrio el arbol resultante carpeta por carpeta contra el texto de la seccion 9 y verifico que cada archivo migrado abre y conserva su contenido |
| `README.md` | Claude (Anthropic) | Redaccion a partir de datos que el equipo proporciono: integrantes, roles, dependencias y secuencia de compilacion | Cada ruta citada se comprobo contra el arbol real; la secuencia de compilacion se ejecuto sobre un clon limpio |
| `CHANGELOG.md`, `CITATION.cff`, `LICENSE` | Claude (Anthropic) | Redaccion de los archivos raiz obligatorios | El equipo verifico que ningun campo quedara escrito como pendiente y que los alcances de licencia correspondan a las rutas reales |
| `04_Trazabilidad/aporte_individual.csv` | Claude (Anthropic) | Extraccion de los identificadores de commit desde el historial de Git de ambos repositorios | Cada identificador se resolvio con `git show` contra el repositorio que la fila declara |
| `07_Datos/diccionario_datos.csv` | Claude (Anthropic) | Redaccion de las definiciones a partir de las cabeceras reales de cada archivo de datos | El equipo contrasto cada fila con la cabecera del archivo que describe |
| `07_Datos/correspondencia_salidas.csv` | Claude (Anthropic) | Emparejamiento de cada salida con el script que la produce, leido del Makefile | Se ejecuto `make all` y se comprobo que cada salida listada aparece regenerada |
| Auditoria del repositorio contra la rubrica | Claude (Anthropic) | Contraste sistematico del arbol y del historial contra los criterios de piso y las evidencias exigibles | El equipo verifico a mano cada hallazgo antes de actuar sobre el: conteos de archivos, ausencia de etiquetas y presencia de marcadores de plantilla |

---

## 3. Limites que el equipo se impuso

Las secciones evaluativas del reporte —analisis, discusion, conclusiones, justificacion
de las decisiones de ingenieria y amenazas a la validez— son **produccion propia del
equipo**, escritas contra la evidencia primaria del proyecto y sostenibles ante el
tribunal por cualquiera de sus integrantes.

Ninguna cifra, tabla, figura, resultado estadistico ni referencia bibliografica de este
trabajo procede de un modelo de lenguaje. Las cifras se generan por script desde los
datos crudos, con la correspondencia declarada en
[`07_Datos/correspondencia_salidas.csv`](../07_Datos/correspondencia_salidas.csv). Las
referencias de `referencias.bib` se verificaron individualmente y cada identificador
digital se resolvio antes de citarlo.

Los resultados no se redactaron antes de existir: la secuencia fue registrar el
protocolo, ejecutar el estudio, analizar con los scripts versionados y solo entonces
redactar.

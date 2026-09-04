# Declaracion de uso de inteligencia artificial

Proyecto SIGA — Entrega Final (2B) — ISR-401 — Equipo FGMMN
Ultima actualizacion: 2026-09-04

Elemento **A9** de la evidencia de autoria. Cubre, seccion por seccion, la herramienta
empleada, el tipo de asistencia recibida y el metodo concreto con el que el equipo valido
el contenido resultante.

**Cubre todas las secciones del entregable, incluidas aquellas en las que no se empleo
ninguna herramienta**, que se enumeran en el apartado 4. Declarar solo donde hubo
asistencia dejaria al lector sin saber si el silencio significa ausencia de uso o ausencia
de declaracion.

---

## 1. Los modelos de lenguaje como objeto de estudio

El Conjunto A de Requisitos Funcionales del componente empirico fue **generado por un
modelo grande de lenguaje**, deliberadamente y como variable independiente del
cuasi-experimento. No es asistencia de redaccion: es el material que el estudio compara.

La consigna literal, el modelo, sus parametros y el material fuente estan en
[`06_Experimento/prompts_llm/`](../06_Experimento/prompts_llm/). Las limitaciones
metodologicas de esa generacion —incluida la exposicion previa parcial del modelo al
Conjunto B en la misma sesion de chat— se declaran en
`06_Experimento/prompts_llm/prompt_llm_conjunto_A.md` y se recogen como amenaza a la
validez de constructo en el reporte.

---

## 2. Asistencia recibida en la elaboracion del entregable

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Estructura del repositorio | Claude (Anthropic) | Reorganizacion del arbol de carpetas contra la seccion 9 de la guia y normalizacion de nombres de archivo a ASCII sin espacios | El equipo recorrio el arbol resultante carpeta por carpeta contra el texto de la seccion 9 y verifico que cada archivo migrado abre y conserva su contenido |
| `README.md` | Claude (Anthropic) | Redaccion a partir de datos que el equipo proporciono: integrantes, roles, dependencias y secuencia de compilacion | Cada ruta citada se comprobo contra el arbol real; la secuencia de compilacion se ejecuto sobre un clon limpio |
| `CHANGELOG.md`, `CITATION.cff`, `LICENSE` | Claude (Anthropic) | Redaccion de los archivos raiz obligatorios | El equipo verifico que ningun campo quedara escrito como pendiente y que los alcances de licencia correspondan a las rutas reales |
| `04_Trazabilidad/aporte_individual.csv` | Claude (Anthropic) | Extraccion de los identificadores de commit desde el historial de Git de ambos repositorios | Cada identificador se resolvio con `git show` contra el repositorio que la fila declara |
| `07_Publicacion/dataset_zenodo/diccionario_datos.csv` | Claude (Anthropic) | Redaccion de las definiciones a partir de las cabeceras reales de cada archivo de datos | El equipo contrasto cada fila con la cabecera del archivo que describe |
| `07_Publicacion/dataset_zenodo/correspondencia_salidas.csv` | Claude (Anthropic) | Emparejamiento de cada salida con el script que la produce, leido del Makefile | Se ejecuto `make all` y se comprobo que cada salida listada aparece regenerada |
| Auditoria del repositorio contra la rubrica | Claude (Anthropic) | Contraste sistematico del arbol y del historial contra los criterios de piso y las evidencias exigibles | El equipo verifico a mano cada hallazgo antes de actuar sobre el: conteos de archivos, ausencia de etiquetas y presencia de marcadores de plantilla |

---

### Trabajo del 1 y 2 de septiembre de 2026

Posterior a la primera version de esta declaracion, y anadido aqui para que la
declaracion cubra el entregable completo y no solo su estado a finales de agosto.

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Modelado UML e i* --- 41 diagramas | Claude (Anthropic) | Reconstruccion de los diagramas en PlantUML a partir de los modelos existentes, leidos de los `.vpp` y los `.drawio` originales | El equipo comprobo por script que los 41 diagramas conservan los elementos y relaciones del modelo original, y a ojo cada figura renderizada. La numeracion de mensajes de las 16 secuencias se verifico sin repeticiones |
| `03_Modelado/09_DFD/` | Claude (Anthropic) | Alineacion de los DFD de nivel 0 y 1 con el diagrama de contexto: traduccion al idioma del modelo y correspondencia de entidades y flujos | Los dibujo el equipo en draw.io. Se comprobo por script que se cumplen las tres reglas de la notacion: ningun flujo sin nombre, ninguno entre dos entidades externas y ninguno entre dos almacenes |
| Amenazas a la validez del manuscrito | Claude (Anthropic) | Redaccion de las ocho amenazas, dos por categoria, con su mitigacion y la limitacion remanente, a partir de los resultados y las desviaciones ya declaradas | Cada cifra citada se contrasto contra la tabla o figura que la produce; el manuscrito compila sin referencias sin resolver |
| `02_Evidencias/Member_Checking/` | Claude (Anthropic) | Redaccion del acta de la sesion, del guion y del consentimiento; censura de los datos identificables de los consentimientos firmados | La sesion la condujo el equipo. El acta consigna lo que ocurrio, incluida su duracion real tomada de la cabecera del video. La censura se verifico pagina por pagina sobre el archivo depositado |
| `02_Evidencias/Etica/acta_constancia_N10.pdf` | Claude (Anthropic) | Composicion del documento y censura de las cedulas de los testigos | Las firmas las recogio el equipo. El documento declara de forma expresa que no es una autorizacion escrita del docente |
| Integridad del repositorio | Claude (Anthropic) | Deteccion de que el manifiesto de sumas verificaba en la maquina local pero habria fallado sobre un clon limpio, y correccion de la normalizacion de fin de linea | Se clono el repositorio desde el remoto y se ejecuto la comprobacion completa: 440 de 440 sumas correctas |
| Recodificacion de video | Claude (Anthropic) | Ajuste de los videos de la sesion de verificacion y de la exposicion al formato declarado del repositorio | Se comprobo que la duracion del archivo depositado coincide con la del original y que decodifica de principio a fin sin errores |

---

### Trabajo del 3 de septiembre de 2026

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| `07_Datos/` --- paquete de datos | Claude (Anthropic) | Redaccion de los tres scripts de etapa y del orquestador, del diccionario de datos, de la licencia de datos y de la documentacion del paquete | Se clono el repositorio en limpio, se borro todo lo generado y se ejecuto la orden unica: las salidas regeneradas resultan identicas byte a byte a las depositadas. Los veinte coeficientes de acuerdo reproducen los que ya calculaba scikit-learn |
| `07_Datos/resultados/acuerdo_interevaluador_ic.csv` | Claude (Anthropic) | Implementacion del kappa de Cohen ponderado y de Fleiss con su intervalo por bootstrap, en biblioteca estandar | Contraste obligado contra los valores ya publicados. La primera version usaba kappa sin ponderar y **no coincidia**; el contraste lo detecto y se corrigio al estimador ponderado que declara el protocolo |
| `04_Trazabilidad/composicion_equipo.md` | Claude (Anthropic) | Redaccion de la declaracion de composicion tras el alta de un integrante y la baja de otro | Los recuentos por autor se comprobaron con `git shortlog -sne main` contra el propio historial. El integrante recien incorporado figura con cero commits porque esa es su situacion real |
| `CHANGELOG.md` --- version 2B-1.7.0 | Claude (Anthropic) | Redaccion de la entrada, incluida la documentacion de la migracion de repositorio | El motivo y la fecha los aporto el equipo; las fechas del historial se leyeron del repositorio |
| `10_Autoria/bitacora_sesiones.csv` | Claude (Anthropic) | Script que deriva la bitacora del historial de versiones | Ningun campo se escribe a mano: se regenera con `python 10_Autoria/generar_bitacora.py` y se comprueba que exista al menos una fila por cada dia con commits |
| `.mailmap` | Claude (Anthropic) | Unificacion de identidades historicas de Git | Comprobado con `git shortlog -sne main`: dos autores, ninguna identidad duplicada, ningun autor ajeno al equipo |
| Recompilacion del ERS en A4 | Claude (Anthropic) | Cambio de geometria y recompilacion | Verificado sobre el registro de compilacion: cero desbordes horizontales, cero verticales, cero referencias sin resolver, cero errores |

### Trabajo del 4 de septiembre de 2026

Herramienta de apoyo a la codificacion tematica de la ronda terminal. **La
codificacion en si no se automatizo y sigue declarada en el apartado 4**: lo que
estas filas cubren es la preparacion mecanica del material y la correccion de dos
defectos de los scripts de analisis.

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| `06_Experimento/scripts_analisis/extender_corpus_json.py` | Claude (Anthropic) | Script que incorpora al corpus JSON las transcripciones depositadas que aun no figuran en el | No reescribe ningun registro anterior: empalma los nuevos y comprueba campo por campo que los diez originales quedan identicos antes de escribir. Los recuentos de turnos de las seis --64, 89, 105, 43, 37 y 91-- coinciden con los verificados al depositarlas |
| `curva_saturacion.py` --- orden determinista | Claude (Anthropic) | Deteccion de que `sort_values` de pandas no es estable y de que las seis entrevistas de la ronda terminal comparten fecha, con lo que el orden entre ellas podia variar entre ejecuciones; desempate por identificador de evidencia | Se reejecuto sobre la codificacion vigente y la tabla resultante es **identica byte a byte** a `saturacion_por_entrevista.csv` ya publicada. La correccion no altera ningun resultado anterior |
| `curva_saturacion.py` del deposito Zenodo | Claude (Anthropic) | Correccion de la ruta por omision del corpus, que apuntaba a una carpeta inexistente dentro del propio deposito | Se comprobo contra el arbol real del deposito: el archivo esta en la raiz, un nivel por encima de `scripts_analisis/` |
| `02_Evidencias/Codificacion_Tematica/incorporar_codificacion.py` | Claude (Anthropic) | Script que valida una hoja de codificacion rellenada y la incorpora al archivo | Probado con filas deliberadamente invalidas: rechaza el fragmento tomado del entrevistador, el retocado al copiar, el que no lleva categoria y el duplicado, y en ninguno de esos casos escribe nada |
| Hoja de turnos y busqueda de umbrales (material de trabajo, fuera del repositorio) | Claude (Anthropic) | Separacion de los turnos del participante, descarte de los que no llegan a 18 palabras y de las formulas de cortesia, y busqueda por termino de los turnos que mencionan cada requisito huerfano | Van **todos** los turnos que superan el umbral, sin seleccion previa, para que la eleccion de que es codificable la haga quien codifica. Las columnas de codigo y de juicio se entregan vacias |

---

## 4. Secciones en las que no se empleo ninguna herramienta

Se enumeran para que la declaracion sea completa y no solo positiva.

| Seccion o artefacto | Quien lo produjo |
|---|---|
| Las diecisiete entrevistas de campo y su conduccion | El equipo, en persona |
| Las puntuaciones de los tres jueces del cuasi-experimento | Tres evaluadores externos, de forma independiente y ciega |
| El diseno del cuasi-experimento y su protocolo registrado en OSF | El equipo |
| Las decisiones de priorizacion MoSCoW, Kano y WSJF | El equipo |
| Los diagramas originales en Visual Paradigm (`.vpp`) y en draw.io | El equipo |
| El analisis, la discusion, las conclusiones y las amenazas a la validez | El equipo |
| La codificacion tematica del corpus y la curva de saturacion | El equipo. Incluida la de las seis entrevistas de la ronda terminal: la asistencia recibida se limito a separar los turnos y a buscar terminos, y las columnas de codigo, categoria y juicio se entregaron vacias |
| La sesion de validacion comunicativa y su conduccion | El equipo |
| La defensa oral y la exposicion grabada | El equipo |
| La obtencion de los consentimientos informados y de las firmas de testigos | El equipo |

## 5. Limites que el equipo se impuso

Las secciones evaluativas del reporte —analisis, discusion, conclusiones, justificacion
de las decisiones de ingenieria y amenazas a la validez— son **produccion propia del
equipo**, escritas contra la evidencia primaria del proyecto y sostenibles ante el
tribunal por cualquiera de sus integrantes.

Ninguna cifra, tabla, figura, resultado estadistico ni referencia bibliografica de este
trabajo procede de un modelo de lenguaje. Las cifras se generan por script desde los
datos crudos, con la correspondencia declarada en
[`07_Publicacion/dataset_zenodo/correspondencia_salidas.csv`](../07_Publicacion/dataset_zenodo/correspondencia_salidas.csv). Las
referencias de `referencias.bib` se verificaron individualmente y cada identificador
digital se resolvio antes de citarlo.

Los resultados no se redactaron antes de existir: la secuencia fue registrar el
protocolo, ejecutar el estudio, analizar con los scripts versionados y solo entonces
redactar.

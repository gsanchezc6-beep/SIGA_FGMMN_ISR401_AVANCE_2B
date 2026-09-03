# Guion de la defensa oral — Proyecto SIGA

**Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos · Entrega Final (2B)

---

## Modalidad: defensa individual

**La defensa es individual.** Cada integrante expone el proyecto completo por separado ante
el tribunal, y responde por la totalidad del trabajo: la especificacion, el diseno del
estudio empirico, los resultados y sus amenazas a la validez.

En la fecha de la defensa el equipo lo integraban dos personas, y **ambas rindieron
la suya**:

| Integrante | Rol en el proyecto |
|---|---|
| Sanchez Cornejo, Gary Alberto | Analista lider; especificacion, componente empirico e integracion |
| Munoz Quinonez, Yeranick Esther | Documentacion, trazabilidad, auditoria de calidad y gestion de evidencias |

Por ser individual, **no hay reparto de tiempos entre personas**. La estructura de bloques
que sigue describe como se organiza la exposicion de cada integrante dentro de los 25
minutos, seguidos de 10 minutos de preguntas.

**Lo que el tribunal evalua en esta modalidad** no es que cada quien defienda su parte, sino
lo contrario: que cada integrante sostenga el proyecto entero, incluidas las decisiones que
no tomo. Quien preparo la trazabilidad tiene que poder explicar por que la prueba de
hipotesis es apareada, y quien corrio el analisis tiene que poder explicar como se cierra
una cadena de trazabilidad rota.

---

## Bloque 1 — Problema y contribuciones (3 min)

- SIGA es un sistema real, con cliente identificable: la Facultad de Ciencias de la
  Computación y Diseño Digital de la UTEQ. No es un ejercicio de curso sobre un
  dominio ficticio.
- El problema de investigación: ¿los Requisitos Funcionales que genera un LLM a partir
  del mismo material de entrevistas son comparables en calidad a los que elicita un
  analista humano?
- Tres contribuciones concretas:
  1. Comparación pareada y ciega usando el **mismo corpus de entrevistas** para ambos
     orígenes — no un corpus distinto por brazo, que es lo que hacen la mayoría de los
     estudios previos.
  2. Un pipeline de análisis 100% reproducible, publicado con el paquete de datos.
  3. Divulgación explícita de dos complicaciones metodológicas reales ocurridas durante
     el estudio (retiro de consentimiento de un participante, y saturación temática no
     alcanzada) en vez de ocultarlas.
- Pregunta de investigación (RQ1): decirla textual, tal como aparece en el manuscrito.

## Bloque 2 — El sistema y sus stakeholders (3 min)

- Las 6 capacidades centrales de SIGA (monitoreo ambiental, control remoto,
  alertas, análisis predictivo, mantenimiento, reportes).
- Los tres perfiles de usuario reales entrevistados: docentes, coordinación
  académica, conserjería/infraestructura — con foto o diagrama de contexto en
  pantalla (`03_Modelado/Diagramas_UML/01_Context/`).
- Mencionar brevemente el volumen real de campo: 10 entrevistas válidas, con al
  menos 3 perfiles bien representados.

## Bloque 3 — Metodología del componente empírico (4 min)

- Diseño: cuasi-experimento apareado, ciego, con 3 jueces independientes de las
  personas entrevistadas.
- 51 ítems evaluados en 5 dimensiones de calidad (completitud, ausencia de
  ambigüedad, verificabilidad, corrección respecto de la fuente, consistencia
  interna), escala 1–5.
- Plan de análisis: Shapiro-Wilk para elegir prueba paramétrica o no paramétrica,
  corrección de Holm-Bonferroni por comparaciones múltiples, tamaño del efecto con
  intervalo de confianza al 95% por *bootstrap*.
- Mencionar el registro previo en OSF (DOI 10.17605/OSF.IO/7PQ3H) y que las
  desviaciones respecto de ese registro están documentadas explícitamente.

## Bloque 4 — Resultados (6 min)

- Mostrar la tabla de descriptivos: en las 5 dimensiones, la mediana/media del LLM
  es igual o mayor que la del humano.
- Mostrar la tabla de hipótesis: **antes** de corregir, Consistencia_interna daba
  p=0,012 (parecía significativo); **después** de Holm-Bonferroni, p=0,059 — ya no
  lo es. Ninguna dimensión sobrevive la corrección.
- Mostrar la figura de tamaños de efecto con sus intervalos de confianza: efectos
  grandes en magnitud, pero intervalos que cruzan el cero — mostrar visualmente por
  qué eso importa.
- Mostrar el cálculo de potencia: con 3 jueces, potencia real = 8,4%; se necesitarían
  34 pares para el 80% convencional. Esto explica por qué los intervalos son tan
  anchos.
- Mencionar brevemente la curva de saturación temática: no llegó a inflexión, y por
  qué (código sin consolidar) — un párrafo, no más de 30 segundos.

## Bloque 5 — Discusión y amenazas a la validez (4 min)

- Implicación principal: la tendencia favorable al LLM en las cifras crudas **no**
  se sostiene estadísticamente con este tamaño de muestra — es un ejemplo concreto de
  por qué la corrección por comparaciones múltiples y el cálculo de potencia importan,
  no un formalismo.
- Las 4 categorías de amenazas, una frase cada una:
  - Interna: panel de 3 jueces, muy baja potencia.
  - Externa: un solo dominio, un solo idioma, un solo modelo — no generaliza sola.
  - Constructo: el LLM tuvo exposición previa parcial al conjunto humano, y el corpus
    fuente del LLM (11 entrevistas) ya no coincide exactamente con el corpus que
    respalda al conjunto humano (10, tras excluir una entrevista por retiro de
    consentimiento).
  - Conclusión: intervalos de confianza muy anchos por el tamaño de muestra pequeño.

## Bloque 6 — Conclusiones y trabajo futuro (3 min)

- Respuesta a RQ1: no se puede confirmar ni descartar una diferencia de calidad con
  el tamaño de muestra actual; se declara así explícitamente, sin sobre-interpretar
  la tendencia numérica favorable al LLM.
- Trabajo futuro concreto (citar los 3 del manuscrito): ampliar el panel a 34 jueces,
  re-generar el Conjunto A sobre el corpus corregido de 10 entrevistas, aplicar
  codificación axial y recalcular la curva de saturación.
- Cerrar reafirmando las 3 contribuciones del bloque 1 con la evidencia ya mostrada.

## Bloque 7 — Demostración del prototipo (2 min)

- Ejecutar en vivo (idealmente `docker compose up`, o el entorno estable que se haya
  preparado) los **dos escenarios de la matriz de trazabilidad** ya identificados de
  antemano — decidir cuáles antes del simulacro, no improvisar el día de la defensa.
- Usar únicamente las credenciales de demostración documentadas en `05_MVP/README.md`.
  Nunca credenciales reales de personas del cliente.
- Si la demo falla por completo, es C13 = 0 — practicar el flujo exacto varias veces
  antes, con la red/entorno ya verificado.

---

## Preguntas del tribunal (10 min) — preparación sugerida

Al ser individual, **cada integrante responde por el proyecto entero**. No hay temas
asignados por persona. Los cinco que el tribunal suele tocar, y que conviene poder responder
sin mirar las diapositivas, son:

- **Por que REFSQ y no el journal.** La plantilla del manuscrito es Springer LNCS, que es la
  de REFSQ; el envio no exige cargo por procesamiento y el calendario cabe en el semestre.
- **El registro previo y sus desviaciones.** Que se preregistro, cuando, y por que las diez
  desviaciones se declaran en lugar de disimularse.
- **La potencia del estudio.** Por que un panel de tres jueces da una potencia de 0,084, que
  significa eso, y por que se reporta en lugar de omitirlo.
- **La matriz de trazabilidad.** Como se cierra una cadena rota y por que las 74 filas no
  tienen ninguna celda vacia.
- **El cierre en diez entrevistas.** Que se declara, que respaldo hay, y cual es el efecto
  reconocido sobre la validez externa.

> **Advertencia de la guia.** La defensa se puede reprobar si el tribunal detecta que un
> integrante no puede explicar decisiones basicas del proyecto, o si aparecen en las
> diapositivas resultados que no estan en el manuscrito ni en los scripts de analisis, lo
> que activa el gatekeeper G4. **Todo numero que se proyecte tiene que poder senalarse en una
> tabla o figura ya generada por el pipeline.**

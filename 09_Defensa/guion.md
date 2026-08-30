# Guion de la defensa oral — Proyecto SIGA
Equipo FGMMN · Entrega 4 (2B) · 25 min presentación + 10 min preguntas

> Cronómetro visible en las diapositivas durante toda la presentación. Excederse en
> más de 2 minutos penaliza C11 a la mitad. Cada integrante que habla al menos 4 minutos
> (criterio C12).
>
> **Gilces Carranza, José no participa en el reparto de tiempos.** No ha aportado al
> proyecto (0 commits en el historial verificable) y la defensa evalúa capacidad
> individual: no tiene sentido asignarle exposición sobre trabajo que no hizo. Si asiste,
> el gatekeeper **G7** ya cubre el caso — su ausencia o su silencio ante el tribunal fija
> su nota individual en máximo 4,00/10, sin afectar la nota de los demás integrantes
> (la defensa es individual). Los 25 minutos se reparten entre los 4 integrantes activos.

| # | Bloque | Minutos | Acumulado | Responsable sugerido |
|---|---|---:|---:|---|
| 1 | Problema y contribuciones | 3 | 0:00–3:00 | Sánchez Cornejo, Gary (Analista líder) |
| 2 | El sistema y sus stakeholders | 3 | 3:00–6:00 | Mendoza Palma, Allan (construyó el diagrama de contexto y el modelo i*) |
| 3 | Metodología del componente empírico | 4 | 6:00–10:00 | Sánchez Cornejo, Gary (ejecutó el pipeline estadístico) |
| 4 | Resultados, con tablas y figuras del manuscrito | 6 | 10:00–16:00 | Sánchez Cornejo, Gary (4 min) + Cedeño Ávila, Winston (2 min: cobertura de RF *Must* en el MVP, como puente hacia la demo) |
| 5 | Discusión y amenazas a la validez | 4 | 16:00–20:00 | Sánchez Cornejo, Gary (3 min) + Mendoza Palma, Allan (1 min: amenaza externa — un solo dominio institucional) |
| 6 | Conclusiones y trabajo futuro | 3 | 20:00–23:00 | Muñoz Quiñónez, Yeranick (Documentación) |
| 7 | Demostración corta del prototipo | 2 | 23:00–25:00 | Cedeño Ávila, Winston (MVP) |

Con este reparto: Sánchez 11 min, Mendoza 4 min, Muñoz 3 min, Cedeño 4 min. **Muñoz
queda con 3 min, por debajo del mínimo de 4** — ampliar su bloque 6 con un minuto de
las conclusiones (p. ej. detallar el trabajo futuro de recodificación temática, que es
parte de su rol de gestión de evidencias) antes del simulacro. Sánchez concentra la
mayor carga porque es quien ejecutó el componente empírico y es el único que puede
defenderlo con solvencia ante preguntas del tribunal; repartir ese contenido a alguien
que no lo trabajó arriesga un silencio individual peor (mismo problema que se está
corrigiendo con Gilces). Ajustar y medir con cronómetro real en el simulacro de la
semana 16 — los tiempos de esta tabla son un punto de partida, no el reparto final.

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

Cada integrante debe poder responder, sin ayuda de las diapositivas, sobre:

- **Sánchez (líder):** por qué se eligió REFSQ Posters & Tools en vez del journal
  Requirements Engineering; cómo se gestionó el registro OSF y sus desviaciones.
- **Mendoza (modelado):** consistencia entre los diagramas UML y el código real del
  MVP; por qué el modelo i* se hizo así.
- **Cedeño (MVP):** por qué el MVP cubre el porcentaje de RF Must que cubre y no más;
  arquitectura del stack (Node.js + Express + Socket.io + SQLite).
- **Muñoz (documentación/evidencias):** cómo se aplicó el modelo de zonas [P]/[R];
  por qué se excluyó la entrevista EV-15 y qué se hizo con esa evidencia.
- **Sánchez (además de lo anterior):** cómo se construyó la matriz de trazabilidad de
  66 filas; por qué el panel de 3 jueces resulta en 8,4% de potencia y qué significa
  eso en términos simples. Se agrega aquí porque Gilces, a quien correspondía
  originalmente este tema por rol declarado, no aportó al trabajo real.

> **Advertencia de la guía.** La defensa se puede reprobar si el tribunal detecta que
> algún integrante no puede explicar decisiones básicas del proyecto, o si aparecen en
> las diapositivas resultados que no están en el manuscrito ni en los scripts de
> análisis (fabricación de evidencia, gatekeeper G4). Todo número que se proyecte debe
> poder señalarse en una tabla o figura ya generada por `make all`.
>
> **Sobre Gilces Carranza, José:** si asiste a la defensa, el tribunal puede dirigirle
> preguntas igual que a cualquier otro integrante registrado. No se le preparó
> contenido porque no participó en el trabajo real; su desempeño ante esa situación es
> su responsabilidad individual (gatekeeper G7), no un riesgo para la nota del resto
> del equipo.

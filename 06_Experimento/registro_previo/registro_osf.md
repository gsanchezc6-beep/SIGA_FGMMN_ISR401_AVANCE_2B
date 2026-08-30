# Registro OSF del protocolo — estado y pendientes

## Registro confirmado

| Campo | Valor |
|---|---|
| **DOI del registro** | [`10.17605/OSF.IO/7PQ3H`](https://doi.org/10.17605/OSF.IO/7PQ3H) |
| Enlace directo | <https://osf.io/7pq3h> |
| Estado | **Aceptado** |
| Protocolo registrado | [`protocolo.pdf`](../protocolo/protocolo.pdf) · fuente en [`protocolo.tex`](../protocolo/protocolo.tex) y [`protocolo.md`](../protocolo/protocolo.md) |

Este DOI es el que debe constar en `CITATION.cff`, en el `README.md` de la raíz, en la
sección *Data and materials availability* del manuscrito y en la descripción del depósito
de Zenodo.

## Estado de los archivos del registro previo

| Archivo | Qué contiene | Estado |
|---|---|---|
| `bitacora_desviaciones.pdf` | Cada desviación del análisis ejecutado respecto del plan pre-registrado, con la razón, el momento en que se detectó y la mitigación aplicada. | Presente en esta carpeta |
| `osf_registration.pdf` | Exportación del registro OSF con su marca temporal, que acredite que el registro es anterior al inicio de la recolección de datos. | **No está en el repositorio.** Se descarga desde <https://osf.io/7pq3h> y se deposita aquí |

El criterio de piso **G9** exige que el protocolo esté registrado con marca temporal
anterior al inicio de la recolección. El registro existe y está aceptado; lo que falta es
la constancia descargable dentro del repositorio, porque toda evidencia declarada tiene
que reposar aquí y superar la verificación de su tipo.

## Desviaciones respecto del protocolo pre-registrado

Encabezan la lista las tres desviaciones críticas del 13/08/2026; las numeradas 4 a 8
se anticiparon antes de conocer los resultados, comparando el protocolo contra lo que
exige la Sección 4.4 de la guía de 2B. Cada una necesita su entrada en
`osf_deviations.pdf`, con la razón, el momento en que se detectó y la mitigación
aplicada.

> **Corrección (2026-08-28).** Al llenar la actualización real en OSF se verificó que
> la corrección de Holm-Bonferroni **ya estaba en el registro pre-registrado**
> (campo "Inference Criteria" del formulario OSF), no es una desviación. Se retiró de
> esta lista y se renumeró; la lista original tenía 10 puntos, ahora tiene 9. Esto no
> se detectó antes porque `protocolo.md`/`.tex` (la copia local) no incluye ese campo
> con el mismo detalle que el formulario real de OSF — verificar siempre contra el
> registro real, no solo contra la copia local, antes de declarar una desviación.

1. **Exclusión de EV-15 (DOC-03) por retiro de consentimiento informado.** El
   participante no firmó el consentimiento, ni para la entrevista ni para el
   walkthrough asociado (WT-03, ya invalidado desde 2A por el mismo motivo). La
   entrevista se excluyó íntegramente el 13/08/2026: se eliminó la transcripción,
   se retiraron sus fragmentos de `codificacion_tematica.csv`, se re-fundamentaron
   en EV-13 y EV-14 los requisitos que dependían de ella (RNF-16, RD-02) y se
   eliminó de `matriz_trazabilidad.csv` la fila sin corroboración alternativa
   (oposición a cámaras, antes ligada solo a EV-15). Ver el detalle completo en
   `02_Evidencias/Transcripciones/00_LEEME_Transcripciones.txt` y en la fila EV-15
   de la Tabla B.1 del ERS.
2. **Contaminación parcial y tardía del corpus fuente del LLM.** El contenido de
   EV-15 formaba parte de `material_fuente_LLM.txt` cuando se generó el Conjunto A
   de RF (LLM) que **ya fue evaluado por los tres jueces ciegos**. La exclusión de
   EV-15 ocurrió *después* de esa evaluación. Por restricción de tiempo de la
   Entrega 4 (2B), **no se re-ejecutó el experimento completo** (no se regeneró el
   Conjunto A ni se repitió la evaluación ciega). El contenido textual de EV-15 ya
   fue redactado de `material_fuente_LLM.txt`; `Conjunto_A_RF_LLM.md` se conserva
   sin alterar como registro histórico exacto de lo efectivamente juzgado, con una
   nota de integridad al inicio del documento. Esta desviación debe declararse
   también como amenaza a la **validez de constructo** en el manuscrito, junto a la
   exposición previa parcial del modelo al Conjunto B (punto 7).
3. **Cierre del levantamiento de campo en N = 10 en lugar de N ≥ 16.** El docente
   responsable, Ing. Gleiston Guerrero Ulloa, autorizó verbalmente en clase el cierre
   de la recolección de entrevistas en las 10 restantes tras la exclusión de EV-15,
   por restricción del calendario (corte adelantado a la semana del 17/08/2026) y por
   agotamiento de la población disponible para nuevas entrevistas.

   **Constancia del equipo (autodeclarada, 2026-08-13).** No existe registro escrito
   de esta autorización al momento de escribir esta nota: fue comunicada verbalmente
   en clase, sin testigos externos ni respaldo documental por parte del docente. El
   equipo intentó obtener confirmación por escrito el 13/08/2026 por WhatsApp, sin
   respuesta al cierre de esa fecha. Se reintentará el 14/08/2026. Esta entrada deja
   constancia de que la desviación es real y de que el equipo actuó de buena fe
   conforme a la instrucción recibida, aun cuando el respaldo documental quede
   pendiente. Si la confirmación escrita llega antes del corte, sustituir este párrafo
   por la cita textual y la fecha del mensaje del docente.
4. **Intervalos de confianza por *bootstrap*.** El protocolo declaraba tamaño del efecto
   (*d* de Cohen / δ de Cliff) sin intervalos de confianza; la guía exige IC al 95 %
   construidos por *bootstrap* de 10 000 réplicas.
5. **Pruebas de supuestos.** El protocolo declaraba Shapiro-Wilk; la guía exige además
   Levene para homogeneidad de varianzas.
6. **Número de jueces.** El protocolo fijaba un mínimo de 3 y recomendaba 5. Se ejecutó
   con 3. Si el panel se amplía en la ronda terminal, el cambio de *n* de jueces se declara;
   si no se amplía, se declara como limitación asumida.
7. **Exposición previa del modelo.** Amenaza a la validez de constructo ya declarada en
   [`prompts_llm/prompt_llm_conjunto_A.md`](prompts_llm/prompt_llm_conjunto_A.md): el
   modelo que generó el Conjunto A tuvo exposición previa parcial al Conjunto B dentro de
   la misma cuenta de chat. Debe aparecer tanto aquí como en la sección de amenazas a la
   validez del manuscrito.
8. **Corpus fuente reducido, no ampliado.** El protocolo declaraba «11 entrevistas
   anonimizadas» como material fuente del Conjunto A; el corpus final válido quedó en
   10 por la exclusión del punto 1. El Conjunto A **no** se regeneró sobre el corpus
   reducido (ver punto 2): la asimetría entre lo que vio el LLM (11, incluida EV-15) y
   lo que finalmente respalda al equipo humano (10) es una desviación que afecta a la
   validez interna y debe declararse de forma explícita.
9. **C6 cerrado por *power calculation*, no por curva de saturación.** El
    pipeline ejecutado el 13/08/2026 confirmó que la curva de saturación
    (`07_Publicacion/figuras/curva_saturacion.png`) **no muestra inflexión**:
    con 10 entrevistas válidas, el promedio de códigos nuevos en las últimas
    3 entrevistas (3,667) supera ampliamente el umbral del 5% (1,8). La causa
    no es falta de datos de campo, sino que `codificacion_tematica.csv` nunca
    pasó por una fase de codificación axial: sus 36 códigos son todos
    distintos entre sí, uno por fragmento, sin fusionar los que representan
    el mismo tema en entrevistas distintas — con un codebook así, la curva
    jamás puede aplanarse, sin importar cuántas entrevistas se agreguen. Dado
    que el Enfoque 1 admite el *power calculation* como vía alterna (Sección
    C6 de la guía), se cierra el criterio con
    `scripts_analisis/power_calculation.py` (Cohen d=0,5, α=0,05,
    potencia=0,80) en lugar de rehacer la codificación bajo la presión de
    tiempo del corte. La curva se conserva y se publica de todas formas,
    como evidencia exploratoria, con esta limitación declarada explícitamente
    en el manuscrito (Amenazas a la validez → validez de conclusión) en vez
    de omitirse.

## Regla que gobierna esta carpeta

> El plan de análisis registrado previamente en el OSF se contrasta con el análisis
> efectivamente ejecutado; **toda desviación se reporta explícitamente** en la sección de
> metodología del manuscrito. Formular hipótesis después de conocer los resultados
> (*HARKing*) o ejecutar múltiples análisis hasta encontrar uno significativo
> (*p-hacking*) son prácticas indebidas y las detectan automáticamente muchos editores del
> área.

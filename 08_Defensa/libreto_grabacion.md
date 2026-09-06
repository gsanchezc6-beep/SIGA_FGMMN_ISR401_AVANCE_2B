# Libreto de grabación de la defensa

**Proyecto SIGA — Sistema Inteligente de Gestión de Aulas · Equipo FGMMN**
Universidad Técnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)
Versión 1.0 · 2026-09-06

---

## Cómo se usa esto

El texto **entre comillas se dice tal cual**. Lo que va en cursiva es una acción, no se lee.

No hay que memorizarlo: hay que **entenderlo y decirlo con sus palabras**, pero sin salirse de
lo que afirma. Cada cifra de este libreto está verificada contra el repositorio; si se cambia
una al hablar, deja de estar respaldada.

**Reglas de la grabación:**

- Una sola toma por bloque. Si alguien se traba, se corta y se repite **ese bloque**, no todo.
- Nadie habla del trabajo de otro en primera persona. Quien no hizo algo dice «el equipo» o
  nombra a quien lo hizo.
- **25 minutos, y pasarse de dos penaliza.** Cronómetro a la vista.

## Reparto

| Quién | Bloques | Minutos |
|---|---|---|
| **Gary** | 1, 4 y 7 | 10 |
| **Yeranick** | 2, 3 y 5 | 9 |
| **Cedeño** | 6 y 8 | 6 |

Es el único reparto que no parte ningún bloque por la mitad, y sigue el aporte real que
declara `04_Trazabilidad/aporte_individual.csv`.

---

# GARY — Diapositiva 1 · portada · 30 s

*Comparte pantalla con la presentación en modo presentador.*

> «Buenos días. Somos el equipo FGMMN y presentamos SIGA, Sistema Inteligente de Gestión de
> Aulas, para la asignatura de Ingeniería de Requerimientos. Soy Gary Sánchez, me acompañan
> Yeranick Muñoz y Winston Cedeño. Vamos a repartirnos veinticinco minutos.»

*Avanza.*

# GARY — Diapositiva 2 · Bloque 1 · 2 min

> «SIGA tiene un cliente real e identificable: la Facultad de Ciencias de la Computación de
> la UTEQ. No es un dominio inventado para el curso.
>
> La pregunta que responde el estudio es esta: los requisitos funcionales que genera un
> modelo de lenguaje a partir del mismo material de entrevistas, ¿son comparables en calidad
> a los que elicita un analista humano?
>
> Y aportamos tres cosas. Primera, una comparación pareada y ciega sobre **el mismo corpus**
> para los dos orígenes; la mayoría de estudios previos usan un corpus distinto por brazo.
> Segunda, un pipeline de análisis reproducible de principio a fin, publicado con el paquete
> de datos. Y tercera, y es la que más nos importa: **declaramos las complicaciones en vez de
> esconderlas** — un participante retiró su consentimiento, y la saturación temática no se
> alcanzó. Las dos cosas están escritas en el manuscrito.»

*Avanza y cede a Yeranick.*

---

# YERANICK — Diapositiva 3 · Bloque 2 · 3 min

> «El sistema atiende a cuatro perfiles: docentes, personal de servicios generales,
> coordinación de carrera y personal técnico de tecnologías de la información.
>
> El corpus son **dieciséis entrevistas** transcritas y anonimizadas, más **nueve sesiones de
> validación** sobre prototipos, dos de ellas con usuario técnico. Y doce notas de campo.
>
> De esas dieciséis entrevistas, **diez están codificadas temáticamente**. Las seis de la
> ronda terminal del tres de septiembre están transcritas y depositadas, y su codificación
> queda declarada como pendiente en el manuscrito, en la amenaza T4. Lo decimos aquí porque
> preferimos decirlo nosotros.»

*Avanza.*

# YERANICK — Diapositiva 4 · Bloque 3 · 3 min

> «El componente empírico es un cuasi-experimento apareado. Cincuenta y un enunciados de
> requisitos, unos redactados por el equipo y otros generados por un modelo, mezclados y
> con el orden aleatorizado.
>
> Los evalúa un panel **ciego**: los jueces no saben de dónde viene cada enunciado. Puntúan
> de uno a cinco en cinco dimensiones: completitud, ausencia de ambigüedad, verificabilidad,
> corrección respecto de la fuente y consistencia interna.
>
> Y el protocolo está **registrado antes de recoger los datos**, en el Open Science Framework,
> con DOI diez punto uno siete seis cero cinco, barra OSF punto IO, barra siete P Q tres H.
> Aceptado el dos de agosto y archivado por el Center for Open Science. Esa marca de tiempo es
> externa a nosotros: no la podemos mover.»

*Avanza y cede a Gary.*

---

# GARY — Diapositivas 5, 6 y 7 · Bloque 4 · 6 min

> ⚠️ **Este bloque depende de una decisión pendiente.** Ver la nota al final del libreto
> antes de grabarlo.

> «Los resultados, con el panel de tres jueces que fija el registro previo.
>
> En las cinco dimensiones las cifras crudas favorecen al modelo. Pero esa frase, sola, sería
> engañosa, y por eso la siguiente diapositiva existe.»

*Avanza.*

> «Ninguna diferencia es estadísticamente significativa después del ajuste. Y el motivo está
> medido: **la potencia del panel es del ocho coma cuatro por ciento** frente al ochenta
> convencional. Para detectar un efecto medio harían falta **treinta y cuatro observaciones
> apareadas**; tenemos tres.
>
> Ese número lo calculamos nosotros y lo publicamos, sabiendo que juega en contra del
> resultado. Un estudio que oculta su potencia parece más fuerte de lo que es.»

*Avanza.*

> «Y por eso el análisis de sensibilidad toma el requisito, y no el juez, como unidad de
> análisis. Está declarado como desviación del protocolo en la bitácora del registro previo.»

*Avanza y cede a Yeranick.*

---

# YERANICK — Diapositiva 8 · Bloque 5 · 3 min

> «Las amenazas a la validez. Están las ocho en el manuscrito, dos por categoría; menciono
> las tres que más pesan.
>
> La primera es el tamaño del panel, que acaban de ver.
>
> La segunda es la saturación temática: **no se alcanzó**, y la curva no se dobla. No la
> forzamos ni la maquillamos; se publica como está y se declara.
>
> Y la tercera es la codificación pendiente de las seis últimas entrevistas. Decir dieciséis
> sin esa precisión haría pasar por analizado lo que solo está transcrito.»

*Avanza y cede a Cedeño.*

---

# CEDEÑO — Diapositiva 9 · Bloque 6 · 3 min

> «Las conclusiones.
>
> Sobre la primera pregunta: en las cinco dimensiones de calidad no encontramos diferencia
> significativa entre los requisitos del equipo humano y los del modelo, con el panel del que
> disponemos.
>
> Sobre la segunda, que es la que añadimos al enunciar RQ2: **cuánta potencia alcanza un panel
> ciego de tres jueces**. La respuesta es ocho coma cuatro por ciento, y una réplica
> necesitaría treinta y cuatro observaciones apareadas o cambiar la unidad de análisis.
>
> Lo publicamos para que el siguiente estudio no repita un diseño con poca potencia sin
> saberlo.»

*Avanza y cede a Gary.*

---

# GARY — Diapositiva 10 · Bloque 7 · demostración · 2 min

*Cambia a la ventana del prototipo, ya abierta y con datos cargados **antes** de empezar a
grabar. No se abre nada en directo.*

**Ruta del código:** `05_MVP/codigo_fuente/`
**Instrucciones de despliegue:** `05_MVP/despliegue/`

> «Dos minutos de prototipo. Esto es el panel de control centralizado: estado de cada aula,
> temperatura y ocupación. Desde aquí se abre la alerta, y desde la alerta se crea el ticket
> de mantenimiento con su aula, su equipo y su prioridad.
>
> La cobertura de requisitos sobre este código está en la matriz, requisito por requisito.»

*Vuelve a la presentación, avanza y cede a Cedeño.*

---

# CEDEÑO — Diapositivas 11, 12 y 13 · Bloque 8 · 3 min

> «Un minuto por cada cosa que hicimos para que esto se sostenga.
>
> **Verificación.** La especificación pasó una inspección de Fagan formal: dieciséis defectos,
> tres críticos, nueve mayores y cuatro menores. Densidad de cero coma sesenta y cuatro
> defectos por requisito. Después una re-inspección donde **cada defecto lo verifica quien no
> lo corrigió**: quince quedan cerrados y uno residual. Y un comité de control de cambios con
> cuatro solicitudes, tres aprobadas y una diferida, porque no verificamos si la interfaz
> instalada permite abrir una cámara individual.
>
> Con un solo residual, la métrica de corrección da **cero coma cero cuatro**, por debajo del
> cero coma cero cinco de referencia. El margen es de un defecto, y lo decimos así.»

*Avanza.*

> «**Trazabilidad.** La matriz tiene setenta y cuatro filas; cuarenta y una con la cadena
> completa desde la fuente hasta el criterio de aceptación, y las setenta y cuatro con todos
> sus eslabones declarados: ninguna celda ambigua.
>
> Y el tablero de gestión tiene sesenta actividades, una por requisito. La sincronización con
> la matriz es del **cien por cien**, sesenta de sesenta, y se recalcula con un script.
>
> Ese cien por cien mide correspondencia entre dos listas, **no avance**: las sesenta están en
> "por hacer", que es su estado real.»

*Avanza.*

> «**Evidencia de campo.** Dieciséis entrevistas, nueve sesiones de validación y doce notas de
> campo. Seis de esas notas son manuscritas y contemporáneas, escritas durante la sesión; las
> otras seis son reconstrucción documentada y **lo dicen ellas mismas en su cabecera**.
>
> Y la codificación la hicimos dos personas por separado sobre el mismo subconjunto: kappa de
> Cohen de cero coma seiscientos treinta y cinco, acuerdo sustancial.»

*Avanza y cede a Gary.*

---

# GARY — Diapositivas 14 y 15 · cierre · 30 s

> «Este es el reparto de la exposición y del trabajo, que sigue la matriz de aporte
> individual. Gracias, quedamos a sus preguntas.»

*Deja la diapositiva 15 en pantalla durante las preguntas.*

---

# Antes de grabar — lista de comprobación

| | |
|---|---|
| Presentación exportada y abierta en modo presentador | `08_Defensa/presentacion.pptx` |
| Prototipo abierto, con datos, **antes** de grabar | `05_MVP/` |
| Cronómetro visible para los tres | — |
| Banco de preguntas leído por los tres | `08_Defensa/banco_preguntas.md` |
| Micrófono probado con una toma de diez segundos | — |

**Que los tres hayan leído el banco de preguntas**, no solo quien expone ese bloque. Las
preguntas del tribunal duran diez minutos y no respetan el reparto.

---

# ⚠️ Nota sobre el Bloque 4, antes de grabarlo

El texto de arriba corresponde al análisis con **tres jueces**, que es el que fija el registro
previo de OSF y el que está publicado en el repositorio.

El 5 de septiembre se incorporaron siete jueces más. Con los diez, **los efectos desaparecen y
el acuerdo entre evaluadores cae a prácticamente cero**. Ese análisis está calculado pero **no
depositado**, y la decisión de qué hacer con él está pendiente del equipo. El informe completo
está en `Escritorio\DECISIONES CLAUDE\2026-09-05_panel_de_10_jueces.md`.

**Si el equipo decide mantener los tres jueces como análisis primario** —la opción
recomendada— este libreto vale tal como está, y conviene añadir una frase al final del
bloque 5:

> «Ampliamos el panel a diez evaluadores como comprobación. El efecto no se replica y el
> acuerdo entre ellos cae, lo que sugiere que la rúbrica necesita entrenamiento previo. Lo
> reportamos porque un resultado que no sobrevive a un panel mayor hay que decirlo.»

**Si el equipo decide adoptar los diez**, hay que reescribir el bloque 4 entero, y también las
conclusiones del bloque 6. No grabar hasta haberlo decidido.

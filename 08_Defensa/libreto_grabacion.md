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

> **Aviso de tiempo.** Los bloques 4 y 5 crecieron al incorporar el panel ampliado y la
> saturación, y entre los dos se van cerca de **un minuto y medio por encima** de sus tres y
> seis minutos. **Crónometren un ensayo antes de grabar.** Si se pasan, lo primero que se
> recorta es el bloque 1: la frase de las tres aportaciones se puede decir en una y no
> sostiene ninguna cifra. Lo último que se toca son las reservas del bloque 5 --- son
> justamente lo que distingue este trabajo, y quitarlas para ganar treinta segundos sale
> caro.

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
> **Las dieciséis están codificadas temáticamente**: ciento treinta y seis fragmentos bajo
> cincuenta códigos. Las seis últimas se codificaron el seis de septiembre, repartidas entre
> los tres por entrevista completa, y cada cita se comprobó literal contra su transcripción
> antes de entrar.»

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

*Antes de avanzar, añade el párrafo del panel ampliado que está al final de este libreto.*

*Avanza y cede a Yeranick.*

---

# YERANICK — Diapositiva 8 · Bloque 5 · 3 min

> «Las amenazas a la validez. Están las ocho en el manuscrito, dos por categoría; menciono
> las tres que más pesan.
>
> La primera es el tamaño del panel, que acaban de ver.
>
> La segunda es la saturación temática. **Sí se alcanzó**, y precisamente por eso hay que
> contar cómo. Con diez entrevistas la curva no se doblaba, y el motivo no era el corpus: era
> nuestro libro de códigos, que tenía treinta y seis códigos para treinta y seis fragmentos,
> uno por uno. Con un libro así la curva **no puede** aplanarse, por muchas entrevistas que se
> hagan. Al codificar las seis restantes contra el libro que ya existía, pasamos a dos coma
> siete fragmentos por código y la curva se dobla.
>
> Dos cosas contra nosotros, y las decimos. Las instrucciones que repartimos pedían reutilizar
> códigos antes que inventarlos: es lo correcto, pero empuja hacia el resultado que salió. Y
> las seis últimas entrevistas son todas de docentes, así que saturamos dentro de un perfil,
> no en todo el dominio.
>
> Y la tercera amenaza: los dos conjuntos de requisitos que compara el experimento salieron
> del material de las diez primeras y **no se regeneraron**. El análisis cualitativo va por
> dieciséis y la comparación por diez. No es lo mismo y no lo mezclamos.»

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

> «**Trazabilidad.** La matriz tiene setenta y cinco filas; cuarenta y una con la cadena
> completa desde la fuente hasta el criterio de aceptación, y las setenta y cinco con todos
> sus eslabones declarados: ninguna celda ambigua.
>
> Y el tablero de gestión tiene sesenta y una actividades, una por requisito. La sincronización con
> la matriz es del **cien por cien**, sesenta y una de sesenta y una, y se recalcula con un
> script.
>
> Ese cien por cien mide correspondencia entre dos listas, **no avance**: las sesenta y una
> están en "por hacer", que es su estado real.»

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

# El panel ampliado: qué se decidió y cómo se cuenta

**Decidido el 2026-09-06. El bloque 4 se graba tal como está escrito arriba.**

Se intentó ampliar el panel de tres a diez evaluadores, dos veces, y las dos fallaron. El
listón se había fijado por escrito antes de convocar la segunda sesión —Fleiss ≥ 0,41— y se
obtuvo **−0,026**. Se mantienen los tres jueces del registro previo como análisis primario,
que es lo que ese documento ya decía que se haría en este caso.

Todo está depositado en `06_Experimento/panel_ampliado/`, con los datos crudos de las dos
vueltas y el script que los analiza.

**Gary lo dice al cerrar el bloque 4**, que es donde se habla del panel. Va después de
la frase sobre la potencia del ocho coma cuatro por ciento, en la diapositiva 6:

> «Y una cuarta que preferimos contar aunque no nos favorezca. Intentamos ampliar el panel de
> tres a diez evaluadores, dos veces, para ganar potencia. Las dos veces el acuerdo entre
> ellos salió **por debajo del azar**.
>
> La segunda vuelta la rehicimos entera: menos enunciados, quitamos la dimensión que no se
> podía responder sin las transcripciones, imprimimos las anclas en la propia hoja y
> calibramos en grupo antes de empezar. No se movió.
>
> Lo que sí encontramos fue de dónde venía el ruido. Habíamos escondido tres enunciados
> repetidos en la hoja, sin decirlo. **Tres de los siete evaluadores se contradijeron a sí
> mismos hasta en tres puntos** sobre el mismo enunciado, en la misma sesión. Uno no repitió
> ninguna de sus doce puntuaciones.
>
> Si alguien no coincide consigo mismo, no puede coincidir con otro. El ruido está dentro de
> cada evaluador, y por eso añadir evaluadores no arregla nada: esta rúbrica necesita gente
> entrenada. Lo publicamos para que quien replique el estudio no reclute un panel de
> estudiantes creyendo que gana potencia, porque lo que gana es ruido.»

**Si en las preguntas les aprietan con «entonces su resultado depende de elegir tres jueces»,**
la respuesta es esta y conviene tenerla preparada:

> «Depende del registro previo, que fija tres y es anterior a los datos. Y los tres concuerdan
> entre sí: coinciden exactamente en el 53 % de sus puntuaciones, frente al 37 % de los
> siete, que es justo lo que da el azar. El criterio para sustituirlos lo escribimos antes de
> mirar los datos y no se cumplió. Cambiarlo después habría sido elegir el resultado.»

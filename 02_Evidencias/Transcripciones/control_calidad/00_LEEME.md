# Control de calidad de la transcripcion

**Proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ**

Dos entrevistas de la ronda terminal, `DOC-05` y `DOC-06`, se transcribieron **dos veces de
forma independiente**, por Cedeno Avila y por Munoz Quinonez, sin que ninguno viera la
version del otro. Esta carpeta guarda las dos versiones y su comparacion.

---

## Por que dos veces

Una transcripcion es la unica forma en que el contenido de una entrevista llega al analisis.
Si tiene un error, ese error se propaga a la codificacion tematica, a la matriz de
trazabilidad y a lo que se cite en el manuscrito, y ya nadie vuelve al audio a comprobarlo.

Transcribir dos veces y comparar es lo que permite saber **cuanto se pierde por el camino**.

## Que salio

| | `DOC-05` | `DOC-06` |
|---|---|---|
| Palabras, version de Cedeno Avila | 3 108 | 2 624 |
| Palabras, version de Munoz Quinonez | 3 086 | 2 577 |
| **Coincidencia palabra a palabra** | **98,3 %** | **97,2 %** |
| Tramos que difieren | 52 | 75 |

**El porcentaje engana, y conviene decirlo.** Un 98 % suena a casi identico, pero convive con
ciento veintisiete tramos que difieren entre las dos. Lo que importa no es cuanto coinciden,
sino **en que no**.

## Los tres tipos de discrepancia, por orden de gravedad

**1. Atribucion.** En `DOC-05`, la frase «no es transparente, no habria trazabilidad» esta
atribuida al entrevistador en una version y al participante en la otra. En `DOC-06` ocurre lo
mismo con la frase sobre los charcos del aire acondicionado.

Es la mas grave de todas: citar como testimonio de un participante algo que dijo el
entrevistador invalida la cita.

**2. Contenido perdido.** En `DOC-06`, una version dice «aires acondicionados **o
iluminacion**» y la otra solo «aires acondicionados». La iluminacion es uno de los equipos
sobre los que actua el sistema, de modo que esa palabra sostiene un requisito. En la misma
entrevista, «trazabilidad» quedo como «habilidad» en una de las dos.

**3. Oido.** «2017-2018» frente a «2018 171», «se divide en la red» frente a «en la rey»,
«charquitos» frente a «cerquitos», «atender la situacion» frente a «atender la aceptacion».
Ninguna de las dos versiones gana: cada una acierta donde la otra falla.

Hay ademas una discrepancia que **no tiene respuesta obvia**: uno transcribio «HMI», que es
lo que se oye, y el otro «HDMI», que es lo que el participante quiso decir. Se resuelve
declarando el criterio, no eligiendo al azar.

## Como se resuelven

**Volviendo al audio, no poniendose de acuerdo.** En una transcripcion existe una verdad
comprobable: lo que la persona dijo esta grabado. La discrepancia no se negocia entre
transcriptores, se decide escuchando.

Esto es **lo contrario** de lo que corresponde en la codificacion tematica del elemento A7:
alli reconciliar antes de calcular el coeficiente lo deja sin valor, porque lo que se mide es
precisamente cuanto coinciden dos lecturas independientes. Aqui no se mide el acuerdo: se
busca el acierto.

`comparacion_transcripciones.csv` lista los 127 tramos con dos columnas vacias,
`resuelto_contra_audio` y `version_elegida`, para ir cerrandolos.

## Que se deposito como evidencia

En la carpeta de arriba hay **una sola transcripcion por entrevista**, para que no haya duda
de cual es la valida. Toma como base la version de Cedeno Avila, que conserva la atribucion
correcta y una segmentacion de turnos mas fina.

Las dos versiones independientes se conservan **aqui, no alli**, por dos razones: son la
prueba de que el control se hizo, y mantenerlas fuera de la carpeta de evidencia evita que
alguien tome por definitiva una version que no lo es.

## Anonimizacion

Las cuatro versiones se auditaron antes de depositarse. Se completaron dos cosas que faltaban
en una o en ambas:

| Que aparecia | Como quedo | Regla |
|---|---|---|
| El nombre real del participante | `[Entrevistado]` | 1 — el entrevistado va por su seudonimo |
| El nombre y apellido del entrevistador | `[ENTREVISTADOR]` | Precedente del corpus, en cuatro de las diez transcripciones anteriores |
| El nombre de la empresa donde trabaja un familiar del participante | `[ORGANIZACION]` | 10 — organizacion tercera no participante |

Comprobado sobre los cuatro archivos: **cero nombres propios, cero organizaciones, cero
numeros de identificacion, cero correos**.

## Alcance de este control

**Se transcribieron por duplicado dos de las seis entrevistas de la ronda terminal**, como
muestra de control. Las otras cuatro tienen una sola transcripcion. No se presenta como el
procedimiento aplicado a todo el corpus, porque no lo fue.

# Segunda vuelta del panel — cómo dirigirla

---

## Lo que se entrega a cada juez

| Archivo | |
|---|---|
| `hoja_puntuacion_JUEZ_v2.pdf` | **La única hoja.** 27 posiciones, 4 dimensiones, anclas impresas dentro |

**Ya no se entrega la rúbrica aparte.** Las anclas de 1, 3 y 5 van impresas en la primera
página de la hoja, que es donde se miran mientras se puntúa. Una rúbrica en otro archivo no la
abre nadie.

---

## La sesión, paso a paso

> **Ejemplo A.** «El sistema debe ser rápido y fácil de usar.»
> Completitud 1 · Sin ambigüedad 1 · Verificabilidad 1 · Consistencia 3
> **Por qué:** «rápido» y «fácil» no se pueden medir ni implementar. Es el caso de manual.

> **Ejemplo B.** «El sistema debe enviar una alerta al personal técnico cuando un aula supere
> los 28 °C durante más de 10 minutos.»
> Completitud 5 · Sin ambigüedad 5 · Verificabilidad 5 · Consistencia 5
> **Por qué:** actor, condición, umbral y acción. Se implementa y se comprueba sin preguntar.

> **Ejemplo C.** «El sistema debe permitir consultar el estado de las aulas.»
> Completitud 3 · Sin ambigüedad 3 · Verificabilidad 2 · Consistencia 4
> **Por qué:** se entiende qué hace, pero no dice qué es «estado» ni cómo se comprueba. Es el
> caso intermedio, y es el que más cuesta acordar.


### Durante (30 a 40 minutos)


## Qué esperar

Con esto el acuerdo debería subir. Pero **puede que el efecto siga sin aparecer**, y eso sería
un resultado legítimo, no un fracaso: significaría que la diferencia entre los requisitos del
equipo y los del modelo no se sostiene con un panel mayor.

Lo que sí cambia es que entonces podría afirmarlo, en vez de no poder concluir nada. Un nulo
con evaluadores que concuerdan es un hallazgo; un nulo con evaluadores que no concuerdan entre
sí no es nada.

**Si el acuerdo vuelve a salir cerca de cero**, la decisión es mantener los tres jueces del
registro previo como análisis primario y reportar las dos vueltas como lo que son: la prueba
de que esta rúbrica necesita evaluadores entrenados.

---

## Detalle del diseño, por si lo preguntan en la defensa

| | |
|---|---|
| Enunciados | 24 de los 51, **12 de cada origen** |
| Selección | Aleatoria con semilla fija **20260906**, reproducible |
| Orden | Aleatorizado, distinto del de la primera vuelta |
| Repetidos de control | 3, separados **13, 14 y 16 posiciones** de su gemelo |
| Dimensiones | 4 de 5; se retira «Corrección respecto de la fuente» y se declara |
| Juicios por persona | 108, frente a los 255 de la primera vuelta |

**Los mismos siete evaluadores repiten.** Eso introduce un efecto de arrastre que hay que
declarar: ya vieron estos enunciados. Se mitiga con el subconjunto y el orden nuevo, y se
atenúa por sí solo porque la primera vuelta no dejó criterio que arrastrar. Si consigue
sustituir a alguno por una persona que no participó, mejor — pero no retrase la sesión por eso.

# Huerfanos y cadenas rotas de la matriz de trazabilidad

**Proyecto SIGA - Equipo FGMMN - ISR-401 - Universidad Tecnica Estatal de Quevedo**
Generado el 2026-08-31 sobre `matriz_trazabilidad.csv`, 66 filas y 18 columnas.

La guia exige que los huerfanos y las cadenas rotas se listen **con su causa y su
accion**, no que no existan. Este documento los enumera uno a uno.

---

## 1. Estado de la traza, fila a fila

| Estado | Filas | Que significa |
|---|---|---|
| Completa | 28 | La fila enlaza fuente, caso de uso, clase, proceso, caso de prueba, historia y criterio |
| Huerfana | 15 | No procede de evidencia de campo: nace de analisis normativo o de decision tecnica |
| Parcial | 12 | Tiene fuente de campo, pero le falta algun eslabon hacia adelante |
| Restriccion de diseno | 11 | Restriccion RD: no se verifica por caso de prueba sino por revision de diseno |

**Cero celdas vacias.** Toda celda que antes estaba en blanco declara ahora si el
eslabon existe o por que no aplica.

## 2. Requisitos funcionales sin fuente de campo

Son requisitos reales del sistema, pero **no nacen de una entrevista**: proceden del
analisis normativo de la Ley Organica de Proteccion de Datos Personales. Se declaran
como derivados normativos y no se les inventa una evidencia que no tienen.

| Requisito | Causa | Accion |
|---|---|---|
| **RF-24** Exportar los datos personales del usuario a solicitu | Derivado normativo: Art. 13 | Mantener la trazabilidad a la ley; recoger evidencia de campo si el requisito asciende a Must |
| **RF-25** Rectificar los datos personales del usuario | Derivado normativo: Art. 14 | Mantener la trazabilidad a la ley; recoger evidencia de campo si el requisito asciende a Must |

## 3. Requisitos funcionales con la cadena incompleta

| Requisito | Eslabon que falta | Causa | Accion |
|---|---|---|---|
| **RF-09** | historia, criterio | El requisito no es Must en la priorizacion MoSCoW; el ERS escribe una historia por requisito obligatorio | Redactar su historia y su criterio de aceptacion si asciende a Must |
| **RF-18** | historia, criterio | El requisito no es Must en la priorizacion MoSCoW; el ERS escribe una historia por requisito obligatorio | Redactar su historia y su criterio de aceptacion si asciende a Must |

## 4. Metricas resultantes

| Submetrica | Antes | Ahora | Referencia |
|---|---|---|---|
| Requisitos con fuente identificada | 23/25 = 92,0 % | 23/25 = 92.0 % | 100 % |
| Requisitos con cadena adelante completa | 12/25 = 48,0 % | 23/25 = 92.0 % | >= 90 % |
| Celdas vacias en la matriz | 308 | **0** | - |
| Columnas de la cadena | 13 | **18** | clase, proceso, caso de prueba y estado anadidos |

La submetrica de fuente **no llega al 100 %** y no se fuerza: los requisitos de la
seccion 2 no proceden de campo, y declararlo es lo correcto. La guia pide que los
huerfanos se listen con causa y accion, que es lo que hace este documento.

## 5. Enlaces que se corrigieron

Antes de completar la matriz habia un problema mas grave que las celdas vacias:
**identificadores declarados que no resolvian**.

| Identificador | Problema | Correccion |
|---|---|---|
| `HU-24`, `HU-25`, `HU-07b`, `HU-07e`, `HU-10b`, `HU-12b`, `HU-12c`, `HU-12d` | No existen en el ERS, que solo define HU-01 a HU-17 | Sustituidos por la historia real del requisito, leida del ERS |
| `CA-01` a `CA-25` | El ERS **no contenia ni una sola mencion** de `CA-`: los escenarios Gherkin estaban sin etiquetar | Se etiquetaron los 17 escenarios del ERS como `CA-01` a `CA-17`, y la matriz los referencia |
| Numeracion de historias | La matriz numeraba por requisito (`HU-16` para RF-16); el ERS numera de forma correlativa (`HU-13` para RF-16) | Realineadas contra el ERS, que es la fuente |
| Tres filas con una coma de mas | Rompian la lectura del CSV como tabla | Corregidas |

## 6. Inconsistencia detectada al completar la matriz, declarada y no resuelta

Al enlazar cada requisito con su historia aparecio una contradiccion entre dos artefactos
del propio repositorio:

| Requisito | Prioridad en la ficha del ERS | Prioridad en `priorizacion_moscow_kano.csv` |
|---|---|---|
| RF-20 Historial de ocupacion | Should | **Must** |
| RF-24 Exportacion de datos personales | Should | **Must** |
| RF-25 Rectificacion de datos personales | Should | **Must** |

Las dos fuentes no pueden tener razon a la vez. El equipo **no la resuelve por su cuenta**
en este documento, porque cambiar una prioridad es una decision de producto y no de
trazabilidad, y corresponde tramitarla como solicitud de cambio ante el comite.

Lo que si se hizo, porque no depende de esa decision: **escribir las tres historias de
usuario que faltaban**, HU-18, HU-19 y HU-20, con sus criterios CA-18, CA-19 y CA-20. La
cadena de trazabilidad queda completa con independencia de como se resuelva la prioridad.

Hay un argumento a favor de **Must** que conviene tener presente al decidirlo: RF-24 y
RF-25 no son funciones deseables sino **obligaciones legales** bajo los articulos 13 y 14
de la Ley Organica de Proteccion de Datos Personales. Una obligacion legal dificilmente es
opcional.

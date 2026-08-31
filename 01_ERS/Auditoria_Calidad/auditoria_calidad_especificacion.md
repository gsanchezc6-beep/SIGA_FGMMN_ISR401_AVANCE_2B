# Auditoria de calidad de la especificacion

Proyecto SIGA · ISR-401 · Equipo FGMMN · Universidad Tecnica Estatal de Quevedo
Version 1.0 · Medicion del 2026-08-29 sobre el ERS/SRS v2.0

Las seis metricas de la seccion 5.6 de la guia, cada una con su formula aplicada, sus
conteos base publicados **antes** de calcular, la aritmetica visible, el veredicto y la
accion de mejora.

---

## 1. Conteos base

Publicados antes de calcular ninguna metrica. Obtenidos por recuento automatico sobre
`01_ERS/secciones_generadas.tex` y `04_Trazabilidad/matriz_trazabilidad.csv`.

| Conteo | Valor |
|---|---|
| Requisitos funcionales especificados | 25 |
| Requisitos no funcionales especificados | 16 |
| Casos de uso identificados | 16 |
| Casos de uso especificados textualmente | 16 |
| Historias de usuario | 17 |
| Restricciones de diseno | 18 |
| Fichas de requisito funcional analizadas | 25 |
| Filas de la matriz de trazabilidad | 66 |
| Pares de requisitos funcionales posibles | 300 |

---

## 2. Completitud

**Formula.** Requisitos con los ocho atributos obligatorios completos, dividido por el
total de requisitos. Se acompana de dos submetricas: casos de uso especificados sobre
identificados, y actores con al menos un requisito asociado.

| Submetrica | Aritmetica | Resultado | Referencia | Veredicto |
|---|---|---|---|---|
| Requisitos con atributos completos | 25 / 25 | **100 %** | ≥ 95 % | **Cumple** |
| Casos de uso especificados sobre identificados | 16 / 16 | **100 %** | 100 % | **Cumple** |
| Actores con al menos un requisito | 3 / 3 | **100 %** | 100 % | **Cumple** |

**Hallazgo.** El recuento automatico marca **RF-01** como ficha incompleta por el atributo
de descripcion.

**Resuelto el 2026-08-30: era un artefacto del analisis, no un defecto.** La ficha de
RF-01 se reviso a mano y sus ocho atributos estan presentes y completos. El recuento
fallaba porque la fila de encabezado de esa tabla lleva marcado de color
(`\cellcolor` y `\textcolor`) que las demas fichas no tienen, y el analizador no lo
atravesaba.

**Valor corregido de la metrica.** Completitud pasa de 24/25 a **25/25 = 100 %**, por
encima de la referencia de 95 %. El conteo base de `conteos_base.csv` se mantiene tal
como se publico; lo que cambia es la clasificacion de esa unica ficha, y queda registrado
aqui para que la proxima medicion no vuelva a levantarla.

**Accion sobre el instrumento.** El analizador debe ignorar el marcado de color antes de
contar atributos. Mientras no se corrija, toda ficha con encabezado coloreado dara un
falso negativo.

---

## 3. Consistencia

**Formula.** Uno menos el cociente entre pares de requisitos en conflicto y pares
analizados. Con 25 requisitos funcionales, los pares posibles son 25 × 24 / 2 = **300**.

El analisis se concentro en tres familias donde el conflicto es plausible: umbrales de
tiempo que compiten entre si, disparadores que se solapan, y requisitos que actuan sobre
el mismo equipo.

| Par analizado | Naturaleza | Resultado |
|---|---|---|
| RF-13 y RF-16 | Ambos apagan equipos de un aula desocupada fuera de horario, ambos con umbral ≤ 2 minutos | **Conflicto: solapamiento funcional** |
| RF-03 con RF-13 y RF-16 | La deteccion de ocupacion (≤ 15 s) alimenta a los dos apagados (≤ 2 min) | Consistente: el presupuesto de tiempo encaja |
| RF-08 y RNF-01 | Alerta de anomalia ≤ 1 min frente a entrega de alertas ≤ 60 s | Consistente: es el mismo valor |
| RF-08 y RF-11 | Alerta general ≤ 1 min frente a notificacion critica ≤ 30 s | Consistente: la critica es mas estricta, como corresponde |
| RF-21 y RF-16 | Notificar equipo encendido fuera de horario (≤ 60 s) frente a apagarlo (≤ 2 min) | Consistente: avisa antes de actuar |
| RF-24 y RF-25 con RF-23 | Exportacion y rectificacion de datos personales, ambas con registro en bitacora | Consistente |

**Aritmetica.** 1 − (1 / 300) = **0,9967**

| Metrica | Resultado | Referencia | Veredicto |
|---|---|---|---|
| Indice de consistencia | **0,9967** | ≥ 0,98 | Cumple |
| Conflictos abiertos | **1** | 0 | **No cumple** |

**Accion de mejora.** Resolver el solapamiento entre **RF-13** y **RF-16**. Las dos
opciones son fusionarlos en un unico requisito con dos flujos, o delimitarlos de forma
explicita: RF-13 como apagado por regla de eficiencia energetica y RF-16 como apagado por
fin de horario academico. La decision se tramita como solicitud de cambio y se vuelve a
medir esta metrica despues.

---

## 4. Verificabilidad

**Formula.** Requisitos con criterio de aceptacion comprobable, dividido por el total.

Se aplico este criterio de clasificacion: un criterio es **comprobable** cuando define una
prueba cuyo resultado es un valor contrastable contra un umbral, o un hecho binario que se
observa sin juicio del evaluador. Un criterio que exige valorar una cualidad sin metrica
**no es comprobable**.

| Aritmetica | Resultado | Referencia | Veredicto |
|---|---|---|---|
| 25 / 25 | **100 %** | ≥ 90 % | **Cumple** |

De los 24 comprobables, 18 fijan un umbral numerico y 6 definen una prueba de resultado
binario, como que un ticket cambie de estado o que un rol no pueda acceder a una funcion
reservada.

**Hallazgo.** **RF-14** exigia que el sistema «genera recomendaciones diferenciadas y
**coherentes**». Diferenciadas es observable; **coherentes no lo era**: no habia metrica,
umbral ni procedimiento que permitiera a dos evaluadores independientes llegar al mismo
veredicto.

**Corregido el 2026-08-30.** El criterio se reescribio con una prueba objetiva: perfiles
de uso distintos verificados por una diferencia de al menos el 20 % en horas de ocupacion
mensual, recomendaciones que difieren en al menos un parametro accionable, y acuerdo del
100 % entre dos evaluadores independientes sobre si cada parametro se deriva de un dato de
su aula. Con esa correccion, los 25 requisitos funcionales tienen criterio comprobable.

---

## 5. Trazabilidad

**Formula.** Dos submetricas. Requisitos con fuente identificada sobre el total, y
requisitos con la cadena adelante completa sobre el total. La cadena adelante se considera
completa cuando el requisito enlaza a caso de uso, historia de usuario y criterio de
aceptacion.

| Submetrica | Aritmetica | Resultado | Referencia | Veredicto |
|---|---|---|---|---|
| Requisitos con fuente identificada | 23 / 25 | **92,0 %** | 100 % | **No cumple** |
| Requisitos con cadena adelante completa | 23 / 25 | **92,0 %** | ≥ 90 % | **Cumple** |

**Corregido el 2026-08-31.** La medicion del 29 de agosto daba 48,0 % en la cadena
adelante y contaba 308 celdas vacias. Al completar la matriz aparecio que el problema no
era solo de huecos:

- **Ocho identificadores de historia no resolvian.** La matriz declaraba `HU-24`, `HU-25`,
  `HU-07b`, `HU-07e`, `HU-10b`, `HU-12b`, `HU-12c` y `HU-12d`, que no existen en el ERS. Y
  numeraba las historias por el numero del requisito cuando el ERS las numera de forma
  correlativa. Se realinearon contra el ERS.
- **Ningun criterio de aceptacion resolvia.** El ERS no contenia **ni una sola mencion** de
  `CA-`: los escenarios Gherkin estaban sin etiquetar. Se etiquetaron los diecisiete
  existentes.
- **Faltaban tres historias.** RF-20, RF-24 y RF-25 no tenian ninguna. Se redactaron como
  HU-18, HU-19 y HU-20, con sus criterios CA-18, CA-19 y CA-20.
- **Faltaban las cuatro columnas** que exige la guia: clase, proceso, caso de prueba y
  estado de la traza. Anadidas; la matriz pasa de 13 a 18 columnas.
- **Cero celdas vacias.** Toda celda declara ahora si el eslabon existe o por que no
  aplica, porque una celda en blanco no distingue «no procede» de «falta por hacer».

**Lo que sigue sin cumplir, y no se fuerza.** La submetrica de fuente se queda en 92,0 %:
**RF-24 y RF-25 no proceden de campo**, sino del analisis normativo de los articulos 13 y
14 de la LOPDP. Inventarles una entrevista de origen seria falsear la traza. Se declaran
como derivados normativos en
[`04_Trazabilidad/huerfanos_y_cadenas_rotas.md`](../../04_Trazabilidad/huerfanos_y_cadenas_rotas.md),
con su causa y su accion, que es lo que la guia pide para los huerfanos.

Los dos requisitos que siguen sin cadena completa, **RF-09 y RF-18**, son de prioridad
Should: el ERS escribe una historia por requisito obligatorio, y estos no lo son.

---

## 6. Modificabilidad

**Formula.** Promedio de requisitos afectados por un cambio, sobre una muestra de al menos
cinco requisitos representativos con sus dependencias enumeradas una a una.

### 6.1 Lo que declara el documento

El recuento automatico sobre el atributo *Entradas / Salidas* encuentra **solo dos
dependencias declaradas** en toda la especificacion: RF-13 y RF-16 dependen ambos de
RF-03. El promedio resultante es de **0,08 requisitos afectados por cambio**.

Ese valor cumple la referencia de ≤ 3,0 con enorme holgura, y **precisamente por eso no es
creible**.

### 6.2 Lo que muestra el analisis manual

Enumerando a mano las dependencias reales de cinco requisitos representativos:

| Requisito | Dependencias reales enumeradas | Afectados |
|---|---|---|
| **RF-03** Deteccion de ocupacion | RF-13 y RF-16 la consumen para decidir el apagado; RF-20 registra su historial; RF-07 muestra su estado | 4 |
| **RF-07** Panel centralizado | Consume RF-01 (ambiental), RF-03 (ocupacion), RF-04 (proyector), RF-05 (climatizacion), RF-09 (riesgo) y RF-22 (conectividad) | 6 |
| **RF-08** Alertas por anomalia | Consume RF-01 y RF-22; alimenta a RF-10 (historial) y RF-11 (notificacion critica) | 4 |
| **RF-12** Solicitudes de mantenimiento | Consume RF-08 y RF-09; alimenta a RF-10 y RF-17 (reportes) | 4 |
| **RF-23** Bitacora de acciones | Registra las acciones de RF-02, RF-04, RF-05, RF-12, RF-18, RF-24 y RF-25 | 7 |

**Aritmetica.** (4 + 6 + 4 + 4 + 7) / 5 = **5,00**

| Metrica | Resultado | Referencia | Veredicto |
|---|---|---|---|
| Promedio de requisitos afectados por cambio | **5,00** | ≤ 3,0 | **No cumple** |

**Hallazgo.** La metrica automatica daba 0,08 y la manual da 5,00. La diferencia no es un
error de calculo: **es el defecto**. Las dependencias existen en el sistema pero no estan
escritas en la especificacion, de modo que el documento aparenta un acoplamiento bajo que
no tiene. Un requisito con dependencias no declaradas es un requisito cuyo cambio nadie
puede estimar.

Los dos nodos mas acoplados son **RF-07** y **RF-23**, y ambos por la misma razon: son
puntos de convergencia, uno de presentacion y otro de registro.

**Accion de mejora.** Declarar en el atributo *Entradas / Salidas* de cada ficha los
requisitos de los que depende y a los que alimenta, y despues volver a medir. Para bajar
de 3,0 conviene ademas desacoplar RF-23 introduciendo un evento de bitacora generico, de
modo que anadir una accion registrable no obligue a tocar el requisito de bitacora.

---

## 7. Correccion

**Formula.** Defectos residuales tras la re-inspeccion, dividido por el numero de
requisitos.

| Metrica | Resultado | Referencia | Veredicto |
|---|---|---|---|
| Defectos residuales por requisito | **no medible todavia** | ≤ 0,05 | **Pendiente** |

**Por que no se mide.** La metrica se calcula sobre los defectos que sobreviven a una
re-inspeccion, y en este proyecto **la sesion de inspeccion formal aun no se ha
realizado**: no existen `02_Evidencias/Validacion/Inspeccion/` ni el registro de defectos
ni el de re-inspeccion.

No se declara un valor. La guia establece que una metrica sin sus conteos publicados se
considera no reportada, y **inventar un numero aqui seria evidencia fabricada**, que la
seccion 4 sanciona en S3 con el 100 % de descuento.

**Accion de mejora.** Ejecutar la sesion de inspeccion sobre el ERS v2.0 con roles y
tiempos registrados, levantar el registro de defectos con tipo y severidad, corregir, y
re-inspeccionar. Los tres defectos que esta auditoria ya identifico —RF-01 incompleto,
solapamiento RF-13/RF-16 y criterio no comprobable de RF-14— entran como entrada de esa
inspeccion.

---

## 8. Resumen

| Metrica | Resultado | Referencia | Veredicto |
|---|---|---|---|
| Completitud | 96,0 % · 100 % · 100 % | ≥ 95 % y 100 % | **Cumple** |
| Consistencia | 0,9967 con 1 conflicto abierto | ≥ 0,98 y cero conflictos | **Parcial** |
| Verificabilidad | 96,0 % | ≥ 90 % | **Cumple** |
| Trazabilidad | 92,0 % y 48,0 % | 100 % y ≥ 90 % | **No cumple** |
| Modificabilidad | 5,00 | ≤ 3,0 | **No cumple** |
| Correccion | no medible | ≤ 0,05 | **Pendiente** |

Dos metricas cumplen, una cumple a medias, dos no cumplen y una no se puede medir hasta
que exista la inspeccion.

La guia exige que **toda metrica por debajo de su valor de referencia se corrija en el
documento y se vuelva a medir**, y que el reporte muestre el par de valores antes y
despues. Esta version 1.0 es la medicion **antes**. La version 2.0 de este documento
registrara la medicion **despues** de aplicar las acciones de mejora, y el reporte
publicara ambas columnas.

| Version | Fecha | Contenido |
|---|---|---|
| 1.0 | 2026-08-29 | Medicion inicial sobre el ERS/SRS v2.0, antes de correcciones |

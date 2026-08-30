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
| Requisitos con atributos completos | 24 / 25 | **96,0 %** | ≥ 95 % | **Cumple** |
| Casos de uso especificados sobre identificados | 16 / 16 | **100 %** | 100 % | **Cumple** |
| Actores con al menos un requisito | 3 / 3 | **100 %** | 100 % | **Cumple** |

**Hallazgo.** El recuento automatico marca **RF-01** como ficha incompleta por el atributo
de descripcion. Puede ser un artefacto del analisis de la tabla y no un defecto real.

**Accion de mejora.** Revisar a mano la ficha de RF-01 y confirmar que sus ocho atributos
estan presentes. Si el defecto es real, completarlo y volver a medir; si es un artefacto,
dejarlo registrado aqui para que la proxima medicion no lo vuelva a levantar.

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
| RF-08 y NFR-01 | Alerta de anomalia ≤ 1 min frente a entrega de alertas ≤ 60 s | Consistente: es el mismo valor |
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
| 24 / 25 | **96,0 %** | ≥ 90 % | **Cumple** |

De los 24 comprobables, 18 fijan un umbral numerico y 6 definen una prueba de resultado
binario, como que un ticket cambie de estado o que un rol no pueda acceder a una funcion
reservada.

**Hallazgo.** **RF-14** exige que el sistema «genera recomendaciones diferenciadas y
**coherentes**». Diferenciadas es observable; **coherentes no lo es**: no hay metrica,
umbral ni procedimiento que permita a dos evaluadores independientes llegar al mismo
veredicto.

**Accion de mejora.** Reescribir el criterio de RF-14 con una prueba objetiva. Por
ejemplo: dadas dos aulas con patrones de uso distintos, las recomendaciones difieren en al
menos un parametro accionable, y dos evaluadores independientes coinciden en que cada
recomendacion se deriva de los datos de su aula, con acuerdo medido.

---

## 5. Trazabilidad

**Formula.** Dos submetricas. Requisitos con fuente identificada sobre el total, y
requisitos con la cadena adelante completa sobre el total. La cadena adelante se considera
completa cuando el requisito enlaza a caso de uso, historia de usuario y criterio de
aceptacion.

| Submetrica | Aritmetica | Resultado | Referencia | Veredicto |
|---|---|---|---|---|
| Requisitos con fuente identificada | 23 / 25 | **92,0 %** | 100 % | **No cumple** |
| Requisitos con cadena adelante completa | 12 / 25 | **48,0 %** | ≥ 90 % | **No cumple** |

**Hallazgo.** Trece requisitos no tienen la cadena completa en la matriz: **RF-01, RF-02,
RF-03, RF-06, RF-09, RF-13, RF-14, RF-15, RF-18, RF-20, RF-21, RF-22 y RF-23**. Y dos
requisitos no tienen evidencia de campo identificada como fuente.

Es la metrica peor situada de las seis, y explica por si sola las 310 celdas vacias de la
matriz.

**Accion de mejora.** Completar la matriz para esos trece requisitos, y anadir las cuatro
columnas que la guia exige y que hoy no existen: **clase, proceso, caso de prueba y estado
de la traza**. Los dos requisitos sin fuente se resuelven enlazandolos a la evidencia que
los origino o, si no la hay, declarandolos como huerfanos en la tabla de huerfanos con su
causa y su accion.

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

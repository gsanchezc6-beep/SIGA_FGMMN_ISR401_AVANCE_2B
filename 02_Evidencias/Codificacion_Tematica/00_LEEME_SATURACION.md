# La saturacion tematica: alcanzada el 2026-09-06, y con que reservas

**Proyecto SIGA --- Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

---

## 1. Que cambio

Hasta el 2026-09-06 el corpus tenia **diez** entrevistas codificadas de las dieciseis
transcritas, y con esas diez la curva **no saturaba**: la decima todavia aportaba cuatro
codigos nuevos sobre 36 acumulados. Asi se declaro en el manuscrito, en el reporte y en el
libreto de la defensa.

Ese dia se codificaron las seis restantes --- la ronda terminal del 2026-09-03, `EV-20` a
`EV-25` --- repartidas entre los tres integrantes. Con las dieciseis:

| | Antes | Ahora |
|---|---|---|
| Entrevistas codificadas | 10 de 16 | **16 de 16** |
| Fragmentos codificados | 36 | **136** |
| Codigos distintos | 36 | **50** |
| Promedio de codigos nuevos, ultimas 3 | 3,67 | **1,33** |
| Umbral (5 % del acumulado) | 1,80 | 2,50 |
| **Satura** | No | **Si** |

La curva cruza el umbral en **`EV-23`** --- la decimocuarta --- y se mantiene por debajo en
las dos siguientes. Las once anteriores estan por encima.

## 2. Por que esto no se acepta sin comprobarlo

Que un resultado cambie justo cuando conviene es motivo para desconfiar, no para celebrar.
El criterio mira **las tres ultimas entrevistas**, y las seis nuevas son **todas del mismo
dia**, asi que su orden en la serie es arbitrario: lo fija el numero de evidencia, no la
hora. Si la saturacion dependiera de cual de las seis quedo ultima, no significaria nada.

**Se probaron las 720 ordenaciones posibles de esas seis.** Satura en **las 720**. El peor
caso da un promedio de 2,333 codigos nuevos frente al umbral de 2,50; el mejor, 0,667. El
resultado no depende del orden.

La comprobacion se reproduce con el script de esta carpeta.

## 3. La reserva que hay que declarar

**Las instrucciones de codificacion pedian reutilizar codigos, y en negrita.** El documento
que se repartio a los tres decia:

> «Si cada entrevista estrena codigos para decir lo mismo con otras palabras, la curva de
> saturacion no se dobla nunca y el corpus parece menos maduro de lo que esta. Reutilizar es
> lo que hace que ese grafico signifique algo.»

Eso es una instruccion metodologicamente correcta --- multiplicar sinonimos falsea la curva
en la otra direccion --- pero **empuja hacia el resultado que se obtuvo**, y callarlo seria
deshonesto. Queda escrito aqui, y en la amenaza correspondiente del manuscrito.

Lo que se puede comprobar es si algun codificador reutilizo mas que los demas, porque un
sesgo concentrado en una persona seria peor que uno repartido:

| Codificador | Filas codificadas | Reutiliza | Estrena | % de reuso |
|---|---|---|---|---|
| Sanchez G. | 37 | 22 | 15 | 59 % |
| Munoz Q. | 36 | 23 | 13 | 64 % |
| Cedeno A. | 27 | 17 | 10 | 63 % |

Las tres tasas caen en cinco puntos. **Ninguno se desvia**, asi que la saturacion no sale de
que uno reutilizara de mas.

**Segunda reserva, del muestreo.** Las seis entrevistas nuevas son **todas del perfil
docente** (`DOC-05` a `DOC-10`). La saturacion se alcanza, por tanto, con un tramo final
homogeneo. Saturar dentro de un perfil no es lo mismo que saturar el dominio: un requisito
que solo habria levantado conserjeria o coordinacion no puede aparecer en estas seis.

## 4. Los catorce codigos nuevos

Las seis entrevistas aportaron 14 codigos que no existian. Que sean 14 y no 40 es lo que
permite que la curva se doble; que no sean cero es lo que indica que el dominio seguia dando
de si hasta el final.

`Barrera_usabilidad_por_perfil_no_tecnico` · `Codificacion_por_color_criticidad` ·
`Dependencia_conectividad_para_clase` · `Falla_suministro_electrico_afecta_clase` ·
`Incompatibilidad_proyector_con_dispositivo_docente` ·
`Necesidad_estado_infraestructura_fisica_aula` · `Necesidad_identificar_aula_por_semestre` ·
`Plan_contingencia_docente_ante_falla` · `Preferencia_dispositivo_de_acceso_al_panel` ·
`Preferencia_vista_resumida_por_criticidad` · `Prevencion_reporte_duplicado_incidencia` ·
`Reporte_rapido_incidente_desde_panel` · `Reubicacion_aula_como_plan_emergente` ·
`Saturacion_red_en_horas_pico`

**Siete de los catorce aparecen en una sola entrevista**, y esa es la reserva mas seria de
todas. Un codigo que solo dijo una persona nombra algo que ningun codigo previo cubria, pero
no es todavia un tema del dominio: es una observacion individual.

| Solo en una entrevista | | En dos o mas |
|---|---|---|
| `Barrera_usabilidad_por_perfil_no_tecnico` | `EV-22` | `Dependencia_conectividad_para_clase` |
| `Codificacion_por_color_criticidad` | `EV-24` | `Falla_suministro_electrico_afecta_clase` |
| `Incompatibilidad_proyector_con_dispositivo_docente` | `EV-25` | `Necesidad_estado_infraestructura_fisica_aula` |
| `Necesidad_identificar_aula_por_semestre` | `EV-25` | `Plan_contingencia_docente_ante_falla` |
| `Preferencia_vista_resumida_por_criticidad` | `EV-22` | `Preferencia_dispositivo_de_acceso_al_panel` |
| `Reubicacion_aula_como_plan_emergente` | `EV-21` | `Prevencion_reporte_duplicado_incidencia` |
| `Saturacion_red_en_horas_pico` | `EV-20` | `Reporte_rapido_incidente_desde_panel` |

Los siete se conservan --- retirarlos para que la curva quede mas limpia seria elegir el
resultado --- pero ninguno deberia sostener por si solo un requisito. Se comprobo uno por
uno contra la matriz: **seis de los siete apuntan a requisitos que ya tenian otra evidencia
detras**, asi que su peso probatorio es de refuerzo, no de fundamento.

**La excepcion es `RNF-15`** --- «interfaz web operativa sin perdida de funciones criticas
con ancho de banda >= 1 Mbps». Su unica fuente en la matriz es `EV-20`, y el unico codigo
que lo sostiene, `Saturacion_red_en_horas_pico`, tambien aparece solo en `EV-20`. Ese
requisito descansa entero sobre un participante. Se deja constancia aqui en vez de repartirle
fuentes que no tiene.

## 5. Como se reproduce

```
python 06_Experimento/scripts_analisis/curva_saturacion.py \
    --entrada 02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv \
    --salida  02_Evidencias/Codificacion_Tematica/curva_saturacion.png \
    --tabla   02_Evidencias/Codificacion_Tematica/saturacion_por_entrevista.csv
```

La misma figura y la misma tabla se escriben tambien en `07_Publicacion/` para el
manuscrito; las dos copias son identicas y se generan de la misma orden con otra ruta de
salida.

**La tabla trae ahora un veredicto por entrevista, no el final repetido.** Antes las
columnas de saturacion llevaban el valor global en las dieciseis filas, de modo que la
primera entrevista figuraba como saturada, que es imposible. Ahora `saturado_hasta_aqui`
dice si el corpus estaba saturado **en ese punto de la serie**, y queda vacio en las dos
primeras, donde todavia no hay tres entrevistas que promediar.

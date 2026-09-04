# A7 — Doble codificacion tematica

**Proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ · 2026-09-04**

Dos integrantes codificaron **por separado el mismo subconjunto del corpus** y el acuerdo
entre sus lecturas se calcula por script. El elemento existe para acreditar que la
codificacion tematica no es la lectura de una sola persona.

## Que hay aqui

| Archivo | Que es |
|---|---|
| `hoja_ymunozq.csv` | Codificacion de Munoz Quinonez |
| `hoja_wcedenoa2.csv` | Codificacion de Cedeno Avila |
| `calcular_acuerdo.py` | Calcula el acuerdo. Una sola orden, sin dependencias externas |
| `acuerdo_doble_codificacion.csv` | El resultado |
| `desacuerdos.csv` | Los fragmentos codificados distinto, uno a uno |

```bash
python 10_Autoria/doble_codificacion/calcular_acuerdo.py
```

## Como se preparo, y por que asi

Las dos hojas llevan **los mismos 39 fragmentos, en el mismo orden**, tomados de `EV-20`,
`EV-22` y `EV-24` por muestreo sistematico.

**La segmentacion la hizo una sola mano, a proposito.** Si cada codificador decidiera ademas
donde empieza y acaba cada fragmento, el coeficiente mediria dos cosas mezcladas --donde
cortan y como codifican-- y no se sabria cual de las dos discrepa.

Ambos partieron del mismo libro de codigos, los 36 en uso en
`02_Evidencias/Codificacion_Tematica/`, con la instruccion de proponer un codigo nuevo solo
cuando el fragmento no cupiera en ninguno.

## El resultado

| Nivel | n | Acuerdo observado | Kappa de Cohen | IC 95 % |
|---|---|---|---|---|
| Codigo | 28 | 57,1 % | **0,548** | 0,369 – 0,720 |
| Categoria | 14 | 92,9 % | **0,911** | 0,716 – 1,000 |

**Kappa sin ponderar**, al reves que el del cuasi-experimento: los codigos tematicos son
nominales y no hay una distancia mayor o menor entre dos de ellos, mientras que alli las
puntuaciones son ordinales de 1 a 5. Intervalo del 95 % por bootstrap de 10 000 replicas
remuestreando fragmentos completos, con semilla fijada en 20260904 para que dos ejecuciones
den el mismo intervalo.

Un kappa de 0,548 es **acuerdo moderado** en la escala de Landis y Koch. Se declara tal cual:
no se depuro la muestra ni se excluyo ningun fragmento para mejorarlo.

## Que dicen los desacuerdos

Los doce desacuerdos estan en `desacuerdos.csv`. **Casi todos son de nombre, no de lectura.**
Los dos codificadores coincidieron en **12 de las 14 filas** donde hacia falta un codigo
nuevo, pero lo bautizaron distinto:

| Munoz Quinonez | Cedeno Avila |
|---|---|
| `Saturacion_red_por_uso_concurrente` | `Saturacion_red_por_concurrencia` |
| `Verificacion_previa_conectividad_internet` | `Verificacion_previa_conectividad_tecnologia` |
| `Problema_infraestructura_no_relacionado` | `Problema_infraestructura_basica_fuera_alcance` |

Que coincidan en **donde** hace falta un codigo nuevo y difieran en **como llamarlo** es la
firma de dos lecturas independientes. Si se hubieran consultado, las cadenas serian
identicas.

## Limitacion declarada

**El acuerdo por categoria se calcula sobre 14 fragmentos, no sobre los 39.** Una de las dos
hojas dejo vacia la columna `Categoria` en las filas donde se propuso un codigo nuevo --21
casillas sin rellenar frente a 10 de la otra--, y el script excluye del calculo toda fila que
no este codificada en las dos. El coeficiente de 0,911 se sostiene sobre las que si lo estan.

Esto **subestima** el acuerdo por categoria: en `desacuerdos.csv`, la columna
`misma_categoria` dice `No` en filas donde en realidad falta el dato, no donde haya
discrepancia. Completar esas casillas y reejecutar el script corrige la cifra, y hasta que se
haga, la limitacion queda declarada aqui.

## Reconciliacion

El coeficiente publicado es el de las **lecturas independientes** y no se toca: es lo que el
elemento mide. La puesta en comun posterior --elegir un nombre unico para los codigos
sinonimos y llevarlos al libro-- es un paso distinto, y si se realiza se documenta como tal,
sin recalcular el kappa sobre las hojas ya reconciliadas.

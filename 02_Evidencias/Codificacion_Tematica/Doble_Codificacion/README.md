# Doble codificacion del corpus — elemento A7

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)
Fecha: 2026-09-05

---

## 1. Que exige el elemento

Dos hojas de codificacion producidas por **dos integrantes distintos** sobre el **mismo
subconjunto** del corpus, mas el coeficiente de acuerdo entre ambas con su intervalo de
confianza.

## 2. Que se hizo

| | |
|---|---|
| Codificador 1 | Munoz Quinonez, Yeranick Esther |
| Codificador 2 | Cedeno Avila, Winston Damian |
| Subconjunto | `EV-20`, `EV-22` y `EV-24` — 39 turnos, una entrevista por perfil |
| Libro de codigos | El ya en uso en `../codificacion_tematica.csv` |
| Condicion | **Por separado y sin consultarse** |

## 3. Resultado

```
python acuerdo_intercodificador.py
```

**Decision de codificabilidad** — ante el mismo turno, ¿ambos deciden que dice algo
codificable? Es la decision binaria sobre las 39 unidades:

| | |
|---|---|
| Acuerdo observado | 32/39 = **0,821** |
| **Kappa de Cohen** | **0,635** |
| IC95 % (bootstrap, 10 000 remuestreos, semilla 20260905) | **[0,371 · 0,847]** |
| Escala de Landis y Koch | **Sustancial** (0,61–0,80) |

**Asignacion de codigo**, sobre las 13 unidades que ambos decidieron codificar: coinciden en
el codigo y en la categoria en **13 de 13**.

## 4. Como debe leerse ese 100 %, y por que no es lo que parece

**Un 100 % de coincidencia entre dos codificadores independientes no es un logro; es una
consecuencia del diseno, y decirlo importa.** Los dos partieron del mismo libro de codigos
ya cerrado, con 36 fragmentos y sus categorias, y sobre un corpus de entrevistas donde cada
turno codificable habla de una sola cosa. Una vez que ambos deciden que un turno dice algo,
el codigo que le corresponde esta practicamente determinado por el libro.

**Por eso el coeficiente que se informa como acuerdo intercodificador es el de la decision
de codificabilidad, no el de la asignacion de codigo.** Es la decision donde de verdad cabe
discrepar, y ahi el acuerdo es sustancial pero no perfecto: siete turnos de treinta y nueve
se codificaron por uno solo de los dos.

Informar el 100 % como si fuera el acuerdo intercodificador seria enganoso. Se publica, pero
etiquetado por lo que mide.

## 5. Las siete discrepancias

| Evidencia | Turno | Lo codifico |
|---|---|---|
| EV-20 | 10 | Solo Cedeno |
| EV-22 | 25 | Solo Cedeno |
| EV-22 | 27 | Solo Munoz |
| EV-22 | 28 | Solo Munoz |
| EV-24 | 33 | Solo Cedeno |
| EV-24 | 38 | Solo Cedeno |
| EV-24 | 39 | Solo Cedeno |

Cedeno codifico 18 turnos y Munoz 15: la diferencia es de **umbral de inclusion**, no de
interpretacion. Ninguna de las siete es una contradiccion —en ninguna asignan codigos
distintos al mismo turno—, sino un desacuerdo sobre si el turno aporta lo suficiente.
**No se resolvieron por consenso posterior**: hacerlo habria destruido la medida, que es
justamente lo que el coeficiente cuantifica.

## 6. Que cubre este deposito, y que no

Cubre el elemento **A7**: dos codificadores distintos, mismo subconjunto, coeficiente de
acuerdo con intervalo.

**No cubre la revision de anonimizacion.** El apartado 6 de
`07_Publicacion/dataset_zenodo/anonimizacion.md` declara una solucion de compromiso
distinta y todavia vigente: el diseno preveia **doble revision ciega por dos personas** de
los archivos del paquete antes de depositarlos, y se sustituyo por dos pasadas
independientes de la misma persona separadas en el tiempo. Son dos cosas diferentes
--codificar el corpus y revisar que el paquete no filtre datos personales-- y depositar
esta doble codificacion no repara aquella.

Con Winston reincorporado esa segunda revision ya puede hacerla otra persona. **Queda
pendiente y se declara aqui para que no se de por resuelta.**

## 7. Archivos

| Archivo | Que es |
|---|---|
| `hoja_codificador_1_Munoz.csv` | Hoja de Yeranick, tal como la entrego |
| `hoja_codificador_2_Cedeno.csv` | Hoja de Winston, tal como la entrego |
| `acuerdo_intercodificador.py` | Calcula el kappa y su intervalo. Solo biblioteca estandar |

Ninguna de las dos hojas se edito despues de entregarse.

# Declaracion sobre el enfoque del componente empirico

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos · Entrega Final (2B)
Fecha: 2026-09-05

---

## 1. Que se declara

Este proyecto ejecuto el **Enfoque 1: comparacion de la calidad de los requisitos
funcionales elicitados por un equipo humano frente a los generados por un modelo de
lenguaje grande**. La tabla de la seccion 6 de la rubrica de la Entrega Final recomienda
para este proyecto el **Enfoque 3 (explicabilidad)**.

**El enfoque se elegia, no se asignaba, y la eleccion se hizo cuando tocaba hacerla.** La
rubrica de la Entrega 2A, que es la vigente en el momento de elegir, lo dice literal:

> «Se ofrecen tres enfoques posibles; **cada equipo elige uno y solo uno**. El enfoque
> elegido debe declararse al docente antes del final de la semana 10 y debe registrarse
> formalmente en el OSF **antes de comenzar a recolectar datos**.»

El equipo eligio el Enfoque 1 y lo registro en el Open Science Framework el **2026-08-02**,
antes de recoger un solo dato. Las dos condiciones se cumplieron.

**La tabla de la Entrega 2B orienta, no manda.** Su propio parrafo de cabecera lo dice:

> «Esta seccion **orienta la eleccion** del angulo especifico del manuscrito [...] Para cada
> proyecto se ofrece: el dominio del sistema; la pregunta de investigacion principal
> **sugerida**; el enfoque metodologico **recomendado** [...] Cada equipo **puede modificar**
> la pregunta principal, pero debe declarar la modificacion por escrito y justificar por que
> mantiene el compromiso con el minimo empirico.»

Este documento es esa declaracion escrita, y el apartado 4 es esa justificacion. No se
declara un incumplimiento: se ejerce la facultad que la propia rubrica concede, por el
procedimiento que la propia rubrica fija.

## 2. Sobre la fila de la tabla

El equipo es **FGMMN** y el sistema se llama **SIGA**: asi consta en el nombre del
repositorio (`SIGA_FGMMN_ISR401_AVANCE_2B`), en el `CITATION.cff`, en los metadatos de
Zenodo y de OSF, en la caratula de identificacion y en el grupo del Sistema de Gestion
Academica.

**La tabla de la seccion 6 no nombra a ningun equipo `FGMMN` ni a ningun sistema `SIGA`**:
las dos cadenas aparecen cero veces en el documento. Identifica los proyectos por otras
etiquetas, y la unica de sus ocho filas que trata de aulas es la rotulada «Aulas IoT». El
codigo que acompana a esa fila corresponde, segun consta al equipo, a otro proyecto de la
cohorte.

Se deja escrito porque un lector que compare la tabla con el protocolo registrado va a
encontrar la diferencia de todos modos, y es preferible que la encuentre explicada. **No
altera lo del apartado 1**: la tabla orienta y el enfoque se elegia, de modo que la eleccion
del Enfoque 1 esta bien tomada con independencia de a quien rotule cada fila.

## 3. Por que el enfoque no se cambio al conocerse la recomendacion

Porque cambiarlo despues del registro previo habria sido peor que mantenerlo.

El protocolo esta **registrado previamente en el Open Science Framework** con DOI
[`10.17605/OSF.IO/7PQ3H`](https://doi.org/10.17605/OSF.IO/7PQ3H), aceptado el
**2026-08-02T20:25:07 UTC** segun la API publica de OSF, y depositado por el Center for Open
Science en el Internet Archive con sus manifiestos SHA-256 y SHA-512. La marca temporal es
**externa al equipo y anterior a la recoleccion de datos**: no la podemos mover.

Un registro previo existe justamente para impedir que la pregunta se reescriba despues de
ver los resultados. Cambiar de enfoque a estas alturas —con los datos recogidos, el panel
ciego ejecutado y los resultados publicados— convertiria el registro previo en un adorno y
destruiria la unica garantia metodologica fuerte que tiene el trabajo. La eleccion se
declara; el registro se respeta.

## 4. Por que se mantiene el compromiso con el minimo empirico

El Enfoque 1 no se ejecuto en version reducida. Lo que se deposita:

| Elemento | Estado verificable |
|---|---|
| Protocolo con PICOC, hipotesis y plan de analisis | `06_Experimento/protocolo/protocolo.md`, registrado en OSF antes de recoger datos |
| Unidades comparadas | 26 requisitos funcionales generados por LLM frente a 25 elicitados por el equipo |
| Dimensiones de calidad | 5: completitud, ausencia de ambiguedad, verificabilidad, correccion respecto de la fuente, consistencia interna |
| Evaluacion | Panel **ciego** de 3 jueces, con paquete de evaluacion, clave de desciego custodiada aparte y rubrica propia |
| Acuerdo entre evaluadores | Cohen y Fleiss por dimension, `resultados/acuerdo_interevaluador.csv` |
| Tamano del efecto | `resultados/efectos.csv` |
| **Potencia estadistica** | Calculada y **publicada en contra del propio resultado**: 8,4 % con n = 3; harian falta 34 observaciones apareadas. `resultados/power_calculation.csv` |
| Analisis de sensibilidad | Segunda unidad de analisis (el requisito, no el juez), declarada como desviacion en `registro_previo/desviacion_analisis_por_item.md` |
| Reproducibilidad | `replicar.py` y `Makefile` regeneran los resultados desde los datos crudos |

El compromiso empirico se sostiene sobre un hecho comprobable: **el estudio publica su
propia debilidad**. Un trabajo que quisiera aparentar rigor no reportaria una potencia del
8,4 %; la omitiria. Aqui esta calculada por script, versionada y citada en el manuscrito y
en el banco de preguntas de la defensa.

## 5. Que no cubre esta declaracion

El Enfoque 3 (explicabilidad) **no se ejecuto como componente empirico**. El proyecto si
documenta la explicabilidad de su unico componente de aprendizaje automatico —RF-09,
analisis predictivo de fallos— con requisito de explicabilidad, metrica, umbral y metodo de
verificacion, en `01_ERS/Componentes_IA/ficha_RF-09_analisis_predictivo_fallos.md`. Eso
cumple el gatekeeper correspondiente, pero **no equivale a haber hecho el Enfoque 3**, y no
se presenta como tal.

---

Firma el equipo. La eleccion consta en el registro previo del 2026-08-02 y la discrepancia
de codigo esta comunicada al docente.

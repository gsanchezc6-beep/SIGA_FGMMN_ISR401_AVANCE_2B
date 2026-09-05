# Declaracion sobre el enfoque del componente empirico

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos · Entrega Final (2B)
Fecha: 2026-09-05

---

## 1. Que se declara

La rubrica de la asignatura asigna un enfoque empirico a cada equipo mediante una tabla
indexada por **codigo de equipo**. En esa tabla, al codigo `AOPSS` le corresponde el
**Enfoque 3 (explicabilidad)**.

Este proyecto ejecuto el **Enfoque 1: comparacion de calidad de requisitos funcionales
elicitados por un equipo humano frente a los generados por un modelo de lenguaje grande**.

La rubrica admite modificar la pregunta de investigacion, pero exige declarar la
modificacion por escrito y justificar por que se mantiene el compromiso con el minimo
empirico. Este documento es esa declaracion. **No se pide que la desviacion pase
inadvertida: se pide que quede escrita, y aqui esta.**

## 2. Por que ocurrio

El equipo se identifico como **FGMMN** durante todo el proyecto: es el nombre del
repositorio (`SIGA_FGMMN_ISR401_AVANCE_2B`), el que firma el `CITATION.cff`, los metadatos
de Zenodo y OSF, la caratula de entrega y los mensajes de confirmacion de cambios. Bajo esa
identificacion se leyo la tabla de asignacion y se eligio el enfoque.

El mapa de calificacion del docente asigna a este proyecto el codigo `AOPSS`. La
discrepancia de codigo se comunico al docente por el canal del curso el 2026-09-05 y se
resolvio como no sustantiva: el proyecto quedo correctamente identificado por su nombre,
su paralelo y sus integrantes.

**No se alega que la confusion justifique la desviacion.** Se registra porque es la causa
real y porque un lector que compare la tabla con el protocolo va a encontrar la diferencia
de todos modos. Es preferible que la encuentre explicada.

## 3. Por que el enfoque no se cambio al detectarse

Porque cambiarlo habria sido peor que declararlo.

El protocolo esta **registrado previamente en el Open Science Framework** con DOI
[`10.17605/OSF.IO/7PQ3H`](https://doi.org/10.17605/OSF.IO/7PQ3H), aceptado el
**2026-08-02T20:25:07 UTC** segun la API publica de OSF, y depositado por el Center for Open
Science en el Internet Archive con sus manifiestos SHA-256 y SHA-512. La marca temporal es
**externa al equipo y anterior a la recoleccion de datos**: no la podemos mover.

Un registro previo existe justamente para impedir que la pregunta se reescriba despues de
ver los resultados. Cambiar de enfoque a estas alturas —con los datos recogidos, el panel
ciego ejecutado y los resultados publicados— convertiria el registro previo en un adorno y
destruiria la unica garantia metodologica fuerte que tiene el trabajo. La desviacion se
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

Firma el equipo. La discrepancia de codigo de equipo esta comunicada al docente.

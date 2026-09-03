# Plan de monitoreo posterior al despliegue del componente inteligente

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos
Version 1.0 — 2026-09-03

---

## Por que existe este documento

La guia de desarrollo del 2026-09-02 lo dice con precision incomoda: la especificacion
nombra el monitoreo **41 veces** y no lo especifica ni una. «Mencionar un concepto en el
texto no equivale a especificarlo.» Esto lo convierte en un plan con indicadores,
periodicidad, responsable y umbral de alerta.

El requisito que obliga a mantener este plan en operacion es **RNF-IA-07**, en
[`requisitos_no_funcionales_ia.csv`](requisitos_no_funcionales_ia.csv).

## Que se vigila, y por que estos indicadores

Un modelo desplegado no falla de golpe: se degrada. Los cuatro modos de degradacion que se
vigilan aqui son los que pueden ocurrir sin que nadie se de cuenta.

| # | Modo de degradacion | Como se manifiesta si nadie mira |
|---|---|---|
| 1 | **Perdida de exactitud** | El modelo sigue prediciendo, pero acierta menos. Nadie lo nota porque las predicciones siguen llegando |
| 2 | **Deriva de los datos de entrada** | El parque de equipos cambia, se instalan sensores nuevos, y el modelo opera sobre una realidad distinta de la que aprendio |
| 3 | **Brecha de equidad** | El servicio empeora para un grupo concreto. Los promedios globales no lo muestran |
| 4 | **Perdida de utilidad de la explicacion** | La explicacion se sigue generando, pero deja de guiar la accion de quien la lee |

---

## 1. Cuadro de indicadores

Cada fila es un indicador con su periodicidad, su responsable, su umbral de alerta y lo que
hay que hacer cuando se supera. **Un indicador sin accion declarada no es un indicador: es
una cifra.**

| Cod. | Indicador | Unidad | Umbral de alerta | Periodicidad | Responsable | Accion al superarse |
|---|---|---|---|---|---|---|
| **MP-01** | Sensibilidad movil del modelo de prediccion de fallas | % en ventana de 90 dias | Cae por debajo de **60 %** | Mensual | Analista lider | Se abre revision del modelo. Si dos ciclos consecutivos siguen por debajo, se suspende la publicacion de la prediccion hasta reajustarlo |
| **MP-02** | Falsos positivos sobre el total de avisos emitidos | % | Supera **30 %** | Mensual | Personal de Infraestructura y Mantenimiento | Se eleva el umbral de disparo del aviso y se documenta el cambio. Un exceso sostenido convierte la alerta en ruido y la gente deja de atenderla |
| **MP-03** | Deriva de las variables de entrada respecto del conjunto de entrenamiento | distancia poblacional | Supera **0,25** | Semanal | Personal de TI | Se notifica al analista lider y se evalua reajuste. Por encima de 0,40 el reajuste es obligatorio |
| **MP-04** | Cobertura del parque de equipos elegibles | % | Cae por debajo de **95 %** | Mensual | Personal de TI | Se identifica que equipos quedaron fuera y por que. Un equipo sin cubrir es un equipo sin mantenimiento preventivo |
| **MP-05** | Exactitud de la deteccion de ocupacion frente a verificacion presencial | % | Cae por debajo de **95 %** | Mensual los tres primeros meses; trimestral despues | Personal de Infraestructura y Mantenimiento | Se revisa la calibracion de sensores del aula afectada antes de tocar el modelo: casi siempre es el sensor |
| **MP-06** | Brecha de cobertura entre carreras y entre franjas horarias | puntos porcentuales | Supera **5 pp** con intervalo que no contiene el cero | Trimestral | Coordinacion | Se suspende la publicacion del indicador agregado y se investiga la causa. **Una brecha real no se promedia: se corrige** |
| **MP-07** | Brecha de atencion en plazo entre grupos de docentes por volumen de reportes | puntos porcentuales | Supera **10 pp** | Semestral | Coordinacion | Revision del criterio de priorizacion de solicitudes |
| **MP-08** | Latencia de la explicacion en el percentil 95 | segundos | Supera **2 s** | En cada version que toque modelo o interfaz | Analista lider | Se optimiza o se degrada a explicacion precalculada, nunca se suprime la explicacion |
| **MP-09** | Comprension de la explicacion por el perfil destinatario | % de respuestas correctas | Cae por debajo de **80 %** | Semestral | Panel de Docentes y Personal de Infraestructura | Se reescribe la plantilla de explicacion y se vuelve a medir |
| **MP-10** | Acciones automaticas registradas, notificadas y reversibles | % | Cualquier valor **por debajo de 100 %** | Continua, con revision documentada mensual | Personal de TI | Se suspende la ejecucion automatica hasta corregir. Este es el unico umbral sin margen |
| **MP-11** | Antiguedad de la revision de la clasificacion de riesgo | meses | Supera **12 meses** | Anual, y ante cada cambio de alcance | Analista lider | Se ejecuta la revision antes de cualquier despliegue nuevo |

## 2. Como se registra cada medicion

Cada ciclo de medicion deja una fila en `06_Experimento/resultados/monitoreo_operacion.csv`
—que se crea con el primer ciclo real— con estos campos:

```
fecha, indicador, valor, unidad, umbral, supera_umbral, quien_midio, observaciones
```

**Ningun valor se escribe a mano.** Los indicadores MP-01 a MP-05, MP-08 y MP-10 se calculan
por script sobre la bitacora de acciones y el registro de predicciones. MP-06 y MP-07
requieren agregacion por grupo y se calculan con el mismo procedimiento de intervalos por
bootstrap que usa el paquete de datos, en
`07_Datos/scripts/etapa2_acuerdo_ic.py`. MP-09 y MP-11 son mediciones humanas y se registran
con el acta de la sesion que las produjo.

## 3. Que pasa si un ciclo no se mide

Se registra igual, con el valor vacio y el motivo. **Un hueco silencioso en la serie es
indistinguible de un valor normal**, y esa es exactamente la forma en que un sistema
desplegado deja de vigilarse sin que nadie lo decida.

RNF-IA-07 fija el umbral: al menos el 95 % de los ciclos previstos deben ejecutarse, y
ningun indicador puede acumular dos ciclos consecutivos sin medir.

## 4. Quien responde de que el plan se cumpla

| Rol | Responsabilidad |
|---|---|
| **Personal de TI** | Ejecuta las mediciones automaticas y mantiene los scripts |
| **Analista lider** | Valida los resultados, decide reajustes del modelo y revisa la clasificacion de riesgo |
| **Coordinacion** | Responde de que el plan se cumpla, y de las decisiones sobre brechas de equidad |
| **Personal de Infraestructura y Mantenimiento** | Ejecuta las verificaciones presenciales de MP-05 y valora los falsos positivos de MP-02 |

## 5. Estado actual

**El sistema no esta desplegado.** Este plan describe la vigilancia prevista, no una
vigilancia en curso, y ningun indicador tiene todavia un ciclo ejecutado. Se declara asi en
lugar de presentar el plan como si estuviera en operacion.

Lo que si esta hecho es la instrumentacion que lo hara posible: la bitacora de acciones
(RF-23), el registro de ejecuciones del componente (RP-IA-03) y los reportes
administrativos (RF-17) existen en la especificacion y el MVP implementa la bitacora.

# Ficha del componente de IA — RF-09 · Analisis predictivo de fallos

Proyecto SIGA · ISR-401 · Equipo FGMMN · Universidad Tecnica Estatal de Quevedo
Version 1.0 · 2026-08-29

---

## 1. Identificacion del componente

| Campo | Valor |
|---|---|
| Requisito del que deriva | RF-09 — Analisis predictivo de fallos mediante IA |
| Prioridad MoSCoW | Should |
| Origen en campo | EV-02 (COORD-01, 2026-06-30); requisito crudo RC-09 |
| Tipo de componente | Modelo de aprendizaje automatico supervisado, clasificacion binaria con salida calibrada a tres niveles |
| Precondicion de operacion | Minimo 30 dias de historico acumulado por equipo |
| Entradas | Serie temporal por equipo: lecturas ambientales del aula (temperatura, humedad), horas de encendido acumuladas, numero de ciclos de encendido y apagado, historico de fallas (RF-10) e historico de mantenimientos (RF-12) |
| Salidas | Indicador de riesgo de falla por equipo en 30 dias, en tres niveles: bajo, medio, alto; mas la probabilidad calibrada y la explicacion asociada |
| Consumidores de la salida | Panel de control centralizado (RF-07), alertas (RF-08), reportes administrativos (RF-17) |

### Comportamiento ante error

| Situacion | Comportamiento exigido |
|---|---|
| Menos de 30 dias de historico para un equipo | El componente devuelve `SIN_DATOS_SUFICIENTES`, nunca un nivel de riesgo. El panel muestra el estado explicitamente, no lo oculta ni lo presenta como riesgo bajo. |
| Serie con huecos superiores al 20 % del periodo | Devuelve `DATOS_INCOMPLETOS` e indica el porcentaje de cobertura real. |
| Fallo del servicio de inferencia | El panel conserva la ultima prediccion valida, marcada con su fecha y con la leyenda de prediccion desactualizada. El sistema no degrada a un valor por defecto. |
| Equipo dado de alta hace menos de 30 dias | Se excluye del calculo y se declara como tal en el reporte. |

> **Regla de diseno.** El componente nunca sustituye una lectura ausente por un valor
> imputado silenciosamente. Un dato que no existe se declara como inexistente.

---

## 2. Requisitos funcionales del componente

| ID | Requisito | Umbral | Unidad | Metodo de comprobacion |
|---|---|---|---|---|
| RF-IA-01 | El componente debe identificar correctamente los equipos que efectivamente fallaron dentro de la ventana de 30 dias. | ≥ 70 | % de sensibilidad (recall) | Validacion sobre conjunto de prueba retenido con fallas conocidas, separado temporalmente del entrenamiento. Se reporta la matriz de confusion completa. |
| RF-IA-02 | El componente debe limitar las alarmas falsas para no saturar al personal de mantenimiento. | ≤ 30 | % de falsos positivos sobre el total de equipos evaluados | Mismo conjunto de prueba retenido. Se reporta precision junto con sensibilidad. |
| RF-IA-03 | El componente debe emitir un nivel de riesgo por cada equipo activo con historico suficiente, sin omitir ninguno. | 100 | % de cobertura de equipos elegibles | Conteo automatico: equipos con nivel emitido dividido por equipos con ≥ 30 dias de historico, ejecutado en cada ciclo de inferencia. |
| RF-IA-04 | La probabilidad que acompana al nivel de riesgo debe estar calibrada, de modo que el nivel declarado corresponda a la frecuencia observada de fallas. | ≤ 0,10 | Error de calibracion esperado (ECE) | Curva de calibracion sobre el conjunto de prueba, con 10 particiones de probabilidad. |

---

## 3. Requisitos de rendimiento

| ID | Requisito | Umbral | Unidad | Metodo de comprobacion |
|---|---|---|---|---|
| RP-IA-01 | Tiempo de inferencia para el parque completo de equipos de la facultad. | ≤ 120 | segundos | Ejecucion cronometrada sobre el parque real registrado, repetida 10 veces; se reporta la mediana y el percentil 95. |
| RP-IA-02 | Latencia de consulta del nivel de riesgo de un equipo desde el panel. | ≤ 2 | segundos | Prueba de carga con 50 consultas concurrentes; se mide el percentil 95. |
| RP-IA-03 | Frecuencia de actualizacion del indicador de riesgo. | ≥ 1 | ejecucion cada 24 horas | Revision de la bitacora de ejecucion (RF-23) durante 30 dias continuos; se cuentan las ejecuciones completadas. |
| RP-IA-04 | Consumo de memoria del proceso de inferencia. | ≤ 512 | MB de memoria residente | Medicion del proceso durante la inferencia sobre el parque completo. |

---

## 4. Requisitos de equidad

El componente no toma decisiones sobre personas, pero **si distribuye un recurso escaso
entre grupos de aulas**: la atencion del personal de mantenimiento. Un modelo que
prediga peor en las aulas de un bloque concreto haria que esas aulas reciban menos
mantenimiento preventivo, y quienes lo sufren son las personas que dan clase alli. Esa
es la razon por la que estos requisitos existen.

| ID | Requisito | Metrica | Grupos comparados | Brecha maxima tolerada | Metodo de comprobacion |
|---|---|---|---|---|---|
| EQ-IA-01 | La sensibilidad del modelo no debe depender del bloque edilicio al que pertenece el aula. | Diferencia de sensibilidad entre grupos | Aulas del bloque antiguo frente a aulas del bloque nuevo | ≤ 10 puntos porcentuales | Sensibilidad calculada por separado en cada grupo sobre el conjunto de prueba retenido; se reporta la diferencia con intervalo de confianza al 95 % por bootstrap. |
| EQ-IA-02 | La tasa de falsos negativos no debe depender de la antiguedad del equipo. | Diferencia de tasa de falsos negativos | Equipos con menos de 3 anos de servicio frente a equipos con 3 anos o mas | ≤ 10 puntos porcentuales | Tasa calculada por separado en cada grupo; se reporta la diferencia con intervalo de confianza al 95 %. |
| EQ-IA-03 | La cobertura de equipos con prediccion emitida debe ser pareja entre aulas de alta y baja ocupacion, para que las aulas menos usadas no queden sin mantenimiento preventivo. | Diferencia de cobertura | Aulas por encima frente a por debajo de la mediana de horas de ocupacion (RF-20) | ≤ 5 puntos porcentuales | Conteo de cobertura por grupo en cada ciclo de inferencia. |

> Si alguna brecha supera su umbral, el componente **no se despliega**: se reentrena con
> muestreo balanceado por el grupo afectado y se vuelve a medir. El par antes-despues se
> publica en el reporte.

---

## 5. Requisito de explicabilidad

Extiende y concreta el requisito NFR-10 ya declarado en el ERS.

| Campo | Definicion |
|---|---|
| **ID** | EX-IA-01 |
| **Que se explica** | Por que un equipo concreto recibio su nivel de riesgo: las tres variables que mas contribuyeron a la prediccion, con el sentido de cada contribucion (aumenta o reduce el riesgo) y su magnitud relativa. |
| **A quien** | Al personal de infraestructura y mantenimiento (perfil CONS) que decide si interviene el equipo, y a la coordinacion academica (COORD) que autoriza el gasto. Ninguno de los dos perfiles es tecnico en aprendizaje automatico. |
| **En que formato** | Texto en lenguaje llano, sin jerga estadistica ni nombres internos de variables, de **60 palabras como maximo**, acompanado de una barra por variable que muestra su peso relativo. Prohibido mostrar coeficientes crudos o nombres de campos de la base de datos. |
| **En que momento** | En el momento en que la persona abre la ficha del equipo en el panel, sin que tenga que pedirla, y dentro de los **2 segundos** siguientes a la apertura. Tambien se incluye integra en la alerta de RF-08 cuando el nivel es alto. |
| **Umbral y metodo de comprobacion** | Tiempo de generacion ≤ 2 s, medido en el percentil 95 sobre 50 consultas. Longitud ≤ 60 palabras, verificada automaticamente. **Comprension**: en la sesion de validacion, al menos 4 de 5 participantes de perfil no tecnico deben explicar con sus palabras por que el sistema marco ese equipo, sin ayuda del entrevistador. El guion de esa sesion es `02_Evidencias/Guiones_Entrevista/guion_entrevista_no_tecnico_v2.0.md`. |

> **Limitacion declarada.** El metodo de explicacion elegido es de atribucion local por
> variable. Indica que variables pesaron en la prediccion, **no establece causalidad**.
> Esta limitacion se enuncia en el propio panel, junto a la explicacion, para que nadie
> lea la atribucion como una causa comprobada del fallo.

---

## 6. Especificacion de los datos de entrenamiento

| Campo | Contenido |
|---|---|
| **Origen** | Datos propios del despliegue de SIGA en la Facultad de Ciencias de la Computacion de la UTEQ: telemetria de sensores del aula, bitacora de encendido y apagado de equipos, historico de fallas (RF-10) e historico de solicitudes de mantenimiento (RF-12). No se usa ningun conjunto de datos externo ni preentrenado. |
| **Volumen minimo para entrenar** | 30 dias por equipo y **al menos 40 eventos de falla etiquetados** en el conjunto completo. Por debajo de ese volumen el componente no se entrena y el sistema opera sin RF-09. |
| **Unidad de observacion** | Un equipo en una ventana de 30 dias. |
| **Etiquetado** | Etiqueta positiva: el equipo registro una falla en `historico_fallas` dentro de los 30 dias siguientes al cierre de la ventana. Etiqueta negativa: no la registro. El etiquetado es **automatico y derivado del registro operativo**, no manual, de modo que no introduce criterio subjetivo. La definicion operativa de falla es la del catalogo de tipos de incidente de RF-10. |
| **Particion** | Separacion **temporal**, no aleatoria: se entrena con los periodos mas antiguos y se valida con el mas reciente, para no filtrar informacion del futuro hacia el entrenamiento. |
| **Sesgos conocidos** | (1) **Sesgo de reporte**: solo se registran las fallas que alguien reporto; una falla no reportada aparece como caso negativo y el modelo aprende a ignorarla. (2) **Sesgo de cobertura**: las aulas piloto tienen mas sensores instalados que el resto (RD-08), asi que el historico es mas denso alli. (3) **Sesgo de mantenimiento previo**: un equipo que recibio mantenimiento preventivo falla menos, y el modelo puede leer eso como que el equipo es fiable. (4) **Desbalance de clases**: las fallas son minoritarias frente a los periodos sin falla. |
| **Mitigaciones aplicadas** | Ante (1) y (3), las variables de mantenimiento se incluyen de forma explicita para que el efecto sea visible en la explicacion y no quede confundido. Ante (2), EQ-IA-01 mide la brecha entre bloques y bloquea el despliegue si se supera. Ante (4), se usa ponderacion de clases y la metrica principal es la sensibilidad, no la exactitud global. |
| **Base legal del tratamiento** | Los datos de telemetria y de estado de equipos **no son datos personales**: describen bienes de la institucion. El unico campo personal es el **responsable** que consta en cada registro de mantenimiento (RF-10, RF-12). Ese campo **se excluye del entrenamiento**: no entra como variable y no influye en ninguna prediccion. Para su conservacion en el registro operativo, la base legal es el cumplimiento de una mision de interes publico de la institucion educativa, conforme a la Ley Organica de Proteccion de Datos Personales del Ecuador. |
| **Conservacion** | El conjunto de entrenamiento se conserva 24 meses y despues se elimina o se agrega de forma irreversible. La politica completa por tipo de dato consta en `08_Etica/`. |

---

## 7. Plan de monitoreo en operacion

| Indicador | Que mide | Frecuencia | Umbral de alerta | Accion al superarse |
|---|---|---|---|---|
| Sensibilidad movil | Fallas reales detectadas frente al total de fallas ocurridas, en ventana movil de 90 dias | Mensual | < 60 % | Se abre una solicitud de cambio y se evalua reentrenar |
| Tasa de falsos positivos movil | Alertas emitidas que no derivaron en falla | Mensual | > 40 % | Se revisa el punto de corte antes de reentrenar |
| Deriva de las entradas | Distancia entre la distribucion de las variables de entrada actuales y las del entrenamiento | Semanal | Distancia poblacional > 0,25 en cualquier variable | Se investiga la causa: cambio de sensores, de horario academico o de parque de equipos |
| Cobertura de prediccion | Equipos elegibles con nivel emitido | Diaria | < 95 % | Se revisa la ingesta de telemetria |
| Brechas de equidad | Las tres metricas de la seccion 4 | Trimestral | Cualquiera supera su brecha maxima | **Se suspende la publicacion del indicador** hasta corregir |
| Volumen de datos nuevos | Eventos de falla etiquetados acumulados desde el ultimo entrenamiento | Mensual | ≥ 40 eventos nuevos | Se dispara reentrenamiento programado |

### Criterio de reentrenamiento

Se reentrena cuando se cumpla **cualquiera** de estas condiciones: se acumulan 40 eventos
de falla nuevos; la sensibilidad movil cae por debajo del 60 %; se detecta deriva por
encima de 0,25 en alguna variable; o han pasado 12 meses desde el ultimo entrenamiento.

Todo reentrenamiento **repite integramente** las comprobaciones de las secciones 2, 3 y 4
antes de sustituir al modelo en produccion. Un modelo que no supera alguna de ellas no se
despliega, y el modelo anterior sigue operando.

---

## 8. Trazado a los requisitos preexistentes

Ningun requisito de este componente queda aislado.

| Requisito de IA | Traza hacia | Naturaleza de la relacion |
|---|---|---|
| RF-IA-01, RF-IA-02, RF-IA-04 | RF-09 | Concretan el criterio de verificacion del requisito padre |
| RF-IA-03 | RF-07, RF-10 | La cobertura se calcula sobre el parque registrado y se muestra en el panel |
| RP-IA-01, RP-IA-04 | NFR-02 | Sostienen la disponibilidad mensual comprometida |
| RP-IA-02 | NFR-01, RF-07 | Se alinea con el tiempo de respuesta del panel |
| RP-IA-03 | RF-23 | La bitacora de acciones registra cada ejecucion |
| EQ-IA-01, EQ-IA-02 | RF-12, RD-08 | La equidad se define sobre la asignacion de mantenimiento y sobre el alcance piloto declarado |
| EQ-IA-03 | RF-20 | Los grupos se construyen con el historico de ocupacion |
| EX-IA-01 | NFR-10, RF-07, RF-08 | Concreta el requisito de explicabilidad ya declarado y define donde se muestra |
| Datos de entrenamiento | RF-10, RF-12, RF-20, RD-09 | Las fuentes son requisitos existentes; RD-09 fija el respeto a la normativa de proteccion de datos |
| Plan de monitoreo | RF-23, RF-17 | Los indicadores se registran en bitacora y se exponen en reportes |

La version en tabla, apta para incorporarse a la matriz, esta en
[`trazado_requisitos_ia.csv`](trazado_requisitos_ia.csv).

---

## 9. Referencias normativas y metodologicas

- Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024, por el que se establecen normas armonizadas en materia de inteligencia artificial.
- Asamblea Nacional del Ecuador (2021). Ley Organica de Proteccion de Datos Personales. Registro Oficial, Quinto Suplemento n.º 459.
- Chazette, L. y Schneider, K. (2020). Explainability as a non-functional requirement: challenges and recommendations. *Requirements Engineering*, 25(4), 493–514.
- Chazette, L., Brunotte, W. y Speith, T. (2022). Explainable software systems: from requirements analysis to system evaluation. *Requirements Engineering*, 27(4), 457–487.
- Habibullah, K. M., Gay, G. y Horkoff, J. (2023). Non-functional requirements for machine learning: understanding current use and challenges among practitioners. *Requirements Engineering*, 28(2), 283–316.
- Vogelsang, A. y Borg, M. (2019). Requirements engineering for machine learning: perspectives from data scientists. *REW 2019*, 245–251.

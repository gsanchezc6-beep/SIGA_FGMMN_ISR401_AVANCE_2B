# Clasificacion de riesgo del sistema y obligaciones derivadas

Proyecto SIGA · ISR-401 · Equipo FGMMN · Universidad Tecnica Estatal de Quevedo
Version 1.0 · 2026-08-29

Clasificacion razonada **sobre SIGA tal como esta especificado**, no sobre un ejemplo de
manual. Marco de referencia: Reglamento (UE) 2024/1689 sobre inteligencia artificial, y
Ley Organica de Proteccion de Datos Personales del Ecuador.

> **Alcance de la aplicabilidad.** SIGA se despliega en Ecuador, donde el Reglamento
> (UE) 2024/1689 no es derecho vigente. Se adopta de forma **voluntaria** como marco de
> clasificacion porque es el instrumento mas exigente disponible y porque la guia de la
> asignatura lo fija como referencia. Las obligaciones legalmente exigibles a este
> sistema son las de la Ley Organica de Proteccion de Datos Personales del Ecuador.

---

## 1. Inventario de componentes sometidos a clasificacion

| Componente | Requisito | ¿Es un sistema de IA? | Justificacion |
|---|---|---|---|
| Analisis predictivo de fallos | RF-09 | **Si** | Modelo de aprendizaje automatico supervisado que infiere probabilidad de falla a partir de datos historicos. Su salida no es programada de forma explicita. |
| Deteccion de ocupacion de aula | RF-03 | **No** | Umbral determinista sobre la senal de un sensor de presencia. Ver la seccion 4. |
| Apagado automatico y reglas horarias | RF-13, RF-15, RF-16, RF-21 | **No** | Reglas condicionales fijas sobre horario y estado de ocupacion. |
| Generacion de alertas por anomalia | RF-08 | **No** | Comparacion contra umbrales declarados en la especificacion. |

**Un unico componente de IA en el sistema: RF-09.**

---

## 2. Descarte de las categorias superiores

### 2.1 No es una practica prohibida (Art. 5)

RF-09 no infiere emociones, no puntua a personas por su comportamiento social, no hace
identificacion biometrica remota, no explota vulnerabilidades de ningun grupo y no
manipula conducta. **Predice el fallo de un equipo electromecanico.** Su objeto es un
bien mueble de la institucion, no una persona.

### 2.2 No es de alto riesgo (Art. 6 y Anexo III)

El Anexo III incluye la educacion y la formacion profesional, de modo que la pregunta
merece analizarse y no descartarse por evidente. Los supuestos del anexo en materia
educativa son cuatro:

| Supuesto del Anexo III, punto 3 | ¿Aplica a RF-09? | Razon |
|---|---|---|
| Determinar el acceso o la admision a centros educativos | No | RF-09 no interviene en ninguna decision sobre estudiantes. |
| Evaluar resultados de aprendizaje | No | No procesa desempeno academico de ninguna persona. |
| Evaluar el nivel educativo adecuado para una persona | No | No emite juicios sobre personas. |
| Vigilar o detectar comportamientos prohibidos durante examenes | No | RF-09 no observa personas. La deteccion de ocupacion (RF-03) registra si un aula esta ocupada, **no quien la ocupa**, y no opera durante evaluaciones con finalidad de vigilancia. |

Tampoco encaja en los demas puntos del anexo: no es componente de seguridad de una
infraestructura critica —gestiona confort y mantenimiento de aulas, no el suministro
electrico ni la seguridad estructural—, no interviene en empleo, ni en acceso a
servicios esenciales, ni en aplicacion de la ley, ni en migracion, ni en justicia.

**Conclusion: RF-09 no es un sistema de alto riesgo.**

### 2.3 No genera obligaciones de transparencia del Art. 50

El articulo 50 obliga cuando el sistema interactua directamente con personas fisicas,
genera contenido sintetico o reconoce emociones. RF-09 no hace ninguna de las tres: emite
un indicador de riesgo sobre un equipo, dentro de un panel de gestion.

---

## 3. Clasificacion resultante y obligaciones asumidas

> **RF-09 se clasifica como sistema de IA de riesgo minimo.**

En riesgo minimo el reglamento no impone obligaciones vinculantes, y remite a codigos de
conducta voluntarios (Art. 95). El equipo **asume voluntariamente** las siguientes
obligaciones, que son las que efectivamente se implementan y se verifican:

| Obligacion asumida | Donde se cumple | Como se comprueba |
|---|---|---|
| Documentar el proposito, las entradas, las salidas y el comportamiento ante error | Ficha RF-09, seccion 1 | Revision documental |
| Declarar la procedencia, el volumen, el etiquetado y los sesgos conocidos de los datos | Ficha RF-09, seccion 6 | Revision documental |
| Medir el desempeno con umbral, unidad y metodo declarados antes de desplegar | Ficha RF-09, secciones 2 y 3 | Ejecucion sobre conjunto de prueba retenido |
| Medir brechas entre grupos y bloquear el despliegue si se superan | Ficha RF-09, seccion 4 | Metricas por grupo con intervalo de confianza |
| Explicar cada prediccion a quien la usa, en su lenguaje | Ficha RF-09, seccion 5 · NFR-10 | Prueba de comprension con participantes no tecnicos |
| Vigilar el modelo en operacion y declarar cuando se reentrena | Ficha RF-09, seccion 7 | Bitacora de indicadores (RF-23) |
| Mantener supervision humana sobre la salida | RF-12 | El indicador **no dispara ninguna accion automatica**: abre una solicitud de mantenimiento que una persona decide atender o descartar |
| Declarar la limitacion del metodo de explicacion | Ficha RF-09, seccion 5 | La leyenda consta en el propio panel |

---

## 4. Por que RF-03 no se clasifica como componente de IA

RF-03 esta especificado en el ERS como la determinacion del estado ocupada o vacia
**mediante sensores de presencia**, con criterio de verificacion de exactitud ≥ 95 % y
latencia ≤ 15 s. Es un umbral determinista sobre la senal de un sensor: dado el mismo
valor de entrada, la salida es siempre la misma y esta programada de forma explicita. No
hay modelo entrenado, no hay parametros aprendidos a partir de datos y no hay inferencia
estadistica. Por definicion del propio reglamento, **no es un sistema de IA**.

Esta clasificacion depende de la especificacion vigente y **dejaria de ser valida** si el
diseno cambia en cualquiera de estos sentidos:

1. Si la ocupacion pasara a inferirse a partir de las camaras de RF-06 mediante vision
   por computador, en lugar de un sensor de presencia.
2. Si se fusionaran varias senales mediante un modelo entrenado en lugar de una regla.
3. Si se estimara el **numero** de personas presentes, y no solo la condicion binaria de
   ocupada o vacia.

Cualquiera de esos cambios convertiria a RF-03 en un componente de IA y **exigiria su
propia ficha completa**. Ademas, el supuesto 3 tocaria material sensible: contar personas
en un aula, cruzado con el horario academico, permite inferir la asistencia de un docente
identificable, lo que activa obligaciones de la Ley Organica de Proteccion de Datos
Personales que hoy no aplican.

Se registra aqui de forma expresa para que la decision quede trazada y para que, si el
diseno evoluciona, la revision sea obligatoria y no quede al criterio de quien la
implemente.

---

## 5. El modelo de lenguaje del componente empirico

El estudio empirico usa un modelo grande de lenguaje para generar el Conjunto A de
requisitos funcionales. Ese modelo **no forma parte de SIGA**: es el objeto de estudio
del cuasi-experimento, no un componente del sistema entregado al cliente. No opera en
produccion, no procesa datos de la organizacion en operacion y no produce ninguna salida
que llegue a un usuario del sistema.

Queda fuera de esta clasificacion, y su uso, sus consignas y sus limitaciones se declaran
en `06_Experimento/consignas/` y en `08_Etica/declaracion_uso_ia.md`.

---

## 6. Revision de esta clasificacion

Se revisa cuando ocurra cualquiera de estos hechos: se incorpore un componente nuevo
basado en datos; cambie la especificacion de RF-03 en los sentidos de la seccion 4;
RF-09 pase a disparar acciones sin intervencion humana; o el sistema se extienda mas alla
de la Facultad de Ciencias de la Computacion.

| Version | Fecha | Responsable | Cambio |
|---|---|---|---|
| 1.0 | 2026-08-29 | Equipo FGMMN | Clasificacion inicial sobre la especificacion v2.0 del ERS |

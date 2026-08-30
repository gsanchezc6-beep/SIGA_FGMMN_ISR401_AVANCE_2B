# Guion de entrevista de validacion — participante no tecnico

Proyecto SIGA (Sistema Inteligente de Gestion de Aulas) · ISR-401 · Equipo FGMMN
Universidad Tecnica Estatal de Quevedo · Facultad de Ciencias de la Computacion

**Version 2.0** · Instrumento aplicado · Duracion prevista: 35–45 minutos

---

## 0. Antes de empezar — lista del entrevistador

Marcar cada casilla **antes** de iniciar la grabacion. Una casilla sin marcar invalida
la sesion como evidencia.

- [ ] Consentimiento informado impreso, en dos copias.
- [ ] Grabadora de video con bateria y espacio para 60 minutos.
- [ ] Grabadora de audio independiente, como respaldo redundante del video.
- [ ] Prototipo cargado y funcionando, con datos de ejemplo sembrados.
- [ ] Codigo de participante asignado de antemano (`DOC-nn`, `COORD-nn` o `CONS-nn`).
      **Nunca se dice ni se escribe el nombre propio durante la grabacion.**
- [ ] Cuaderno de notas de campo con la fecha y el codigo ya escritos.
- [ ] Sala sin terceros presentes y sin ruido de fondo.

**Datos que se registran al inicio de la sesion**

| Campo | Valor |
|---|---|
| Fecha y hora de inicio | |
| Codigo de participante | |
| Perfil | Docencia · Coordinacion academica · Conserjeria e infraestructura |
| Anos de experiencia en la facultad | |
| Aulas con las que trabaja habitualmente | |
| Entrevistador responsable | |
| Duracion total | |
| Archivo de video | `AAAA-MM-DD_TipoParticipante_Codigo_Validacion.mp4` |
| Archivo de audio | `AAAA-MM-DD_TipoParticipante_Codigo_Audio.mp3` |

---

## 1. Consentimiento informado — se lee en voz alta, textual (3 min)

> Buenos dias. Gracias por acompanarnos. Somos estudiantes de la carrera de Software de
> la UTEQ y estamos trabajando en un proyecto de la asignatura Ingenieria de
> Requerimientos. El proyecto se llama SIGA y es un sistema para manejar las aulas de la
> facultad: la temperatura, los proyectores, el aire acondicionado y los pedidos de
> mantenimiento.
>
> Lo que vamos a hacer hoy es ensenarle como quedo el sistema y pedirle su opinion. No
> hay respuestas correctas ni incorrectas, y **no lo estamos evaluando a usted**: usted
> nos esta evaluando a nosotros. Si algo no se entiende o le parece mal, decirlo es
> exactamente lo que necesitamos.
>
> La sesion se graba en video y en audio, solo para poder transcribirla despues. En todo
> lo que publiquemos usted aparece con un codigo, nunca con su nombre. Nadie fuera del
> equipo y del docente responsable ve la grabacion original.
>
> Su participacion es voluntaria. Puede pedir que apaguemos la grabacion en cualquier
> momento, puede saltarse cualquier pregunta y puede pedirnos despues que borremos todo
> lo suyo, sin dar explicaciones y sin ninguna consecuencia para usted.
>
> Esto ultimo no es una formula: en este mismo estudio un participante nos pidio retirar
> su entrevista y la eliminamos por completo.
>
> ¿Tiene alguna pregunta antes de firmar?

**Firma del consentimiento. Recien despues se inicia la grabacion.**

> *(ya grabando)* Para dejarlo registrado: ¿nos autoriza a grabar esta sesion en video y
> audio, en los terminos que acabamos de leer y que usted firmo?

---

## 2. Contexto y calentamiento (5 min)

Preguntas abiertas. No mencionar todavia el sistema ni mostrarlo.

1. Cuenteme como es un dia normal suyo en la facultad, en lo que tiene que ver con las
   aulas.
2. ¿Que es lo que mas le complica de las aulas hoy? Piense en la ultima semana.
3. Cuando en un aula hace demasiado calor, o el proyector no enciende, ¿que hace usted?
   Lleveme paso a paso, desde que se da cuenta hasta que se resuelve.
4. ¿Cuanto suele tardar en resolverse? ¿Y como se entera de que ya se resolvio?
5. ¿Alguna vez dio aviso de un problema y no paso nada? ¿Que ocurrio?

> **Al entrevistador.** Estas cinco preguntas alimentan la codificacion tematica. No
> interrumpir. Si la respuesta se queda corta, usar solo: «¿me puede dar un ejemplo
> concreto?» o «¿y que paso despues?».

---

## 3. Recorrido guiado por el prototipo (18 min)

Se abre el prototipo y se recorre pantalla por pantalla. En cada bloque: **primero se
deja mirar en silencio**, despues se pregunta.

Consigna literal de apertura, la misma para todos los participantes:

> Le voy a mostrar unas pantallas del sistema. Mirelas con calma unos segundos y despues
> le hago un par de preguntas. Vaya diciendo en voz alta lo que se le pase por la cabeza,
> aunque le parezca una tontera.

### Bloque 3.1 — Panel de control (RF-07, RF-01, RF-22)

*Se muestra el panel con el estado de varias aulas.*

1. Sin que yo le explique nada: ¿que cree que esta viendo aqui?
2. Senale un aula que, segun esta pantalla, tenga algun problema. ¿Como se dio cuenta?
3. ¿Que informacion le sobra en esta pantalla? ¿Y cual le falta para que le sirva?
4. Si abriera esto a primera hora de la manana, ¿que seria lo primero que miraria?

### Bloque 3.2 — Alertas y avisos (RF-08, RF-11, RF-21)

*Se muestra el historial de alertas y una notificacion de falla critica.*

5. ¿Que le esta diciendo el sistema con este aviso?
6. Si le llegara este aviso un miercoles a las tres de la tarde, ¿que haria usted?
7. ¿Por que via preferiria recibirlo: correo, mensaje al celular, o verlo aqui dentro?
8. ¿Cuantos avisos al dia le parecerian demasiados? Digame un numero.

> **Al entrevistador.** La respuesta a la 8 es un umbral cuantitativo. Anotarla textual
> con el numero: sustenta un requisito no funcional de usabilidad.

### Bloque 3.3 — Control de proyector y climatizacion (RF-04, RF-05, RF-13, RF-16)

*Se muestra la pantalla de control remoto de equipos.*

9. Aqui se puede apagar el aire de un aula desde el telefono. ¿Le parece util o le
    preocupa? ¿Por que?
10. ¿Quien cree usted que deberia poder hacer esto, y quien no?
11. El sistema puede apagar solo los equipos de un aula vacia. ¿Que riesgo le ve?
12. ¿Se le ocurre alguna situacion en la que apagar automaticamente seria un problema?

### Bloque 3.4 — Solicitudes de mantenimiento (RF-12, RF-10)

*Se muestra el flujo de creacion y seguimiento de una solicitud.*

13. Muestreme como pediria usted que arreglen un proyector danado. Hagalo usted, yo no
    le ayudo salvo que se trabe.
14. *(si se traba mas de 30 segundos)* ¿Que esperaba encontrar y no encontro?
15. Una vez enviada la solicitud, ¿que espera que pase? ¿Que le gustaria saber mientras
    tanto?
16. ¿Le sirve poder ver el historial de lo que se ha arreglado en un aula? ¿Para que lo
    usaria?

> **Al entrevistador.** La pregunta 13 es una tarea, no una pregunta. Cronometrar en
> silencio y anotar en las notas de campo si la completa, si pide ayuda y en que punto
> duda. Ese dato sustenta un requisito de usabilidad con umbral.

---

## 4. Preguntas de cierre sobre el sistema (7 min)

17. Si manana instalaran esto en su facultad, ¿lo usaria? ¿Que tendria que pasar para
    que lo usara todos los dias?
18. ¿Que es lo que mas le gusto y que es lo que definitivamente cambiaria?
19. ¿Hay algo que este sistema hace y que a usted le incomoda? Piense en privacidad: el
    sistema sabe cuando un aula esta ocupada.
20. ¿Falta algo importante que usted necesita y que no vimos hoy?
21. ¿Que le diria a un companero suyo que va a usar esto por primera vez?

---

## 5. Derechos sobre sus datos y despedida (3 min)

> Ultima cosa, y es importante. Todo lo que grabamos hoy queda guardado con su codigo,
> no con su nombre. Usted tiene derecho a pedirnos en cualquier momento que le mostremos
> lo que tenemos suyo, que lo corrijamos si algo esta mal, o que lo borremos por
> completo. Para eso escribe a este correo y le respondemos.
>
> *(entregar la hoja con el correo de contacto del corresponsal del equipo)*
>
> ¿Le gustaria que le contemos como termino el proyecto cuando lo cerremos?
>
> Muchisimas gracias por el tiempo.

**Se detiene la grabacion. Se anota la hora de fin.**

---

## 6. Inmediatamente despues — notas de campo

Se redactan **en los quince minutos siguientes**, antes de que se pierda el detalle. Una
nota por sesion, en `02_Evidencias/Notas_Campo/`.

| Campo | Contenido |
|---|---|
| Codigo y fecha | |
| Duracion real | |
| Estado del entorno | ruido, interrupciones, terceros presentes |
| Lenguaje no verbal relevante | dudas, incomodidad, entusiasmo, en que pantalla |
| Donde se trabo en la tarea del bloque 3.4 | |
| Frases textuales que valen como cita | |
| Contradicciones respecto de otras entrevistas | |
| Desviaciones respecto de este guion | que pregunta se omitio o se anadio, y por que |
| Requisitos que la sesion pone en duda | |

---

## Anexo A — Acta de la sesion de validacion

Se completa y se firma al terminar. Se publica enmascarada, junto al video, en
`02_Evidencias/Validacion/Sesiones_Validacion/`.

**Acta de sesion de validacion — SIGA**

| | |
|---|---|
| Codigo de participante | |
| Perfil | Tecnico · **No tecnico** |
| Fecha y hora | |
| Duracion | |
| Modalidad | Presencial · Remota |
| Entrevistador | |
| Observador | |
| Archivo de video | |
| Archivo de audio | |

**Requisitos puestos a validacion en esta sesion**

| Requisito | Descripcion breve | Veredicto | Observacion del participante |
|---|---|---|---|
| RF-01 | Monitorear el estado ambiental del aula | Acepta · Acepta con cambios · Rechaza | |
| RF-04 | Controlar remotamente los proyectores | Acepta · Acepta con cambios · Rechaza | |
| RF-05 | Ajustar remotamente la climatizacion | Acepta · Acepta con cambios · Rechaza | |
| RF-07 | Consultar un panel de control centralizado | Acepta · Acepta con cambios · Rechaza | |
| RF-08 | Generar y enviar alertas por anomalias | Acepta · Acepta con cambios · Rechaza | |
| RF-11 | Notificar de forma inmediata las fallas criticas | Acepta · Acepta con cambios · Rechaza | |
| RF-12 | Gestionar las solicitudes de mantenimiento | Acepta · Acepta con cambios · Rechaza | |
| RF-16 | Apagar automaticamente equipos de aulas desocupadas | Acepta · Acepta con cambios · Rechaza | |
| RF-21 | Notificar equipos encendidos fuera de horario | Acepta · Acepta con cambios · Rechaza | |

**Defectos detectados en la sesion**

| N.º | Requisito | Tipo | Severidad | Descripcion | Accion acordada | Responsable |
|---|---|---|---|---|---|---|
| 1 | | Omision · Ambiguedad · Inconsistencia · Incorreccion | Alta · Media · Baja | | | |

> Tipo y severidad se registran con estos mismos valores en el registro de defectos de
> `02_Evidencias/Validacion/Inspeccion/`. Todo defecto de severidad alta abre una
> solicitud de cambio en `02_Evidencias/Validacion/Solicitudes_Cambio/`.

**Umbrales cuantitativos declarados por el participante**

| Pregunta | Valor declarado | Requisito no funcional que sustenta |
|---|---|---|
| Maximo de avisos al dia (P8) | | |
| Tiempo que completar la solicitud le tomo (P13) | | |

Firma del participante: ____________________  Firma del entrevistador: ____________________

> En la copia publicada se enmascaran la firma y la cedula. El original integro se
> conserva bajo custodia del docente responsable.

---

## Historial de cambios del instrumento

| Version | Fecha | Cambio | Motivo |
|---|---|---|---|
| 1.0 | 2026-05-10 | Guion inicial de elicitacion, once preguntas abiertas. | Primera ronda de campo. |
| 1.1 | 2026-06-25 | Se anade el bloque de recorrido por el prototipo. | El prototipo alcanza estado demostrable. |
| 1.2 | 2026-07-12 | Se separa la version para perfil tecnico de la de perfil no tecnico. | Los terminos «umbral», «bitacora» y «rol» no se entendian fuera del perfil tecnico. |
| 1.3 | 2026-07-20 | Se anaden las preguntas 8 y 13 con registro de valor y de tiempo. | Los requisitos no funcionales carecian de umbral sustentado en campo. |
| **2.0** | **2026-08-29** | Se reescribe como sesion de validacion: veredicto por requisito, registro de defectos con tipo y severidad, y notas de campo obligatorias. Se explicita el derecho de retiro y el circuito de derechos sobre los datos. | Cierre de la Entrega Final: la validacion debe producir evidencia verificable, no solo opinion. |

> Las versiones 1.0 a 1.3 se conservan en el historial de Git de este archivo. El
> instrumento aplicado en cada sesion es el vigente en la fecha del acta.

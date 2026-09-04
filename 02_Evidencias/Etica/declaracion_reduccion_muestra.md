# Declaracion de reduccion de la muestra de entrevistas

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos · Entrega Final (2B)

---

> ## Estado de esta declaracion a 2026-09-04
>
> **Superada por los hechos.** La **ronda terminal del 2026-09-03** anadio seis entrevistas
> a docentes (`EV-20` a `EV-25`) y llevo el corpus de diez a **dieciseis**. El informe
> escrito de calificacion de la Entrega 2B fija el minimo terminal en dieciseis, de modo que
> ya no hay reduccion que declarar respecto del minimo aplicable.
>
> **Este documento no se reescribe.** Registra una decision real, su fecha, su fundamento y
> el hecho de que no se obtuvo autorizacion escrita para ella. Borrarlo o reescribirlo en
> pasado dejaria sin rastro un periodo en el que el equipo trabajo con una muestra reducida y
> lo declaro abiertamente. Lo que sigue vale como historia del proceso, no como estado actual.
>
> **Lo que sigue vigente sin cambios:** la exclusion integra de `EV-15` por retiro del
> consentimiento, el calculo de potencia --que se refiere al numero de evaluadores del
> cuasi-experimento, no al de entrevistas--, y las amenazas a la validez externa derivadas
> de la composicion de la muestra, que la ronda terminal no corrige: nueve de los dieciseis
> participantes son docentes, y conserjeria y coordinacion siguen infrarrepresentadas.

---

## 1. Que se declara

La seccion 5.1 de la guia de la Entrega Final fija un minimo de **24 participantes** con
consentimiento, entrevista en video y entrevista en audio. El equipo cerro el levantamiento
de campo en **diez entrevistas validas**.

**El equipo no dispone de autorizacion escrita para esa reduccion.** El criterio de piso G8
exige que toda reduccion de un minimo cuente con autorizacion escrita del docente anterior a
la fecha de corte. Esa autorizacion no existe, y este documento no la sustituye ni pretende
equivaler a ella.

Lo que existe es una **autorizacion verbal** dada por el docente responsable ante el curso
reunido, y la constancia de haberla solicitado por escrito sin obtener respuesta. Ambas
cosas se documentan aqui con su fecha, para que el limite de la evidencia quede declarado
por el equipo y no lo tenga que descubrir el tribunal.

## 2. Lo ocurrido, con fechas

| Fecha | Hecho | Constancia |
|---|---|---|
| 2026-08-17, 17:22 | El docente autoriza verbalmente, en el area de TICS y ante el curso reunido, cerrar el levantamiento en diez entrevistas validas | `acta_constancia_N10.pdf`, **depositada**: firmada por los dos integrantes y por **cuatro testigos del equipo AOPSS**, ajenos a esta entrega |
| 2026-08-29 | Se solicita al docente confirmacion escrita por mensajeria | Sin respuesta |
| 2026-08-31, 13:50 | Se reitera la solicitud por correo institucional | `solicitud_confirmacion_N10.pdf`, **depositado**: captura del mensaje enviado desde la cuenta institucional. Sin respuesta a la fecha de este documento |

El acta de constancia recoge la declaracion de los integrantes presentes y la firma de
testigos de otros equipos, que escucharon la autorizacion y **no tienen interes en esta
entrega**. Es el respaldo mas fuerte disponible, y sigue sin ser una autorizacion escrita del
docente.

**Estado a 2026-09-01.** El acta ya esta firmada y depositada. La suscriben los dos
integrantes y **cuatro testigos del equipo AOPSS**, identificados por nombre completo y
equipo. Sus numeros de cedula estan tapados en la copia publicada: firmaron como testigos
de un hecho, no otorgaron consentimiento para el tratamiento de sus datos, y el numero de
cedula no es necesario para que la constancia cumpla su funcion. El original sin tapar lo
conserva el equipo y esta a disposicion del docente si lo requiere.

**Una precision sobre una ruta.** El apartado 2 del acta remite al comprobante del correo
como `08_Etica/solicitud_confirmacion_N10.pdf`. La carpeta de etica de este repositorio es
`02_Evidencias/Etica/`, que es donde el archivo esta realmente depositado. La referencia
interna del acta no se corrige porque el documento ya esta firmado; se deja constancia
aqui de la ruta correcta.

**Lo que esto no cambia.** El acta no es una autorizacion escrita del docente y no se
presenta como tal: su propio apartado 5 lo dice. La reduccion de la muestra sigue siendo
una desviacion declarada, no un minimo cumplido.

## 3. Motivos expresados en su momento

Dos, ambos verificables contra el resto del expediente:

**Adelanto del calendario de entrega.** La fecha de corte se adelanto respecto de lo
previsto al planificar la segunda ronda de campo.

**Agotamiento de la poblacion disponible.** Tras la exclusion integra de la entrevista EV-15
por retiro del consentimiento informado del participante, no quedaba poblacion accesible para
nuevas entrevistas dentro del plazo.

## 4. Estrategia de muestreo

La guia admite sustentar un tamano menor con un argumento de muestreo documentado. Se declara
el que efectivamente se aplico, sin reconstruirlo a posteriori.

| Elemento | Valor declarado |
|---|---|
| Poblacion objetivo | Personal y usuarios de las aulas de la Facultad de Ciencias de la Computacion de la UTEQ implicados en su uso, mantenimiento o asignacion |
| Marco muestral | Cuatro perfiles: personal de servicios generales, coordinacion de carrera, docencia y estudiantado |
| Metodo de seleccion | Muestreo por conveniencia con cuotas por perfil, condicionado por la accesibilidad del personal en jornada laboral |
| Tamano alcanzado | 10 entrevistas validas sobre 11 realizadas; EV-15 excluida integramente por retiro del consentimiento |
| Complemento cuantitativo | Cuestionario aplicado con **n = 60** respuestas, que cubre el perfil dominante con el minimo que la guia exige para ese instrumento |
| Saturacion | Declarada y medida sobre las transcripciones disponibles; la curva figura en `07_Publicacion/figuras/curva_saturacion.png`, generada por `06_Experimento/scripts_analisis/curva_saturacion.py` |

**Sesgo reconocido.** El muestreo por conveniencia sobrerrepresenta a quien estaba disponible
en jornada laboral y en el edificio de la facultad. Los perfiles de coordinacion y de
servicios generales quedan mejor cubiertos que el estudiantado, que se compensa parcialmente
por la via del cuestionario. Ningun hallazgo de este trabajo se generaliza mas alla de la
facultad estudiada.

## 5. Efecto sobre la validez, sin atenuarlo

**Validez externa.** Diez entrevistas no sostienen generalizacion. Las conclusiones se
limitan a la organizacion cliente estudiada y asi se enuncian en el informe.

**Saturacion.** Con diez entrevistas la saturacion tematica se declara sobre la evidencia
disponible y no se afirma alcanzada mas alla de lo que la curva muestra.

**Triangulacion.** Todo hallazgo que se sostiene en este trabajo se apoya en al menos dos
fuentes de tipo distinto: entrevista, observacion de entorno, documento de la organizacion o
respuesta de cuestionario. Es lo que compensa, en parte, el numero de entrevistas.

## 6. Posicion del equipo

El equipo **no invoca esta declaracion como justificacion**. La presenta como lo que es: el
registro de un incumplimiento asumido del minimo de la seccion 5.1, con sus circunstancias,
su argumento de muestreo y su efecto sobre la validez declarados por adelantado.

Si el docente confirma por escrito la autorizacion verbal, este documento queda sustituido
por esa confirmacion. Si la corrige o la niega, el equipo mantiene la declaracion tal como
esta.

---

**Integrantes que suscriben esta declaracion**

| Integrante | Cedula | Correo institucional |
|---|---|---|
| Sanchez Cornejo, Gary Alberto | 1208338291 | gsanchezc6@uteq.edu.ec |
| Munoz Quinonez, Yeranick Esther | 1207929645 | ymunozq@uteq.edu.ec |

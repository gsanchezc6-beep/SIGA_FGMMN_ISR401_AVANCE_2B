# Declaracion sobre el perfil tecnico en las sesiones de validacion

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos · Entrega Final (2B)
Fecha: 2026-09-04 · **Actualizada el 2026-09-07**

---

## 1. Que se declara

La guia de la Entrega Final pide **seis sesiones de validacion grabadas con acta firmada, tres
con usuarios tecnicos y tres con usuarios no tecnicos**.

**El reparto se cumple.** Las tres sesiones tecnicas estan depositadas:

| Sesion | Evidencia | Fecha | Perfil declarado por el participante |
|---|---|---|---|
| `WT-08` · `TIC-01` | `EV-26` | 2026-09-04 | Asistente de Tecnologias TIC; administra equipamiento y laboratorios |
| `WT-09` · `TIC-02` | `EV-27` | 2026-09-05 | Responsable de redes y soporte tecnico; atiende y diagnostica averias |
| `WT-10` · `TIC-03` | `EV-28` | 2026-09-07 | Laboratorista de Ciencias de la Computacion; control operativo de aulas y laboratorios |

A los tres se les aplico el mismo criterio: **lo que la persona declara que hace**, preguntado
antes de clasificarla, y contrastado con el cargo que escribio de su puno y letra en el
consentimiento firmado.

> **Este documento ya no declara un incumplimiento.** Hasta el 2026-09-06 declaraba dos
> sesiones tecnicas de las tres exigidas y asumia la consecuencia en la calificacion. Se
> conserva --en vez de retirarse-- porque lo que sostiene la clasificacion de un participante
> como tecnico no es el recuento, sino el criterio de los apartados 2 y 3, y ese criterio hay
> que poder auditarlo.

## 2. Como se decidio quien es usuario tecnico

El criterio aplicado fue **lo que la persona declara que hace**, no el nombre de su cargo ni
la conveniencia del recuento. A cada candidato se le formulo la misma pregunta abierta antes
de clasificarlo:

> ¿De que se encarga en concreto: redes, servidores, proyectores, soporte a usuarios?

Se considera **usuario tecnico** a quien administra sistemas, cuentas, equipamiento o red.
Se considera **usuario no tecnico** a quien opera el equipamiento y reporta incidencias, aunque
las detecte a diario.

## 3. Perfiles descartados, y por que

| Perfil | Por que no califica |
|---|---|
| **Personal de servicios generales** (`CONS-01` a `CONS-04`) | Operan y reportan; no administran. Sus propias transcripciones lo dicen: `CONS-03` describe que comunica la falla a la autoridad de la facultad y que *«ella realiza el escrito y ella manda para el tecnico»*; `CONS-02` que se avisa a los jefes *«para que manden a los responsables a dar un mantenimiento»*. Se distinguen ellos mismos del tecnico |
| **Coordinacion de carrera** (`COORD-01` a `COORD-03`) | Gestion academica. Encaminan el reporte, no lo resuelven |
| **Docentes** (`DOC-01` a `DOC-10`) | Usuarios finales del equipamiento del aula |
| **Secretaria** | Funcion administrativa: tramites, matriculas, horarios. No administra sistemas ni cuentas |

**Ninguno de estos perfiles se reclasifico para completar el recuento.** Declararlos tecnicos
habria contradicho sus propias palabras, recogidas en transcripciones que forman parte de esta
misma entrega.

## 4. Por que las tres califican

**`TIC-01`.** Pertenece al area de Tecnologias de la Informacion y Comunicacion. Diagnostica
equipos, sustituye perifericos, retira y formatea maquinas con falla mayor y lleva el registro
de control de clases. Diagnosticar, sustituir perifericos y formatear equipos **es administrar
equipamiento**, no operarlo y reportarlo: es exactamente la frontera que la separa del perfil
de servicios generales.

**`TIC-02`.** Identifica fallos de red y realiza las pruebas necesarias para determinar la
causa cuando fallan los proyectores. Administra la infraestructura de red del aula.

**`TIC-03`.** Responsable del control operativo de las aulas de computacion y de los
laboratorios: revision y mantenimiento de equipos, formateo, instalacion de software,
verificacion de la infraestructura informatica y soporte durante las clases. Declara
aproximadamente dieciocho anios en el cargo.

> **El cargo se toma del documento firmado, no de lo que se recordo despues.** La primera
> version de esta declaracion llamaba a `TIC-01` «Administradora de tecnologias de la
> informacion de laboratorios», que es como se describio la sesion de memoria; el
> consentimiento dice «Asistente de Tecnologias TIC». Manda el papel. Por la misma razon
> `TIC-03` consta como «Laboratorista, Ciencias de la Computacion»: es lo que escribio de su
> puno y letra, y no la formula mas vistosa que llego a figurar en un borrador del acta.

## 5. Como se llego a las tres

La busqueda empezo el **2026-09-04** recorriendo la facultad y las areas de servicio de la
universidad. Ese dia **el area de Tecnologias de la Informacion y Comunicacion estaba en
remodelacion y su personal no se encontraba en la institucion**, que es donde estaria el resto
del personal con el perfil. Se consulto ademas en biblioteca y en el area administrativa;
ninguna de las personas disponibles ese dia administraba sistemas, cuentas, equipamiento o
red. Solo se localizo a `TIC-01`.

La busqueda continuo el **2026-09-05** y dio con `TIC-02`, y el **2026-09-07** con `TIC-03`.

**La causa del retraso fue de calendario, no de plantilla.** Se deja escrito para no atribuir
a la organizacion una carencia de personal tecnico que no tiene.

## 6. Que sigue faltando en la matriz, y por que importa

Diez requisitos de la matriz declaran a `Personal de TI` como destinatario y **ocho no tenian
ninguna evidencia de campo**: `RNF-03`, `RNF-06`, `RNF-09`, `RNF-10`, `RNF-12`, `RD-03`,
`RD-10` y `RD-11`. Sus umbrales se escribieron sin consultar al perfil que tendria que
cumplirlos.

Las tres sesiones cubren lo que se alcanzo a consultar en quince minutos cada una:

| Requisito | Evidencia de campo hoy |
|---|---|
| `RD-10` — control remoto restringido por roles | `EV-27`, `EV-28` |
| `RD-11` — bitacora de acciones para auditoria | `EV-27`, `EV-28` |
| `RNF-01` — alerta de anomalia <= 60 s | `EV-26`, `EV-27`, `EV-28` |
| `RNF-14` — diagnostico de una falla <= 15 min | `EV-12`, `EV-27`, `EV-28` |

**Seis siguen huerfanos**: `RNF-03`, `RNF-06`, `RNF-09`, `RNF-10`, `RNF-12` y `RD-03`. En
`RNF-03` y `RD-03` los tres participantes constan como **«No responde»** en el apartado 4 de
sus actas; no se dan por sostenidos por haber preguntado.

La limitacion que se traslada al manuscrito sigue siendo de muestreo: el perfil que menos se
consulto es el destinatario de los requisitos mas exigentes en umbral --`RNF-06`, `RNF-09` y
`RNF-14`--, de modo que son los que menos respaldo empirico tienen de toda la especificacion.
Se declara como amenaza a la validez de constructo.

## 7. Efecto sobre la evaluacion

El sub-criterio de reparto de perfiles **se cumple**: tres sesiones con usuario tecnico y tres
con usuario no tecnico, cada una con su acta firmada y su grabacion inventariada.

Lo que no se ha subsanado es el **alcance** de esas sesiones: quince minutos por participante
dejan seis umbrales sin consultar, y eso consta arriba en lugar de disolverse en el recuento.

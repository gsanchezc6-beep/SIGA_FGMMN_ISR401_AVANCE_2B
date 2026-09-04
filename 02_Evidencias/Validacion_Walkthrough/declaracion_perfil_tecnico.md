# Declaracion sobre el perfil tecnico en las sesiones de validacion

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos · Entrega Final (2B)
Fecha: 2026-09-04

---

## 1. Que se declara

La guia de la Entrega Final pide **seis sesiones de validacion grabadas con acta firmada, tres
con usuarios tecnicos y tres con usuarios no tecnicos**.

El equipo deposita las sesiones no tecnicas completas y **una sola sesion con usuario
tecnico**. No se alcanzan las tres, y no por falta de gestion: **en la institucion no hay tres
personas que cumplan el perfil**.

Este documento deja constancia de a quien se busco, por que no califica, y que se hizo en su
lugar. No sustituye al requisito ni pretende equivaler a el.

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

## 4. La sesion tecnica que si se realizo

| Campo | Valor |
|---|---|
| Codigo de participante | `TI-01` |
| Identificador de evidencia | `EV-26` |
| Codigo de sesion | `WT-____` |
| Fecha | 2026-09-04 |
| Cargo declarado | Administradora de tecnologias de la informacion de laboratorios |
| Por que califica | Administra el equipamiento y los sistemas de los laboratorios de la facultad. El cargo y la funcion declarada coinciden |

## 5. Por que no hubo mas

La busqueda se realizo el **2026-09-04**, recorriendo la facultad y las areas de servicio de
la universidad.

**El area de Tecnologias de la Informacion y Comunicacion (TICS) estaba en remodelacion ese
dia y su personal no se encontraba en la institucion.** Es el area donde estaria el resto del
personal que cumple el perfil, y es la razon concreta por la que no se pudieron realizar las
otras dos sesiones.

Se consulto ademas en biblioteca por personal que administrara los computadores y las cuentas
de usuario, y en el area administrativa. Ninguna de las personas disponibles ese dia ejercia
funcion de administracion de sistemas, cuentas, equipamiento o red.

La sesion que si se realizo se hizo con la unica persona localizada que cumple el perfil sin
ambiguedad.

## 6. Lo que este hallazgo significa para la especificacion

Que la institucion cuente con **una sola persona** en funcion de administracion tecnica no es
solo una limitacion del muestreo: **es un dato sobre la organizacion cliente**, y afecta a
requisitos que el equipo escribio suponiendo lo contrario.

Diez requisitos de la matriz declaran a `Personal de TI` como destinatario y **ocho no tenian
ninguna evidencia de campo** antes de esta sesion: `RNF-03`, `RNF-06`, `RNF-09`, `RNF-10`,
`RNF-12`, `RD-03`, `RD-10` y `RD-11`. La razon de ese vacio queda ahora explicada: no habia a
quien preguntarle.

Tres de ellos presuponen un equipo tecnico que no existe con ese tamano:

| Requisito | Umbral escrito | Supuesto que no se sostiene |
|---|---|---|
| `RNF-06` | Cobertura de pruebas unitarias `>= 70 %` en modulos criticos | Que exista una funcion de aseguramiento de calidad que la exija y la verifique |
| `RNF-09` | Incorporar un sensor IoT nuevo en `<= 8 horas-persona` | Que haya personal disponible para dedicar esas horas |
| `RNF-14` | Diagnostico de una falla reportada `<= 15 min` | Que haya alguien de guardia para diagnosticar en ese plazo |

Se traslada a la seccion de amenazas a la validez del manuscrito, y al apartado de hallazgos
contraintuitivos: **un sistema disenado para una organizacion se especifico suponiendo una
estructura de soporte que la organizacion no tiene.**

## 7. Efecto sobre la evaluacion

El equipo asume que el sub-criterio de reparto de perfiles **no se cumple** y que eso tiene
consecuencia en la calificacion. Se prefiere declararlo a clasificar mal a un participante:
las actas y las transcripciones se leen juntas, y una contradiccion entre lo que una persona
dice que hace y el perfil que se le asigna es visible de inmediato.

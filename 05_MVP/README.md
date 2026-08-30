# Prototipo funcional — SIGA

Producto Minimo Viable del Sistema Inteligente de Gestion de Aulas.

| | |
|---|---|
| Codigo fuente | [`codigo_fuente/`](codigo_fuente/) — 45 archivos, organizado por modulos |
| Commit de origen | `1ef2873` del repositorio `gsanchezc6-beep/SIGA_FGMMN_MVP` |
| Despliegue | [`despliegue/instrucciones_despliegue.md`](despliegue/instrucciones_despliegue.md) |
| Cobertura de requisitos | [`cobertura_requisitos.csv`](cobertura_requisitos.csv) |
| Video de demostracion | [`demostracion/`](demostracion/) |
| Licencia del codigo | Apache-2.0 |

El codigo se desarrollo en un repositorio separado y se integro aqui para que la cobertura
sea verificable requisito por requisito sobre el codigo del repositorio entregado, como
exige la guia.

---

## Alcance

Seis modulos: autenticacion y roles, panel de control, alertas, mantenimiento, reportes y
bitacora, mas un simulador de sensores que permite ejercitar el sistema sin desplegar
hardware en un aula.

**Cobertura: 17 de los 20 requisitos obligatorios, un 85 %**, frente al 60 % que exige la
guia. El detalle por requisito, con el modulo que lo implementa, esta en
[`cobertura_requisitos.csv`](cobertura_requisitos.csv).

Los tres requisitos obligatorios **no implementados** son RF-20 (historial de ocupacion),
RF-24 (exportacion de datos personales) y RF-25 (rectificacion de datos personales). Los
dos ultimos son derechos reconocidos por la Ley Organica de Proteccion de Datos Personales:
estan especificados y trazados en el ERS, pero **no implementados en el prototipo**, y se
declara asi en lugar de darlos por cubiertos.

---

## Stack

Node.js con Express y Socket.io para el tiempo real, SQLite mediante el modulo nativo
`node:sqlite`, y frontend en HTML, CSS y JavaScript plano. Sin paso de compilacion y sin
dependencias que requieran compilacion nativa. Requiere Node.js >= 22.5.

---

## Declaracion de asistencia recibida en el desarrollo

Conforme a la seccion 5.7 de la guia.

| Aspecto | Detalle |
|---|---|
| **Herramienta** | Claude (Anthropic), como asistente de programacion |
| **Tipo de asistencia** | Generacion de codigo de andamiaje para los modulos de Express y Socket.io, redaccion de consultas SQLite, y depuracion de errores concretos que el equipo identifico al ejecutar el prototipo |
| **Que hizo el equipo** | El diseno de los modulos, la correspondencia de cada modulo con los requisitos del ERS, el modelo de datos, las reglas de negocio de apagado automatico y de alertas, y la verificacion funcional de cada requisito declarado como cubierto |
| **Metodo de validacion** | Cada requisito de `cobertura_requisitos.csv` se verifico ejecutando el prototipo y comprobando su criterio de aceptacion del ERS. Ningun requisito se declara cubierto sin haberlo ejercitado en la aplicacion corriendo |

**Cualquier integrante del equipo puede explicar cualquiera de los modulos**, que es lo que
la guia exige y lo que el tribunal puede comprobar en la defensa.

---

## Credenciales de demostracion

Las cuentas de demostracion estan documentadas en `codigo_fuente/README.md`. Son **cuentas
ficticias creadas para la demostracion**: no corresponden a ninguna persona real de la
organizacion cliente y no dan acceso a ningun sistema institucional.

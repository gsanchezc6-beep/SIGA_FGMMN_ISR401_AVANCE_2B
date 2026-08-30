# Despliegue local del prototipo — SIGA

Reproducible desde cero sobre una instalacion limpia. Verificado el 2026-08-29.

## Requisitos previos

- **Node.js >= 22.5**. El prototipo usa el modulo nativo `node:sqlite`, que aparece en
  esa version. No hay dependencias que requieran compilacion nativa.
- Nada mas. No hay base de datos externa, ni Docker, ni paso de compilacion.

Comprobar la version:

```bash
node --version
```

## Puesta en marcha

Desde `05_MVP/codigo_fuente/`:

```bash
npm install
npm start
```

El servidor queda en <http://localhost:3000>. Al primer arranque se crea la base SQLite y
se siembran datos de ejemplo automaticamente: aulas, sensores, equipos y usuarios de
demostracion.

## Cuentas de demostracion

Las credenciales de demostracion estan en `codigo_fuente/README.md` y en
`codigo_fuente/.env.example`. **Son cuentas ficticias creadas para la demostracion**: no
corresponden a ninguna persona real de la organizacion cliente y no dan acceso a ningun
sistema institucional.

## Detener y reiniciar desde cero

```bash
rm -f siga.sqlite
npm start
```

Borrar el archivo de base de datos devuelve el prototipo a su estado inicial con los datos
sembrados.

## Simulador de sensores

El modulo `src/simulator` genera lecturas ambientales y eventos de ocupacion sin necesidad
de hardware. Es lo que permite ejercitar RF-01, RF-03, RF-08 y las reglas de apagado en una
maquina de escritorio, sin desplegar sensores en un aula.

## Stack

Node.js con Express y Socket.io para el tiempo real, SQLite mediante el modulo nativo, y
frontend en HTML, CSS y JavaScript plano sin paso de compilacion.

## Cobertura de requisitos

Declarada requisito por requisito en [`../cobertura_requisitos.csv`](../cobertura_requisitos.csv):
**17 de los 20 requisitos obligatorios, un 85 %**, por encima del 60 % que exige la guia.

Los tres no implementados son RF-20, RF-24 y RF-25. Los dos ultimos son los derechos de
exportacion y rectificacion de datos personales: estan especificados y trazados, pero no
implementados en el prototipo, y se declara asi en lugar de darlos por cubiertos.

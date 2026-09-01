# Diagramas de flujo de datos

**Proyecto SIGA - Equipo FGMMN - ISR-401 - Entrega Final (2B)**

> Esta carpeta esta vacia a proposito y este archivo explica por que. Git no
> versiona directorios vacios: sin este fichero la carpeta no existiria en un
> clon limpio, y el README estaria nombrando una ruta inexistente.

---

## Que va aqui

Los diagramas de flujo de datos de **nivel 0 y nivel 1**, con sus flujos, entidades
externas, procesos y almacenes.

## Estado

**Depositados.** Los dos niveles constan aqui en fuente editable `.drawio`, `.png` y `.svg`.

| | Entidades externas | Procesos | Almacenes | Flujos |
|---|---|---|---|---|
| Nivel 0 | 10 | 1 | 0 | 25 |
| Nivel 1 | 10 | 8 | 9 | 65 |

Comprobado sobre el archivo depositado: **ningun flujo sin nombre, ninguno entre dos
entidades externas y ninguno entre dos almacenes**, que son las tres reglas que un DFD debe
cumplir. Los diez entidades y los 25 flujos del nivel 0 son los mismos del diagrama de
contexto de `01_Contexto/`: un DFD de nivel 0 y un diagrama de contexto son el mismo
contenido en dos notaciones.

## Una precision sobre su exigibilidad

El criterio **C2** de la rubrica pide, literalmente, *diagramas UML consistentes con
el codigo del MVP* y una matriz de trazabilidad. **La rubrica no menciona los DFD en
ninguna de sus 23 paginas**, y el DFD no es notacion UML. El modelado que el criterio
evalua esta completo en las once carpetas restantes de `03_Modelado/`: 41 diagramas
entre UML e i*.

Los DFD se mantienen porque aportan la vista de flujo de datos que ninguna de las
otras once da, no porque el criterio los reclame.

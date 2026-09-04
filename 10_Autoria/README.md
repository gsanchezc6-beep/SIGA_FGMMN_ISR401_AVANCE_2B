# Evidencia de autoria y de trabajo propio

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Carpeta exigida por la seccion 6 de la guia de desarrollo emitida el 2026-09-02. Su
finalidad es que quede acreditado, de forma verificable, que los artefactos entregados
fueron producidos por las personas que los firman. La guia lo dice sin rodeos: **la ausencia
de esta evidencia no se suple con una declaracion.**

Este README declara el estado real de cada elemento. Lo que falta figura como faltante.

---

## Estado de los doce elementos

| Cod. | Elemento | Estado | Nota |
|---|---|---|---|
| A1 | `bitacora_sesiones.csv` | **Depositado** | Derivado del historial por `generar_bitacora.py`. Una fila por persona y dia con commits |
| A2 | `capturas/` | **Parcial: 1 de 3 por integrante** | Hay una por persona, tomada cada uno en su maquina, con archivo del proyecto, reloj y nombre de sesion visibles. **Faltan dos mas de cada uno** |
| A3 | Fuentes editables | **Depositado** | En el propio arbol, junto a cada imagen exportada. Inventario en `fuentes_editables.md` |
| A4 | `grabaciones/` | **Depositado** | Dos sesiones de 15:18 y 15:43 con pantalla compartida y discusion audible, mas 18 capturas tomadas durante ellas |
| A5 | `notas_campo/` | **Depositado** | Las seis de la ronda terminal, manuscritas, con fecha, hora de inicio y fin, duracion y codigo de participante. Sin nombres propios |
| A6 | `fotos_equipo/` | **Pendiente** | Con dos integrantes identificables y la fecha en los metadatos |
| A7 | `doble_codificacion/` | **Pendiente** | Hasta el 2026-09-02 el equipo eran dos personas y una de ellas hizo toda la codificacion; con la reincorporacion vuelve a ser posible que la hagan dos integrantes distintos |
| A8 | `correspondencia/` | **Depositado** | Tres capturas de la coordinacion de la ronda terminal, con la fecha del sistema visible y los datos de terceros censurados |
| A9 | `declaracion_uso_ia.md` | **Depositado** | Por seccion, incluidas las secciones en las que no se empleo ninguna herramienta |
| A10 | `aporte_individual.md` | **Depositado, sin firmar** | Generado desde el historial por `04_Trazabilidad/generar_aporte_individual.py`. Lleva el bloque de firmas; falta imprimirlo y firmarlo |
| A11 | `exif_inventario.csv` | **Pendiente** | Depende de A6. Se genera con `python 10_Autoria/generar_exif.py` |
| A12 | `.mailmap` | **Depositado** | En la raiz del repositorio, que es donde Git lo lee |

## Las carpetas pendientes y por que no contienen evidencia falsa

`capturas/`, `grabaciones/`, `notas_campo/`, `fotos_equipo/`, `doble_codificacion/` y
`correspondencia/` estan creadas y **cada una contiene solo un `00_LEEME.md`** que explica
que material va dentro, con que nombre y con que precauciones.

Conviene decir por que no hay nada mas. El criterio de piso P3 sanciona con cero cualquier
archivo que anuncie una pieza de evidencia y no la contenga. **Aqui no hay ningun archivo
de ese tipo.** Un `00_LEEME.md` no anuncia una evidencia: anuncia una instruccion, y la
contiene. Un archivo llamado `2026-09-03_CONS-05_NotasCampo.pdf` de cero bytes si afirmaria
que existe una nota de campo que no existe, y eso es lo que el criterio persigue.

Ninguna carpeta se rellena con marcadores de posicion. Cuando el material exista, se
deposita; mientras no exista, la tabla de arriba lo dice.

## Sobre el ritmo del historial

La guia advierte que un repositorio cuyo trabajo aparece concentrado en uno o dos dias no
acredita trabajo distribuido en el tiempo, con independencia de la calidad del resultado.
El equipo lo asume: este repositorio se creo el 2026-08-29 por cambio de rubrica, y el
motivo, las fechas y el repositorio de origen constan en `CHANGELOG.md`, version `2B-1.7.0`.

A partir de la recepcion de la guia, el trabajo se registra el mismo dia en que se realiza.
La bitacora de sesiones permite comprobarlo sin leer el historial completo.

## La lista de verificacion previa

La seccion 11 de la guia exige una lista de doce comprobaciones, firmada por una persona
distinta de quien produjo cada artefacto, depositada como `verificacion_previa.pdf`.

**Las doce se ejecutan, no se marcan a mano:**

```
python 10_Autoria/verificacion_previa.py --clonar
```

Con `--clonar`, el script clona el remoto en una carpeta temporal y comprueba alli, que es
como lo hara el docente. Es la unica forma de detectar lo que solo falla en un clon: fue
asi como aparecieron, en su dia, tres fallos de integridad que la copia de trabajo no
mostraba.

El resultado se escribe en `verificacion_previa.md` y de ahi sale el PDF firmable.

**Estado a 2026-09-03: once de doce.** La que falla es la octava, que exige los doce
elementos A1 a A12 completos, y falla por lo que esta tabla ya declara. Hay que volver a
ejecutarla, y volver a firmarla, cuando se deposite la evidencia pendiente.

Tres comprobaciones quedan como manuales a proposito, y el documento dice por que: que todo
numero proceda de un script exige leer los documentos; que la URL abra sin sesion exige un
navegador sin credenciales; y la busqueda de datos personales da indicios, no pruebas.

## Como se regenera la bitacora

```
python 10_Autoria/generar_bitacora.py
```

Ningun campo se escribe a mano. La hora de inicio de cada sesion es la del primer commit de
esa persona ese dia, y la de fin la del ultimo; el tiempo trabajado antes del primer commit
no se puede reconstruir desde el historial y por eso no se declara.

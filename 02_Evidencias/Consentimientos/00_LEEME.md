# Consentimientos informados

**Proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ**

---

## El registro es lo que hay que mirar primero

[`registro_consentimientos.csv`](registro_consentimientos.csv) ata cada participante con su
evidencia, su archivo de consentimiento y **el alcance que autorizo**. Se regenera con:

```
python 02_Evidencias/Consentimientos/generar_registro.py
```

Existe porque **no todos autorizaron lo mismo**, y sin una tabla que lo diga es facil citar
en el manuscrito a alguien que no lo permitio. La columna `citable_en_manuscrito` responde
esa pregunta de un vistazo.

## Veinte consentimientos de diecisiete personas

| | |
|---|---|
| Personas participantes | **17** |
| Consentimientos firmados | **20** |
| Citables en el manuscrito | **17** |

La diferencia no es un error. **Tres personas participaron en dos sesiones distintas y
firmaron un consentimiento para cada una**: primero su entrevista, meses despues la sesion
de validacion comunicativa del 2026-09-01.

`CONS-01`, `COORD-01` y `DOC-01` aparecen por eso dos veces en el registro, con alcances
distintos:

| Sesion | Alcance | Citable |
|---|---|---|
| Su entrevista (`EV-01`, `EV-02`, `EV-12`) | Curso y publicacion | **Si** |
| Validacion comunicativa (`MC-01`) | Solo ambito del curso | **No** |

**Que una fila diga NO no significa que esa persona sea incitable.** Significa que *esa
sesion* no lo es. Lo que dijo en su entrevista sigue estando disponible para el manuscrito;
lo que dijo en la sesion de validacion, no.

## Los tres alcances que hay en juego

| Grupo | Alcance | Como consta |
|---|---|---|
| Las diez entrevistas de las rondas 1 y 2 | Curso y publicacion | Adenda de segunda ronda del expediente etico de la Entrega 2A |
| La sesion de validacion comunicativa | **Solo curso** | Los tres marcaron la segunda casilla, visible en cada PDF sobre la banda de censura |
| Las seis entrevistas de la ronda terminal | Curso y publicacion | Los seis marcaron la primera casilla del formulario LOPDP de la ronda terminal |
| La sesion de validacion con usuario tecnico (`TIC-01`, `EV-26`) | Curso y publicacion | Marco la primera casilla. El ejemplar que firmo primero llevaba las dos marcadas, que son excluyentes; se le pidio que corrigiera y firmara de nuevo, y solo el corregido se deposito |

## Sobre la censura de los archivos

Todos los PDF depositados llevan **barra negra sobre el nombre manuscrito, la firma y la
cedula**, y dejan visible el codigo de participante, la fecha y **la casilla marcada**, que
es precisamente lo que permite comprobar el alcance sin abrir el original.

La censura esta aplicada **sobre el mapa de bits**, no como un rectangulo dibujado encima.
Un rectangulo en un PDF deja la imagen original debajo y se recupera con cualquier
herramienta; aqui los pixeles estan destruidos y el dato no existe en el archivo.

**Los originales sin censurar no estan en el repositorio** y no deben incorporarse. Se
conservan en el contenedor cifrado descrito en
[`../00_Restringido/README_Restringido.md`](../00_Restringido/README_Restringido.md).

## Una correccion de codigos que conviene conocer

Los seis formularios de la ronda terminal se numeraron en campo **desde `DOC-03`**, sin
contrastar el corpus. Esos codigos estaban tomados: `DOC-04` es un docente entrevistado el
2026-07-30, y `DOC-03` es el participante que **no firmo** el consentimiento y cuya
entrevista quedo invalidada por eso. Un consentimiento firmado bajo ese codigo habria
contradicho lo que declara el expediente.

**La correccion se hizo sobre el papel, antes de escanear**, y los formularios depositados
llevan ya el codigo correcto, de `DOC-05` a `DOC-10`. No se corrigio el escaneo ni se parcheo
el PDF: alterar la imagen de un documento firmado es otra cosa.

Lo unico que se corrigio fue el campo **«Codigo de participante asignado en el estudio»**,
que el propio formulario declara como asignado por el equipo. El nombre, la cedula, la firma,
la fecha y la casilla marcada no se tocaron: eso lo declaro el participante.

## Estado a 2026-09-03

Los veinte consentimientos estan depositados y censurados. Ninguno figura como
pendiente.

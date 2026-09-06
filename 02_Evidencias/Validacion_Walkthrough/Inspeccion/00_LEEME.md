# Inspeccion de la especificacion

**Proyecto SIGA - Equipo FGMMN - ISR-401 - Entrega Final (2B)**

> Esta carpeta esta vacia a proposito y este archivo explica por que. Git no
> versiona directorios vacios: sin este fichero la carpeta no existiria en un
> clon limpio, y el README estaria nombrando una ruta inexistente.

---

## Que va aqui

El registro de la inspeccion formal de la especificacion, su registro de defectos y
el de la re-inspeccion **REINS-01**. Responden a la pregunta de si alguien reviso el
ERS con metodo, y no solo si esta escrito.

## Estado

Los tres estan **celebrados, firmados y depositados**:

| Archivo | Sesion | Cuando |
|---|---|---|
| `2026-09-05_INS-01_Registro_Inspeccion.pdf` | INS-01, inspeccion de Fagan | 2026-09-05, 16:30 a 17:00 |
| `2026-09-05_REINS-01_Registro_Reinspeccion.pdf` | REINS-01, verificacion cruzada | 2026-09-05, 17:00 a 17:30 |
| `registro_defectos.csv` | Los 16 defectos con su estado | Vivo |

Firman los tres integrantes. Los cinco roles de Fagan se reparten entre ellos: Munoz
Quinonez modera y anota, Sanchez Cornejo lee y responde como autor, y Cedeno Avila
inspecciona. En la re-inspeccion verifica quien no corrigio.

## Lo que la re-inspeccion resolvio

De los 16 defectos, **quince quedan cerrados y uno residual**: `DEF-06`, la apertura
individual de camara, que el comite de control de cambios difiere de forma expresa en
`SC-03`. Con eso la metrica de **Correccion** deja de estar pendiente:

```
Correccion = 1 residual / 25 requisitos funcionales = 0,04     (referencia <= 0,05)
```

**El margen es de un solo defecto.** Con dos residuales saldria 0,08 y no cumpliria.

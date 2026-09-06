# Prototipos de interfaz — MU-01 a MU-04

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

---

## 1. Correspondencia

La matriz de trazabilidad referencia estos prototipos por su codigo en **22 de sus 74
filas**, a traves de la columna `ID-Mockup`. La correspondencia entre codigo y archivo no
estaba escrita en ningun sitio; queda fijada aqui.

| Codigo | Archivo | Pantalla | Requisitos que soporta |
|---|---|---|---|
| `MU-01` | `Mockup_Panel.png` | Panel de control centralizado: estado de aulas, temperatura, ocupacion y video | RF-01, RF-02, RF-03, RF-04, RF-05, RF-07, RF-22 |
| `MU-02` | `Mockup_Alertas.png` | Vista de alertas, detalle de la alerta y creacion del ticket | RF-08, RF-10, RF-11 |
| `MU-03` | `Mockup_Mantenimiento.png` | Registro de solicitud de mantenimiento con aula, equipo y prioridad | RF-10, RF-12 |
| `MU-04` | `Mockup_Reportes.png` | Reportes de ocupacion, consumo electrico e incidencias | RF-14, RF-17, RF-18, RF-20 |

Los cuatro se recorrieron con los participantes en las sesiones de validacion, y las actas
de `02_Evidencias/Validacion_Walkthrough/Sesiones_Validacion/` los nombran por estos codigos.

## 2. Herramienta y archivo fuente

Los cuatro prototipos se construyeron en **Figma**.

> **El archivo fuente `.fig` no esta depositado todavia.** Se declara aqui en vez de dejar el
> hueco callado: la guia exige el fuente editable de todo artefacto grafico, con el argumento
> de que sin el no hay prueba de que se construyo y no se descargo. Los cuatro `.png` son
> exportaciones, no originales.

Es la **unica** carpeta de `03_Modelado/` sin fuente nativa. Las otras once llevan su `.vpp`
de Visual Paradigm o su `.drawio` junto a cada imagen.

## 3. Que falta y como se cierra

Exportar el archivo desde Figma --menu del archivo, *Guardar copia local*, que produce un
`.fig`-- y depositarlo en esta carpeta. Con eso el inventario de fuentes editables del
elemento **A3** pasa de 43 a 44 fuentes y `03_Modelado/` queda completo.

Si el `.fig` no se pudiera obtener, la alternativa es el enlace compartido de Figma con
permiso de lectura, **pero es peor**: un enlace puede cambiar o dejar de responder, y quien
revise sin conexion no lo puede comprobar. El `.fig` se basta a si mismo.

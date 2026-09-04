# Inventario de fotografias de entorno

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

Veintinueve fotografias del sitio del cliente, en tres rondas. Cada una se describe por lo
que muestra y por el requisito que sostiene.

**Actualizado el 2026-09-03.** Las once fotografias de la segunda ronda se retiraron y se
sustituyeron por catorce del laboratorio de computo. El motivo, y lo que se pierde con el
cambio, estan explicados mas abajo.

---

## Ronda de campo, junio y julio de 2026 — ENT-01 a ENT-15

Quince fotografias tomadas durante las jornadas de observacion documentadas en las notas de
campo NC-01 a NC-06, que estan en `02_Evidencias/Notas_Campo/` cuando se depositen. Su
descripcion detallada figura en esas notas.

## Segunda ronda, 2026-09-01 — ENT-16 a ENT-26: **retiradas**

Once fotografias de aulas, depositadas en la Entrega Final y **retiradas del
repositorio el 2026-09-03**.

**Por que.** Ninguna de las once conservaba su fecha de captura en los metadatos: se
transfirieron por una via que borra el EXIF, y una fotografia sin ese dato no acredita
cuando se tomo. Solo declaraba su fecha el nombre del archivo, que lo escribe quien lo
nombra.

**Que se pierde, y se dice.** Documentaban **aulas** --- pupitres, luminarias,
tomacorrientes ---, y las que las sustituyen documentan **el laboratorio de computo**.
No son el mismo espacio. El repositorio pierde por tanto la evidencia fotografica de las
aulas de la segunda ronda, y conserva la de la primera (ENT-01 a ENT-15) y la del
laboratorio.

**Que no se pierde.** Los hallazgos que esas fotografias sostenian estan sostenidos
ademas por las entrevistas y por la codificacion tematica, que son la fuente principal.
La fotografia era evidencia de contexto, no la unica base de ningun requisito.

Su registro en `CHANGELOG.md` se conserva sin editar: documenta que existieron y cuando
entraron.

---

## Tercera ronda, 2026-09-03 — ENT-27 a ENT-40

Catorce fotografias del **laboratorio de computo** de la Facultad de Ciencias de la
Computacion, tomadas en una sola sesion entre las 17:26:42 y las 17:28:15. **Las catorce
conservan su fecha de captura, su dispositivo y su hash**, comprobable con:

```
python 10_Autoria/generar_exif.py 02_Evidencias/Fotos_Entorno
```

| Id | Que muestra | Requisito que sostiene |
|---|---|---|
| ENT-27 | Dos puestos de trabajo con monitor, teclado y raton sobre mesa corrida, contra pared de ladrillo visto. Al fondo, la mesa del docente con regleta y perifericos | Parque de equipos que el sistema debe monitorear. RF-01, RF-02 |
| ENT-28 | Fila de puestos con dos monitores apagados y sillas giratorias, junto a un tomacorriente de pared | Puesto tipo y punto electrico disponible para instrumentar. RF-01, RF-22 |
| ENT-29 | Puestos alineados contra la pared de ladrillo, con cable de red azul recorriendo la mesa entre equipos | Cableado de datos existente, base del despliegue IoT. RF-22 |
| ENT-30 | Puesto con monitor de formato grande y sillas de distinto modelo; al fondo, otra fila de equipos | Heterogeneidad del parque: el inventario no es uniforme. RF-01, RF-10 |
| ENT-31 | Puesto con monitor sobre brazo articulado y un segundo monitor en la mesa contigua, contra pared de ladrillo | Variedad de montaje del equipamiento en un mismo espacio. RF-01 |
| ENT-32 | Puestos y sillas junto a una pared con humedad y pintura levantada en la parte baja | Condicion ambiental del recinto, relevante para la vida util del equipo. RF-09 |
| ENT-33 | Puestos contra la pared de ladrillo con una botella de agua sobre la mesa, junto al teclado | Uso real del espacio, con riesgo fisico para el equipamiento. RF-09, RF-10 |
| ENT-34 | Vista cenital de dos filas de puestos, con cable de red azul y perifericos conectados | Densidad de equipos por aula, que condiciona el volumen de telemetria. RF-01, RF-22 |
| ENT-35 | Puesto en esquina y pared con humedad y desprendimiento visible a la altura del zocalo | Deterioro del recinto documentado como contexto de mantenimiento. RF-10 |
| ENT-36 | Mesa corrida con dos puestos completos, monitores apagados y sillas de dos modelos distintos | Estado de reposo del equipamiento fuera de clase. RF-16, RF-21 |
| ENT-37 | Equipo de climatizacion tipo split montado sobre ventana con reja, con su tuberia de drenaje a la vista | Climatizacion existente sobre la que actuan el control remoto y el apagado automatico. RF-05, RF-13, RF-16 |
| ENT-38 | Techo del laboratorio: proyector suspendido, dos luminarias fluorescentes y canalizacion electrica superficial; al fondo, el split y las ventanas con reja | Equipamiento fijo del aula y canalizacion disponible para sensores. RF-13, RF-15, RF-21, RF-22 |
| ENT-39 | Vista general del laboratorio vacio: filas de puestos, proyector, luminarias encendidas y ventanas con reja | Aula desocupada con iluminacion encendida, escenario central del sistema. RF-03, RF-16, RF-21 |
| ENT-40 | Vista general hacia la pizarra: pantalla de proyeccion, proyector, extintor y filas de puestos. **Un monitor permanece encendido en el aula vacia** | Evidencia directa del desperdicio que el sistema busca eliminar: equipo encendido sin ocupacion. RF-03, RF-16, RF-21 |

### Lo que esta ronda aporta y las anteriores no

**El equipamiento fijo del aula, documentado.** ENT-37 y ENT-38 muestran el split de
climatizacion y el proyector con las luminarias y la canalizacion superficial. Son los
tres equipos sobre los que actuan RF-05, RF-13, RF-15 y RF-16, y hasta ahora ninguna
fotografia los mostraba juntos en su montaje real.

**Y el hallazgo central, fotografiado.** ENT-39 y ENT-40 muestran el laboratorio
**vacio**, con las luminarias encendidas y **un monitor todavia encendido**. Es
exactamente el desperdicio que el sistema busca eliminar, y es la unica evidencia
fotografica directa de el que tiene el proyecto.

### Personas en el encuadre

En **ENT-27** y **ENT-40** aparece una persona. En la primera la cabeza queda fuera de
cuadro y en la segunda la figura es pequena y esta de espaldas, pero el original tiene
4064 px de ancho y en una facultad pequena cualquiera de las dos podria reconocerse.

**Ambas estan difuminadas sobre el mapa de bits**, no con un rectangulo superpuesto: los
pixeles estan destruidos y el dato no existe en el archivo. El difuminado se aplico por
script conservando el EXIF; hacerlo en el telefono habria borrado los metadatos, que es
justo lo que da valor a estas fotografias.

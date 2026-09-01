# Inventario de fotografias de entorno

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

Veintiseis fotografias del sitio del cliente, en dos rondas. Cada una se describe por lo
que muestra y por el requisito que sostiene.

---

## Ronda de campo, junio y julio de 2026 — ENT-01 a ENT-15

Quince fotografias tomadas durante las jornadas de observacion documentadas en las notas de
campo NC-01 a NC-06, que estan en `02_Evidencias/Notas_Campo/` cuando se depositen. Su
descripcion detallada figura en esas notas.

## Segunda ronda, 2026-09-01 — ENT-16 a ENT-26

Once fotografias tomadas en aulas de la Facultad de Ciencias de la Computacion.

| Id | Que muestra | Requisito que sostiene |
|---|---|---|
| ENT-16 | Pupitres individuales de tablero laminado con estructura metalica, en el rincon de un aula. Mobiliario movil, sin instalacion fija asociada | Delimita el alcance: la deteccion de ocupacion no puede apoyarse en el puesto del estudiante. RF-03 |
| ENT-17 | Aula vacia con filas de pupitres y luz natural por ventanas altas. Una botella plastica en el suelo | RF-03 deteccion de ocupacion; RF-16 apagado de aulas desocupadas |
| ENT-18 | Pupitres vistos desde el pasillo central del aula, con reflejo de la luz natural en el piso | RF-03 |
| ENT-19 | Vista general del aula vacia, con toda la disposicion de pupitres y las ventanas altas al fondo | RF-03; RF-20 historial de ocupacion |
| ENT-20 | **Techo completo de un aula:** proyector Epson montado, detector de techo, luminarias encendidas, aire acondicionado de pared marca RCA y camara de vigilancia en la esquina | Es el conjunto entero de equipamiento que el sistema monitorea. RF-01, RF-02, RF-04, RF-05, RF-06 |
| ENT-21 | Proyector Epson montado en el techo, junto a una luminaria encendida | RF-04 control remoto de proyectores |
| ENT-22 | **Camara de videovigilancia de marca Dahua**, tipo domo, montada en la esquina de un aula. La marca es legible | RF-06 integracion con el sistema de videovigilancia existente; sostiene la condicion de viabilidad de SC-03 |
| ENT-23 | **Aula vacia con todas las luminarias encendidas a plena luz de dia**, con el proyector, el aire acondicionado y la camara en el mismo encuadre | RF-13 apagado por eficiencia energetica; RF-16 apagado por fin de horario |
| ENT-24 | Tomacorrientes de pared: uno normal, uno regulado de color rojo y un punto de red, con cargadores conectados | Infraestructura electrica y de datos disponible para el despliegue de sensores. RF-01, RF-22 |
| ENT-25 | Pupitre en primer plano, con el detalle del tablero y la estructura | RF-03 |
| ENT-26 | Aula vacia con residuos en el piso y bajo los pupitres: una botella y papel | RF-16; documenta el ciclo de limpieza y la ventana ciega descrita en NC-03 |

---

## Procedencia y limites de esta ronda

**Fecha de captura:** 2026-09-01, declarada por el observador.

**Las once fotografias no conservan metadatos EXIF.** Se transfirieron desde el telefono por
mensajeria, y ese transito elimina los metadatos de origen. Se declara aqui en lugar de
presentar la fecha del archivo como si fuera la de la toma: la fecha de modificacion del
archivo corresponde al momento de la transferencia, no al de la captura.

**Observador:** Sanchez Cornejo, Gary Alberto.

## Un matiz que conviene registrar

La nota de campo NC-05 dejo asentado que, en la jornada del 2026-07-13, **la mayoria de las
aulas sin estudiantes tenia las luces apagadas**, y por eso el hallazgo central del proyecto
se enuncia sobre la climatizacion y no sobre la iluminacion.

**ENT-23 muestra lo contrario en un aula concreta:** vacia, con todas las luminarias
encendidas y con luz natural abundante. No invalida la observacion de julio ni la sustituye:
son aulas distintas en dias distintos. Se registra porque el patron real es
**heterogeneo** --- unas aulas se apagan al salir y otras no --- y esa heterogeneidad es
precisamente el argumento del sistema: el control manual depende de que alguien se acuerde,
y no siempre ocurre.

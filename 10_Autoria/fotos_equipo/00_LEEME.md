# A6 — Fotografias del equipo en la organizacion

Con **al menos dos integrantes identificables** y **la fecha conservada en los metadatos**.

## Lo que arruina esta evidencia

**No las envie por WhatsApp.** El reenvio por mensajeria recomprime la imagen y borra el
EXIF, y con el desaparece la fecha de captura, que es justamente lo que acredita cuando se
tomo. Lo mismo ocurre con la mayoria de los sistemas de mensajeria y con algunas subidas a
la nube.

Pase las fotografias **por cable**, o subalas a Drive sin comprimir y descarguelas como
original.

## Como comprobar que conservan la fecha

```
python 10_Autoria/generar_exif.py
```

Ese script produce `exif_inventario.csv`, el elemento A11, y avisa de cualquier fotografia
que haya perdido sus metadatos. Si avisa, la foto ya no sirve como evidencia fechada y hay
que recuperar el original.

## Nombre del archivo

```
AAAA-MM-DD_Equipo_NN.jpg
```

Conserve el archivo original tal como salio de la camara. No lo recorte ni lo edite.

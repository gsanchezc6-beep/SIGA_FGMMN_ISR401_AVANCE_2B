# -*- coding: utf-8 -*-
"""Genera 10_Autoria/exif_inventario.csv — elemento A11.

Para cada fotografia de 10_Autoria/fotos_equipo/ registra su nombre, la fecha de
captura tomada de los metadatos, el dispositivo y el hash SHA-256.

    python 10_Autoria/generar_exif.py

La guia exige que las fotografias conserven sus metadatos originales, asi que el
script **avisa** de cualquier imagen que haya perdido la fecha de captura. Perder
el EXIF es lo que ocurre al reenviar una foto por mensajeria, y una foto sin fecha
de captura ya no acredita cuando se tomo.

Uso opcional sobre otra carpeta:
    python 10_Autoria/generar_exif.py 02_Evidencias/Fotos_Entorno
"""
import csv
import hashlib
import io
import os
import struct
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
POR_DEFECTO = os.path.join(AQUI, "fotos_equipo")
EXTENSIONES = (".jpg", ".jpeg", ".tif", ".tiff", ".png", ".heic")

# Etiquetas EXIF que interesan.
FECHA_ORIGINAL = 0x9003   # DateTimeOriginal
FECHA_DIGITAL = 0x9004    # DateTimeDigitized
FECHA_ARCHIVO = 0x0132    # DateTime
MARCA = 0x010F            # Make
MODELO = 0x0110           # Model
EXIF_IFD = 0x8769


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for b in iter(lambda: f.read(65536), b""):
            h.update(b)
    return h.hexdigest()


def _leer_ifd(datos, offset, orden, buscados, salida, profundidad=0):
    """Recorre un IFD TIFF y recoge las etiquetas buscadas."""
    if profundidad > 2 or offset + 2 > len(datos):
        return
    n = struct.unpack(orden + "H", datos[offset:offset + 2])[0]
    for i in range(n):
        p = offset + 2 + i * 12
        if p + 12 > len(datos):
            return
        tag, tipo, cuenta = struct.unpack(orden + "HHI", datos[p:p + 8])
        valor_bruto = datos[p + 8:p + 12]

        if tag == EXIF_IFD:
            sub = struct.unpack(orden + "I", valor_bruto)[0]
            _leer_ifd(datos, sub, orden, buscados, salida, profundidad + 1)
            continue
        if tag not in buscados:
            continue

        # Tipo 2 = ASCII. Es el unico que necesitamos.
        if tipo != 2:
            continue
        if cuenta <= 4:
            crudo = valor_bruto[:cuenta]
        else:
            desp = struct.unpack(orden + "I", valor_bruto)[0]
            crudo = datos[desp:desp + cuenta]
        texto = crudo.split(b"\x00")[0].decode("latin-1", "replace").strip()
        if texto:
            salida.setdefault(tag, texto)


def leer_exif(ruta):
    """Devuelve {tag: texto} leyendo el segmento APP1 de un JPEG. Sin dependencias."""
    salida = {}
    try:
        with open(ruta, "rb") as f:
            if f.read(2) != b"\xff\xd8":
                return salida            # no es JPEG
            while True:
                cab = f.read(2)
                if len(cab) < 2 or cab[0] != 0xFF:
                    return salida
                marcador = cab[1]
                if marcador in (0xD8, 0xD9) or 0xD0 <= marcador <= 0xD7:
                    continue
                longitud = struct.unpack(">H", f.read(2))[0]
                cuerpo = f.read(longitud - 2)
                if marcador == 0xE1 and cuerpo[:6] == b"Exif\x00\x00":
                    tiff = cuerpo[6:]
                    orden = "<" if tiff[:2] == b"II" else ">"
                    primero = struct.unpack(orden + "I", tiff[4:8])[0]
                    _leer_ifd(tiff, primero, orden,
                              {FECHA_ORIGINAL, FECHA_DIGITAL, FECHA_ARCHIVO,
                               MARCA, MODELO}, salida)
                    return salida
                if marcador == 0xDA:     # empieza el dato comprimido
                    return salida
    except Exception:
        return salida
    return salida


def main():
    carpeta = sys.argv[1] if len(sys.argv) > 1 else POR_DEFECTO
    if not os.path.isabs(carpeta):
        carpeta = os.path.join(os.path.dirname(AQUI), carpeta)
    if not os.path.isdir(carpeta):
        print("No existe la carpeta: %s" % carpeta)
        return 1

    fotos = sorted(f for f in os.listdir(carpeta)
                   if f.lower().endswith(EXTENSIONES))
    if not fotos:
        print("No hay fotografias en %s" % carpeta)
        print("Deposite primero las de A6 y vuelva a ejecutar.")
        return 0

    filas, sin_fecha, otro_formato = [], [], []
    for nombre in fotos:
        ruta = os.path.join(carpeta, nombre)
        ex = leer_exif(ruta)
        fecha = ex.get(FECHA_ORIGINAL) or ex.get(FECHA_DIGITAL) or ex.get(FECHA_ARCHIVO) or ""
        marca = ex.get(MARCA, "")
        modelo = ex.get(MODELO, "")
        dispositivo = (marca + " " + modelo).strip() or "no consta en los metadatos"
        if not fecha:
            # Un PNG no lleva EXIF en el segmento APP1 de JPEG: es una
            # limitacion del formato, no una senal de que se borraran los
            # metadatos. Se distingue para no acusar en falso.
            if nombre.lower().endswith(".png"):
                otro_formato.append(nombre)
            else:
                sin_fecha.append(nombre)
        filas.append({
            "archivo": nombre,
            "fecha_captura": fecha or "AUSENTE",
            "dispositivo": dispositivo,
            "sha256": sha256(ruta),
            "bytes": os.path.getsize(ruta),
        })

    salida = os.path.join(AQUI, "exif_inventario.csv")
    with io.open(salida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["archivo", "fecha_captura",
                                          "dispositivo", "sha256", "bytes"])
        w.writeheader()
        w.writerows(filas)

    print("exif_inventario.csv")
    print("  %d fotografias inventariadas" % len(filas))
    con = len(filas) - len(sin_fecha) - len(otro_formato)
    print("  %d conservan la fecha de captura en los metadatos" % con)
    if otro_formato:
        print("")
        print("  %d en formato PNG, que no transporta EXIF." % len(otro_formato))
        print("  No es que se hayan borrado los metadatos: el formato no los lleva.")
        print("  Si necesita acreditar la fecha, deposite el original de la camara.")
    if sin_fecha:
        print("")
        print("  AVISO: %d fotografia(s) SIN fecha de captura." % len(sin_fecha))
        print("  Una foto sin EXIF no acredita cuando se tomo. Suele pasar al")
        print("  reenviarla por mensajeria. Recupere el original de la camara:")
        for n in sin_fecha:
            print("    - %s" % n)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

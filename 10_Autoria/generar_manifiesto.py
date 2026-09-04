# -*- coding: utf-8 -*-
"""Regenera `checksums.sha256` sobre los archivos versionados.

    python 10_Autoria/generar_manifiesto.py            escribe el manifiesto
    python 10_Autoria/generar_manifiesto.py --revisar   solo informa, no escribe

Hasta ahora el manifiesto se regeneraba a mano. Eso deja un hueco que la propia
comprobacion no ve: `verificacion_previa.py` recorre las lineas del manifiesto y
comprueba que cada archivo listado sigue teniendo su suma, pero **un archivo
nuevo que nadie anadio al manifiesto no aparece en ninguna linea**, asi que no
falla ninguna comprobacion y queda fuera de la cadena de integridad sin que nada
lo delate. Generarlo desde `git ls-files` cierra ese hueco: entra todo lo
versionado, sin excepcion y sin depender de que alguien se acuerde.

El propio manifiesto se excluye, porque no puede contener su propia suma.

Las sumas se calculan sobre los bytes del archivo tal como esta en disco. Por eso
la comprobacion que vale es la que se hace **sobre un clon limpio**: en la copia
de trabajo pueden quedar finales de linea o archivos que el clon no reproduce.

Solo biblioteca estandar.
"""
import argparse
import hashlib
import io
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, ".."))
MANIFIESTO = os.path.join(RAIZ, "checksums.sha256")
NOMBRE = "checksums.sha256"


def versionados():
    """Rutas versionadas, incluidas las ya preparadas con `git add`."""
    r = subprocess.run(["git", "ls-files"], cwd=RAIZ, capture_output=True)
    if r.returncode != 0:
        raise SystemExit("git ls-files fallo: %s" % r.stderr.decode("utf-8", "replace"))
    salida = r.stdout.decode("utf-8")
    return sorted(p.strip() for p in salida.split("\n")
                  if p.strip() and p.strip() != NOMBRE)


def suma(ruta):
    d = hashlib.sha256()
    with open(ruta, "rb") as f:
        for b in iter(lambda: f.read(65536), b""):
            d.update(b)
    return d.hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--revisar", action="store_true",
                    help="informa de las diferencias sin escribir nada")
    args = ap.parse_args()

    rutas = versionados()
    lineas, ausentes = [], []
    for rel in rutas:
        abs_ = os.path.join(RAIZ, rel.replace("/", os.sep))
        if not os.path.isfile(abs_):
            ausentes.append(rel)
            continue
        lineas.append("%s *./%s" % (suma(abs_), rel))

    if ausentes:
        print("%d archivo(s) versionado(s) que no estan en disco. No se escribe:"
              % len(ausentes))
        for a in ausentes[:10]:
            print("  " + a)
        return 1

    antes = []
    if os.path.isfile(MANIFIESTO):
        antes = [l.rstrip("\n") for l in
                 io.open(MANIFIESTO, encoding="utf-8") if l.strip()]

    ruta_de = lambda l: l.split(" *./", 1)[1]
    previas, nuevas = set(map(ruta_de, antes)), set(map(ruta_de, lineas))
    entran = sorted(nuevas - previas)
    salen = sorted(previas - nuevas)
    cambian = [ruta_de(l) for l in sorted(set(lineas) - set(antes))
               if ruta_de(l) not in entran]

    print("%d entradas (antes %d)" % (len(lineas), len(antes)))
    for etiqueta, grupo in (("entran", entran), ("salen", salen),
                            ("cambian de suma", cambian)):
        if grupo:
            print("  %s: %d" % (etiqueta, len(grupo)))
            for g in grupo[:12]:
                print("    " + g)
            if len(grupo) > 12:
                print("    ... y %d mas" % (len(grupo) - 12))

    if args.revisar:
        print("Modo revision: no se escribio nada.")
        return 0 if not (entran or salen or cambian) else 1

    if not (entran or salen or cambian):
        print("El manifiesto ya estaba al dia. Sin cambios.")
        return 0

    io.open(MANIFIESTO, "w", encoding="utf-8", newline="\n").write(
        "\n".join(lineas) + "\n")
    print("Escrito %s" % NOMBRE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

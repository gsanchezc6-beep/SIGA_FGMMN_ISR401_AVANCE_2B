# -*- coding: utf-8 -*-
"""Etapa 5 - Las tablas y figuras del documento, regeneradas y comprobadas.

Las etapas 1 a 4 reconstruyen el contenido de este paquete. Las tablas y las
figuras que aparecen en el manuscrito y en el reporte las produce la cadena de
analisis del componente empirico, 06_Experimento/replicar.py. Esta etapa la
ejecuta desde aqui, para que la misma orden unica

    python 07_Datos/scripts/ejecutar.py

deje regeneradas tambien las tablas y figuras del documento, y despues las
compara byte a byte con las sumas que constan en el manifiesto de la raiz,
checksums.sha256. Si una sola salida no coincide, la etapa falla y dice cual.

Que se compara: todo lo que el manifiesto registra bajo
    06_Experimento/datos_procesados/
    06_Experimento/resultados/          (salvo entorno_python.txt, que es un
                                         volcado del entorno de quien ejecuta)
    07_Publicacion/tablas/
    07_Publicacion/figuras/
salvo los README de esas carpetas, que no son salidas.

Dependencias. A diferencia de las etapas 1 a 4, esta necesita las seis
bibliotecas del analisis estadistico, con version fijada en
06_Experimento/requirements.txt:

    pip install -r 06_Experimento/requirements.txt

Si falta alguna, la etapa lo dice y termina con codigo 3, sin ejecutar nada.
"""
import hashlib
import importlib.util
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PAQUETE = os.path.dirname(AQUI)
RAIZ = os.path.dirname(PAQUETE)

REPLICAR = os.path.join(RAIZ, "06_Experimento", "replicar.py")
MANIFIESTO = os.path.join(RAIZ, "checksums.sha256")
REQUISITOS = os.path.join(RAIZ, "06_Experimento", "requirements.txt")

CARPETAS = ("06_Experimento/datos_procesados/", "06_Experimento/resultados/",
            "07_Publicacion/tablas/", "07_Publicacion/figuras/")
EXCLUIDOS = ("06_Experimento/resultados/entorno_python.txt",)

MODULOS = {"matplotlib": "matplotlib", "numpy": "numpy", "pandas": "pandas",
           "scikit-learn": "sklearn", "scipy": "scipy", "statsmodels": "statsmodels"}


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def esperadas():
    salida = {}
    with open(MANIFIESTO, encoding="utf-8") as f:
        for linea in f:
            linea = linea.rstrip("\r\n")
            if not linea.strip():
                continue
            suma, ruta = linea.split(" ", 1)
            ruta = ruta.lstrip("*").lstrip()
            if ruta.startswith("./"):
                ruta = ruta[2:]
            if (ruta.startswith(CARPETAS) and ruta not in EXCLUIDOS
                    and not os.path.basename(ruta).upper().startswith("README")):
                salida[ruta] = suma
    return salida


def main():
    faltan = [p for p, m in MODULOS.items() if importlib.util.find_spec(m) is None]
    if faltan:
        print("  Faltan dependencias del analisis: %s" % ", ".join(faltan))
        print("  Instalelas con:  pip install -r %s" % os.path.relpath(REQUISITOS, os.getcwd()))
        return 3

    objetivo = esperadas()
    if not objetivo:
        print("  El manifiesto no registra ninguna salida del documento")
        return 1

    r = subprocess.run([sys.executable, REPLICAR], cwd=RAIZ,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if r.returncode != 0:
        print(r.stdout[-3000:])
        print("  06_Experimento/replicar.py termino con codigo %d" % r.returncode)
        return r.returncode

    distintas, ausentes = [], []
    for ruta, suma in sorted(objetivo.items()):
        absoluta = os.path.join(RAIZ, ruta)
        if not os.path.isfile(absoluta):
            ausentes.append(ruta)
        elif sha256(absoluta) != suma:
            distintas.append(ruta)

    for ruta in ausentes:
        print("    NO SE GENERO  %s" % ruta)
    for ruta in distintas:
        print("    DIFIERE       %s" % ruta)
    n_tab = sum(1 for x in objetivo if x.startswith("07_Publicacion/tablas/"))
    n_fig = sum(1 for x in objetivo if x.startswith("07_Publicacion/figuras/"))
    if ausentes or distintas:
        print("  %d de %d salidas no coinciden con el manifiesto"
              % (len(ausentes) + len(distintas), len(objetivo)))
        return 1
    print("  %d salidas identicas byte a byte al manifiesto: %d tablas, %d figuras "
          "y %d resultados intermedios" % (len(objetivo), n_tab, n_fig,
                                           len(objetivo) - n_tab - n_fig))
    return 0


if __name__ == "__main__":
    sys.exit(main())

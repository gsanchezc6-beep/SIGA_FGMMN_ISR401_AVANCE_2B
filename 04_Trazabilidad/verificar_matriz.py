# -*- coding: utf-8 -*-
"""Comprueba que la columna Estado-Traza coincide con las celdas de cada fila.

    python 04_Trazabilidad/verificar_matriz.py            informa
    python 04_Trazabilidad/verificar_matriz.py --escribir corrige la columna

La columna `Estado-Traza` se escribia a mano, y una columna escrita a mano sobre
setenta y cuatro filas se desincroniza sin que nadie lo note: puede declarar una
fila incompleta cuando ya tiene todos sus eslabones, o al reves. Este script la
recalcula desde las celdas y avisa de cada discrepancia.

**Que cuenta como cadena completa**, tal como lo declara
`huerfanos_y_cadenas_rotas.md`: fuente, caso de uso, clase, proceso, caso de
prueba, historia y criterio. El mockup no entra: hay filas de evidencia y de
restriccion que ninguna pantalla realiza.

Una celda cuenta como declarada cuando dice algo distinto de «Sin ...». «No
aplica» tambien cuenta como declarada: es una respuesta, no un hueco.

Solo biblioteca estandar.
"""
import argparse
import csv
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MATRIZ = os.path.join(AQUI, "matriz_trazabilidad.csv")
ESPEJO = os.path.abspath(os.path.join(
    AQUI, "..", "07_Publicacion", "dataset_zenodo", "matriz_trazabilidad.csv"))

CADENA = [("ID-EV", "fuente"), ("ID-CU", "caso de uso"), ("Clase", "clase"),
          ("Proceso", "proceso"), ("ID-CasoPrueba", "caso de prueba"),
          ("ID-HU", "historia"), ("ID-CA", "criterio")]


def declarada(v):
    v = (v or "").strip()
    return bool(v) and not v.lower().startswith("sin ")


def eslabones_que_faltan(fila):
    return [etq for campo, etq in CADENA if not declarada(fila[campo])]


def estado(fila):
    """El estado que le corresponde a la fila segun sus celdas.

    **La familia declarada se respeta cuando es una restriccion de diseno.** Que
    una fila lo sea es un juicio sobre su naturaleza --se verifica por revision de
    diseno y no por caso de prueba-- y eso no se deduce de las celdas. Lo que este
    script recalcula es el conjunto de eslabones que faltan, que si es mecanico.
    """
    faltan = eslabones_que_faltan(fila)
    es_rd = (fila["Estado-Traza"] or "").strip().lower().startswith("restriccion")
    if not faltan:
        return "Restriccion de diseno" if es_rd else "Completa"
    familia = "Restriccion de diseno" if es_rd else (
        "Huerfana" if "fuente" in faltan else "Parcial")
    return "%s - sin %s" % (familia, ", ".join(faltan))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--escribir", action="store_true",
                    help="corrige la columna en lugar de solo informar")
    args = ap.parse_args()

    filas = list(csv.DictReader(io.open(MATRIZ, encoding="utf-8-sig")))
    campos = list(filas[0].keys())

    discrepancias = []
    for f in filas:
        esperado = estado(f)
        actual = (f["Estado-Traza"] or "").strip()
        # se compara la familia y el conjunto de eslabones, no la redaccion
        fam_e, fam_a = esperado.split(" - ")[0], actual.split(" - ")[0]
        sub_e = set(re.split(r",\s*", esperado.split("sin ", 1)[1])) if "sin " in esperado else set()
        sub_a = set(re.split(r",\s*", actual.split("sin ", 1)[1])) if "sin " in actual else set()
        if fam_e != fam_a or sub_e != sub_a:
            discrepancias.append((f["ID"], f["ID-RF"], actual, esperado))
            if args.escribir:
                f["Estado-Traza"] = esperado

    completas = sum(1 for f in filas if not eslabones_que_faltan(f))
    print("%d filas | %d con la cadena completa | %d con todos sus eslabones declarados"
          % (len(filas), completas, sum(1 for f in filas
             if all(declarada(f[c]) or (f[c] or "").strip() for c, _ in CADENA))))
    print()
    if not discrepancias:
        print("La columna Estado-Traza coincide con las celdas en las %d filas." % len(filas))
        return 0

    print("%d fila(s) en las que la columna no coincide con las celdas:" % len(discrepancias))
    for i, rf, a, e in discrepancias:
        print("   ID %-3s %-24s" % (i, rf[:24]))
        print("        dice     %s" % a)
        print("        deberia  %s" % e)

    if not args.escribir:
        print()
        print("Modo informe: no se escribio nada. Use --escribir para corregir.")
        return 1

    for destino in (MATRIZ, ESPEJO):
        if not os.path.isfile(destino):
            continue
        with io.open(destino, "w", encoding="utf-8-sig", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=campos)
            w.writeheader()
            w.writerows(filas)
    print()
    print("Columna corregida en la matriz y en la copia del deposito.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

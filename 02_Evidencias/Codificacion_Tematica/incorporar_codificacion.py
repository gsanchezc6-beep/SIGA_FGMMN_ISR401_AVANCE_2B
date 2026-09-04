# -*- coding: utf-8 -*-
"""Incorpora una hoja de codificacion rellenada a `codificacion_tematica.csv`.

    python 02_Evidencias/Codificacion_Tematica/incorporar_codificacion.py \\
        "C:\\Users\\...\\turnos_para_codificar.csv" --analista "Sanchez G."

Comprueba antes de escribir, y no escribe nada si algo falla:

  1. Que el fragmento aparece **literalmente** en la transcripcion que la fila
     declara. Un fragmento retocado al copiarlo deja de ser una cita.
  2. Que aparece dentro de un turno **del participante**, no del entrevistador.
     Codificar una frase del entrevistador convierte en dato lo que era la
     pregunta, y eso inflaria el corpus con las palabras del propio equipo.
  3. Que el codigo, la categoria y el requisito derivado estan rellenos.
  4. Que el par (fragmento, codigo) no esta ya en el archivo.

Las filas sin codigo se ignoran en silencio: la hoja lleva todos los turnos
que superan el umbral de palabras, y no todos tienen por que codificarse.

Solo biblioteca estandar.
"""
import argparse
import csv
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(AQUI, "codificacion_tematica.csv")
TRANS = os.path.abspath(os.path.join(AQUI, "..", "Transcripciones"))
CAMPOS = ["Fragmento", "Codigo", "Categoria", "Requisito_derivado",
          "ID_evidencia", "Analista_codificador"]


def turnos_del_participante(ev):
    """Texto de los turnos del participante de esa evidencia, en una lista."""
    for nombre in os.listdir(TRANS):
        if nombre.endswith("_Transcripcion.md") and ("_%s_" % ev) in nombre:
            ruta = os.path.join(TRANS, nombre)
            break
    else:
        return None, None
    cod = nombre.split("_")[2]          # 2026-09-03_Docente_DOC-05_EV-20_...
    cuerpo = io.open(ruta, encoding="utf-8").read().split("\n---\n", 1)[-1]
    turnos = []
    for linea in cuerpo.split("\n"):
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", linea.strip())
        if m and m.group(1).strip() == cod:
            turnos.append(m.group(2).strip())
    return turnos, nombre


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("hoja", help="CSV rellenado con las columnas de codificacion")
    ap.add_argument("--analista", required=True,
                    help="quien codifico, tal como debe figurar en la columna")
    args = ap.parse_args()

    with io.open(args.hoja, encoding="utf-8-sig") as f:
        hoja = list(csv.DictReader(f))
    with io.open(DESTINO, encoding="utf-8-sig") as f:
        ya = list(csv.DictReader(f))
    existentes = set((r["Fragmento"].strip(), r["Codigo"].strip()) for r in ya)

    cache, nuevas, errores = {}, [], []
    for i, fila in enumerate(hoja, 2):      # 2 = primera fila de datos del CSV
        codigo = (fila.get("Codigo") or "").strip()
        nuevo = (fila.get("Codigo_nuevo_propuesto") or "").strip()
        if not codigo and not nuevo:
            continue
        if codigo and nuevo:
            errores.append("fila %d: lleva codigo y codigo nuevo a la vez" % i)
            continue
        codigo = codigo or nuevo

        ev = (fila.get("ID_evidencia") or "").strip()
        frag = (fila.get("Fragmento") or "").strip()
        cat = (fila.get("Categoria") or "").strip()
        req = (fila.get("Requisito_derivado") or "").strip()

        if not cat:
            errores.append("fila %d (%s): sin categoria" % (i, codigo))
            continue
        if not req:
            errores.append("fila %d (%s): sin requisito derivado" % (i, codigo))
            continue

        if ev not in cache:
            cache[ev] = turnos_del_participante(ev)
        turnos, archivo = cache[ev]
        if turnos is None:
            errores.append("fila %d: no hay transcripcion para %s" % (i, ev))
            continue
        if not any(frag in t for t in turnos):
            errores.append("fila %d (%s): el fragmento no aparece literal en un "
                           "turno del participante de %s" % (i, codigo, ev))
            continue
        if (frag, codigo) in existentes:
            errores.append("fila %d: (%s) ya esta en el archivo" % (i, codigo))
            continue

        existentes.add((frag, codigo))
        nuevas.append({"Fragmento": frag, "Codigo": codigo, "Categoria": cat,
                       "Requisito_derivado": req, "ID_evidencia": ev,
                       "Analista_codificador": args.analista})

    if errores:
        print("No se escribio nada. %d fila(s) que revisar:" % len(errores))
        for e in errores:
            print("  " + e)
        return 1
    if not nuevas:
        print("La hoja no trae ninguna fila codificada.")
        return 1

    with io.open(DESTINO, "a", encoding="utf-8", newline="") as f:
        csv.DictWriter(f, fieldnames=CAMPOS).writerows(nuevas)

    codigos_previos = set(r["Codigo"] for r in ya)
    estrenados = sorted(set(r["Codigo"] for r in nuevas) - codigos_previos)
    print("Incorporadas %d filas. El archivo queda en %d."
          % (len(nuevas), len(ya) + len(nuevas)))
    print("Codigos nuevos: %d de %d distintos usados."
          % (len(estrenados), len(set(r["Codigo"] for r in nuevas))))
    for c in estrenados:
        print("  " + c)
    print()
    print("Siguiente paso: regenerar la curva.")
    print("  cd 06_Experimento && make saturacion")
    return 0


if __name__ == "__main__":
    sys.exit(main())

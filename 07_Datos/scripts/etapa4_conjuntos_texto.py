# -*- coding: utf-8 -*-
"""Etapa 4 - Los dos conjuntos de requisitos comparados, en texto plano.

El cuasi-experimento compara dos conjuntos de requisitos funcionales obtenidos
del mismo corpus fuente:

    Conjunto A   generado por el modelo de lenguaje     (brazo LLM)
    Conjunto B   elicitado por el equipo humano         (brazo Humano)

Esta etapa escribe cada conjunto en su propio archivo de texto plano, tal como
lo vieron los jueces: con el identificador ciego y el enunciado literal del
paquete de evaluacion. No redacta, no resume y no corrige nada; separa.

Entradas, las dos en datos_crudos/:
    paquete_evaluacion_ciega.md    el instrumento entregado a los jueces, con
                                   los 51 items en el orden aleatorizado
    asignacion_brazo_items.csv     a que brazo pertenece cada item ciego

Salidas, en datos_procesados/:
    conjunto_A_llm.txt
    conjunto_B_humano.txt

Lo que estas salidas NO contienen es la tabla de desciego: la correspondencia
entre cada item ciego y el codigo real del requisito (RF-nn) sigue fuera del
repositorio publico, como declara 06_Experimento/clave_desciego_UBICACION.md.

El corpus fuente del que salieron ambos conjuntos es
datos_crudos/material_fuente_LLM.txt, las transcripciones anonimizadas que se
entregaron al modelo. Esta etapa comprueba que existe y que no esta vacio.

Solo biblioteca estandar.
"""
import csv
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PAQUETE = os.path.dirname(AQUI)
CRUDOS = os.path.join(PAQUETE, "datos_crudos")
PROC = os.path.join(PAQUETE, "datos_procesados")

PAQUETE_CIEGO = os.path.join(CRUDOS, "paquete_evaluacion_ciega.md")
BRAZOS = os.path.join(CRUDOS, "asignacion_brazo_items.csv")
CORPUS = os.path.join(CRUDOS, "material_fuente_LLM.txt")

SALIDAS = {
    "LLM": ("conjunto_A_llm.txt",
            "Conjunto A - requisitos funcionales generados por el modelo de lenguaje"),
    "Humano": ("conjunto_B_humano.txt",
               "Conjunto B - requisitos funcionales elicitados por el equipo humano"),
}

RE_ITEM = re.compile(r"^\*\*(Item-\d{2})\.\*\*\s+(.+?)\s*$")


def leer_items():
    items = {}
    with io.open(PAQUETE_CIEGO, encoding="utf-8") as f:
        for linea in f:
            m = RE_ITEM.match(linea.strip())
            if m:
                items[m.group(1)] = m.group(2)
    return items


def leer_brazos():
    with io.open(BRAZOS, encoding="utf-8") as f:
        return {r["Item_ciego"]: r["Origen"] for r in csv.DictReader(f)}


def main():
    for ruta in (PAQUETE_CIEGO, BRAZOS, CORPUS):
        if not os.path.isfile(ruta) or os.path.getsize(ruta) == 0:
            print("  FALTA o esta vacio: %s" % os.path.relpath(ruta, PAQUETE))
            return 1

    items = leer_items()
    brazos = leer_brazos()
    if set(items) != set(brazos):
        print("  El paquete y la asignacion de brazos no nombran los mismos items")
        print("    solo en el paquete:    %s" % sorted(set(items) - set(brazos)))
        print("    solo en la asignacion: %s" % sorted(set(brazos) - set(items)))
        return 1
    desconocidos = sorted(set(brazos.values()) - set(SALIDAS))
    if desconocidos:
        print("  Brazo desconocido: %s" % ", ".join(desconocidos))
        return 1

    os.makedirs(PROC, exist_ok=True)
    for brazo, (nombre, titulo) in SALIDAS.items():
        sel = sorted(k for k, v in brazos.items() if v == brazo)
        lineas = [
            titulo,
            "Proyecto SIGA - cuasi-experimento de evaluacion ciega",
            "Generado por 07_Datos/scripts/etapa4_conjuntos_texto.py desde",
            "datos_crudos/paquete_evaluacion_ciega.md y datos_crudos/asignacion_brazo_items.csv.",
            "No editar a mano.",
            "Requisitos: %d" % len(sel),
            "",
        ]
        lineas += ["%s. %s" % (k, items[k]) for k in sel]
        with io.open(os.path.join(PROC, nombre), "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lineas) + "\n")
        print("  %-24s %d requisitos" % (nombre, len(sel)))

    palabras = len(io.open(CORPUS, encoding="utf-8").read().split())
    print("  Corpus fuente comun      material_fuente_LLM.txt, %d palabras" % palabras)
    return 0


if __name__ == "__main__":
    sys.exit(main())

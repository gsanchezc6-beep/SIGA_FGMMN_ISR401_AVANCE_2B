# -*- coding: utf-8 -*-
"""Mide la sincronizacion entre el tablero de gestion y la matriz de trazabilidad.

    python 04_Trazabilidad/sincronizacion_tablero.py <export_jira.csv>

La guia pide un tablero con el backlog sincronizado y un **porcentaje de
sincronizacion calculado y reproducible**. Un tablero que se pobló una vez y
nunca se volvio a mirar no esta sincronizado: esta congelado. Este script
compara las dos listas y dice en que difieren.

**Que se compara.** El identificador de requisito --`RF-01`, `RNF-04`, `RD-02`--
que la matriz declara en `ID-RF` y que el tablero lleva al principio del resumen
de cada actividad. No se comparan textos: se comparan conjuntos de
identificadores, que es lo unico que no depende de como este redactado el titulo.

**Como se obtiene el export.** En Jira, vista *Lista* del espacio, boton de
exportar, *Exportar CSV*. Sirve cualquier CSV que tenga una columna con el
resumen o el titulo de cada actividad.

Se informan las dos direcciones por separado, porque significan cosas distintas:

- **Requisito sin actividad**: el equipo especifico algo que nadie planifico.
- **Actividad sin requisito**: hay trabajo en el tablero que no responde a
  ningun requisito de la especificacion.

Solo biblioteca estandar.
"""
import csv
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
MATRIZ = os.path.join(AQUI, "matriz_trazabilidad.csv")
PATRON = re.compile(r"\b(RF|RNF|RNF-IA|RD)-\d{1,3}\b")


def ids_de_texto(texto):
    return set(m.group(0) for m in PATRON.finditer(texto or ""))


def ids_matriz():
    ids = set()
    with io.open(MATRIZ, encoding="utf-8-sig") as fh:
        for fila in csv.DictReader(fh):
            for trozo in (fila.get("ID-RF") or "").split(";"):
                trozo = trozo.strip()
                if PATRON.fullmatch(trozo):
                    ids.add(trozo)
    return ids


def ids_export(ruta):
    ids = set()
    with io.open(ruta, encoding="utf-8-sig", errors="replace") as fh:
        lector = csv.DictReader(fh)
        campos = [c for c in (lector.fieldnames or [])
                  if c and c.strip().lower() in
                  ("summary", "resumen", "actividad", "titulo", "título")]
        if not campos:
            campos = (lector.fieldnames or [])[:3]   # tolerante: mira las primeras
        for fila in lector:
            for c in campos:
                ids |= ids_de_texto(fila.get(c))
    return ids


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    export = sys.argv[1]
    if not os.path.isfile(export):
        print("No existe el archivo: %s" % export)
        return 2

    repo, tablero = ids_matriz(), ids_export(export)
    if not tablero:
        print("El export no contiene ningun identificador de requisito.")
        print("Compruebe que exporto la columna de resumen.")
        return 1

    comunes = repo & tablero
    solo_repo = sorted(repo - tablero)
    solo_tablero = sorted(tablero - repo)
    union = repo | tablero
    pct = 100.0 * len(comunes) / len(union) if union else 0.0

    print("Sincronizacion entre el tablero de gestion y la matriz")
    print("  requisitos en la matriz ....... %d" % len(repo))
    print("  actividades en el tablero ..... %d" % len(tablero))
    print("  coinciden ..................... %d" % len(comunes))
    print()
    print("  SINCRONIZACION = %d / %d = %.1f %%" % (len(comunes), len(union), pct))
    print()
    if solo_repo:
        print("  %d requisito(s) sin actividad en el tablero:" % len(solo_repo))
        print("     %s" % ", ".join(solo_repo))
    if solo_tablero:
        print("  %d actividad(es) sin requisito en la matriz:" % len(solo_tablero))
        print("     %s" % ", ".join(solo_tablero))
    if not solo_repo and not solo_tablero:
        print("  Las dos listas coinciden exactamente.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

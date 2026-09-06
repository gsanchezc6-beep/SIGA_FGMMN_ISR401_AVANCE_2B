# -*- coding: utf-8 -*-
"""Comprueba que la saturacion no depende del orden de las entrevistas.

    python 02_Evidencias/Codificacion_Tematica/robustez_saturacion.py

El criterio de saturacion mira **las tres ultimas entrevistas** de la serie. Seis
de las dieciseis --- la ronda terminal, `EV-20` a `EV-25` --- se hicieron el mismo
dia, de modo que el orden en que aparecen lo fija el numero de evidencia y no la
hora real. Si la saturacion dependiera de cual de esas seis quedo ultima, el
resultado seria un accidente de como se numeraron.

Este script prueba las 720 ordenaciones posibles de ese bloque, dejando fijas las
diez anteriores, que si tienen fechas distintas. Informa en cuantas satura.

Solo biblioteca estandar.
"""
import csv
import io
import itertools
import os
import sys
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
ENTRADA = os.path.join(AQUI, "codificacion_tematica.csv")

# La ronda terminal: seis entrevistas del 2026-09-03, todas el mismo dia.
MISMO_DIA = ["EV-20", "EV-21", "EV-22", "EV-23", "EV-24", "EV-25"]
VENTANA = 3          # entrevistas que mira el criterio
FRACCION = 0.05      # umbral: 5 % del total acumulado


def codigos_por_entrevista():
    d = defaultdict(set)
    fecha = {}
    for r in csv.DictReader(io.open(ENTRADA, encoding="utf-8-sig")):
        c = r["Codigo"].strip()
        if c:
            d[r["ID_evidencia"]].add(c)
    return d


def satura(orden, por_ev):
    vistos, nuevos = set(), []
    for ev in orden:
        nuevos.append(len(por_ev[ev] - vistos))
        vistos |= por_ev[ev]
    media = sum(nuevos[-VENTANA:]) / float(VENTANA)
    umbral = FRACCION * len(vistos)
    return media <= umbral, media, umbral


def main():
    por_ev = codigos_por_entrevista()
    faltan = [e for e in MISMO_DIA if e not in por_ev]
    if faltan:
        print("Sin codificar todavia: %s" % ", ".join(faltan))
        return 1

    fijas = [e for e in sorted(por_ev) if e not in MISMO_DIA]
    base = fijas + MISMO_DIA
    ok_base, media_base, umbral = satura(base, por_ev)

    print("Entrevistas codificadas: %d  |  codigos distintos: %d"
          % (len(por_ev), len(set().union(*por_ev.values()))))
    print()
    print("Orden depositado (%s ... %s)" % (base[0], base[-1]))
    print("  promedio de codigos nuevos en las ultimas %d: %.3f" % (VENTANA, media_base))
    print("  umbral (%.0f %% del acumulado):               %.3f" % (FRACCION * 100, umbral))
    print("  satura: %s" % ("SI" if ok_base else "NO"))
    print()

    total = ok = 0
    medias = []
    peor = None
    for p in itertools.permutations(MISMO_DIA):
        s, m, _u = satura(fijas + list(p), por_ev)
        total += 1
        ok += 1 if s else 0
        medias.append(m)
        if peor is None or m > peor[0]:
            peor = (m, p)

    print("Las %d ordenaciones posibles del bloque del mismo dia:" % total)
    print("  satura en %d de %d (%.1f %%)" % (ok, total, 100.0 * ok / total))
    print("  promedio de nuevos en las ultimas %d: minimo %.3f, maximo %.3f"
          % (VENTANA, min(medias), max(medias)))
    print("  el peor caso, %.3f, sigue %s del umbral de %.3f"
          % (peor[0], "por debajo" if peor[0] <= umbral else "POR ENCIMA", umbral))
    print("    ese orden es: %s" % " ".join(peor[1]))
    print()
    if ok == total:
        print("La saturacion no depende del orden: se alcanza con cualquiera de las %d."
              % total)
    else:
        print("ATENCION: la saturacion depende del orden. Con %d ordenaciones de %d no se"
              % (total - ok, total))
        print("alcanza, asi que no se puede afirmar sin decir cual se eligio y por que.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

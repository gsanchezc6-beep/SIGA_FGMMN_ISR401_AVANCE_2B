# -*- coding: utf-8 -*-
"""Acuerdo entre los dos codificadores del elemento A7.

    python acuerdo_intercodificador.py

Dos integrantes codificaron **por separado y sin consultarse** el mismo
subconjunto del corpus --EV-20, EV-22 y EV-24, una entrevista de cada perfil--
partiendo del libro de codigos ya en uso en `../codificacion_tematica.csv`.

**Se miden dos cosas distintas, y conviene no confundirlas:**

1. **La decision de codificabilidad.** Ante el mismo turno, ¿los dos deciden que
   dice algo codificable? Es una decision binaria sobre las 39 unidades, y es
   donde de verdad discrepan dos codificadores: no en como nombran lo que ven,
   sino en si ven algo. Se informa con kappa de Cohen.

2. **La asignacion de codigo**, sobre las unidades que ambos decidieron codificar.

El kappa se acompana de un intervalo por bootstrap porque con 39 unidades un
coeficiente puntual no dice nada por si solo.

Solo biblioteca estandar. Reproducible: la semilla esta fijada.
"""
import csv
import io
import os
import random

AQUI = os.path.dirname(os.path.abspath(__file__))
HOJAS = [("Munoz Quinonez, Yeranick Esther", "hoja_codificador_1_Munoz.csv"),
         ("Cedeno Avila, Winston Damian", "hoja_codificador_2_Cedeno.csv")]
SEMILLA = 20260905
REMUESTREOS = 10000


def carga(nombre):
    filas = {}
    with io.open(os.path.join(AQUI, nombre), encoding="utf-8-sig") as fh:
        for x in csv.DictReader(fh):
            clave = (x["ID_evidencia"], x["n"])
            filas[clave] = ((x.get("Codigo") or "").strip(),
                            (x.get("Categoria") or "").strip())
    return filas


def kappa(pares):
    """Kappa de Cohen sobre una decision binaria."""
    n = len(pares)
    if not n:
        return float("nan")
    po = sum(1 for a, b in pares if a == b) / float(n)
    pa = sum(1 for a, _ in pares if a) / float(n)
    pb = sum(1 for _, b in pares if b) / float(n)
    pe = pa * pb + (1 - pa) * (1 - pb)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)


def intervalo(pares):
    random.seed(SEMILLA)
    muestras = []
    for _ in range(REMUESTREOS):
        m = [pares[random.randrange(len(pares))] for _ in pares]
        v = kappa(m)
        if v == v:                      # descarta los NaN de remuestras degeneradas
            muestras.append(v)
    muestras.sort()
    return (muestras[int(0.025 * len(muestras))],
            muestras[int(0.975 * len(muestras))])


def main():
    a, b = carga(HOJAS[0][1]), carga(HOJAS[1][1])
    claves = sorted(set(a) & set(b))
    if not claves:
        print("Las dos hojas no comparten ninguna unidad.")
        return 1

    dec = [(bool(a[k][0]), bool(b[k][0])) for k in claves]
    ambos = [k for k in claves if a[k][0] and b[k][0]]
    k = kappa(dec)
    lo, hi = intervalo(dec)

    print("Doble codificacion --- elemento A7")
    print("  codificador 1: %s" % HOJAS[0][0])
    print("  codificador 2: %s" % HOJAS[1][0])
    print("  subconjunto:   EV-20, EV-22 y EV-24 --- %d unidades comunes" % len(claves))
    print()
    print("1. Decision de codificabilidad")
    print("   acuerdo observado ... %d/%d = %.3f"
          % (sum(1 for x, y in dec if x == y), len(dec),
             sum(1 for x, y in dec if x == y) / float(len(dec))))
    print("   kappa de Cohen ...... %.3f   IC95%% [%.3f, %.3f]" % (k, lo, hi))
    print("   %d remuestreos, semilla %d" % (REMUESTREOS, SEMILLA))
    print()
    print("2. Asignacion de codigo, sobre las %d que ambos codificaron" % len(ambos))
    ig_cod = sum(1 for x in ambos if a[x][0].lower() == b[x][0].lower())
    ig_cat = sum(1 for x in ambos if a[x][1].lower() == b[x][1].lower())
    if ambos:
        print("   mismo codigo ........ %d/%d (%.0f%%)"
              % (ig_cod, len(ambos), 100.0 * ig_cod / len(ambos)))
        print("   misma categoria ..... %d/%d (%.0f%%)"
              % (ig_cat, len(ambos), 100.0 * ig_cat / len(ambos)))
    print()
    print("Discrepancias de codificabilidad:")
    for x in claves:
        if bool(a[x][0]) != bool(b[x][0]):
            quien = HOJAS[0][0] if a[x][0] else HOJAS[1][0]
            print("   %s turno %-4s  solo lo codifico %s" % (x[0], x[1], quien.split(",")[0]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

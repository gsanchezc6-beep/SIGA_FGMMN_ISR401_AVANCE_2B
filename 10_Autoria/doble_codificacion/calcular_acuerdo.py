# -*- coding: utf-8 -*-
"""Calcula el acuerdo entre las dos codificaciones tematicas — elemento A7.

    python 10_Autoria/doble_codificacion/calcular_acuerdo.py

Lee las dos hojas de esta carpeta, comprueba que codifican los mismos
fragmentos y calcula el acuerdo con su intervalo de confianza.

Que se calcula, y por que asi:

  - **Kappa de Cohen sin ponderar.** Los codigos tematicos son nominales: entre
    `Reporte_verbal_sin_registro_digital` y `Falla_recurrente_conexion_HDMI` no
    hay una distancia mayor o menor que entre otros dos. Ponderar exigiria una
    escala que aqui no existe. (En el cuasi-experimento si se pondera, porque
    alli las puntuaciones son ordinales de 1 a 5.)

  - **Intervalo del 95 % por bootstrap** sobre los fragmentos, con semilla
    fijada, para que dos ejecuciones den el mismo intervalo.

  - **Acuerdo por categoria ademas del codigo.** Dos personas pueden discrepar
    en el codigo exacto y coincidir en la categoria; distinguirlo dice si el
    desacuerdo es de matiz o de fondo.

Solo biblioteca estandar.
"""
import csv
import io
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
SEMILLA = 20260904
REPLICAS = 10000
CODIFICADORES = ("ymunozq", "wcedenoa2")


def leer(usuario):
    ruta = os.path.join(AQUI, "hoja_%s.csv" % usuario)
    if not os.path.isfile(ruta):
        return None, ruta
    with io.open(ruta, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f)), ruta


def kappa(a, b):
    """Kappa de Cohen sin ponderar entre dos listas de etiquetas nominales."""
    n = len(a)
    if n == 0:
        return None
    categorias = sorted(set(a) | set(b))
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pe = 0.0
    for c in categorias:
        pe += (a.count(c) / n) * (b.count(c) / n)
    if pe >= 1.0:
        return 1.0 if po == 1.0 else 0.0
    return (po - pe) / (1 - pe)


def ic_bootstrap(pares, rng):
    n = len(pares)
    valores = []
    for _ in range(REPLICAS):
        m = [pares[rng.randrange(n)] for _ in range(n)]
        v = kappa([x for x, _ in m], [y for _, y in m])
        if v is not None:
            valores.append(v)
    if not valores:
        return None, None
    valores.sort()

    def pct(p):
        k = (len(valores) - 1) * p
        i = int(k)
        return valores[i] if i + 1 >= len(valores) else \
            valores[i] + (k - i) * (valores[i + 1] - valores[i])
    return pct(0.025), pct(0.975)


def etiqueta(fila, campo):
    """Codigo asignado. Si se propuso uno nuevo, cuenta como etiqueta propia."""
    v = (fila.get(campo) or "").strip()
    if v:
        return v
    nuevo = (fila.get("Codigo_nuevo_propuesto") or "").strip()
    return ("NUEVO:" + nuevo) if nuevo else ""


def main():
    hojas = {}
    for u in CODIFICADORES:
        filas, ruta = leer(u)
        if filas is None:
            print("Falta %s" % ruta)
            print("Las dos hojas tienen que estar en esta carpeta antes de calcular.")
            return 1
        hojas[u] = filas

    a, b = hojas[CODIFICADORES[0]], hojas[CODIFICADORES[1]]
    if len(a) != len(b):
        print("Las hojas tienen distinto numero de filas: %d y %d" % (len(a), len(b)))
        return 1

    # Los fragmentos tienen que ser los mismos y en el mismo orden.
    for i, (fa, fb) in enumerate(zip(a, b), 1):
        if fa["Fragmento"].strip() != fb["Fragmento"].strip():
            print("La fila %d no codifica el mismo fragmento en las dos hojas." % i)
            return 1

    resultados = []
    for campo, titulo in (("Codigo", "Codigo"), ("Categoria", "Categoria")):
        pares, sin_codificar = [], 0
        for fa, fb in zip(a, b):
            ea = etiqueta(fa, campo) if campo == "Codigo" else (fa.get(campo) or "").strip()
            eb = etiqueta(fb, campo) if campo == "Codigo" else (fb.get(campo) or "").strip()
            if not ea or not eb:
                sin_codificar += 1
                continue
            pares.append((ea, eb))
        if not pares:
            print("Ninguna fila esta codificada en las dos hojas para %s." % titulo)
            return 1
        k = kappa([x for x, _ in pares], [y for _, y in pares])
        rng = random.Random(SEMILLA)
        lo, hi = ic_bootstrap(pares, rng)
        coincidencias = sum(1 for x, y in pares if x == y)
        resultados.append({
            "nivel": titulo,
            "n_fragmentos": len(pares),
            "sin_codificar_en_alguna": sin_codificar,
            "acuerdo_observado": round(100.0 * coincidencias / len(pares), 1),
            "kappa_cohen": round(k, 4),
            "IC95_inferior": round(lo, 4),
            "IC95_superior": round(hi, 4),
            "n_bootstrap": REPLICAS,
            "semilla": SEMILLA,
        })

    salida = os.path.join(AQUI, "acuerdo_doble_codificacion.csv")
    with io.open(salida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(resultados[0].keys()))
        w.writeheader()
        w.writerows(resultados)

    print("acuerdo_doble_codificacion.csv")
    for r in resultados:
        print("  %-10s n=%-3d  acuerdo %5.1f %%  kappa %6.3f  [%6.3f, %6.3f]"
              % (r["nivel"], r["n_fragmentos"], r["acuerdo_observado"],
                 r["kappa_cohen"], r["IC95_inferior"], r["IC95_superior"]))
        if r["sin_codificar_en_alguna"]:
            print("             %d fragmento(s) sin codificar en alguna de las dos, excluidos"
                  % r["sin_codificar_en_alguna"])

    # --- desacuerdos, para poder mirarlos uno a uno ---
    ruta_d = os.path.join(AQUI, "desacuerdos.csv")
    with io.open(ruta_d, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["n", "ID_evidencia", "Fragmento",
                                          "codigo_ymunozq", "codigo_wcedenoa2",
                                          "misma_categoria"])
        w.writeheader()
        n = 0
        for fa, fb in zip(a, b):
            ca, cb = etiqueta(fa, "Codigo"), etiqueta(fb, "Codigo")
            if ca and cb and ca != cb:
                n += 1
                w.writerow({
                    "n": fa["n"], "ID_evidencia": fa["ID_evidencia"],
                    "Fragmento": fa["Fragmento"][:300],
                    "codigo_ymunozq": ca, "codigo_wcedenoa2": cb,
                    "misma_categoria": "Si" if (fa.get("Categoria", "").strip() ==
                                                fb.get("Categoria", "").strip()) else "No",
                })
    print("desacuerdos.csv: %d fragmentos codificados distinto" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())

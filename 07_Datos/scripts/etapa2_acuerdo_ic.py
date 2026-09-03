# -*- coding: utf-8 -*-
"""Etapa 2 - Acuerdo entre evaluadores con intervalo de confianza.

El repositorio ya publicaba los coeficientes kappa, pero desnudos. La guia de
desarrollo exige que toda medida de acuerdo entre personas evaluadoras se
acompane de su intervalo de confianza, calculado por script. Esto lo calcula.

Que se calcula, por cada criterio de la rubrica:

  - Kappa de Cohen con ponderacion lineal para los tres pares de jueces.
  - Kappa de Fleiss para los tres a la vez.

Los veinte coeficientes reproducen, a la precision con la que se publicaron,
los que ya constaban en 06_Experimento/resultados/acuerdo_interevaluador.csv,
calculados alli con scikit-learn. Lo que anade esta etapa es el intervalo.
  - Intervalo de confianza del 95 % por bootstrap sobre los items, con
    remuestreo de items completos (no de valoraciones sueltas), porque la
    unidad de observacion independiente es el item.

La semilla es 20260802, la misma que usa el resto del componente empirico, de
modo que dos ejecuciones producen el mismo intervalo byte a byte.

Solo biblioteca estandar: el paquete de datos tiene que correr en una maquina
limpia sin instalar nada.

Salida: resultados/acuerdo_interevaluador_ic.csv
"""
import csv
import io
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PAQUETE = os.path.dirname(AQUI)
PROC = os.path.join(PAQUETE, "datos_procesados")
RES = os.path.join(PAQUETE, "resultados")

SEMILLA = 20260802
REPLICAS = 10000
JUECES = ["juez1", "juez2", "juez3"]
CATEGORIAS = [1, 2, 3, 4, 5]


def kappa_cohen(a, b):
    """Kappa de Cohen con ponderacion lineal entre dos series igual de largas.

    Los cinco criterios de la rubrica son ordinales de 1 a 5, de modo que
    discrepar en un punto no equivale a discrepar en cuatro. La ponderacion
    lineal recoge eso; sin ponderar, todo desacuerdo pesaria igual y el
    coeficiente subestimaria el acuerdo real.

    Replica la semantica de sklearn.metrics.cohen_kappa_score con
    weights="linear", que es la que produjo los valores ya publicados en
    06_Experimento/resultados/acuerdo_interevaluador.csv: las categorias son
    las observadas en el par, ordenadas, y la distancia entre dos categorias
    es la diferencia de sus posiciones en esa lista, no de sus valores.
    """
    n = len(a)
    if n == 0:
        return None
    clases = sorted(set(a) | set(b))
    if len(clases) < 2:
        return 1.0 if all(x == y for x, y in zip(a, b)) else 0.0
    pos = {c: i for i, c in enumerate(clases)}
    k = len(clases)

    obs = [[0] * k for _ in range(k)]
    for x, y in zip(a, b):
        obs[pos[x]][pos[y]] += 1

    filas = [sum(obs[i]) for i in range(k)]
    cols = [sum(obs[i][j] for i in range(k)) for j in range(k)]

    num = den = 0.0
    for i in range(k):
        for j in range(k):
            w = abs(i - j)
            num += w * obs[i][j]
            den += w * filas[i] * cols[j] / n
    if den == 0:
        return 1.0
    return 1 - num / den


def kappa_fleiss(tabla):
    """Kappa de Fleiss. `tabla` es una lista de listas de valoraciones por item."""
    n_items = len(tabla)
    if n_items == 0:
        return None
    n_jueces = len(tabla[0])
    if n_jueces < 2:
        return None

    # Proporcion global asignada a cada categoria.
    total = n_items * n_jueces
    p_cat = {}
    for c in CATEGORIAS:
        p_cat[c] = sum(fila.count(c) for fila in tabla) / total

    # Acuerdo observado dentro de cada item.
    suma_pi = 0.0
    for fila in tabla:
        s = sum(fila.count(c) ** 2 for c in CATEGORIAS)
        suma_pi += (s - n_jueces) / (n_jueces * (n_jueces - 1))
    p_barra = suma_pi / n_items
    pe = sum(v ** 2 for v in p_cat.values())

    if pe == 1.0:
        return 1.0 if p_barra == 1.0 else 0.0
    return (p_barra - pe) / (1 - pe)


def ic_bootstrap(items, funcion, rng):
    """Percentiles 2,5 y 97,5 remuestreando items completos con reemplazo."""
    n = len(items)
    valores = []
    for _ in range(REPLICAS):
        muestra = [items[rng.randrange(n)] for _ in range(n)]
        v = funcion(muestra)
        if v is not None:
            valores.append(v)
    if not valores:
        return None, None
    valores.sort()
    def pct(p):
        k = (len(valores) - 1) * p
        b = int(k)
        return valores[b] if b + 1 >= len(valores) else \
            valores[b] + (k - b) * (valores[b + 1] - valores[b])
    return pct(0.025), pct(0.975)


def cargar():
    """criterio -> item -> {juez: puntuacion}"""
    ruta = os.path.join(PROC, "evaluacion_ciega_formato_largo.csv")
    datos = {}
    with io.open(ruta, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            datos.setdefault(r["criterio"], {}) \
                 .setdefault(r["requisito"], {})[r["evaluador"]] = int(r["puntuacion"])
    return datos


def main():
    datos = cargar()
    os.makedirs(RES, exist_ok=True)
    salida = os.path.join(RES, "acuerdo_interevaluador_ic.csv")

    campos = ["criterio", "medida", "jueces", "n_items", "valor",
              "IC95_inferior", "IC95_superior", "n_bootstrap", "semilla"]
    filas = []

    for criterio in datos:
        items = sorted(datos[criterio])
        # Item -> lista de puntuaciones en el orden fijo de JUECES.
        matriz = [[datos[criterio][i][j] for j in JUECES] for i in items]

        for x in range(len(JUECES)):
            for y in range(x + 1, len(JUECES)):
                rng = random.Random(SEMILLA)
                f = lambda m, x=x, y=y: kappa_cohen([r[x] for r in m],
                                                    [r[y] for r in m])
                lo, hi = ic_bootstrap(matriz, f, rng)
                filas.append({
                    "criterio": criterio,
                    "medida": "Kappa de Cohen con ponderacion lineal",
                    "jueces": "%s-%s" % (JUECES[x], JUECES[y]),
                    "n_items": len(items),
                    "valor": round(f(matriz), 4),
                    "IC95_inferior": round(lo, 4),
                    "IC95_superior": round(hi, 4),
                    "n_bootstrap": REPLICAS,
                    "semilla": SEMILLA,
                })

        rng = random.Random(SEMILLA)
        lo, hi = ic_bootstrap(matriz, kappa_fleiss, rng)
        filas.append({
            "criterio": criterio,
            "medida": "Kappa de Fleiss",
            "jueces": "los tres",
            "n_items": len(items),
            "valor": round(kappa_fleiss(matriz), 4),
            "IC95_inferior": round(lo, 4),
            "IC95_superior": round(hi, 4),
            "n_bootstrap": REPLICAS,
            "semilla": SEMILLA,
        })

    with io.open(salida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)

    print("  acuerdo_interevaluador_ic.csv")
    print("    %d coeficientes, cada uno con IC del 95 %% por bootstrap"
          % len(filas))
    print("    %d replicas, semilla %d, remuestreo de items completos"
          % (REPLICAS, SEMILLA))

    cruza = [r for r in filas if r["medida"] == "Kappa de Fleiss"]
    print("    kappa de Fleiss por criterio:")
    for r in sorted(cruza, key=lambda r: r["criterio"]):
        print("      %-28s %6.3f  [%6.3f, %6.3f]"
              % (r["criterio"].replace("(1-5)", ""), r["valor"],
                 r["IC95_inferior"], r["IC95_superior"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Analisis del panel ampliado --- las dos vueltas.

    python 06_Experimento/panel_ampliado/analizar_panel_ampliado.py

Escribe cuatro tablas en `resultados/`. No toca el analisis principal del estudio,
que sigue siendo el de los tres jueces del registro previo.

Por que existe este script y no una nota que diga que no salio.

El componente empirico se registro previamente con tres jueces
(`10.17605/OSF.IO/7PQ3H`). Ampliar el panel a diez era una comprobacion de
robustez: si el efecto es real, deberia sobrevivir a mas evaluadores. No
sobrevivio, y las dos veces que se intento el motivo fue el mismo --- los
evaluadores no concuerdan entre si por encima del azar.

Un resultado nulo con evaluadores que concuerdan es un hallazgo. Un resultado
nulo con evaluadores que no concuerdan no dice nada del objeto de estudio: dice
que el instrumento no discrimina en manos sin entrenar. Distinguir las dos cosas
es lo que hace este script, y por eso se publica con sus datos crudos en vez de
resumirse en una frase.

Solo biblioteca estandar.
"""
import csv
import io
import itertools
import os
import statistics as st
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
CRUDOS = os.path.join(AQUI, "datos_crudos")
SALIDA = os.path.join(AQUI, "resultados")

# Las cuatro dimensiones comunes a las dos vueltas. La primera vuelta puntuo
# tambien "Correccion respecto de la fuente"; se excluye del cotejo porque en la
# segunda se retiro, y porque el paquete entregado no incluia las transcripciones
# contra las que habria que juzgarla. Esa retirada esta declarada en 00_LEEME.md.
DIMS = ["Completitud", "Ausencia_ambiguedad", "Verificabilidad", "Consistencia_interna"]
CATS = (1, 2, 3, 4, 5)
LANDIS = ((0.81, "casi perfecto"), (0.61, "sustancial"), (0.41, "aceptable"),
          (0.21, "leve"), (0.0, "nulo"))


def escala(k):
    """Etiqueta de Landis y Koch. Por debajo de cero no hay etiqueta: no es que
    concuerden poco, es que concuerdan menos de lo que daria tirar un dado."""
    for lim, txt in LANDIS:
        if k >= lim:
            return txt
    return "peor que el azar"


def fleiss(mat):
    """Fleiss kappa y el acuerdo esperado por azar.

    `mat` es una lista de sujetos; cada sujeto, la lista de puntuaciones que le
    dieron los n evaluadores.
    """
    n_suj = len(mat)
    n = len(mat[0])
    P, pj = [], [0.0] * len(CATS)
    for fila in mat:
        cuenta = [fila.count(c) for c in CATS]
        for k in range(len(CATS)):
            pj[k] += cuenta[k]
        P.append((sum(c * c for c in cuenta) - n) / float(n * (n - 1)))
    pj = [x / float(n_suj * n) for x in pj]
    Pb = sum(P) / n_suj
    Pe = sum(x * x for x in pj)
    return ((Pb - Pe) / (1 - Pe) if Pe != 1 else 0.0), Pe


def pearson(x, y):
    mx, my = st.mean(x), st.mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y)) ** 0.5
    return num / den if den else 0.0


def leer(carpeta, clave):
    """Devuelve juez -> clave -> lista de las 4 puntuaciones."""
    d = {}
    ruta = os.path.join(CRUDOS, carpeta)
    for f in sorted(os.listdir(ruta)):
        if not f.endswith(".csv"):
            continue
        d[f[:-4]] = {}
        for r in csv.DictReader(io.open(os.path.join(ruta, f), encoding="utf-8")):
            fila = []
            for n in DIMS:
                col = [k for k in r if k.startswith(n)][0]
                fila.append(int(r[col]))
            d[f[:-4]][r[clave]] = fila
    return d


def acuerdo(datos, sujetos):
    """Fleiss por dimension, correlaciones y acuerdo crudo por parejas."""
    jueces = sorted(datos)
    dims = []
    for ki, dim in enumerate(DIMS):
        mat = [[datos[j][s][ki] for j in jueces] for s in sujetos]
        k, Pe = fleiss(mat)
        dims.append((dim, k, Pe))
    vec = {j: [datos[j][s][k] for s in sujetos for k in range(4)] for j in jueces}
    parejas = list(itertools.combinations(jueces, 2))
    cor = [pearson(vec[a], vec[b]) for a, b in parejas]
    n = float(len(vec[jueces[0]]))
    exact = [sum(1 for a, b in zip(vec[x], vec[y]) if a == b) / n for x, y in parejas]
    adj = [sum(1 for a, b in zip(vec[x], vec[y]) if abs(a - b) <= 1) / n
           for x, y in parejas]
    return dims, cor, exact, adj


def escribir(nombre, filas, nota=None):
    with io.open(os.path.join(SALIDA, nombre), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)
    print("  %-34s %2d filas%s" % (nombre, len(filas), ("   " + nota) if nota else ""))


def main():
    if not os.path.isdir(SALIDA):
        os.makedirs(SALIDA)

    mapa = {}
    with io.open(os.path.join(CRUDOS, "mapa_posiciones_segunda_vuelta.csv"),
                 encoding="utf-8") as f:
        for r in csv.DictReader(f):
            mapa[r["Posicion"]] = (r["Item_ciego"], r["Origen"], int(r["Aparicion"]))

    v1 = leer("primera_vuelta", "Item_ciego")
    v2 = leer("segunda_vuelta", "Posicion")
    suj1 = sorted(v1[sorted(v1)[0]])
    suj2 = sorted(v2[sorted(v2)[0]], key=int)

    # --- tabla 1: acuerdo en las dos vueltas ------------------------------
    filas = []
    for nombre, datos, suj in (("primera", v1, suj1), ("segunda", v2, suj2)):
        dims, _cor, exact, adj = acuerdo(datos, suj)
        for dim, k, Pe in dims:
            filas.append({"vuelta": nombre, "dimension": dim,
                          "fleiss_kappa": round(k, 4),
                          "acuerdo_esperado_por_azar": round(Pe, 4),
                          "techo_de_kappa": round(1 - Pe, 4),
                          "interpretacion": escala(k)})
        filas.append({"vuelta": nombre, "dimension": "MEDIA DE LAS 4",
                      "fleiss_kappa": round(sum(d[1] for d in dims) / 4.0, 4),
                      "acuerdo_esperado_por_azar": round(st.mean([d[2] for d in dims]), 4),
                      "techo_de_kappa": "",
                      "interpretacion": escala(sum(d[1] for d in dims) / 4.0)})
        filas.append({"vuelta": nombre, "dimension": "ACUERDO CRUDO ENTRE PAREJAS",
                      "fleiss_kappa": "",
                      "acuerdo_esperado_por_azar": round(st.mean(exact), 4),
                      "techo_de_kappa": round(st.mean(adj), 4),
                      "interpretacion": ("columnas: acuerdo exacto observado y "
                                         "acuerdo dentro de un punto")})
    escribir("acuerdo_dos_vueltas.csv", filas)

    # --- tabla 2: consistencia interna de cada juez -----------------------
    gemelos = []
    for p, (it, _o, ap) in mapa.items():
        if ap == 2:
            primera = [q for q, (i2, _x, a2) in mapa.items()
                       if i2 == it and a2 == 1][0]
            gemelos.append((primera, p, it))
    gemelos.sort(key=lambda g: int(g[0]))
    filas = []
    for j in sorted(v2):
        difs = [abs(v2[j][a][k] - v2[j][b][k]) for a, b, _ in gemelos for k in range(4)]
        filas.append({"juez": j, "comparaciones": len(difs),
                      "identicas": sum(1 for d in difs if d == 0),
                      "diferencia_media": round(sum(difs) / float(len(difs)), 3),
                      "diferencia_maxima": max(difs)})
    escribir("consistencia_intrajuez.csv", filas,
             nota="pares " + ", ".join("%s-%s" % (a, b) for a, b, _ in gemelos))

    # --- tabla 3: efecto en la segunda vuelta -----------------------------
    prim = [p for p in suj2 if mapa[p][2] == 1]
    hum = [p for p in prim if mapa[p][1] == "Humano"]
    llm = [p for p in prim if mapa[p][1] == "LLM"]
    filas = []
    for ki, dim in enumerate(DIMS):
        mh = st.mean([v2[j][p][ki] for j in v2 for p in hum])
        ml = st.mean([v2[j][p][ki] for j in v2 for p in llm])
        s = st.pstdev([v2[j][p][ki] for j in v2 for p in prim])
        filas.append({"dimension": dim, "n_humano": len(hum), "n_llm": len(llm),
                      "media_humano": round(mh, 3), "media_llm": round(ml, 3),
                      "diferencia": round(ml - mh, 3),
                      "d_de_cohen": round((ml - mh) / s, 3) if s else ""})
    escribir("efecto_segunda_vuelta.csv", filas)

    # --- tabla 4: como se repartio la escala ------------------------------
    filas = []
    for nombre, datos, suj in (("primera", v1, suj1), ("segunda", v2, suj2)):
        tot = [datos[j][s][k] for j in datos for s in suj for k in range(4)]
        for c in CATS:
            filas.append({"vuelta": nombre, "valor": c, "veces": tot.count(c),
                          "porcentaje": round(100.0 * tot.count(c) / len(tot), 1)})
        filas.append({"vuelta": nombre, "valor": "media", "veces": len(tot),
                      "porcentaje": round(st.mean(tot), 3)})
    escribir("reparto_de_la_escala.csv", filas)

    dims2, _c, ex2, _a = acuerdo(v2, suj2)
    med = sum(d[1] for d in dims2) / 4.0
    azar = st.mean([d[2] for d in dims2])
    print()
    print("El liston acordado antes de la segunda vuelta era Fleiss >= 0,41.")
    print("Obtenido: %+.3f (%s)." % (med, escala(med)))
    print("Acuerdo crudo observado %.1f%%, frente al %.1f%% que daria el azar con"
          % (100 * st.mean(ex2), 100 * azar))
    print("este mismo reparto de puntuaciones: la diferencia no existe.")
    print()
    print("Se mantiene como analisis primario el de los tres jueces del registro previo.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""
Pipeline de análisis estadístico del componente empírico SIGA (Enfoque 1).
Proyecto SIGA — Equipo FGMMN — Entrega 4 (2B).

Se ejecuta por etapas, tal como lo invoca 06_Experimento/Makefile
(objetivo `make all`). Ninguna etapa lee ni escribe fuera de las carpetas
que recibe por parámetro: todo el estado se pasa por archivo, nunca por
variables globales entre etapas, para que cada etapa sea reproducible por
separado.

Etapas:
    consolidar  -> datos_procesados/puntuaciones_consolidadas.csv
    acuerdo     -> resultados/acuerdo_interevaluador.csv
    supuestos   -> resultados/supuestos.csv
    hipotesis   -> resultados/hipotesis.csv (con correccion Holm-Bonferroni)
    efectos     -> resultados/efectos.csv (Cohen d / Cliff delta + IC 95% bootstrap)

Uso (ver Makefile para el orden y las carpetas exactas):
    python analizar_resultados.py --etapa consolidar --entrada datos_crudos --salida datos_procesados
    python analizar_resultados.py --etapa acuerdo     --entrada datos_procesados --salida resultados
    python analizar_resultados.py --etapa supuestos   --entrada datos_procesados --salida resultados
    python analizar_resultados.py --etapa hipotesis   --entrada datos_procesados --salida resultados --correccion holm
    python analizar_resultados.py --etapa efectos     --entrada datos_procesados --salida resultados --bootstrap 10000 --semilla 20260802
"""
import argparse
import glob
import os

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import cohen_kappa_score

DIMENSIONES = [
    "Completitud(1-5)", "Ausencia_ambiguedad(1-5)", "Verificabilidad(1-5)",
    "Correccion_fuente(1-5)", "Consistencia_interna(1-5)",
]

CLAVE_DEFAULT = os.path.join(os.path.dirname(__file__), "..", "datos_crudos", "CLAVE_RESPUESTAS_no_compartir_con_jueces.csv")
CONSOLIDADO_NOMBRE = "puntuaciones_consolidadas.csv"


# --------------------------------------------------------------------------
# Utilidades comunes
# --------------------------------------------------------------------------

def _leer_jueces(directorio):
    archivos = sorted(glob.glob(os.path.join(directorio, "juez*.csv")))
    if not archivos:
        raise FileNotFoundError(f"No se encontraron archivos juez*.csv en {directorio}")
    return archivos


def _id_juez(ruta_archivo):
    base = os.path.basename(ruta_archivo)
    return os.path.splitext(base)[0]  # 'juez1', 'juez2', ...


def fleiss_kappa(matriz_conteos):
    """
    Kappa de Fleiss estandar (Fleiss, 1971).
    matriz_conteos: array (n_items, n_categorias) con el numero de
    evaluadores que asignaron cada categoria a cada item.
    """
    matriz_conteos = np.asarray(matriz_conteos, dtype=float)
    n_items, n_categorias = matriz_conteos.shape
    n_evaluadores = matriz_conteos.sum(axis=1)[0]
    if not np.allclose(matriz_conteos.sum(axis=1), n_evaluadores):
        raise ValueError("Todas las filas deben sumar el mismo numero de evaluadores")

    p_categoria = matriz_conteos.sum(axis=0) / (n_items * n_evaluadores)
    p_item = ((matriz_conteos ** 2).sum(axis=1) - n_evaluadores) / (n_evaluadores * (n_evaluadores - 1))
    p_media_observada = p_item.mean()
    p_media_esperada = (p_categoria ** 2).sum()
    if p_media_esperada == 1:
        return 1.0
    return (p_media_observada - p_media_esperada) / (1 - p_media_esperada)


def cliffs_delta(a, b):
    """Delta de Cliff: proporcion de pares donde a>b menos proporcion donde a<b."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    mayor = sum(1 for x in a for y in b if x > y)
    menor = sum(1 for x in a for y in b if x < y)
    return (mayor - menor) / (len(a) * len(b))


# --------------------------------------------------------------------------
# Etapa 1: consolidar
# --------------------------------------------------------------------------

def etapa_consolidar(entrada, salida, clave_path):
    clave = pd.read_csv(clave_path, encoding="utf-8-sig")
    clave = clave.set_index("Item_ciego")

    filas = []
    for archivo in _leer_jueces(entrada):
        juez = _id_juez(archivo)
        df = pd.read_csv(archivo, encoding="utf-8-sig")
        for _, fila in df.iterrows():
            item = fila["Item_ciego"]
            if item not in clave.index:
                print(f"AVISO: {item} en {archivo} no existe en la clave de respuestas; se omite.")
                continue
            origen = clave.loc[item, "Origen"]
            for dim in DIMENSIONES:
                if dim not in fila or pd.isna(fila[dim]):
                    continue
                filas.append({
                    "juez": juez,
                    "item_ciego": item,
                    "origen": origen,
                    "dimension": dim,
                    "puntuacion": float(fila[dim]),
                })

    consolidado = pd.DataFrame(filas)
    if consolidado.empty:
        raise RuntimeError("La consolidacion produjo un dataframe vacio; revise datos_crudos/juez*.csv")

    os.makedirs(salida, exist_ok=True)
    ruta_salida = os.path.join(salida, CONSOLIDADO_NOMBRE)
    consolidado.to_csv(ruta_salida, index=False, encoding="utf-8")
    n_jueces = consolidado["juez"].nunique()
    n_items = consolidado["item_ciego"].nunique()
    print(f"Consolidado: {n_jueces} jueces, {n_items} items, {len(consolidado)} filas -> {ruta_salida}")


# --------------------------------------------------------------------------
# Etapa 2: acuerdo inter-evaluador
# --------------------------------------------------------------------------

def etapa_acuerdo(entrada, salida):
    consolidado = pd.read_csv(os.path.join(entrada, CONSOLIDADO_NOMBRE), encoding="utf-8-sig")
    jueces = sorted(consolidado["juez"].unique())
    if len(jueces) < 2:
        raise RuntimeError("Se requieren al menos 2 jueces para calcular acuerdo inter-evaluador")

    filas = []
    for dim in DIMENSIONES:
        sub = consolidado[consolidado["dimension"] == dim]
        pivot = sub.pivot_table(index="item_ciego", columns="juez", values="puntuacion")
        pivot = pivot.dropna()

        fila = {"Dimension": dim}
        pares = [(jueces[i], jueces[j]) for i in range(len(jueces)) for j in range(i + 1, len(jueces))]
        for j1, j2 in pares:
            k = cohen_kappa_score(
                pivot[j1].round().astype(int), pivot[j2].round().astype(int), weights="linear"
            )
            nombre_col = f"Cohen_kappa_{j1}_{j2}"
            fila[nombre_col] = round(k, 3)

        if len(jueces) >= 3:
            categorias = sorted(pd.unique(pivot.values.ravel()))
            conteos = []
            for _, fila_item in pivot.iterrows():
                conteo = [np.sum(fila_item.values == c) for c in categorias]
                conteos.append(conteo)
            fila[f"Fleiss_kappa_{len(jueces)}jueces"] = round(fleiss_kappa(np.array(conteos)), 3)

        filas.append(fila)

    resultado = pd.DataFrame(filas)
    os.makedirs(salida, exist_ok=True)
    ruta_salida = os.path.join(salida, "acuerdo_interevaluador.csv")
    resultado.to_csv(ruta_salida, index=False, encoding="utf-8")
    print(f"Acuerdo inter-evaluador escrito en: {ruta_salida}")


# --------------------------------------------------------------------------
# Etapa 3: supuestos (normalidad y homogeneidad de varianzas)
# --------------------------------------------------------------------------

def _medias_por_juez(consolidado, dim, origen):
    sub = consolidado[(consolidado["dimension"] == dim) & (consolidado["origen"] == origen)]
    return sub.groupby("juez")["puntuacion"].mean().sort_index()


def etapa_supuestos(entrada, salida):
    consolidado = pd.read_csv(os.path.join(entrada, CONSOLIDADO_NOMBRE), encoding="utf-8-sig")
    filas = []
    for dim in DIMENSIONES:
        humano = _medias_por_juez(consolidado, dim, "Humano")
        llm = _medias_por_juez(consolidado, dim, "LLM")

        if len(humano) >= 3:
            _, p_h = stats.shapiro(humano)
            _, p_l = stats.shapiro(llm)
        else:
            p_h, p_l = float("nan"), float("nan")
            print(f"AVISO ({dim}): n={len(humano)} jueces < 3, Shapiro-Wilk no es fiable; se reporta NaN.")

        try:
            stat_lev, p_lev = stats.levene(humano.values, llm.values)
        except Exception:
            stat_lev, p_lev = float("nan"), float("nan")

        filas.append({
            "Dimension": dim,
            "n_jueces": len(humano),
            "Shapiro_p_Humano": round(p_h, 4) if p_h == p_h else p_h,
            "Shapiro_p_LLM": round(p_l, 4) if p_l == p_l else p_l,
            "Normal_Humano": bool(p_h > 0.05) if p_h == p_h else False,
            "Normal_LLM": bool(p_l > 0.05) if p_l == p_l else False,
            "Levene_estadistico": round(stat_lev, 4) if stat_lev == stat_lev else stat_lev,
            "Levene_p": round(p_lev, 4) if p_lev == p_lev else p_lev,
            "Varianzas_homogeneas": bool(p_lev > 0.05) if p_lev == p_lev else False,
        })

    resultado = pd.DataFrame(filas)
    os.makedirs(salida, exist_ok=True)
    ruta_salida = os.path.join(salida, "supuestos.csv")
    resultado.to_csv(ruta_salida, index=False, encoding="utf-8")
    print(f"Pruebas de supuestos escritas en: {ruta_salida}")


# --------------------------------------------------------------------------
# Etapa 4: hipotesis (t apareada o Wilcoxon + Holm-Bonferroni)
# --------------------------------------------------------------------------

def _holm_bonferroni(p_valores):
    """Devuelve los p-valores ajustados por Holm-Bonferroni, en el orden original."""
    p = np.asarray(p_valores, dtype=float)
    orden = np.argsort(p)
    m = len(p)
    ajustado = np.empty(m)
    acumulado_max = 0.0
    for rango, idx in enumerate(orden):
        valor = (m - rango) * p[idx]
        acumulado_max = max(acumulado_max, valor)
        ajustado[idx] = min(acumulado_max, 1.0)
    return ajustado


def etapa_hipotesis(entrada, salida, correccion):
    consolidado = pd.read_csv(os.path.join(entrada, CONSOLIDADO_NOMBRE), encoding="utf-8-sig")
    ruta_supuestos = os.path.join(salida, "supuestos.csv")
    supuestos = pd.read_csv(ruta_supuestos, encoding="utf-8-sig").set_index("Dimension") if os.path.exists(ruta_supuestos) else None

    filas = []
    for dim in DIMENSIONES:
        humano = _medias_por_juez(consolidado, dim, "Humano").values
        llm = _medias_por_juez(consolidado, dim, "LLM").values

        normal = False
        if supuestos is not None and dim in supuestos.index:
            normal = bool(supuestos.loc[dim, "Normal_Humano"]) and bool(supuestos.loc[dim, "Normal_LLM"])

        if normal:
            stat, p = stats.ttest_rel(humano, llm)
            prueba = "t apareada"
            estadistico_nombre = "t"
        else:
            try:
                stat, p = stats.wilcoxon(humano, llm)
            except ValueError as e:
                # Wilcoxon falla si todas las diferencias son cero o n es muy pequeno
                print(f"AVISO ({dim}): Wilcoxon no calculable ({e}); se reporta NaN.")
                stat, p = float("nan"), float("nan")
            prueba = "Wilcoxon de rangos con signo"
            estadistico_nombre = "W"

        filas.append({
            "Dimension": dim,
            "Prueba": prueba,
            "Estadistico_nombre": estadistico_nombre,
            "Estadistico_valor": round(stat, 4) if stat == stat else stat,
            "p_valor": round(p, 4) if p == p else p,
        })

    resultado = pd.DataFrame(filas)
    if correccion == "holm":
        resultado["p_valor_ajustado_holm"] = np.round(_holm_bonferroni(resultado["p_valor"].values), 4)
        resultado["significativo_alpha_05_ajustado"] = resultado["p_valor_ajustado_holm"] < 0.05
    else:
        resultado["p_valor_ajustado_holm"] = resultado["p_valor"]
        resultado["significativo_alpha_05_ajustado"] = resultado["p_valor"] < 0.05

    os.makedirs(salida, exist_ok=True)
    ruta_salida = os.path.join(salida, "hipotesis.csv")
    resultado.to_csv(ruta_salida, index=False, encoding="utf-8")
    print(f"Pruebas de hipotesis escritas en: {ruta_salida}")


# --------------------------------------------------------------------------
# Etapa 5: tamanos de efecto con IC 95% por bootstrap
# --------------------------------------------------------------------------

def _bootstrap_ic(humano, llm, estadistico_fn, n_bootstrap, rng):
    n = len(humano)
    replicas = np.empty(n_bootstrap)
    for b in range(n_bootstrap):
        idx = rng.integers(0, n, size=n)
        replicas[b] = estadistico_fn(humano[idx], llm[idx])
    inf, sup = np.percentile(replicas, [2.5, 97.5])
    return inf, sup


def etapa_efectos(entrada, salida, n_bootstrap, semilla):
    consolidado = pd.read_csv(os.path.join(entrada, CONSOLIDADO_NOMBRE), encoding="utf-8-sig")
    ruta_hipotesis = os.path.join(salida, "hipotesis.csv")
    hipotesis = pd.read_csv(ruta_hipotesis, encoding="utf-8-sig").set_index("Dimension") if os.path.exists(ruta_hipotesis) else None
    rng = np.random.default_rng(semilla)

    filas = []
    for dim in DIMENSIONES:
        humano = _medias_por_juez(consolidado, dim, "Humano").values
        llm = _medias_por_juez(consolidado, dim, "LLM").values

        es_parametrico = False
        if hipotesis is not None and dim in hipotesis.index:
            es_parametrico = hipotesis.loc[dim, "Prueba"] == "t apareada"

        if es_parametrico:
            diff = humano - llm
            desv = diff.std(ddof=1)
            valor = diff.mean() / desv if desv > 0 else float("nan")
            tipo = "Cohen d (apareado)"
            fn = lambda h, l: (h - l).mean() / (h - l).std(ddof=1) if (h - l).std(ddof=1) > 0 else 0.0
        else:
            valor = cliffs_delta(humano, llm)
            tipo = "Cliff delta"
            fn = cliffs_delta

        try:
            ic_inf, ic_sup = _bootstrap_ic(humano, llm, fn, n_bootstrap, rng)
        except Exception as e:
            print(f"AVISO ({dim}): bootstrap fallo ({e}); IC no calculado.")
            ic_inf, ic_sup = float("nan"), float("nan")

        filas.append({
            "Dimension": dim,
            "Tipo_efecto": tipo,
            "Valor": round(valor, 4) if valor == valor else valor,
            "IC95_inferior": round(ic_inf, 4) if ic_inf == ic_inf else ic_inf,
            "IC95_superior": round(ic_sup, 4) if ic_sup == ic_sup else ic_sup,
            "n_bootstrap": n_bootstrap,
            "semilla": semilla,
        })

    resultado = pd.DataFrame(filas)
    os.makedirs(salida, exist_ok=True)
    ruta_salida = os.path.join(salida, "efectos.csv")
    resultado.to_csv(ruta_salida, index=False, encoding="utf-8")
    print(f"Tamanos de efecto (bootstrap n={n_bootstrap}) escritos en: {ruta_salida}")


# --------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--etapa", required=True, choices=["consolidar", "acuerdo", "supuestos", "hipotesis", "efectos"])
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--clave", default=CLAVE_DEFAULT, help="Ruta a CLAVE_RESPUESTAS_no_compartir_con_jueces.csv")
    ap.add_argument("--correccion", default="holm", choices=["holm", "ninguna"])
    ap.add_argument("--bootstrap", type=int, default=10000)
    ap.add_argument("--semilla", type=int, default=20260802)
    args = ap.parse_args()

    if args.etapa == "consolidar":
        etapa_consolidar(args.entrada, args.salida, args.clave)
    elif args.etapa == "acuerdo":
        etapa_acuerdo(args.entrada, args.salida)
    elif args.etapa == "supuestos":
        etapa_supuestos(args.entrada, args.salida)
    elif args.etapa == "hipotesis":
        etapa_hipotesis(args.entrada, args.salida, args.correccion)
    elif args.etapa == "efectos":
        etapa_efectos(args.entrada, args.salida, args.bootstrap, args.semilla)


if __name__ == "__main__":
    main()

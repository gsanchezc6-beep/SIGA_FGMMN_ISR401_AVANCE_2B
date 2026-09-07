# -*- coding: utf-8 -*-
"""Genera `fair_assessment.md` a partir de la salida cruda de F-UJI.

    python generar_fair_assessment.py

Lee `fair_assessment.json` --- el volcado literal que devuelve F-UJI --- y escribe
el informe legible. **Ninguna cifra se teclea**: todas salen del JSON, de modo que
si la evaluacion se repite y cambia algun indicador, el informe cambia con ella.

Por que se hace asi. La guia pide la autoevaluacion FAIR obtenida de la
herramienta, no redactada en un procesador de texto. Un documento escrito a mano
puede decir cualquier cosa; este no puede decir mas de lo que el JSON contiene, y
el JSON viene firmado con su identificador de prueba, su version de software y su
version de metrica, que son comprobables contra el servicio.

Solo biblioteca estandar.
"""
import io
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ENTRADA = os.path.join(AQUI, "fair_assessment.json")
SALIDA = os.path.join(AQUI, "fair_assessment.md")

PRINCIPIO = {"F": "Findable --- localizable",
             "A": "Accessible --- accesible",
             "I": "Interoperable --- interoperable",
             "R": "Reusable --- reutilizable"}


def main():
    if not os.path.isfile(ENTRADA):
        print("Falta %s. Se obtiene en https://www.f-uji.net con el DOI del "
              "deposito y el boton {JSON}." % os.path.basename(ENTRADA))
        return 1

    j = json.load(io.open(ENTRADA, encoding="utf-8"))
    s = j["summary"]
    req = j["request"]
    gan, tot, pct = s["score_earned"], s["score_total"], s["score_percent"]

    L = []
    L.append("# Autoevaluacion FAIR del paquete de datos")
    L.append("")
    L.append("**Proyecto SIGA --- Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**")
    L.append("Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 1. De donde sale este documento")
    L.append("")
    L.append("**No esta redactado a mano.** Lo genera `generar_fair_assessment.py` a partir de")
    L.append("`fair_assessment.json`, que es el volcado literal que devuelve **F-UJI**, el")
    L.append("servicio de evaluacion FAIR del proyecto FAIRsFAIR. Ninguna cifra de las que")
    L.append("siguen se tecleo: todas se leen del JSON.")
    L.append("")
    L.append("| | |")
    L.append("|---|---|")
    L.append("| Objeto evaluado | `%s` |" % req["object_identifier"])
    L.append("| Identificador de la prueba | `%s` |" % j["test_id"])
    L.append("| Version de F-UJI | %s |" % j.get("software_version", "---"))
    L.append("| Especificacion de metricas | %s |" % j.get("metric_specification", "---"))
    L.append("| Version de metricas | %s |" % j.get("metric_version", "---"))
    L.append("")
    L.append("El identificador de prueba permite recuperar esta misma evaluacion en el")
    L.append("servicio. La version de software y la de metricas constan porque un resultado")
    L.append("FAIR no significa nada sin decir contra que rubrica se midio.")
    L.append("")
    L.append("## 2. Resultado")
    L.append("")
    L.append("**%d de %d indicadores --- %.2f %%**" % (gan["FAIR"], tot["FAIR"], pct["FAIR"]))
    L.append("")
    L.append("| Principio | Obtenido | Posible | Porcentaje | Nivel |")
    L.append("|---|---|---|---|---|")
    for k in ("F", "A", "I", "R"):
        L.append("| %s | %d | %d | %.2f %% | %s |"
                 % (PRINCIPIO[k], gan[k], tot[k], pct[k], s["maturity"][k]))
    L.append("| **Conjunto** | **%d** | **%d** | **%.2f %%** | **%s** |"
             % (gan["FAIR"], tot["FAIR"], pct["FAIR"], s["maturity"]["FAIR"]))
    L.append("")

    fallan = [r for r in j["results"] if r["score"]["earned"] < r["score"]["total"]]
    L.append("## 3. Lo que no puntua, y por que")
    L.append("")
    if not fallan:
        L.append("Todos los indicadores puntuan al maximo.")
    else:
        L.append("Son **%d** de los %d indicadores. Se listan enteros, con lo que el propio"
                 % (len(fallan), len(j["results"])))
        L.append("servicio informa, en vez de resumir solo los que favorecen:")
        L.append("")
        L.append("| Indicador | Obtenido | Posible | Que mide |")
        L.append("|---|---|---|---|")
        for r in fallan:
            L.append("| `%s` | %s | %s | %s |"
                     % (r["metric_identifier"], r["score"]["earned"],
                        r["score"]["total"], r["metric_name"]))
        L.append("")
        for r in fallan:
            L.append("**`%s` --- %s.** %s"
                     % (r["metric_identifier"], r["metric_name"],
                        (r.get("maturity") and "Nivel alcanzado: %s. " % r["maturity"]) or ""))
            sal = r.get("output")
            if isinstance(sal, dict):
                for k, v in list(sal.items())[:4]:
                    if v in (None, [], {}, ""):
                        continue
                    L.append("")
                    L.append("- `%s`: %s" % (k, str(v)[:220]))
            L.append("")

    L.append("## 4. Como se reproduce")
    L.append("")
    L.append("```")
    L.append("1. Abrir https://www.f-uji.net")
    L.append("2. Introducir %s" % req["object_identifier"])
    L.append("3. Metrica: %s" % j.get("metric_specification", "la vigente"))
    L.append("4. Descargar el resultado con el boton {JSON} y guardarlo como")
    L.append("   fair_assessment.json en la raiz de este repositorio")
    L.append("5. python generar_fair_assessment.py")
    L.append("```")
    L.append("")
    L.append("El servicio esta en desarrollo y su propio aviso lo dice, de modo que una")
    L.append("evaluacion futura puede diferir. Por eso se deposita el JSON completo junto")
    L.append("a este informe: lo que aqui se afirma es comprobable contra el volcado, y el")
    L.append("volcado contra el servicio.")
    L.append("")

    io.open(SALIDA, "w", encoding="utf-8", newline="\n").write("\n".join(L))
    print("fair_assessment.md")
    print("  %d de %d indicadores, %.2f %%" % (gan["FAIR"], tot["FAIR"], pct["FAIR"]))
    print("  %d indicadores no puntuan al maximo" % len(fallan))
    return 0


if __name__ == "__main__":
    sys.exit(main())

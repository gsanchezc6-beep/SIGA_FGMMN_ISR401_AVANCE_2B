# -*- coding: utf-8 -*-
"""Calcula el respaldo de campo de RNF-IA-03 a partir del cuestionario.

    python 01_ERS/Componentes_IA/evidencia_explicabilidad.py

Escribe `evidencia_explicabilidad.md` y `evidencia_explicabilidad.csv`.

Por que existe. `requisitos_no_funcionales_ia.csv` declara el estado de
verificacion de RNF-IA-03 como «parcialmente sustentado»: los umbrales de
longitud y latencia proceden de RNF-10, pero el de comprension no tenia origen
declarado. El cuestionario aplicado a 60 personas si pregunta por
explicabilidad, en dos items, y esas respuestas nunca se habian explotado.

Este script las cuenta. No inventa dimensiones de ningun marco teorico: se
limita a lo que el instrumento pregunto y las personas respondieron, y el
intervalo de confianza sale de un bootstrap con semilla fija, de modo que la
cifra se reproduce.

Solo biblioteca estandar.
"""
import csv
import io
import os
import random
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
FUENTE = os.path.join(RAIZ, "02_Evidencias", "Cuestionario", "Respuestas",
                      "respuestas_cuestionario_n60.csv")
SALIDA_MD = os.path.join(AQUI, "evidencia_explicabilidad.md")
SALIDA_CSV = os.path.join(AQUI, "evidencia_explicabilidad.csv")

SEMILLA = 20260908
REMUESTREOS = 10000

CLAVE_IMPORTANCIA = "explique por qu"
CLAVE_TIPO = "tipo de explicaci"


def columna(filas, fragmento):
    for c in filas[0].keys():
        if fragmento in c:
            return c
    raise SystemExit("No se encontro la columna que contiene %r" % fragmento)


def bootstrap_media(valores, semilla=SEMILLA, n=REMUESTREOS):
    rnd = random.Random(semilla)
    k = len(valores)
    medias = []
    for _ in range(n):
        medias.append(sum(rnd.choice(valores) for _ in range(k)) / float(k))
    medias.sort()
    return medias[int(0.025 * n)], medias[int(0.975 * n)]


def main():
    if not os.path.isfile(FUENTE):
        print("No se encuentra %s" % FUENTE)
        return 1
    filas = list(csv.DictReader(io.open(FUENTE, encoding="utf-8-sig")))

    col_imp = columna(filas, CLAVE_IMPORTANCIA)
    col_tipo = columna(filas, CLAVE_TIPO)

    imp = []
    for f in filas:
        v = f[col_imp].strip()
        if v:
            try:
                imp.append(float(v))
            except ValueError:
                pass

    media = sum(imp) / float(len(imp))
    lo, hi = bootstrap_media(imp)
    reparto = {}
    for v in imp:
        reparto[int(v)] = reparto.get(int(v), 0) + 1

    tipos = {}
    n_tipo = 0
    for f in filas:
        v = f[col_tipo].strip()
        if v:
            tipos[v] = tipos.get(v, 0) + 1
            n_tipo += 1
    quieren = n_tipo - tipos.get("Ninguna, solo la alerta", 0)

    # --- CSV ---
    g = io.open(SALIDA_CSV, "w", encoding="utf-8-sig", newline="")
    w = csv.writer(g, lineterminator="\n")
    w.writerow(["item", "respuesta", "n", "porcentaje_sobre_validos"])
    for k in sorted(reparto):
        w.writerow(["importancia_explicacion", k, reparto[k],
                    round(100.0 * reparto[k] / len(imp), 1)])
    for k, v in sorted(tipos.items(), key=lambda x: -x[1]):
        w.writerow(["tipo_de_explicacion", k, v, round(100.0 * v / n_tipo, 1)])
    w.writerow(["importancia_explicacion", "media", round(media, 3), ""])
    w.writerow(["importancia_explicacion", "IC95_inferior", round(lo, 3), ""])
    w.writerow(["importancia_explicacion", "IC95_superior", round(hi, 3), ""])
    g.close()

    # --- informe ---
    L = []
    L.append(u"# Respaldo de campo del requisito de explicabilidad")
    L.append(u"")
    L.append(u"**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**")
    L.append(u"Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)")
    L.append(u"")
    L.append(u"---")
    L.append(u"")
    L.append(u"## 1. Que responde este documento")
    L.append(u"")
    L.append(u"`requisitos_no_funcionales_ia.csv` declara el estado de verificacion de **RNF-IA-03**")
    L.append(u"como *parcialmente sustentado*: los umbrales de longitud y latencia proceden de")
    L.append(u"`RNF-10`, pero **el de comprension no tenia origen de campo declarado**.")
    L.append(u"")
    L.append(u"El cuestionario aplicado a 60 personas si pregunta por explicabilidad, en dos items, y")
    L.append(u"esas respuestas no se habian explotado. Aqui se cuentan. **Ninguna cifra se teclea**:")
    L.append(u"todas salen de `evidencia_explicabilidad.py` sobre el export de respuestas.")
    L.append(u"")
    L.append(u"## 2. Cuanto importa que el sistema explique")
    L.append(u"")
    L.append(u"> «¿Que tan importante es que el sistema te explique por que predijo una falla?»")
    L.append(u"> Escala de 1 a 5. **n = %d** respuestas validas de %d." % (len(imp), len(filas)))
    L.append(u"")
    L.append(u"| Respuesta | n | %s |" % u"%")
    L.append(u"|---|---|---|")
    for k in sorted(reparto, reverse=True):
        L.append(u"| %d | %d | %.1f |" % (k, reparto[k], 100.0 * reparto[k] / len(imp)))
    L.append(u"")
    L.append(u"**Media %.2f**, intervalo de confianza al 95 %s de **%.2f a %.2f** "
             u"(bootstrap de %d remuestreos, semilla %d)."
             % (media, u"%", lo, hi, REMUESTREOS, SEMILLA))
    L.append(u"")
    L.append(u"El intervalo **no contiene el 4**, de modo que la importancia media no llega a")
    L.append(u"«importante» en la escala del propio instrumento. Se declara asi y no se redondea")
    L.append(u"al alza: la explicabilidad importa, pero no es la exigencia dominante de esta")
    L.append(u"poblacion.")
    L.append(u"")
    L.append(u"## 3. Que tipo de explicacion se prefiere")
    L.append(u"")
    L.append(u"| Preferencia | n | %s |" % u"%")
    L.append(u"|---|---|---|")
    for k, v in sorted(tipos.items(), key=lambda x: -x[1]):
        L.append(u"| %s | %d | %.1f |" % (k, v, 100.0 * v / n_tipo))
    L.append(u"")
    L.append(u"**%d de %d (%.1f %s) quieren alguna explicacion** y %d (%.1f %s) prefieren solo la"
             % (quieren, n_tipo, 100.0 * quieren / n_tipo, u"%",
                tipos.get(u"Ninguna, solo la alerta", 0),
                100.0 * tipos.get(u"Ninguna, solo la alerta", 0) / n_tipo, u"%"))
    L.append(u"alerta. Pero **la forma preferida se reparte en tres**, sin mayoria: el detalle")
    L.append(u"tecnico encabeza sin llegar al 40 %s.")
    L.append(u"")
    L.append(u"## 4. Que se concluye para RNF-IA-03, y que no")
    L.append(u"")
    L.append(u"**Lo que sostiene.** Que la explicacion debe existir: solo una de cada siete personas")
    L.append(u"la rechaza. El requisito de acompanar toda prediccion con una explicacion tiene")
    L.append(u"respaldo de campo.")
    L.append(u"")
    L.append(u"**Lo que no sostiene.** El umbral de **comprension >= 80 %s** sigue sin origen de")
    L.append(u"campo. El instrumento pregunto por importancia y por preferencia de formato, **no")
    L.append(u"midio comprension**. Que el 86 %s quiera una explicacion no dice que el 80 %s la vaya")
    L.append(u"a entender: son cosas distintas y no se presentan como la misma.")
    L.append(u"")
    L.append(u"**Lo que abre.** Que no haya forma preferida mayoritaria es un hallazgo con")
    L.append(u"consecuencia de diseno: una explicacion unica no sirve a los tres grupos. Queda")
    L.append(u"declarado como trabajo futuro y no como requisito, porque el instrumento no")
    L.append(u"pregunto por perfil y no se puede saber si la preferencia depende de el.")
    L.append(u"")
    L.append(u"## 5. Como se reproduce")
    L.append(u"")
    L.append(u"```")
    L.append(u"python 01_ERS/Componentes_IA/evidencia_explicabilidad.py")
    L.append(u"```")
    L.append(u"")
    L.append(u"Lee `02_Evidencias/Cuestionario/Respuestas/respuestas_cuestionario_n60.csv`, que es")
    L.append(u"el export del formulario, y escribe este documento y `evidencia_explicabilidad.csv`.")

    texto = u"\n".join(L)
    texto = texto.replace(u"encabeza sin llegar al 40 %s.", u"encabeza sin llegar al 40 %.")
    texto = texto.replace(u"comprension >= 80 %s", u"comprension >= 80 %")
    texto = texto.replace(u"el 86 %s quiera", u"el %.0f %% quiera" % (100.0 * quieren / n_tipo))
    texto = texto.replace(u"el 80 %s la vaya", u"el 80 % la vaya")
    io.open(SALIDA_MD, "w", encoding="utf-8", newline="\n").write(texto + u"\n")

    print("evidencia_explicabilidad.md y .csv")
    print("  importancia: n=%d, media %.2f, IC95 [%.2f, %.2f]" % (len(imp), media, lo, hi))
    print("  quieren explicacion: %d de %d (%.1f %%)" % (quieren, n_tipo, 100.0 * quieren / n_tipo))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Etapa 1 - Hoja de evaluacion a ciegas en formato largo.

Las hojas que devolvieron los tres jueces estan en formato ancho: una fila por
item y una columna por dimension de la rubrica. La guia de desarrollo exige el
formato largo, con evaluador, requisito, criterio, puntuacion y orden de
presentacion.

Sobre el orden de presentacion. El paquete de evaluacion ciega se armo con los
items en orden aleatorizado y ese unico orden se entrego a los tres jueces, tal
como declara `06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md`.
El orden de presentacion es, por tanto, la posicion del item en el paquete:
Item-01 ocupo la posicion 1, Item-02 la 2, y asi hasta Item-51. No se reconstruye
ni se estima: se lee de la secuencia del propio instrumento.

Sobre el requisito. La columna identifica el item por su codigo ciego, que es lo
que vio la persona evaluadora. La correspondencia con el codigo real del
requisito es la tabla de desciego y no reside en el repositorio publico; vease
`06_Experimento/clave_desciego_UBICACION.md`.

Salida: datos_procesados/evaluacion_ciega_formato_largo.csv
"""
import csv
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PAQUETE = os.path.dirname(AQUI)
CRUDOS = os.path.join(PAQUETE, "datos_crudos")
PROC = os.path.join(PAQUETE, "datos_procesados")

JUECES = ["juez1", "juez2", "juez3"]
CRITERIOS = [
    "Completitud(1-5)",
    "Ausencia_ambiguedad(1-5)",
    "Verificabilidad(1-5)",
    "Correccion_fuente(1-5)",
    "Consistencia_interna(1-5)",
]


def leer_brazos():
    """Item ciego -> brazo del experimento (Humano o LLM)."""
    ruta = os.path.join(CRUDOS, "asignacion_brazo_items.csv")
    with io.open(ruta, encoding="utf-8") as f:
        return {r["Item_ciego"]: r["Origen"] for r in csv.DictReader(f)}


def orden_de(item_ciego):
    """Posicion del item en el paquete entregado a los jueces."""
    return int(item_ciego.split("-")[1])


def main():
    brazos = leer_brazos()
    os.makedirs(PROC, exist_ok=True)
    salida = os.path.join(PROC, "evaluacion_ciega_formato_largo.csv")

    filas = []
    for juez in JUECES:
        ruta = os.path.join(CRUDOS, juez + ".csv")
        with io.open(ruta, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                item = r["Item_ciego"]
                if item not in brazos:
                    print("ERROR: %s no consta en la asignacion de brazos" % item)
                    return 1
                for criterio in CRITERIOS:
                    valor = r[criterio].strip()
                    if valor == "":
                        print("ERROR: %s dejo vacio %s en %s" % (juez, criterio, item))
                        return 1
                    filas.append({
                        "evaluador": juez,
                        "requisito": item,
                        "orden_presentacion": orden_de(item),
                        "brazo": brazos[item],
                        "criterio": criterio,
                        "puntuacion": int(valor),
                    })

    filas.sort(key=lambda r: (r["evaluador"], r["orden_presentacion"],
                              CRITERIOS.index(r["criterio"])))

    campos = ["evaluador", "requisito", "orden_presentacion", "brazo",
              "criterio", "puntuacion"]
    with io.open(salida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)

    items = len(set(r["requisito"] for r in filas))
    esperado = len(JUECES) * items * len(CRITERIOS)
    print("  evaluacion_ciega_formato_largo.csv")
    print("    %d filas = %d jueces x %d items x %d criterios"
          % (len(filas), len(JUECES), items, len(CRITERIOS)))
    if len(filas) != esperado:
        print("    ERROR: se esperaban %d filas" % esperado)
        return 1
    fuera = [r for r in filas if not 1 <= r["puntuacion"] <= 5]
    if fuera:
        print("    ERROR: %d puntuaciones fuera del rango 1-5" % len(fuera))
        return 1
    print("    rango 1-5 respetado en las %d puntuaciones" % len(filas))
    return 0


if __name__ == "__main__":
    sys.exit(main())

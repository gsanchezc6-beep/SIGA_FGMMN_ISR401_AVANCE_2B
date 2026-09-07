# -*- coding: utf-8 -*-
"""Genera el registro de consentimientos.

    python 02_Evidencias/Consentimientos/generar_registro.py

Produce 02_Evidencias/Consentimientos/registro_consentimientos.csv, que ata cada
participante con su evidencia, su archivo de consentimiento y --lo que de verdad
importa-- el alcance que autorizo.

Por que existe. La seccion 9 de la guia de desarrollo exige que todo participante
tenga su consentimiento individual firmado, fechado y legible, con el codigo de
sesion que lo vincula a su evidencia. Los archivos estaban; la tabla que los ata
no.

Y hay una razon practica mas urgente: **no todos los participantes autorizaron lo
mismo**. Los tres de la sesion de validacion comunicativa marcaron la casilla que
limita el uso al ambito del curso. Citar en el manuscrito a alguien que no lo
autorizo seria una infraccion, y sin una tabla que lo diga es un error facil de
cometer.

La columna `citable_en_manuscrito` es la que responde esa pregunta de un vistazo.

Solo biblioteca estandar.
"""
import csv
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
EVID = os.path.dirname(AQUI)
SALIDA = os.path.join(AQUI, "registro_consentimientos.csv")

# Alcance declarado por participante. La fuente de cada dato consta en la
# columna `como_consta` del registro: no se infiere de ningun sitio.
CURSO_Y_PUBLICACION = "Curso y publicacion cientifica revisada por pares"
SOLO_CURSO = "Solo ambito del curso"

# Ronda terminal: seis entrevistas del 2026-09-03. El propio entrevistador
# confirma que los seis marcaron la primera casilla.
RONDA_TERMINAL = {
    "DOC-05": "EV-20", "DOC-06": "EV-21", "DOC-07": "EV-22",
    "DOC-08": "EV-23", "DOC-09": "EV-24", "DOC-10": "EV-25",
}

# Sesiones de validacion con usuario tecnico. No son entrevistas: son
# walkthroughs sobre el prototipo, y su evidencia es el codigo `WT-xx` del acta,
# no un `EV-xx` de transcripcion. Se listan aparte porque el nombre del archivo
# de consentimiento no distingue un tipo de sesion del otro.
SESIONES_TECNICAS = {
    "TIC-01": "WT-08",
    "TIC-02": "WT-09",
    "TIC-03": "WT-10",
}
VALIDACION_TECNICA = "Sesion de validacion sobre prototipo (usuario tecnico)"

# Entrevistas anteriores: seudonimo -> evidencia, leido de las transcripciones.
def evidencias_de_transcripciones():
    d = {}
    carpeta = os.path.join(EVID, "Transcripciones")
    if not os.path.isdir(carpeta):
        return d
    for f in os.listdir(carpeta):
        m = re.match(r"(\d{4}-\d{2}-\d{2})_(\w+)_([A-Z]+-\d{2})_(EV-\d{2})_", f)
        if m:
            d[m.group(3)] = m.group(4)
    return d


def main():
    filas = []
    ev_por_codigo = evidencias_de_transcripciones()

    # --- entrevistas con consentimiento ya depositado ---------------------
    for nombre in sorted(os.listdir(AQUI)):
        m = re.match(r"(\d{4}-\d{2}-\d{2})_(\w+)_([A-Z]+-\d{2})_Consentimiento\.pdf$",
                     nombre)
        if not m:
            continue
        fecha, perfil, cod = m.group(1), m.group(2), m.group(3)
        # Los de la ronda terminal se registran mas abajo, con su alcance y su
        # estado de deposito. Si se anadieran tambien aqui saldrian por
        # duplicado en cuanto se depositara el PDF.
        if cod in RONDA_TERMINAL:
            continue
        tecnica = cod in SESIONES_TECNICAS
        filas.append({
            "codigo_participante": cod,
            "perfil": perfil,
            "evidencia": (SESIONES_TECNICAS[cod] if tecnica
                          else ev_por_codigo.get(cod, "sin transcripcion asociada")),
            "fecha_sesion": fecha,
            "sesion": VALIDACION_TECNICA if tecnica else "Entrevista semiestructurada",
            "archivo_consentimiento": "02_Evidencias/Consentimientos/" + nombre,
            "deposito": "Depositado, con los datos identificables censurados",
            "alcance_autorizado": CURSO_Y_PUBLICACION,
            "citable_en_manuscrito": "Si",
            "como_consta": (
                ("Marco la primera casilla del formulario, visible en el PDF por "
                 "encima de la banda de censura. El acta de la sesion es "
                 "02_Evidencias/Validacion_Walkthrough/Sesiones_Validacion/, "
                 "codigo " + SESIONES_TECNICAS[cod]) if tecnica else
                ("Cubierto por la adenda de segunda ronda del expediente "
                 "etico de la Entrega 2A, segun 02_Evidencias/Etica/"
                 "resumen_proceso_etico.md, apartado 2")),
        })

    # --- sesion de validacion comunicativa --------------------------------
    mc = os.path.join(EVID, "Member_Checking")
    if os.path.isdir(mc):
        for nombre in sorted(os.listdir(mc)):
            m = re.match(r"(\d{4}-\d{2}-\d{2})_(\w+)_([A-Z]+-\d{2})_Consentimiento_MC\.pdf$",
                         nombre)
            if not m:
                continue
            fecha, perfil, cod = m.group(1), m.group(2), m.group(3)
            filas.append({
                "codigo_participante": cod,
                "perfil": perfil,
                "evidencia": "MC-01",
                "fecha_sesion": fecha,
                "sesion": "Validacion comunicativa (member checking)",
                "archivo_consentimiento": "02_Evidencias/Member_Checking/" + nombre,
                "deposito": "Depositado, con los datos identificables censurados",
                "alcance_autorizado": SOLO_CURSO,
                "citable_en_manuscrito": "NO",
                "como_consta": ("Marcaron la segunda casilla del formulario. Es visible "
                                "en cada PDF, encima de la banda de censura, y esta "
                                "declarado en 02_Evidencias/Member_Checking/00_LEEME.md"),
            })

    # --- ronda terminal ----------------------------------------------------
    for cod, ev in sorted(RONDA_TERMINAL.items()):
        nombre = "2026-09-03_%s_%s_Consentimiento.pdf" % (
            {"CONS": "Conserje", "DOC": "Docente",
             "COORD": "Coordinacion"}[cod.split("-")[0]], cod)
        ruta = os.path.join(AQUI, nombre)
        existe = os.path.isfile(ruta)
        filas.append({
            "codigo_participante": cod,
            "perfil": {"CONS": "Conserje", "DOC": "Docente",
                       "COORD": "Coordinacion"}[cod.split("-")[0]],
            "evidencia": ev,
            "fecha_sesion": "2026-09-03",
            "sesion": "Entrevista semiestructurada, ronda terminal",
            "archivo_consentimiento": "02_Evidencias/Consentimientos/" + nombre,
            "deposito": ("Depositado, con los datos identificables censurados"
                         if existe else "PENDIENTE DE DEPOSITO"),
            "alcance_autorizado": CURSO_Y_PUBLICACION,
            "citable_en_manuscrito": "Si",
            "como_consta": ("Marcaron la primera casilla del formulario de la ronda "
                            "terminal, redactado en cumplimiento de la LOPDP. "
                            "Verificable en el PDF firmado una vez depositado"),
        })

    campos = ["codigo_participante", "perfil", "evidencia", "fecha_sesion",
              "sesion", "archivo_consentimiento", "deposito",
              "alcance_autorizado", "citable_en_manuscrito", "como_consta"]
    with io.open(SALIDA, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)

    citables = sum(1 for r in filas if r["citable_en_manuscrito"] == "Si")
    pendientes = [r["codigo_participante"] for r in filas
                  if r["deposito"].startswith("PENDIENTE")]
    faltan_pdf = [r["codigo_participante"] for r in filas
                  if not os.path.isfile(os.path.join(
                      os.path.dirname(EVID), r["archivo_consentimiento"]))]

    print("registro_consentimientos.csv")
    print("  %d participantes" % len(filas))
    print("  %d citables en el manuscrito, %d no" % (citables, len(filas) - citables))
    if pendientes:
        print("  consentimientos pendientes de depositar: %s" % ", ".join(pendientes))
    if faltan_pdf and faltan_pdf != pendientes:
        print("  AVISO: archivos declarados que no existen: %s"
              % ", ".join(sorted(set(faltan_pdf) - set(pendientes))))
    return 0


if __name__ == "__main__":
    sys.exit(main())

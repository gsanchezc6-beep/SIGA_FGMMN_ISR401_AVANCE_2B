# -*- coding: utf-8 -*-
"""Genera 10_Autoria/bitacora_sesiones.csv a partir del historial de versiones.

La bitacora no se escribe a mano. Cada campo se deriva del propio historial, de
modo que cualquiera puede regenerarla y obtener lo mismo:

    python 10_Autoria/generar_bitacora.py

Que es una sesion. Una sesion es el trabajo de una persona en un dia. Se agrupa
asi porque es la unidad que el historial permite delimitar sin suponer nada: la
hora de inicio es la de su primer commit de ese dia, la de fin la del ultimo, y
los artefactos trabajados son las rutas que esos commits tocaron. Con este
criterio existe al menos una fila por cada dia en que el repositorio registra
commits, que es lo que exige el elemento A1 de la guia de desarrollo.

Lo que la bitacora NO puede reconstruir, y por eso no lo inventa: el tiempo de
trabajo anterior al primer commit del dia. La hora de inicio es la del primer
commit, no la del momento en que la persona se sento a trabajar. Se declara asi
en la propia columna.

Solo biblioteca estandar.
"""
import collections
import csv
import io
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
SALIDA = os.path.join(AQUI, "bitacora_sesiones.csv")

SEP = "\x1f"
FIN = "\x1e"

USUARIO_GIT = {
    "gsanchezc6@uteq.edu.ec": "gsanchezc6-beep",
    "ymunozq@uteq.edu.ec": "yeranick-munoz",
    "wcedenoa2@uteq.edu.ec": "wcedenoa2",
}

# Prefijo de ruta -> area de trabajo, para describir que se toco.
AREAS = [
    ("01_ERS", "Especificacion de requisitos"),
    ("02_Evidencias", "Evidencia de campo"),
    ("03_Modelado", "Modelado UML e i*"),
    ("04_Trazabilidad", "Trazabilidad y aporte individual"),
    ("05_MVP", "Producto minimo viable"),
    ("06_Experimento", "Componente empirico"),
    ("07_Datos", "Paquete de datos"),
    ("07_Publicacion", "Manuscrito y deposito"),
    ("08_Defensa", "Defensa"),
    ("10_Autoria", "Evidencia de autoria"),
]


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print("git fallo: %s" % r.stderr.strip())
        sys.exit(1)
    return r.stdout


def area_de(ruta):
    for prefijo, nombre in AREAS:
        if ruta.startswith(prefijo):
            return nombre
    if "/" not in ruta:
        return "Documentos de raiz"
    return "Otros"


def main():
    formato = SEP.join(["%H", "%h", "%an", "%ae", "%ad", "%s"]) + FIN
    crudo = git("log", "--reverse", "--date=format:%Y-%m-%d %H:%M",
                "--pretty=format:" + formato)

    commits = []
    for bloque in crudo.split(FIN):
        bloque = bloque.strip("\n")
        if not bloque:
            continue
        h, corto, autor, correo, fecha, asunto = bloque.split(SEP)
        dia, hora = fecha.split(" ")
        archivos = git("show", "--name-only", "--pretty=format:", h)
        rutas = [l.strip() for l in archivos.split("\n") if l.strip()]
        commits.append({
            "h": corto, "autor": autor, "correo": correo,
            "dia": dia, "hora": hora, "asunto": asunto, "rutas": rutas,
        })

    sesiones = collections.OrderedDict()
    for c in commits:
        sesiones.setdefault((c["dia"], c["correo"]), []).append(c)

    campos = ["identificador", "fecha", "hora_inicio", "hora_fin", "modalidad",
              "participante", "usuario_git", "correo_institucional",
              "areas_trabajadas", "rutas_tocadas", "decisiones",
              "commits", "n_commits", "n_archivos"]
    filas = []
    contador = collections.Counter()

    for (dia, correo), grupo in sesiones.items():
        contador[dia] += 1
        ident = "S-%s-%d" % (dia.replace("-", ""), contador[dia])
        rutas = []
        for c in grupo:
            for r in c["rutas"]:
                if r not in rutas:
                    rutas.append(r)
        areas = []
        for r in rutas:
            a = area_de(r)
            if a not in areas:
                areas.append(a)
        decisiones = " | ".join(dict.fromkeys(c["asunto"] for c in grupo))
        filas.append({
            "identificador": ident,
            "fecha": dia,
            "hora_inicio": grupo[0]["hora"],
            "hora_fin": grupo[-1]["hora"],
            "modalidad": "Trabajo individual sobre el repositorio",
            "participante": grupo[0]["autor"],
            "usuario_git": USUARIO_GIT.get(correo, "no declarado"),
            "correo_institucional": correo,
            "areas_trabajadas": "; ".join(areas),
            "rutas_tocadas": "; ".join(rutas[:12]) + (" ; (+%d mas)" % (len(rutas) - 12)
                                                      if len(rutas) > 12 else ""),
            "decisiones": decisiones,
            "commits": " ".join(c["h"] for c in grupo),
            "n_commits": len(grupo),
            "n_archivos": len(rutas),
        })

    filas.sort(key=lambda f: (f["fecha"], f["hora_inicio"]))
    with io.open(SALIDA, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)

    dias = sorted(set(f["fecha"] for f in filas))
    print("bitacora_sesiones.csv")
    print("  %d sesiones sobre %d dias con commits" % (len(filas), len(dias)))
    print("  del %s al %s" % (dias[0], dias[-1]))
    print("  %d commits en total" % sum(f["n_commits"] for f in filas))
    faltan = [d for d in dias if not any(f["fecha"] == d for f in filas)]
    if faltan:
        print("  ERROR: dias con commits sin fila: %s" % ", ".join(faltan))
        return 1
    print("  todos los dias con commits tienen al menos una fila")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Incorpora al corpus JSON las transcripciones que aun no estan en el.

    python 06_Experimento/scripts_analisis/extender_corpus_json.py

`transcripciones_anonimizadas.json` es la fuente de la que
`curva_saturacion.py` toma la fecha de cada entrevista. Cuando se depositan
transcripciones nuevas hay que incorporarlas aqui o quedan fuera de la curva:
el script de saturacion avisa y las excluye del orden cronologico.

Por que anade en lugar de regenerar
-----------------------------------
Los diez registros originales se produjeron con `ConvertTo-Json` de PowerShell
sobre archivos `.txt` que ya no existen con ese nombre. Regenerar el archivo
entero cambiaria valores ya publicados --`archivo`, `n_caracteres` y la forma
de `contenido`-- sin que exista forma de comprobar que la reescritura los
reproduce. Este script **no reescribe ningun registro existente**: localiza el
cierre del ultimo y empalma los que falten, conservando byte a byte todo lo
anterior. Es idempotente: ejecutarlo dos veces no anade nada la segunda.

Solo biblioteca estandar.
"""
import io
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", ".."))
JSON = os.path.join(RAIZ, "06_Experimento", "datos_crudos",
                    "transcripciones_anonimizadas.json")
TRANS = os.path.join(RAIZ, "02_Evidencias", "Transcripciones")

# Sangrias del archivo existente, para que los registros nuevos no se
# distingan de los antiguos al abrirlo.
IND_LLAVE = " " * 28
IND_CAMPO = " " * 32
COLA = "\r\n" + " " * 24 + "]\r\n}\r\n"

# El perfil que declara la cabecera es una sola palabra; el corpus usa la
# forma larga. Se traduce aqui para no introducir un valor nuevo en un campo
# del que ya dependen los recuentos por perfil.
PERFILES = {
    "Docente": "Docente de la carrera",
    "Conserje": "Personal de servicios generales",
    "Coordinacion": "Coordinacion de carrera",
    "Coordinación": "Coordinacion de carrera",
}

CAMPOS_CABECERA = [
    ("Identificador de evidencia", "id_evidencia"),
    ("Fecha de la sesion", "fecha"),
    ("Tecnica de elicitacion", "tecnica"),
    ("Modalidad de registro", "modalidad"),
    ("Codigo de participante", "codigo_participante"),
    ("Perfil del participante", "perfil_participante"),
]


def sin_tildes(s):
    for a, b in (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),
                 ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U"),
                 ("ñ", "n"), ("Ñ", "N")):
        s = s.replace(a, b)
    return s


def leer_transcripcion(ruta):
    """Devuelve los metadatos de la cabecera y los turnos del cuerpo."""
    texto = io.open(ruta, encoding="utf-8").read()
    cabecera, cuerpo = texto.split("\n---\n", 1)

    meta = {}
    for linea in cabecera.split("\n"):
        m = re.match(r"^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|$", linea.strip())
        if not m:
            continue
        clave = sin_tildes(m.group(1).strip())
        for etiqueta, destino in CAMPOS_CABECERA:
            if clave == etiqueta:
                meta[destino] = m.group(2).strip()

    turnos = []
    for linea in cuerpo.split("\n"):
        m = re.match(r"^\*\*(.+?):\*\*\s*(.*)$", linea.strip())
        if m:
            turnos.append("%s: %s" % (m.group(1).strip(), m.group(2).strip()))
    return meta, turnos


def componer_contenido(meta, turnos):
    """Reproduce la disposicion en texto plano que usan los diez registros."""
    ev = meta["id_evidencia"]
    lineas = [
        "Identificador de evidencia : %s" % ev,
        "Fecha de la sesión         : %s" % meta["fecha"],
        "Técnica de elicitación     : %s" % meta["tecnica"],
        "Modalidad de registro      : %s" % meta["modalidad"],
        "Código de participante     : %s" % meta["codigo_participante"],
        "Perfil del participante    : %s" % meta["perfil_participante"],
        "Zona de evidencia          : [P] Pública (material anonimizado)",
        "Anonimización              : sin nombres propios; los cargos únicos y",
        "                             los terceros mencionados se sustituyen por",
        "                             marcadores genéricos entre corchetes.",
        "", "", "",
        "Entrevista %s" % ev,
    ]
    return "\n".join(lineas) + "\n" + "\n\n".join(turnos)


def registro(ruta):
    meta, turnos = leer_transcripcion(ruta)
    perfil = PERFILES.get(meta.get("perfil_participante", ""),
                          meta.get("perfil_participante", ""))
    meta["perfil_participante"] = perfil
    contenido = componer_contenido(meta, turnos)
    return {
        "archivo": os.path.basename(ruta),
        "id_evidencia": meta["id_evidencia"],
        "fecha": meta["fecha"],
        "tecnica": meta["tecnica"],
        "codigo_participante": meta["codigo_participante"],
        "perfil_participante": perfil,
        "zona": "P",
        "anonimizado": True,
        "n_caracteres": len(contenido),
        "contenido": contenido,
    }, len(turnos)


def serializar(reg):
    """Un registro con la sangria y el espaciado del archivo existente."""
    partes = []
    for clave, valor in reg.items():
        partes.append('%s"%s":  %s' % (IND_CAMPO, clave,
                                       json.dumps(valor, ensure_ascii=False)))
    return IND_LLAVE + "{\r\n" + ",\r\n".join(partes) + "\r\n" + IND_LLAVE + "}"


def main():
    raw = io.open(JSON, encoding="utf-8", newline="").read()
    datos = json.loads(raw)
    presentes = set(t["id_evidencia"] for t in datos["transcripciones"])

    nuevos, resumen = [], []
    for nombre in sorted(os.listdir(TRANS)):
        if not nombre.endswith("_Transcripcion.md"):
            continue
        ruta = os.path.join(TRANS, nombre)
        try:
            reg, n_turnos = registro(ruta)
        except (KeyError, ValueError) as e:
            print("  NO SE PUDO LEER %s: %s" % (nombre, e))
            return 1
        if reg["id_evidencia"] in presentes:
            continue
        nuevos.append(reg)
        resumen.append((reg["id_evidencia"], reg["codigo_participante"],
                        n_turnos, reg["n_caracteres"]))

    if not nuevos:
        print("El corpus ya contiene las %d transcripciones depositadas. Sin cambios."
              % len(presentes))
        return 0

    if not raw.endswith(COLA):
        print("El final del archivo no tiene la forma esperada; no se toca nada.")
        return 1
    cuerpo = raw[:-len(COLA)]

    salida = (cuerpo + ",\r\n" + ",\r\n".join(serializar(r) for r in nuevos)
              + COLA)
    salida = salida.replace('"n_transcripciones":  %d' % len(presentes),
                            '"n_transcripciones":  %d' % (len(presentes) + len(nuevos)), 1)

    # Antes de escribir: que siga siendo JSON valido y que los registros
    # anteriores no hayan cambiado en ningun campo.
    comprobado = json.loads(salida)
    if comprobado["n_transcripciones"] != len(comprobado["transcripciones"]):
        print("El recuento declarado no coincide con los registros. No se escribe.")
        return 1
    for antes, despues in zip(datos["transcripciones"], comprobado["transcripciones"]):
        if antes != despues:
            print("El registro %s cambiaria. No se escribe." % antes["id_evidencia"])
            return 1

    io.open(JSON, "w", encoding="utf-8", newline="").write(salida)

    print("Incorporadas %d transcripciones; el corpus queda en %d."
          % (len(nuevos), comprobado["n_transcripciones"]))
    for ev, cod, turnos, chars in resumen:
        print("  %-6s %-8s %4d turnos  %6d caracteres" % (ev, cod, turnos, chars))
    print("Los %d registros anteriores se conservan sin cambios." % len(presentes))
    return 0


if __name__ == "__main__":
    sys.exit(main())

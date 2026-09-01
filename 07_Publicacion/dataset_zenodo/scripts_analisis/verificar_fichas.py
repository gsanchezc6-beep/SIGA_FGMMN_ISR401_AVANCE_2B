# -*- coding: utf-8 -*-
"""
Contrasta el contenido del contenedor restringido descifrado contra
02_Evidencias/00_Restringido/fichas_tecnicas.csv: por cada archivo
declarado, verifica que exista, que su hash SHA-256 coincida con el
registrado (calculado antes del cifrado) y, si es audio o video, que
ffprobe le mida una duración mayor que cero.

Un archivo ausente, con hash distinto o con duración cero se trata como
evidencia ausente o sustituida (gatekeeper G4) y hace fallar el script
con código de salida distinto de cero.

Uso:
    python verificar_fichas.py --fichas ../../02_Evidencias/00_Restringido/fichas_tecnicas.csv \
        --directorio /ruta/al/contenedor/descifrado
"""
import argparse
import hashlib
import os
import subprocess
import sys

import pandas as pd

TIPOS_MULTIMEDIA = {"video", "audio"}


def sha256_de(ruta, tam_bloque=1024 * 1024):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(tam_bloque), b""):
            h.update(bloque)
    return h.hexdigest()


def buscar_archivo(directorio, nombre_archivo):
    for raiz, _dirs, archivos in os.walk(directorio):
        if nombre_archivo in archivos:
            return os.path.join(raiz, nombre_archivo)
    return None


def duracion_ffprobe(ruta):
    try:
        salida = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", ruta],
            capture_output=True, text=True, timeout=60,
        )
    except FileNotFoundError:
        return None, "ffprobe no está instalado o no está en el PATH"
    if salida.returncode != 0 or not salida.stdout.strip():
        return None, (salida.stderr.strip() or "ffprobe no devolvió duración")
    try:
        return float(salida.stdout.strip()), None
    except ValueError:
        return None, f"salida de ffprobe no numérica: {salida.stdout!r}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fichas", required=True, help="fichas_tecnicas.csv")
    ap.add_argument("--directorio", required=True, help="Carpeta del contenedor ya descifrado")
    args = ap.parse_args()

    if not os.path.isdir(args.directorio):
        print(f"ERROR: {args.directorio} no es una carpeta accesible.")
        sys.exit(2)

    df = pd.read_csv(args.fichas, encoding="utf-8-sig")
    fallos = []

    for _, fila in df.iterrows():
        nombre = str(fila["nombre_archivo"]).strip()
        tipo = str(fila.get("tipo", "")).strip().lower()
        hash_esperado = str(fila.get("sha256", "")).strip().lower()

        ruta = buscar_archivo(args.directorio, nombre)
        if ruta is None:
            fallos.append((nombre, "AUSENTE del contenedor descifrado"))
            print(f"[FALLO] {nombre}: ausente del contenedor descifrado")
            continue

        hash_real = sha256_de(ruta)
        if hash_esperado and hash_real != hash_esperado:
            fallos.append((nombre, f"hash no coincide (esperado {hash_esperado[:12]}…, real {hash_real[:12]}…)"))
            print(f"[FALLO] {nombre}: hash SHA-256 no coincide")
            continue

        if tipo in TIPOS_MULTIMEDIA:
            duracion, error = duracion_ffprobe(ruta)
            if duracion is None:
                fallos.append((nombre, f"ffprobe: {error}"))
                print(f"[FALLO] {nombre}: {error}")
                continue
            if duracion <= 0:
                fallos.append((nombre, "duración cero"))
                print(f"[FALLO] {nombre}: duración cero")
                continue
            print(f"[OK]    {nombre}: hash coincide, duración {duracion:.1f}s")
        else:
            print(f"[OK]    {nombre}: hash coincide")

    print(f"\nTotal verificado: {len(df)} — OK: {len(df) - len(fallos)} — FALLOS: {len(fallos)}")
    if fallos:
        print("\nArchivos con problema (gatekeeper G4 — evidencia ausente o sustituida):")
        for nombre, motivo in fallos:
            print(f"  - {nombre}: {motivo}")
        sys.exit(1)


if __name__ == "__main__":
    main()

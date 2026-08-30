# Entrevistas en video

Los archivos de esta carpeta son **video real, reproducible y verificable**. No son
referencias ni punteros.

## Formato

Todos cumplen los minimos que fija la seccion 5.1 de la guia:

| Requisito | Minimo | Real |
|---|---|---|
| Contenedor y codec de video | MP4 H.264 | MP4 H.264 |
| Resolucion | ≥ 720p | 1280 × 720 |
| Audio incorporado | Si | Si, AAC |
| Tasa de bits de audio | ≥ 96 kbps | 128 kbps |

Se comprueba con:

```bash
ffprobe -v error -show_entries stream=codec_name,width,height,bit_rate \
        -show_entries format=duration,bit_rate -of json ARCHIVO.mp4
```

## Sobre la recodificacion

Los originales de camara sumaban 4,69 GB, con tasas de video de hasta 8967 kbps para
grabaciones de camara fija. Siete de los nueve superaban el limite de 100 MB por archivo
que GitHub rechaza.

Los archivos de esta carpeta se **recodificaron con FFmpeg** manteniendo la resolucion
original de 1280 × 720 y elevando la compresion del video, de modo que caben en el
repositorio como objetos normales de Git, **sin necesidad de Git LFS**.

Lo que se conservo intacto: la resolucion, la duracion completa de cada sesion, el
contenido integro y una tasa de audio muy por encima del minimo. Lo que se redujo: la tasa
de bits del video, que en grabaciones de camara fija con una persona hablando no aporta
informacion util al analisis.

Los originales de camara se conservan fuera del repositorio, y su hash SHA-256 consta en
[`../00_Restringido/fichas_tecnicas.csv`](../00_Restringido/fichas_tecnicas.csv) en la
columna `sha256_original`, junto al hash del archivo recodificado que si esta aqui.

## Sobre los datos personales

Estos videos muestran a los participantes. Su publicacion se sostiene en el consentimiento
informado firmado por cada uno, que consta enmascarado en
[`../Consentimientos/`](../Consentimientos/), y en el codigo de participante que sustituye
al nombre propio en el nombre del archivo y en toda la evidencia.

La version anonimizada de cada entrevista es su transcripcion, en
[`../Transcripciones/`](../Transcripciones/).

## Inventario

La sesion del **2026-07-28 (COORD-03, EV-14)** se registro **solo en audio**, por peticion
expresa del participante: no existe video de esa entrevista y su ausencia no es una
omision.

La entrevista **EV-15 (2026-07-29, DOC-03)** fue realizada pero se excluyo integramente
porque el participante no firmo el consentimiento. Ningun fragmento suyo se conserva.

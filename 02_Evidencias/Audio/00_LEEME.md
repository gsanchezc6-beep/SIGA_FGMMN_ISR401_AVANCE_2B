# Entrevistas en audio

Los archivos de esta carpeta son **audio real y reproducible**.

## Formato

| Requisito de la guia | Minimo | Real |
|---|---|---|
| Formato | MP3 o WAV | MP3 |
| Tasa de bits | >= 96 kbps | 128 kbps |
| Uno por entrevista | 10 | 10 |

Los siete registros originales en WAV sin comprimir sumaban 202 MB. Se convirtieron a MP3
a 128 kbps, muy por encima del minimo, conservando la duracion integra de cada sesion. Los
tres que ya estaban en MP3 se conservan tal cual.

El hash del archivo publicado y el del original de camara constan uno junto al otro en
[`../00_Restringido/fichas_tecnicas.csv`](../00_Restringido/fichas_tecnicas.csv).

## Redundancia con el video

Los audios se grabaron en paralelo al video con un dispositivo independiente, como
respaldo ante fallo. Por eso su duracion coincide con la del video de la misma sesion.

La excepcion es **2026-07-28 (COORD-03, EV-14)**, que se registro **solo en audio** por
peticion expresa del participante: ahi el audio no es respaldo sino el registro primario, y
es la unica sesion sin video.

## Version anonimizada

La version publicable sin voz identificable de cada entrevista es su transcripcion, en
[`../Transcripciones/`](../Transcripciones/).

La entrevista **EV-15 (2026-07-29, DOC-03)** se excluyo integramente por falta de
consentimiento firmado. Su audio no se conserva en ninguna parte.

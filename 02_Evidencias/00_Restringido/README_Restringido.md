# Ficha tecnica de la evidencia y zona restringida [R]

Esta carpeta contiene la **ficha tecnica en claro** de toda la evidencia audiovisual, y
documenta que se publica y que se conserva fuera del repositorio.

---

## 1. Toda la evidencia audiovisual esta en el repositorio

A diferencia de la Entrega 2A, **el material audiovisual no se sustituye por referencias**.
Los nueve registros de entrevista residen aqui como archivos reales, reproducibles y
verificables:

| | Cantidad | Ubicacion | Volumen |
|---|---|---|---|
| Entrevistas en video | 8 | [`../Video/`](../Video/) | 458 MB |
| Entrevistas en audio | 10 | [`../Audio/`](../Audio/) | 158 MB |

Todos superan el sondeo de codec y duracion que exige la guia: MP4 H.264 a 1280 × 720 con
audio AAC, y MP3 a 128 kbps.

Para que cupieran en GitHub sin recurrir a Git LFS, los videos se **recodificaron**
conservando la resolucion original y elevando la compresion. El procedimiento y lo que se
conserva estan explicados en [`../Video/00_LEEME.md`](../Video/00_LEEME.md).

---

## 2. Que si queda fuera del repositorio

Solo lo que contiene datos personales que el consentimiento no autoriza a publicar:

| Material | Por que no se publica |
|---|---|
| Originales de camara sin recodificar | Redundantes con los publicados; su hash consta en la ficha |
| Consentimientos originales con cedula y firma visibles | Datos identificables. En el repositorio estan las copias **enmascaradas** |
| Actas de sesion de validacion con firma visible | Idem: en el repositorio estan enmascaradas |
| Registro de custodia codigo–participante | Es la unica pieza que permite reidentificar. Se entrega solo al docente |

Ese material se conserva en un contenedor cifrado con **AES-256** y nombres de archivo
ocultos, alojado en el OneDrive institucional de la UTEQ:

<https://uteqeduec-my.sharepoint.com/:f:/g/personal/gsanchezc6_msuteq_edu_ec/IgAIbQP1scbLQoCrcCWgqMbNAQrzV6V3SQg8yhuu2D1TZEc?e=3JJvgX>

La contrasena se entrega al docente responsable por el Sistema de Gestion Academica. No se
transmite por ningun otro medio y no consta en este repositorio.

---

## 3. La ficha tecnica

[`fichas_tecnicas.csv`](fichas_tecnicas.csv) registra, por cada archivo:

| Columna | Contenido |
|---|---|
| `nombre_archivo` | Nomenclatura `AAAA-MM-DD_TipoParticipante_Codigo_Tecnica.ext` |
| `tipo`, `fecha`, `codigo_participante`, `id_evidencia` | Identificacion y trazado |
| `duracion`, `resolucion`, `codec`, `audio_kbps` | Sondeados con `ffprobe` sobre el archivo real |
| `tamano_bytes` | Del archivo publicado |
| `sha256_publicado` | Hash del archivo que esta en el repositorio |
| `sha256_original_camara` | Hash del original de camara, calculado **antes** de recodificar |

Las dos columnas de hash permiten dos verificaciones distintas: que el archivo del
repositorio no fue alterado, y que el original conservado fuera es el que se declaro.

### Comprobar

```bash
# el archivo publicado, desde la raiz del repositorio
sha256sum -c checksums.sha256

# el codec y la duracion reales de cualquier registro
ffprobe -v error -show_entries stream=codec_name,width,height,bit_rate \
        -show_entries format=duration -of json 02_Evidencias/Video/ARCHIVO.mp4
```

En Windows, para un archivo suelto: `certutil -hashfile ARCHIVO SHA256`.

---

## 4. Inventario y sus dos ausencias declaradas

Diez entrevistas validas. Dos ausencias, ninguna de ellas una omision:

1. **No hay video del 2026-07-28 (COORD-03, EV-14).** Esa sesion se registro solo en
   audio, por peticion expresa del participante. De ahi que haya 8 videos y 10 audios.
2. **La entrevista EV-15 (2026-07-29, DOC-03) no existe en ninguna parte.** Fue realizada,
   pero el participante no firmo el consentimiento informado, ni para la entrevista ni
   para la sesion de validacion asociada. Se elimino integramente: no consta en el
   repositorio, ni en el contenedor, ni en la codificacion tematica, ni en el material
   fuente del componente empirico.

Ademas, **el video del 2026-07-30 (DOC-04, EV-16) no esta en el repositorio**: existe y su
hash consta en el historial del proyecto, pero el archivo no se pudo recuperar de los
medios disponibles. Su audio si esta publicado.

---

## 5. Codigos de participante

Los codigos `DOC-nn`, `COORD-nn` y `CONS-nn` sustituyen a los nombres propios en todo el
material publicado, incluidos los nombres de archivo y esta ficha, de modo que ninguno de
los dos constituye un dato identificable.

El procedimiento completo de disociacion esta en
[`../../07_Publicacion/dataset_zenodo/anonimizacion.md`](../../07_Publicacion/dataset_zenodo/anonimizacion.md).

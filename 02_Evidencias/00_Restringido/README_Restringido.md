# Ficha tecnica de la evidencia y zona restringida [R]

Esta carpeta contiene la **ficha tecnica en claro** de toda la evidencia audiovisual, y
documenta que se publica y que se conserva fuera del repositorio.

---

## 1. Dos regimenes de publicacion, segun el consentimiento firmado

El corpus son **dieciseis entrevistas**, y no todas se publican igual. La diferencia no es
de criterio nuestro: es lo que dice el formulario que cada participante firmo.

Las **diez primeras** (mayo a julio de 2026) se consintieron con un formulario que autoriza
publicar el registro anonimizado. Su material reside aqui como archivos reales,
reproducibles y verificables:

| | Cantidad | Ubicacion | Volumen |
|---|---|---|---|
| Entrevistas en video | 8 | [`../Video/`](../Video/) | 458 MB |
| Entrevistas en audio | 10 | [`../Audio/`](../Audio/) | 158 MB |

Las **seis de la ronda terminal** (2026-09-03, `EV-20` a `EV-25`) se consintieron con el
formulario de esa ronda, que dice literalmente que *las grabaciones originales no se
publican*. De ellas, a la zona publica va unicamente la transcripcion anonimizada y el
consentimiento enmascarado; el video y el audio quedan en la zona restringida. Estan
declaradas en la ficha tecnica con `zona = Restringida`, con su duracion, su codec y su
hash, para que se pueda comprobar que existen y cuales son sin publicarlas.

**Ninguna de las dieciseis entrevistas carece de registro sonoro.** Hay dieciseis audios y
catorce videos; las ausencias de video estan explicadas una a una en el apartado 4.

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
| **Video y audio de las seis entrevistas de la ronda terminal** (`EV-20` a `EV-25`) | El consentimiento de esa ronda dice que las grabaciones originales no se publican. No es una decision de conveniencia: publicarlas seria usarlas fuera de lo consentido |
| Clave de desciego del cuasi-experimento | Su ubicacion y custodia constan en [`../../06_Experimento/clave_desciego_UBICACION.md`](../../06_Experimento/clave_desciego_UBICACION.md) |

Ese material se conserva en **`SIGA_zona_restringida.7z`**, un contenedor cifrado con **AES-256** y nombres de archivo
ocultos, alojado en el OneDrive institucional de la UTEQ:

<https://uteqeduec-my.sharepoint.com/:u:/g/personal/gsanchezc6_msuteq_edu_ec/IQAHZ7FrestzSICGfFoaJfzWAX9gkf9XQpZj5JTi_zYuNhA?e=SJHr4N>

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

**En las filas con `zona = Restringida` la primera columna dice `N/A - no se publica`**,
porque no existe archivo publicado que verificar. La segunda si lleva hash: el del original
de camara, calculado antes de recodificar. Con el se comprueba, cuando se abra el
contenedor, que lo depositado es lo que aqui se declara.

El emparejamiento entre cada original de camara --cuyo nombre es una marca de tiempo-- y su
recodificado no se establecio por orden de archivo sino **comparando duraciones sondeadas
con `ffprobe`**, y se comprobo que ninguna pareja quedara a menos de tres segundos de otra,
que habria hecho ambiguo el emparejamiento.

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

## 4. Inventario y sus ausencias declaradas

Dieciseis entrevistas validas: diez de mayo a julio y seis del 2026-09-03. Las ausencias de
video son dos, y ninguna es una omision:

1. **No hay video del 2026-07-28 (COORD-03, EV-14).** Esa sesion se registro solo en
   audio, por peticion expresa del participante. De ahi que haya 8 videos y 10 audios.
2. **La entrevista EV-15 (2026-07-29, DOC-03) no existe en ninguna parte.** Fue realizada,
   pero el participante no firmo el consentimiento informado, ni para la entrevista ni
   para la sesion de validacion asociada. Se elimino integramente: no consta en el
   repositorio, ni en el contenedor, ni en la codificacion tematica, ni en el material
   fuente del componente empirico.

3. **El video del 2026-07-30 (DOC-04, EV-16) no esta en el repositorio.** Existe y su
   hash consta en el historial del proyecto, pero el archivo no se pudo recuperar de los
   medios disponibles. Su audio si esta publicado.

Las seis de la ronda terminal **no son una ausencia**: existen las doce piezas --seis videos
y seis audios--, estan declaradas en la ficha tecnica con su duracion y su hash, y residen
en la zona restringida por lo que dice su consentimiento. Sus duraciones se pueden
contrastar contra la cabecera de cada transcripcion, donde consta la misma cifra:

| Evidencia | Participante | Duracion | Video | Audio |
|---|---|---|---|---|
| `EV-20` | DOC-05 | 19:28 | Restringida | Restringida |
| `EV-21` | DOC-06 | 14:20 | Restringida | Restringida |
| `EV-22` | DOC-07 | 21:16 | Restringida | Restringida |
| `EV-23` | DOC-08 | 13:44 | Restringida | Restringida |
| `EV-24` | DOC-09 | 11:45 | Restringida | Restringida |
| `EV-25` | DOC-10 | 16:22 | Restringida | Restringida |

---

## 5. Codigos de participante

Los codigos `DOC-nn`, `COORD-nn` y `CONS-nn` sustituyen a los nombres propios en todo el
material publicado, incluidos los nombres de archivo y esta ficha, de modo que ninguno de
los dos constituye un dato identificable.

El procedimiento completo de disociacion esta en
[`../../07_Publicacion/dataset_zenodo/anonimizacion.md`](../../07_Publicacion/dataset_zenodo/anonimizacion.md).

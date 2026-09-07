# Registro de deposito

**Paquete de datos del proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ**

Identificadores persistentes bajo los que este material esta depositado, con sus fechas.

---

## 1. Identificadores

| Que | Identificador persistente | Fecha |
|---|---|---|
| **Paquete de datos, version vigente** `2B-1.11.0` | [`10.5281/zenodo.22557171`](https://doi.org/10.5281/zenodo.22557171) | 2026-09-06 |
| Registro previo del protocolo | [`10.17605/OSF.IO/7PQ3H`](https://doi.org/10.17605/OSF.IO/7PQ3H) | 2026-08-02, 20:25:07 UTC |
| Instantanea del codigo | `swh:1:snp:861295fead33417e3efc2753fd4a34897014a891` | 2026-08-31 |

### Versiones anteriores del paquete

| Version | DOI | Fecha | Que cambio despues |
|---|---|---|---|
| `2B-1.9.x` | [`10.5281/zenodo.22137679`](https://doi.org/10.5281/zenodo.22137679) | 2026-08-31 | Llevaba la codificacion tematica de diez entrevistas y no incluia el panel ampliado |

**El DOI de una version no se reutiliza.** Cada version publicada en Zenodo recibe el suyo y
sigue resolviendo para siempre, de modo que una cita antigua no se rompe: lleva al paquete
tal como estaba cuando se cito. Lo que este repositorio declara en `CITATION.cff` y en el
manuscrito es el DOI de la **version vigente**, porque es la que corresponde al contenido
actual del arbol.

> **Pendiente.** Zenodo emite ademas un DOI de concepto, que agrupa todas las versiones y
> siempre lleva a la ultima. Aparece en la pagina del registro como «Cite all versions». No
> consta aqui todavia; cuando se recoja, es el que conviene usar en textos de divulgacion,
> mientras que el de version se queda donde hace falta fijar el contenido exacto.

## 2. Por que importa la fecha del registro previo

El registro en OSF **es anterior a la primera sesion de puntuacion** y lleva sello temporal
externo. Eso es lo que permite sostener que la justificacion del tamano muestral y del
numero de evaluadores se fijo antes de ver los resultados, y no despues.

Las pruebas del sello temporal, obtenidas de la propia API de OSF y de una captura
independiente en Internet Archive, estan en
[`../06_Experimento/registro_previo/`](../06_Experimento/registro_previo/):
`osf_registration_api.json`, `osf_internet_archive.pdf` y `osf_internet_archive_bag.zip`.

## 3. Correspondencia entre lo depositado y este repositorio

El deposito de Zenodo es un paquete curado, no un volcado del repositorio. La
correspondencia pieza a pieza consta en
[`../07_Publicacion/dataset_zenodo/`](../07_Publicacion/dataset_zenodo/).

## 4. Version del repositorio a la que corresponde este paquete

La linea base vigente se declara en el `README.md` de la raiz y en el `CHANGELOG.md`. El
manifiesto `checksums_datos.sha256` de esta carpeta permite comprobar que el contenido del
paquete no ha cambiado desde entonces.

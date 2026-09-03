# Paquete de datos — Proyecto SIGA

**Equipo FGMMN · Ingenieria de Requisitos (ISR-401) · Universidad Tecnica Estatal de Quevedo**

Este es el paquete de datos del componente empirico: el cuasi-experimento de evaluacion
ciega en el que tres jueces independientes puntuaron 51 requisitos —unos redactados por el
equipo, otros generados por un modelo de lenguaje— en cinco dimensiones de calidad.

---

## 1. Como se reproduce, en una sola orden

Desde la raiz del repositorio recien clonado:

```
python 07_Datos/scripts/ejecutar.py
```

Eso reconstruye **todo** el contenido de `datos_procesados/` y de `resultados/` a partir
unicamente de `datos_crudos/`, y termina comprobando la integridad del paquete.

**No hace falta instalar nada.** Los scripts usan solo la biblioteca estandar de Python
3.8 o superior. No hay `pip install`, ni entorno virtual, ni fichero de dependencias que
pueda quedarse obsoleto. Se tomo esa decision precisamente para que la comprobacion de
reproducibilidad no dependa de que un tercero consiga instalar las versiones correctas de
nada.

Para ver las etapas sin ejecutarlas:

```
python 07_Datos/scripts/ejecutar.py --listar
```

---

## 2. Que contiene cada carpeta

| Ruta | Contenido |
|---|---|
| `datos_crudos/` | Los datos **tal como salieron del instrumento**, sin ninguna edicion manual |
| `datos_procesados/` | Derivados, generados solo por los scripts. Se pueden borrar y regenerar |
| `scripts/` | El orquestador y las tres etapas |
| `resultados/` | Tablas generadas por los scripts. Nunca escritas a mano |
| `diccionario_datos.csv` | Cada columna de cada CSV: tipo, unidad, rango, faltantes y procedencia |
| `desviaciones.md` | Toda diferencia respecto de lo previsto en el protocolo, con fecha y motivo |
| `registro_deposito.md` | Identificadores persistentes del deposito y sus fechas |
| `checksums_datos.sha256` | Manifiesto de sumas de todo el paquete |
| `LICENSE-DATA.txt` | Licencia de los datos, distinta de la del codigo |

### Los datos crudos

| Archivo | Que es |
|---|---|
| `juez1.csv`, `juez2.csv`, `juez3.csv` | Las hojas de puntuacion devueltas por cada juez. 51 items x 5 dimensiones |
| `asignacion_brazo_items.csv` | A que brazo del experimento pertenece cada item ciego: `Humano` o `LLM` |
| `corpus_rf_rnf_etiquetado.json` | El corpus fuente completo del que salieron ambos conjuntos de requisitos |
| `respuestas_cuestionario.csv` | Las 31 respuestas del cuestionario digital v2.0 (EV-17), anonimas |

### Las etapas

| Etapa | Que produce |
|---|---|
| `formato_largo` | `evaluacion_ciega_formato_largo.csv` — evaluador, requisito, orden de presentacion, brazo, criterio y puntuacion. 765 filas |
| `acuerdo_ic` | `acuerdo_interevaluador_ic.csv` — kappa de Cohen ponderado y de Fleiss, cada uno con su intervalo de confianza del 95 % |
| `integridad` | Comprueba la correspondencia con `06_Experimento`, la cobertura del diccionario, y regenera el manifiesto de sumas |

---

## 3. Sobre el orden de presentacion

La hoja en formato largo incluye la columna `orden_presentacion`, y conviene decir de donde
sale porque no es un dato que se haya medido despues.

El paquete de evaluacion ciega se armo **una sola vez, con los items en orden aleatorizado**,
y ese mismo orden se entrego a los tres jueces. Asi lo declara
`06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md` en sus instrucciones. Por
tanto el orden de presentacion de un item es su posicion en el paquete: `Item-01` se
presento en primer lugar, `Item-51` en ultimo.

**No hubo un orden distinto por juez.** Quien quiera comprobarlo tiene el instrumento
completo en esa ruta.

---

## 4. Sobre la tabla de desciego

`asignacion_brazo_items.csv` dice a que brazo pertenece cada item, que es lo que el analisis
necesita. **No** dice a que requisito real corresponde cada item ciego.

Esa correspondencia —la tabla de desciego propiamente dicha— no reside en el repositorio
publico. Donde esta y quien la custodia consta en
[`06_Experimento/clave_desciego_UBICACION.md`](../06_Experimento/clave_desciego_UBICACION.md),
y la desviacion que la motivo sigue anotada en
[`06_Experimento/registro_previo/desviacion_clave_desciego.md`](../06_Experimento/registro_previo/desviacion_clave_desciego.md).

---

## 5. Relacion con 06_Experimento

Las dos carpetas no se solapan por descuido, y conviene entender el reparto:

- **`06_Experimento/`** es el componente empirico: el protocolo, el registro previo en OSF,
  los instrumentos, las consignas dadas al modelo de lenguaje, los scripts de analisis
  estadistico y sus salidas. Es la cadena del estudio.
- **`07_Datos/`** es el paquete de datos: la unidad depositable, autocontenida y verificable
  por un tercero sin conocer el resto del repositorio.

Los datos crudos son **los mismos**, no una version parecida. La etapa `integridad` lo
comprueba comparando las sumas SHA-256 de las cinco copias, y falla si alguien edita una
sola de las dos. Esa comprobacion es la razon por la que la duplicacion es segura.

---

## 6. Que numeros salen de aqui

Ningun numero de los documentos del proyecto esta escrito a mano. Los que proceden de este
paquete son:

| Numero | Donde aparece | Se regenera con |
|---|---|---|
| Kappa de Cohen y de Fleiss por dimension | Reporte del estudio y manuscrito | `acuerdo_ic` |
| Intervalos de confianza del acuerdo | Reporte del estudio | `acuerdo_ic` |
| 765 valoraciones, 51 items, 3 jueces | Reporte, manuscrito y ERS | `formato_largo` |

Los tamanos del efecto, los contrastes de hipotesis y el calculo de potencia se generan en
`06_Experimento` con `replicar.py`, que es la cadena del estudio y se conserva intacta.

---

## 7. Politica de datos personales

En este paquete **no hay ningun dato personal**. Las hojas de los jueces se identifican como
`juez1`, `juez2` y `juez3`; el cuestionario se recogio de forma anonima y sin campos
identificables. El material que si contiene datos personales —consentimientos firmados,
originales de camara, registro de custodia codigo-participante— se conserva en el contenedor
cifrado AES-256 descrito en
[`02_Evidencias/00_Restringido/README_Restringido.md`](../02_Evidencias/00_Restringido/README_Restringido.md)
y no se publica.

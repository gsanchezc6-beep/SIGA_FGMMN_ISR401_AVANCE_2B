# Lista de verificacion previa

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Seccion 11 de la guia de desarrollo del 2026-09-02. Las doce comprobaciones se
**ejecutaron**, no se marcaron a mano: el detalle de cada una es la salida real de
`10_Autoria/verificacion_previa.py`.

| | |
|---|---|
| Comprobado sobre | un clon limpio del remoto |
| Version | `2fded58` |

---

## Resultado

| N.º | Comprobacion | Cumple | Detalle |
|---|---|---|---|
| 1 | Se clono en carpeta limpia y se compilo el documento principal desde el .tex siguiendo unicamente el README | **Si** | Compilado sobre el clon con pdfLaTeX + BibTeX, sin errores |
| 2 | El PDF resultante coincide con el entregado y no presenta referencias sin resolver | **Si** | 26 paginas regeneradas, 0 referencias sin resolver. La comparacion es por contenido y no por suma: pdfLaTeX incrusta la fecha de compilacion, de modo que dos PDF del mismo fuente nunca son byte a byte iguales |
| 3 | No existe ningun archivo de cero o un byte cuyo nombre anuncie contenido de evidencia | **Si** | Cero archivos de 0 o 1 byte en todo el arbol |
| 4 | La comprobacion de sumas termina sin error sobre el clon limpio | **Si** | 564 de 564 sumas correctas |
| 5 | Todos los autores del historial son integrantes declarados con correo institucional | **Si** | 3 autor(es): gsanchezc6@uteq.edu.ec, wcedenoa2@uteq.edu.ec, ymunozq@uteq.edu.ec |
| 6 | Existe etiqueta anotada de linea base, publicada y alcanzable desde la rama por defecto | **Si** | 2 etiqueta(s) anotada(s) y alcanzable(s) desde main: 2B-final, 2B-final-v2.1 |
| 7 | La carpeta 07_Datos existe y la orden unica de analisis se ejecuta sin error | **Si** | python 07_Datos/scripts/ejecutar.py termino con codigo 0 |
| 8 | La carpeta 10_Autoria contiene los elementos A1 a A12 | **Si** | Los doce elementos existen y tienen contenido |
| 9 | Todo numero que aparece en los documentos procede de la salida de un script | Manual | La correspondencia salida-script esta declarada en 07_Publicacion/dataset_zenodo/correspondencia_salidas.csv. Requiere revision humana |
| 10 | Ningun dato personal aparece en la zona publica del repositorio | **Si** | Ninguna cedula ajena al equipo fuera de la zona restringida. Las 6 apariciones detectadas son las de los propios integrantes, declaradas por ellos en la caratula y en la composicion del equipo, no datos de participantes |
| 11 | Cada requisito del componente inteligente tiene metrica, unidad, umbral y metodo de verificacion | **Si** | 8 requisitos, todos con los seis atributos |
| 12 | La URL declarada en la caratula abre el repositorio desde una sesion sin autenticar | Manual | Comprobar en una ventana privada del navegador: https://github.com/gsanchezc6-beep/SIGA_FGMMN_ISR401_AVANCE_2B.git |

---

## Criterio de piso P4: ningun agente automatizado firma el historial

Comprobado sobre el cuerpo completo de todos los mensajes de commit: **ninguna**
marca de coautoria automatizada, ninguna firma de agente, ningun correo de
notificacion. El historial lo firman unicamente personas del equipo con su correo
institucional.

---

## Lo que esta lista no decide

Tres comprobaciones quedan marcadas como **manual** a proposito.

La numero 9 --- que todo numero de los documentos proceda de un script --- exige leer
los documentos y contrastarlos con la correspondencia declarada. Una maquina puede
comprobar que la correspondencia existe, no que sea cierta.

La numero 12 exige abrir la URL sin sesion iniciada, y este script no puede saber si
quien lo ejecuta tiene credenciales guardadas.

La numero 10 se ejecuta, pero su resultado es un indicio: busca secuencias de diez
digitos fuera de la zona restringida. Que no encuentre ninguna no prueba que no haya
datos personales de otra forma.

---

## Firmas

La guia exige que quien comprueba sea **una persona distinta de quien produjo cada
artefacto**. Con un solo firmante eso no se puede cumplir sobre el arbol entero:
los tres integrantes tienen confirmaciones, y quien mas produjo no puede verificarse
a si mismo. Se reparte en dos firmas que **entre las dos cubren todo el arbol sin
que nadie compruebe lo suyo**.

El reparto no es una declaracion de intenciones: sale del historial. Y se comprueba
**por archivo**, no por carpeta: los dos firmantes tienen confirmaciones dentro de
`02_Evidencias` y de `10_Autoria`, pero ninguno sobre los archivos que verifica el
otro.

### Primera firma

| | |
|---|---|
| Nombre | Cedeno Avila, Winston Damian |
| Correo institucional | wcedenoa2@uteq.edu.ec |
| Artefactos que **no** produjo, y que por tanto verifica | `01_ERS`, `03_Modelado`, `04_Trazabilidad`, `05_MVP`, `06_Experimento`, `07_Datos`, `07_Publicacion` y `08_Defensa` |
| Como se comprueba | Cero confirmaciones suyas en esas ocho carpetas, con `git log --format=%ae -- <carpeta>` |

Firma: ____________________________    Fecha: ______________

### Segunda firma

Cubre lo que produjo el primer firmante, y que por eso el no puede verificar.

| | |
|---|---|
| Nombre | Munoz Quinonez, Yeranick Esther |
| Correo institucional | ymunozq@uteq.edu.ec |
| Artefactos que **no** produjo, y que por tanto verifica | Los archivos depositados por Cedeno Avila: las seis transcripciones de la ronda terminal (`EV-20` a `EV-25`), la carpeta `control_calidad/` completa, `incorporar_codificacion.py` y sus dos capturas de A2 |
| Como se comprueba | Cero confirmaciones suyas **sobre esos archivos**. El reparto es por archivo y no por carpeta: los dos tienen confirmaciones en `02_Evidencias` y en `10_Autoria`, pero no sobre los mismos archivos. Se comprueba con `git log --format=%ae -- <archivo>` |

Firma: ____________________________    Fecha: ______________

> Ambos firmantes declaran haber revisado el resultado de arriba y las tres
> comprobaciones marcadas como manuales, cada uno sobre las rutas que le corresponden.

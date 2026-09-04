# SIGA — Sistema Inteligente de Gestion de Aulas

**Proyecto Fin de Curso — Entrega Final (2B)**
Ingenieria de Requerimientos (ISR-401) · 4.º nivel · Carrera de Software
Facultad de Ciencias de la Computacion · Universidad Tecnica Estatal de Quevedo (UTEQ)
Periodo Academico Ordinario 2026–2027

**URL del repositorio:** https://github.com/gsanchezc6-beep/SIGA_FGMMN_ISR401_AVANCE_2B

---

## 1. El sistema

SIGA es un sistema de gestion inteligente de aulas universitarias basado en Internet de
las Cosas y aprendizaje automatico, especificado para la Facultad de Ciencias de la
Computacion de la UTEQ como organizacion cliente identificable.

Cubre seis capacidades: monitoreo ambiental en tiempo real de temperatura, humedad y
ocupacion; control remoto de proyectores y climatizacion; generacion automatica de
alertas ante condiciones anomalas; analisis predictivo de fallos de equipamiento;
gestion del ciclo de vida de solicitudes de mantenimiento; y reportes administrativos
exportables.

Los perfiles de usuario elicitados en campo son **docentes (DOC)**, **coordinacion
academica (COORD)** y **conserjeria e infraestructura (CONS)**. La especificacion se
rige por ISO/IEC/IEEE 29148:2018 y los requisitos no funcionales se cuantifican sobre
el modelo de calidad de ISO/IEC 25010:2023.

El componente empirico es un cuasi-experimento apareado que compara la calidad de los
Requisitos Funcionales elicitados por analistas humanos frente a los generados por un
Modelo Grande de Lenguaje a partir del mismo corpus de entrevistas anonimizadas,
evaluados a ciegas por tres jueces independientes en cinco dimensiones de calidad.

---

## 2. Integrantes y roles

| Integrante | Rol | Correo institucional | ORCID |
|---|---|---|---|
| Sanchez Cornejo, Gary Alberto | Analista lider · componente empirico · integracion | gsanchezc6@uteq.edu.ec | [`0009-0009-9599-8806`](https://orcid.org/0009-0009-9599-8806) |
| Munoz Quinonez, Yeranick Esther | Documentacion, trazabilidad y gestion de evidencias | ymunozq@uteq.edu.ec | [`0009-0005-7711-8730`](https://orcid.org/0009-0005-7711-8730) |
| Cedeno Avila, Winston Damian | Transcripcion y anonimizacion del corpus de entrevistas | wcedenoa2@uteq.edu.ec | [`0009-0000-6086-6269`](https://orcid.org/0009-0000-6086-6269) |

> **Sobre la composicion.** Cedeno Avila se reincorpora el 2026-09-02 para la ronda terminal
> de campo. Mendoza Palma, Allan Jeremy, que figuraba en la caratula del SGA, se retiro del
> equipo sin producir artefactos ni confirmaciones. Quien responde por que, y desde cuando,
> se declara en
> [`04_Trazabilidad/composicion_equipo.md`](04_Trazabilidad/composicion_equipo.md).

> **Sobre los ORCID.** El apartado 9.2 de la guia los exige. Los tres integrantes se
> registraron el 2026-09-03 y sus identificadores constan arriba, cada uno enlazado a su
> registro publico. Hasta esa fecha el repositorio declaraba el hueco en lugar de omitir la
> columna.

Docente responsable: Ing. Gleiston Guerrero Ulloa.

El aporte de cada integrante, con el identificador del commit que lo respalda, se
declara en [`04_Trazabilidad/aporte_individual.csv`](04_Trazabilidad/aporte_individual.csv).

### Entregas anteriores del proyecto

El historial de **este** repositorio comienza el 2026-08-30, cuando se reorganizo el arbol
para la Entrega Final. La trazabilidad acumulada del proyecto no vive aqui: se reparte entre
los repositorios de cada entrega, que se enlazan para que la cadena 1A a 2B pueda auditarse
sin depender de la memoria de nadie.

| Entrega | Repositorio |
|---|---|
| Entrega 3 (2A) --- Especificacion y modelado | <https://github.com/gsanchezc6-beep/SIGA_FGMMN_ISR401_AVANCE_2A> |
| Entrega Final (2B) --- esta | <https://github.com/gsanchezc6-beep/SIGA_FGMMN_ISR401_AVANCE_2B> |

Los artefactos de las entregas anteriores que siguen vigentes se incorporaron a este
repositorio y su evolucion consta en `CHANGELOG.md`. Los que quedaron superados permanecen
solo en el repositorio de su entrega.

> **Por que hay un repositorio nuevo.** La Entrega Final se rigio por una rubrica distinta
> de la que goberno la Entrega 2A, con otra estructura de carpetas y otro conjunto de
> entregables. El equipo abrio este repositorio el 2026-08-29 para que el arbol
> correspondiera exactamente a la estructura exigida, en lugar de reorganizar el anterior y
> arrastrar carpetas de una entrega ya evaluada. Por eso el historial de aqui empieza el
> 2026-08-30 aunque la evidencia de campo este fechada meses antes: el trabajo anterior
> consta en el repositorio de la 2A, enlazado arriba. El motivo, las fechas y lo que el
> equipo asume por esa decision estan en `CHANGELOG.md`, version `2B-1.7.0`.

---

## 3. Identificadores persistentes y como citar

| Que | Identificador |
|---|---|
| Paquete de datos en Zenodo | [`10.5281/zenodo.22137679`](https://doi.org/10.5281/zenodo.22137679) |
| Registro previo del protocolo en OSF | [`10.17605/OSF.IO/7PQ3H`](https://doi.org/10.17605/OSF.IO/7PQ3H) |
| **Linea base vigente** | Etiqueta anotada **`2B-final-v2.1`**, sobre el commit `0e69071`. `2B-final` apunta al mismo commit y se conserva como referencia historica |
| Desviaciones respecto del protocolo | `06_Experimento/osf_deviations.pdf` |
| Codigo archivado en Software Heritage | `swh:1:snp:861295fead33417e3efc2753fd4a34897014a891` |
| Autoevaluacion FAIR | `fair_assessment.pdf` --- 21 de 26 indicadores, **80,8 %** |
| Manuscrito | `07_Publicacion/manuscrito_final.pdf` |
| Especificacion de requisitos | [`01_ERS/ERS_SRS_2B_v2.0.pdf`](01_ERS/ERS_SRS_2B_v2.0.pdf) --- 130 paginas |
| **Curva de saturacion tematica** | [`02_Evidencias/Codificacion_Tematica/curva_saturacion.png`](02_Evidencias/Codificacion_Tematica/curva_saturacion.png) · datos en `saturacion_por_entrevista.csv` · insertada en el manuscrito, Fig. 4 |
| **Calculo de potencia** | [`06_Experimento/resultados/power_calculation.csv`](06_Experimento/resultados/power_calculation.csv) · script `scripts_analisis/power_calculation.py` · tabla en el manuscrito, `tabla_power_calculation.tex` |

**Cita recomendada del paquete de datos:**

> Sanchez Cornejo, G. A. y Munoz Quinonez, Y. E. (2026). *Conjunto de datos del proceso de
> Ingenieria de Requerimientos del proyecto SIGA*. Zenodo.
> https://doi.org/10.5281/zenodo.22137679

Los metadatos de citacion legibles por maquina estan en `CITATION.cff`, con los tres
identificadores anteriores.

## 4. Estructura del repositorio

Nombres ASCII, sin acentos, sin espacios, palabras separadas con guion bajo.
Los archivos multimedia siguen la convencion `AAAA-MM-DD_TipoParticipante_Codigo_Tecnica.ext`.

> **Sobre el tercer campo del nombre.** La convencion nombra ese campo
> `NombreApellido`. En este repositorio se sustituye por el **codigo de participante**
> (`DOC-nn`, `COORD-nn`, `CONS-nn`, `ENT-nn`) porque el protocolo de disociacion de
> datos personales exigido por la seccion 5.10 y por la Ley Organica de Proteccion de
> Datos Personales prohibe publicar nombres propios en la evidencia. La correspondencia
> codigo–participante existe unicamente en el registro de custodia que se entrega al
> docente por el sistema de gestion academica. Sustitucion declarada en
> [`07_Publicacion/dataset_zenodo/anonimizacion.md`](07_Publicacion/dataset_zenodo/anonimizacion.md).

```
SIGA_FGMMN_ISR401_AVANCE_2B/
├── README.md                     Este archivo
├── LICENSE                       Apache-2.0 (codigo) + CC BY 4.0 (datos y documentos)
├── CITATION.cff                  Metadatos de citacion
├── CHANGELOG.md                  Historial de versiones
├── checksums.sha256              Sumas SHA-256 de la evidencia binaria y de datos
├── reporte.tex                   Documento entregado (se compila a reporte.pdf)
├── referencias.bib               Bibliografia del reporte, formato IEEE
├── 01_ERS/                       Especificacion de Requisitos de Software
│   ├── ERS_SRS_2B_v2.0.tex       Documento maestro
│   ├── secciones_generadas.tex   Cuerpo de la especificacion
│   ├── referencias.bib
│   ├── Auditoria_Calidad/        Las seis metricas de la seccion 5.6, con conteos base
│   └── Componentes_IA/           Fichas de los componentes de aprendizaje automatico
│
├── 02_Evidencias/                Evidencia primaria de campo
│   ├── Consentimientos/          Consentimientos informados firmados
│   ├── Video/                    Entrevistas en video
│   ├── Audio/                    Entrevistas en audio, redundantes con el video
│   ├── Transcripciones/          Una por entrevista, con marca de tiempo
│   ├── Guiones_Entrevista/       Version final aplicada, con historial de cambios
│   ├── Cuestionario/
│   │   ├── Respuestas/           Exportacion directa con marca temporal
│   │   └── Fotos_Aplicacion/     Evidencia fotografica de la aplicacion
│   ├── Fotos_Entorno/            Fotografias del sitio del cliente
│   ├── Documentos_Organizacion/  Documentos originales de la organizacion
│   ├── Codificacion_Tematica/    Tabla de codificacion con cobertura declarada
│   └── Validacion/
│       └── Sesiones_Validacion/  Sesiones con partes interesadas: video mas acta
│
├── 03_Modelado/                  Cada diagrama con su archivo fuente nativo
│   ├── 01_Contexto/              Contexto y frontera del sistema
│   ├── 02_iStar_SD/              Dependencias estrategicas
│   ├── 03_iStar_SR/              Razones estrategicas
│   ├── 04_Casos_Uso/             Diagrama general de casos de uso
│   ├── 05_Clases/                Diagrama de clases refinado
│   ├── 06_Secuencia/             Uno por caso de uso obligatorio
│   ├── 07_Actividad/             Uno por flujo principal
│   ├── 08_Estados/               Uno por entidad con ciclo de vida no trivial
│   ├── 10_Componentes/           Diagrama de componentes
│   ├── 11_Despliegue/            Diagrama de despliegue
│   └── 12_Prototipos_Interfaz/   Uno por pantalla obligatoria
│
├── 04_Trazabilidad/              Matriz, priorizacion MoSCoW/Kano y aporte individual
├── 05_MVP/
│   ├── codigo_fuente/            Codigo organizado por modulos
│   ├── despliegue/               Instrucciones reproducibles desde cero
│   └── demostracion/             Video del recorrido funcional
│
├── 06_Experimento/               Componente empirico y paquete de replicacion
│   ├── Makefile                  Pipeline completo con una sola orden
│   ├── replicar.py               El mismo pipeline sin depender de make
│   ├── protocolo/                Preguntas, hipotesis, variables y plan de analisis
│   ├── osf_deviations.pdf        Desviaciones declaradas respecto del protocolo
│   ├── registro_previo/          Comprobante OSF y bitacora de desviaciones
│   ├── instrumentos/             Guiones, cuestionarios y rubricas en version final
│   ├── prompts_llm/              Consignas literales usadas con el modelo de lenguaje
│   ├── clave_desciego_items.csv  Tabla que asigna origen a cada item ciego
│   ├── datos_crudos/             Formato abierto, sin edicion manual posterior
│   ├── datos_procesados/         Generados exclusivamente por script
│   ├── scripts_analisis/         Analisis reproducible, con una sola orden
│   └── resultados/               Salidas estadisticas
│
├── 07_Publicacion/               Manuscrito y deposito de datos
│   ├── manuscrito_final.tex      Manuscrito en plantilla Springer LNCS
│   ├── manuscrito_final.pdf      Compilado, 12 paginas
│   ├── referencias.bib           40 entradas, 35 con DOI verificado
│   ├── analisis_revistas.md      Eleccion de la conferencia objetivo
│   ├── figuras/  tablas/         Producidas por los scripts, no a mano
│   └── dataset_zenodo/           Paquete depositado en Zenodo con DOI
│
└── 08_Defensa/                   Presentacion, guion, folleto y banco de preguntas
```

La estructura sigue el arbol obligatorio de la seccion 9.1 de la guia. Las evidencias
de etica quedan en `02_Evidencias/Etica/`, junto al resto de la evidencia primaria, y el
resumen del proceso etico del paquete publicado esta en
`07_Publicacion/dataset_zenodo/ETHICS.md`.

---

### Elementos aun no depositados

Se declaran aqui, y no en el arbol de arriba, para que **nada de lo que este repositorio
nombra deje de existir**. Cada uno tiene su artefacto redactado o disenado fuera del
repositorio, a la espera de la firma o del trabajo de campo que lo respalda.

| Elemento | Estado |
|---|---|
| `02_Evidencias/Cuestionario/Instrumento/` | El formulario aplicado no se ha depositado. Las respuestas y las fotografias de aplicacion si constan |
| `02_Evidencias/Notas_Campo/` | Seis notas redactadas para las seis jornadas de observacion, pendientes de revision y firma del observador |
| `02_Evidencias/Validacion/Inspeccion/` | Registros de inspeccion, defectos y re-inspeccion redactados; la sesion formal esta pendiente de celebrarse |
| `02_Evidencias/Validacion/Solicitudes_Cambio/` | Tres solicitudes y el acta del comite redactadas, pendientes de la sesion del comite |
| `03_Modelado/09_DFD/` | Diagramas de nivel 0 y nivel 1 disenados y dibujados, pendientes de revision antes de depositarlos. El criterio C2 pide diagramas UML consistentes con el codigo y no menciona los DFD; el modelado que ese criterio evalua esta completo en las otras once carpetas de `03_Modelado/` |

---

## 5. Compilacion del documento entregado

Compilador: **pdfLaTeX** con **BibTeX**, distribucion TeX Live 2024 o MiKTeX 24.
Paquetes requeridos: `babel`, `geometry`, `graphicx`, `float`, `longtable`, `booktabs`,
`amssymb`, `xcolor`, `hyperref`, `enumitem`, `fancyhdr`, `titlesec`, `lastpage`.

Archivo principal: `reporte.tex`. Orden exacto de comandos, desde la raiz de un clon
limpio:

```bash
pdflatex  -interaction=nonstopmode reporte.tex
bibtex    reporte
pdflatex  -interaction=nonstopmode reporte.tex
pdflatex  -interaction=nonstopmode reporte.tex
```

El resultado es `reporte.pdf`, identico en contenido al documento entregado.

La Especificacion de Requisitos se compila por separado, con la misma secuencia:

```bash
cd 01_ERS
pdflatex  -interaction=nonstopmode ERS_SRS_2B_v2.0.tex
bibtex    ERS_SRS_2B_v2.0
pdflatex  -interaction=nonstopmode ERS_SRS_2B_v2.0.tex
pdflatex  -interaction=nonstopmode ERS_SRS_2B_v2.0.tex
```

---

## 6. Reproduccion del analisis

### Dependencias

- Python >= 3.11
- `pandas`, `numpy`, `scipy`, `scikit-learn`, `matplotlib`, `statsmodels`
- `sha256sum` (en Windows, disponible con Git Bash)
- GNU Make es **opcional**: `replicar.py` ejecuta el mismo pipeline sin el

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install pandas numpy scipy scikit-learn matplotlib statsmodels
```

### Ejecucion completa

Una sola orden, partiendo unicamente de los datos crudos. Las dos rutas son
equivalentes y producen las mismas salidas byte a byte:

```bash
python 06_Experimento/replicar.py
```

```bash
cd 06_Experimento && make all
```

El pipeline consolida las hojas de puntuacion de los tres jueces, calcula el acuerdo
inter-evaluador (kappa de Cohen ponderado por par y kappa de Fleiss), ejecuta las
pruebas de supuestos (Shapiro-Wilk y Levene), aplica la prueba de hipotesis por
dimension con correccion de Holm-Bonferroni, calcula el tamano del efecto con intervalo
de confianza al 95 % por bootstrap de 10 000 replicas con semilla `20260802`, genera la
curva de saturacion tematica y el calculo de potencia, y escribe todas las tablas y
todas las figuras del reporte en `tablas/` y `figuras/`.

Ninguna cifra del reporte se escribe a mano. Cada tabla y cada figura se regenera con
esa orden; la correspondencia entre cada salida y el script que la produce esta en
[`07_Publicacion/dataset_zenodo/correspondencia_salidas.csv`](07_Publicacion/dataset_zenodo/correspondencia_salidas.csv).

### Verificacion de integridad

```bash
sha256sum -c checksums.sha256
```

Debe terminar sin un solo error sobre un clon limpio.

Sin `sha256sum`, y anadiendo el sondeo de codec y duracion del material audiovisual:

```bash
python 06_Experimento/replicar.py --verificar
```

---

## 7. Cierre de campo en dieciseis entrevistas

El corpus son **N = 16 entrevistas validas**. El levantamiento se habia cerrado en diez el
2026-08-17, por autorizacion verbal del docente ante la restriccion de calendario; esa
decision y sus limites estan documentados en
[`02_Evidencias/Etica/declaracion_reduccion_muestra.md`](02_Evidencias/Etica/declaracion_reduccion_muestra.md).
La **ronda terminal del 2026-09-03** anadio seis entrevistas a docentes (`EV-20` a `EV-25`)
y llevo el corpus al minimo terminal aplicable, con lo que aquella reduccion queda superada.
El documento de etica se conserva sin reescribir, con una nota de estado al inicio: registra
lo que ocurrio y cuando, que es justamente lo que lo hace util.

**Las seis de la ronda terminal estan transcritas pero todavia no codificadas**, de modo que
la codificacion tematica y la curva de saturacion que se citan mas abajo siguen cubriendo las
diez primeras. Las grabaciones de esas seis no se publican, por lo que dice su
consentimiento: su ficha tecnica y su ubicacion constan en
[`02_Evidencias/00_Restringido/`](02_Evidencias/00_Restringido/).

Un tamano menor al de referencia se sostiene con el calculo que lo justifica, conforme
a la seccion 6 de la guia. Ese calculo esta en
[`06_Experimento/resultados/power_calculation.csv`](06_Experimento/resultados/power_calculation.csv):
para detectar un efecto d = 0,50 con alfa = 0,05 y potencia 0,80 se requieren 34
unidades; con las disponibles la potencia alcanzada es del 8,4 %. La consecuencia sobre
la interpretacion de los resultados se declara en la seccion de amenazas a la validez
del reporte.

La curva de saturacion tematica **no alcanza inflexion** sobre las diez codificadas: la
ultima entrevista todavia aporta cuatro codigos nuevos sobre 36 acumulados
([`tablas/saturacion_por_entrevista.csv`](tablas/saturacion_por_entrevista.csv)). Se
declara como limitacion remanente, no como saturacion alcanzada.

Una entrevista adicional (EV-15, participante DOC-03) fue excluida por retiro del
consentimiento informado del participante, y su material fue suprimido conforme a la
politica de conservacion y supresion declarada en `02_Evidencias/Etica/`.

---

## 8. Licenciamiento

| Alcance | Licencia |
|---|---|
| Codigo del prototipo y scripts de analisis | Apache-2.0 |
| Datos, documentos, figuras, transcripciones y reporte | CC BY 4.0 |

El alcance exacto de cada una se declara en [`LICENSE`](LICENSE).

---

## 9. Declaracion de uso de inteligencia artificial

La declaracion obligatoria, seccion por seccion, con herramienta empleada, tipo de
asistencia y metodo concreto de validacion aplicado, esta en
[`02_Evidencias/Etica/declaracion_uso_ia.md`](02_Evidencias/Etica/declaracion_uso_ia.md) y se reproduce como
anexo del reporte.

Los modelos de lenguaje intervienen en este trabajo en dos capacidades separadas: como
**objeto de estudio**, generando el Conjunto A de Requisitos Funcionales bajo condiciones
registradas en [`06_Experimento/consignas/`](06_Experimento/consignas/); y como **apoyo
de redaccion** sobre contenido escrito por el equipo. Las secciones evaluativas
—analisis, discusion, conclusiones, justificacion de decisiones de ingenieria y amenazas
a la validez— son produccion propia verificada contra la evidencia primaria.

---

## 10. Estado de la entrega

El inventario de lo que existe y de lo que falta, contrastado item por item contra los
minimos de la seccion 5 de la guia, se lleva en el control de trabajo del equipo, **fuera
de este repositorio**, para que ninguna nota de proceso se cuele en la entrega.

---

<sub>Universidad Tecnica Estatal de Quevedo · Facultad de Ciencias de la Computacion ·
Ingenieria de Requerimientos ISR-401 · Equipo FGMMN · 2026</sub>

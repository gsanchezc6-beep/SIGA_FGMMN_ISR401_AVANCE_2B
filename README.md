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

| Integrante | Rol | Correo institucional |
|---|---|---|
| Sanchez Cornejo, Gary Alberto | Analista lider · componente empirico · integracion | gsanchezc6@uteq.edu.ec |
| Munoz Quinonez, Yeranick Esther | Documentacion y gestion de evidencias | — |
| Cedeno Avila, Winston Damian | Modelado y desarrollo del prototipo | — |
| Mendoza Palma, Allan Jeremy | Modelado UML e i* | — |
| Gilces Carranza, Jose Ignacio | Verificacion — **sin aporte registrado en el historial** | — |

Docente responsable: Ing. Gleiston Guerrero Ulloa.

El aporte de cada integrante, con el identificador del commit que lo respalda, se
declara en [`04_Trazabilidad/aporte_individual.csv`](04_Trazabilidad/aporte_individual.csv).

---

## 3. Estructura del repositorio

Nombres ASCII, sin acentos, sin espacios, palabras separadas con guion bajo.
Los archivos multimedia siguen la convencion `AAAA-MM-DD_TipoParticipante_Codigo_Tecnica.ext`.

> **Sobre el tercer campo del nombre.** La convencion nombra ese campo
> `NombreApellido`. En este repositorio se sustituye por el **codigo de participante**
> (`DOC-nn`, `COORD-nn`, `CONS-nn`, `ENT-nn`) porque el protocolo de disociacion de
> datos personales exigido por la seccion 5.10 y por la Ley Organica de Proteccion de
> Datos Personales prohibe publicar nombres propios en la evidencia. La correspondencia
> codigo–participante existe unicamente en el registro de custodia que se entrega al
> docente por el sistema de gestion academica. Sustitucion declarada en
> [`07_Datos/anonimizacion.md`](07_Datos/anonimizacion.md).

```
SIGA_FGMMN_ISR401_AVANCE_2B/
├── README.md                     Este archivo
├── LICENSE                       Apache-2.0 (codigo) + CC BY 4.0 (datos y documentos)
├── CITATION.cff                  Metadatos de citacion
├── CHANGELOG.md                  Historial de versiones
├── checksums.sha256              Sumas SHA-256 de todos los archivos multimedia
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
│   │   ├── Instrumento/          Formulario aplicado
│   │   ├── Respuestas/           Exportacion directa con marca temporal
│   │   └── Fotos_Aplicacion/     Evidencia fotografica de la aplicacion
│   ├── Fotos_Entorno/            Fotografias del sitio del cliente
│   ├── Documentos_Organizacion/  Documentos originales de la organizacion
│   ├── Notas_Campo/              Una por sesion de observacion
│   ├── Codificacion_Tematica/    Tabla de codificacion con cobertura declarada
│   └── Validacion/
│       ├── Inspeccion/           Registro de inspeccion, defectos y re-inspeccion
│       ├── Solicitudes_Cambio/   Solicitudes tramitadas y actas del comite
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
│   ├── 09_DFD/                   Flujo de datos de nivel 0 y nivel 1
│   ├── 10_Componentes/           Diagrama de componentes
│   ├── 11_Despliegue/            Diagrama de despliegue
│   └── 12_Prototipos_Interfaz/   Uno por pantalla obligatoria
│
├── 04_Trazabilidad/              Matriz, huerfanos, tablero, linea base, aporte
├── 05_MVP/
│   ├── codigo_fuente/            Codigo organizado por modulos
│   ├── despliegue/               Instrucciones reproducibles desde cero
│   └── demostracion/             Video del recorrido funcional
│
├── 06_Experimento/               Componente empirico
│   ├── Makefile                  Pipeline completo con una sola orden
│   ├── protocolo/                Preguntas, hipotesis, variables y plan de analisis
│   ├── registro_previo/          Comprobante OSF y bitacora de desviaciones
│   ├── instrumentos/             Guiones, cuestionarios y rubricas en version final
│   ├── consignas/                Consignas literales usadas con el modelo de lenguaje
│   └── resultados/               Salidas estadisticas
│
├── 07_Datos/                     Paquete de replicacion ejecutable
│   ├── datos_crudos/             Formato abierto, sin edicion manual posterior
│   ├── datos_procesados/         Generados exclusivamente por script
│   ├── scripts/                  Analisis reproducible, con una sola orden
│   ├── figuras/  tablas/         Salidas correspondidas con el reporte
│   ├── diccionario_datos.csv     Significado, tipo y rango de cada variable
│   └── anonimizacion.md          Procedimiento de disociacion aplicado
│
├── 08_Etica/                     Consentimiento, base legal, conservacion, uso de IA
└── 09_Defensa/                   Presentacion, banco de preguntas y guion de reparto
```

`08_Etica/` y `09_Defensa/` no figuran en la lista de carpetas obligatorias de la
seccion 9, pero las secciones 5.10 y 5.11 exigen artefactos que necesitan alojamiento
propio y que no encajan en las siete carpetas nombradas. Se anaden sin desplazar a
ninguna de ellas.

---

## 4. Compilacion del documento entregado

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

## 5. Reproduccion del analisis

### Dependencias

- Python >= 3.11
- `pandas`, `numpy`, `scipy`, `scikit-learn`, `matplotlib`, `statsmodels`
- GNU Make y `sha256sum` (en Windows, disponibles con Git Bash)

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install pandas numpy scipy scikit-learn matplotlib statsmodels
```

### Ejecucion completa

Una sola orden, partiendo unicamente de los datos crudos:

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
[`07_Datos/correspondencia_salidas.csv`](07_Datos/correspondencia_salidas.csv).

### Verificacion de integridad

```bash
sha256sum -c checksums.sha256
```

Debe terminar sin un solo error sobre un clon limpio.

---

## 6. Cierre de campo en diez entrevistas

El levantamiento de campo se cerro en **N = 10 entrevistas validas**, por autorizacion
expresa del docente responsable ante la restriccion de calendario. La constancia escrita
de esa autorizacion se deposita en `08_Etica/` y se cita desde la seccion de
participantes del reporte.

Un tamano menor al de referencia se sostiene con el calculo que lo justifica, conforme
a la seccion 6 de la guia. Ese calculo esta en
[`06_Experimento/resultados/power_calculation.csv`](06_Experimento/resultados/power_calculation.csv):
para detectar un efecto d = 0,50 con alfa = 0,05 y potencia 0,80 se requieren 34
unidades; con las disponibles la potencia alcanzada es del 8,4 %. La consecuencia sobre
la interpretacion de los resultados se declara en la seccion de amenazas a la validez
del reporte.

La curva de saturacion tematica **no alcanza inflexion**: la ultima entrevista todavia
aporta cuatro codigos nuevos sobre 36 acumulados
([`tablas/saturacion_por_entrevista.csv`](tablas/saturacion_por_entrevista.csv)). Se
declara como limitacion remanente, no como saturacion alcanzada.

Una entrevista adicional (EV-15, participante DOC-03) fue excluida por retiro del
consentimiento informado del participante, y su material fue suprimido conforme a la
politica de conservacion y supresion declarada en `08_Etica/`.

---

## 7. Licenciamiento

| Alcance | Licencia |
|---|---|
| Codigo del prototipo y scripts de analisis | Apache-2.0 |
| Datos, documentos, figuras, transcripciones y reporte | CC BY 4.0 |

El alcance exacto de cada una se declara en [`LICENSE`](LICENSE).

---

## 8. Declaracion de uso de inteligencia artificial

La declaracion obligatoria, seccion por seccion, con herramienta empleada, tipo de
asistencia y metodo concreto de validacion aplicado, esta en
[`08_Etica/declaracion_uso_ia.md`](08_Etica/declaracion_uso_ia.md) y se reproduce como
anexo del reporte.

Los modelos de lenguaje intervienen en este trabajo en dos capacidades separadas: como
**objeto de estudio**, generando el Conjunto A de Requisitos Funcionales bajo condiciones
registradas en [`06_Experimento/consignas/`](06_Experimento/consignas/); y como **apoyo
de redaccion** sobre contenido escrito por el equipo. Las secciones evaluativas
—analisis, discusion, conclusiones, justificacion de decisiones de ingenieria y amenazas
a la validez— son produccion propia verificada contra la evidencia primaria.

---

## 9. Estado de la entrega

El inventario de lo que existe y de lo que falta, contrastado item por item contra los
minimos de la seccion 5 de la guia, se lleva en el control de trabajo del equipo, **fuera
de este repositorio**, para que ninguna nota de proceso se cuele en la entrega.

---

<sub>Universidad Tecnica Estatal de Quevedo · Facultad de Ciencias de la Computacion ·
Ingenieria de Requerimientos ISR-401 · Equipo FGMMN · 2026</sub>

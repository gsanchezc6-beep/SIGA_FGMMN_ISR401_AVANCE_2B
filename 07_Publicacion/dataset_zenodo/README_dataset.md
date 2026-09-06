# README — Dataset Zenodo: Proyecto SIGA (Ingeniería de Requerimientos, ISR-401, UTEQ)

## Descripción general
Este paquete contiene los artefactos de datos del proceso de Ingeniería de
Requerimientos del proyecto SIGA (Sistema Inteligente de Gestión de Aulas),
equipo FGMMN, asignatura ISR-401, Universidad Técnica Estatal de Quevedo (UTEQ).
Corresponde a la Entrega 4 (2B) y acompaña al manuscrito
`07_Publicacion/manuscrito_final.tex`.

## Estructura y diccionario de datos

Todos los archivos de esta carpeta están en su raíz (sin subcarpetas por
sección del repositorio principal).

- `ANONYMIZATION.md` — Procedimiento de seudonimización y anonimización aplicado
  a entrevistas, consentimientos y actas antes de su publicación.
- `ETHICS.md` — Declaración ética y proceso de consentimiento informado.
- `panel_ampliado/` — **Las dos vueltas del panel ampliado de evaluadores, que
  no se pudo usar.** Datos crudos de siete evaluadores el 2026-09-05 y de los
  mismos siete con un instrumento corregido el 2026-09-06, el mapa de posiciones
  de la segunda vuelta y el script que reproduce las cuatro tablas de análisis.
  No es el análisis del estudio --- ese sigue siendo el de los tres jueces del
  registro previo, en `resultados_jueces/` --- sino la comprobación de robustez
  que falló las dos veces, con el diagnóstico de por qué. Se publica porque un
  intento fallido que se calla es lo que hace irreproducible un estudio.
  Ejecutar con `python panel_ampliado/analizar_panel_ampliado.py`.
- `scripts_analisis/robustez_saturacion.py` — Comprueba que la saturación
  temática no depende del orden de las entrevistas, probando las 720
  ordenaciones posibles del bloque de seis realizadas el mismo día.
- `codificacion_tematica.csv` — Codificación abierta de **136 fragmentos** bajo
  **50 códigos**, extraídos de las **16 entrevistas** del corpus (EV-01, EV-02,
  EV-08 a EV-14, EV-16 y EV-20 a EV-25; EV-15 excluida por retiro de
  consentimiento informado). Las seis de la ronda terminal se codificaron el
  2026-09-06 y entran ya en este archivo y en la curva de saturación. Aviso para
  quien replique: **los dos conjuntos de requisitos que compara el
  cuasi-experimento se generaron a partir de las diez primeras** y no se
  regeneraron. Columnas:
  Fragmento (cita textual), Codigo (etiqueta de codificación abierta),
  Categoria (categoría axial), Requisito_derivado (RF/RNF relacionado),
  ID_evidencia (código de entrevista), Analista_codificador.
- `corpus_rf_rnf_etiquetado.json` — Corpus de RF/RNF etiquetado (`proyecto`,
  `n_requisitos`, `requisitos`) usado como insumo del componente empírico.
- `matriz_trazabilidad.csv` — **74 filas**. Columnas: Ley, Articulo, Objetivo,
  Stakeholder, ID-EV, ID-RF, Tipo, ID-CU, ID-HU, ID-CA, ID-Componente,
  ID-Mockup.
- `priorizacion_moscow_kano.csv` — Prioridad MoSCoW, resultados WSJF (17 filas
  con datos reales de sesión de equipo) y clasificación Kano (3 pares
  funcional/disfuncional reales del cuestionario; RF-12 y RF-09 sin
  clasificar por ausencia de instrumento Kano para esos ítems).
- `respuestas_cuestionario.csv` — 31 respuestas reales del cuestionario a
  usuarios (Google Forms), anonimizadas.
- `transcripciones_anonimizadas.json` — Las 10 transcripciones válidas,
  anonimizadas (`n_transcripciones = 10`).
- `prompts_llm/`
  - `prompt_llm_conjunto_A.md` — Registro de la consigna exacta, modelo
    (Claude Sonnet 5, interfaz de chat), material fuente y limitación
    metodológica declarada (el modelo no era una instancia "ingenua": tuvo
    exposición previa parcial al Conjunto B humano en la misma cuenta de
    chat — amenaza a la validez de constructo).
  - `material_fuente_LLM.txt` — Corpus de las **11 entrevistas recolectadas**
    entregado al modelo (snapshot congelado, anterior a la exclusión de
    EV-15; ver limitación 1 más abajo).
  - `Conjunto_A_RF_LLM.md` — Los 26 RF generados por el LLM.
- `resultados_jueces/` — Componente empírico (Enfoque 1: RF humanos vs. LLM):
  - `juez1.csv`, `juez2.csv`, `juez3.csv` — Puntuaciones reales de los 3
    jueces evaluadores (5 dimensiones × 51 ítems cada uno).
  - `resumen_resultados.csv` — Medias por conjunto (Humano/LLM) y estadístico
    por dimensión.
  - `supuestos.csv` — Normalidad (Shapiro-Wilk) y homogeneidad de varianzas
    (Levene) por dimensión.
  - `hipotesis.csv` — Prueba (t apareada o Wilcoxon), p-valor crudo y p-valor
    ajustado por Holm-Bonferroni, por dimensión.
  - `efectos.csv` — Tamaño del efecto (Cohen's d o equivalente) con IC 95 %
    por bootstrap (10 000 réplicas, semilla 20260802).
  - `acuerdo_interevaluador.csv` — κ de Cohen (por par de jueces) y κ de
    Fleiss conjunto, por dimensión.
  - `power_calculation.csv` — Cálculo de potencia post-hoc: potencia
    alcanzada con n = 3 jueces y n necesario para 80 % de potencia
    convencional.
- `scripts_analisis/` — Pipeline de análisis estadístico reproducible
  (`analizar_resultados.py`, `curva_saturacion.py`, `generar_figuras.py`,
  `generar_tablas.py`, `power_calculation.py`, `verificar_fichas.py`;
  requiere pandas/scipy/numpy/statsmodels). Orquestado por
  `06_Experimento/Makefile` (`make all`).

## Limitaciones metodológicas declaradas (transparencia obligatoria)
1. **Asimetría de corpus entre Conjunto A y Conjunto B:** el Conjunto A (LLM)
   se generó sobre el corpus completo de las 11 entrevistas recolectadas
   (`material_fuente_LLM.txt`); el Conjunto B (humano) usa las 10 que
   permanecen válidas tras excluir EV-15 por retiro de consentimiento
   informado. Se declara como amenaza a la validez de constructo.
   **Y una asimetría más, posterior:** el análisis cualitativo
   (`codificacion_tematica.csv`, `transcripciones_anonimizadas.json`) pasó a
   cubrir las 16 entrevistas del corpus el 2026-09-06, mientras que los dos
   conjuntos comparados siguen anclados a las 10 primeras porque no se
   regeneraron. Quien replique debe tener presente que el corpus codificado y
   el corpus del que salieron los requisitos comparados **no son el mismo**.
2. **Validez de constructo (exposición previa del LLM):** el modelo que
   generó los 26 RF del Conjunto A tuvo exposición previa parcial al
   Conjunto B humano en la misma cuenta de chat. Ver detalle en
   `prompts_llm/prompt_llm_conjunto_A.md`.
3. **Potencia estadística:** con n = 3 jueces, la potencia alcanzada es de
   8,4 % (ver `resultados_jueces/power_calculation.csv`); se necesitarían 34
   jueces para el 80 % convencional. Los tamaños de efecto deben
   interpretarse con cautela, no como magnitudes poblacionales robustas.
4. **Corrección por comparaciones múltiples:** tras Holm-Bonferroni, ninguna
   de las 5 dimensiones evaluadas mantiene significancia estadística (ver
   `resultados_jueces/hipotesis.csv`).
5. **Saturación temática alcanzada, y con qué reservas:** con las 16
   entrevistas codificadas el promedio de códigos nuevos de las tres últimas es
   1,333 frente a un umbral de 2,50. Con solo 10 no saturaba, por un libro de
   códigos de 36 códigos para 36 fragmentos que estructuralmente no podía
   aplanarse. El resultado resiste las 720 ordenaciones posibles del bloque de
   entrevistas del mismo día. Dos reservas declaradas: las instrucciones de
   codificación pedían reutilizar códigos, lo que empuja hacia este resultado, y
   las seis entrevistas añadidas son todas del perfil docente.

## Licencia
CC BY 4.0.

## Preregistro
Protocolo registrado en OSF — DOI [10.17605/OSF.IO/7PQ3H](https://doi.org/10.17605/OSF.IO/7PQ3H).
Las desviaciones respecto del registro se documentan explícitamente en
`06_Experimento/registro_previo/registro_osf.md`.

## Contacto
Gary Alberto Sánchez Cornejo, analista líder, equipo FGMMN — Facultad de
Ciencias de la Computación y Diseño Digital, UTEQ.

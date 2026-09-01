# Protocolo del componente empírico — Proyecto SIGA
## Enfoque 1: Comparación de calidad de RF humanos vs. RF generados por LLM

## PICOC

| Elemento | Definición |
|---|---|
| **P**oblación | Requisitos funcionales del sistema SIGA (26 generados por LLM, 25 elicitados por el equipo humano) |
| **I**ntervención | Elicitación asistida por modelo de lenguaje grande (Claude Sonnet 5), a partir del corpus completo de 11 entrevistas anonimizadas |
| **C**omparación | Elicitación tradicional por el equipo humano (entrevistas + análisis manual) |
| **O**utcome (resultado) | Puntuación de calidad en 5 dimensiones (completitud, ausencia de ambigüedad, verificabilidad, corrección respecto de la fuente, consistencia interna), evaluada por ≥3 jueces ciegos |
| **C**ontexto | Proyecto académico de Ingeniería de Requerimientos, dominio de gestión inteligente de aulas, Facultad de Ciencias de la Computación, UTEQ |

## Pregunta de investigación

¿En qué dimensiones de calidad los requisitos funcionales elicitados por
un equipo humano difieren de los generados por un modelo de lenguaje
grande a partir del mismo material fuente?

## Hipótesis

- **H0:** No hay diferencia significativa en la puntuación media de
  calidad entre el Conjunto A (LLM) y el Conjunto B (humano) en ninguna
  de las 5 dimensiones evaluadas.
- **H1:** Existe una diferencia significativa en la puntuación media de
  calidad entre el Conjunto A y el Conjunto B en al menos una dimensión.

## Variables

| Tipo | Variable |
|---|---|
| Independiente | Origen del requisito (Humano / LLM) |
| Dependientes | Puntuación 1-5 en cada una de las 5 dimensiones de la rúbrica |
| Control | Mismo material fuente para ambos conjuntos; mismos jueces evalúan ambos conjuntos; orden aleatorizado y ciego |

## Participantes (jueces evaluadores)

**Requisito de independencia:** ninguno de los jueces puede ser una de
las personas entrevistadas en las 11 transcripciones que sirvieron como
material fuente (DOC-01 a DOC-04, COORD-01 a COORD-03, CONS-01 a
CONS-04), para preservar la ceguera del diseño. Mínimo 3 jueces; se
recomiendan 5 si es posible, siguiendo la Sección 5.1 de la guía.

## Diseño

Cuasi-experimento apareado. Cada juez evalúa los 51 ítems del paquete
ciego (`Paquete_Evaluacion_Ciega_Jueces.md`), sin saber el origen de
cada uno, usando la `Hoja_Puntuacion_JUEZ.csv`. El orden fue aleatorizado
con semilla fija (20260802) para reproducibilidad.

## Plan de análisis estadístico

1. Consolidar las hojas de puntuación de los ≥3 jueces.
2. Calcular acuerdo inter-evaluador: κ de Cohen por par de jueces, κ de
   Fleiss para el conjunto completo.
3. Prueba de normalidad Shapiro-Wilk sobre las puntuaciones de cada
   conjunto, por dimensión.
4. Si los datos son normales: prueba t para muestras apareadas
   (comparando la media de cada juez en Conjunto A vs. Conjunto B).
   Si no son normales: prueba de Wilcoxon.
5. Tamaño del efecto: Cohen d (si paramétrico) o Cliff δ (si no
   paramétrico).
6. Cálculo de potencia estadística previo (α = 0.05, potencia deseada
   1-β = 0.80).

## Amenazas a la validez (declaración obligatoria, ver también
`prompt_llm_conjunto_A.md`)

- **Validez de constructo:** el modelo usado para generar el Conjunto A
  tuvo exposición previa parcial al Conjunto B dentro de la misma
  cuenta de chat (ver limitación detallada en `prompt_llm_conjunto_A.md`).
- **Validez interna:** los jueces deben ser verificablemente
  independientes de las 11 entrevistas fuente; su selección debe
  documentarse.
- **Validez externa:** los resultados son específicos del dominio SIGA
  y de un modelo de LLM particular; no se generalizan automáticamente
  a otros dominios o modelos.
- **Validez de conclusión:** el tamaño de muestra (51 ítems, ≥3 jueces)
  es modesto; se recomienda ampliar jueces hacia la Entrega 4 (2B) si
  el tiempo lo permite.

## Registro previo

Este protocolo debe registrarse en OSF (https://osf.io) **antes** de
distribuir el paquete ciego a los jueces, conforme al gatekeeper G6 de
la guía. El equipo ya reportó tener el proyecto OSF creado pero sin
completar/registrar formalmente — completar antes de enviar el paquete.

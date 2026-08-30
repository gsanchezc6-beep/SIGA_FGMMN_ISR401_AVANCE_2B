# Rúbrica de evaluación — Comparación de calidad de RF (Enfoque 1)

Cada persona evaluadora puntúa **cada requisito de forma individual**,
sin saber si proviene del equipo humano o del LLM, en las siguientes
5 dimensiones, escala 1 (muy deficiente) a 5 (excelente).

## 1. Completitud
¿El requisito incluye toda la información necesaria para implementarlo
sin tener que adivinar detalles (actor, condición, resultado esperado)?

| Puntaje | Ancla |
|---|---|
| 1 | Falta información esencial; no se puede implementar sin preguntar de nuevo al cliente |
| 3 | Cubre lo esencial pero omite detalles secundarios (ej. formato exacto de salida) |
| 5 | Autocontenido: cualquier desarrollador podría implementarlo sin dudas |

## 2. Ausencia de ambigüedad
¿El texto admite una sola interpretación razonable?

| Puntaje | Ancla |
|---|---|
| 1 | Usa cuantificadores vagos ("rápido", "fácil") o admite varias lecturas contradictorias |
| 3 | Mayormente claro, con algún término que podría interpretarse de más de una forma |
| 5 | Una sola lectura posible; términos y umbrales precisos |

## 3. Verificabilidad
¿Existe una forma objetiva de comprobar que el requisito se cumplió?

| Puntaje | Ancla |
|---|---|
| 1 | No hay criterio de aceptación, o es subjetivo ("debe ser satisfactorio") |
| 3 | Hay criterio, pero requiere juicio humano para decidir si se cumplió |
| 5 | Criterio medible y objetivo (umbral numérico, prueba reproducible) |

## 4. Corrección respecto de la fuente
¿El requisito refleja fielmente lo que decían las transcripciones, sin
inventar ni contradecir lo que dijeron los participantes?

| Puntaje | Ancla |
|---|---|
| 1 | Contradice o no tiene respaldo alguno en el material fuente |
| 3 | Tiene respaldo parcial o requiere una interpretación forzada de la fuente |
| 5 | Trazable directamente a una afirmación concreta de una o más entrevistas |

## 5. Consistencia interna
¿El requisito no se contradice con otros requisitos del mismo conjunto?

| Puntaje | Ancla |
|---|---|
| 1 | Contradice abiertamente otro requisito del mismo conjunto |
| 3 | No contradice, pero se solapa parcialmente sin diferenciarse con claridad |
| 5 | Coherente y bien diferenciado de los demás requisitos del conjunto |

## Nota de acuerdo inter-evaluador

Cada persona evaluadora puntúa de forma independiente, sin consultar a
las demás. Una vez recogidas las 3 (o más) hojas de puntuación, se
calcula:
- **κ de Cohen** entre cada par de evaluadores.
- **κ de Fleiss** para el conjunto completo de evaluadores.

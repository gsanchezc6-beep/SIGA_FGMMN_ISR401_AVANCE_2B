# `figuras/` — Figuras del manuscrito

Carpeta obligatoria del árbol de la Sección 9.1. **Toda figura se genera por script**
desde `06_Experimento/datos_crudos/` mediante `make all`. Ninguna figura se pega desde
una hoja de cálculo (Secciones 4 y 5.5 de la guía).

## Figuras previstas

| # | Figura | RQ | Script que la genera |
|---|---|---|---|
| 1 | Curva de saturación temática — códigos nuevos acumulados por entrevista, con la inflexión marcada | Contexto | `curva_saturacion.py` |
| 2 | Distribución de puntuaciones por dimensión y por origen (Humano / LLM) — diagramas de caja con puntos individuales | RQ1 | `analizar_resultados.py` |
| 3 | Tamaños del efecto por dimensión (*d* de Cohen o δ de Cliff) con intervalos de confianza al 95 % por *bootstrap* | RQ1 | `analizar_resultados.py` |
| 4 | Acuerdo inter-evaluador — κ de Cohen por par de jueces y κ de Fleiss del conjunto | RQ1 | `analizar_resultados.py` |

## Requisitos de formato

- **Vectorial** (PDF o EPS) para el envío a revista; PNG a ≥ 300 dpi sólo como respaldo.
- Legibles **en escala de grises**: no codificar información únicamente por color.
- Tipografía de al menos 8 pt al tamaño final de impresión.
- Nombre del archivo = número de figura en el manuscrito: `fig01_curva_saturacion.pdf`.
- Cada figura referenciada por número en el texto y con pie de figura autocontenido.

## Regla de trazabilidad

Cada archivo de esta carpeta debe poder borrarse por completo y reaparecer idéntico tras
ejecutar `cd 06_Experimento && make all`. Si no reaparece, la figura no es reproducible y
activa el gatekeeper **G4**.

> **Criterios afectados:** C5 (peso 1,00), C6 (peso 0,50 — la curva de saturación es la
> Figura 1), C7 (peso 1,50).

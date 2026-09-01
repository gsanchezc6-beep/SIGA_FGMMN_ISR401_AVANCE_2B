# `tablas/` — Tablas del manuscrito

Carpeta obligatoria del árbol de la Sección 9.1. **Toda tabla se genera por script**
desde `06_Experimento/datos_crudos/` mediante `make all`, en formato `.tex` listo para
incluir con `\input{}` en el manuscrito. No se aceptan tablas producidas manualmente en
hoja de cálculo (Sección 4 de la guía).

## Tablas previstas

| # | Tabla | RQ | Contenido mínimo obligatorio |
|---|---|---|---|
| 1 | Caracterización de los participantes | Contexto | Perfil, código, técnica aplicada, duración — **sin datos identificables** |
| 2 | Cuadro comparativo del trabajo relacionado | — | Referencia, Año, Tipo de estudio, Población, Intervención, Resultados principales, Diferencia con nuestro trabajo (10 a 15 trabajos) |
| 3 | Estadísticos descriptivos por dimensión y origen | RQ1 | Mediana, media, desviación estándar, mínimo, máximo, intervalo intercuartílico |
| 4 | Pruebas de supuestos | RQ1 | Shapiro-Wilk y Levene, con estadístico y valor *p* |
| 5 | Pruebas de hipótesis por dimensión | RQ1 | Nombre exacto de la prueba, estadístico (*t*, *U*, χ²), grados de libertad, valor *p* con ≥ 3 decimales, *p* ajustado por Holm-Bonferroni, tamaño del efecto e IC 95 % |
| 6 | Acuerdo inter-evaluador | RQ1 | κ de Cohen por par, κ de Fleiss del conjunto, con interpretación |

## Requisitos de reporte (Secciones 4.4 y 5.5 de la guía)

- Valor *p* con **al menos tres decimales**; nunca «p < 0,05» sin el valor exacto.
- **Siempre** tamaño del efecto e intervalo de confianza al 95 % junto al valor *p*.
- Corrección de **Holm-Bonferroni** declarada cuando hay comparaciones múltiples (aquí:
  cinco dimensiones ⇒ es obligatoria).
- Sin cifras redondeadas «a criterio»: el redondeo lo aplica el script, de forma uniforme.

> **Criterios afectados:** C5 (peso 1,00), C7 (peso 1,50).

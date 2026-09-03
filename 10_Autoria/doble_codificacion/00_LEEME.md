# A7 — Doble codificacion del corpus

Lo que exige la guia:

- **Dos hojas de codificacion** producidas por **dos integrantes distintos** sobre el
  **mismo subconjunto** del corpus.
- El **coeficiente de acuerdo** entre ambas, con su **intervalo de confianza**, generado
  por script.

## Por que faltaba, y por que ahora es posible

`07_Publicacion/dataset_zenodo/anonimizacion.md` declara que el procedimiento previsto era
una doble revision ciega por dos personas distintas del equipo, y que **se sustituyo por dos
pasadas independientes de la misma persona separadas en el tiempo**, porque el equipo se
habia reducido a dos integrantes y una de ellas hizo toda la codificacion.

Con la reincorporacion del 2026-09-02 vuelven a existir dos personas disponibles, de modo
que el procedimiento original es aplicable. Cuando se deposite esta evidencia, hay que
actualizar tambien esa declaracion para que deje de describir la solucion de compromiso.

## Como hacerlo

1. Elegir un subconjunto del corpus. Con tres o cuatro transcripciones completas basta,
   siempre que sean las mismas para ambas personas.
2. Cada integrante codifica **por separado y sin consultar** la del otro, usando el mismo
   libro de codigos, que esta en `02_Evidencias/Codificacion_Tematica/`.
3. Depositar las dos hojas sin retocarlas, con el nombre de quien las produjo.
4. Calcular el acuerdo con intervalo. El script de
   `07_Datos/scripts/etapa2_acuerdo_ic.py` ya implementa kappa de Cohen ponderado y su
   intervalo por bootstrap, y se puede reutilizar cambiando la entrada.

## Nombres de archivo

```
codificacion_<usuario_git>.csv
acuerdo_doble_codificacion.csv
```

# Guion de reparto de la exposicion — Defensa individual

Proyecto SIGA · ISR-401 · Equipo FGMMN · Universidad Tecnica Estatal de Quevedo
Version 2.0 · 2026-08-29

---

## Modalidad

La defensa de esta entrega es **individual**: cada integrante expone el proyecto
**completo** ante el tribunal, no una parte asignada. Por eso este guion no reparte
bloques entre personas: reparte **el tiempo dentro de una misma exposicion**, y esa misma
estructura la recorre cada integrante en su turno.

El criterio de piso **D0** es explicito: quien no rinde la defensa obtiene cero en el
criterio de defensa y su factor de ajuste individual queda limitado a 0,85 como maximo.
No hay forma de compensarlo con el trabajo del repositorio.

Y el criterio **C7** en su nivel maximo exige que **cada integrante domine el proyecto
completo**, no solo su parte. Con defensa individual eso deja de ser una recomendacion:
es la condicion de la nota.

---

## Estructura de la exposicion

La secuencia sigue el orden del reporte, que es lo que la guia pide como
«correspondencia con los artefactos entregados». Los tiempos son proporciones sobre el
total que fije el tribunal; la columna de minutos supone una exposicion de 20 minutos y se
reescala si el tiempo real es otro.

| # | Bloque | Proporcion | Min. (sobre 20) | Diapositivas | Artefacto que lo respalda |
|---|---|---|---|---|---|
| 1 | Problema, contexto y organizacion cliente | 10 % | 2 | 2–3 | Documentos de la organizacion; notas de campo |
| 2 | Pregunta de investigacion y brecha | 10 % | 2 | 2 | Protocolo registrado; cuadro de trabajo relacionado |
| 3 | El sistema y sus partes interesadas | 10 % | 2 | 2 | Diagrama de contexto; modelo iStar |
| 4 | Metodologia del componente empirico | 15 % | 3 | 3 | Protocolo; instrumentos; consignas del modelo |
| 5 | Resultados | 25 % | 5 | 4–5 | Tablas y figuras de `07_Datos/`, generadas por script |
| 6 | Amenazas a la validez y limitaciones | 15 % | 3 | 2–3 | Bitacora de desviaciones; auditoria de calidad |
| 7 | Especificacion final, trazabilidad y prototipo | 10 % | 2 | 2 | ERS v2.0; matriz; demostracion del prototipo |
| 8 | Conclusiones | 5 % | 1 | 1 | Reporte, seccion de conclusiones |
| | **Total** | **100 %** | **20** | **18–21** | |

Con esta estructura la presentacion queda en **18 a 21 diapositivas**, dentro del rango de
15 a 20 que exige la guia si se consolidan los bloques 7 y 8.

---

## Lo que el tribunal evalua en cada bloque

| Bloque | Lo que buscan | Como se demuestra |
|---|---|---|
| 1–3 | Que el sistema es real y el cliente identificable | Nombrar la facultad, los tres perfiles y citar una frase de entrevista |
| 4 | Que las decisiones se tomaron **antes** de ver los datos | Senalar el protocolo registrado y su fecha |
| 5 | Que ninguna cifra se escribio a mano | Explicar que `make all` regenera cada tabla y cada figura desde los datos crudos |
| 6 | Criterio tecnico para reconocer los limites | Declarar la potencia del 8,4 % y la saturacion no alcanzada, sin adornarlas |
| 7 | Que el prototipo corresponde a lo especificado | Cobertura del 85 % de los requisitos obligatorios, verificable en el codigo |
| 8 | Que cada conclusion remite a un dato | Cada afirmacion senala su tabla o su figura |

---

## Las tres cosas que hay que decir sin que las pregunten

La guia premia en C7 que **se reconozcan las limitaciones con criterio tecnico**. Estas
tres se declaran de frente en el bloque 6, antes de que el tribunal las encuentre:

1. **La potencia estadistica es del 8,4 %.** Para detectar el efecto que el estudio buscaba
   harian falta 34 unidades y hay 3. Ningun resultado sobrevive a la correccion por
   comparaciones multiples, y eso se reporta como tal.
2. **La saturacion tematica no se alcanzo.** La ultima entrevista todavia aporta cuatro
   codigos nuevos sobre 36. No se presenta como saturacion lograda.
3. **La unidad de analisis es el juez, no el item.** Con tres jueces, los grados de
   libertad son dos, y de ahi salen intervalos de confianza muy anchos. Es una decision
   que el equipo reconoce como mejorable y sabe explicar por que.

Decir esto primero cambia la conversacion: el tribunal deja de buscar el error y pasa a
evaluar el criterio.

---

## Preparacion individual

Cada integrante, antes de su turno:

- [ ] Recorre la presentacion completa con cronometro, al menos dos veces.
- [ ] Abre y revisa **cada artefacto** que va a mencionar. No mencionar nada sin haberlo
      abierto.
- [ ] Ejecuta `make all` una vez y ve las tablas regenerarse. Es la respuesta a la pregunta
      mas probable sobre reproducibilidad.
- [ ] Levanta el prototipo y recorre dos escenarios de la matriz de trazabilidad.
- [ ] Repasa el banco de preguntas, en especial las que no corresponden a su rol.

**Lo que hunde una defensa individual no es no saber un dato: es no saber donde esta.**
Cada respuesta del banco senala su artefacto por esa razon.

---

## Demostracion del prototipo

Se ejecuta en local segun `05_MVP/despliegue/instrucciones_despliegue.md`, con las cuentas
de demostracion documentadas. **Nunca con credenciales reales de personas del cliente.**

Se preparan de antemano **dos escenarios** trazados en la matriz, y se ensayan hasta que
salgan sin dudar. Si la demostracion falla en vivo, se continua con el video de
`05_MVP/demostracion/`, que corresponde a la misma version entregada.

---

## Historial de versiones

| Version | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-08-26 | Guion de reparto por bloques entre cinco integrantes, para exposicion conjunta de 25 minutos |
| **2.0** | **2026-08-29** | Reescrito para **defensa individual**: cada integrante expone el proyecto completo. Se reordena la secuencia segun la estructura del reporte, se anaden la correspondencia con artefactos y la lista de preparacion individual, y se retiran las referencias a criterios de la guia anterior. |

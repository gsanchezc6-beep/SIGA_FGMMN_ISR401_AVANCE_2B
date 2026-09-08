# Respaldo de campo del requisito de explicabilidad

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

---

## 1. Que responde este documento

`requisitos_no_funcionales_ia.csv` declara el estado de verificacion de **RNF-IA-03**
como *parcialmente sustentado*: los umbrales de longitud y latencia proceden de
`RNF-10`, pero **el de comprension no tenia origen de campo declarado**.

El cuestionario aplicado a 60 personas si pregunta por explicabilidad, en dos items, y
esas respuestas no se habian explotado. Aqui se cuentan. **Ninguna cifra se teclea**:
todas salen de `evidencia_explicabilidad.py` sobre el export de respuestas.

## 2. Cuanto importa que el sistema explique

> «¿Que tan importante es que el sistema te explique por que predijo una falla?»
> Escala de 1 a 5. **n = 59** respuestas validas de 60.

| Respuesta | n | % |
|---|---|---|
| 5 | 18 | 30.5 |
| 4 | 9 | 15.3 |
| 3 | 15 | 25.4 |
| 2 | 10 | 16.9 |
| 1 | 7 | 11.9 |

**Media 3.36**, intervalo de confianza al 95 % de **3.00 a 3.69** (bootstrap de 10000 remuestreos, semilla 20260908).

El intervalo **no contiene el 4**, de modo que la importancia media no llega a
«importante» en la escala del propio instrumento. Se declara asi y no se redondea
al alza: la explicabilidad importa, pero no es la exigencia dominante de esta
poblacion.

## 3. Que tipo de explicacion se prefiere

| Preferencia | n | % |
|---|---|---|
| Un detalle técnico | 22 | 37.3 |
| Una frase simple | 16 | 27.1 |
| Un ejemplo de un caso anterior | 13 | 22.0 |
| Ninguna, solo la alerta | 8 | 13.6 |

**51 de 59 (86.4 %) quieren alguna explicacion** y 8 (13.6 %) prefieren solo la
alerta. Pero **la forma preferida se reparte en tres**, sin mayoria: el detalle
tecnico encabeza sin llegar al 40 %.

## 4. Que se concluye para RNF-IA-03, y que no

**Lo que sostiene.** Que la explicacion debe existir: solo una de cada siete personas
la rechaza. El requisito de acompanar toda prediccion con una explicacion tiene
respaldo de campo.

**Lo que no sostiene.** El umbral de **comprension >= 80 %** sigue sin origen de
campo. El instrumento pregunto por importancia y por preferencia de formato, **no
midio comprension**. Que el 86 % quiera una explicacion no dice que el 80 % la vaya
a entender: son cosas distintas y no se presentan como la misma.

**Lo que abre.** Que no haya forma preferida mayoritaria es un hallazgo con
consecuencia de diseno: una explicacion unica no sirve a los tres grupos. Queda
declarado como trabajo futuro y no como requisito, porque el instrumento no
pregunto por perfil y no se puede saber si la preferencia depende de el.

## 5. Como se reproduce

```
python 01_ERS/Componentes_IA/evidencia_explicabilidad.py
```

Lee `02_Evidencias/Cuestionario/Respuestas/respuestas_cuestionario_n60.csv`, que es
el export del formulario, y escribe este documento y `evidencia_explicabilidad.csv`.

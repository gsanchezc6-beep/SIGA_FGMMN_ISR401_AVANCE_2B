# Catalogo de casos de prueba

**Proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ** — creado el 2026-09-03

---

## El problema que resuelve

La matriz de trazabilidad declaraba, para cada requisito, el caso de prueba que lo verifica:
`CP-RF-01`, `CP-RNF-07`, y asi hasta cuarenta y nueve identificadores.

**Ninguno de esos identificadores correspondia a nada.** No habia catalogo de casos de
prueba, ni en el ERS, ni en `05_MVP`, ni en ninguna otra carpeta. La columna enlazaba con el
vacio, y una cadena de trazabilidad que termina en un identificador inexistente no esta
cerrada: lo parece.

Este catalogo los define. `casos_prueba.csv` contiene los cuarenta y nueve, cada uno con su
objetivo, precondicion, procedimiento, resultado esperado, criterio de aceptacion, elemento
de diseno y caso de uso.

## Como se regenera

```
python 04_Trazabilidad/generar_casos_prueba.py
```

El script **falla** si la correspondencia con la matriz se rompe en cualquiera de los dos
sentidos: si la matriz cita un caso que aqui no existe, o si aqui se define uno que la matriz
no cita. Esa comprobacion es el motivo de que el catalogo se genere y no se escriba a mano.

## De donde sale cada campo

| Campo | Procedencia |
|---|---|
| Objetivo y resultado esperado | Del enunciado del requisito en la matriz, que es donde vive su umbral |
| Criterio de aceptacion | De la columna `ID-CA` de la matriz. Los criterios estan escritos en Gherkin en el ERS |
| Elemento de diseno y caso de uso | De las columnas correspondientes de la matriz |
| Procedimiento | Del tipo de requisito. No hay plantilla unica: un requisito funcional se prueba ejecutandolo, uno con umbral se mide, y una restriccion de diseno se comprueba mirando el diseno |
| Metodo de los ocho casos del componente inteligente | Literal de `01_ERS/Componentes_IA/requisitos_no_funcionales_ia.csv`, que ya lo especificaba |
| `Ejecutable_hoy` | De `05_MVP/cobertura_requisitos.csv`. No se supone: se lee |

## Que contiene

| Tipo de prueba | Casos |
|---|---|
| Funcional | 25 |
| No funcional, medicion contra umbral | 16 |
| Medicion contra umbral, componente inteligente | 8 |
| **Total** | **49** |

**18 son ejecutables hoy** sobre el prototipo, porque el MVP implementa el requisito
correspondiente. Los otros 31 exigen un sistema desplegado o una medicion en operacion.

## Lo que este catalogo NO afirma

**No dice que ninguna prueba se haya ejecutado.** Todas constan como *especificado, no
ejecutado*, salvo los ocho del componente inteligente, que llevan el estado de verificacion
que ya declaraba su ficha.

La distincion importa. Un catalogo de casos de prueba es parte de la especificacion: dice
como se comprobaria cada requisito. Presentarlo como si fuera un informe de ejecucion seria
afirmar resultados que no existen.

## Los casos funcionales y su nivel de detalle

Los veinticinco casos funcionales comparten la estructura del procedimiento, y conviene
decirlo antes de que se note: lo que varia entre ellos es el requisito que prueban, el
elemento de diseno sobre el que se ejecuta y el criterio Gherkin que decide si pasan. El
paso concreto de cada escenario ya esta escrito en ese criterio, en el ERS, y duplicarlo aqui
solo crearia dos versiones del mismo escenario que acabarian divergiendo.

Los dieciseis no funcionales y los ocho del componente inteligente si llevan procedimiento
propio, porque medir contra un umbral exige decir cuantas mediciones, con que estadistico y
con que intervalo.

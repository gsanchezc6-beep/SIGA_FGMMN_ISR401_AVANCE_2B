# Autoevaluacion FAIR del paquete de datos

**Proyecto SIGA --- Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

---

## 1. De donde sale este documento

**No esta redactado a mano.** Lo genera `generar_fair_assessment.py` a partir de
`fair_assessment.json`, que es el volcado literal que devuelve **F-UJI**, el
servicio de evaluacion FAIR del proyecto FAIRsFAIR. Ninguna cifra de las que
siguen se tecleo: todas se leen del JSON.

| | |
|---|---|
| Objeto evaluado | `https://doi.org/10.5281/zenodo.21774350` |
| Identificador de la prueba | `798a865fc300c85591e150e884b0ba3b40b87ec0` |
| Version de F-UJI | 4.0.0 |
| Especificacion de metricas | https://doi.org/10.5281/zenodo.15045911 |
| Version de metricas | 0.8 |

El identificador de prueba permite recuperar esta misma evaluacion en el
servicio. La version de software y la de metricas constan porque un resultado
FAIR no significa nada sin decir contra que rubrica se midio.

## 2. Resultado

**22 de 26 indicadores --- 84.62 %**

| Principio | Obtenido | Posible | Porcentaje | Nivel |
|---|---|---|---|---|
| Findable --- localizable | 7 | 7 | 100.00 % | 3 |
| Accessible --- accesible | 6 | 7 | 85.71 % | 2 |
| Interoperable --- interoperable | 4 | 6 | 66.67 % | 2 |
| Reusable --- reutilizable | 5 | 6 | 83.33 % | 2 |
| **Conjunto** | **22** | **26** | **84.62 %** | **2.25** |

## 3. Lo que no puntua, y por que

Son **3** de los 17 indicadores. Se listan enteros, con lo que el propio
servicio informa, en vez de resumir solo los que favorecen:

| Indicador | Obtenido | Posible | Que mide |
|---|---|---|---|
| `FsF-A1-01M` | 0 | 1 | Metadata contains access level and access conditions of the data. |
| `FsF-I2-01M` | 0 | 2 | Metadata uses registered semantic resources |
| `FsF-R1-01M` | 1 | 2 | Metadata specifies the content of the data. |

**`FsF-A1-01M` --- Metadata contains access level and access conditions of the data..** 

**`FsF-I2-01M` --- Metadata uses registered semantic resources.** 

**`FsF-R1-01M` --- Metadata specifies the content of the data..** Nivel alcanzado: 1. 

- `object_type`: ['Dataset', 'http://schema.org/WebPage']

- `data_content_descriptor`: [{'descriptor': 'file type', 'descriptor_value': 'text/csv', 'matches_content': False}, {'descriptor': 'file type', 'descriptor_value': 'text/markdown', 'matches_content': False}, {'descriptor': 'file type', 'descriptor_

## 4. Como se reproduce

```
1. Abrir https://www.f-uji.net
2. Introducir https://doi.org/10.5281/zenodo.21774350
3. Metrica: https://doi.org/10.5281/zenodo.15045911
4. Descargar el resultado con el boton {JSON} y guardarlo como
   fair_assessment.json en la raiz de este repositorio
5. python generar_fair_assessment.py
```

El servicio esta en desarrollo y su propio aviso lo dice, de modo que una
evaluacion futura puede diferir. Por eso se deposita el JSON completo junto
a este informe: lo que aqui se afirma es comprobable contra el volcado, y el
volcado contra el servicio.

# Análisis de revistas objetivo — Proyecto SIGA

Documento exigido por la Sección 7.11 de la Guía de Entrega 3 (2A): selección de
revista objetivo comparando **al menos una alternativa de acceso abierto con APC**
y **una alternativa por suscripción o híbrida sin cargo obligatorio**, ambas
indexadas en el *Journal Citation Reports* (JCR) de Clarivate.

Área temática del manuscrito: Ingeniería de Requerimientos, con componente empírico
sobre elicitación asistida por modelos de lenguaje grande (LLM) y explicabilidad
como requisito no funcional.

---

## 1. Candidatas evaluadas

| # | Revista | Editorial | Modalidad | APC | Indexación |
|---|---|---|---|---|---|
| 1 | **Requirements Engineering** | Springer Nature | Híbrida | Opcional (solo si se elige la vía OA) | JCR — Q2 aprox. en Software Engineering |
| 2 | **Information and Software Technology** | Elsevier | Híbrida | **USD 3 350** si se elige OA | JCR — Q1, factor de impacto 4.6 |
| 3 | **IEEE Access** | IEEE | Acceso abierto completo | **USD 2 160** obligatorio | JCR — Q1/Q2 multidisciplinar |
| 4 | **Empirical Software Engineering** | Springer Nature | Híbrida | Opcional | JCR — Q1 |

> Los montos de APC fueron verificados en agosto de 2026 en las fuentes oficiales
> citadas al final. **Deben reconfirmarse antes del envío**, ya que las editoriales
> los actualizan anualmente.

---

## 2. Alternativa de acceso abierto con APC

### IEEE Access

- **Modalidad:** *gold open access* completo. Todo artículo aceptado se publica en
  abierto y paga APC; no existe vía sin cargo.
- **APC:** USD 2 160 por artículo, más impuestos locales aplicables. Sin límite de
  páginas, lo que evita cargos adicionales por extensión.
- **Descuentos:** los miembros de IEEE y de sociedades técnicas acceden a tarifas
  reducidas.
- **Ventajas para SIGA:** alcance multidisciplinar (admite trabajos que cruzan
  ingeniería de requerimientos con IoT e IA), tiempos de revisión cortos
  (habitualmente 4 a 6 semanas hasta la primera decisión) y visibilidad inmediata
  del conjunto de datos depositado en Zenodo.
- **Desventajas:** el APC es obligatorio y elevado para un equipo estudiantil sin
  financiamiento institucional; su carácter multidisciplinar hace que el artículo
  no quede en el nicho específico de la comunidad de requerimientos.

---

## 3. Alternativa por suscripción o híbrida sin cargo obligatorio

### Requirements Engineering (Springer Nature)

- **Modalidad:** híbrida. Se puede publicar **sin pagar APC** por la vía de
  suscripción; el pago solo aplica si el autor elige voluntariamente la opción de
  acceso abierto.
- **Ajuste temático:** es la revista de referencia específica del área. Su alcance
  declarado cubre elicitación, representación y validación de requisitos de sistemas
  intensivos en software, que es exactamente el objeto de este trabajo.
- **Ventajas para SIGA:** costo cero en la vía de suscripción, audiencia
  especializada, y encaje directo del componente empírico (comparación de calidad de
  requisitos humanos frente a generados por LLM).
- **Desventajas:** proceso de revisión más largo y exigente; el artículo queda tras
  muro de pago salvo que se autoarchive la versión aceptada en un repositorio
  institucional (vía verde).

---

## 4. Decision y justificacion

**Objetivo primario: REFSQ 2027 --- _Requirements Engineering: Foundation for Software
Quality_, Basel, Suiza, 12 a 15 de abril de 2027, track Research.**

Razones:

1. **Coherencia con lo que ya esta escrito.** El manuscrito esta redactado en la plantilla
   oficial `llncs.cls` de Springer LNCS, que es exactamente la que REFSQ exige. La extension
   del track Research es de 15 paginas incluidas las referencias, y el manuscrito ocupa
   **12**, de modo que cumple sin recortes.
2. **Viabilidad economica.** El envio a REFSQ no exige cargo por procesamiento de articulo.
   El equipo no dispone de financiamiento para un APC de entre USD 2 160 y 3 350, y esa
   restriccion es real, no retorica.
3. **Encaje tematico exacto.** REFSQ es la conferencia especializada en fundamentos de
   ingenieria de requisitos; la comparacion entre elicitacion humana y asistida por modelos
   de lenguaje cae en su nucleo tematico.
4. **Calendario compatible con el ciclo academico.** El track Research abre con envio de
   resumen el 5 de noviembre de 2026 y de articulo el 12 de noviembre de 2026, dentro del
   semestre, con notificacion el 14 de enero de 2027.

**Segunda opcion, mas accesible: REFSQ 2027 --- track _Research Previews_**, con envio el 12
de noviembre de 2026 y extension de 8 paginas. Requiere condensar el manuscrito en cuatro
paginas, lo que es factible reduciendo el trabajo relacionado y fusionando las subsecciones
de discusion. Se mantiene como alternativa si el comite recomienda un formato mas breve.

**Tercera opcion, de mayor recorrido: el journal _Requirements Engineering_ (Springer
Nature), via de suscripcion sin cargo obligatorio.** Exigiria migrar el manuscrito a la
plantilla `sn-jnl.cls` y ampliarlo a la extension propia de un articulo de revista. Es la
via natural si el trabajo se amplia despues del cierre del semestre, y es la que la guia
senala para los equipos que escalen su envio.

**Nota sobre la eleccion.** La guia exige que la eleccion se registre por correo
institucional al docente responsable antes del inicio de la semana 14. Este documento fija
la eleccion del equipo; **la constancia del correo debe adjuntarse cuando se disponga de
ella**, y hasta entonces esa formalidad queda declarada como pendiente en lugar de darse
por cumplida.

---

## 5. Disponibilidad de datos

El conjunto de datos anonimizado que acompaña al manuscrito está depositado en
Zenodo con licencia Creative Commons Atribución 4.0 Internacional (CC BY 4.0):

**DOI:** https://doi.org/10.5281/zenodo.22137679

El registro previo del protocolo experimental se encuentra en OSF. Se cita el
**registro**, que es inmutable y tiene DOI, y no el nodo de proyecto del que cuelga:

**OSF:** https://doi.org/10.17605/OSF.IO/7PQ3H — https://osf.io/7pq3h

---

## 6. Fuentes consultadas

- [IEEE Access — Article Processing Charges](https://ieeeaccess.ieee.org/about/article-processing-charges/)
- [2026 IEEE Publications Article Processing Charge (APC) List](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE-Article-Processing-Charges-List.pdf)
- [Information and Software Technology — ScienceDirect](https://www.sciencedirect.com/journal/information-and-software-technology)
- [Elsevier — Journal pricing policy](https://www.elsevier.com/about/policies-and-standards/pricing)
- [Requirements Engineering — Springer Nature Link](https://link.springer.com/journal/766)
- [Springer Nature — Open access article processing charges](https://stories.springernature.com/apcguide/index.html)

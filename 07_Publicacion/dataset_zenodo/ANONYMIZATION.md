# Procedimiento de seudonimización y anonimización

**Paquete de replicación SIGA — Sistema Inteligente de Gestión de Aulas**
Equipo FGMMN · Universidad Técnica Estatal de Quevedo (UTEQ) · ISR-401 · 2026

Documento exigido por la Sección 7.2 de la Guía de Entrega 4 (2B). Describe el
procedimiento aplicado a todos los materiales antes de su depósito público en Zenodo,
en cumplimiento de los principios de **minimización** y **seudonimización** de la Ley
Orgánica de Protección de Datos Personales del Ecuador (Registro Oficial Suplemento
459, 26 de mayo de 2021) y de las guías de investigación cualitativa reproducible.

---

## 1. Principio rector

> El paquete público de Zenodo contiene **exclusivamente material seudonimizado o
> anonimizado**. Ningún archivo que permita la reidentificación directa de una persona
> participante sale del repositorio privado de evidencia.

Los materiales que **nunca** se publican son:

| Material | Motivo | Dónde permanece |
|---|---|---|
| Consentimientos informados firmados | Firma manuscrita y número de cédula | `02_Evidencias/Consentimientos/` (acceso restringido) |
| Videos de entrevista | Rostro y voz identificables | `02_Evidencias/Video/` (acceso restringido) |
| Audios de entrevista | Voz identificable (biométrico) | `02_Evidencias/Audio/` (acceso restringido) |
| Fotografías con personas identificables | Imagen personal | `02_Evidencias/Fotos_Entorno/` (acceso restringido) |
| Clave de origen del paquete ciego | Rompe el diseño ciego del experimento | `06_Experimento/` (acceso restringido) |

Lo que **sí** se publica son las **transcripciones seudonimizadas**, la codificación
temática, las respuestas del cuestionario, el corpus etiquetado de RF/RNF, la matriz
de trazabilidad, los prompts y salidas del LLM, y los scripts de análisis.

---

## 2. Esquema de seudónimos

Cada participante recibe un identificador estable compuesto por **perfil + número
correlativo**, asignado en orden cronológico de primera participación:

| Perfil | Prefijo | Descripción |
|---|---|---|
| Docencia | `DOC-nn` | Personal docente que imparte clases en las aulas del estudio |
| Coordinación académica | `COORD-nn` | Personal de coordinación y gestión académica |
| Conserjería e infraestructura | `CONS-nn` | Personal de conserjería, mantenimiento e infraestructura |
| Estudiantes | `EST-nn` | Estudiantes voluntarios de 4.º–5.º nivel, habilitados como sujetos de entrevista por el Anexo CB5 (Política de manejo de datos de menores — Declaración de no aplicabilidad), que ya declara a los "estudiantes voluntarios de cuarto y quinto nivel" como parte de la población participante |

Ejemplos: `DOC-01`, `COORD-03`, `CONS-04`, `EST-01`.

**Propiedades del esquema:**

1. **Estable.** El mismo seudónimo identifica a la misma persona en todos los
   artefactos: transcripciones, codificación temática, matriz de trazabilidad, actas
   de walkthrough, acta de *member checking* y manuscrito.
2. **No reversible públicamente.** La tabla de correspondencia entre seudónimo y
   persona real **no forma parte del paquete Zenodo**. Se conserva en un único
   archivo cifrado bajo custodia del docente responsable y del analista líder.
3. **Sin información semántica.** El seudónimo no codifica edad, sexo, antigüedad,
   departamento ni ningún otro atributo que permita inferir la identidad.

Los identificadores de evidencia (`EV-nn`) y de sesión de validación (`WT-nn`,
`MC-nn`) son independientes del seudónimo de persona y se mantienen para trazabilidad
interna.

---

## 3. Reglas de transformación aplicadas a las transcripciones

Cada transcripción publicada se somete a las siguientes sustituciones, en este orden:

| # | Elemento detectado | Sustitución |
|---|---|---|
| 1 | Nombre propio y apellido de la persona entrevistada | Su seudónimo (`DOC-01`, …) |
| 2 | Nombre propio de terceras personas mencionadas | `[PERSONA-A]`, `[PERSONA-B]`, … dentro de la misma transcripción |
| 3 | Número de cédula, pasaporte o identificación | `[IDENTIFICACION]` |
| 4 | Número de teléfono | `[TELEFONO]` |
| 5 | Correo electrónico | `[CORREO]` |
| 6 | Dirección domiciliaria | `[DIRECCION]` |
| 7 | Cargo administrativo único e identificable por sí solo (p. ej. el único titular de un puesto) | `[CARGO-ADMINISTRATIVO]` |
| 8 | Código de aula o edificio que permita ubicar a una persona en un horario concreto | `[AULA-nn]` con numeración interna del estudio |
| 9 | Fechas exactas de eventos personales | Se reducen a mes y año |
| 10 | Menciones a terceras organizaciones no participantes | `[ORGANIZACION]` |

**Lo que NO se altera**, por ser esencial para la validez del análisis:

- El contenido semántico de las declaraciones sobre el sistema, los procesos y las
  necesidades operativas.
- El perfil del participante (docencia / coordinación / conserjería), que constituye
  la variable de estrato del estudio.
- La secuencia y estructura del diálogo, incluidas pausas y aclaraciones relevantes.
- La fecha de la entrevista a nivel de día, necesaria para reconstruir la curva de
  saturación en orden cronológico.

---

## 4. Tratamiento de los datos del cuestionario

1. Se elimina toda columna de identificación directa generada por el formulario:
   dirección de correo, nombre, dirección IP y cualquier identificador de sesión.
2. La marca temporal se **conserva**, porque el orden de respuesta es necesario para
   verificar la independencia de las observaciones; se trunca a fecha y hora sin
   segundos.
3. Cada respuesta recibe un identificador correlativo `RESP-nnn`, sin relación con el
   seudónimo de entrevista, para impedir el cruce entre ambos instrumentos.
4. Las respuestas en texto libre pasan por las mismas reglas de sustitución de la
   Sección 3.
5. Las variables demográficas se publican **agregadas por categoría**, nunca como
   valores exactos que puedan singularizar a una persona (por ejemplo, rangos de
   antigüedad en lugar de años exactos).

---

## 5. Riesgo de reidentificación y su mitigación

La población del estudio es pequeña y está circunscrita a una facultad, lo que eleva
el riesgo de reidentificación por inferencia contextual. Mitigaciones aplicadas:

| Riesgo | Mitigación |
|---|---|
| Un cargo único identifica a la persona | Sustitución por `[CARGO-ADMINISTRATIVO]` (regla 7) |
| La combinación perfil + aula + horario singulariza a un docente | Codificación interna de aulas y supresión de horarios exactos (reglas 8 y 9) |
| Una anécdota narrada es reconocible dentro de la facultad | Reformulación del pasaje conservando el contenido de requisitos y suprimiendo el detalle circunstancial; el pasaje reformulado se marca con `[…]` |
| El cruce entre cuestionario y entrevista revela identidad | Espacios de identificadores disjuntos (`RESP-nnn` vs. `DOC-nn`), sin tabla de correspondencia publicada |
| El grupo de conserjería es numéricamente reducido | Las citas de este perfil se publican sin marca temporal fina y se revisan una a una antes de la publicación |

---

## 6. Procedimiento de verificación antes del depósito

Ejecutado sobre **la totalidad** de los archivos del paquete. El diseño original preveía
doble revisión ciega por dos personas distintas del equipo; con el equipo operando en la
práctica como analista único para el cierre de esta entrega, la doble revisión se
sustituye por **dos pasadas independientes de la misma persona, separadas en el tiempo**
(idealmente un día de diferencia, para reducir el sesgo de haber revisado el mismo texto
recientemente), documentadas por separado en el registro de control de la Sección 7.

1. **Búsqueda automática** de patrones sensibles sobre todo el árbol
   `dataset_zenodo/`:

   ```bash
   # Nombres propios del equipo y de participantes conocidos
   grep -rniE "nombre1|nombre2|apellido1|apellido2" .

   # Cedulas ecuatorianas (10 digitos) y telefonos (09 + 8 digitos)
   grep -rnE "\b[0-9]{10}\b" .
   grep -rnE "\b09[0-9]{8}\b" .

   # Correos electronicos
   grep -rnE "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}" .
   ```

2. **Revisión manual** completa de cada transcripción por una persona distinta de
   quien la transcribió.
3. **Verificación de metadatos incrustados**: se eliminan autor, comentarios y
   propiedades de todo PDF, DOCX, XLSX e imagen que llegue al paquete.

   ```bash
   exiftool -all= -overwrite_original *.pdf *.png *.jpg
   ```

4. **Verificación de consistencia de seudónimos** entre transcripciones, codificación
   temática y matriz de trazabilidad: cada `DOC-nn`, `COORD-nn` y `CONS-nn` citado en
   un artefacto debe existir en los demás.
5. **Acta de verificación** firmada por las dos personas revisoras, archivada junto al
   paquete.

> El paquete no se sube a Zenodo hasta que los cinco pasos estén completos y el acta
> firmada.

---

## 7. Registro de control

| Verificación | Responsable | Fecha | Resultado |
|---|---|---|---|
| Búsqueda automática de patrones sensibles | PENDIENTE | PENDIENTE | PENDIENTE |
| Revisión manual de transcripciones | PENDIENTE | PENDIENTE | PENDIENTE |
| Limpieza de metadatos incrustados | PENDIENTE | PENDIENTE | PENDIENTE |
| Consistencia de seudónimos | PENDIENTE | PENDIENTE | PENDIENTE |
| Acta de verificación firmada | PENDIENTE | PENDIENTE | PENDIENTE |

---

## 8. Contacto

Consultas sobre el procedimiento de anonimización o solicitudes de rectificación,
eliminación u oposición al tratamiento de datos, conforme a los derechos reconocidos
por la Ley Orgánica de Protección de Datos Personales del Ecuador:

**Ing. Gleiston Guerrero Ulloa** — docente responsable
Facultad de Ciencias de la Computación, Universidad Técnica Estatal de Quevedo
Correo institucional: `PENDIENTE-COMPLETAR`

Ver también [`ETHICS.md`](ETHICS.md).

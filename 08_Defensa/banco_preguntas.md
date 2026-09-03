# Banco de preguntas del tribunal

Proyecto SIGA · ISR-401 · Equipo FGMMN · Universidad Tecnica Estatal de Quevedo
Version 1.0 · 2026-08-29

Una respuesta por pregunta del temario. **Cada respuesta senala el artefacto que la
respalda**, porque la guia evalua que las respuestas se anclen en artefactos concretos y no
en opiniones.

---

## A. Sistema, dominio y partes interesadas

**A1. ¿Que problema real resuelve SIGA y para quien?**
Gestion de aulas en la Facultad de Ciencias de la Computacion de la UTEQ: hoy la deteccion
de un aire acondicionado danado o un proyector sin senal depende de que alguien pase por el
aula y avise. SIGA monitorea, alerta y gestiona el ticket.
→ `02_Evidencias/Transcripciones/`, EV-01 (CONS-01); `02_Evidencias/Documentos_Organizacion/`

**A2. ¿Como saben que el problema existe y no lo supusieron?**
De diez entrevistas con tres perfiles distintos, codificadas en 36 fragmentos con su
categoria y el requisito que derivan.
→ `02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv`

**A3. ¿Quienes son los usuarios y como se eligieron?**
Docencia (DOC), coordinacion academica (COORD) y conserjeria e infraestructura (CONS). Son
los tres perfiles que intervienen en el ciclo de vida de una falla de aula.
→ `03_Modelado/02_iStar_SD/`, `01_ERS/` seccion de actores

**A4. ¿Que documentos de la organizacion consultaron?**
Estatuto de la UTEQ, codigo de etica, reglamento de vinculacion y horario academico.
→ `02_Evidencias/Documentos_Organizacion/`

---

## B. Especificacion

**B1. ¿Cuantos requisitos hay y como se garantiza que estan completos?**
25 funcionales con ocho atributos y 16 no funcionales cuantificados sobre ISO/IEC
25010:2023. Completitud medida: **100 %**, 25 de 25. Antes de la auditoria era 96 %; el requisito que faltaba se corrigio y la metrica esta recalculada.
→ `01_ERS/ERS_SRS_2B_v2.0.pdf`; `01_ERS/Auditoria_Calidad/auditoria_calidad_especificacion.md`

**B2. Deme un requisito no funcional y su forma de comprobarlo.**
RNF-01: las alertas de anomalia se entregan en ≤ 60 s desde la deteccion. Se comprueba con
prueba de carga sobre 50 aulas simuladas midiendo el tiempo real de entrega.
→ `01_ERS/`, tabla de requisitos no funcionales

**B3. ¿Algun requisito no es verificable?**
Si, uno: RF-14 pide recomendaciones «diferenciadas y **coherentes**». Diferenciadas es
observable; coherentes no tiene metrica. Esta identificado como defecto y tiene accion de
mejora.
→ `01_ERS/Auditoria_Calidad/auditoria_calidad_especificacion.md`, seccion 4

**B4. ¿Hay requisitos en conflicto?**
Uno abierto: RF-13 y RF-16 apagan ambos equipos de aulas desocupadas fuera de horario, los
dos con umbral ≤ 2 minutos. Se resuelve fusionandolos o delimitando su alcance.
→ misma auditoria, seccion 3

**B5. ¿Como mapearon los requisitos legales?**
Articulo por articulo en la matriz, columnas `Ley` y `Articulo`. RF-24 y RF-25 derivan de
los derechos de exportacion y rectificacion de la Ley Organica de Proteccion de Datos
Personales.
→ `04_Trazabilidad/matriz_trazabilidad.csv`

---

## C. Modelado y trazabilidad

**C1. ¿Que garantiza que los diagramas los hicieron ustedes?**
Cada diagrama se entrega con su archivo fuente nativo: `.vpp` de Visual Paradigm y
`.drawio` para los modelos iStar, junto a las exportaciones.
→ `03_Modelado/`

**C2. Tome un requisito y traceelo de punta a punta.**
RF-01 nace de EV-01, se realiza en CU-01 y CU-03, lo soporta el prototipo MU-01 y lo
implementan los componentes SensorIoT y LecturaSensor.
→ `04_Trazabilidad/matriz_trazabilidad.csv`, fila 1

**C3. ¿Su matriz esta completa?**
Completa en filas, no en cadenas, y conviene decirlo en ese orden. Son **66 filas** sobre
las **60** que pide el criterio, con **cero celdas vacias** y las cuatro columnas que
faltaban -clase, proceso, caso de prueba y estado de la traza- ya anadidas: la matriz paso
de 13 a 18 columnas. El **92 %** de los requisitos, 23 de 25, tiene la cadena hacia
adelante completa; antes era 12 de 25.

Ahora la parte incomoda, por si la preguntan: de las 66 filas, **28 cierran la cadena
entera**. Las otras 38 no se esconden, se clasifican: quince huerfanas -el requisito nace
de la ley, no de una entrevista-, doce parciales y once restricciones de diseno, que se
verifican por revision y no por caso de prueba. Cada una con su causa y su accion.
→ auditoria de calidad, seccion 5

**C4. ¿Que pasa si cambia un requisito?**
Afecta en promedio a 5 requisitos, medido sobre cinco casos representativos. El nodo mas
acoplado es RF-23, la bitacora, porque registra las acciones de siete requisitos.
→ auditoria de calidad, seccion 6

---

## D. Componente empirico

**D1. ¿Cual es la pregunta de investigacion?**
En que dimensiones de calidad difieren los requisitos funcionales elicitados por analistas
humanos frente a los generados por un modelo de lenguaje, a partir del mismo corpus de
entrevistas.
→ `06_Experimento/protocolo/protocolo.pdf`

**D2. ¿Como evitaron sesgar la evaluacion?**
Paquete ciego: los 51 items se presentan con identificador ciego y orden aleatorizado, sin
indicar origen. Los tres jueces son independientes y ninguno es participante del estudio.
→ `06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md`

**D3. ¿Cual es el acuerdo entre evaluadores?**
Kappa de Fleiss entre 0,29 y 0,34 segun la dimension. En la escala de Landis y Koch es
acuerdo **justo**, y asi se reporta: no se presenta como bueno.
→ `06_Experimento/resultados/acuerdo_interevaluador.csv`

**D4. ¿Que resultados obtuvieron?**
Ninguno significativo tras la correccion de Holm-Bonferroni. La unica dimension con p por
debajo de 0,05 sin corregir, consistencia interna, sube a 0,059 al corregir.
→ `06_Experimento/resultados/hipotesis.csv`

**D5. ¿Y el tamano del efecto?**
Reportado con intervalo de confianza al 95 % por bootstrap de 10 000 replicas y semilla
fija. Los intervalos son muy anchos y cruzan el cero, que es lo esperable con esta potencia.
→ `06_Experimento/resultados/efectos.csv`

**D6. ¿Por que la muestra es tan pequena?**
El calculo de potencia lo cuantifica: para detectar d = 0,50 con alfa 0,05 y potencia 0,80
harian falta 34 unidades y hay 3. La potencia alcanzada es del **8,4 %** con el juez como
unidad de analisis. El analisis de sensibilidad por item, declarado como exploratorio y
posterior al registro, la sube a **41,7 %** con 25 y 26 observaciones. **Las dos
aproximaciones coinciden en el resultado**: ninguna dimension es significativa tras Holm.
Y 41,7 % sigue por debajo del 80 % convencional. Se declara como limitacion central, no se
disimula.
→ `06_Experimento/resultados/power_calculation.csv`

**D7. ¿Alcanzaron saturacion tematica?**
No. La ultima entrevista todavia aporta cuatro codigos nuevos sobre 36 acumulados. La curva
no tiene inflexion y se declara asi.
→ `07_Publicacion/tablas/saturacion_por_entrevista.csv`, `07_Publicacion/figuras/curva_saturacion.png`

**D8. ¿Como se que las cifras del reporte no estan escritas a mano?**
Porque se regeneran. `cd 06_Experimento && make all` reconstruye las cuatro figuras y las
cinco tablas desde los datos crudos, y la correspondencia entre cada salida y su script
esta declarada.
→ `07_Publicacion/dataset_zenodo/correspondencia_salidas.csv`

**D9. ¿Se desviaron del protocolo?**
Si, y estan documentadas con fecha, desviacion y motivo.
→ `06_Experimento/registro_previo/bitacora_desviaciones.pdf`

---

## E. Etica y datos

**E1. ¿Como protegieron a los participantes?**
Consentimiento informado firmado por cada uno, sustitucion de nombres por codigo, y
material audiovisual fuera de la zona publica. Un participante retiro su consentimiento y
su entrevista completa se elimino.
→ `02_Evidencias/Consentimientos/`, `07_Publicacion/dataset_zenodo/anonimizacion.md`

**E2. ¿Que hicieron con la entrevista retirada?**
EV-15 (DOC-03) se excluyo integramente. Ningun fragmento suyo consta en el corpus, ni en
la codificacion, ni en el material fuente del componente empirico.
→ purga registrada en el commit `639bea4`

**E3. ¿Cual es la base legal del tratamiento?**
Consentimiento informado para los datos de campo. Para los datos operativos del sistema,
mision de interes publico de la institucion educativa, conforme a la Ley Organica de
Proteccion de Datos Personales.
→ `08_Etica/`, `01_ERS/Componentes_IA/ficha_RF-09_analisis_predictivo_fallos.md` seccion 6

**E4. ¿Usaron inteligencia artificial? ¿Para que?**
En dos capacidades separadas: como **objeto de estudio**, generando el Conjunto A; y como
**apoyo de redaccion** sobre contenido del equipo. Las secciones evaluativas son produccion
propia. Declarado seccion por seccion.
→ `08_Etica/declaracion_uso_ia.md`

---

## F. Componentes de inteligencia artificial

**F1. ¿Que partes de SIGA son inteligencia artificial?**
Una sola: RF-09, el analisis predictivo de fallos. RF-03 detecta ocupacion con un umbral
determinista sobre un sensor de presencia, y por definicion no es un sistema de IA.
→ `01_ERS/Componentes_IA/clasificacion_riesgo_ia.md`, seccion 1

**F2. ¿Que riesgo tiene ese componente?**
Riesgo minimo. El analisis descarta una a una las cuatro hipotesis educativas del Anexo III
del Reglamento (UE) 2024/1689: RF-09 no decide sobre admision, no evalua aprendizaje, no
determina nivel educativo y no vigila examenes. Predice el fallo de un equipo.
→ misma clasificacion, seccion 2

**F3. ¿Como se explica una prediccion a quien no es tecnico?**
Las tres variables que mas pesaron, en lenguaje llano, maximo 60 palabras, en menos de 2
segundos y sin que haya que pedirla. Se valida con una prueba de comprension: 4 de 5
participantes no tecnicos deben explicarla con sus palabras.
→ ficha RF-09, seccion 5

**F4. ¿Que pasa si el modelo trata peor a unas aulas que a otras?**
Tres requisitos de equidad lo miden: brecha de sensibilidad entre bloques edilicios, brecha
de falsos negativos por antiguedad del equipo y brecha de cobertura por ocupacion. Si
alguna supera su umbral, **el componente no se despliega**.
→ ficha RF-09, seccion 4

---

## G. Gestion, repositorio y aporte

**G1. ¿Como se verifica quien hizo que?**
Cada fila de la declaracion de aporte cita el identificador del commit que la respalda, con
el repositorio donde se resuelve.
→ `04_Trazabilidad/aporte_individual.csv`

**G2. Como se reparte el trabajo entre los integrantes?**
De forma equilibrada entre los dos que sostuvieron la entrega calificada, y el historial lo
demuestra sin necesidad de creer en la declaracion: 65 commits de Sanchez Cornejo y 55 de
Munoz Quinonez, los dos con correo institucional. No hay ningun otro autor en el historial.
La declaracion de aporte tiene una fila por commit, cada una con su identificador, y todas
resuelven.

El equipo son hoy **tres**: Cedeno Avila, Winston Damian se reincorporo el 2026-09-02 y
asume la transcripcion y anonimizacion del corpus de la ronda terminal. Sus confirmaciones
empiezan con ese trabajo, y hasta que existan la declaracion muestra su recuento en cero en
lugar de atribuirle una contribucion que el historial todavia no respalda. Mendoza Palma,
Allan Jeremy, que figuraba en la caratula del SGA, se retiro sin producir artefactos.
-> `04_Trazabilidad/aporte_individual.csv` y `04_Trazabilidad/composicion_equipo.md`

**G2b. El registro previo en OSF declara mas personas de las que firman. Por que?**
Porque el protocolo se preregistro cuando el equipo era mayor. La lista de contribuyentes se
actualizo despues a la composicion vigente, y ambas cosas se declaran en lugar de ocultarse.
Lo que un registro OSF congela es el contenido registrado, que es lo que sostiene la marca
temporal frente al p-hacking, no la lista de personas.
-> `04_Trazabilidad/composicion_equipo.md`

**G3. ¿Como reproduzco su documento?**
Clonando el repositorio y ejecutando la secuencia de cuatro pasos del README: pdflatex,
bibtex, pdflatex, pdflatex.
→ `README.md`, apartado 4

**G4. ¿Como se que la evidencia no fue sustituida?**
`sha256sum -c checksums.sha256` comprueba sin error sobre un clon limpio, y cada archivo
multimedia tiene su hash en la ficha tecnica.
→ `checksums.sha256`, `02_Evidencias/00_Restringido/fichas_tecnicas.csv`

---

## H. Las preguntas incomodas

**H1. Si su estudio no encontro nada significativo, ¿de que sirve?**
De reportar un resultado nulo bien medido en lugar de uno significativo mal medido. El
estudio cuantifica su propia potencia, declara que es insuficiente y deja el pipeline
reproducible para que ampliar la muestra sea ejecutar una orden. Ocultarlo habria sido lo
facil.

**H2. ¿No es un problema que el mismo equipo elicitara los requisitos y evaluara la calidad?**
Si, y es una amenaza a la validez declarada. Se mitigo con evaluacion ciega por jueces
independientes que no participaron en la elicitacion. La limitacion remanente es que el
material fuente lo preparo el equipo.
→ reporte, seccion de amenazas a la validez

**H3. ¿Cuantas entrevistas deberian haber hecho?**
Mas. El cierre en 10 fue autorizado por el docente ante la restriccion de calendario, y la
consecuencia sobre la saturacion y la potencia esta cuantificada y declarada. No se
presenta como suficiente: se presenta como lo que fue.

**H4. ¿Que harian distinto si empezaran de nuevo?**
Tres cosas: llevar la unidad de analisis al item en lugar del juez, que multiplicaria la
potencia sin recolectar mas datos; registrar el protocolo antes de tocar ningun dato; y
documentar las dependencias entre requisitos desde la primera version, porque su ausencia
hizo que la especificacion aparentara un acoplamiento bajo que no tiene.

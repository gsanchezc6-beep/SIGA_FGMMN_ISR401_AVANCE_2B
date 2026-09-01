# Conjunto A — Requisitos Funcionales generados por LLM

Generado a partir del material fuente (11 transcripciones anonimizadas),
sin acceso al Conjunto B (RF elicitados por el equipo humano). Ver
`prompt_llm_conjunto_A.md` para la consigna exacta y la limitación
metodológica declarada.

> **Nota de integridad — exclusión posterior de EV-15/DOC-03 (2026-08-13).**
> Una de las 11 entrevistas fuente (EV-15, DOC-03) fue excluida del corpus
> **después** de que este Conjunto A ya había sido generado y evaluado por
> los tres jueces ciegos (ver `06_Experimento/resultados/`), por retiro del
> consentimiento informado del participante. Este documento se conserva
> **sin alterar** como registro histórico exacto de lo efectivamente
> generado y juzgado, para no romper la correspondencia con las hojas de
> puntuación ya recogidas (`06_Experimento/datos_crudos/juez1.csv`,
> `juez2.csv`, `juez3.csv`) ni la numeración de ítems del
> `Paquete_Evaluacion_Ciega_Jueces.md`. Las referencias a "EV-15" o
> "Docente (EV-15...)" que aparecen más abajo son, por tanto,
> **atribuciones históricas dentro de un experimento ya ejecutado**, no una
> afirmación vigente de que esa evidencia siga siendo válida. El contenido
> textual original de EV-15 ya no existe en `material_fuente_LLM.txt` (fue
> redactado tras la exclusión). Esta contaminación parcial y tardía del
> corpus fuente se documenta como desviación respecto del protocolo
> pre-registrado y como amenaza a la validez de constructo en
> `06_Experimento/README_OSF.md` y en la sección correspondiente del
> manuscrito; no se re-ejecutó el experimento completo por restricción de
> tiempo de la Entrega 4 (2B).

---

### RFA-01 — Monitoreo de variables ambientales del aula
- **Descripción:** El sistema debe registrar y mostrar en tiempo real la temperatura y el estado de ocupación de cada aula.
- **Actor / Origen:** Personal de servicios generales (EV-01); Coordinación de carrera (EV-10)
- **Entradas / Salidas:** Entrada: lecturas de sensores de temperatura y presencia. Salida: valor actual visible por aula.
- **Precondición / Postcondición:** Aula con sensor instalado y operativo. / Valor actualizado disponible en el panel.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** El valor mostrado en el panel coincide con una lectura de referencia tomada manualmente en el aula, con margen de error aceptable.

### RFA-02 — Consulta de disponibilidad de aulas en tiempo real
- **Descripción:** El sistema debe permitir consultar qué aulas están libres u ocupadas en un momento dado, sin necesidad de desplazarse físicamente.
- **Actor / Origen:** Personal de servicios generales (EV-01); Docente (EV-15)
- **Entradas / Salidas:** Entrada: solicitud de consulta de estado. Salida: listado de aulas con su estado (libre/ocupada).
- **Precondición / Postcondición:** Aula registrada en el sistema. / Estado mostrado corresponde al estado real.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Al ocupar físicamente un aula de prueba, el sistema refleja el cambio de estado en un tiempo razonable.

### RFA-03 — Control remoto de proyectores
- **Descripción:** El sistema debe permitir verificar y, cuando el hardware lo soporte, controlar remotamente el estado de encendido de los proyectores del aula.
- **Actor / Origen:** Docente (EV-16); Personal de servicios generales (EV-01)
- **Entradas / Salidas:** Entrada: comando de encendido/apagado o consulta de estado. Salida: confirmación del nuevo estado del proyector.
- **Precondición / Postcondición:** Proyector conectado a un módulo de control compatible. / Estado del proyector actualizado en el sistema.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un comando de prueba enviado desde el sistema cambia el estado físico observado del proyector.

### RFA-04 — Control remoto de climatización
- **Descripción:** El sistema debe permitir ajustar remotamente la temperatura del aire acondicionado del aula.
- **Actor / Origen:** Personal de servicios generales (EV-01)
- **Entradas / Salidas:** Entrada: valor de temperatura deseado. Salida: confirmación del ajuste aplicado.
- **Precondición / Postcondición:** Unidad de climatización compatible instalada. / Temperatura del aula ajustada al valor solicitado.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un ajuste de prueba enviado desde el sistema se refleja en el equipo físico dentro de un tiempo razonable.

### RFA-05 — Apagado automático de climatización en aulas desocupadas
- **Descripción:** El sistema debe apagar automáticamente el aire acondicionado cuando detecte que un aula quedó desocupada.
- **Actor / Origen:** Personal de servicios generales (EV-01)
- **Entradas / Salidas:** Entrada: estado de ocupación = desocupada. Salida: comando de apagado enviado al equipo.
- **Precondición / Postcondición:** Aula marcada como desocupada por el sensor de presencia. / Aire acondicionado apagado sin intervención manual.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Al desocupar un aula de prueba, el sistema apaga el equipo sin que el personal deba hacerlo manualmente.

### RFA-06 — Alertas automáticas de fallas de equipamiento
- **Descripción:** El sistema debe generar una alerta automática cuando detecte una anomalía en el funcionamiento de un equipo del aula (proyector, climatización).
- **Actor / Origen:** Docente (EV-13, EV-16)
- **Entradas / Salidas:** Entrada: señal de anomalía del equipo. Salida: notificación de alerta con el aula y el equipo afectado.
- **Precondición / Postcondición:** Equipo con capacidad de reportar su propio estado. / Alerta visible para el personal responsable.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Al simular una falla del equipo, se genera una alerta visible en un tiempo razonable.

### RFA-07 — Clasificación de prioridad de alertas
- **Descripción:** El sistema debe permitir clasificar cada alerta según su nivel de prioridad (por ejemplo, baja para un goteo de aire acondicionado, alta para una inundación del aula).
- **Actor / Origen:** Docente (EV-16)
- **Entradas / Salidas:** Entrada: tipo de incidente reportado. Salida: nivel de prioridad asignado.
- **Precondición / Postcondición:** Incidente registrado en el sistema. / Prioridad visible junto a la alerta.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Un incidente de prueba de cada tipo recibe la prioridad esperada según la regla definida.

### RFA-08 — Registro de solicitud de mantenimiento con adjunto fotográfico
- **Descripción:** El sistema debe permitir registrar una solicitud de mantenimiento indicando aula, equipo afectado, tipo de incidencia y una fotografía opcional del problema.
- **Actor / Origen:** Docente (EV-15, EV-16)
- **Entradas / Salidas:** Entrada: datos del incidente + imagen adjunta. Salida: ticket de mantenimiento creado.
- **Precondición / Postcondición:** Usuario autenticado con permiso de reporte. / Ticket visible en el listado de solicitudes.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un reporte de prueba con foto adjunta se registra correctamente y es recuperable en el listado.

### RFA-09 — Catálogo ampliado de tipos de incidencia
- **Descripción:** El sistema debe ofrecer un catálogo de tipos de incidencia que incluya, además de fallas de equipo, categorías como mobiliario deteriorado, pizarra en mal estado, problemas de iluminación, inundación del aula y aula cerrada.
- **Actor / Origen:** Docente (EV-15)
- **Entradas / Salidas:** Entrada: selección del tipo de incidencia desde una lista. Salida: incidencia clasificada correctamente.
- **Precondición / Postcondición:** Catálogo de tipos de incidencia cargado en el sistema. / Reporte asociado a un tipo válido.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** El formulario de reporte ofrece las categorías mencionadas como opciones seleccionables, no como texto libre.

### RFA-10 — Seguimiento de ticket de mantenimiento con estado único
- **Descripción:** El sistema debe permitir consultar el historial de un ticket de mantenimiento mostrando el estado actual, la fecha y hora de cada actualización, sin duplicar columnas de estado anterior/nuevo.
- **Actor / Origen:** Docente (EV-16)
- **Entradas / Salidas:** Entrada: consulta de un ticket por su identificador. Salida: historial con fecha, hora y estado.
- **Precondición / Postcondición:** Ticket existente en el sistema. / Historial completo visible para el usuario que lo reportó.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Al actualizar el estado de un ticket de prueba varias veces, el historial muestra cada cambio con su fecha y hora, sin columnas redundantes.

### RFA-11 — Acuse de recepción de solicitudes de mantenimiento
- **Descripción:** El sistema debe notificar de inmediato al usuario que reportó una falla que su solicitud fue recibida por el responsable, dentro del horario laboral.
- **Actor / Origen:** Docente (EV-16)
- **Entradas / Salidas:** Entrada: nueva solicitud de mantenimiento. Salida: estado "recibido" visible para quien reportó.
- **Precondición / Postcondición:** Solicitud registrada dentro del horario laboral. / Estado de acuse de recepción visible en un tiempo breve.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Una solicitud de prueba cambia a estado "recibido" en un tiempo breve tras su creación.

### RFA-12 — Notificación multicanal de incidencias críticas
- **Descripción:** El sistema debe notificar simultáneamente a la autoridad de la facultad, a la persona que reportó el incidente y al responsable de la reparación cuando se registre una incidencia.
- **Actor / Origen:** Docente (EV-15)
- **Entradas / Salidas:** Entrada: incidencia registrada. Salida: notificación enviada a los tres destinatarios.
- **Precondición / Postcondición:** Roles de autoridad y responsable configurados en el sistema. / Constancia de notificación enviada a cada destinatario.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Una incidencia de prueba genera notificación registrada para los tres roles simultáneamente.

### RFA-13 — Consulta agregada de estado de cámaras existentes
- **Descripción:** El sistema debe consultar, de forma agregada y sin identificar personas, si las cámaras de videovigilancia de un aula están operativas.
- **Actor / Origen:** Personal de servicios generales (EV-08)
- **Entradas / Salidas:** Entrada: consulta de estado de cámara por aula. Salida: indicador de funcionalidad (operativa / no operativa).
- **Precondición / Postcondición:** Cámara instalada en el aula consultada. / Estado de funcionalidad visible sin mostrar video.
- **Prioridad (MoSCoW):** Could
- **Criterio de verificación:** El sistema muestra correctamente el estado de una cámara operativa y de una no operativa, sin exponer imagen alguna.

### RFA-14 — Restricción de acceso a cámaras por rol
- **Descripción:** El sistema no debe permitir que el personal docente visualice el contenido de las cámaras de videovigilancia de las aulas.
- **Actor / Origen:** Docente (EV-15, expresó oposición explícita)
- **Entradas / Salidas:** Entrada: intento de acceso a video de cámara por un usuario con rol docente. Salida: acceso denegado.
- **Precondición / Postcondición:** Usuario autenticado con rol docente. / Intento de acceso registrado como denegado.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un intento de prueba de acceso a video con una cuenta de rol docente es rechazado por el sistema.

### RFA-15 — Consulta de disponibilidad de aulas alternativas
- **Descripción:** El sistema debe permitir consultar qué aulas están disponibles cuando la asignada resulta inutilizable, para facilitar un cambio de espacio.
- **Actor / Origen:** Docente (EV-15)
- **Entradas / Salidas:** Entrada: solicitud de aulas libres en un horario determinado. Salida: listado de aulas disponibles.
- **Precondición / Postcondición:** Aula original marcada como no disponible. / Listado de alternativas mostrado al usuario.
- **Prioridad (MoSCoW):** Could
- **Criterio de verificación:** Ante un aula marcada como no disponible, el sistema devuelve al menos una alternativa libre en el mismo horario, si existe.

### RFA-16 — Filtrado del panel por horario académico del docente
- **Descripción:** El sistema debe filtrar la vista de aulas del rol docente, mostrando únicamente las aulas correspondientes a su horario de clases.
- **Actor / Origen:** Docente (EV-15)
- **Entradas / Salidas:** Entrada: identidad del docente autenticado. Salida: listado de aulas restringido a su horario.
- **Precondición / Postcondición:** Horario del docente cargado en el sistema. / Vista muestra solo las aulas relevantes para ese docente.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Al iniciar sesión con una cuenta docente de prueba, la vista solo incluye las aulas de su horario asignado.

### RFA-17 — Inventario de equipos disponibles en laboratorios
- **Descripción:** El sistema debe mostrar la cantidad de equipos de cómputo en buen estado disponibles en un laboratorio, considerando la capacidad requerida según la asignatura.
- **Actor / Origen:** Docente (EV-16)
- **Entradas / Salidas:** Entrada: consulta de un laboratorio específico. Salida: cantidad de equipos operativos disponibles.
- **Precondición / Postcondición:** Inventario del laboratorio registrado en el sistema. / Cantidad mostrada corresponde al estado real de los equipos.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** El número de equipos "en buen estado" mostrado coincide con una verificación física de referencia.

### RFA-18 — Reportes administrativos de ocupación y consumo
- **Descripción:** El sistema debe generar reportes con el porcentaje de ocupación promedio, el consumo eléctrico estimado y las incidencias registradas de un aula en un periodo determinado.
- **Actor / Origen:** Docente (EV-16, mencionado como vista administrativa)
- **Entradas / Salidas:** Entrada: aula y rango de fechas. Salida: reporte con los tres indicadores solicitados.
- **Precondición / Postcondición:** Datos históricos de ocupación, consumo e incidencias disponibles para el aula. / Reporte generado y visible.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Un reporte generado para un aula y periodo de prueba refleja los valores esperados de los tres indicadores.

### RFA-19 — Simplificación de la pantalla principal para personal no técnico
- **Descripción:** El sistema debe presentar al personal no técnico una vista simple del estado de las aulas, comprensible sin explicación previa.
- **Actor / Origen:** Personal de servicios generales (EV-08, EV-09, validaron comprensibilidad de MU-01)
- **Entradas / Salidas:** Entrada: acceso a la vista principal con rol no técnico. Salida: información esencial de ocupación y estado del aula.
- **Precondición / Postcondición:** Usuario autenticado con rol de personal de servicios generales. / Vista mostrada sin requerir capacitación previa.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Una persona sin formación técnica logra identificar el estado de un aula usando únicamente la vista, sin asistencia.

### RFA-20 — Gestión de permisos diferenciados por rol
- **Descripción:** El sistema debe explicitar y aplicar permisos distintos según el rol del usuario (por ejemplo, si un docente puede reportar o solo consultar alertas).
- **Actor / Origen:** Docente (EV-13)
- **Entradas / Salidas:** Entrada: acción solicitada por un usuario autenticado. Salida: acción permitida o denegada según su rol.
- **Precondición / Postcondición:** Rol del usuario definido en el sistema. / Acción ejecutada solo si el rol lo permite.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un usuario de prueba con rol docente puede realizar las acciones permitidas para ese rol y ninguna otra.

### RFA-21 — Historial de intervenciones de mantenimiento por equipo
- **Descripción:** El sistema debe exponer, también al rol docente, el historial de intervenciones de mantenimiento realizadas sobre un equipo específico.
- **Actor / Origen:** Docente (EV-13, detectó esta brecha en el prototipo)
- **Entradas / Salidas:** Entrada: consulta de historial por equipo. Salida: listado de intervenciones previas con fecha y causa.
- **Precondición / Postcondición:** Equipo con al menos una intervención registrada. / Historial visible para el rol docente, no solo administrativo.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Un usuario docente de prueba puede consultar el historial de un equipo con intervenciones previas registradas.

### RFA-22 — Registro de estado del aula por sesión de clase
- **Descripción:** El sistema debe permitir registrar, al inicio y al final de cada sesión de clase, el estado de los equipos del aula (proyector, climatización), dejando constancia de en qué condición se recibió y se dejó el espacio.
- **Actor / Origen:** Docente (EV-13)
- **Entradas / Salidas:** Entrada: registro de estado con responsable identificado. Salida: bitácora de estado por sesión.
- **Precondición / Postcondición:** Sesión de clase activa en el sistema. / Registro de estado asociado a esa sesión y ese responsable.
- **Prioridad (MoSCoW):** Could
- **Criterio de verificación:** Un registro de prueba al inicio y fin de una sesión queda almacenado con responsable, fecha y hora.

### RFA-23 — Registro de bitácora de acciones de usuario
- **Descripción:** El sistema debe registrar en una bitácora las acciones relevantes ejecutadas por los usuarios (control remoto de equipos, gestión de roles).
- **Actor / Origen:** Personal de servicios generales (EV-01); Docente (EV-02)
- **Entradas / Salidas:** Entrada: acción ejecutada por un usuario. Salida: entrada de bitácora con usuario, acción y fecha/hora.
- **Precondición / Postcondición:** Usuario autenticado ejecuta una acción relevante. / Entrada de bitácora generada de forma automática.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Una acción de prueba (por ejemplo, apagar un proyector) genera una entrada de bitácora verificable.

### RFA-24 — Monitoreo de conectividad de dispositivos IoT
- **Descripción:** El sistema debe indicar si los sensores y dispositivos IoT de un aula están conectados y transmitiendo datos correctamente.
- **Actor / Origen:** Personal de servicios generales (EV-01, mención indirecta sobre confiabilidad de sensores)
- **Entradas / Salidas:** Entrada: señal de estado de conexión del dispositivo. Salida: indicador de conectividad por aula.
- **Precondición / Postcondición:** Dispositivo IoT configurado en la red del aula. / Estado de conectividad visible y actualizado.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Al desconectar intencionalmente un sensor de prueba, el sistema refleja el cambio de estado de conectividad.

### RFA-25 — Consulta desde dispositivo móvil
- **Descripción:** El sistema debe ser consultable desde un teléfono celular, sin requerir instalación adicional.
- **Actor / Origen:** Docente (EV-15, EV-16, ambos indicaron preferencia por consulta desde el teléfono)
- **Entradas / Salidas:** Entrada: acceso desde navegador móvil. Salida: interfaz funcional adaptada a pantalla pequeña.
- **Precondición / Postcondición:** Dispositivo móvil con navegador y conexión a la red institucional. / Interfaz utilizable sin instalación de aplicación adicional.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un usuario de prueba accede y opera las funciones principales desde un navegador móvil sin instalar software adicional.

### RFA-26 — Alerta ante conectividad de red no disponible
- **Descripción:** El sistema debe advertir a los usuarios cuando la conectividad de red del aula no permita el funcionamiento normal del sistema, dado que no todas las aulas cuentan con acceso a internet.
- **Actor / Origen:** Docente (EV-15, señaló la falta de conectividad como riesgo crítico)
- **Entradas / Salidas:** Entrada: pérdida de señal de red del aula. Salida: aviso de funcionalidad limitada.
- **Precondición / Postcondición:** Aula sin conectividad de red disponible. / Aviso mostrado antes de que el usuario intente usar funciones dependientes de red.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Al simular la pérdida de conectividad de un aula de prueba, el sistema muestra el aviso correspondiente.

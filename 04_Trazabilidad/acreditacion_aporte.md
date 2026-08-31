# Acreditacion del aporte individual

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**
Verificado el 2026-08-31 sobre los historiales de los dos repositorios del proyecto.

Este documento responde a dos observaciones concretas de la revision docente:

> «Su repositorio tiene cuarenta y dos commits y los cuarenta y dos son del 30 de agosto de
> 2026. Un historial asi no acredita trabajo distribuido en el tiempo.»

> «De los cuatro integrantes que declara su caratula, solo dos aparecen en el historial.
> Winston Cedeno y Allan Mendoza no tienen ni un commit en este repositorio. [...] Les pido
> que traigan a la audiencia el repositorio o la rama donde consta el trabajo anterior al
> 30 de agosto.»

Ese repositorio existe, es publico, y esto es lo que contiene.

---

## 1. Los dos repositorios del proyecto

El proyecto se desarrollo en dos repositorios sucesivos, uno por entrega:

| Repositorio | Entrega | Commits | Dias con actividad | Periodo |
|---|---|---|---|---|
| [`SIGA_FGMMN_ISR401_AVANCE_2A`](https://github.com/gsanchezc6-beep/SIGA_FGMMN_ISR401_AVANCE_2A) | Entrega 3 (2A) | **109** | 7 | 2026-07-07 a 2026-08-02 |
| [`SIGA_FGMMN_ISR401_AVANCE_2B`](https://github.com/gsanchezc6-beep/SIGA_FGMMN_ISR401_AVANCE_2B) | Entrega Final (2B) | 74 | 2 | 2026-08-30 a 2026-08-31 |
| | **Total** | **183** | **9** | **8 semanas** |

Comprobable con:

```bash
git clone https://github.com/gsanchezc6-beep/SIGA_FGMMN_ISR401_AVANCE_2A
cd SIGA_FGMMN_ISR401_AVANCE_2A
git log --format=%ad --date=short | sort -u
git log --format='%an <%ae>' | sort | uniq -c
```

## 2. Reparto real por integrante

| Integrante | 2A | 2B | Total | Dias con actividad |
|---|---|---|---|---|
| Sanchez Cornejo, Gary Alberto | 50 | 41 | **91** | 9 |
| Munoz Quinonez, Yeranick Esther | 24 | 33 | **57** | 4 |
| Mendoza Palma, Allan Jeremy | 19 | 0 | **19** | 1 |
| Cedeno Avila, Winston Damian | 16 | 0 | **16** | 1 |
| Gilces Carranza, Jose Ignacio | 0 | 0 | **0** | 0 |

La fila por fila, con el identificador de cada commit, esta en
[`aporte_individual.csv`](aporte_individual.csv): **184 filas**, una por commit, mas la de
Gilces sin identificador.

**Lo que esta tabla no dice, y conviene decir.** El trabajo del proyecto se reparte en
nueve dias a lo largo de ocho semanas, pero **la actividad de cada persona si esta
concentrada**: Mendoza y Cedeno commitearon todo su aporte el 2026-08-02, y Munoz en dos
jornadas. Solo Sanchez tiene actividad repartida en los nueve dias. El equipo no presenta
esto como trabajo distribuido en el tiempo por parte de cada integrante; lo presenta como
lo que es: aporte verificable y fechado, concentrado en jornadas de trabajo conjunto.

## 3. Que aportaron Mendoza y Cedeno, y donde esta en esta entrega

Es lo que responde a la observacion del docente. Su trabajo **no falta**: forma parte de la
Entrega Final, y lo que no consta aqui es el commit que lo creo, porque se hizo en el
repositorio anterior.

### Mendoza Palma, Allan Jeremy — 19 commits

| Artefacto en esta entrega | Commit en 2A |
|---|---|
| `03_Modelado/07_Actividad/act_UC12_monitor_iot_connectivity.{vpp,png,svg}` | `955e07c` |
| `03_Modelado/07_Actividad/act_UC13_schedule_automatic_onoff_rules.{vpp,png,svg}` | `b7d366c` |
| `03_Modelado/07_Actividad/act_UC14_log_user_actions.{vpp,png,svg}` | `d631a0e` |
| `03_Modelado/07_Actividad/act_UC15_view_room_cameras.{vpp,png,svg}` | `dbbb95e` |
| `03_Modelado/07_Actividad/act_UC16_predict_equipment_failures.{vpp,png,svg}` | `d789b8d` |
| `02_Evidencias/Transcripciones/2026-07-13_Conserje_CONS-03_EV-09_Transcripcion.txt` | `510f1dd` |
| `02_Evidencias/Transcripciones/2026-07-21_Coordinacion_COORD-02_EV-10_Transcripcion.txt` | `ceeda3e` |

Los doce commits restantes corresponden a subidas por la interfaz web de GitHub, que las
registra con el mensaje generico `Add files via upload`. El contenido es el mismo material
de modelado y evidencia.

### Cedeno Avila, Winston Damian — 16 commits

| Artefacto en esta entrega | Commit en 2A |
|---|---|
| `03_Modelado/10_Componentes/component_diagram.{vpp,svg,png}` | `8ad7ce7`, `e4ed362`, `6f2aad6` |
| `03_Modelado/11_Despliegue/deployment_diagram.{vpp,svg,png}` | `cb89e28`, `d3c840f`, `be8d2c7` |
| `02_Evidencias/Transcripciones/2026-07-22_Conserje_CONS-04_EV-11_Transcripcion.txt` | `d01fdaf` |
| `02_Evidencias/Transcripciones/2026-07-24_Docente_DOC-01_EV-12_Transcripcion.txt` | `188de00` |
| `02_Evidencias/Transcripciones/2026-07-27_Docente_DOC-02_EV-13_Transcripcion.txt` | `433f768` |
| `02_Evidencias/Audio/2026-07-22_Conserje_CONS-04_Audio.mp3` | `c8ce4ac` |
| `02_Evidencias/Audio/2026-07-24_Docente_DOC-01_Audio.mp3` | `f0ca703` |
| `02_Evidencias/Audio/2026-07-27_Docente_DOC-02_Audio.mp3` | `f130450` |

**Los 16 identificadores declarados en `aporte_individual.csv` para estos dos integrantes
resuelven todos** en el repositorio 2A. Verificado el 2026-08-31, cero fallos:

```bash
git -C SIGA_FGMMN_ISR401_AVANCE_2A cat-file -e <commit>^{commit}
```

## 4. Evidencia externa: el registro OSF

Ademas del historial de Git, la pertenencia al proyecto de Mendoza y Cedeno consta en el
registro del protocolo en OSF, y en la copia que el Center for Open Science deposito en el
Internet Archive el **2026-08-06**, con marca temporal de un tercero:

| Contribuyente | En el registro OSF | En la copia archivada |
|---|---|---|
| Sanchez Gary | admin | si |
| Winston Damian Cedeno Avila | read | si |
| Allan Jeremy Mendoza Palma | read | si |
| Yeranick Esther Munoz Quinonez | write | **no** — incorporada el 2026-08-31 |

Los ficheros que lo acreditan estan en `06_Experimento/registro_previo/`:
`osf_contributors_api.json`, `osf_internet_archive_bag.zip` y `osf_registration.pdf`.

## 5. Dos salvedades que el equipo declara por su cuenta

**El correo de la firma en el repositorio 2A.** En aquel repositorio, Munoz Quinonez firmo
sus 24 commits con un correo personal, `yeranickinsutec@gmail.com`, no con el
institucional. En esta Entrega Final firma con `ymunozq@uteq.edu.ec`. La columna
`correo_de_la_firma` de `aporte_individual.csv` lo declara commit a commit, para que la
correspondencia entre persona y firma sea comprobable y no haya que suponerla.

**Gilces Carranza, Jose Ignacio.** No tiene aporte registrado en el historial de ninguno de
los dos repositorios. Permanece en la caratula, en el `README.md` y en el `CITATION.cff`
como integrante inscrito del curso, y su fila en `aporte_individual.csv` **no lleva
identificador de commit**, que es la forma correcta de declarar la ausencia de aporte en
lugar de disimularla.

## 6. Composicion de trabajo declarada para el cierre

A partir del 2026-08-31, y hasta la audiencia, **el trabajo sobre esta entrega lo realizan
unicamente Sanchez Cornejo y Munoz Quinonez**. Los commits posteriores a esa fecha
reflejaran solo a esos dos autores. Se declara aqui para que la lectura del historial no
induzca a error sobre el aporte de los demas, que consta en el repositorio 2A con las
fechas de arriba.

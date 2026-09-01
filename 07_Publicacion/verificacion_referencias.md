# Verificacion del archivo de referencias

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

Fecha de la verificacion: **2026-09-01**. Archivo verificado:
`07_Publicacion/referencias.bib`.

---

## Como se verifico

Cada entrada con DOI se resolvio contra el registro de la fuente pidiendo sus metadatos
en formato CSL-JSON, y el titulo devuelto se comparo con el declarado en el archivo. Una
entrada cuyo DOI resuelve a otro trabajo es peor que una entrada sin DOI, y por eso la
comprobacion es sobre el titulo y no sobre la mera existencia del identificador.

El procedimiento descarto al menos un candidato: durante la busqueda automatica, la
revision sistematica de Cheng y otros recibio como propuesta el DOI `10.1002/spe.3428`,
que resuelve a un articulo distinto sobre aprendizaje automatico multietiqueta en
domotica. Se rechazo y se sustituyo por `10.1002/spe.70029`, que si corresponde.

## Resumen

| | |
|---|---|
| Entradas totales | **40** |
| Con DOI que resuelve al trabajo citado | **35** |
| Sin DOI, por no tener uno asignado | **5** |
| Con problema | **0** |

El minimo que fija la guia es de 40 entradas. Hay **40**.

## Entradas sin DOI, con su motivo

Ninguna de estas cinco carece de DOI por descuido: son documentos que no reciben uno.

| Clave | Que es | Por que no tiene DOI |
|---|---|---|
| `iso25010_2023` | ISO/IEC 25010:2023 --- Systems and software engineer | Norma ISO/IEC. Las normas ISO no reciben DOI; se identifican por su codigo. |
| `washizaki2024swebok` | Guide to the Software Engineering Body of Knowledge, | Informe tecnico de la IEEE Computer Society. Sin DOI asignado. |
| `sommerville2015software` | Software Engineering | Libro. Se identifica por ISBN, no por DOI. |
| `asamblea2021lopdp` | Ley Org'anica de Protecci'on de Datos Personales | Ley publicada en el Registro Oficial del Ecuador. Sin DOI. |
| `kitchenham2007guidelines` | Guidelines for performing systematic literature revi | Informe tecnico conjunto de Keele y Durham (EBSE-2007-01). Sin DOI. |

## Entradas verificadas

| Clave | DOI | Resuelve a |
|---|---|---|
| `polin2023smartcampus` | `10.3390/buildings13040891` | The Making of Smart Campus: A Review and Conceptual Framework — Buildings |
| `zhang2024smartclassrooms` | `10.3390/s24175487` | Smart Classrooms: How Sensors and AI Are Shaping Educational Paradigms — Sensors |
| `delgado2026riemat` | `10.33936/riemat.v11i1.7824` | Sistema internet de las cosas (IOT), para la automatización y monitore — Revista |
| `iso29148_2018` | `10.1109/ieeestd.2018.8559686` | ISO/IEC/IEEE International Standard - Systems and software engineering — IEEE |
| `pohl2010requirements` | `10.5860/choice.48-3304` | Requirements engineering: fundamentals, principles, and techniques — Choice Revi |
| `cheng2026genai` | `10.1002/spe.70029` | Generative AI for Requirements Engineering: A Systematic Literature Re — Softwar |
| `arora2024advancing` | `10.1007/978-3-031-55642-5_6` | Advancing Requirements Engineering Through Generative AI: Assessing th — Generat |
| `vogelsang2024using` | `10.1007/978-3-031-73143-3_16` | Using Large Language Models for Natural Language Processing Tasks in R — Handboo |
| `chazette2020explainability` | `10.1007/s00766-020-00333-1` | Explainability as a non-functional requirement: challenges and recomme — Require |
| `chazette2021exploring` | `10.1109/re51729.2021.00025` | Exploring Explainability: A Definition, a Model, and a Knowledge Catal — 2021 IE |
| `chazette2022explainable` | `10.1007/s00766-022-00393-5` | Explainable software systems: from requirements analysis to system eva — Require |
| `molleri2020empirically` | `10.1016/j.infsof.2019.106240` | An empirically evaluated checklist for surveys in software engineering — Informa |
| `hennink2017code` | `10.1177/1049732316665344` | Code Saturation Versus Meaning Saturation — Qualitative Health Research |
| `guest2006how` | `10.1177/1525822X05279903` | How Many Interviews Are Enough? — Field Methods |
| `runeson2009guidelines` | `10.1007/s10664-008-9102-8` | Guidelines for conducting and reporting case study research in softwar — Empiric |
| `jedlitschka2008reporting` | `10.1007/978-1-84800-044-5_8` | Reporting Experiments in Software Engineering — Guide to Advanced Empirical Soft |
| `wohlin2012experimentation` | `10.1007/3-540-27662-9_19` | Experimentation in Software Engineering — Foundations of Empirical Software Engi |
| `nosek2018preregistration` | `10.31219/osf.io/2dxu5` | The Preregistration Revolution — Center for Open Science |
| `montgomery2022empirical` | `10.1007/s00766-021-00367-z` | Empirical research on requirements quality: a systematic mapping study — Require |
| `cohen1960coefficient` | `10.1177/001316446002000104` | A Coefficient of Agreement for Nominal Scales — Educational and Psychological Me |
| `fleiss1971measuring` | `10.1037/h0031619` | Measuring nominal scale agreement among many raters. — Psychological Bulletin |
| `wilkinson2016fair` | `10.1038/sdata.2016.18` | The FAIR Guiding Principles for scientific data management and steward — Scienti |
| `smith2016software` | `10.7287/peerj.preprints.2169v2` | Software Citation Principles — PeerJ |
| `druskat2021citation` | `10.5281/zenodo.5171937` | Citation File Format — Zenodo |
| `lubos2024leveraging` | `10.1109/RE59067.2024.00046` | Leveraging LLMs for the Quality Assurance of Software Requirements — 2024 IEEE 3 |
| `kurni2025iot` | `10.1007/978-3-031-67387-0_3` | IoT-Based Smart Classroom — The Internet of Educational Things |
| `talu2025exploring` | `10.12928/biste.v7i1.12361` | Exploring IoT Applications for Transforming University Education: Smar — Buletin |
| `ronanki2023investigating` | `10.1109/seaa60479.2023.00061` | Investigating ChatGPT’s Potential to Assist in Requirements Elicitatio — 2023 49 |
| `gorer2023generating` | `10.1109/rew57809.2023.00015` | Generating Requirements Elicitation Interview Scripts with Large Langu — 2023 IE |
| `ray2023agile` | `10.3390/systems11070352` | Agile Methodology for the Standardization of Engineering Requirements  — Systems |
| `challa2025gas` | `10.1016/j.mex.2025.103386` | Gas sensors and real-time video for accurate classroom occupancy detec — Methods |
| `chaudhari2024fundamentals` | `10.3390/s24072123` | Fundamentals, Algorithms, and Technologies of Occupancy Detection for  — Sensors |
| `hymel2025analysis` | `10.48550/arXiv.2501.19297` | Analysis of LLMs vs Human Experts in Requirements Engineering — arXiv |
| `almeida2025elicitation` | `10.29327/1588952.28-12` | From Elicitation Interviews to Software Requirements: Evaluating LLM P — Anais d |
| `ronanki2023chatgpt` | `10.1007/978-3-031-48550-3_17` | ChatGPT as a Tool for User Story Quality Evaluation: Trustworthy Out o — Lecture |

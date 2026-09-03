# Fuentes editables de los diagramas — elemento A3

**Proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ**

La guia exige el archivo fuente editable de todo diagrama junto a su imagen exportada:
«sin el archivo fuente no hay prueba de que el diagrama se construyo y no se descargo».

Las fuentes **no se copian a esta carpeta**: residen junto a la imagen que producen, que
es donde sirven para trabajar. Este inventario dice donde esta cada una.

| Tipo de fuente | Cantidad | Herramienta |
|---|---|---|
| `.vpp` | 39 | Visual Paradigm |
| `.drawio` | 4 | draw.io |

| Imagen exportada | Cantidad |
|---|---|
| `.svg` | 43 |
| `.png` | 54 |

## Inventario de fuentes

| Fuente editable | Carpeta |
|---|---|
| `Diagrama_Contexto.vpp` | `03_Modelado/01_Contexto` |
| `iStar_SD.drawio` | `03_Modelado/02_iStar_SD` |
| `iStar_SR.drawio` | `03_Modelado/03_iStar_SR` |
| `usecase_general.vpp` | `03_Modelado/04_Casos_Uso` |
| `class_diagram_refined.vpp` | `03_Modelado/05_Clases` |
| `seq_UC01_monitor_room_status.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC02_remote_equipment_control.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC03_detect_room_occupancy.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC04_generate_anomaly_alerts.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC05_attend_anomaly_alert.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC06_register_maintenance_request.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC07_track_maintenance_ticket.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC08_view_failure_maintenance_history.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC09_generate_administrative_reports.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC10_export_reports.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC11_manage_users_roles_permissions.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC12_monitor_iot_connectivity.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC13_schedule_automatic_onoff_rules.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC14_log_user_actions.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC15_view_room_cameras.vpp` | `03_Modelado/06_Secuencia` |
| `seq_UC16_predict_equipment_failures.vpp` | `03_Modelado/06_Secuencia` |
| `act_UC01_monitor_room_status.vpp` | `03_Modelado/07_Actividad` |
| `act_UC02_remote_equipment_control.vpp` | `03_Modelado/07_Actividad` |
| `act_UC03_detect_room_occupancy.vpp` | `03_Modelado/07_Actividad` |
| `act_UC04_generate_anomaly_alerts.vpp` | `03_Modelado/07_Actividad` |
| `act_UC05_attend_anomaly_alert.vpp` | `03_Modelado/07_Actividad` |
| `act_UC06_register_maintenance_request.vpp` | `03_Modelado/07_Actividad` |
| `act_UC07_track_maintenance_ticket.vpp` | `03_Modelado/07_Actividad` |
| `act_UC08_view_failure_maintenance_history.vpp` | `03_Modelado/07_Actividad` |
| `act_UC09_generate_administrative_reports.vpp` | `03_Modelado/07_Actividad` |
| `act_UC10_export_reports.vpp` | `03_Modelado/07_Actividad` |
| `act_UC11_manage_users_roles_permissions.vpp` | `03_Modelado/07_Actividad` |
| `act_UC12_monitor_iot_connectivity.vpp` | `03_Modelado/07_Actividad` |
| `act_UC13_schedule_automatic_onoff_rules.vpp` | `03_Modelado/07_Actividad` |
| `act_UC14_log_user_actions.vpp` | `03_Modelado/07_Actividad` |
| `act_UC15_view_room_cameras.vpp` | `03_Modelado/07_Actividad` |
| `act_UC16_predict_equipment_failures.vpp` | `03_Modelado/07_Actividad` |
| `state_alert.vpp` | `03_Modelado/08_Estados` |
| `state_maintenance_request.vpp` | `03_Modelado/08_Estados` |
| `dfd_nivel_0.drawio` | `03_Modelado/09_DFD` |
| `dfd_nivel_1.drawio` | `03_Modelado/09_DFD` |
| `component_diagram.vpp` | `03_Modelado/10_Componentes` |
| `deployment_diagram.vpp` | `03_Modelado/11_Despliegue` |

## Comprobacion

```
git ls-files '*.vpp' '*.drawio' | wc -l
```

Debe dar **43**.

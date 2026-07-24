# Métricas de éxito

**Proyecto:** EngineeringOS
**Fase:** Discovery inicial
**Día de trabajo:** W01D01
**Issue relacionada:** [#1](https://github.com/JuanCarlosBP/portfolio/issues/1)
**Estado:** Borrador inicial

## Objetivo

Definir señales verificables que permitan comprobar si EngineeringOS mejora la trazabilidad, la calidad del cierre y la capacidad de reconstruir el trabajo sin introducir una carga administrativa excesiva.

## Principios de medición

- Utilizar únicamente datos obtenidos durante el uso real del sistema.
- Diferenciar resultados observados de objetivos todavía no validados.
- Evitar métricas que premien producir documentación sin aportar valor.
- Mantener métodos de cálculo sencillos y reproducibles.
- Revisar las métricas cuando la evidencia demuestre que no ayudan a tomar decisiones.
- No presentar una mejora como demostrada mientras no exista una referencia comparable.

## Métricas principales

| ID | Métrica | Cálculo | Objetivo inicial | Evidencia |
|---|---|---|---|---|
| KPI-01 | Trazabilidad completa | Incrementos cerrados con issue, rama, commit, validación y entrega enlazados / total de incrementos cerrados | 100 % | Issue, historial Git y registro de evidencias |
| KPI-02 | Cumplimiento de terminado | Elementos satisfechos de la Definition of Done / elementos exigibles | 100 % antes del cierre | Checklist de la issue o entrega |
| KPI-03 | Validación reproducible | Incrementos cerrados con comandos y resultados de validación conservados / total de incrementos cerrados | 100 % | CI, logs o documentos de evidencia |
| KPI-04 | Recuperación de contexto | Tiempo necesario para identificar objetivo, estado, decisiones y siguiente acción utilizando solo el repositorio | 10 minutos o menos | Ejercicio de reconstrucción registrado |
| KPI-05 | Sobrecarga administrativa | Tiempo dedicado a mantener EngineeringOS / tiempo total del incremento | 15 % o menos | Registro horario del incremento |
| KPI-06 | Cambios de alcance controlados | Nuevas necesidades incorporadas mediante issue o backlog / nuevas necesidades detectadas | 100 % | Issues y backlog |
| KPI-07 | Cierres incompletos | Incrementos cerrados con elementos obligatorios pendientes | 0 | Checklist y revisión de cierre |
| KPI-08 | Revisión externa autosuficiente | Entregas que pueden comprenderse sin explicación oral adicional / entregas revisadas | 90 % o más tras disponer de muestra suficiente | Lista de comprobación de revisión |

## Métricas de apoyo

### Tiempo de ciclo

Tiempo transcurrido desde que un incremento comienza hasta que cumple su Definition of Done. Se utilizará para detectar bloqueos y crecimientos de alcance, no para premiar la velocidad aislada.

### Trabajo pendiente declarado

Número de limitaciones, riesgos o tareas pendientes identificados explícitamente al cerrar cada incremento. Su existencia no representa por sí misma un fallo; ocultarlos o perderlos sí.

### Automatización útil

Número de comprobaciones repetitivas ejecutadas automáticamente y utilizadas realmente durante el desarrollo. No se contabilizarán automatizaciones creadas pero no integradas en el flujo.

### Fallos detectados antes de la entrega

Número de problemas relevantes encontrados por pruebas, linters, revisiones o controles automáticos antes del cierre del incremento.

## Línea base inicial

Al comenzar EngineeringOS todavía no existe una muestra suficiente para calcular resultados cuantitativos fiables. La situación inicial observada es:

- La trazabilidad no sigue todavía un formato uniforme.
- Las validaciones pueden ejecutarse sin conservar evidencia persistente.
- No existe una Definition of Done común para todos los incrementos.
- El tiempo de recuperación de contexto no se registra.
- La carga administrativa del proceso no se mide.
- Los cambios de alcance pueden incorporarse sin pasar por un backlog explícito.

Los primeros incrementos servirán para establecer la línea base cuantitativa. Hasta entonces, los valores deberán figurar como no disponibles y no como cero.

## Método de recogida

Para cada incremento se registrarán, como mínimo:

1. Issue de origen.
2. Rama utilizada.
3. Commits relacionados.
4. Criterios de aceptación.
5. Validaciones ejecutadas.
6. Evidencias conservadas.
7. Estado de la Definition of Done.
8. Tiempo total aproximado.
9. Tiempo administrativo aproximado.
10. Riesgos, limitaciones y siguiente acción.

## Frecuencia de revisión

- Al cerrar cada incremento: KPI-01, KPI-02, KPI-03, KPI-06 y KPI-07.
- Al finalizar cada semana: KPI-04, KPI-05 y métricas de apoyo.
- Al completar una entrega revisable: KPI-08.
- Al finalizar cada fase: revisión de objetivos, utilidad y coste de todas las métricas.

## Umbral de utilidad del sistema

EngineeringOS se considerará útil inicialmente si, después de varios incrementos reales:

1. Mantiene una trazabilidad completa de principio a fin.
2. Reduce los cierres sin validación o con trabajo obligatorio pendiente.
3. Permite recuperar el contexto en diez minutos o menos.
4. Mantiene la carga administrativa por debajo del 15 %.
5. Facilita una revisión externa sin depender de explicaciones verbales extensas.

## Señales de alerta

El sistema deberá simplificarse o revisarse si ocurre alguna de estas situaciones:

- Mantenerlo consume más del 15 % del tiempo de trabajo de forma repetida.
- Se crean documentos que no se consultan ni ayudan a decidir.
- Las evidencias existen, pero no permiten reproducir las comprobaciones.
- Los pasos manuales se omiten habitualmente por ser demasiado complejos.
- Las métricas incentivan cerrar rápido en lugar de cerrar correctamente.
- La trazabilidad exige duplicar la misma información en varios lugares.

## Limitaciones

Estas métricas evaluarán el funcionamiento de EngineeringOS y la calidad de sus evidencias. No medirán directamente la capacidad profesional completa del desarrollador ni permitirán atribuir por sí solas una mejora de empleabilidad o una futura contratación.

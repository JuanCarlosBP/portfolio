# Proceso actual

**Proyecto:** EngineeringOS
**Fase:** Discovery inicial
**Día de trabajo:** W01D01
**Issue relacionada:** [#1](https://github.com/JuanCarlosBP/portfolio/issues/1)
**Estado:** Borrador inicial

## Objetivo

Describir cómo se organiza actualmente el trabajo del portfolio, detectar sus principales carencias y establecer una referencia inicial para comprobar posteriormente si EngineeringOS aporta mejoras reales.

## Alcance del análisis

Este documento representa una primera aproximación basada en el proceso disponible al comenzar el proyecto. Deberá revisarse con evidencias obtenidas durante el uso real de EngineeringOS.

## Proceso actual de referencia

### 1. Seleccionar el trabajo

Se elige una tarea a partir de la ruta del portfolio, una necesidad detectada o una idea pendiente.

### 2. Interpretar el objetivo

Se analiza qué debe construirse, aunque el problema, los usuarios y los criterios de aceptación no siempre quedan registrados en un mismo lugar.

### 3. Implementar la solución

Se crean o modifican archivos para producir el resultado previsto. Durante esta fase pueden aparecer nuevas ideas que amplíen el alcance inicial.

### 4. Tomar decisiones técnicas

Se eligen estructuras, herramientas o enfoques, pero sus alternativas y motivos pueden quedar únicamente en la conversación o en el contexto de la sesión.

### 5. Realizar comprobaciones

Se revisa el resultado y se ejecutan las validaciones disponibles. La ejecución puede ser correcta sin que quede una evidencia persistente y fácilmente localizable.

### 6. Registrar los cambios

Los cambios se incorporan al repositorio mediante commits, aunque todavía no existe un criterio común que garantice su relación con una necesidad, una issue y una validación concreta.

### 7. Presentar el resultado

El proyecto se publica en el portfolio, pero reconstruir todo el proceso puede requerir consultar distintas fuentes y explicar verbalmente parte del contexto.

## Flujo resumido

```text
Necesidad o idea
       ↓
Interpretación del objetivo
       ↓
Implementación
       ↓
Comprobaciones
       ↓
Commit y presentación
```

## Carencias detectadas

| Área | Situación inicial | Consecuencia |
|---|---|---|
| Planificación | Los objetivos pueden no estar divididos en incrementos verificables. | Aumenta el riesgo de abordar demasiado trabajo a la vez. |
| Trazabilidad | No siempre existe una relación explícita entre necesidad, issue, rama, commit y entrega. | Resulta difícil reconstruir el origen y la finalidad de un cambio. |
| Decisiones | Los motivos y alternativas pueden no conservarse. | Se pierde contexto y se dificulta revisar las elecciones técnicas. |
| Validación | Las comprobaciones pueden ejecutarse sin registrar su resultado. | No siempre existe evidencia reproducible de la calidad alcanzada. |
| Cierre | No hay todavía una definición común de trabajo terminado. | Una tarea puede cerrarse con elementos pendientes. |
| Presentación | La información relevante puede quedar distribuida. | La revisión externa requiere más tiempo y explicaciones adicionales. |
| Alcance | Las nuevas ideas pueden incorporarse durante la ejecución. | El incremento crece y se retrasa su finalización. |

## Puntos de fricción prioritarios

1. Pérdida de contexto entre sesiones.
2. Dificultad para saber cuál es el siguiente trabajo prioritario.
3. Falta de una trazabilidad uniforme de principio a fin.
4. Ausencia de evidencias persistentes para algunas validaciones.
5. Riesgo de ampliar el alcance antes de terminar el incremento.
6. Tiempo necesario para preparar una revisión externa comprensible.

## Información que ya existe

El proceso no parte de cero. Ya dispone de elementos aprovechables:

- Una ruta maestra con proyectos y trabajo diario.
- Un repositorio Git como fuente de verdad para los entregables.
- Issues de GitHub para describir necesidades y criterios de aceptación.
- Ramas y commits para aislar y registrar cambios.
- Documentación Markdown versionada junto al proyecto.
- Herramientas locales capaces de ejecutar validaciones y automatizaciones.

## Oportunidad de mejora

EngineeringOS puede conectar los elementos existentes mediante un flujo común que defina qué debe registrarse antes, durante y después de cada incremento, sin convertir el mantenimiento del sistema en una carga superior al trabajo que pretende facilitar.

## Estado deseado inicial

El primer estado objetivo será un flujo mínimo en el que cada incremento relevante:

1. Parta de una issue con alcance y criterios de aceptación.
2. Se desarrolle en una rama identificable.
3. Registre las decisiones técnicas que necesiten explicación.
4. Ejecute controles de calidad reproducibles.
5. Conserve evidencias suficientes de las validaciones.
6. Termine con commits comprensibles y una entrega revisable.
7. Permita detectar explícitamente cualquier elemento pendiente.

## Preguntas por validar

- ¿Cuánto tiempo administrativo añade el nuevo flujo?
- ¿Qué documentos aportan valor real y cuáles resultan redundantes?
- ¿Qué comprobaciones pueden automatizarse de forma sencilla?
- ¿La trazabilidad permite reconstruir un incremento sin explicaciones externas?
- ¿Una definición explícita de terminado reduce los cierres incompletos?

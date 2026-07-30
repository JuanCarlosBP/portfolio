# ADR-0002 · Contrato ejecutable de planificación y terminado

**Estado:** Aceptada

**Fecha:** 2026-07-30

**Decisión relacionada:** W01D02

**Issue:** [#8](https://github.com/JuanCarlosBP/portfolio/issues/8)

## Contexto

W01D01 demostró que una validación estructural pequeña puede impedir cerrar un
discovery incompleto. Sin embargo, EngineeringOS todavía carecía de un contrato
operativo para decidir qué trabajo debe realizarse primero, cuánto trabajo puede
permanecer activo y cuándo un incremento puede considerarse terminado.

El riesgo principal de W01D02 es crear un backlog y una Definition of Done que
parezcan profesionales, pero que puedan incumplirse sin producir ningún fallo
observable.

## Decisión

Mantener el backlog y la Definition of Done como documentos Markdown
versionados y añadir un validador determinista en Python que compruebe:

- existencia de los dos documentos;
- metadatos y trazabilidad obligatorios;
- diez elementos de backlog ordenados;
- prioridades y estados permitidos;
- cumplimiento del límite WIP;
- seis criterios literales de terminado;
- secciones operativas de planificación, validación y cierre.

El mismo contrato se ejecutará localmente y dentro del workflow existente de
GitHub Actions.

## Alternativas consideradas

### Checklist exclusivamente manual

Descartada porque no impide estados inválidos, elementos ausentes ni un
incumplimiento del límite WIP.

### Adoptar Jira o una herramienta externa

Pospuesta. GitHub Issues, Git y Markdown cubren el alcance actual sin añadir
cuentas, coste, sincronización ni administración adicional.

### Representar el backlog mediante JSON o YAML

Pospuesta. Un formato estructurado facilitaría validaciones más profundas, pero
reduciría la lectura humana y duplicaría la información durante esta fase.

### Validación semántica mediante IA

Pospuesta porque no ofrece por sí sola una señal determinista y reproducible.

## Consecuencias

### Positivas

- El backlog deja de ser una lista informal.
- El límite WIP produce una condición comprobable.
- Los estados y prioridades inválidos generan un fallo.
- La DoD conserva un núcleo mínimo común.
- El contrato funciona sin dependencias externas.
- La CI utiliza las mismas reglas que la ejecución local.

### Negativas

- Las reglas dependen parcialmente de marcadores textuales.
- Modificar la estructura exige actualizar código y pruebas.
- El gate no puede decidir si la prioridad empresarial es correcta.
- La revisión humana sigue siendo necesaria.

## Trade-off aceptado

Se acepta una estructura Markdown validada mediante reglas explícitas. Es menos
flexible que una revisión completamente manual, pero aporta una señal binaria,
bajo coste y trazabilidad sin introducir una plataforma adicional.

## Criterio de revisión

Revisar esta decisión cuando:

- el backlog necesite relaciones o consultas que Markdown no pueda mantener;
- aparezcan falsos positivos o negativos repetidos;
- el coste de mantener las reglas supere su utilidad;
- se necesite una CLI que genere o actualice el contrato;
- exista evidencia suficiente para adoptar un formato estructurado.

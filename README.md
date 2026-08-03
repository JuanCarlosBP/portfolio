# Portfolio de desarrollo de software

Soy **Juan Carlos Bohórquez Plato**, Técnico Superior en Desarrollo de
Aplicaciones Multiplataforma y desarrollador de software junior, orientado
principalmente a **backend, análisis de datos e inteligencia artificial aplicada
al desarrollo**.

Este repositorio reúne proyectos construidos como incrementos pequeños,
trazables y verificables. El objetivo no es únicamente mostrar resultados
finales, sino conservar evidencias sobre cómo se planifica, implementa, prueba,
documenta y entrega cada cambio.

## Proyecto disponible

### EngineeringOS

Sistema personal de ingeniería diseñado para convertir el desarrollo del
portfolio en un proceso reproducible y auditable.

EngineeringOS conecta:

```text
Problema
   ↓
Issue y backlog
   ↓
Rama de trabajo
   ↓
Cambio atómico
   ↓
Pruebas y quality gates
   ↓
Pull request
   ↓
Integración continua
   ↓
Entrega y evidencia verificables
```

**Estado actual:** W01D04 · recuperación de contexto y gate ejecutable implementados.

## Evolución verificable

### W01D01 · Discovery inicial

El primer incremento estableció la base de EngineeringOS:

- problema, usuarios, proceso actual y métricas de éxito;
- issue, rama y commits trazables;
- 4/4 pruebas automáticas;
- quality gate de discovery con 40/40 comprobaciones;
- integración continua mediante GitHub Actions;
- decisión técnica documentada mediante ADR;
- evidencia de validación reproducible.

Evidencias principales:

- [Issue #1 · Discovery inicial](https://github.com/JuanCarlosBP/portfolio/issues/1)
- [Pull request #2 · Quality gate, pruebas y CI](https://github.com/JuanCarlosBP/portfolio/pull/2)
- [CI de W01D01](https://github.com/JuanCarlosBP/portfolio/actions/runs/30136387462)
- [ADR-0001](projects/engineeringos/docs/adr/ADR-0001-executable-discovery-gate.md)
- [Evidencia W01D01](projects/engineeringos/docs/evidence/w01d01-validation.md)

### W01D02 · Backlog y Definition of Done

El segundo incremento amplió la base sin sustituirla:

- backlog priorizado con diez elementos operativos;
- política de prioridades `P0` a `P3`;
- flujo explícito de estados;
- límite WIP de un elemento activo;
- Definition of Done reutilizable;
- validador ejecutable del contrato de planificación;
- seis pruebas nuevas del contrato;
- 10/10 pruebas automáticas totales;
- quality gate de discovery: 40/40;
- quality gate de planificación: 39/39;
- ADR-0002 con alternativas, consecuencias y trade-off;
- dos commits AM y PM conservados en el historial de `main`;
- pull request y CI verificadas.

Evidencias principales:

- [Issue #8 · Backlog y Definition of Done](https://github.com/JuanCarlosBP/portfolio/issues/8)
- [Pull request #9](https://github.com/JuanCarlosBP/portfolio/pull/9)
- [CI de W01D02 sobre main](https://github.com/JuanCarlosBP/portfolio/actions/runs/30586377704)
- [Backlog priorizado](projects/engineeringos/docs/planning/backlog.md)
- [Definition of Done](projects/engineeringos/docs/standards/definition-of-done.md)
- [Validador de planificación](projects/engineeringos/tools/validate_planning.py)
- [Pruebas del contrato](projects/engineeringos/tests/test_validate_planning.py)
- [ADR-0002](projects/engineeringos/docs/adr/ADR-0002-executable-planning-contract.md)
- [Evidencia W01D02](projects/engineeringos/docs/evidence/w01d02-validation.md)

### W01D03 · Plantilla reutilizable de evidencia

El tercer incremento incorpora un contrato común para conservar evidencia:

- plantilla canónica con hechos, objetivos, comandos, métricas y riesgos;
- separación explícita entre resultados observados y objetivos pendientes;
- validador ejecutable con 46 comprobaciones;
- once pruebas nuevas de casos correctos y fallos relevantes;
- 21/21 pruebas automáticas totales;
- quality gate de discovery: 40/40;
- quality gate de planificación: 39/39;
- quality gate de evidencia: 46/46;
- integración del nuevo gate en GitHub Actions;
- actualización del backlog y de la Definition of Done;
- revisión de todos los README afectados.

La evidencia distingue la validación local del cierre remoto; la trazabilidad
definitiva de PR, CI e integración se conserva en GitHub.

Evidencias principales:

- [Issue #12 · Plantilla reutilizable de evidencia](https://github.com/JuanCarlosBP/portfolio/issues/12)
- [Commit AM](https://github.com/JuanCarlosBP/portfolio/commit/376d9263e4b2a91f2e10e9f4ae87c4ca86e2b50d)
- [Plantilla de evidencia](projects/engineeringos/docs/templates/increment-evidence-template.md)
- [Validador de evidencia](projects/engineeringos/tools/validate_evidence.py)
- [Pruebas del contrato](projects/engineeringos/tests/test_validate_evidence.py)
- [Evidencia W01D03](projects/engineeringos/docs/evidence/w01d03-validation.md)

### W01D04 · Recuperación de contexto

El cuarto incremento incorpora:

- estado canónico versionado;
- ejercicio autónomo completado en 83 segundos;
- 5/5 campos recuperados y 0 contradicciones;
- nueve pruebas nuevas y 30/30 pruebas totales;
- gate de recuperación con 36/36 comprobaciones;
- integración del gate en GitHub Actions;
- actualización del backlog, DoD y documentación afectada.

Evidencias principales:

- [Issue #14](https://github.com/JuanCarlosBP/portfolio/issues/14)
- [Estado canónico](projects/engineeringos/docs/state/current-state.md)
- [Validador](projects/engineeringos/tools/validate_context_recovery.py)
- [Pruebas](projects/engineeringos/tests/test_validate_context_recovery.py)
- [Evidencia W01D04](projects/engineeringos/docs/evidence/w01d04-context-recovery.md)

## Acceso al proyecto

- [README de EngineeringOS](projects/engineeringos/README.md)
- [Código y documentación de EngineeringOS](projects/engineeringos)
- [Historial de cambios](projects/engineeringos/CHANGELOG.md)

## Capacidades demostradas actualmente

Las siguientes capacidades cuentan con código, documentación o evidencias
revisables dentro del repositorio:

- Python.
- Pruebas automáticas con `unittest`.
- Git y GitHub.
- Issues, ramas, commits y pull requests.
- Integración continua con GitHub Actions.
- Automatización mediante Bash.
- Documentación técnica en Markdown.
- Configuración de workflows en YAML.
- Quality gates y códigos de salida.
- Backlog priorizado.
- Políticas de prioridad y estados.
- Límites de trabajo en curso.
- Definition of Done reutilizable.
- Plantillas reutilizables de evidencia.
- Validación ejecutable de evidencias documentales.
- Clasificación de métricas observadas, objetivo y no medidas.
- Validación de contratos documentales mediante código.
- Trazabilidad entre requisito, cambio, prueba y entrega.
- Registro de decisiones mediante ADR.
- Diagnóstico y recuperación segura ante errores.

## Tecnologías en desarrollo

Mi ruta profesional continúa ampliándose hacia:

- Java y Spring Boot.
- SQL y diseño de bases de datos.
- APIs REST.
- Backend con Python.
- Análisis de datos.
- Docker y CI/CD.
- Inteligencia artificial y LLM aplicados al desarrollo.

Estas tecnologías forman parte de la ruta de aprendizaje y de los próximos
proyectos. No se presentan aquí como capacidades ya demostradas mientras no
exista una evidencia técnica revisable.

## Principios de trabajo

- No considerar terminado un incremento sin criterios de aceptación.
- Separar planificación, implementación, validación y entrega.
- Mantener commits pequeños y con una finalidad reconocible.
- Probar también los casos de fallo, no solo el caso correcto.
- Documentar las decisiones que necesiten contexto.
- Automatizar comprobaciones repetitivas cuando aporten una señal útil.
- Reconocer las limitaciones de cada validación.
- Mantener siempre la revisión y la responsabilidad humanas.
- Revisar y actualizar todos los archivos `README.md` afectados antes de cerrar
  cada incremento.

## Siguiente incremento

El siguiente paso priorizado de EngineeringOS es **EOS-006**:

- definir cuándo una decisión técnica exige ADR;
- distinguir decisiones triviales de decisiones arquitectónicas;
- conservar contexto, alternativas, consecuencias y criterio de revisión;
- evitar documentación innecesaria.

## Perfil profesional

- **Ubicación:** Sevilla, España.
- **Modalidad:** presencial, híbrida o remota.
- **Objetivo:** primera oportunidad profesional en desarrollo de software,
  backend o datos.
- **GitHub:** [JuanCarlosBP](https://github.com/JuanCarlosBP)
- **Portfolio:** [jcbpsoftware.com](https://jcbpsoftware.com/)

---

Este portfolio está en evolución. Cada capacidad nueva se incorporará cuando
exista una evidencia que pueda revisarse, ejecutarse y explicarse.

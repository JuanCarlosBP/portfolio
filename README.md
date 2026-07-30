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

**Estado actual:** W01D02 completado y validado.

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

El siguiente paso priorizado de EngineeringOS es **EOS-004**:

- crear una plantilla reutilizable de evidencia;
- reducir duplicación entre incrementos;
- conservar comandos, resultados, métricas, riesgos, límites y siguiente acción.

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

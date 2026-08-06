# EngineeringOS

Sistema operativo personal de ingeniería para convertir el trabajo del portfolio
en incrementos trazables, verificables y revisables.

## Estado

W01D05 · Política de decisiones técnicas es el último incremento integrado y verificado.

EngineeringOS dispone actualmente de:

- discovery inicial;
- backlog priorizado;
- política de prioridad;
- flujo de estados;
- límite WIP;
- Definition of Done reutilizable;
- validadores ejecutables;
- pruebas automáticas;
- CI mediante GitHub Actions.
- plantilla reutilizable de evidencia;
- validador ejecutable del contrato de evidencia;
- pruebas negativas de estructura y contenido mínimo;
- política proporcional de decisiones técnicas;
- plantillas de ADR y nota local;
- gate de decisiones con 44 comprobaciones;
- ejercicio reproducible de clasificación.

La CLI general y el proceso completo de release permanecen fuera del alcance actual.

## Trazabilidad de W01D02

- Issue: [#8 · Backlog y Definition of Done](https://github.com/JuanCarlosBP/portfolio/issues/8)
- Rama: `docs/p01-w01d02-backlog-dod`
- Incremento AM: `docs(w0012am): discovery engineeringos`
- Incremento PM: `test(w0012pm): discovery engineeringos`
- Backlog: [`docs/planning/backlog.md`](docs/planning/backlog.md)
- Definition of Done:
  [`docs/standards/definition-of-done.md`](docs/standards/definition-of-done.md)
- Decisión:
  [`ADR-0002`](docs/adr/ADR-0002-executable-planning-contract.md)
- Evidencia:
  [`w01d02-validation.md`](docs/evidence/w01d02-validation.md)

## Trazabilidad de W01D03

- Issue: [#12 · Plantilla reutilizable de evidencia](https://github.com/JuanCarlosBP/portfolio/issues/12)
- Rama: `docs/p01-w01d03-evidence-template`
- Incremento AM: `docs(w0013am): discovery engineeringos`
- Incremento PM previsto: `test(w0013pm): discovery engineeringos`
- Plantilla:
  [`increment-evidence-template.md`](docs/templates/increment-evidence-template.md)
- Validador:
  [`validate_evidence.py`](tools/validate_evidence.py)
- Pruebas:
  [`test_validate_evidence.py`](tests/test_validate_evidence.py)
- Evidencia:
  [`w01d03-validation.md`](docs/evidence/w01d03-validation.md)

La PR, la CI y la integración se registran como hechos después de verificarse.

## Trazabilidad de W01D04

- Issue: [#14 · Recuperación de contexto](https://github.com/JuanCarlosBP/portfolio/issues/14)
- Rama: `docs/p01-w01d04-context-recovery`
- Incremento AM: `docs(w0014am): discovery engineeringos`
- Incremento PM previsto: `test(w0014pm): discovery engineeringos`
- Estado canónico: [`current-state.md`](docs/state/current-state.md)
- Validador: [`validate_context_recovery.py`](tools/validate_context_recovery.py)
- Pruebas: [`test_validate_context_recovery.py`](tests/test_validate_context_recovery.py)
- Evidencia: [`w01d04-context-recovery.md`](docs/evidence/w01d04-context-recovery.md)
- Resultado humano: 5/5 campos, 0 contradicciones y 83 segundos.

La PR, la CI y la integración se registrarán después de verificar sus SHA.

## Trazabilidad de W01D05

- Issue: [#16 · Política de decisiones técnicas](https://github.com/JuanCarlosBP/portfolio/issues/16)
- Rama: `docs/p01-w01d05-technical-decision-policy`
- Commit AM:
  `86f5f9006e07e02d811332feb2b1bba43e8dcd6f`
- Commit PM: `a0aa18fcf6df27adec955250b3f0e6fa9f8ebaea`
- Pull request: [#17](https://github.com/JuanCarlosBP/portfolio/pull/17)
- Commit de integración: `6e6657833043638a823f8677eca32107cd5512c6`
- CI de la PR: run `31055354496` · `success`
- CI de `main`: run `31056205331` · `success`
- Política:
  [`technical-decision-policy.md`](docs/standards/technical-decision-policy.md)
- Plantilla ADR:
  [`adr-template.md`](docs/templates/adr-template.md)
- Plantilla local:
  [`local-decision-note-template.md`](docs/templates/local-decision-note-template.md)
- ADR:
  [`ADR-0003`](docs/adr/ADR-0003-technical-decision-policy.md)
- Nota local:
  [`w01d05-reuse-existing-workflow.md`](docs/decisions/local/w01d05-reuse-existing-workflow.md)
- Ejercicio:
  [`w01d05-decision-classification-exercise.md`](docs/evidence/w01d05-decision-classification-exercise.md)
- Validador:
  [`validate_decision_policy.py`](tools/validate_decision_policy.py)
- Pruebas:
  [`test_validate_decision_policy.py`](tests/test_validate_decision_policy.py)
- Evidencia:
  [`w01d05-technical-decision-policy.md`](docs/evidence/w01d05-technical-decision-policy.md)
- Resultado local: 40/40 pruebas, 44/44 comprobaciones,
  12/12 escenarios y 0 contradicciones.

La PR fue integrada mediante squash, la issue #16 quedó cerrada con
22/22 criterios y la rama de trabajo fue eliminada local y remotamente.

## Contratos ejecutables

### Discovery

El gate de W01D01 ejecuta 40 comprobaciones sobre cuatro documentos:

- metadatos comunes;
- secciones obligatorias;
- estado validado;
- enlace uniforme con la issue #1.

### Planificación y terminado

El gate de W01D02 ejecuta 39 comprobaciones sobre:

- backlog y Definition of Done existentes;
- trazabilidad con la issue #8;
- diez elementos EOS ordenados;
- prioridades permitidas;
- estados permitidos;
- límite WIP;
- seis criterios obligatorios de terminado;
- secciones operativas de cierre y evidencia.

Los gates verifican estructura y reglas deterministas. No sustituyen la revisión
humana de la calidad semántica, la prioridad empresarial o la utilidad real.

### Evidencia reutilizable

El gate de W01D03 ejecuta 46 comprobaciones sobre:

- estructura y placeholders de la plantilla;
- metadatos trazables de la evidencia real;
- separación entre hechos observados y objetivos;
- comandos y códigos de salida;
- clases y fuentes de métricas;
- riesgos, limitaciones e impacto documental;
- enlaces canónicos sin duplicación;
- revisión de los dos README afectados.

### Recuperación de contexto

El gate de W01D04 superó 36/36 comprobaciones sobre:

- existencia de las fuentes canónicas;
- metadatos y trazabilidad del incremento;
- resultado autónomo del ejercicio;
- cinco campos recuperados;
- tiempo inferior a 600 segundos;
- ausencia de contradicciones;
- coherencia entre estado, backlog, README, DoD y workflow.

El ejercicio observado recuperó 5/5 campos en 83 segundos, sin red,
fuentes externas ni ayuda durante la medición.

### Política de decisiones técnicas

El gate de W01D05 ejecuta 44 comprobaciones sobre:

- política y secciones canónicas;
- tres niveles de clasificación;
- precedencia y algoritmo;
- desencadenantes ADR;
- reglas locales;
- casos triviales;
- plantillas;
- ADR-0003;
- nota local real;
- coherencia entre backlog y estado.

El ejercicio contiene doce escenarios: cuatro ADR, cuatro notas locales y
cuatro cambios sin registro adicional. Se observaron 12/12 coincidencias,
0 contradicciones y 0 grupos de reglas inválidos.

La materialidad y la calidad semántica continúan requiriendo revisión humana.

## Ejecución local

Desde la raíz del repositorio:

```bash
python -m unittest discover \
  -s projects/engineeringos/tests \
  -p "test_*.py" \
  -v

python projects/engineeringos/tools/validate_discovery.py

python projects/engineeringos/tools/validate_planning.py

python projects/engineeringos/tools/validate_evidence.py

python projects/engineeringos/tools/validate_context_recovery.py

python projects/engineeringos/tools/validate_decision_policy.py
```

No se requieren dependencias externas. El código utiliza la biblioteca estándar
de Python.

## Estructura actual

```text
projects/engineeringos/
├── CHANGELOG.md
├── README.md
├── docs/
│   ├── adr/
│   │   ├── ADR-0001-executable-discovery-gate.md
│   │   ├── ADR-0002-executable-planning-contract.md
│   │   └── ADR-0003-technical-decision-policy.md
│   ├── decisions/
│   │   └── local/
│   │       └── w01d05-reuse-existing-workflow.md
│   ├── discovery/
│   ├── evidence/
│   │   ├── w01d01-validation.md
│   │   ├── w01d02-validation.md
│   │   ├── w01d03-validation.md
│   │   ├── w01d04-context-recovery.md
│   │   ├── w01d05-decision-classification-exercise.md
│   │   └── w01d05-technical-decision-policy.md
│   ├── planning/
│   │   └── backlog.md
│   ├── standards/
│   │   ├── definition-of-done.md
│   │   └── technical-decision-policy.md
│   ├── state/
│   │   └── current-state.md
│   └── templates/
│       ├── adr-template.md
│       ├── increment-evidence-template.md
│       └── local-decision-note-template.md
├── tests/
│   ├── test_validate_context_recovery.py
│   ├── test_validate_decision_policy.py
│   ├── test_validate_discovery.py
│   ├── test_validate_evidence.py
│   └── test_validate_planning.py
└── tools/
    ├── validate_context_recovery.py
    ├── validate_decision_policy.py
    ├── validate_discovery.py
    ├── validate_evidence.py
    └── validate_planning.py
```

## Decisiones principales

- [`ADR-0001`](docs/adr/ADR-0001-executable-discovery-gate.md):
  validación ejecutable del discovery.
- [`ADR-0002`](docs/adr/ADR-0002-executable-planning-contract.md):
  validación ejecutable del backlog, WIP y Definition of Done.
- [`ADR-0003`](docs/adr/ADR-0003-technical-decision-policy.md):
  política proporcional para ADR, notas locales y cambios sin registro adicional.

## Limitaciones actuales

- La calidad semántica requiere revisión humana.
- El backlog se mantiene manualmente.
- El validador depende de un contrato textual estable.
- La CI no demuestra por sí sola que el resultado aporte valor empresarial.
- La plantilla requiere cumplimentación deliberada y revisión humana.
- El gate valida estructura mínima, no veracidad semántica completa.
- La CLI general de EngineeringOS todavía no está implementada.

## Siguiente acción

Mantener W01D05 cerrado y preparar, sin iniciarlo todavía, el incremento
**EOS-007 · Medición de carga administrativa** correspondiente a W01D06.

# EngineeringOS

Sistema operativo personal de ingeniería para convertir el trabajo del portfolio
en incrementos trazables, verificables y revisables.

## Estado

W01D03 · Contrato reutilizable de evidencia implementado.

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
- pruebas negativas de estructura y contenido mínimo.

La CLI general, la recuperación cronometrada de contexto y el proceso completo de
release permanecen fuera del alcance actual.

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
│   │   └── ADR-0002-executable-planning-contract.md
│   ├── discovery/
│   │   ├── current-process.md
│   │   ├── problem-statement.md
│   │   ├── success-metrics.md
│   │   └── users-and-needs.md
│   ├── evidence/
│   │   ├── w01d01-validation.md
│   │   ├── w01d02-validation.md
│   │   └── w01d03-validation.md
│   ├── planning/
│   │   └── backlog.md
│   ├── standards/
│   │   └── definition-of-done.md
│   └── templates/
│       └── increment-evidence-template.md
├── tests/
│   ├── test_validate_discovery.py
│   ├── test_validate_evidence.py
│   └── test_validate_planning.py
└── tools/
    ├── validate_discovery.py
    ├── validate_evidence.py
    └── validate_planning.py
```

## Decisiones principales

- [`ADR-0001`](docs/adr/ADR-0001-executable-discovery-gate.md):
  validación ejecutable del discovery.
- [`ADR-0002`](docs/adr/ADR-0002-executable-planning-contract.md):
  validación ejecutable del backlog, WIP y Definition of Done.

## Limitaciones actuales

- La calidad semántica requiere revisión humana.
- El backlog se mantiene manualmente.
- El validador depende de un contrato textual estable.
- La CI no demuestra por sí sola que el resultado aporte valor empresarial.
- La plantilla requiere cumplimentación deliberada y revisión humana.
- El gate valida estructura mínima, no veracidad semántica completa.
- La CLI general de EngineeringOS todavía no está implementada.

## Siguiente acción

EOS-005: ejecutar una recuperación real de contexto usando solo el repositorio,
registrar el tiempo utilizado y comprobar que objetivo, estado, decisiones,
bloqueos y siguiente acción pueden reconstruirse en diez minutos o menos.

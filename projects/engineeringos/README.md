# EngineeringOS

Sistema operativo personal de ingeniería para convertir el trabajo del portfolio
en incrementos trazables, verificables y revisables.

## Estado

W01D02 · Contrato de planificación y terminado validado.

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

La CLI general, la plantilla reutilizable de evidencia y el proceso completo de
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

## Ejecución local

Desde la raíz del repositorio:

```bash
python -m unittest discover \
  -s projects/engineeringos/tests \
  -p "test_*.py" \
  -v

python projects/engineeringos/tools/validate_discovery.py

python projects/engineeringos/tools/validate_planning.py
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
│   │   └── w01d02-validation.md
│   ├── planning/
│   │   └── backlog.md
│   └── standards/
│       └── definition-of-done.md
├── tests/
│   ├── test_validate_discovery.py
│   └── test_validate_planning.py
└── tools/
    ├── validate_discovery.py
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
- La CLI general de EngineeringOS todavía no está implementada.

## Siguiente acción

EOS-004: crear una plantilla reutilizable de evidencia que reduzca duplicación y
conserve comandos, resultados, métricas, riesgos, límites y siguiente acción.

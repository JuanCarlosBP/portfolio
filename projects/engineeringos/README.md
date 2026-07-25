# EngineeringOS

Sistema operativo personal de ingeniería para convertir el trabajo del portfolio
en incrementos trazables, verificables y revisables.

## Estado

W01D01 · Discovery inicial validado.

La primera entrega conecta problema, usuarios, proceso actual, métricas, issue,
rama, commits, pruebas, evidencia y CI. No implementa todavía la CLI completa ni
el resto del flujo de EngineeringOS.

## Trazabilidad de W01D01

- Issue: [#1 · Discovery inicial de EngineeringOS](https://github.com/JuanCarlosBP/portfolio/issues/1)
- Rama: `docs/p01-w01d01-engineeringos-discovery`
- Incremento AM: documentación inicial del discovery.
- Incremento PM: quality gate ejecutable, pruebas, métrica, ADR, evidencia y CI.

## Qué se valida

El quality gate comprueba un contrato mínimo de 40 condiciones:

- Cuatro documentos obligatorios.
- Cinco metadatos comunes por documento.
- Cinco secciones específicas por documento.
- Estado explícito `Validado en W01D01`.
- Enlace uniforme a la issue de origen.

Este control no intenta decidir si toda la investigación es correcta. Su función
es impedir que el incremento se cierre con documentos ausentes, sin trazabilidad,
en borrador o sin las secciones mínimas acordadas.

## Ejecución local

Desde la raíz del repositorio:

```bash
python -m unittest discover \
  -s projects/engineeringos/tests \
  -p "test_*.py" \
  -v

python projects/engineeringos/tools/validate_discovery.py
```

Resultado esperado:

```text
EngineeringOS discovery quality gate
Checks: 40/40 passed
Result: PASS
```

No se requieren dependencias externas: las pruebas y el validador utilizan
exclusivamente la biblioteca estándar de Python.

## Estructura actual

```text
projects/engineeringos/
├── CHANGELOG.md
├── README.md
├── docs/
│   ├── adr/
│   │   └── ADR-0001-executable-discovery-gate.md
│   ├── discovery/
│   │   ├── current-process.md
│   │   ├── problem-statement.md
│   │   ├── success-metrics.md
│   │   └── users-and-needs.md
│   └── evidence/
│       └── w01d01-validation.md
├── tests/
│   └── test_validate_discovery.py
└── tools/
    └── validate_discovery.py
```

## Decisión principal

Se eligió una validación pequeña, local y ejecutable antes que añadir más
documentación manual o contratar una herramienta externa. La decisión y sus
límites están registrados en
[`ADR-0001`](docs/adr/ADR-0001-executable-discovery-gate.md).

## Límite actual

La validación es estructural: confirma presencia, trazabilidad y estado, pero no
evalúa automáticamente la calidad semántica de las conclusiones. La revisión
humana sigue siendo necesaria.

## Siguiente acción

W01D02: transformar los hallazgos del discovery en backlog priorizado y una
Definition of Done reutilizable, manteniendo el mismo vínculo entre issue,
incremento, validación y evidencia.

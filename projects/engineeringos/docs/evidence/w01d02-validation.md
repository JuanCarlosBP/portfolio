# Evidencia de validación · W01D02

**Proyecto:** EngineeringOS

**Fecha de ejecución:** 2026-07-30

**Issue:** [#8](https://github.com/JuanCarlosBP/portfolio/issues/8)

**Rama:** `docs/p01-w01d02-backlog-dod`

**Commit AM:** `5da6ca0ffeda20499c742ba9586c3fc3c67b768c`

**Commit PM previsto:** `test(w0012pm): discovery engineeringos`

**Resultado local:** Superado

## Riesgo principal probado

> Crear documentación extensa que no cambie la forma real de trabajar.

La mitigación se prueba mediante un contrato ejecutable que falla cuando:

- falta el backlog;
- falta una sección obligatoria;
- se utiliza una prioridad inválida;
- existen varios elementos activos y se incumple el WIP;
- falta un criterio obligatorio de la Definition of Done.

## Comandos reproducibles

Ejecutados desde la raíz del repositorio:

```bash
python -m unittest discover \
  -s projects/engineeringos/tests \
  -p "test_*.py" \
  -v

python projects/engineeringos/tools/validate_discovery.py

python projects/engineeringos/tools/validate_planning.py
```

## Resultado de las pruebas

```text
Ran 10 tests
OK
```

Las diez pruebas corresponden a:

- cuatro pruebas del contrato de discovery;
- seis pruebas del contrato de planificación y terminado.

## Resultado de los quality gates

```text
EngineeringOS discovery quality gate
Checks: 40/40 passed
Result: PASS

EngineeringOS planning quality gate
Checks: 39/39 passed
Result: PASS
```

## Señales medidas

| Señal | Resultado | Cálculo | Interpretación |
|---|---:|---|---|
| Pruebas automáticas superadas | 100 % | 10 / 10 | Los casos válidos y fallos principales están cubiertos. |
| Contrato de discovery | 100 % | 40 / 40 | W01D01 continúa cumpliendo su contrato. |
| Contrato de planificación | 100 % | 39 / 39 | Backlog, WIP, estados y DoD cumplen las reglas definidas. |
| Criterios obligatorios de DoD | 100 % | 6 / 6 | El núcleo literal de la ruta está presente. |
| Elementos priorizados | 100 % | 10 / 10 | El backlog contiene EOS-001 a EOS-010 en orden. |

Estos valores miden estructura, trazabilidad y comportamiento del gate. No
demuestran por sí solos que la prioridad empresarial sea óptima ni que el
contenido tenga calidad semántica completa.

## Trazabilidad

- Problema y criterios: issue #8.
- Incremento AM: backlog y Definition of Done.
- Incremento PM: validador, pruebas, CI, ADR, README, changelog y evidencia.
- Validación remota: workflow `EngineeringOS discovery quality`.
- Evidencia canónica de CI: GitHub Actions y la issue #8.
- Entrega: pull request desde la rama de W01D02 contra `main`.

## Decisión y alternativas

Se eligió mantener Markdown como formato legible y añadir un gate determinista
en Python. Se descartó depender exclusivamente de una checklist manual y se
pospusieron Jira, formatos estructurados e IA semántica.

El detalle se conserva en
[`ADR-0002`](../adr/ADR-0002-executable-planning-contract.md).

## Limitaciones

- El gate no decide si una prioridad empresarial es correcta.
- La presencia de una sección no garantiza calidad semántica.
- El backlog todavía se actualiza manualmente.
- La revisión humana continúa siendo obligatoria.

## Siguiente acción

EOS-004: crear una plantilla reutilizable de evidencia que reduzca duplicación
y conserve los resultados relevantes de cada incremento.

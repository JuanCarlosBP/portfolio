# Evidencia de validación · W01D01

**Proyecto:** EngineeringOS

**Fecha de ejecución:** 2026-07-25

**Issue:** [#1](https://github.com/JuanCarlosBP/portfolio/issues/1)

**Rama:** `docs/p01-w01d01-engineeringos-discovery`

**Resultado local:** Superado

## Riesgo probado

> Convertir EngineeringOS en documentación extensa sin comportamiento
> verificable ni utilidad práctica.

La prueba consiste en un contrato ejecutable que falla si falta un documento,
una sección obligatoria, la trazabilidad común o el estado validado.

## Comandos reproducibles

Ejecutados desde la raíz del repositorio:

```bash
python -m unittest discover \
  -s projects/engineeringos/tests \
  -p "test_*.py" \
  -v

python projects/engineeringos/tools/validate_discovery.py
```

## Resultado de las pruebas

```text
test_complete_discovery_passes_all_40_checks ... ok
test_draft_status_cannot_pass_the_gate ... ok
test_missing_document_fails_its_10_checks ... ok
test_missing_required_section_is_detected ... ok

Ran 4 tests
OK
```

## Resultado del quality gate

```text
EngineeringOS discovery quality gate
Checks: 40/40 passed
Result: PASS
```

## Señal medida

| Señal | Resultado | Cálculo | Interpretación |
|---|---:|---|---|
| Cumplimiento del contrato de discovery | 100 % | 40 / 40 comprobaciones | Los cuatro documentos cumplen la estructura y trazabilidad acordadas. |
| Pruebas automáticas superadas | 100 % | 4 / 4 casos | El caso válido y tres fallos relevantes están cubiertos. |
| Documentos obligatorios presentes | 100 % | 4 / 4 documentos | No falta ningún entregable de discovery. |

Estos valores miden la completitud estructural del incremento. No demuestran por
sí solos la calidad semántica total ni una mejora de empleabilidad.

## Trazabilidad

- Problema y objetivo: issue #1.
- Incremento AM: commit inicial de documentación.
- Incremento PM: quality gate, tests, métrica, ADR, evidencia y CI.
- Validación remota: workflow `EngineeringOS discovery quality`.
- Entrega: pull request del bloque PM contra `main`.

## Decisión y alternativa descartada

Se eligió un gate local y determinista. Se descartó añadir únicamente otra
checklist manual porque no habría probado el riesgo principal. El detalle y el
trade-off están en
[`ADR-0001`](../adr/ADR-0001-executable-discovery-gate.md).

## Límite actual

El validador comprueba señales estructurales, no interpreta la calidad del
contenido. La revisión humana sigue siendo obligatoria.

## Siguiente acción

W01D02: crear el backlog priorizado y la Definition of Done reutilizable a
partir de los hallazgos de este discovery.

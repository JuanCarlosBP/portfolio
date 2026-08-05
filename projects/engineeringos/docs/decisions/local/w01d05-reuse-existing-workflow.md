# Nota local · Reutilización del workflow existente en W01D05

**Proyecto:** EngineeringOS

**Día o incremento:** W01D05 · EOS-006

**Fecha:** 2026-08-05

**Issue:** [#16](https://github.com/JuanCarlosBP/portfolio/issues/16)

**Rama:** `docs/p01-w01d05-technical-decision-policy`

**Estado:** En validación

## Contexto local

EngineeringOS ya dispone del workflow:

` .github/workflows/engineeringos-discovery.yml `

Ese workflow ejecuta los validadores de discovery, planificación, evidencia y
recuperación de contexto. W01D05 necesita añadir el validador de política de
decisiones técnicas.

La decisión de este incremento no consiste en rediseñar la estrategia de CI,
crear otro workflow ni introducir un proveedor nuevo. Solo determina si el
quinto gate debe incorporarse al workflow existente.

## Decisión

Reutilizar `engineeringos-discovery.yml` y añadir en el bloque PM un paso
adicional que ejecute:

`python3 projects/engineeringos/tools/validate_decision_policy.py`

No se creará un segundo workflow para W01D05.

## Motivo de clasificación

**Nivel elegido:** `LOCAL_NOTE`

La decisión no exige ADR porque:

- está limitada a la integración del gate de W01D05;
- no cambia el proveedor ni la arquitectura de CI;
- no introduce una dependencia o servicio;
- no cambia permisos, secretos ni tratamiento de datos;
- es reversible eliminando un único paso;
- no crea un contrato público nuevo;
- la estrategia general de CI permanece intacta.

**Reglas locales aplicables:**

- `LOCAL-01` · No aplica un desencadenante material de ADR.
- `LOCAL-02` · El alcance está limitado a un incremento.
- `LOCAL-03` · La reversión es sencilla y económica.
- `LOCAL-04` · No cambia contratos externos.
- `LOCAL-05` · No introduce dependencia, seguridad, privacidad ni coste.
- `LOCAL-06` · La explicación aclara por qué se modifica el workflow existente.

## Alcance y límites

### Incluido

- añadir un paso para el validador de política;
- conservar el mismo evento y entorno de ejecución;
- utilizar Python estándar;
- ejecutar el mismo comando localmente y en CI.

### Fuera de alcance

- crear otro workflow;
- modificar permisos;
- introducir matrices de versiones;
- añadir servicios externos;
- rediseñar la estrategia de CI;
- modificar los otros cuatro gates.

## Consecuencias

### Positivas

- La CI conserva un único punto de entrada.
- El quinto gate sigue el patrón de los validadores anteriores.
- No se duplica configuración.
- La reversión es directa.
- El coste operativo permanece sin cambios.

### Negativas o limitaciones

- El workflow seguirá acumulando pasos.
- Un crecimiento futuro podría justificar dividir responsabilidades.
- La decisión no resuelve la futura medición de tiempo de CI.

## Reversión

Para revertir la decisión basta con:

1. eliminar el paso de `validate_decision_policy.py`;
2. ejecutar los cuatro gates anteriores;
3. confirmar que el workflow continúa válido;
4. documentar la causa de la retirada en la evidencia.

No se requiere migración ni restauración de datos.

## Criterio de escalado

Esta nota debe convertirse en ADR cuando:

- se sustituya GitHub Actions;
- se creen varios workflows coordinados;
- cambien permisos o secretos;
- se introduzcan servicios externos;
- se modifique la arquitectura de entrega;
- la CI condicione varios proyectos;
- la reversión deje de ser local.

## Trazabilidad

| Elemento | Referencia |
|---|---|
| Issue | [#16](https://github.com/JuanCarlosBP/portfolio/issues/16) |
| Rama | `docs/p01-w01d05-technical-decision-policy` |
| Commit | Pendiente de creación |
| Pull request | Pendiente de creación |
| Workflow | `.github/workflows/engineeringos-discovery.yml` |
| Evidencia | `projects/engineeringos/docs/evidence/w01d05-technical-decision-policy.md` |

## Lista de comprobación

- [x] No aplica ningún desencadenante material de ADR.
- [x] El alcance está limitado.
- [x] La decisión es reversible.
- [x] No cambia contratos externos.
- [x] No introduce dependencia permanente.
- [x] No afecta a seguridad, privacidad o coste recurrente.
- [x] La explicación mejora la revisión o recuperación de contexto.
- [x] Existe una condición de escalado.
- [x] La trazabilidad está completa para el estado actual.
- [x] No quedan marcadores de plantilla sin resolver.

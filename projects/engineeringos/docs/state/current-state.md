# Estado actual de EngineeringOS

## Metadatos

| Campo | Valor |
|---|---|
| Proyecto | EngineeringOS |
| Día lógico | `W01D05` |
| Fecha de actualización | `2026-08-06` |
| Foco actual | `EOS-006 · Política de decisiones técnicas` |
| Estado del foco actual | `En validación` |
| Último elemento completado | `EOS-005 · Recuperación de contexto` |
| Issue activa | [#16](https://github.com/JuanCarlosBP/portfolio/issues/16) |
| Rama activa | `docs/p01-w01d05-technical-decision-policy` |
| Commit AM | `86f5f9006e07e02d811332feb2b1bba43e8dcd6f` |
| Commit PM | Pendiente |
| Pull request | Pendiente |
| CI del candidato PM | Pendiente |
| Integración en main | Pendiente |

## Objetivo actual

Completar la validación y entrega de una política proporcional que clasifique
decisiones técnicas como ADR, nota local o cambio sin registro adicional.

## Decisiones vigentes

- Mantener `WIP = 1`.
- Utilizar el repositorio como fuente canónica.
- Clasificar mediante `ADR`, `LOCAL_NOTE` y `NO_EXTRA_RECORD`.
- Aplicar `ADR > LOCAL_NOTE > NO_EXTRA_RECORD`.
- Exigir impacto material.
- Mantener Markdown como formato canónico.
- Utilizar la biblioteca estándar de Python.
- Conservar revisión humana.
- No terminar EOS-006 antes de verificar PR, CI y merge.

## Bloqueos

No se observan bloqueos activos.

Permanecen pendientes:

- commit PM;
- push definitivo;
- pull request;
- CI del SHA PM;
- integración;
- cierre de la issue.

## Trabajo observado en W01D05

- Base verificada:
  `2f59037191b5db2dd2a06eea214a185f1a4420f5`.
- Commit AM publicado:
  `86f5f9006e07e02d811332feb2b1bba43e8dcd6f`.
- Política y plantillas creadas.
- ADR-0003 y nota local real creados.
- Diez pruebas nuevas.
- 40/40 pruebas.
- Discovery: 40/40.
- Planificación: 39/39.
- Evidencia: 46/46.
- Contexto: 36/36.
- Decisiones: 44/44.
- Ejercicio: 12/12.
- Coincidencias: 12/12.
- Contradicciones: 0.
- S09 corregido.
- Candidato documental PM preparado.

## Siguiente acción operativa

Auditar las trece rutas PM, preparar exclusivamente esas rutas, revisar el
índice, crear el commit `test(w0015pm): discovery engineeringos` y publicar la
rama.

## Fuentes canónicas

| Ruta | Finalidad |
|---|---|
| `projects/engineeringos/docs/planning/backlog.md` | Estado de EOS-006. |
| `projects/engineeringos/docs/standards/technical-decision-policy.md` | Política. |
| `projects/engineeringos/docs/templates/adr-template.md` | Plantilla ADR. |
| `projects/engineeringos/docs/templates/local-decision-note-template.md` | Plantilla local. |
| `projects/engineeringos/docs/adr/ADR-0003-technical-decision-policy.md` | ADR real. |
| `projects/engineeringos/docs/decisions/local/w01d05-reuse-existing-workflow.md` | Nota local. |
| `projects/engineeringos/tools/validate_decision_policy.py` | Gate. |
| `projects/engineeringos/tests/test_validate_decision_policy.py` | Pruebas. |
| `projects/engineeringos/docs/evidence/w01d05-decision-classification-exercise.md` | Ejercicio. |
| `projects/engineeringos/docs/evidence/w01d05-technical-decision-policy.md` | Evidencia. |
| `.github/workflows/engineeringos-discovery.yml` | Cinco gates. |
| `README.md` | Estado público. |
| `projects/engineeringos/README.md` | Estado técnico. |

## Protocolo de recuperación

1. Abrir este archivo.
2. Recuperar objetivo, estado, decisiones, bloqueos y siguiente acción.
3. Confirmar cada dato mediante las rutas canónicas.
4. Distinguir working tree, staging, commit, rama remota, PR, CI y merge.
5. No presentar como integrado un cambio local.
6. Confirmar SHA y rama antes de operar.

## Regla de actualización

- Actualizar cuando cambien foco, estado, decisión, bloqueo o siguiente acción.
- Mantener coherencia con backlog y README.
- No declarar EOS-006 terminado antes de integrar y verificar.
- Conservar pendientes remotos de forma explícita.

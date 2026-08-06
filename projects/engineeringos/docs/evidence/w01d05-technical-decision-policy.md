# Evidencia de incremento · W01D05

## Metadatos

| Campo | Valor |
|---|---|
| Proyecto | EngineeringOS |
| Día de trabajo | W01D05 |
| Fecha de ejecución | 2026-08-05–2026-08-06 |
| Issue | [#16](https://github.com/JuanCarlosBP/portfolio/issues/16) |
| Rama | `docs/p01-w01d05-technical-decision-policy` |
| Commit AM | `86f5f9006e07e02d811332feb2b1bba43e8dcd6f` |
| Commit PM | `a0aa18fcf6df27adec955250b3f0e6fa9f8ebaea` |
| Estado | Terminado |
| Versión de la plantilla | `1.0.0` |

## Propósito

Definir una política proporcional para distinguir decisiones arquitectónicas,
decisiones locales y cambios triviales sin perder contexto técnico ni generar
documentación innecesaria.

## Alcance

### Incluido

- Política con `ADR`, `LOCAL_NOTE` y `NO_EXTRA_RECORD`.
- Plantillas de ADR y nota local.
- ADR-0003 y nota local real.
- Gate con 44 comprobaciones.
- Diez pruebas nuevas.
- Ejercicio de doce escenarios.
- Actualización del workflow, README, backlog, DoD, estado y changelog.

### Fuera de alcance

- EOS-007 a EOS-010.
- Servicios externos.
- Dependencias Python nuevas.
- Automatización de la decisión semántica.
- Declarar PR, CI o integración antes de observarlas.

## Hechos observados

- Base: `2f59037191b5db2dd2a06eea214a185f1a4420f5`.
- Commit AM: `86f5f9006e07e02d811332feb2b1bba43e8dcd6f`.
- Pruebas: 40/40.
- Gate de discovery: 40/40.
- Gate de planificación: 39/39.
- Gate de evidencia: 46/46.
- Gate de contexto: 36/36.
- Gate de decisiones: 44/44.
- Escenarios: 12/12.
- Distribución: 4 ADR, 4 notas locales y 4 cambios sin registro.
- Coincidencias: 12/12.
- Contradicciones: 0.
- Grupos de reglas inválidos: 0.
- La evidencia insuficiente de S09 fue corregida.
- Commit PM: `a0aa18fcf6df27adec955250b3f0e6fa9f8ebaea`.
- PR #17 integrada mediante squash.
- Commit de integración: `6e6657833043638a823f8677eca32107cd5512c6`.
- CI de la PR: run `31055354496` · `success`.
- CI de `main`: run `31056205331` · `success`.
- Issue #16 cerrada con 22/22 criterios.
- Rama local y remota eliminadas.

## Objetivos aún no verificados

- Ninguno dentro del alcance aprobado de W01D05.

## Comandos y resultados

| Orden | Comando | Código de salida | Resultado |
|---:|---|---:|---|
| 1 | `python3 -B -m unittest discover -s projects/engineeringos/tests -p 'test_*.py' -v` | 0 | 40/40 pruebas. |
| 2 | `python3 projects/engineeringos/tools/validate_discovery.py` | 0 | 40/40 comprobaciones. |
| 3 | `python3 projects/engineeringos/tools/validate_planning.py` | 0 | 39/39 comprobaciones. |
| 4 | `python3 projects/engineeringos/tools/validate_evidence.py` | 0 | 46/46 comprobaciones. |
| 5 | `python3 projects/engineeringos/tools/validate_context_recovery.py` | 0 | 36/36 comprobaciones. |
| 6 | `python3 projects/engineeringos/tools/validate_decision_policy.py` | 0 | 44/44 comprobaciones. |
| 7 | `python3 validate-classification-exercise.py` | 0 | 12/12 coincidencias. |
| 8 | `git diff --check` | 0 | Sin errores de formato. |

## Métricas

| Clase | Señal | Valor | Fuente | Interpretación |
|---|---|---|---|---|
| Observada | Pruebas | 40/40 | `unittest` | La suite local pasa. |
| Observada | Discovery | 40/40 | Gate | Contrato conservado. |
| Observada | Planificación | 39/39 | Gate | Backlog y DoD coherentes. |
| Observada | Evidencia | 46/46 | Gate | Contrato documental conservado. |
| Observada | Contexto | 36/36 | Gate | Transición de EOS-006 soportada. |
| Observada | Decisiones | 44/44 | Gate | Política estructuralmente válida. |
| Observada | Escenarios | 12/12 | Ejercicio | Corpus completo. |
| Observada | Coincidencias | 12/12 | Ejercicio | Resultado reproducible. |
| Observada | Contradicciones | 0 | Ejercicio | Sin discrepancias. |
| Observada | Grupos inválidos | 0 | Ejercicio | Sin mezcla de niveles. |
| Observada | CI del SHA PM | `success` | Run `31055354496` | El commit PM fue validado remotamente. |

## Decisión y trade-off

| Campo | Contenido |
|---|---|
| Decisión | Adoptar clasificación proporcional. |
| Alternativa descartada | Exigir ADR para todo. |
| Ventaja | Conserva contexto material. |
| Coste aceptado | Añade reglas, plantillas y gate. |
| Revisión | Revisar ante contradicciones o carga excesiva. |

## Riesgos y limitaciones

| Tipo | Descripción | Tratamiento | Estado |
|---|---|---|---|
| Limitación | El gate no evalúa toda la semántica. | Revisión humana. | Activa |
| Riesgo | Usar nota local para evitar ADR. | Precedencia ADR. | Mitigado |
| Riesgo | Crear ADR por palabras aisladas. | Exigir impacto material. | Mitigado |
| Resuelto | CI del commit PM. | Run `31055354496` verificado. | Cerrado |
| Resuelto | Integración en `main`. | Squash `6e6657833043638a823f8677eca32107cd5512c6` y run `31056205331` verificados. | Cerrado |

## Impacto documental

| Superficie | Acción |
|---|---|
| `README.md` | Actualizar. |
| `projects/engineeringos/README.md` | Actualizar. |
| Changelog | Actualizar. |
| Backlog | Pasar EOS-006 a `Terminado`. |
| DoD | Añadir clasificación de decisiones. |
| Workflow | Añadir quinto gate. |
| Estado canónico | Actualizar siguiente acción. |

## Trazabilidad y enlaces canónicos

| Elemento | Referencia |
|---|---|
| Issue | https://github.com/JuanCarlosBP/portfolio/issues/16 |
| Pull request | https://github.com/JuanCarlosBP/portfolio/pull/17 |
| CI de PR | Run `31055354496` · `success` |
| CI de main | Run `31056205331` · `success` |
| Integración en `main` | `6e6657833043638a823f8677eca32107cd5512c6` |
| Commit AM | `86f5f9006e07e02d811332feb2b1bba43e8dcd6f` |
| Commit PM | `a0aa18fcf6df27adec955250b3f0e6fa9f8ebaea` |
| Evidencia | `projects/engineeringos/docs/evidence/w01d05-technical-decision-policy.md` |

## Siguiente acción

Mantener W01D05 cerrado y preparar EOS-007 dentro de W01D06 sin considerar que
su mera aparición como siguiente elemento equivalga a haberlo iniciado.

## Reglas de uso

1. No presentar objetivos como hechos.
2. No declarar métricas sin fuente.
3. No afirmar CI verde antes de verificar el SHA.
4. No ocultar riesgos o pendientes.
5. Revisar todos los README afectados.
6. No declarar terminado EOS-006 antes del merge verificado.

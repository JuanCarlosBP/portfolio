# Estado actual de EngineeringOS

## Metadatos

| Campo | Valor |
|---|---|
| Proyecto | EngineeringOS |
| Día lógico | `W01D05` |
| Fecha de actualización | `2026-08-05` |
| Foco actual | `EOS-006 · Política de decisiones técnicas` |
| Estado del foco actual | `En curso` |
| Último elemento completado | `EOS-005 · Recuperación de contexto` |
| Issue activa | [#16](https://github.com/JuanCarlosBP/portfolio/issues/16) |
| Rama activa | `docs/p01-w01d05-technical-decision-policy` |

## Objetivo actual

Definir, probar e integrar una política proporcional que permita clasificar
decisiones técnicas como ADR, nota local o cambio sin registro adicional.

La política debe conservar contexto, alternativas, consecuencias, trade-off y
criterio de revisión cuando el impacto lo exija, sin producir documentación
innecesaria para cambios triviales.

## Decisiones vigentes

- Mantener un límite de trabajo en curso de un único elemento: `WIP = 1`.
- Utilizar el repositorio como fuente canónica del contexto.
- Clasificar decisiones mediante `ADR`, `LOCAL_NOTE` y `NO_EXTRA_RECORD`.
- Aplicar la precedencia `ADR > LOCAL_NOTE > NO_EXTRA_RECORD`.
- Exigir un efecto material y no una mera coincidencia terminológica.
- Mantener las decisiones en Markdown legible.
- Implementar validaciones deterministas con la biblioteca estándar de Python.
- Conservar revisión humana para materialidad, alternativas y consecuencias.
- Conservar evidencia verificable antes de declarar terminado un incremento.

## Bloqueos

No se observan bloqueos activos.

La issue #16 está abierta, la rama existe solo localmente y el bloque AM todavía
no se ha versionado ni publicado.

## Trabajo completado en W01D05

- Línea base verificada sobre
  `2f59037191b5db2dd2a06eea214a185f1a4420f5`.
- Cierre de W01D04 revalidado.
- Issue #16 creada y comprobada.
- Rama local creada desde la base exacta.
- Contrato de clasificación congelado.
- Política y plantillas construidas en un candidato temporal.
- ADR-0003 y nota local real preparados.

## Siguiente acción operativa

Auditar las siete rutas AM, preparar exclusivamente esas rutas, ejecutar las
pruebas y gates existentes, crear el commit AM y publicar la rama.

## Fuentes canónicas

| Ruta | Finalidad |
|---|---|
| `projects/engineeringos/docs/planning/backlog.md` | Prioridad, estado y criterios de EOS-006. |
| `projects/engineeringos/docs/standards/technical-decision-policy.md` | Política de clasificación. |
| `projects/engineeringos/docs/templates/adr-template.md` | Plantilla canónica de ADR. |
| `projects/engineeringos/docs/templates/local-decision-note-template.md` | Plantilla de nota local. |
| `projects/engineeringos/docs/adr/ADR-0003-technical-decision-policy.md` | Decisión de adopción de la política. |
| `projects/engineeringos/docs/decisions/local/w01d05-reuse-existing-workflow.md` | Caso local real. |
| `projects/engineeringos/docs/standards/definition-of-done.md` | Condiciones obligatorias de cierre. |
| `README.md` | Estado público y siguiente incremento. |
| `projects/engineeringos/README.md` | Estado técnico del proyecto. |

## Protocolo de recuperación

1. Abrir este archivo como punto de entrada.
2. Recuperar objetivo, estado, decisiones, bloqueos y siguiente acción.
3. Confirmar cada respuesta mediante las rutas enlazadas.
4. No sustituir el estado versionado por memoria o fuentes externas.
5. Confirmar la rama y el SHA antes de ejecutar una operación.
6. Verificar si el trabajo está solo local, publicado, en PR o integrado.

## Regla de actualización

- Actualizar este archivo cuando cambien foco, estado, decisión, bloqueo o
  siguiente acción.
- Realizar la actualización dentro del mismo incremento.
- No mantener un estado que contradiga el backlog o los README afectados.
- No declarar integrado un cambio que solo existe en el working tree.

# Estado actual de EngineeringOS

## Metadatos

| Campo | Valor |
|---|---|
| Proyecto | EngineeringOS |
| Día lógico | `W01D04` |
| Fecha de actualización | `2026-08-03` |
| Foco actual | `EOS-006 · Política de decisiones técnicas` |
| Estado del foco actual | `Pendiente` |
| Último elemento completado | `EOS-005 · Recuperación de contexto` |

## Objetivo actual

Definir cuándo una decisión técnica exige un ADR y cuándo basta una explicación
local, conservando contexto, alternativas, consecuencias y criterio de revisión
sin generar documentación innecesaria.

## Decisiones vigentes

- Mantener un límite de trabajo en curso de un único elemento: `WIP = 1`.
- Utilizar el repositorio como fuente canónica del contexto.
- Mantener este documento breve y enlazar fuentes en lugar de duplicarlas.
- Implementar validaciones deterministas con la biblioteca estándar de Python.
- Conservar evidencia verificable antes de declarar terminado un incremento.

## Bloqueos

No se observan bloqueos para preparar EOS-006. La PR, la CI y la integración de
W01D04 deben verificarse antes de iniciar su implementación.

## Siguiente acción operativa

Crear el commit PM de W01D04, publicar la rama, abrir la pull request, verificar
la CI, integrar el cambio y preparar la política de decisiones de EOS-006.

## Fuentes canónicas

| Ruta | Finalidad |
|---|---|
| `projects/engineeringos/docs/planning/backlog.md` | Prioridades, estados y siguiente incremento. |
| `projects/engineeringos/docs/standards/definition-of-done.md` | Condiciones obligatorias de cierre. |
| `projects/engineeringos/docs/evidence/w01d04-context-recovery.md` | Última evidencia candidata. |
| `README.md` | Estado público y siguiente incremento. |
| `projects/engineeringos/README.md` | Estado técnico del proyecto. |

## Protocolo de recuperación

1. Abrir este archivo como punto de entrada.
2. Recuperar objetivo, estado, decisión, bloqueos y siguiente acción.
3. Confirmar cada respuesta mediante las rutas enlazadas.
4. No sustituir el estado versionado por memoria o fuentes externas.

## Regla de actualización

- Actualizar este archivo cuando cambien foco, estado, decisión, bloqueo o siguiente acción.
- Realizar la actualización dentro del mismo incremento.
- No mantener un estado que contradiga el backlog o los README afectados.

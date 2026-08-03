# Backlog priorizado de EngineeringOS

**Proyecto:** EngineeringOS
**Fase:** Discovery y planificación inicial
**Día de trabajo:** W01D02
**Fecha de ejecución:** 2026-07-30
**Última actualización:** 2026-08-03
**Issue relacionada:** [#8](https://github.com/JuanCarlosBP/portfolio/issues/8)
**Rama:** `docs/p01-w01d02-backlog-dod`
**Estado:** Validado en W01D02

## Objetivo

Convertir los hallazgos del discovery de W01D01 en trabajo ordenado,
priorizado, limitado y verificable.

Este backlog no sustituye la ruta maestra. La traduce a incrementos operativos
de EngineeringOS y conserva la relación entre problema, prioridad, resultado,
criterios de aceptación, dependencias y evidencia.

## Fuentes utilizadas

Los elementos derivan de las evidencias validadas durante W01D01:

- `problem-statement.md`: pérdida de contexto, dificultad para priorizar y
  cierres sin evidencia suficiente.
- `current-process.md`: trazabilidad irregular, crecimiento de alcance y
  ausencia de una definición común de terminado.
- `users-and-needs.md`: necesidad de conocer el siguiente trabajo, limitarlo y
  conservar evidencias reproducibles.
- `success-metrics.md`: trazabilidad completa, DoD al 100 %, validación
  reproducible, alcance controlado y cero cierres incompletos.

## Política de prioridad

| Prioridad | Significado | Regla |
|---|---|---|
| `P0` | Bloqueante | Sin este elemento no puede cerrarse correctamente el siguiente incremento. |
| `P1` | Alta | Reduce un riesgo importante o mejora directamente el flujo diario. |
| `P2` | Media | Aporta valor, pero no bloquea el incremento inmediato. |
| `P3` | Aparcada | Idea fuera del horizonte actual o pendiente de nueva evidencia. |

Cuando dos elementos tengan la misma prioridad se ordenarán por:

1. Dependencias necesarias.
2. Reducción del riesgo principal.
3. Valor para el usuario principal.
4. Evidencia verificable que producirán.
5. Menor esfuerzo compatible con un resultado completo.

No se priorizará por cantidad de archivos, líneas, documentos o commits.

## Flujo de estados

```text
Pendiente
   ↓
Preparado
   ↓
En curso
   ↓
En validación
   ↓
Terminado
```

También puede utilizarse el estado `Bloqueado`.

Todo elemento bloqueado debe registrar:

- motivo;
- evidencia del bloqueo;
- decisión necesaria;
- siguiente revisión.

Un elemento no puede pasar directamente de `Pendiente` a `Terminado`.

## Límite de trabajo en curso

El límite inicial es:

```text
WIP = 1 elemento en estado En curso
```

Solo puede iniciarse otro elemento cuando el actual:

- pase a `En validación`;
- vuelva explícitamente a `Pendiente`;
- o quede `Bloqueado` con causa documentada.

El límite WIP pretende reducir trabajo abierto, cambios de contexto,
crecimiento silencioso del alcance y cierres incompletos.

## Criterios para pasar a Preparado

Un elemento está `Preparado` cuando contiene:

- problema o fuente;
- usuario afectado;
- resultado observable;
- criterios de aceptación;
- evidencia prevista;
- dependencias;
- fuera de alcance cuando sea necesario.

## Resumen priorizado

| Orden | ID | Prioridad | Elemento | Estado | Dependencias |
|---:|---|---|---|---|---|
| 1 | `EOS-001` | `P0` | Contrato de planificación y terminado | Terminado | W01D01 |
| 2 | `EOS-002` | `P0` | Validador ejecutable del contrato | Terminado | EOS-001 |
| 3 | `EOS-003` | `P0` | Pruebas y CI del contrato | Terminado | EOS-002 |
| 4 | `EOS-004` | `P1` | Plantilla reutilizable de evidencia | Terminado | EOS-001 |
| 5 | `EOS-005` | `P1` | Recuperación de contexto | En curso | EOS-001 |
| 6 | `EOS-006` | `P1` | Política de decisiones técnicas | Pendiente | EOS-001 |
| 7 | `EOS-007` | `P1` | Medición de carga administrativa | Pendiente | EOS-004 |
| 8 | `EOS-008` | `P2` | CLI local de evidencias | Pendiente | EOS-002, EOS-004 |
| 9 | `EOS-009` | `P2` | Release reproducible | Pendiente | EOS-003, EOS-004 |
| 10 | `EOS-010` | `P3` | Interfaz gráfica | Aparcada | Nueva evidencia |

## EOS-001 · Contrato de planificación y terminado

**Prioridad:** `P0`
**Estado:** Terminado
**Dependencia:** W01D01

### Resultado observable

Existen un backlog priorizado y una Definition of Done reutilizable,
versionados y enlazados con la issue #8.

### Criterios de aceptación

- La política de prioridad está documentada.
- El flujo de estados está documentado.
- Existe un límite WIP explícito.
- Cada elemento incluye resultado, aceptación, evidencia y dependencias.
- La DoD contiene los seis requisitos literales de la ruta.
- Los criterios no aplicables exigen justificación.
- Un incremento bloqueado o incompleto no puede declararse terminado.

### Evidencia prevista

- `docs/planning/backlog.md`.
- `docs/standards/definition-of-done.md`.
- Issue #8.
- Commit AM de W01D02.

## EOS-002 · Validador ejecutable

**Prioridad:** `P0`
**Estado:** Terminado
**Dependencia:** EOS-001

### Resultado observable

Un comando local valida de forma determinista la estructura mínima del backlog
y de la Definition of Done.

### Criterios de aceptación

- Devuelve código `0` cuando el contrato es válido.
- Devuelve código distinto de `0` cuando falta un requisito.
- Informa de comprobaciones superadas y fallidas.
- No requiere dependencias externas.
- Documenta los aspectos que requieren revisión humana.

## EOS-003 · Pruebas y CI

**Prioridad:** `P0`
**Estado:** Terminado
**Dependencia:** EOS-002

### Resultado observable

El contrato se prueba localmente y mediante GitHub Actions.

### Criterios de aceptación

- Existe un caso válido.
- Existe un caso con archivo ausente.
- Existe un caso con sección obligatoria ausente.
- Existe un caso con prioridad o estado inválido.
- Existe un fallo controlado.
- La CI queda verde con documentos válidos.
- La CI bloquea documentos inválidos.

## EOS-004 · Plantilla reutilizable de evidencia

**Prioridad:** `P1`
**Estado:** Terminado
**Dependencia:** EOS-001

### Resultado observable

Cada incremento conserva comandos, resultados, métricas, riesgos, límites y
siguiente acción mediante una estructura común.

### Criterios de aceptación

- Identifica issue, rama y commits.
- Registra resultados observados.
- Distingue hechos de objetivos.
- Evita duplicar información ya enlazada.

### Evidencia entregada

- Plantilla: `docs/templates/increment-evidence-template.md`.
- Evidencia W01D03: `docs/evidence/w01d03-validation.md`.
- Validador: `tools/validate_evidence.py`.
- Pruebas: `tests/test_validate_evidence.py`.
- Workflow: `.github/workflows/engineeringos-discovery.yml`.
- Issue: [#12](https://github.com/JuanCarlosBP/portfolio/issues/12).

## EOS-005 · Recuperación de contexto

**Prioridad:** `P1`
**Estado:** En curso
**Dependencia:** EOS-001

### Resultado observable

El objetivo, estado, decisiones, bloqueos y siguiente acción pueden
reconstruirse usando solo el repositorio en diez minutos o menos.

### Criterios de aceptación

- Existe una ubicación canónica del estado.
- El siguiente paso es operativo.
- Se ejecuta un ejercicio real de recuperación.
- Se registra el tiempo utilizado.

## EOS-006 · Política de decisiones técnicas

**Prioridad:** `P1`
**Estado:** Pendiente
**Dependencia:** EOS-001

### Resultado observable

Se define cuándo una decisión exige ADR y cuándo basta una explicación local.

### Criterios de aceptación

- Incluye desencadenantes claros.
- Exige contexto, decisión, alternativas y consecuencias.
- Evita ADR innecesarios para decisiones triviales.

## EOS-007 · Medición de carga administrativa

**Prioridad:** `P1`
**Estado:** Pendiente
**Dependencia:** EOS-004

### Resultado observable

Puede calcularse el porcentaje de tiempo dedicado a mantener EngineeringOS.

### Criterios de aceptación

- Se registra el tiempo total aproximado.
- Se registra el tiempo administrativo.
- El cálculo es reproducible.
- Una carga repetida superior al 15 % genera revisión.

## EOS-008 · CLI local de evidencias

**Prioridad:** `P2`
**Estado:** Pendiente
**Dependencias:** EOS-002 y EOS-004

### Resultado observable

Una CLI local facilita iniciar, validar y resumir evidencias.

### Criterios de aceptación

- Incluye ayuda integrada.
- No sobrescribe trabajo sin confirmación.
- Produce salidas deterministas.
- No requiere servicios de pago.

## EOS-009 · Release reproducible

**Prioridad:** `P2`
**Estado:** Pendiente
**Dependencias:** EOS-003 y EOS-004

### Resultado observable

EngineeringOS genera una entrega versionada, comprobable y reversible.

### Criterios de aceptación

- Identifica commit y evidencias.
- Incluye instrucciones de reproducción.
- Incluye límites y rollback.
- No se publica con CI fallando.

## EOS-010 · Interfaz gráfica

**Prioridad:** `P3`
**Estado:** Aparcada
**Dependencia:** Nueva evidencia

### Regla de reconsideración

Solo se reconsiderará cuando exista una fricción medida que no pueda resolverse
de forma ligera mediante archivos, CLI o GitHub.

## Control de cambios de alcance

Toda necesidad nueva debe:

1. Registrarse como elemento de backlog o comentario en la issue.
2. Recibir prioridad.
3. Declarar dependencias.
4. Permanecer fuera del incremento actual salvo que bloquee su aceptación.
5. No incorporarse silenciosamente al trabajo en curso.

## Regla de cierre

Un elemento solo pasa a `Terminado` cuando:

- cumple su Definition of Done aplicable;
- conserva la evidencia correspondiente;
- no mantiene criterios obligatorios pendientes;
- no contiene bloqueos incompatibles;
- y puede reconstruirse desde el repositorio.

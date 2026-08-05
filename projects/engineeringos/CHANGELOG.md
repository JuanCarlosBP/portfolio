# Changelog

Los cambios relevantes de EngineeringOS se registran en este documento.

## [Unreleased]

### W01D05 · En validación local

#### Añadido

- Política con `ADR`, `LOCAL_NOTE` y `NO_EXTRA_RECORD`.
- Plantillas de ADR y nota local.
- ADR-0003 y nota local real.
- Validador con 44 comprobaciones.
- Diez pruebas nuevas.
- Ejercicio de doce escenarios.
- Evidencia candidata W01D05.

#### Cambiado

- El contrato contextual acepta EOS-006 activo.
- El workflow incorpora el quinto gate.
- EOS-006 pasa a `En validación`.
- README, backlog, DoD y estado reflejan W01D05.

#### Validación local observada

- 40/40 pruebas.
- Discovery: 40/40.
- Planificación: 39/39.
- Evidencia: 46/46.
- Contexto: 36/36.
- Decisiones: 44/44.
- Escenarios: 12/12.
- Contradicciones: 0.

#### Pendiente de validación remota

- Commit PM.
- Push definitivo.
- Pull request.
- CI del SHA PM.
- Integración en `main`.
- Cierre de la issue #16.

## [W01D04] - 2026-08-03

### Añadido

- Estado canónico de EngineeringOS.
- Validador de recuperación con 36 comprobaciones.
- Nueve pruebas del contrato y de fallos relevantes.
- Evidencia reproducible de W01D04.
- Ejercicio autónomo de recuperación de contexto.

### Cambiado

- EOS-005 pasa a `Terminado`.
- EOS-006 queda como siguiente elemento `Pendiente`.
- El workflow incorpora el gate de recuperación.
- README, backlog, DoD y changelog reflejan el estado de W01D04.

### Validación local

- 30/30 pruebas automáticas.
- Gate de discovery: 40/40.
- Gate de planificación: 39/39.
- Gate de evidencia: 46/46.
- Gate de recuperación: 36/36.
- Ejercicio humano: 5/5 campos, 0 contradicciones y 83 segundos.

### Limitaciones conocidas

- El gate no sustituye la revisión semántica humana.
- La validación remota se registrará después de verificar PR, CI e integración.
- La CLI y el proceso completo de release permanecen fuera del alcance.

## [W01D03] - 2026-08-01

### Añadido

- Plantilla reutilizable de evidencia.
- Evidencia real del incremento W01D03.
- Validador ejecutable con 46 comprobaciones.
- Once pruebas del caso válido y de fallos relevantes.
- Separación explícita entre hechos observados y objetivos pendientes.
- Registro de comandos, códigos de salida, métricas, riesgos y limitaciones.

### Cambiado

- El workflow incorpora el gate de evidencia.
- EOS-004 pasa a `Terminado` en el cambio candidato.
- La Definition of Done exige plantilla canónica o excepción documentada.
- README raíz y README de EngineeringOS actualizados para W01D03.

### Validación local

- 21/21 pruebas automáticas.
- Gate de discovery: 40/40.
- Gate de planificación: 39/39.
- Gate de evidencia: 46/46.

### Limitaciones conocidas

- La validación remota se registra en GitHub después de verificar cada SHA.
- El validador no determina por sí solo la utilidad empresarial.
- La cumplimentación continúa requiriendo revisión humana.
- La CLI y el proceso de release permanecen fuera del alcance.

## [W01D02] - 2026-07-30

### Añadido

- Backlog priorizado con diez elementos operativos.
- Política de prioridades `P0` a `P3`.
- Flujo explícito de estados.
- Límite WIP de un elemento en curso.
- Definition of Done reutilizable.
- Validador ejecutable del contrato de planificación.
- Seis pruebas del caso válido y de fallos relevantes.
- ADR-0002 con la decisión y sus alternativas.
- Evidencia reproducible del incremento.

### Cambiado

- El workflow de EngineeringOS ejecuta los gates de discovery y planificación.
- README actualizado al estado de W01D02.
- EOS-001, EOS-002 y EOS-003 pasan a `Terminado`.

### Limitaciones conocidas

- El gate valida estructura y reglas, no prioridad empresarial.
- El mantenimiento del backlog sigue siendo manual.
- La CLI general permanece fuera del alcance de W01D02.

## [W01D01] - 2026-07-25

### Añadido

- Discovery inicial: problema, usuarios, proceso actual y métricas de éxito.
- Quality gate ejecutable de 40 comprobaciones.
- Cuatro pruebas automáticas para los casos principal y de fallo.
- GitHub Actions para validar el discovery en pull requests y en `main`.
- ADR de la decisión de validación.
- Evidencia reproducible del incremento.

### Cambiado

- Los cuatro documentos pasan de `Borrador inicial` a
  `Validado en W01D01`.

### Limitaciones conocidas

- El control valida estructura y trazabilidad, no la calidad semántica completa.
- La CLI general de EngineeringOS permanece fuera del alcance de W01D01.

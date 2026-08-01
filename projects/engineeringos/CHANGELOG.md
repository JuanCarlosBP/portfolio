# Changelog

Los cambios relevantes de EngineeringOS se registran en este documento.

## [Unreleased]

### Próximo

- Ejecutar EOS-005 y medir la recuperación de contexto.
- Definir la política para registrar decisiones técnicas.

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

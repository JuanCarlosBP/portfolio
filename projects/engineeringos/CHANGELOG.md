# Changelog

Los cambios relevantes de EngineeringOS se registran en este documento.

## [Unreleased]

### Próximo

- Crear una plantilla reutilizable de evidencia.
- Medir la recuperación de contexto entre sesiones.
- Definir la política para registrar decisiones técnicas.

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

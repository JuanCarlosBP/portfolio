# Changelog

Los cambios relevantes de EngineeringOS se registran en este documento.

## [Unreleased]

### Próximo

- Convertir los hallazgos de discovery en backlog priorizado.
- Definir una Definition of Done reutilizable.

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

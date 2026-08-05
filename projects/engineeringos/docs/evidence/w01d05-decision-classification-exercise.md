# Ejercicio de clasificación de decisiones · W01D05

| Campo | Valor |
|---|---|
| Proyecto | EngineeringOS |
| Elemento | `EOS-006 · Política de decisiones técnicas` |
| Día lógico | `W01D05` |
| Fecha de ejecución | `2026-08-05` |
| Issue | [#16](https://github.com/JuanCarlosBP/portfolio/issues/16) |
| Política aplicada | `docs/standards/technical-decision-policy.md` |
| Escenarios | 12 |
| ADR esperados | 4 |
| Notas locales esperadas | 4 |
| Sin registro adicional esperados | 4 |
| Contradicciones permitidas | 0 |
| Estado | En validación |

## Objetivo

Comprobar que la política permite distinguir de forma reproducible entre `ADR`, `LOCAL_NOTE` y `NO_EXTRA_RECORD`.

## Método de inferencia

1. Uno o más identificadores `ADR-*` implican `ADR`.
2. Las seis reglas `LOCAL-01` a `LOCAL-06`, sin identificadores ADR, implican `LOCAL_NOTE`.
3. Uno o más identificadores `TRIV-*`, sin identificadores ADR o LOCAL, implican `NO_EXTRA_RECORD`.
4. No se permiten grupos mezclados.
5. La clasificación esperada debe coincidir con la inferida.
6. Cualquier discrepancia se registra como contradicción.

## Distribución

| Clasificación | Escenarios | Cantidad |
|---|---|---|
| `ADR` | S01–S04 | 4 |
| `LOCAL_NOTE` | S05–S08 | 4 |
| `NO_EXTRA_RECORD` | S09–S12 | 4 |

## S01 · Cambiar el contrato canónico de Markdown a JSON

**Descripción:** Sustituir el formato Markdown de todas las evidencias por JSON, modificando validadores, plantillas, documentación y consumidores futuros.

**Clasificación esperada:** `ADR`

**Reglas aplicadas:** `ADR-01`, `ADR-02`, `ADR-07`, `ADR-08`, `ADR-10`

**Clasificación inferida por precedencia:** `ADR`

**Contradicción:** `No`

**Evidencia mínima:** Contrato anterior y nuevo, componentes afectados, alternativas, estrategia de migración, reversión y criterio de revisión.

**Justificación:** La decisión afecta a varios componentes, cambia un contrato estable, puede requerir migración y condiciona incrementos posteriores.

## S02 · Sustituir GitHub Actions por otra plataforma de CI

**Descripción:** Reemplazar el workflow actual y trasladar todos los gates a un proveedor de integración continua diferente.

**Clasificación esperada:** `ADR`

**Reglas aplicadas:** `ADR-06`, `ADR-08`, `ADR-10`

**Clasificación inferida por precedencia:** `ADR`

**Contradicción:** `No`

**Evidencia mínima:** Flujo anterior y nuevo, alternativas, impacto operativo, plan de transición, reversión y criterio de revisión.

**Justificación:** Se modifica una superficie estructural de CI, existen alternativas materiales y la elección condicionará la entrega futura.

## S03 · Introducir un servicio externo de pago

**Descripción:** Enviar documentos a una API de terceros con facturación por uso para realizar una validación adicional.

**Clasificación esperada:** `ADR`

**Reglas aplicadas:** `ADR-03`, `ADR-05`, `ADR-08`

**Clasificación inferida por precedencia:** `ADR`

**Contradicción:** `No`

**Evidencia mínima:** Proveedor, versión, coste esperado, límites, alternativas sin coste, disponibilidad y estrategia de salida.

**Justificación:** Se incorpora una dependencia externa con coste recurrente y trade-offs materiales frente a la validación local.

## S04 · Incorporar telemetría externa con datos de ejecución

**Descripción:** Enviar a un servicio remoto identificadores, tiempos, resultados y metadatos de las ejecuciones del repositorio.

**Clasificación esperada:** `ADR`

**Reglas aplicadas:** `ADR-03`, `ADR-04`, `ADR-10`

**Clasificación inferida por precedencia:** `ADR`

**Contradicción:** `No`

**Evidencia mínima:** Datos transmitidos, finalidad, amenazas, controles, retención, proveedor, estrategia de salida y riesgo residual.

**Justificación:** Aparecen un servicio permanente, tratamiento de datos y una restricción estable sobre la operación futura.

## S05 · Reutilizar el workflow existente para añadir un gate

**Descripción:** Añadir un único paso al workflow actual sin cambiar proveedor, eventos, permisos, secretos o arquitectura de CI.

**Clasificación esperada:** `LOCAL_NOTE`

**Reglas aplicadas:** `LOCAL-01`, `LOCAL-02`, `LOCAL-03`, `LOCAL-04`, `LOCAL-05`, `LOCAL-06`

**Clasificación inferida por precedencia:** `LOCAL_NOTE`

**Contradicción:** `No`

**Evidencia mínima:** Nota local con contexto, decisión, alcance, consecuencias, reversión, condición de escalado e issue relacionada.

**Justificación:** La decisión está limitada al incremento, es reversible y su explicación mejora la revisión sin crear una norma transversal.

## S06 · Separar el ejercicio de la evidencia final

**Descripción:** Conservar los doce escenarios en un archivo específico y reservar la evidencia final para el resumen integral de W01D05.

**Clasificación esperada:** `LOCAL_NOTE`

**Reglas aplicadas:** `LOCAL-01`, `LOCAL-02`, `LOCAL-03`, `LOCAL-04`, `LOCAL-05`, `LOCAL-06`

**Clasificación inferida por precedencia:** `LOCAL_NOTE`

**Contradicción:** `No`

**Evidencia mínima:** Explicación local de la separación, rutas afectadas, ventaja para la revisión y forma de reunificar los documentos.

**Justificación:** La organización afecta solo a W01D05, no cambia contratos y puede revertirse trasladando el contenido.

## S07 · Utilizar un corpus fijo de doce escenarios

**Descripción:** Emplear doce casos versionados en lugar de generar escenarios dinámicamente durante cada ejecución.

**Clasificación esperada:** `LOCAL_NOTE`

**Reglas aplicadas:** `LOCAL-01`, `LOCAL-02`, `LOCAL-03`, `LOCAL-04`, `LOCAL-05`, `LOCAL-06`

**Clasificación inferida por precedencia:** `LOCAL_NOTE`

**Contradicción:** `No`

**Evidencia mínima:** Razón de reproducibilidad, alcance del corpus, límites, reversión y condición para ampliar o sustituir los casos.

**Justificación:** Es una decisión metodológica local, reversible y útil para comparar resultados sin crear una política general de datos.

## S08 · Validar en un directorio sombra antes de instalar

**Descripción:** Construir y ejecutar los cambios PM en un directorio temporal antes de copiarlos al working tree real.

**Clasificación esperada:** `LOCAL_NOTE`

**Reglas aplicadas:** `LOCAL-01`, `LOCAL-02`, `LOCAL-03`, `LOCAL-04`, `LOCAL-05`, `LOCAL-06`

**Clasificación inferida por precedencia:** `LOCAL_NOTE`

**Contradicción:** `No`

**Evidencia mínima:** Directorio utilizado, fuente exportada, validaciones ejecutadas, criterio de instalación y procedimiento de limpieza.

**Justificación:** La decisión limita el riesgo del incremento, es reversible y no altera el contrato externo del proyecto.

## S09 · Corregir una falta ortográfica

**Descripción:** Cambiar una palabra mal escrita sin modificar el significado, la estructura ni el comportamiento observable.

**Clasificación esperada:** `NO_EXTRA_RECORD`

**Reglas aplicadas:** `TRIV-01`

**Clasificación inferida por precedencia:** `NO_EXTRA_RECORD`

**Contradicción:** `No`

**Evidencia mínima:** Diff completo, mensaje de commit y confirmación de ausencia de cambio semántico.

**Justificación:** Es una corrección ortográfica sin decisión técnica nueva y el historial ordinario permite reconstruirla.

## S10 · Ajustar el formato de un documento Markdown

**Descripción:** Sustituir un salto visual por una construcción Markdown equivalente sin cambiar contenido ni contrato.

**Clasificación esperada:** `NO_EXTRA_RECORD`

**Reglas aplicadas:** `TRIV-02`

**Clasificación inferida por precedencia:** `NO_EXTRA_RECORD`

**Contradicción:** `No`

**Evidencia mínima:** Diff, ejecución de git diff --check y comprobación del renderizado cuando corresponda.

**Justificación:** El cambio es exclusivamente de formato y conserva el significado y el comportamiento observable.

## S11 · Actualizar un enlace roto

**Descripción:** Sustituir una URL obsoleta por la dirección canónica del mismo recurso sin modificar el contrato documentado.

**Clasificación esperada:** `NO_EXTRA_RECORD`

**Reglas aplicadas:** `TRIV-03`

**Clasificación inferida por precedencia:** `NO_EXTRA_RECORD`

**Contradicción:** `No`

**Evidencia mínima:** Diff completo y comprobación verificable del destino canónico del enlace actualizado.

**Justificación:** La actualización no crea una decisión técnica nueva ni altera el comportamiento contractual.

## S12 · Extraer una función auxiliar sin cambiar comportamiento

**Descripción:** Reorganizar código duplicado en una función auxiliar manteniendo las mismas entradas, salidas e interfaces.

**Clasificación esperada:** `NO_EXTRA_RECORD`

**Reglas aplicadas:** `TRIV-06`

**Clasificación inferida por precedencia:** `NO_EXTRA_RECORD`

**Contradicción:** `No`

**Evidencia mínima:** Pruebas antes y después, diff completo y revisión explícita de las interfaces conservadas.

**Justificación:** Es un refactor cubierto por pruebas que conserva el comportamiento y no introduce una decisión arquitectónica.

## Resultado esperado

| Métrica | Resultado |
|---|---|
| Escenarios clasificados | 12/12 |
| Coincidencias esperada/inferida | 12/12 |
| Escenarios ADR | 4/4 |
| Escenarios LOCAL_NOTE | 4/4 |
| Escenarios NO_EXTRA_RECORD | 4/4 |
| Grupos de reglas mezclados | 0 |
| Contradicciones | 0 |
| Resultado | `PASS` |

## Límites

El ejercicio valida coherencia estructural y aplicación explícita de las reglas. No sustituye la revisión humana de materialidad.

## Trazabilidad

| Elemento | Referencia |
|---|---|
| Issue | [#16](https://github.com/JuanCarlosBP/portfolio/issues/16) |
| Rama | `docs/p01-w01d05-technical-decision-policy` |
| Política | `projects/engineeringos/docs/standards/technical-decision-policy.md` |
| Gate | `projects/engineeringos/tools/validate_decision_policy.py` |
| Evidencia final | `projects/engineeringos/docs/evidence/w01d05-technical-decision-policy.md` |
| Commit PM | Pendiente de creación |
| Pull request | Pendiente de creación |

# ADR-{{ADR_NUMBER}} · {{TITLE}}

**Estado:** {{STATUS}}<br>
**Fecha:** {{DATE}}<br>
**Decisión relacionada:** {{RELATED_DECISION}}<br>
**Issue:** {{ISSUE_URL}}<br>
**Componentes afectados:** {{AFFECTED_COMPONENTS}}<br>
**Sustituye:** {{SUPERSEDES_OR_NONE}}<br>
**Sustituida por:** {{SUPERSEDED_BY_OR_NONE}}

<!-- TEMPLATE_INSTRUCTION:
Los valores permitidos para Estado son Propuesta, Aceptada, Rechazada,
Sustituida y Obsoleta. Elimine todas las instrucciones antes de aceptar el ADR.
-->

## Contexto

{{CONTEXT}}

<!-- TEMPLATE_INSTRUCTION:
Describa el problema, restricciones, hechos observados, fuerzas técnicas,
personas afectadas y razón por la que la decisión es necesaria.
-->

## Desencadenantes aplicables

- {{ADR_TRIGGER_ID}} · {{ADR_TRIGGER_REASON}}

<!-- TEMPLATE_INSTRUCTION:
Incluya al menos un desencadenante ADR-01 a ADR-10 y explique su aplicación
material. No marque desencadenantes por coincidencia terminológica.
-->

## Decisión

{{DECISION}}

<!-- TEMPLATE_INSTRUCTION:
Describa una decisión concreta, comprobable y delimitada. Indique qué se adopta,
qué no se adopta y desde cuándo gobierna.
-->

## Alternativas consideradas

### Alternativa A · {{ALTERNATIVE_A_TITLE}}

{{ALTERNATIVE_A_DESCRIPTION}}

**Ventajas:**

- {{ALTERNATIVE_A_ADVANTAGE}}

**Inconvenientes:**

- {{ALTERNATIVE_A_DISADVANTAGE}}

**Resultado:** {{ALTERNATIVE_A_RESULT}}

### Alternativa B · {{ALTERNATIVE_B_TITLE}}

{{ALTERNATIVE_B_DESCRIPTION}}

**Ventajas:**

- {{ALTERNATIVE_B_ADVANTAGE}}

**Inconvenientes:**

- {{ALTERNATIVE_B_DISADVANTAGE}}

**Resultado:** {{ALTERNATIVE_B_RESULT}}

<!-- TEMPLATE_INSTRUCTION:
Añada alternativas reales. No construya alternativas artificialmente débiles
para justificar la decisión elegida.
-->

## Consecuencias

### Positivas

- {{POSITIVE_CONSEQUENCE}}

### Negativas

- {{NEGATIVE_CONSEQUENCE}}

### Riesgos

- {{RISK}}

### Trabajo posterior

- {{FOLLOW_UP_WORK}}

## Trade-off aceptado

Se acepta {{ACCEPTED_COST}} a cambio de {{OBTAINED_ADVANTAGE}}.

## Plan de reversión

{{ROLLBACK_PLAN}}

<!-- TEMPLATE_INSTRUCTION:
Explique cómo se desharía la decisión, qué datos o contratos deben migrarse y
qué limitaciones tendría la reversión.
-->

## Criterio de revisión

Revisar esta decisión cuando:

- {{REVIEW_TRIGGER}}

## Trazabilidad

| Elemento | Referencia |
|---|---|
| Issue | {{ISSUE_URL}} |
| Rama | `{{BRANCH}}` |
| Commit | `{{COMMIT_OR_PENDING}}` |
| Pull request | {{PR_URL_OR_PENDING}} |
| Evidencia | {{EVIDENCE_PATH_OR_URL}} |
| Decisión anterior | {{SUPERSEDES_OR_NONE}} |
| Decisión sucesora | {{SUPERSEDED_BY_OR_NONE}} |

## Lista de comprobación

- [ ] El estado utiliza un valor permitido.
- [ ] El contexto diferencia hechos, hipótesis y objetivos.
- [ ] Existe al menos un desencadenante material.
- [ ] La decisión es concreta.
- [ ] Se evaluaron alternativas reales.
- [ ] Se declararon consecuencias positivas y negativas.
- [ ] El trade-off es explícito.
- [ ] Existe criterio de revisión.
- [ ] La trazabilidad está completa.
- [ ] No quedan marcadores sin resolver.

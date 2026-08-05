# Nota local · {{TITLE}}

**Proyecto:** EngineeringOS<br>
**Día o incremento:** {{DAY_OR_INCREMENT}}<br>
**Fecha:** {{DATE}}<br>
**Issue:** {{ISSUE_URL}}<br>
**Rama:** `{{BRANCH}}`<br>
**Estado:** {{STATUS}}

<!-- TEMPLATE_INSTRUCTION:
Use esta plantilla solo cuando no aplique ningún desencadenante material de ADR.
Elimine todas las instrucciones y marcadores antes del cierre.
-->

## Contexto local

{{LOCAL_CONTEXT}}

## Decisión

{{LOCAL_DECISION}}

## Motivo de clasificación

**Nivel elegido:** `LOCAL_NOTE`

**Por qué no exige ADR:**

{{WHY_NOT_ADR}}

**Reglas locales aplicables:**

- {{LOCAL_RULE_ID}} · {{LOCAL_RULE_REASON}}

## Alcance y límites

### Incluido

- {{IN_SCOPE}}

### Fuera de alcance

- {{OUT_OF_SCOPE}}

## Consecuencias

### Positivas

- {{POSITIVE_CONSEQUENCE}}

### Negativas o limitaciones

- {{NEGATIVE_CONSEQUENCE}}

## Reversión

{{ROLLBACK_STEPS}}

## Criterio de escalado

Esta nota debe convertirse en ADR cuando:

- {{ESCALATION_TRIGGER}}

## Trazabilidad

| Elemento | Referencia |
|---|---|
| Issue | {{ISSUE_URL}} |
| Rama | `{{BRANCH}}` |
| Commit | `{{COMMIT_OR_PENDING}}` |
| Pull request | {{PR_URL_OR_PENDING}} |
| Evidencia | {{EVIDENCE_PATH_OR_URL}} |

## Lista de comprobación

- [ ] No aplica ningún desencadenante material de ADR.
- [ ] El alcance está limitado.
- [ ] La decisión es reversible.
- [ ] No cambia contratos externos.
- [ ] No introduce dependencia permanente.
- [ ] No afecta a seguridad, privacidad o coste recurrente.
- [ ] La explicación mejora la revisión o recuperación de contexto.
- [ ] Existe una condición de escalado.
- [ ] La trazabilidad está completa.
- [ ] No quedan marcadores sin resolver.

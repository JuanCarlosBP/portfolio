# ADR-0003 · Política proporcional de decisiones técnicas

**Estado:** Propuesta

**Fecha:** 2026-08-05

**Decisión relacionada:** W01D05 · EOS-006

**Issue:** [#16](https://github.com/JuanCarlosBP/portfolio/issues/16)

**Componentes afectados:** ADR, notas locales, backlog, estado canónico,
validadores, pruebas, CI y evidencias futuras.

**Sustituye:** Ninguna.

**Sustituida por:** Ninguna.

## Contexto

EngineeringOS ya conserva decisiones mediante ADR-0001 y ADR-0002, pero todavía
no dispone de una regla versionada que permita decidir cuándo una decisión
necesita un ADR, cuándo basta una nota local y cuándo el commit, el diff, las
pruebas y la evidencia ordinaria son suficientes.

La ausencia de esa regla produce dos riesgos opuestos:

1. perder el contexto de decisiones materiales;
2. generar documentación excesiva para cambios triviales o reversibles.

La nueva política afectará a incrementos futuros y se convertirá en un contrato
documental validado de forma determinista.

## Desencadenantes aplicables

- `ADR-01` · La decisión afecta a varios componentes e incrementos futuros.
- `ADR-02` · La política crea un contrato documental reutilizable.
- `ADR-08` · Existen alternativas con costes y niveles de trazabilidad distintos.
- `ADR-10` · La decisión condicionará cómo se documentan decisiones posteriores.

## Decisión

Adoptar una política proporcional con tres niveles de clasificación:

1. `ADR` para decisiones materiales, transversales, duraderas o difíciles de
   revertir.
2. `LOCAL_NOTE` para decisiones limitadas a un incremento, reversibles y útiles
   para comprender un cambio concreto.
3. `NO_EXTRA_RECORD` para cambios triviales, mecánicos o ya gobernados por una
   decisión vigente.

La clasificación utilizará:

- diez desencadenantes de ADR;
- seis reglas para notas locales;
- siete casos de cambio trivial;
- una regla de precedencia;
- un algoritmo de seis pasos;
- criterios explícitos de escalado;
- un ciclo de vida de cinco estados.

La estructura se mantendrá en Markdown y se validará con Python estándar, sin
dependencias ni servicios externos.

## Alternativas consideradas

### Alternativa A · Exigir ADR para cualquier decisión

Descartada porque convertiría cambios pequeños y reversibles en trabajo
administrativo desproporcionado.

**Ventaja:** máxima uniformidad documental.

**Inconveniente:** elevada carga de mantenimiento y pérdida de señal entre
decisiones importantes y triviales.

### Alternativa B · Mantener únicamente los ADR actuales

Descartada porque no ofrece un criterio reutilizable para decisiones futuras.

**Ventaja:** no añade archivos ni reglas.

**Inconveniente:** la clasificación seguiría dependiendo de memoria y criterio
informal.

### Alternativa C · Registrar todas las decisiones solo en issues

Descartada porque las issues son adecuadas para coordinación, pero no sustituyen
un registro versionado y enlazado con el código y los contratos.

**Ventaja:** menor número de documentos.

**Inconveniente:** peor recuperación histórica desde el repositorio.

### Alternativa D · Utilizar JSON o YAML como formato canónico

Pospuesta. Facilitaría consultas y validación estructurada, pero reduciría la
lectura directa y añadiría complejidad antes de disponer de evidencia que la
justifique.

**Ventaja:** estructura rígida y procesamiento sencillo.

**Inconveniente:** mayor coste de edición, migración y mantenimiento.

## Consecuencias

### Positivas

- Las decisiones materiales conservarán contexto, alternativas y consecuencias.
- Los cambios locales dispondrán de una vía documental ligera.
- Los cambios triviales no producirán ADR innecesarios.
- La clasificación podrá revisarse mediante identificadores estables.
- El repositorio seguirá siendo la fuente canónica.
- El contrato podrá comprobarse localmente y en CI.

### Negativas

- La política añade tres documentos base y dos casos reales.
- Los validadores dependerán parcialmente de marcadores textuales.
- La materialidad de una decisión seguirá requiriendo revisión humana.
- La política deberá actualizarse cuando cambie la estructura del repositorio.

### Riesgos

- Utilizar una nota local para evitar un ADR necesario.
- Crear ADR por coincidencia terminológica sin impacto material.
- Tratar una clasificación automática como sustituto de revisión técnica.
- Mantener documentos obsoletos sin actualizar su estado.

### Trabajo posterior

- Implementar el validador de política.
- Crear pruebas positivas y negativas.
- Clasificar doce escenarios.
- Integrar el quinto gate en GitHub Actions.
- Medir posteriormente la carga administrativa mediante EOS-007.

## Trade-off aceptado

Se acepta una estructura documental adicional y un coste moderado de
mantenimiento a cambio de conservar decisiones materiales sin imponer el mismo
peso documental a todos los cambios.

## Plan de reversión

La decisión puede revertirse mediante:

1. retirar el gate de política de la CI;
2. eliminar las plantillas y la política;
3. conservar ADR-0001, ADR-0002 y ADR-0003 como historia;
4. devolver EOS-006 a `Pendiente`;
5. restaurar el estado canónico anterior;
6. documentar mediante un nuevo ADR la política sustituta.

No se eliminarán decisiones históricas para ocultar que la política estuvo
vigente.

## Criterio de revisión

Revisar esta decisión cuando:

- la clasificación genere contradicciones repetidas;
- la carga documental supere el valor obtenido;
- aparezcan decisiones materiales sin ADR;
- las notas locales se conviertan sistemáticamente en ADR;
- Markdown deje de ser suficiente;
- EngineeringOS adopte una CLI o un formato estructurado;
- cambie el modelo de CI o almacenamiento.

## Compatibilidad con decisiones anteriores

ADR-0001 y ADR-0002 conservan su validez histórica.

No se reescriben para añadir identificadores de desencadenantes creados con
posterioridad. Se consideran conformes cuando contienen como mínimo:

- contexto;
- decisión;
- alternativas consideradas;
- consecuencias;
- trade-off aceptado;
- criterio de revisión.

## Trazabilidad

| Elemento | Referencia |
|---|---|
| Issue | [#16](https://github.com/JuanCarlosBP/portfolio/issues/16) |
| Rama | `docs/p01-w01d05-technical-decision-policy` |
| Política | `projects/engineeringos/docs/standards/technical-decision-policy.md` |
| Plantilla ADR | `projects/engineeringos/docs/templates/adr-template.md` |
| Plantilla local | `projects/engineeringos/docs/templates/local-decision-note-template.md` |
| Evidencia | `projects/engineeringos/docs/evidence/w01d05-technical-decision-policy.md` |
| Pull request | Pendiente de creación |
| Commit AM | Pendiente de creación |

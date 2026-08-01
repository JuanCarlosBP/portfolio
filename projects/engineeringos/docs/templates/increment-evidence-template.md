# Evidencia de incremento · {{DAY_ID}}

## Metadatos

| Campo | Valor |
|---|---|
| Proyecto | {{PROJECT}} |
| Día de trabajo | {{DAY_ID}} |
| Fecha de ejecución | {{EXECUTION_DATE}} |
| Issue | {{ISSUE_URL}} |
| Rama | `{{BRANCH}}` |
| Commit AM | `{{AM_COMMIT}}` |
| Commit PM | `{{PM_COMMIT_MESSAGE}}` |
| Estado | {{STATUS}} |
| Versión de la plantilla | `1.0.0` |

<!-- TEMPLATE_INSTRUCTION:
Sustituya todos los marcadores entre llaves antes de declarar terminada una
evidencia real. La plantilla conserva instrucciones; la evidencia final no.
-->

## Propósito

**Problema:**

<!-- TEMPLATE_INSTRUCTION:
Describa el problema concreto que originó el incremento.
-->

**Usuario o destinatario:**

<!-- TEMPLATE_INSTRUCTION:
Identifique quién necesita el resultado.
-->

**Resultado empresarial perseguido:**

<!-- TEMPLATE_INSTRUCTION:
Explique qué incertidumbre, riesgo, coste o fricción pretende reducir.
-->

**Resultado observable esperado:**

<!-- TEMPLATE_INSTRUCTION:
Defina qué deberá existir o funcionar al terminar.
-->

## Alcance

### Incluido

<!-- TEMPLATE_INSTRUCTION:
Enumere únicamente el trabajo comprometido para este incremento.
-->

### Fuera de alcance

<!-- TEMPLATE_INSTRUCTION:
Enumere lo que se excluye para impedir crecimiento silencioso.
-->

## Hechos observados

<!-- TEMPLATE_INSTRUCTION:
Registre solo hechos comprobados mediante archivos, comandos, GitHub, pruebas
o inspección directa. No escriba objetivos, previsiones ni afirmaciones futuras.
-->

## Objetivos aún no verificados

<!-- TEMPLATE_INSTRUCTION:
Registre resultados previstos que todavía no puedan presentarse como hechos.
Cuando se verifiquen, muévalos a Hechos observados y enlace su evidencia.
-->

## Comandos y resultados

Cada comando debe conservar su código de salida y un resultado resumido. La
salida completa puede enlazarse cuando ya exista en GitHub o en otra evidencia
canónica.

| Orden | Comando | Código de salida | Resultado observado | Evidencia |
|---:|---|---:|---|---|

<!-- TEMPLATE_INSTRUCTION:
Añada una fila por comando relevante. Use un entero como código de salida.
No copie salidas extensas si ya están disponibles mediante un enlace estable.
-->

## Métricas

Clases permitidas:

- `Observada`: valor medido durante la ejecución.
- `Objetivo`: valor esperado que todavía no se ha observado.
- `No medida`: señal relevante sin medición disponible.

| Clase | Señal | Valor | Fuente | Interpretación |
|---|---|---|---|---|

<!-- TEMPLATE_INSTRUCTION:
Debe existir al menos una métrica de clase Observada para cerrar el incremento.
No mezcle valores históricos, actuales, acumulativos y vivos.
-->

## Decisión y trade-off

| Campo | Contenido |
|---|---|
| Decisión | |
| Alternativa descartada | |
| Ventaja obtenida | |
| Coste o inconveniente aceptado | |
| Criterio de revisión | |

<!-- TEMPLATE_INSTRUCTION:
Explique por qué se eligió la solución, qué alternativa se descartó y bajo qué
condición debería revisarse la decisión.
-->

## Riesgos y limitaciones

| Tipo | Descripción | Mitigación o tratamiento | Estado |
|---|---|---|---|

<!-- TEMPLATE_INSTRUCTION:
Diferencie riesgo activo, limitación conocida, bloqueo y trabajo pendiente.
No presente una limitación como si hubiera sido resuelta.
-->

## Impacto documental

| Superficie revisada | Decisión | Resultado |
|---|---|---|
| `README.md` raíz | | |
| `projects/engineeringos/README.md` | | |
| Changelog | | |
| Backlog | | |
| Definition of Done | | |

<!-- TEMPLATE_INSTRUCTION:
Registre cada README afectado aunque la decisión final sea No requiere cambio.
-->

## Trazabilidad y enlaces canónicos

| Elemento | URL o ruta canónica | Finalidad |
|---|---|---|
| Issue | | |
| Pull request | | |
| CI | | |
| Commit AM | | |
| Commit PM | | |
| Archivo o evidencia principal | | |

<!-- TEMPLATE_INSTRUCTION:
Enlace la fuente canónica. No duplique dentro de este documento contenido que ya
pueda verificarse en la issue, la PR, la CI o el repositorio.
-->

## Siguiente acción

<!-- TEMPLATE_INSTRUCTION:
Defina una acción concreta, ejecutable y coherente con el backlog.
-->

## Reglas de uso

1. No presentar objetivos como resultados observados.
2. No declarar una métrica sin valor, fuente e interpretación.
3. No omitir el código de salida de los comandos relevantes.
4. No copiar información extensa que ya tenga una fuente canónica enlazable.
5. No ocultar riesgos, limitaciones, bloqueos o trabajo pendiente.
6. No cerrar la evidencia sin revisar todos los archivos `README.md` afectados.
7. No afirmar que existe CI verde si no corresponde al SHA entregado.
8. No declarar terminado el incremento mientras queden marcadores sin resolver.

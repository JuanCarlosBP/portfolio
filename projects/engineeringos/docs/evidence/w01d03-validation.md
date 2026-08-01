# Evidencia de incremento · W01D03

## Metadatos

| Campo | Valor |
|---|---|
| Proyecto | EngineeringOS |
| Día de trabajo | W01D03 |
| Fecha de ejecución | 2026-08-01 |
| Issue | https://github.com/JuanCarlosBP/portfolio/issues/12 |
| Rama | `docs/p01-w01d03-evidence-template` |
| Commit AM | `376d9263e4b2a91f2e10e9f4ae87c4ca86e2b50d` |
| Commit PM | `test(w0013pm): discovery engineeringos` |
| Estado | En validación |
| Versión de la plantilla | `1.0.0` |

## Propósito

**Problema:** Las evidencias de W01D01 y W01D02 conservaron información útil,
pero fueron redactadas con estructuras individuales que no garantizaban un
contrato común.

**Usuario o destinatario:** Juan Carlos, como desarrollador y responsable del
mantenimiento de EngineeringOS.

**Resultado empresarial perseguido:** Reducir pérdida de contexto, omisiones,
duplicación documental y confusión entre objetivos previstos y resultados
realmente observados.

**Resultado observable esperado:** Disponer de una plantilla reutilizable, un
validador determinista, pruebas negativas y un quality gate ejecutable.

## Alcance

### Incluido

- Plantilla canónica de evidencia.
- Evidencia real de W01D03.
- Validador de 46 comprobaciones.
- Once pruebas nuevas.
- Integración del gate en GitHub Actions.
- Actualización del backlog y de la Definition of Done.
- Actualización del changelog y de los dos README afectados.

### Fuera de alcance

- EOS-005: recuperación cronometrada de contexto.
- EOS-006: política formal para decidir cuándo crear ADR.
- EOS-007: medición de carga administrativa.
- EOS-008: CLI generadora de evidencias.
- EOS-009: release reproducible.
- EOS-010: interfaz gráfica.
- Jira, Confluence, CV, dominio, DNS y Sites.

## Hechos observados

- La issue 12 está abierta y conserva el contrato del incremento.
- El commit AM `376d9263e4b2a91f2e10e9f4ae87c4ca86e2b50d` está publicado en la rama W01D03.
- La plantilla contiene 16 encabezados.
- La plantilla contiene nueve apariciones de ocho placeholders distintos.
- Se detectó y corrigió una expectativa incorrecta sobre las dos apariciones de
  `DAY_ID`.
- Se corrigió la normalización de delimitadores Markdown en `strip_code()`.
- Se corrigió el cargador de verificación para registrar el módulo dinámico en
  `sys.modules` bajo Python 3.14.
- Las once pruebas nuevas del contrato de evidencia están superadas.
- La suite local completa obtuvo 21/21 pruebas.
- El gate de discovery obtuvo 40/40 comprobaciones.
- El gate de planificación obtuvo 39/39 comprobaciones.
- El gate de evidencia obtuvo 46/46 comprobaciones.
- Se detectó que un heredoc no literal interpretó acentos graves como
  sustituciones de comandos.
- La evidencia se reconstruyó con un heredoc literal y sustitución controlada
  de placeholders.

## Objetivos aún no verificados

- Crear el commit PM con el mensaje `test(w0013pm): discovery engineeringos`.
- Crear la pull request y verificar su CI sobre el SHA entregado.
- Fusionar mediante merge commit conservando los commits AM y PM.
- Verificar la CI de `main`.
- Cerrar la issue 12 después de la integración.
- Confirmar el estado del feed automático posterior al merge.

## Comandos y resultados

| Orden | Comando | Código de salida | Resultado observado | Evidencia |
|---:|---|---:|---|---|
| 1 | `python3 -B -m unittest discover -s projects/engineeringos/tests -p test_validate_evidence.py -v` | 0 | 11/11 pruebas nuevas superadas | Salida local W01D03 |
| 2 | `python3 -B -m unittest discover -s projects/engineeringos/tests -p test_*.py -v` | 0 | 21/21 pruebas totales superadas | Salida local W01D03 |
| 3 | `python3 -B projects/engineeringos/tools/validate_discovery.py` | 0 | 40/40 comprobaciones | Gate local |
| 4 | `python3 -B projects/engineeringos/tools/validate_planning.py` | 0 | 39/39 comprobaciones | Gate local |
| 5 | `python3 -B projects/engineeringos/tools/validate_evidence.py` | 0 | 46/46 comprobaciones | Gate local |

## Métricas

| Clase | Señal | Valor | Fuente | Interpretación |
|---|---|---|---|---|
| Observada | Pruebas nuevas | 11/11 | Ejecución local | Casos correcto y negativos superados |
| Observada | Pruebas automáticas totales | 21/21 | Ejecución local | Diez pruebas previas y once nuevas superadas |
| Observada | Gate de discovery | 40/40 | Validador local | El contrato previo permanece válido |
| Observada | Gate de planificación | 39/39 | Validador local | Backlog, WIP y DoD permanecen válidos |
| Observada | Gate de evidencia | 46/46 | Ejecución local | El contrato completo es válido |
| Observada | Encabezados de plantilla | 16 | Inspección estructural | La plantilla cubre ejecución, decisión y cierre |
| Objetivo | CI remota | Success | Pull request futura | Debe corresponder al commit PM |

## Decisión y trade-off

| Campo | Contenido |
|---|---|
| Decisión | Usar Markdown versionado y un validador Python sin dependencias externas |
| Alternativa descartada | Formulario externo o herramienta SaaS |
| Ventaja obtenida | Reproducibilidad, revisión con Git y ejecución local o en CI |
| Coste o inconveniente aceptado | La cumplimentación continúa requiriendo juicio humano |
| Criterio de revisión | Revisar la decisión si la carga administrativa supera repetidamente el 15 % |

## Riesgos y limitaciones

| Tipo | Descripción | Mitigación o tratamiento | Estado |
|---|---|---|---|
| Riesgo | Rellenar la plantilla mecánicamente sin aportar trazabilidad real | Pruebas negativas y revisión humana | Mitigado parcialmente |
| Limitación | El validador no decide si una explicación es empresarialmente útil | Revisión humana en issue y PR | Conocida |
| Incidencia resuelta | La normalización con `strip()` no eliminaba delimitadores Markdown internos | Se sustituyó por una eliminación global del carácter delimitador y se probaron tres casos | Resuelta |
| Incidencia resuelta | El cargador dinámico no registraba el módulo en `sys.modules` | Se utilizó `importlib` con registro temporal del módulo | Resuelta |
| Incidencia resuelta | Un heredoc expandible interpretó acentos graves como comandos | Se reconstruyó el archivo mediante un heredoc literal | Resuelta |
| Limitación | La evidencia no puede contener de forma estable el SHA del commit que la incluye | Registrar el SHA PM en Git, PR e issue | Conocida |
| Pendiente | PR, CI, merge y cierre remoto todavía no existen | Ejecutar MB-075 a MB-084 | Abierto |

## Impacto documental

| Superficie revisada | Decisión | Resultado |
|---|---|---|
| `README.md` raíz | Actualizar | Incorporar W01D03 y establecer EOS-005 como siguiente incremento |
| `projects/engineeringos/README.md` | Actualizar | Documentar plantilla, validador, pruebas y gate |
| Changelog | Actualizar | Registrar W01D03 sin eliminar el historial anterior |
| Backlog | Actualizar | Cambiar EOS-004 de En curso a Terminado |
| Definition of Done | Actualizar | Exigir plantilla canónica o excepción documentada |

## Trazabilidad y enlaces canónicos

| Elemento | URL o ruta canónica | Finalidad |
|---|---|---|
| Issue | Registrada en los metadatos superiores | Contrato y criterios |
| Pull request | Pendiente de creación | Revisión e integración |
| CI | Pendiente de ejecución | Validación remota |
| Commit AM | https://github.com/JuanCarlosBP/portfolio/commit/376d9263e4b2a91f2e10e9f4ae87c4ca86e2b50d | Plantilla y estado En curso |
| Commit PM | Mensaje exacto registrado en metadatos | Validación y documentación PM |
| Archivo o evidencia principal | `projects/engineeringos/docs/evidence/w01d03-validation.md` | Evidencia reproducible |

## Siguiente acción

- Ejecutar EOS-005 mediante un ejercicio real de recuperación de contexto que
  reconstruya objetivo, estado, decisiones, bloqueos y siguiente paso usando
  únicamente el repositorio.

## Reglas de uso

1. No presentar objetivos como resultados observados.
2. No declarar métricas sin valor, fuente e interpretación.
3. Conservar el código de salida de los comandos relevantes.
4. Enlazar las fuentes canónicas en vez de copiar información extensa.
5. Mantener visibles riesgos, límites, bloqueos y trabajo pendiente.
6. Revisar todos los archivos README afectados antes del cierre.
7. No afirmar CI verde hasta verificar el SHA correspondiente.
8. Registrar el SHA PM mediante Git, PR e issue; no crear autorreferencias.

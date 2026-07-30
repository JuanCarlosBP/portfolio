# Definition of Done de EngineeringOS

**Proyecto:** EngineeringOS
**Fase:** Discovery y planificación inicial
**Día de trabajo:** W01D02
**Fecha de ejecución:** 2026-07-30
**Issue relacionada:** [#8](https://github.com/JuanCarlosBP/portfolio/issues/8)
**Rama:** `docs/p01-w01d02-backlog-dod`
**Estado:** Validada en W01D02

## Propósito

Establecer las condiciones mínimas y reutilizables que debe cumplir un
incremento de EngineeringOS antes de declararse terminado.

La Definition of Done complementa los criterios de aceptación específicos con
controles comunes de trazabilidad, cambio, validación, calidad, documentación y
entrega.

## Regla general

Un incremento solo está terminado cuando:

1. Todos los criterios obligatorios están cumplidos.
2. Todos los criterios aplicables están cumplidos.
3. Cada criterio no aplicable contiene una justificación verificable.
4. No existen bloqueos incompatibles.
5. La evidencia permite verificar el cierre sin depender de memoria o de una
   explicación oral.

Una tarea `En curso`, `En validación` o `Bloqueada` no está terminada.

## Estados permitidos

| Estado | Significado |
|---|---|
| `Cumplido` | Existe evidencia verificable. |
| `No cumplido` | El criterio aplica, pero está pendiente. |
| `No aplica` | El criterio no corresponde y existe justificación. |
| `Bloqueado` | Un impedimento registrado evita completarlo. |

`No aplica` no puede utilizarse para ocultar trabajo pendiente.

## Núcleo obligatorio literal de la ruta

- [ ] Issue enlazada.
- [ ] Rama correcta.
- [ ] Cambio atómico.
- [ ] Validación ejecutada.
- [ ] CI verde.
- [ ] Documentación coherente.

## Checklist reutilizable

### 1. Problema, alcance y aceptación

- [ ] Existe una necesidad, issue o elemento de backlog.
- [ ] El usuario o destinatario está identificado.
- [ ] El resultado observable está definido.
- [ ] Los criterios de aceptación son verificables.
- [ ] El fuera de alcance está declarado.
- [ ] Las necesidades nuevas no se incorporan silenciosamente.

### 2. Trazabilidad

- [ ] Existe una issue enlazada.
- [ ] La issue contiene contexto, objetivo, aceptación y riesgo.
- [ ] La rama es correcta y parte de una base conocida.
- [ ] Los commits se relacionan con la issue.
- [ ] La pull request enlaza la issue.
- [ ] La evidencia conecta problema, cambio, validación y resultado.

### 3. Cambio realizado

- [ ] El cambio produce el resultado previsto.
- [ ] No contiene archivos vacíos ni scaffolding sin comportamiento.
- [ ] No contiene marcadores pendientes incompatibles.
- [ ] El cambio es atómico.
- [ ] No incluye modificaciones accidentales.
- [ ] El backlog refleja el estado real.

### 4. Validación

- [ ] Se ejecutan las validaciones aplicables.
- [ ] Existe una comprobación del caso correcto.
- [ ] Existen casos incorrectos cuando corresponda.
- [ ] Existe un fallo controlado para el riesgo principal.
- [ ] Se conservan comandos y resultados.
- [ ] Las limitaciones automáticas están documentadas.
- [ ] Existe revisión humana de aspectos no automatizables.

### 5. Calidad y seguridad

- [ ] Pasan los linters y controles de formato aplicables.
- [ ] Pasa el type checking aplicable.
- [ ] Pasan las pruebas aplicables.
- [ ] No se incluyen contraseñas, tokens ni claves privadas.
- [ ] No se publican datos sensibles innecesarios.
- [ ] No se incluyen cachés ni archivos generados accidentales.
- [ ] El repositorio queda limpio.

### 6. Documentación

- [ ] Describe el estado real.
- [ ] Las capacidades futuras aparecen como pendientes.
- [ ] README, ADR, changelog y evidencias son coherentes.
- [ ] Todos los archivos `README.md` afectados fueron revisados y actualizados.
- [ ] Los enlaces, rutas y comandos son válidos.
- [ ] Las métricas distinguen objetivos y resultados.
- [ ] Los riesgos, límites y siguiente acción están registrados.
- [ ] No existen contradicciones.

### 7. Git y GitHub

- [ ] El diff fue revisado.
- [ ] Los archivos preparados fueron revisados.
- [ ] Se realizó una comprobación de secretos.
- [ ] El mensaje del commit expresa el propósito.
- [ ] El commit está publicado en la rama correcta.
- [ ] La pull request tiene origen y destino correctos.
- [ ] La CI aplicable está verde para el SHA entregado.
- [ ] La estrategia de commits acordada se conserva.
- [ ] `main` queda sincronizada y limpia después de integrar.

### 8. Evidencia y cierre

- [ ] Existe una señal útil.
- [ ] La evidencia identifica el SHA.
- [ ] La issue refleja el estado real.
- [ ] Los elementos pendientes permanecen visibles.
- [ ] El siguiente paso está definido.
- [ ] La issue solo se cierra después de integrar y verificar.
- [ ] El cierre puede comprobarse mediante repositorio, PR, CI y documentación.

## Evidencias aceptables

| Criterio | Evidencia |
|---|---|
| Issue enlazada | Número y URL. |
| Rama correcta | Rama y commit base. |
| Cambio atómico | Diff y archivos del commit. |
| Validación ejecutada | Comando, código de salida y resultado. |
| Pruebas | Salida local y CI. |
| CI verde | Workflow, ejecución y SHA coincidente. |
| Documentación coherente | README, ADR, changelog y evidencia. |
| Ausencia de secretos | Inspección del diff y búsqueda automática. |
| Entrega integrada | PR fusionada y commit en `main`. |
| Repositorio limpio | `git status --short --branch`. |

## Uso de No aplica

Debe registrarse:

```text
Criterio:
Estado: No aplica
Justificación:
Evidencia o contexto:
Revisor:
Fecha:
```

No son justificaciones válidas:

- No hubo tiempo.
- Se hará después.
- La herramienta falló.
- El cambio es pequeño.
- Parece innecesario.

## Regla sobre CI

`CI verde` es obligatorio cuando existe un workflow aplicable.

Cuando no exista un workflow aplicable, el incremento debe:

1. Declararlo.
2. Ejecutar validaciones locales reproducibles.
3. Registrar el riesgo.
4. Priorizar la automatización.
5. No afirmar que existe CI verde.

W01D02 debe terminar con CI aplicable y verde.

## Regla sobre atomicidad

Un commit es atómico cuando:

- tiene una finalidad principal;
- puede explicarse mediante un mensaje preciso;
- no mezcla cambios independientes;
- no contiene archivos accidentales;
- deja el repositorio en estado coherente.

## Regla sobre documentación coherente

La documentación debe:

- describir únicamente lo implementado;
- etiquetar claramente lo pendiente;
- utilizar nombres, rutas, métricas y estados coherentes;
- enlazar la evidencia real;
- conservar riesgos y limitaciones.

## Responsabilidad humana

Los validadores no pueden decidir automáticamente:

- si la prioridad empresarial es correcta;
- si el contenido es suficientemente claro;
- si una alternativa fue evaluada con rigor;
- si una métrica demuestra impacto;
- si el resultado es útil para una persona real.

## Condición de cierre

```text
Terminado =
    criterios obligatorios cumplidos
    AND criterios aplicables cumplidos
    AND criterios no aplicables justificados
    AND validaciones superadas
    AND evidencia conservada
    AND ausencia de bloqueos incompatibles
```

Si alguna condición es falsa, el incremento permanece abierto.

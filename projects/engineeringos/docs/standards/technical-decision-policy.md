# Política de decisiones técnicas de EngineeringOS

**Proyecto:** EngineeringOS<br>
**Elemento de backlog:** `EOS-006`<br>
**Día de trabajo:** `W01D05`<br>
**Fecha de ejecución:** `2026-08-05`<br>
**Issue:** [#16](https://github.com/JuanCarlosBP/portfolio/issues/16)<br>
**Estado:** En validación<br>
**Versión de la política:** `1.0.0`

## Propósito

Definir cuándo una decisión técnica exige un registro arquitectónico completo,
cuándo basta una explicación local y cuándo el commit, el diff, las pruebas y
la evidencia ordinaria ya proporcionan trazabilidad suficiente.

La política pretende conservar el razonamiento necesario para reconstruir una
decisión sin convertir cada modificación del repositorio en documentación
arquitectónica.

## Problema que resuelve

EngineeringOS ya contiene decisiones técnicas registradas mediante ADR, pero no
dispone de una regla explícita que permita decidir de forma repetible:

- qué decisiones son suficientemente relevantes para exigir un ADR;
- qué decisiones limitadas necesitan una nota local;
- qué cambios no justifican documentación adicional;
- cuándo una decisión inicialmente pequeña debe escalarse;
- cómo sustituir o declarar obsoleta una decisión anterior.

Sin esta clasificación pueden producirse dos fallos opuestos:

1. decisiones materiales sin contexto, alternativas ni consecuencias;
2. burocracia documental para cambios triviales, mecánicos o reversibles.

## Alcance

Esta política gobierna decisiones relacionadas con:

- arquitectura de EngineeringOS;
- contratos documentales y ejecutables;
- validadores y pruebas;
- automatización y CI;
- estructura de almacenamiento;
- dependencias y servicios;
- seguridad, privacidad y tratamiento de datos;
- costes técnicos recurrentes;
- decisiones que condicionen incrementos posteriores.

## Fuera de alcance

Esta política no implementa:

- EOS-007 · Medición de carga administrativa;
- EOS-008 · CLI local de evidencias;
- EOS-009 · Release reproducible;
- EOS-010 · Interfaz gráfica;
- Jira;
- Confluence;
- servicios externos de documentación;
- validación semántica mediante IA;
- cambios en Sites;
- cambios en la web pública.

## Principio general

La cantidad de documentación debe ser proporcional al impacto, duración,
reversibilidad y riesgo de la decisión.

~~~text
Mayor impacto, duración, coste o irreversibilidad
    → mayor necesidad de contexto conservado.

Menor impacto, alcance local y reversión sencilla
    → registro más ligero.

Cambio trivial o ya gobernado
    → sin documento adicional.
~~~

## Niveles de clasificación

| Nivel | Uso | Ubicación canónica |
|---|---|---|
| `ADR` | Decisión duradera, transversal, material o difícil de revertir. | `projects/engineeringos/docs/adr/ADR-NNNN-*.md` |
| `LOCAL_NOTE` | Decisión limitada a un incremento, reversible y útil para comprender el cambio. | `projects/engineeringos/docs/decisions/local/*.md` |
| `NO_EXTRA_RECORD` | Cambio trivial, mecánico o ya gobernado por una política vigente. | Commit, diff, pruebas o evidencia ordinaria. |

## Regla de precedencia

Cuando una decisión coincida con varios niveles se utilizará el nivel de mayor
trazabilidad:

~~~text
ADR > LOCAL_NOTE > NO_EXTRA_RECORD
~~~

Una nota local no puede utilizarse para evitar un ADR cuando existe un
desencadenante material. La ausencia de registro adicional tampoco puede
utilizarse para ocultar una decisión nueva.

## Algoritmo de clasificación

La clasificación se realiza antes de escribir el documento de decisión.

### Paso 1 · Comprobar si existe una política vigente

Determinar si la operación ya está obligada o resuelta por:

- una política aceptada;
- un ADR vigente;
- la Definition of Done;
- un contrato ejecutable;
- una convención estable del repositorio.

Cuando la respuesta sea afirmativa y no exista una nueva decisión, normalmente
no se necesita un registro adicional.

### Paso 2 · Comprobar si el cambio es trivial

Determinar si el cambio es mecánico, cosmético, ortográfico o incapaz de alterar
el comportamiento observable.

Un cambio trivial puede conservarse mediante commit, diff y pruebas.

### Paso 3 · Evaluar los desencadenantes de ADR

Comprobar uno por uno los diez desencadenantes materiales definidos por esta
política.

La presencia de un solo desencadenante puede exigir ADR cuando su efecto sea
real y no meramente hipotético.

### Paso 4 · Evaluar la necesidad de nota local

Cuando no exista desencadenante de ADR, determinar si la decisión:

- afecta a un único incremento;
- es reversible;
- merece conservar una explicación para revisar el diff;
- no crea una norma arquitectónica general.

### Paso 5 · Registrar la clasificación y su razón

El documento, commit o evidencia debe indicar:

- nivel elegido;
- razón principal;
- desencadenantes evaluados;
- ubicación de la evidencia;
- persona responsable de revisar el cambio.

### Paso 6 · Revaluar cuando cambie el alcance

La clasificación debe repetirse cuando:

- aumente el número de componentes afectados;
- aparezca una dependencia nueva;
- cambie el impacto en seguridad o privacidad;
- la reversión deje de ser sencilla;
- el cambio empiece a condicionar otros incrementos;
- aparezca un coste recurrente no previsto.

## Resultado del algoritmo

~~~text
¿La operación ya está gobernada?
    Sí → NO_EXTRA_RECORD, salvo que exista una decisión nueva.
    No ↓

¿Es trivial y no cambia comportamiento?
    Sí → NO_EXTRA_RECORD.
    No ↓

¿Existe un desencadenante material?
    Sí → ADR.
    No ↓

¿La explicación local mejora la revisión?
    Sí → LOCAL_NOTE.
    No → NO_EXTRA_RECORD.
~~~

## Desencadenantes de ADR

Un ADR es obligatorio cuando exista un impacto material asociado a uno o más de
los siguientes desencadenantes.

| ID | Desencadenante | Motivo | Ejemplo | Evidencia mínima |
|---|---|---|---|---|
| `ADR-01` | Afecta a varios componentes o incrementos. | La decisión deja de ser local y condiciona trabajo posterior. | Cambiar la estructura común de todos los validadores. | Componentes afectados y dependencias. |
| `ADR-02` | Crea o modifica un contrato público. | Otros componentes o usuarios dependerán del nuevo comportamiento. | Modificar el formato canónico de una evidencia. | Contrato anterior, contrato nuevo y migración. |
| `ADR-03` | Introduce una dependencia, servicio o plataforma. | Aparecen mantenimiento, disponibilidad y acoplamiento externos. | Incorporar una librería o servicio de terceros. | Alternativas, versión, coste y estrategia de salida. |
| `ADR-04` | Modifica seguridad, privacidad o tratamiento de datos. | El riesgo supera el alcance de un cambio puramente local. | Almacenar datos nuevos o cambiar permisos. | Datos, amenazas, controles y riesgo residual. |
| `ADR-05` | Introduce un coste recurrente. | El coste condiciona operación y continuidad. | Adoptar una API o plataforma de pago. | Coste esperado, límite y alternativa sin coste. |
| `ADR-06` | Cambia almacenamiento, despliegue, CI o arquitectura. | Modifica una superficie estructural del sistema. | Sustituir el workflow o el formato de persistencia. | Diagrama, flujo anterior y flujo nuevo. |
| `ADR-07` | Es difícil o costosa de revertir. | Una reversión tardía puede exigir migración o pérdida de trabajo. | Cambiar identificadores canónicos ya publicados. | Plan de reversión y coste estimado. |
| `ADR-08` | Existen alternativas con trade-offs materiales. | La elección necesita conservar por qué se aceptó un coste concreto. | Elegir Markdown frente a JSON para un contrato. | Alternativas y consecuencias comparadas. |
| `ADR-09` | Sustituye una decisión arquitectónica anterior. | Debe preservarse la relación histórica entre decisiones. | Reemplazar ADR-0002 por un contrato estructurado. | ADR sustituida y motivo de sustitución. |
| `ADR-10` | Condiciona decisiones técnicas futuras. | La elección actuará como restricción estable. | Adoptar una política general de decisiones. | Alcance futuro y criterio de revisión. |

## Regla de materialidad

La mera aparición de una palabra como «arquitectura», «seguridad» o
«dependencia» no obliga automáticamente a crear un ADR.

Debe existir un efecto observable sobre al menos una de estas dimensiones:

- comportamiento;
- riesgo;
- coste;
- contrato;
- operación;
- reversibilidad;
- mantenimiento;
- decisiones futuras.

## Decisiones urgentes

Una incidencia urgente no elimina la obligación de conservar la decisión.

Cuando no sea posible completar el ADR antes de actuar:

1. registrar la decisión provisional en la issue o evidencia;
2. declarar el riesgo aceptado;
3. definir una fecha o condición de revisión;
4. completar o rechazar el ADR antes de cerrar el incremento.

## Regla de nota local

Una nota local conserva una decisión útil para comprender un incremento sin
convertirla en una norma arquitectónica general.

Solo puede utilizarse cuando se cumplen las seis reglas siguientes.

| ID | Regla |
|---|---|
| `LOCAL-01` | No aplica ningún desencadenante material de ADR. |
| `LOCAL-02` | La decisión afecta a un único incremento o a una superficie claramente delimitada. |
| `LOCAL-03` | La reversión es sencilla, económica y no exige migración. |
| `LOCAL-04` | No cambia contratos externos ni comportamiento público estable. |
| `LOCAL-05` | No introduce dependencia permanente, riesgo de seguridad, tratamiento de datos ni coste recurrente. |
| `LOCAL-06` | La explicación mejora de forma concreta la revisión del diff o la recuperación del contexto. |

## Contenido mínimo de una nota local

Una nota local debe conservar:

1. contexto concreto;
2. decisión adoptada;
3. motivo por el que no exige ADR;
4. alcance y límites;
5. consecuencias observables;
6. forma de reversión;
7. condición que obligaría a escalarla a ADR;
8. issue, rama y evidencia relacionadas.

## Ubicación

~~~text
projects/engineeringos/docs/decisions/local/
~~~

## Nombre de archivo

~~~text
<dia-o-incremento>-<descripcion-breve>.md
~~~

Ejemplo:

~~~text
w01d05-reuse-existing-workflow.md
~~~

## Límite de la nota local

Una nota local no puede:

- crear una política transversal;
- sustituir silenciosamente un ADR;
- omitir un impacto en seguridad o privacidad;
- ocultar una dependencia permanente;
- utilizarse para decisiones difíciles de revertir;
- mantenerse como norma general sin reclasificación.

## Cambios sin registro específico

No se crea ADR ni nota local cuando el cambio ya puede reconstruirse
suficientemente mediante el commit, el diff, las pruebas y la evidencia
ordinaria.

| ID | Caso | Evidencia suficiente |
|---|---|---|
| `TRIV-01` | Corrección ortográfica sin cambio semántico. | Diff y commit. |
| `TRIV-02` | Ajuste de formato Markdown. | Diff y renderizado cuando aplique. |
| `TRIV-03` | Actualización de un enlace sin cambiar el contrato. | Diff y comprobación del enlace. |
| `TRIV-04` | Renombrado puramente mecánico. | Diff, búsqueda de referencias y pruebas. |
| `TRIV-05` | Cambio cosmético sin comportamiento. | Diff y comprobación visual cuando aplique. |
| `TRIV-06` | Refactor que conserva comportamiento y está cubierto por pruebas. | Pruebas antes y después. |
| `TRIV-07` | Operación exigida por una política o ADR vigente. | Enlace a la decisión vigente. |

## Condiciones obligatorias

La ausencia de documento adicional solo es válida cuando:

- no existe una decisión nueva;
- no cambia un contrato;
- no aparece un riesgo nuevo;
- no aumenta el coste;
- no cambia la reversibilidad;
- la evidencia ordinaria permite reconstruir el cambio.

## Regla de escalado

Un cambio inicialmente trivial debe reclasificarse cuando durante su ejecución:

- cambie comportamiento;
- afecte a más componentes;
- exija una excepción;
- altere seguridad o datos;
- introduzca una dependencia;
- requiera una migración;
- genere consecuencias no previstas.

## Contenido obligatorio de un ADR

| ID | Campo | Finalidad |
|---|---|---|
| `ADR-CONTENT-01` | Estado | Indicar si la decisión está propuesta, aceptada, rechazada, sustituida u obsoleta. |
| `ADR-CONTENT-02` | Fecha | Situar la decisión en el tiempo. |
| `ADR-CONTENT-03` | Contexto | Explicar el problema, restricciones y fuerzas relevantes. |
| `ADR-CONTENT-04` | Decisión | Describir con precisión qué se adopta. |
| `ADR-CONTENT-05` | Alternativas consideradas | Conservar opciones reales y por qué no se eligieron. |
| `ADR-CONTENT-06` | Consecuencias | Separar efectos positivos, negativos, riesgos y trabajo posterior. |
| `ADR-CONTENT-07` | Trade-off aceptado | Declarar explícitamente qué coste se acepta para obtener qué ventaja. |
| `ADR-CONTENT-08` | Criterio de revisión | Definir cuándo la decisión debe reabrirse. |

## Metadatos recomendados

Además del contenido obligatorio, cada ADR debe registrar cuando corresponda:

- número y título;
- issue;
- día o incremento relacionado;
- decisión sustituida;
- decisión que lo sustituye;
- componentes afectados;
- responsables;
- enlaces a evidencia y pruebas.

## Calidad de las alternativas

No basta con escribir «no hacer nada» como única alternativa.

Las alternativas deben ser:

- técnicamente posibles;
- relevantes para el problema;
- comparables mediante criterios explícitos;
- descritas sin favorecer artificialmente la opción elegida.

## Calidad de las consecuencias

Las consecuencias deben distinguir:

- efectos positivos;
- efectos negativos;
- riesgos;
- limitaciones;
- deuda aceptada;
- obligaciones futuras.

## Hechos y previsiones

Un ADR debe distinguir entre:

- hechos observados;
- hipótesis;
- previsiones;
- objetivos;
- riesgos.

Una previsión no debe presentarse como resultado verificado.

## Ciclo de vida de una decisión

| Estado | Significado | Transiciones permitidas |
|---|---|---|
| `Propuesta` | La decisión está en revisión y todavía no gobierna el sistema. | Aceptada o Rechazada. |
| `Aceptada` | La decisión gobierna el alcance declarado. | Sustituida u Obsoleta. |
| `Rechazada` | La alternativa fue evaluada y no se adopta. | No gobierna el sistema. |
| `Sustituida` | Otra decisión posterior ocupa su lugar. | Debe enlazar el ADR sucesor. |
| `Obsoleta` | La decisión dejó de ser aplicable sin un reemplazo directo. | Debe explicar por qué desapareció su contexto. |

## Regla de aceptación

Una decisión pasa a `Aceptada` cuando:

- existe una issue o contexto equivalente;
- el documento está completo;
- las alternativas fueron evaluadas;
- las consecuencias están declaradas;
- la validación aplicable ha sido ejecutada;
- el cambio fue integrado o el alcance justifica aceptación previa;
- no existen contradicciones conocidas sin tratamiento.

## Regla de sustitución

Cuando una decisión sustituya otra:

1. el nuevo ADR debe identificar al anterior;
2. el ADR anterior debe cambiar a `Sustituida`;
3. ambos documentos deben enlazarse;
4. debe declararse qué parte deja de ser válida;
5. la historia no debe reescribirse eliminando el ADR anterior.

## Regla de obsolescencia

Un ADR se marca `Obsoleto` cuando:

- desaparece el componente que gobernaba;
- cambia el problema original;
- la decisión ya no tiene aplicación;
- no existe una decisión sucesora directa.

## Cambios sobre decisiones aceptadas

El texto histórico de una decisión aceptada no debe reescribirse para hacerla
parecer correcta con información posterior.

Las correcciones menores pueden añadirse como aclaraciones fechadas. Los cambios
materiales requieren un nuevo ADR.

## Ejemplos de clasificación

| Escenario | Clasificación | Razón principal |
|---|---|---|
| Adoptar una nueva base de datos. | `ADR` | Almacenamiento, migración y reversión material. |
| Cambiar el formato público de una evidencia. | `ADR` | Modifica un contrato utilizado por validadores y personas. |
| Introducir una API de pago. | `ADR` | Dependencia y coste recurrente. |
| Cambiar permisos sobre datos. | `ADR` | Seguridad, privacidad y tratamiento de datos. |
| Reutilizar el workflow existente dentro de un único incremento. | `LOCAL_NOTE` | Decisión limitada, reversible y útil para comprender el diff. |
| Elegir el nombre de un archivo temporal de W01D05. | `LOCAL_NOTE` | No es arquitectónico, pero facilita reconstruir el procedimiento. |
| Corregir una errata. | `NO_EXTRA_RECORD` | No cambia semántica ni comportamiento. |
| Actualizar un enlace roto. | `NO_EXTRA_RECORD` | El diff y la comprobación del enlace son suficientes. |
| Aplicar una regla ya exigida por la DoD. | `NO_EXTRA_RECORD` | No existe una decisión nueva. |

## Escenarios fronterizos

### Refactor interno

Un refactor con comportamiento preservado y pruebas suficientes no exige ADR.

Debe escalarse cuando cambie:

- una interfaz;
- un contrato;
- el modelo de ejecución;
- la arquitectura;
- el riesgo de operación.

### Dependencia de desarrollo

Una dependencia usada exclusivamente durante desarrollo puede ser una nota local
cuando sea fácil de eliminar y no condicione la CI ni el producto.

Exige ADR cuando:

- se vuelve obligatoria para todos los incrementos;
- afecta a la CI;
- introduce coste;
- condiciona versiones;
- requiere mantenimiento permanente.

### Cambio de workflow

Añadir un paso pequeño al workflow existente puede documentarse localmente.

Crear, sustituir o rediseñar la estrategia de CI exige ADR.

## Regla general de escalado

~~~text
Decisión local
    + alcance creciente
    + nueva dependencia
    + contrato estable
    + riesgo material
    + reversión costosa
    = reclasificación a ADR
~~~

## Revisión humana

El validador puede comprobar estructura, marcadores y coherencia literal, pero
no puede decidir automáticamente:

- si el impacto es realmente material;
- si las alternativas son honestas;
- si la prioridad empresarial es correcta;
- si una consecuencia está suficientemente evaluada;
- si la documentación aporta valor real.

La responsabilidad final permanece en la persona que propone y revisa la
decisión.

## Control de burocracia

Antes de crear un documento debe responderse:

1. ¿Qué incertidumbre reducirá?
2. ¿Quién necesitará esta información?
3. ¿Qué decisión no podría reconstruirse mediante el diff?
4. ¿Cuánto tiempo seguirá siendo útil?
5. ¿Qué riesgo existiría si no se documenta?

Cuando estas preguntas no produzcan una utilidad concreta, no debe crearse un
documento adicional.

## Criterio de revisión de esta política

Revisar esta política cuando:

- produzca clasificaciones contradictorias;
- aparezcan falsos positivos frecuentes;
- las notas locales se conviertan sistemáticamente en ADR;
- existan decisiones materiales sin registrar;
- la carga documental supere el valor obtenido;
- cambie la estructura del repositorio;
- EngineeringOS adopte una CLI o formato estructurado para decisiones.

## Trazabilidad

| Elemento | Referencia |
|---|---|
| Backlog | `projects/engineeringos/docs/planning/backlog.md` |
| Definition of Done | `projects/engineeringos/docs/standards/definition-of-done.md` |
| Plantilla ADR | `projects/engineeringos/docs/templates/adr-template.md` |
| Plantilla de nota local | `projects/engineeringos/docs/templates/local-decision-note-template.md` |
| ADR de adopción | `projects/engineeringos/docs/adr/ADR-0003-technical-decision-policy.md` |
| Issue | `#16` |

## Regla de cierre de EOS-006

EOS-006 solo puede declararse terminado cuando:

- la política esté versionada;
- existan las dos plantillas;
- exista un ADR real;
- exista una nota local real;
- doce escenarios hayan sido clasificados;
- no existan contradicciones sin resolver;
- el validador supere 44/44 comprobaciones;
- las pruebas y la CI estén verdes;
- backlog, estado, README, changelog y DoD sean coherentes.

# ADR-0001 · Quality gate ejecutable para el discovery

**Estado:** Aceptada

**Fecha:** 2026-07-25

**Decisión relacionada:** W01D01

**Issue:** [#1](https://github.com/JuanCarlosBP/portfolio/issues/1)

## Contexto

El riesgo principal de W01D01 es convertir EngineeringOS en documentación
extensa sin comportamiento verificable ni utilidad práctica. Los documentos de
discovery aportan contexto, pero por sí solos no impiden cerrar una entrega
incompleta, sin trazabilidad o todavía marcada como borrador.

## Decisión

Crear un quality gate pequeño en Python, sin dependencias externas, que valide un
contrato mínimo y determinista sobre los cuatro documentos de discovery.

El contrato contiene 40 comprobaciones:

- 20 comprobaciones de metadatos comunes.
- 20 comprobaciones de secciones específicas.

El mismo control se ejecutará localmente y en GitHub Actions. Su código tendrá
pruebas automáticas que cubran el caso válido y los fallos principales.

## Alternativas consideradas

### Mantener solo una checklist manual

Descartada porque una checklist puede marcarse sin comprobar el contenido real y
no aporta una ejecución reproducible.

### Añadir más documentación explicativa

Descartada porque aumentaría precisamente el riesgo que se pretende reducir:
más texto sin una señal automática de calidad.

### Adoptar una plataforma externa de gestión o calidad

Descartada en esta fase por coste, dependencia, configuración y alcance
innecesarios para un contrato de discovery pequeño.

### Validación semántica mediante IA

Pospuesta. Puede resultar útil más adelante, pero introduce resultados menos
deterministas, coste y una complejidad que W01D01 no necesita.

## Consecuencias

### Positivas

- El cierre tiene una señal binaria y reproducible.
- Los borradores no pueden superar el gate.
- La issue, el día y el proyecto quedan trazados de forma uniforme.
- El control funciona sin instalar paquetes.
- Los fallos se localizan por documento y requisito.

### Negativas

- La presencia de una sección no garantiza que su contenido sea bueno.
- Cambiar el contrato requiere actualizar código y pruebas.
- Una regla de texto puede necesitar evolución cuando cambie la estructura.

## Trade-off aceptado

Se acepta una validación estructural limitada a cambio de obtener inmediatamente
reproducibilidad, bajo coste y comportamiento verificable. La revisión humana
conserva la responsabilidad sobre la calidad semántica.

## Criterio de revisión

Revisar esta decisión cuando:

- el contrato genere falsos positivos o falsos negativos frecuentes;
- existan varios tipos de discovery con estructuras diferentes;
- la carga de mantener reglas supere el valor de la señal;
- una validación semántica pueda añadirse sin perder determinismo básico.

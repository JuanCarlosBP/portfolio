# JCBP Software — prueba end-to-end del feed verificable

## Objetivo

Comprobar mediante una modificación real que la cadena de evidencia de
JCBP Software funciona desde el repositorio hasta el feed público.

## Flujo validado

1. Una modificación significativa se integra en `main`.
2. El workflow `EngineeringOS discovery quality` ejecuta sus pruebas.
3. La automatización `JCBP Software feed synchronization` detecta el cambio.
4. El feed registra el commit real y la ejecución de CI asociada.
5. Los commits técnicos que actualizan el feed no se muestran como entregas
   profesionales.

## Criterios de aceptación

- La pull request supera el control de calidad de EngineeringOS.
- El mismo control vuelve a ejecutarse tras la fusión en `main`.
- El feed muestra como último commit significativo el commit de la fusión.
- `ci.matchesLatestCommit` queda establecido en `true`.
- El estado público de CI termina en `success`.
- El feed permanece válido y sin degradación.
- Una regeneración posterior sin cambios no crea otro commit técnico.

## Alcance

Este documento es una evidencia técnica controlada. No modifica la lógica de
negocio de EngineeringOS, no despliega el sitio web y no conecta ningún
dominio.

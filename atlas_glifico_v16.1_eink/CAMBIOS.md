# ATLAS GLÍFICO VISUAL v16.1 · e-ink · red farmacodinámica y vectores como áreas

Base: **v16.0 del usuario** (v15.9 + bloque de metabolitos). Sin cambios en `DRUGS`, `aggregate` ni `vectorProfile`.
Reconstrucción: `python3 build.py RUTA/ATLAS_GLIFICO_VISUAL_v16.0.html [SALIDA.html]` (anclas únicas con aserciones).

## Añadido
- **Red farmacodinámica** (`pdnet`): fármaco → diana, estilo de borde según acción (antagonista, inhibidor, agonista parcial, agonista, modulador), grosor según potencia documentada, competición (⇄) y convergencia (▣), umbral, metabolitos, tabla accesible.
- **Vectores clínicos como áreas** (`vectors`): por fármaco, un polígono con cuatro semiejes (activación, sedación, antidepresión/ánimo, antimanía/antipsicosis) alrededor del estado declarado; área conjunta por unión no lineal 1−Π(1−cᵢ); casco convexo y flecha neta opcionales.
- **Matriz de cobertura** de los 167 fármacos (buscable, filtrable, exportable a CSV).
- Figuras (receptoroma, Fountoulakis, mapas): zoom, ajuste automático (mediana de texto ≥ 10 px), pantalla completa, nodos gris claro con texto negro, ramas reforzadas; panel de pauta oculto automáticamente en vistas de figura (conmutador visible).
- Avisos heredados sin función: ocultos (22), recuperables con «Mostrar avisos heredados».

## Tres capas (no se mezclan)
- **O** operativa: la del atlas, intacta.
- **P** potencia documentada: misma fórmula y pesos; modulada por dosis si hay fila activa; exige dirección explícita; excluye baja afinidad, no demostrado, probable, indirecto, preclínico.
- **Q** dirección cualitativa (p. ej. GABA-A PAM → sedación): sin magnitud.
- «—»: sin eje aplicable, con motivo. **No se inventan cifras.**

## Hallazgo estructural
En el atlas H1/α1/M1 tienen `polarEligible=false` para los 167 fármacos, por lo que la sedación operativa vale 0 en todos. La capa P la recupera de forma separada y rotulada.

## Cobertura final (167)
Área 53 · solo dirección 42 · amortiguación (estabilizadores: litio, valproato, lamotrigina, carbamazepina) 4 · sin eje aplicable 68. Los productos con presentación (p. ej. asociaciones de tramadol) se evalúan con su presentación de referencia y 1 unidad/día, indicado en el motivo.
Pimozida, metadona, tramadol y tapentadol no tienen en el atlas dianas NET/SERT/D2 (solo hERG o ninguna): se quedan sin eje por diseño.

## Límites
Ki ≠ ocupación ≠ respuesta clínica. Las áreas son resumen de afinidad documentada, no predicción de efecto ni recomendación terapéutica.

## Revisión posterior (correcciones)
Red: deduplicación por régimen de origen; nodos de componentes en asociaciones fijas; evidencia con `potencyEligible=false` tratada como no numérica; trazo punteado para evidencia ordinal/cualitativa. Vectores: escala según la extensión real; el «centro» pasa a llamarse balance heurístico de componentes. Figuras: el bloqueo de scroll se sincroniza con las figuras abiertas. CSS: columnas fijas solo en escritorio.

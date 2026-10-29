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

## Política de sedación (anti/pro) y capa C
Definida por el usuario; implementada en las capas P/C/Q y, a petición posterior del usuario, **también en la capa O** (ver el apartado siguiente).
- **Antagonismo (anti-):** H1 → sedación (principal) y apetito/peso; α1 → ortostasis/hipotensión y somnolencia añadida (secundaria); M1 → prototipo antimuscarínico (xerostomía, antiperistaltismo/íleo, prodelirium; sedación leve; leve aumento dopaminérgico secundario, por lo que M1 antagonista deja de sumar a «contención»). Ejemplo: clozapina (madre).
- **Agonismo (pro-):** H1 → vigilia; α1 → vigilia/↑ presión arterial (ambos hacia «activación»); M1 → peristaltismo/sialorrea y efecto procognitivo-antipsicótico (hacia «contención»). Ejemplo: norclozapina (metabolito hijo), mostrada como dirección «m» sin magnitud, porque el atlas no calibra exposición de metabolitos.
- **Efectos asociados** (apetito, ortostasis, carga antimuscarínica, vigilia/PA, procolinérgico): columna propia, no ejes. La carga antimuscarínica acepta también M3 y M sin subtipo (los efectos periféricos son mayoritariamente M3), sin forzarlos hacia sedación.
- **Capa C (ordinal clínico):** entradas ordinales/regulatorias (p. ej. periciazina, zuclopentixol, droperidol) con dirección explícita; la magnitud es la ordinal que ya figura en el atlas (no una afinidad) y solo rellena ejes que P deja vacíos. Los «débil»/«baja afinidad» ordinales entran con su magnitud baja; «probable», «indirecto», «preclínico» siguen excluidos.
- **Pesos:** los agonistas usan pesos espejo de los antagonistas (H1 .58 y α1 .18 hacia activación; M1 .24 hacia contención). **Son constantes de modelo sin calibrar**, no datos de fármaco.

## Política en la capa O (cambio sobre `vectorProfile` de la v16.0)
`build.py` sustituye `vectorProfile` (ancla única con aserción). El resto del cálculo de la v16.0 no cambia.
- **Qué cambia:** H1, α1 y M1 dejan de excluirse por `polarEligible=false`; se leen por `operationalEligible`, con dosis (`value`), solo fármaco madre/componente (sin PET, cualitativos ni metabolitos) y sin textos de baja afinidad, probables, indirectos o preclínicos. Los ordinales débiles conservan su magnitud baja.
- **Fórmulas:** sedación = H1⊣ .58 + M1⊣ .24 + α1⊣ .18; activación = original + H1⊕ .58 + α1⊕ .18; contención = original con H1⊣ .14 + M1⊕ .24 (el M1⊣ deja de sumar contención). Los pesos de agonistas son espejo, sin calibrar.
- **Efecto medido (167 fármacos):** la sedación operativa pasa de 1 fármaco con valor a **27** (O 27 · Q 30 · sin dato 110). Ejemplos del vector (x, y) antes → después: olanzapina (0,00; −3,21) → (−5,13; −3,91); clozapina (0,00; −2,06) → (−4,62; −2,73); cariprazina (1,42; 1,11) → (−0,33; 0,68); haloperidol sin cambios.
- **Vistas afectadas:** todas las que leen `vectorProfile` (campo de polaridad, trayectoria, comparación A/B, informe). Es un cambio de comportamiento respecto a la v16.0.
- **Para volver al cálculo anterior:** quitar el bloque «capa O» de `build.py` y reconstruir.

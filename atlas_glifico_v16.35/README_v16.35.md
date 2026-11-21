# ATLAS GLÍFICO v16.35 · ampliación de las alertas de interacción

Reconstrucción: `node build_v1635.mjs ../ATLAS_GLIFICO_VISUAL_v16.34.html` (exige el SHA-256 de la v16.34).

Amplía el bloque «Alertas de interacción» de la v16.34 con nuevas combinaciones de dos o más fármacos. Mismos niveles (⛔ contraindicación · ⚠ precaución mayor · ◇ vigilancia) y mismo principio: avisos por presencia en la pauta, sin cálculo de exposición. Fuentes: fichas técnicas CIMA (consulta 12-11-2026).

| Grupo | Regla | Nivel | Fuente |
|---|---|---|---|
| Depresión SNC/respiratoria | Opioide + benzodiacepina o hipnótico Z | ⚠ | FT oxicodona 4.4; FT zolpidem 4.4 |
| | Opioide + gabapentinoide | ⚠ | FT gabapentina 4.4; FT Lyrica 4.4 (también estreñimiento/íleo) |
| | Clozapina + benzodiacepina (colapso circulatorio) | ⚠ | FT clozapina 4.5 |
| | ≥ 2 benzodiacepinas/Z | ◇ | FT diazepam |
| | Benzodiacepina/Z + gabapentinoide | ◇ | FT gabapentina |
| Eutimizantes | Valproato + lamotrigina (semivida ≈ ×2; exantema grave) | ⚠ | FT lamotrigina 4.4/4.5 |
| | Valproato + topiramato (encefalopatía, hiperamonemia) | ⚠ | FT ácido valproico 4.5 |
| | Valproato + carbamazepina (toxicidad, epóxido) | ⚠ | FT ácido valproico 4.5 |
| | Litio + antipsicótico (no recomendado; neurotoxicidad) | ⚠ | FT Plenur 4.4/4.5 |
| | Litio + AINE/COX-2 (litemia) | ⚠ | FT Plenur 4.5 |
| Inductores (carbamazepina, fenitoína, fenobarbital, primidona) | + lurasidona | ⛔ | FT lurasidona 4.3 |
| | + cariprazina | ⛔ | FT Reagila 4.3 |
| | + quetiapina, + aripiprazol, + lamotrigina (menor exposición) | ⚠ | FT quetiapina, aripiprazol, lamotrigina 4.5 |
| IMAO | Tranilcipromina + metilfenidato/anfetaminas (crisis hipertensiva) | ⛔ | FT metilfenidato 4.3 |
| | Bupropión + cualquier IMAO | ⛔ | FT bupropión 4.3 |
| | Tetrabenazina + IMAO | ⛔ | FT Nitoman 4.3 |
| | Tetrabenazina + antipsicótico (QTc, SNM, EPS) | ⚠ | FT Nitoman 4.4 |
| Sodio y sangrado | ≥ 2 que bajan el sodio (ISRS/IRSN, carbamazepina, oxcarbazepina, eslicarbazepina) | ◇ | FT Besitran, carbamazepina, oxcarbazepina 4.4 |
| | ISRS/IRSN + AINE o valproato | ⚠ | FT Besitran 4.4 |
| Cargas de clase | ≥ 2 con riesgo metabólico | ◇ | FT olanzapina 4.4 |
| | ≥ 2 que elevan la prolactina | ◇ | FT amisulprida 4.4 |
| | ≥ 2 con riesgo extrapiramidal (también SNM) | ◇ | FT Nitoman 4.4 |
| | ≥ 2 con bloqueo α1 o agonismo α2 (ortostatismo) | ◇ | FT Minipres 4.4 |

Familias calculadas con los datos del atlas (etiquetas de riesgo, diana D2 en la familia de antipsicóticos, antagonismo α1 operativo) y completadas por nombre cuando la afinidad del atlas no basta (p. ej., quetiapina como antipsicótico). Si una contraindicación pareja a pareja heredada queda cubierta por una regla nueva con su ficha, se muestra una sola vez.

## Verificación
- 18 escenarios con la respuesta esperada (incluida una pauta sin alertas).
- 86 visitas por la barra sin errores; móvil a 390 px sin desbordes; sin bucles en reposo; alertas actualizadas desde la interfaz.
- Comparación de vistas v16.34 → v16.35 (641 combinaciones): idénticas salvo 2-4 entradas de la lente oculta «safety», que varían entre ejecuciones (temporización del renderizado), no por esta versión.

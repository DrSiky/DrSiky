# ATLAS GLÍFICO v16.34 · alertas de interacción por familia

Reconstrucción: `node build_v1634.mjs ../ATLAS_GLIFICO_VISUAL_v16.33.html` (exige el SHA-256 de la v16.33; anclas únicas).

Bloque **«Alertas de interacción»** bajo la pauta, siempre visible, con tres niveles (⛔ contraindicación · ⚠ precaución mayor · ◇ vigilancia). Avisos por presencia en la pauta: no calculan exposición, lavado ni dosis compensatoria, y no sustituyen la ficha. Las familias se construyen con los datos del atlas (etiquetas de riesgo, SERT, antagonismo muscarínico) y se completan con lo verificado en ficha. No se modelan porcentajes por citocromo, unión a proteínas ni eliminación renal (decisión del usuario).

## Reglas y fuentes (fichas técnicas CIMA, apartados 4.3/4.4/4.5, consulta 12-11-2026)

| Familia | Regla | Nivel | Fuente |
|---|---|---|---|
| Síndrome serotoninérgico | IMAO no selectivo (tranilcipromina, moclobemida) + cualquier serotoninérgico | ⛔ | FT fluvoxamina, duloxetina, citalopram |
| | Selegilina + ISRS/IRSN/tricíclicos/opioides | ⛔ | FT Plurimen |
| | Rasagilina o safinamida + otro IMAO o petidina | ⛔ | FT rasagilina, Xadago |
| | Rasagilina o safinamida + fluoxetina/fluvoxamina; rasagilina + dextrometorfano | ⚠ | ídem |
| | Rasagilina o safinamida + otros antidepresivos serotoninérgicos | ◇ | ídem |
| | ≥ 2 serotoninérgicos (ISRS, IRSN, tricíclicos, tramadol, buprenorfina, litio…) | ◇ | FT fluvoxamina, Plenur, Adolonta |
| QT | Citalopram o escitalopram + otro fármaco que prolonga QT | ⛔ | FT citalopram, escitalopram (4.3) |
| | ≥ 2 fármacos QT con alguno de alto riesgo (QT en 4.3 o torsades) | ⚠ | FT ondansetrón, Eptadone |
| | ≥ 2 fármacos QT sin alto riesgo | ◇ | ídem |
| Umbral convulsivo | Bupropión + fármacos que lo reducen | ⚠ | FT bupropión |
| | ≥ 2 fármacos con advertencia de convulsiones | ◇ | FT Adolonta, bupropión |
| Carga anticolinérgica | ≥ 2 antagonistas muscarínicos | ◇ (⚠ con clozapina) | FT clozapina |
| Agranulocitosis | Clozapina + carbamazepina | ⛔ | FT clozapina 4.5 |
| Fluvoxamina · CYP1A2 | + duloxetina (≈ 6 × AUC) | ⛔ | FT duloxetina 4.3 |
| | + agomelatina (≈ 60 × exposición) | ⛔ | FT agomelatina 4.3 |
| | + clomipramina, imipramina, amitriptilina, clozapina, olanzapina, quetiapina, propranolol, ropinirol | ⚠ | FT fluvoxamina 4.5, olanzapina, Anafranil |
| | + clonidina (vía menor) | ◇ | Claessens 2010, Drug Metab Dispos (no figura en la FT de fluvoxamina) |
| | Xantinas: cafeína y teofilina (fuera del catálogo) | ◇ | FT fluvoxamina 4.5 |
| CYP2D6 | Fluoxetina, paroxetina o bupropión + sustratos 2D6 de la pauta | ⚠ | FT fluoxetina, Frosinor, bupropión |
| Previas | Contraindicaciones pareja a pareja de tranilcipromina, moclobemida y pimozida | ⛔ | ya existentes en el atlas |

**Familia QT ampliada** con fichas que advierten del QT y no tenían la marca: quetiapina, olanzapina, clozapina, paroxetina, ondansetrón, hidroxizina. Aripiprazol no se añade (su ficha describe una incidencia comparable a placebo).

**Manejo del síndrome serotoninérgico** (texto en cada alerta serotoninérgica): retirar los agentes, soporte y benzodiacepinas; en casos moderados o graves se han usado antagonistas 5-HT2A (ciproheptadina; también clorpromazina u olanzapina), con evidencia de casos y series y sin eficacia demostrada (Chiew e Isbister, Br J Clin Pharmacol 2025, DOI 10.1111/bcp.16152; King y Rotella, revisión sistemática, Emerg Med Australas 2025, DOI 10.1111/1742-6723.14554). El antagonismo 5-HT1A de la ciproheptadina no está documentado en el atlas ni en las fuentes consultadas; solo H1, 5-HT2A y muscarínico (ficha CIMA).

## Verificación

- 13 escenarios de prueba con la respuesta esperada (IMAO, selegilina, rasagilina, carga serotoninérgica, QT, bupropión, anticolinérgicos, clozapina + carbamazepina, fluvoxamina, CYP2D6, pimozida, pauta sin alertas).
- Las alertas se actualizan al cambiar la pauta desde la interfaz.
- 86 visitas por la barra sin errores; móvil a 390 px sin desbordes; sin bucles de observadores en reposo.
- Comparación v16.33 → v16.34 en 641 combinaciones vista × lente × pauta: idénticas (el bloque de alertas vive en la columna de la pauta).

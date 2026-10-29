# Auditoría de textos de acción (12 dianas del modelo)

Archivo de detalle: `AUDITORIA_textos_accion.csv` (94 relaciones de fármaco madre/componente, sin PET, cuyo texto no produce dirección). Generada sobre los 167 fármacos con la dosis nominal y la presentación de referencia.

| Categoría | Relaciones |
|---|---|
| Excluidas por texto (débil, probable, indirecto, preclínico…) | 50 |
| Sin dirección reconocible, numéricas | 29 |
| Sin dirección reconocible, cualitativas | 14 |
| Sin dirección reconocible, ordinales | 1 |

## Correcciones de lectura ya aplicadas
- «Adrenolítico marcado» (periciazina, α1, ordinal) se lee ahora como antagonismo α1. Efecto: la sedación O de periciazina pasa de 0,49 a 0,64.
- Los ordinales «débiles» (p. ej. zuclopentixol, H1) entran en «Efectos asociados» con su magnitud baja, como ya hacía la capa O.

## Lo que está bien excluido
La mayoría de las 29 numéricas son uniones sin función establecida («Unión a NET mínima», «Afinidad 5-HT1A baja», «relevancia funcional no establecida»): no deben generar dirección.

## Decisiones de modelo pendientes (no son errores de lectura)
1. **Agonismo parcial D2** (cariprazina, brexpiprazol, aripiprazol): hoy no aporta a ningún eje; solo el antagonismo D2 suma «contención». ¿Debe un agonista parcial D2/D3 contar como contención, activación o ninguno?
2. **Antagonismo 5-HT1A** (asenapina, iloperidona): el modelo solo usa agonismo 5-HT1A.
3. **Agonistas D2 completos** (bromocriptina, cabergolina, apomorfina…): no tienen eje; ¿activación/pro-monoaminérgico?

# ATLAS GLÍFICO v16.41 · componente antidepresivo con ancla clínica

Reconstrucción: `node build_v1641.mjs ../ATLAS_GLIFICO_VISUAL_v16.40.html` (exige el SHA-256 de la v16.40; anclas únicas).

Decisiones del usuario: (1c) el ancla depende de la lente; (2b) la eficacia solo como coadyuvante se acredita siempre, con etiqueta; (3) el término clínico se basa en el tamaño de efecto.

## Problema de la v16.40
- Diez antidepresivos tenían componente antidepresivo 0 (agomelatina, mirtazapina, moclobemida, tranilcipromina, tianeptina, esketamina, levomilnacipran, desipramina, maprotilina, trimipramina): su mecanismo no pasa por las dianas del vector o el atlas lo tiene solo como dato cualitativo.
- El valor más alto era el de brexpiprazol (0,338), por agonismo 5-HT1A y D3.
- Quetiapina, olanzapina y lamotrigina, eficaces en depresión bipolar, valían 0.

## Fórmula (capa O)
1. **Mecanístico** (sin cambios): NET 0,24 + SERT 0,14 + agonismo 5-HT1A 0,23 + agonismo D3 0,16 + DAT 0,10 + MAO-A 0,13.
2. **Ancla clínica por fármaco y lente.** Solo los fármacos acreditados mueven el punto; el resto queda en el segmento.
   - Lente bipolar → evidencia en depresión bipolar aguda.
   - Demás lentes → evidencia en depresión unipolar.
3. **Término clínico**, solo para acreditados cuyo vector no tiene magnitud: 0,24 × (DME ÷ 0,418) × escala de dosis (f^0,55, la de `aggregate()`).
   - Escala común: DME. Las OR se convierten con ln(OR) ÷ 1,81 (Chinn 2000, doi:10.1002/1097-0258(20001130)19:22<3127::aid-sim784>3.0.co;2-m).
   - 0,418 = amitriptilina (OR 2,13), la mayor de Cipriani 2018.
   - Sin tamaño de efecto publicado en la fuente → se usa el menor de Cipriani 2018 (reboxetina, OR 1,37 → 0,174), marcado «mínimo».
4. **Tope en coadyuvantes con magnitud en el vector** (aripiprazol, brexpiprazol, cariprazina): lo acreditado no supera 0,24 × (DME ÷ 0,418). Es una extensión de la decisión 3, no pedida expresamente; se retira eliminando el cálculo de `cap` en `v1641Model`.
5. Vertical del mapa = 7 × (antidepresivo acreditado − antimaníaco acreditado). Dos segmentos: hacia arriba el antidepresivo mecanístico no acreditado, hacia abajo el antimaníaco.

## Ancla en depresión unipolar
| Categoría | Fármacos | Fuente |
|---|---|---|
| Demostrada | amitriptilina 2,13 · mirtazapina 1,89 · duloxetina 1,85 · venlafaxina 1,78 · paroxetina 1,75 · fluvoxamina 1,69 · escitalopram 1,68 · sertralina 1,67 · vortioxetina 1,66 · agomelatina 1,65 · vilazodona 1,60 · levomilnacipran 1,59 · bupropión 1,58 · fluoxetina 1,52 · citalopram 1,52 · trazodona 1,51 · clomipramina 1,49 · desvenlafaxina 1,49 · reboxetina 1,37 (OR frente a placebo) | Cipriani 2018, figura 3, doi:10.1016/S0140-6736(17)32802-7 |
| | tranilcipromina (log OR 0,509; 4 estudios) | Ricken 2017, doi:10.1016/j.euroneuro.2017.04.003 |
| | moclobemida (superior a placebo; sin cifra en el resumen) | Lotufo-Neto 1999, doi:10.1016/S0893-133X(98)00075-X; FT Manerix |
| | lurasidona (un ECA en depresión mayor con rasgos mixtos; tamaño de efecto 0,80) | Suppes 2016, doi:10.1176/appi.ajp.2015.15060770 |
| Ficha técnica española | imipramina, nortriptilina, doxepina, trimipramina, mianserina, tianeptina | CIMA 4.1 (consulta 20-11-2026) |
| Solo coadyuvante | quetiapina DME 0,40 · olanzapina 0,35 · aripiprazol 0,28 · brexpiprazol 0,25 | Wang 2023, doi:10.1097/MD.0000000000034670 |
| | risperidona OR 2,17 · cariprazina OR 1,34 (no eficaz en remisión) | Yan 2022, doi:10.1017/S0033291722001246 |
| | litio, modafinilo, lisdexanfetamina (respuesta superior a placebo; sin cifra en el resumen) | Nuñez 2022, doi:10.1016/j.jad.2021.12.134; FT Plenur |
| | esketamina (−2,94 MADRS a 4 semanas; «small») | Naudet 2025, doi:10.1186/s12916-025-04435-x; FT Spravato |
| Negativa | ziprasidona | Yan 2022 |
| Sin ancla localizada | desipramina, maprotilina | sin presentación comercializada ni metaanálisis frente a placebo localizado |

## Ancla en depresión bipolar
| Categoría | Fármacos | Fuente |
|---|---|---|
| Demostrada | quetiapina, olanzapina, lurasidona, cariprazina, lamotrigina (DME 0,16); olanzapina + fluoxetina (DME 0,41) | Yildiz 2023, doi:10.1016/S2215-0366(23)00199-2; Kadakia 2021, doi:10.1186/s12888-021-03220-3 |
| Antidepresivos (familia N06) | no se acreditan: «as a class seem to be efficacious, but had a higher risk for manic switch», confianza baja | Yildiz 2023 |
| Negativa | aripiprazol, ziprasidona | Vázquez 2015, doi:10.1016/j.jad.2015.05.016; Kadakia 2021 |
| Insuficiente | litio | Vázquez 2015 |
| Sin ancla | brexpiprazol (piloto abierto, n = 21) | Brown 2019, doi:10.1016/j.jad.2019.02.056 |

**Magnitud no verificada por fármaco:** el resumen de Yildiz 2023 solo da el intervalo de DME (0,16–0,41). Para quetiapina y olanzapina se usa el punto medio (0,285), indicado en la etiqueta; Kadakia 2021 da −4,80 y −4,57 puntos MADRS.

## Efecto a dosis por defecto
| Fármaco | v16.40 | Lente no bipolar | Lente bipolar (acreditado · mecanístico) |
|---|---|---|---|
| Brexpiprazol 2 | 0,338 | 0,144 (tope) | 0 · 0,338 |
| Aripiprazol 10 | 0,264 | 0,161 (tope) | 0 · 0,264 |
| Ziprasidona 80 | 0,179 | 0 · mec. 0,179 | 0 · 0,179 |
| Mirtazapina 15 | 0 | 0,141 | 0 · 0 |
| Agomelatina 25 | 0 | 0,138 | 0 · 0 |
| Tranilcipromina 30 | 0 | 0,140 | 0 · 0 |
| Quetiapina 300 | 0 | 0,171 | 0,121 |
| Olanzapina 10 | 0 | 0,175 | 0,142 |
| Lamotrigina 200 | 0 | 0 | 0,080 |
| Sertralina 50 | 0,083 | 0,083 | 0 · 0,083 |
| Lurasidona 37 | 0,115 | 0,115 | 0,115 |

- 18 entidades cambian en las lentes no bipolares y 26 en la bipolar.
- Los ejes de activación y sedación, el antimaníaco y las capas P y Q no cambian.

## Verificación
- El mecanístico coincide con la v16.40 en las 170 entidades (diferencia 3 × 10⁻¹⁷), salvo el término clínico.
- El desglose reproduce `vectorProfile` (acreditado y mecanístico, antidepresivo y antimaníaco) en las 170 entidades y en una combinación de cuatro fármacos, en ambas lentes: diferencia 0.
- Ningún fármaco con magnitud antidepresiva queda sin ancla revisada.
- Al cambiar de lente se actualizan mapa, Proyecciones (base O) y desglose.
- 86 visitas por la barra sin errores; móvil a 390 px sin desbordes.
- Las cifras de Cipriani 2018 se leyeron de la figura 3 (Europe PMC). Los siete artículos que deciden categoría o magnitud se verificaron directamente en PubMed.

## Limitaciones
- Los acreditados con magnitud propia conservan su valor mecanístico, sin escalar por tamaño de efecto: sertralina 50 mg (0,083) queda por debajo de risperidona 2 mg como coadyuvante (0,171). Escalar todos por tamaño de efecto sería un cambio de criterio.
- Sin umbral de dosis: quetiapina 50 mg conserva crédito (0,064 unipolar), aunque la ficha sitúa el tratamiento adicional en 150–300 mg.
- En la lente bipolar, los antidepresivos sin magnitud en el vector (mirtazapina, agomelatina…) no muestran segmento.
- Lumateperona no está en el atlas.

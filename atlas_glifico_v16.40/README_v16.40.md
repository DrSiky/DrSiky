# ATLAS GLÍFICO v16.40 · el antagonismo 5-HT2A queda solo como mecanismo en el componente antimaníaco

Reconstrucción: `node build_v1640.mjs ../ATLAS_GLIFICO_VISUAL_v16.39.html` (exige el SHA-256 de la v16.39; anclas únicas).

Decisión del usuario: opción (b). El término 5-HT2A (peso 0,14, heredado de la v16.0) deja de mover el punto del mapa (acreditado 0) y se conserva en el antimaníaco mecanístico, dibujado como segmento.

## Motivos
- No hay ECA de antagonistas 5-HT2A selectivos en monoterapia para la manía. El único ECA controlado es coadyuvante: ritanserina añadida a litio + haloperidol, n = 45 (Akhondzadeh 2003, doi:10.1186/1471-244X-3-7).
- En Cipriani 2011 (doi:10.1016/S0140-6736(11)60873-8) el haloperidol, sin antagonismo 5-HT2A, tiene la mayor DME (−0,56) y fue superior a quetiapina, aripiprazol, asenapina y ziprasidona.
- Exploración propia, con 7 antipsicóticos a dosis habituales en ensayos de manía elegidas editorialmente: la correlación entre la señal 5-HT2A del atlas y la DME es negativa (Spearman −0,50). Con n = 7 y dosis heterogéneas no es una prueba; solo indica que el término no reproduce el orden de eficacia. El componente sin 5-HT2A tampoco lo reproduce (Spearman +0,09).

## Efecto (antimaníaco acreditado · mecanístico)
| Pauta | v16.39 | v16.40 |
|---|---|---|
| Haloperidol 10 | 0,474 | 0,474 · 0,474 |
| Risperidona 4 | 0,668 | 0,531 · 0,668 |
| Olanzapina 15 | 0,461 | 0,327 · 0,461 |
| Quetiapina 600 | 0,286 | 0,182 · 0,286 |
| Aripiprazol 15 | 0,340 | 0,231 · 0,340 |
| Asenapina 20 | 0,706 | 0,568 · 0,706 |
| Ziprasidona 120 | 0,494 | 0,357 · 0,494 |
| Iloperidona 12 | 0,525 | 0,422 · 0,525 |
| Clozapina 300 | 0,294 | 0,211 · 0,294 |

- La capa P (potencia intrínseca) no cambia.
- Desglose: el término aparece con aporte 0 y origen «solo mecanístico · no acreditado», con una nota y sus fuentes.
- Mapa: cuando el vector supera el borde del campo (±10), la tarjeta lateral lo indica. Antes, el recorte heredado podía superponer punto y segmento en el borde, sin que se viera que había segmento.

## Verificación
- El desglose reproduce `vectorProfile` en las 170 entidades (diferencia máxima 0).
- 86 visitas por la barra sin errores; móvil a 390 px sin desbordes.

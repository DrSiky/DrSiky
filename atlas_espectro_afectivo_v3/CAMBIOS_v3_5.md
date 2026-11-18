# Atlas clínico-geométrico del espectro afectivo — v3.4 → v3.5 (Ampliación VI: grafismo farmacológico)

Fecha: 18 noviembre 2026. De 95 a **103 páginas**: ocho páginas nuevas (72–79) con tipos de gráfico que el atlas no tenía.
Usan solo datos ya extraídos de los dosieres D01–D13 y síntesis ya verificadas (P83–P91). No hay referencias nuevas.

Regenerar: `python3 build_v35.py ATLAS_..._v2.pdf ATLAS_..._v3.pdf ATLAS_..._v3_5.pdf`

| Pág. | Contenido | Grafismo nuevo |
|---|---|---|
| 72 | Posición en las guías por fase (CANMAT/ISBD 2023 y NICE CG185, según los dosieres) | Mapa de calor de líneas de recomendación, con adición y depot |
| 73 | Titulación hasta la dosis de referencia | Curvas en escalón normalizadas en escala de raíz cuadrada |
| 74 | Mantenimiento: medianas hasta la recaída y NNT bruto | Pares fármaco–placebo en escala logarítmica; NNT en piruleta |
| 75 | Fase aguda: NNT en manía y depresión, junto a los NNT de P85 | NNT agrupados por polo |
| 76 | Brújula preventiva: prevención maníaca frente a depresiva | Diagrama de dispersión log-log con IC en cruz y diagonal de equilibrio |
| 77 | Carga metabólica y endocrina | Gráfico de bosque de peso (P85) y pares fármaco–comparador |
| 78 | **Lámina Curso 16** · lamotrigina: titulación y prevención depresiva | Lámina longitudinal con dos marcadores |
| 79 | Mapa de ocho preguntas antes de elegir (no es un algoritmo) | Diagrama de flujo con remisiones a páginas |

Además: guía (p. 80) con remisión a pp. 72–79, índice de 12 filas y pie de enlace de la p. 20 actualizado.

## Rigor

- Los NNT de las pp. 74–75 son cálculos brutos del atlas (1 / diferencia absoluta de proporciones publicadas), sin intervalo ni ajuste. Se marcan G/I y la p. 74 explica por qué los diseños enriquecidos abaratan el NNT de mantenimiento.
- Las medianas no se usan para reconstruir curvas de Kaplan-Meier, siguiendo la advertencia de los dosieres.
- «Sin línea» en el mapa de guías significa que el dosier no la recoge, no que la guía la desaconseje.
- La p. 76 compara cada ensayo con su placebo. Los episodios índice y los diseños difieren, y así se indica.

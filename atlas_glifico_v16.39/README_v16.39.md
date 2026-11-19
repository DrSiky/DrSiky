# ATLAS GLÍFICO v16.39 · ancla clínica de los antipsicóticos sin ancla revisada

Reconstrucción: `node build_v1639.mjs ../ATLAS_GLIFICO_VISUAL_v16.38.html` (exige el SHA-256 de la v16.38; anclas únicas).

Decisión del usuario: la eficacia demostrada solo frente a un comparador activo, sin placebo, **se acredita** con etiqueta propia (opción a).

## Clasificación (PubMed y CIMA, noviembre de 2026)
| Fármaco | Categoría | Crédito | Evidencia |
|---|---|---|---|
| Iloperidona | eficacia demostrada | sí | ECA fase 3 frente a placebo, n = 414, YMRS −4,0 (Torres 2024, doi:10.4088/JCP.23m14966). Sin comercialización en España |
| Clorpromazina | solo comparador activo | sí | ECA doble ciego frente a litio, en el que resultó inferior al litio (Takahashi 1975, doi:10.1001/archpsyc.1975.01760280108010); frente a litio y haloperidol (Shopsin 1975, doi:10.1001/archpsyc.1975.01760190036004). El metaanálisis en red de Asia oriental no halla diferencia frente a placebo (Ishizuka 2022, doi:10.1002/pcn5.60). La FT Largactil incluye las «crisis maniacas» entre los estados de agitación |
| Clozapina | solo comparador activo | sí | ECA abierto frente a clorpromazina, ambos con litio, n = 30 (Barbini 1997, doi:10.1097/00004850-199703000-00006) |
| Amisulprida | solo comparador activo | sí | ECA abierto frente a haloperidol, ambos con valproato, n = 123 (Thomas 2008, doi:10.2147/ndt.s3135) |
| Loxapina | solo agitación | no | ECA frente a placebo en agitación del trastorno bipolar I, inhalada, n = 314 (Kwentus 2012, doi:10.1111/j.1399-5618.2011.00975.x); la FT Adasuve la autoriza para la agitación |
| Droperidol | solo agitación | no | ECA en agitación con diagnósticos mezclados (Khokhar 2016, Cochrane, doi:10.1002/14651858.CD002830.pub3); la FT española solo autoriza náuseas y vómitos |
| Perfenazina | sin ECA en manía aguda | no | Único ECA frente a placebo: continuación tras la remisión, con resultado perjudicial (Zarate 2004, doi:10.1176/appi.ajp.161.1.169) |
| Sulpirida | sin ECA en manía aguda | no | Estudio abierto, n = 8 (Christie 1989, doi:10.1016/0165-0327(89)90064-5) |
| Clotiapina | sin ECA en manía aguda | no | Cochrane de psicosis aguda sin placebo ni datos de manía (Carpenter 2001, doi:10.1002/14651858.CD002304) |
| Levosulpirida, tiaprida, sertindol, flufenazina, periciazina | sin ECA en manía aguda | no | Búsqueda sin ensayos controlados en manía; una búsqueda no prueba la ausencia |

Agitación aguda no equivale a eficacia antimaníaca; la sedación tiene su propio eje.

## Efecto
- Los no acreditados dejan de mover el punto; su bloqueo D2 queda en el segmento mecanístico. Siguen compitiendo por el receptor: con un antagonista acreditado, este conserva su crédito (haloperidol 10 + perfenazina 8: acreditado 0,474, igual que haloperidol solo; mecanístico 0,588).
- Ya no queda ningún fármaco con aporte antimaníaco en la categoría «sin ancla revisada».

## Verificación
- Las 14 categorías se comprobaron en el atlas a sus dosis por defecto.
- El desglose reproduce `vectorProfile` en las 170 entidades (diferencia máxima 0).
- 86 visitas por la barra sin errores; móvil a 390 px sin desbordes.
- Los ocho artículos que deciden categoría y las tres revisiones o estudios citados se verificaron directamente en PubMed. Los ensayos de clorpromazina anteriores a 1975 sin resumen no se usan.

## Pendiente
- Peso 0,14 del antagonismo 5-HT2A en el componente antimaníaco de los antipsicóticos (heredado de la v16.0).

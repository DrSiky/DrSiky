# ATLAS GLÍFICO v16.38 · crédito antimaníaco del antagonismo 5-HT2A en antidepresivos

Reconstrucción: `node build_v1638.mjs ../ATLAS_GLIFICO_VISUAL_v16.37.html` (exige el SHA-256 de la v16.37; anclas únicas).

## Diagnóstico (v16.37)
- Solo dos antidepresivos recibían crédito antimaníaco, ambos por antagonismo 5-HT2A (peso heredado 0,14): **mirtazapina** (0,062 a 15 mg; 0,099 a 45 mg) y **trazodona** (0,064 a 100 mg; 0,120 a 400 mg).
- Tricíclicos (amitriptilina, clomipramina, imipramina, nortriptilina), mianserina y agomelatina tienen datos 5-HT2A, pero marcados como «función no tipificada», «5-HT2 sin subtipo» o «afinidad mínima», y no entran en el vector. Hasta ahora, solo los dos antidepresivos con antagonismo tipificado ganaban crédito antimaníaco.

## Evidencia
- No consta eficacia antimaníaca de ningún antidepresivo. La búsqueda en PubMed no encontró ensayos de antagonistas 5-HT2A selectivos en monoterapia para la manía. Solo hay un ECA pequeño de ritanserina **añadida** a litio + haloperidol (n = 45; Akhondzadeh 2003, doi:10.1186/1471-244X-3-7), que no sirve para acreditar el mecanismo aislado.
- Fichas técnicas (CIMA, 4.4):
  - Mirtazapina (nº 86890): la fase depresiva del trastorno bipolar «puede transformarse en fase maníaca»; si ocurre, debe abandonarse el tratamiento.
  - Trazodona (nº 83568): «una fase depresiva puede cambiar … a una fase maníaca»; debe retirarse.
- Casos publicados de manía inducida: mirtazapina (Bhanji 2002, doi:10.1097/00004850-200211000-00009) y trazodona (Warren y Bick 1984, doi:10.1176/ajp.141.9.1103). Son casos clínicos y no permiten estimar incidencia.

## Cambio
- Nueva categoría del ancla clínica: **«antidepresivo · sin eficacia antimaníaca; no se acredita»** (crédito 0). Mirtazapina y trazodona llevan nota y fuentes propias.
- Regla de familia: cualquier fármaco de la familia «Antidepresivos N06» sin ancla propia recibe la misma categoría (los 30 del atlas).
- Su antagonismo 5-HT2A sigue en la capa mecanística y se dibuja como segmento en el mapa de polaridad.
- Desglose: la tabla por fármaco («Bloqueo D2 y ancla clínica por fármaco») incluye también a los fármacos sin acción D2 que aportan al antimaníaco mecanístico (5-HT2A, M1, D3), con su ancla y fuentes.
- Las capas P y Q no cambian.

## Verificación
| Pauta | Acreditado | Mecanístico |
|---|---|---|
| Mirtazapina 15 / 45 | 0 / 0 | 0,062 / 0,099 |
| Trazodona 100 / 400 | 0 / 0 | 0,064 / 0,120 |
| Litio 800 + mirtazapina 30 | 0,330 (solo litio) | 0,420 |
| Olanzapina 10 + trazodona 100 | 0,458 (solo olanzapina) | 0,473 |
| Haloperidol 10 + aripiprazol 15 | 0,463 (sin cambios) | 0,463 |

- El desglose reproduce `vectorProfile` en las 170 entidades (diferencia máxima 0).
- 86 visitas por la barra sin errores; móvil a 390 px sin desbordes.

## Pendiente
- El peso 0,14 del antagonismo 5-HT2A dentro del componente antimaníaco de los antipsicóticos es heredado de la v16.0 y no tiene soporte específico más allá del ECA coadyuvante de ritanserina.
- Los antipsicóticos sin ancla revisada (amisulprida, sulpirida, clozapina, clorpromazina, perfenazina, loxapina, etc.) conservan su mecanismo como acreditado.

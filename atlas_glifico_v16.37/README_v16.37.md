# ATLAS GLÍFICO v16.37 · nueva fórmula del componente antimaníaco

Reconstrucción: `node build_v1637.mjs ../ATLAS_GLIFICO_VISUAL_v16.36.html` (exige el SHA-256 de la v16.36; anclas únicas).

Decisiones del usuario: (1) sustituir la suma probabilística y el × 0,5 por competición con actividad intrínseca; (2b) ε diferenciado; (3) segmento entre lo acreditado y lo mecanístico; (4) término antimaníaco clínico no D2.

## Problema de la v16.36
- La suma probabilística 1 − Π(1 − x) trataba agonista parcial + antagonista como dos antagonistas: haloperidol 10 mg (0,474) + aripiprazol 15 mg daba 0,747.
- Litio, valproato y carbamazepina tenían componente antimaníaco 0.
- Brexpiprazol 2 mg (0,287) y lurasidona 37 mg (0,309) superaban a haloperidol 2 mg (0,195) sin eficacia antimaníaca demostrada.

## Fórmula (capa O)
1. **Ocupación operativa por fármaco** oᵢ: la señal Ki × dosis del atlas (la misma escala para todos). Razón rᵢ = oᵢ/(1 − oᵢ); en combinación θᵢ = rᵢ/(1 + Σr) (competición simple en equilibrio).
2. **Bloqueo D2 neto** B = Σ θᵢ(1 − εᵢ). ε = 0 en antagonistas. ε editorial: aripiprazol 0,30 y cariprazina 0,30 (del orden del Emax 30 % de cariprazina en fosfatos de inositol, Kiss 2010); brexpiprazol 0,20 (menor que aripiprazol, Maeda 2014). La actividad intrínseca depende del ensayo (Kiss 2010: antagonismo en GTPγS, Emax 30 % en fosfatos de inositol) y del tejido.
3. **D3**: todos los ligandos compiten; solo el antagonismo suma al término antimaníaco (el agonismo D3 sigue en antidepresivo/activación, sin cambios).
4. **Ancla clínica** por fármaco y dosis:

| Categoría | Fármacos | Fuente |
|---|---|---|
| Demostrada | haloperidol (DME −0,56), risperidona (−0,50), olanzapina (−0,43), quetiapina (−0,37), asenapina (−0,30), ziprasidona (−0,20), litio (−0,37), carbamazepina (−0,36), valproato (−0,20) | Cipriani 2011, doi:10.1016/S0140-6736(11)60873-8 |
| | paliperidona LP | Fornaro 2026, doi:10.1016/j.jad.2026.122329 |
| | aripiprazol ≥ 15 mg (DME −0,37) | FT aripiprazol 4.2 (inicio 15 mg en manía del adulto); Romeo 2018, doi:10.1177/0269881118760661 |
| | cariprazina ≥ 3 mg | Durgam 2015, 3–12 mg (media 8,8 mg), doi:10.1111/bdi.12238; en España la FT solo autoriza esquizofrenia |
| Dosis por debajo del rango probado | aripiprazol < 15 mg; cariprazina < 3 mg | ídem |
| Estudiada y negativa | brexpiprazol | Vieta 2021, doi:10.1177/0269881120985102 |
| | lamotrigina, gabapentina, topiramato | Cipriani 2011 |
| No estudiada | lurasidona | Ali 2020, doi:10.1080/14656566.2019.1695777; FT 4.1 solo esquizofrenia |
| Sin ancla revisada | resto | se conserva el mecanismo como acreditado |

5. **Acreditado** = mínimo entre el valor total y el que darían solos los fármacos con eficacia demostrada (D2, D3, 5-HT2A y M1). Un antagonista no acreditado añadido no reduce lo demostrado; un agonista parcial no acreditado sí, porque desplaza al antagonista.
6. **Antimaníaco clínico no D2** (litio, valproato, carbamazepina): 0,38 × f^0,55, con f la escala de dosis de `aggregate()`; magnitud ordinal, no derivada de la DME.
7. am acreditado = 0,38·B_acr + 0,20·D3_acr + 0,14·5-HT2A_acr + 0,24·M1_acr + 0,38·N. El mecanístico usa los valores totales. Vertical del mapa = 7 × (antidepresivo − am acreditado).

**PET**: se muestra como contraste por fármaco y no entra en el cálculo. Mezclar PET (10 fármacos) con la escala operativa (el resto) haría incomparables las magnitudes entre fármacos. La fracción libre no se corrige aparte: la PET ya la integra y la escala Ki no la incluye.

**Capa P** (potencia intrínseca, un fármaco por ficha): ε en lugar del × 0,5; sin ancla clínica (capa mecanística). **Capa Q** sin cambios.

## Interfaz
- Mapa de polaridad: el punto usa el antimaníaco acreditado; un segmento discontinuo con círculo hueco llega al valor mecanístico («mecanismo sin eficacia antimaníaca acreditada»). Tarjeta lateral con ambos valores.
- Desglose «Qué mueve el vector»: columna mecanística en el componente antimaníaco y tabla por fármaco con ocupación sola, ocupación en la pauta, aporte a B, ancla clínica con fuentes, PET de contraste y aviso de competición agonista parcial–antagonista (Shim 2007, doi:10.1176/appi.ajp.2007.06071075).
- Corrección heredada: los botones de objetivo del mapa ya no hacen desaparecer el desglose.

## Verificación
| Caso | am acreditado | am mecanístico |
|---|---|---|
| Haloperidol 10 | 0,474 | 0,474 |
| Haloperidol 10 + aripiprazol 15 | 0,463 | 0,463 (antes 0,747) |
| Haloperidol 10 + lurasidona 74 | 0,474 | 0,628 |
| Haloperidol 10 + brexpiprazol 2 | 0,376 | 0,498 |
| Aripiprazol 15 / 10 | 0,340 / 0 | 0,340 / 0,272 |
| Cariprazina 4,5 / 1,5 | 0,374 / 0 | 0,374 / 0,220 |
| Brexpiprazol 2 | 0 | 0,386 |
| Lurasidona 37 | 0 | 0,309 |
| Litio 800 · valproato 750 · carbamazepina 600 | 0,330 · 0,282 · 0,282 | ídem |

- A dosis por defecto, solo cambian 7 entidades; los antagonistas puros en monoterapia conservan su valor.
- El desglose reproduce `vectorProfile` (acreditado y mecanístico) en las 170 entidades y en combinaciones: diferencia máxima 0.
- 86 visitas por la barra sin errores; móvil a 390 px sin desbordes.

## Pendiente
- El crédito 5-HT2A de los antidepresivos (p. ej., mirtazapina) sigue sin revisar (categoría «sin ancla revisada»).
- Agonistas D2 plenos (pramipexol, ropinirol…) no entran en la competición: su contribución no es polar en los datos.
- Cinética de disociación, diferencias regionales de ε y exposición de DCAR/DDCAR no modeladas.

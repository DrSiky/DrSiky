# ATLAS GLÍFICO v16.33 · curación de la base e interfaz centrada en los atlas

Reconstrucción: `node ../atlas_glifico_v16.32/build_v1632.mjs RUTA/v16.31.html` y después `node build_v1633.mjs ../ATLAS_GLIFICO_VISUAL_v16.32.html`. Cada constructor exige el SHA-256 de su ancestro y aborta si alguna ancla no es única.

## 1 · Curación de la base

**Auditoría estructural (170 entidades):** todas tienen ficha curada y fuente; todas las dianas tienen evidencia y acción; potencias en 0–10; ninguna dosis supera el máximo; ninguna diana sin definir. Las dianas, potencias, dosis y PK no se modifican.

**Situación en España contra CIMA (AEMPS), consulta REST del 12-11-2026** (`curation_v1633.js`):

| Entidad | Antes | Ahora (CIMA) |
|---|---|---|
| Selegilina | «Referencia extranjera» | Plurimen 5 mg comercializado; familia Antiparkinsonianos N04 · IMAO-B |
| Rasagilina | «Referencia extranjera» | 27 presentaciones comercializadas (Azilect y EFG) |
| Safinamida | «Referencia extranjera» | 13 presentaciones comercializadas (Xadago y EFG) |
| Maprotilina | «Referencia extranjera» | Ludiomil 25 y 75 mg autorizados con comercialización suspendida; fuera del inventario activo |
| Ondansetrón | fuera del inventario | 30 presentaciones comercializadas |
| Clorazepato dipotásico | «comercialización no reenumerada» | 8 presentaciones comercializadas (Tranxilium y EFG) |
| Trihexifenidilo | «comercialización no reenumerada» | Artane 2 y 5 mg comercializados |
| Flufenazina | ficha de Modecate | sin presentaciones en CIMA por principio activo ni por Modecate |
| Xanomelina | marcada en inventario español | sin registro en CIMA; fuera del inventario |

Inventario español: 156 → 159. Familia añadida a 7 referencias extranjeras que no la tenían (iloperidona, tioridazina, pimavanserina → antipsicóticos; levomilnacipran, desipramina, vilazodona, tranilcipromina → antidepresivos).
Quinidina se mantiene: CIMA solo devuelve hidroquinidina, que el atlas ya advierte que no es sustituible.

**Decisiones de modelo pendientes, resueltas de forma explícita y reversible:**
- **Agonismo parcial D2** (aripiprazol, brexpiprazol, cariprazina) suma **contención** en O y P con un **factor editorial de 0,5** del peso D2 (sin calibrar; la actividad intrínseca no se incorpora). Aripiprazol 15 mg: contención O 0,27; cariprazina 3 mg: 0,26.
- **Antagonismo 5-HT1A**: sin eje (efectos pre y postsinápticos de sentido opuesto); se conserva como registro.
- **Agonistas D2 completos**: sin eje numérico; siguen visibles en receptoroma, red y patrones.

## 2 · Interfaz

- **Indicación como pestañas** (Molecular · Bipolar · Depresión/ansiedad · Psicosis · Atención · Adicciones/dolor · Sueño), en lugar del desplegable «Contexto».
- **Tres vistas principales**: Receptoroma · **Atlas de la indicación** (Fountoulakis en bipolar; mapa espacial en las demás) · **Mecanismo** (red funcional, con los paneles de patrones y de estabilizadores, que solo aparecen aquí).
- **«Más»**: un único selector para PK/PD, mapas estratégicos, proyecciones, informe, comparador A→B, contraste previo, polaridad y trayectoria (bipolar), mapa de psicosis beta (psicosis), atribución, evidencia y catálogo.
- **Ajustes**: tema, avisos heredados y panel de pauta, en un único menú.
- La **pauta queda siempre visible** a la izquierda; desaparecen el cajón de herramientas, la fila de contexto, la tarjeta de navegación y el aviso metodológico plegado (resumido en una línea fija bajo la barra).
- La barra queda fija al desplazarse; en móvil se apila.
- Se conservan todos los cálculos y manejadores; la navegación antigua solo se oculta.

## Verificación

- Chromium: 86 visitas por la barra nueva (7 indicaciones × vistas principales y todas las opciones de «Más») sin errores ni vistas vacías; los paneles de patrones solo aparecen en «Mecanismo».
- Sin bucles de recolocación entre observadores (0 llamadas en reposo).
- Comparación v16.32 → v16.33 en 641 combinaciones vista × lente × pauta: solo cambian el porcentaje de zoom automático, el inventario del catálogo y las vistas que leen `vectorProfile` (por el agonismo parcial D2).
- Móvil a 390 px sin desbordes; temas e-ink y color revisados en captura.

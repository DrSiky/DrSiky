# ATLAS GLÍFICO v16.32 · sobre la v16.31

Reconstrucción: `node build_v1632.mjs RUTA/ATLAS_GLIFICO_VISUAL_v16.31.html [SALIDA.html]`.
El constructor exige el SHA-256 de la v16.31 del paquete (`8bfd2fd6…a45d2`) y aborta si alguna ancla no es única. No modifica el archivo de origen.

## Cambios

1. **Política anti/pro de H1, α1 y M1 en la capa O** (decisión del usuario; `vectorprofile_v1632.js`).
   - Antagonismo → sedación: H1 0,58 (principal), M1 0,24, α1 0,18 (secundarios). Agonismo H1 0,58 y α1 0,18 → activación; agonismo M1 0,24 → contención. M1 antagonista deja de sumar contención.
   - Lee esas dianas por elegibilidad operativa y con dosis; excluye PET, registros cualitativos, metabolitos y textos de baja afinidad, probables, indirectos o preclínicos (los ordinales débiles conservan su magnitud). «Adrenolítico» se lee como antagonismo α1.
   - Sedación O > 0 en 24 de 170 entidades (antes 1). Olanzapina (0,00; −3,21) → (−5,13; −3,91); clozapina (0,00; −2,06) → (−4,62; −2,73); haloperidol sin cambios.
   - Afecta a proyecciones O, polaridad, trayectoria y comparación A→B. Pesos de agonistas: espejo, sin calibrar.
2. **Proyecciones P y Q** con la misma política (`projectionP_v1632.js`); P sigue siendo independiente de la dosis.
3. **Panel «Lectura funcional asociada»**: el agonismo H1/α1/M1 recibe su lectura (vigilia; vigilia y ↑ PA; peristaltismo, sialorrea, procognitivo-antipsicótico) como inferencia de clase sin intensidad (`effects_v1632.js`). Ejemplo: norclozapina.
4. **Rendimiento**: memoización pura de `v1616TargetMatch` (`memo_v1632.js`). Detección de patrones idéntica en 470 pautas (170 individuales + 300 aleatorias); 3,3× más rápida. `evaluate()` con 8 fármacos: ~200 → ~105 ms.
5. **Panel de ocupación** (correcciones comprobadas en la fuente primaria):
   - Rabiner 2000: enlace sustituido por PubMed 10942852 (DOI 10.1016/S0893-133X(00)00109-3).
   - Moriguchi 2017: se elimina «No se mezcla con el seguimiento longitudinal» (el estudio es de dosis única) y se añade «máximo individual 46,7 %; PET 6 h; referencia en sustancia blanca».
   - Nogami 2013: se indica que varios puntos son de un solo sujeto (NET 25, 125 y 200 mg; SERT 50 y 200 mg).

## Verificación

- Chromium: 108 vistas × lentes sin errores; móvil 390 px sin desbordes; guardar/cargar caso.
- Comparación v16.31 → v16.32 en 641 combinaciones vista × lente × pauta: idénticas salvo las vistas que leen `vectorProfile` (proyecciones, polaridad, trayectoria) y un porcentaje de zoom automático.
- Cifras PET: 21 fichas revisadas contra la fuente primaria. Correctas en Arakawa, Moriguchi, Girgis 2016 y 2020, Aboukaoud, Bymaster, Volkow, Kim, Nyberg, Nogami y el ED50 de Takano.

## Pendiente de comprobar en el texto completo (no se ha cambiado)

- Nogami 2013: la nota «una frase de resultados dice 50 mg» no se encontró en la versión consultada (resumen de la página del editor); confirmar en el PDF antes de retirarla.
- Stenkrona 2013: K aparente de 20 nM, los 9 pares de la tabla 1 y la ventana de 7–8,5 h (el resumen da KD(ND) 16,7 nM).
- Takano 2006: punto de 5 mg (43,6 %), tálamo, n = 12; 20/40 mg solo coinciden con Moriguchi como fuente secundaria.
- Kapur 2000 (n 13/9; medias 59/75 %) y Rabiner 2000 (valores por región): sin texto completo accesible.
- Girgis 2016: número de figura.

Lectura exploratoria: Ki ≠ ocupación ≠ respuesta; no es una herramienta de prescripción.

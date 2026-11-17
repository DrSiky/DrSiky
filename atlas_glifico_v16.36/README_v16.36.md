# ATLAS GLÍFICO v16.36 · correcciones tras revisión externa de la v16.35

Reconstrucción: `node build_v1636.mjs ../ATLAS_GLIFICO_VISUAL_v16.35.html` (exige el SHA-256 de la v16.35; anclas únicas).

## Alertas de interacción
1. **Inductores moderados de CYP3A4.** Cariprazina + modafinilo pasa a contraindicación: la ficha de Reagila (4.3 y 4.5) contraindica los inductores potentes **o moderados** y nombra el modafinilo. Lurasidona + modafinilo queda en vigilancia: su ficha prevé una reducción de la exposición menor de 2 veces con inductores moderados.
2. **Activa frente a borrador.** Cada tarjeta indica «activa en la pauta» (todos los fármacos implicados con dosis activa) o «en el borrador» (alguno sin dosis activa, p. ej. a 0 mg), con la lista de los que faltan. Dentro de cada nivel, las activas van primero.
3. **Mensaje vacío.** «Ninguna de las reglas cubiertas se activó con esta pauta. No significa que la combinación sea segura…» en lugar de «sin alertas».

## Vector clínico (capa O y proyecciones P/Q)
4. **H1 solo en sedación.** El antagonismo H1 deja de sumar al componente antimaníaco (peso 0,14 que la política anti/pro había activado). Ejemplos: mirtazapina, antimaníaco 0,227 → 0,090; quetiapina 0,286 → 0,195; la sedación no cambia. La dirección Q del H1 antagonista queda solo en sedación.
5. **Desglose «Qué mueve el vector · capa O»** en el campo de polaridad y en Proyecciones (base O): cada término (señal × peso) por componente, con su origen: heredado v16.0, política anti/pro del usuario o factor editorial sin calibrar (agonismo parcial D2 × 0,5). La suma reproduce `vectorProfile` en las 170 entidades (diferencia máxima 0).

## Verificación
- Casos de la revisión: cariprazina + modafinilo (⛔ activa), valproato 0 mg + lamotrigina (⚠ en el borrador), valproato activo + lamotrigina (⚠ activa), clozapina + diazepam y cariprazina + carbamazepina (siguen detectándose).
- 86 visitas por la barra sin errores; móvil a 390 px sin desbordes; alertas actualizadas desde la interfaz.

## Pendiente de decisión del usuario
- Mantener o retirar el agonismo parcial D2 × 0,5 en el componente antimaníaco (ahora visible como «factor editorial sin calibrar»).

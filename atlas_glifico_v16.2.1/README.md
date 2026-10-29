# ATLAS GLÍFICO v16.2.1 · fusión de la v16.1 e-ink y la v16.2

Reconstrucción: `python3 build.py RUTA/ATLAS_GLIFICO_VISUAL_v16.0.html [SALIDA.html]` (reconstruye antes la v16.1 del paquete `../atlas_glifico_v16.1_eink/`; las anclas son únicas y se comprueban).

## Origen de cada parte
- **De la v16.2 de ChatGPT** (archivos `interface_v162.js` y `interface_v162.css`, sin cambios salvo estilos añadidos): selector de tema e-ink/color, modo foco de la red, etiquetas descriptivas («coincidencia/oposición» en lugar de suma/competencia), proyecciones con **una sola base exclusiva cada vez (P, O, Q)**, envolvente de máximos, centroide geométrico, matriz y CSV por base.
- **De la v16.1 de este repositorio** (ya corregida): componentes de asociaciones fijas como nodos de la red, procedencia de metabolitos por régimen, punteado de evidencia ordinal/cualitativa, sincronización del bloqueo de scroll en pantalla completa, columnas de figura solo en escritorio, unidades de dosis del atlas, política anti/pro en la capa O.

## Cambios propios sobre la v16.2 de ChatGPT
1. **Política anti/pro de H1, α1 y M1** (decisión del usuario):
   - antagonismo → sedación (H1 principal, M1 y α1 secundarios);
   - agonismo H1/α1 → activación; agonismo M1 → contención;
   - M1 antagonista deja de sumar contención.
   Aplicada en la **capa O** (`vectorProfile`, vía el paquete v16.1), en **P** (potencia intrínseca) y en **Q** (direcciones). Pesos de agonistas: espejo de los de sedación, sin calibrar.
2. **Ordinales con dirección y magnitud clínica:** entran en O con la magnitud ordinal que ya figura en el atlas (no es afinidad). P sigue siendo solo afinidad documentada; Q conserva las direcciones.
3. **Columna «Efectos asociados»** (tabla de la pauta, matriz y CSV): lectura cualitativa por dirección, **sin cifras** y con procedencia (afinidad documentada · ordinal clínico · cualitativo · metabolito). No es un eje ni una base y no entra en las áreas. Ejemplo: clozapina → H1⊣, α1⊣, M⊣ y M1⊕ del metabolito norclozapina.
4. El texto de «Base, alcance y cálculo» refleja la capa O actual.

## Qué conserva de ChatGPT y por qué
No se mezclan bases en un mismo polígono; no se «completa» una con otra; P no depende de la dosis; la envolvente no crece al duplicar un perfil. La unión no lineal de la v16.1 queda fuera de esta vista.

## Verificación (navegador, Chromium)
- Regresión de añadir/quitar/dosis/guardar/cargar/lente/pauta vacía; recorrido de 108 vistas y lentes; móvil a 390 px: sin errores ni desbordes.
- P invariante a la dosis (clozapina 25 y 300 mg: 0,95 y 0,95); O dosis-dependiente (0,18 → 0,66).
- Sedación operativa con valor en 27 fármacos (O) y 24 (P).
- Red: nodos de componentes y metabolitos presentes; foco y «Ver toda la red» funcionan; unidades correctas (µg/h transdérmico; comprimidos/día con cantidades por componente).
- Selector de tema y bloqueo de scroll en pantalla completa tras recalcular.

## Límites
Sin validación clínica: Ki ≠ ocupación ≠ respuesta. Los coeficientes son editoriales y los de los agonistas, además, sin calibrar. No se ha probado en un dispositivo de tinta electrónica. La capa O cambia el comportamiento de las vistas que leen `vectorProfile` (campo de polaridad, trayectoria, A/B, informe) respecto a la v16.0.

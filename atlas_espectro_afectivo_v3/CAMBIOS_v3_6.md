# Atlas clínico-geométrico del espectro afectivo — v3.5 → v3.6 (láminas de curso farmacológico)

Fecha: 18 noviembre 2026. De 103 a **112 páginas**: un índice en miniatura (p. 80) y ocho láminas longitudinales
nuevas (Cursos 17–24, pp. 81–88). Cada lámina es una viñeta ilustrativa (G) anclada en una cifra de su dosier.
En cada una, el panel inferior de la plantilla se reetiqueta para representar una dimensión farmacológica.

Regenerar: `python3 build_v36.py ATLAS_..._v2.pdf ATLAS_..._v3.pdf ATLAS_..._v3_6.pdf`

| Pág. | Lámina | Dato de anclaje | Panel inferior |
|---|---|---|---|
| 80 | Índice en miniatura de los cursos 15–24 | Dato clave de cada curso | — |
| 81 | Curso 17 · Quetiapina: depresión aguda y continuación | BOLDER I 57,6 % frente a 36,1 %; HR depresivo 0,43 y maníaco 0,75 [D05] | carga adversa |
| 82 | Curso 18 · Litio en depresión aguda: efecto incierto, con trayectoria placebo superpuesta | EMBOLDEN I p=0,123; RR 1,18 [0,99–1,41] [D01] | litemia |
| 83 | Curso 19 · Aripiprazol: manía y mantenimiento antimaníaco | HR maníaco 0,35; depresivo 0,81 [D09] | acatisia |
| 84 | Curso 20 · Olanzapina-fluoxetina en depresión I | Respuesta 56,1 % frente a 30,4 %; manía emergente 6,4 % frente a 6,7 % [D07] | peso |
| 85 | Curso 21 · Cariprazina: respuesta depresiva sin prevención demostrada | MD-56 −4,0; MD-25 HR 0,89 [D10] | acatisia |
| 86 | Curso 22 · Risperidona de acción prolongada: prevención por polo | Elevación p<0,001; depresiva p=0,805; latencia de unas 3 semanas [D08] | prolactina |
| 87 | Curso 23 · Carbamazepina: autoinducción y exposición | Semivida 36 h, 16–24 h y 9–10 h [D03] | exposición |
| 88 | Curso 24 · Litio e interacción: ascenso de la litemia | Tiazidas, IECA/ARA-II, AINE; signos de toxicidad [D01] | litemia |

También se actualizan:
- la guía (p. 89), que remite a las pp. 80–88;
- el índice, con 13 filas;
- la paginación del método (p. 90), de la bibliografía (pp. 91–109) y de los dosieres (pp. 110–112).

## Rigor

- Ninguna lámina representa pacientes ni promedios. Las amplitudes y los tiempos no están calibrados, y el panel inferior carece de unidades.
- La lámina del litio en depresión superpone la trayectoria placebo para mostrar visualmente un resultado negativo.
- Las de cariprazina y risperidona inyectable dibujan la recurrencia del polo no prevenido.

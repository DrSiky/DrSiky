# Atlas clínico-geométrico del espectro afectivo — v3.3 → v3.4 (Ampliación V: farmacología)

Fecha: 18 noviembre 2026. De 74 a **95 páginas**.

- **Ampliación V:** 16 páginas nuevas (56–71), construidas a partir de los 13 dosieres monográficos del Atlas Glífico (D01–D13, 222 láminas) que aportó el autor.
- **Bibliografía:**
  - 9 síntesis transversales nuevas (P83–P91), verificadas en PubMed (metadatos y resúmenes);
  - 3 páginas nuevas que describen los dosieres (93–95).
- **Guía de lectura:** pasa a 16 preguntas (p. 72).

Regenerar: `python3 build_v34.py ATLAS_..._v2.pdf ATLAS_..._v3.pdf ATLAS_..._v3_4.pdf`
(con `pages31–34.py` y `refs31–34.py`).

## Páginas nuevas

| Pág. | Contenido | Gráfico | Fuentes |
|---|---|---|---|
| 56 | Mapa de autorizaciones CIMA por fase y nota FDA (15 principios activos) | Matriz de indicación | D01–D13 [R] |
| 57 | Cómo leer la evidencia: afinidad, ocupación, respuesta y prevención | Esquema del diseño de retirada enriquecido | D05, D08, D11, D12 |
| 58 | Manía aguda | Gráfico de bosque de SMD (10 fármacos) y gráfico de pares fármaco–placebo de los ensayos pivotales | P83, D01–D13 |
| 59 | Depresión bipolar | Respuesta MADRS por pares y gráfico de bosque de diferencias MADRS | P84–P86, D03, D05–D07, D10, D12 |
| 60 | Mantenimiento por polaridad | Matriz de Kishi y HR/RR por polo (cualquier episodio, manía, depresión) | P87, P88, D05, D09, D11 |
| 61 | Índice de polaridad (enlace con p. 45) | Barras en escala logarítmica centradas en 1 | P89, P90 |
| 62 | **Lámina Curso 15** · mantenimiento con litio, antes y después | Lámina longitudinal | D01, P88 |
| 63 | Perfil receptorial y mecanismos | Mapa de calor de pKi (asenapina, cariprazina, lurasidona, quetiapina, norquetiapina) | D05, D06, D10, D11, D01–D04 |
| 64 | Ocupación D2 por PET y semividas | Rangos de ocupación y semividas en escala logarítmica | D01–D13 |
| 65 | Interacciones que cambian la exposición | Tabla de causa, fármaco afectado y efecto, con flechas | D01–D13 |
| 66 | Monitorización | Matriz de controles y calendarios NICE de litio y antipsicóticos | D01–D13 [G4] |
| 67 | Seguridad | Acatisia y otras cifras de tolerabilidad por pares | D05–D13 |
| 68 | Seguridad reproductiva (enlace con pp. 32–33) | Barras de riesgo del valproato | D02–D04, D10 |
| 69–70 | Fichas sintéticas de los 15 principios activos | — | D01–D13 |
| 71 | Hoja longitudinal farmacológica del caso | — | D01–D13 |

## Criterios de rigor

- **Citación:**
  - cada dato de un dosier se cita como D## y, entre corchetes, el código de su fuente primaria;
  - esas fuentes primarias no se han verificado de nuevo en esta edición, y así se declara en las pp. 73, 92 y 95;
  - solo las síntesis P83–P91 se han verificado en PubMed.
- **Avisos en las páginas:**
  - P85 (Kadakia) está financiado por el fabricante de lurasidona;
  - el índice de polaridad (P89) va acompañado de su validación naturalista negativa (P90);
  - Yildiz (P84) se cita solo con los extremos del rango de SMD que da el resumen.
- **Datos ambiguos:** las cifras que los extractores marcaron como ambiguas por la maquetación en columnas se cotejaron con el texto fuente antes de representarlas (cariprazina MD-25 y tabla MADRS por dosis). Las que siguieron siendo dudosas no se usan (olanzapina como control en los ensayos de asenapina; asignación por brazo en Berwaerts).
- **Mapa de calor:** solo incluye moléculas con valores numéricos en su dosier; el pKi se calcula del Ki publicado.
- **Carácter no prescriptivo:** se mantiene, como en la p. 20, y la p. 20 lleva ahora un pie de enlace a las pp. 56–71.

## Pendiente

1. Verificar en PubMed los ensayos pivotales de cada dosier, para darles su propio P## con enlace.
2. Los dosieres no traen datos reproductivos de litio ni de los antipsicóticos atípicos (lo declara la p. 68).
3. Las indicaciones FDA de varios fármacos «no constan en el dosier» y no se han completado con fuentes externas.
4. Siguen pendientes los puntos de las versiones anteriores (p. 22 frente a N4, glosario y redacción de las pp. 1–25).

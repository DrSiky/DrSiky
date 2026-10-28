# Atlas clínico-geométrico del espectro afectivo — registro de cambios v2 → v3

Fecha de corte: 28 octubre 2026. Fuente única: el PDF v2 entregado.
Regenerar: `python3 build_v3.py ATLAS_..._v2.pdf ATLAS_..._v3.pdf`
(requiere ReportLab, pypdf y la fuente Roboto; `replay.py` lee el PDF v2 y lo vuelve a dibujar).

## A. Correcciones de contenido

| Pág. | Cambio | Motivo |
|---|---|---|
| 13 (Curso 04, ciclotimia) | La activación pasa a alternar con la depresión (desfase de un punto). | En v1 y v2 los seis picos de ambas curvas coincidían: se leía como ciclado mixto continuo, no como periodos hipomaníacos y depresivos alternantes. |
| 15 (Curso 06, bipolar I) | El segundo pico de manía vuelve al punto 9→8 y el segundo episodio depresivo se desplaza un punto; el recuadro «psicosis» acompaña a la manía. | En v2 el segundo pico de activación coincidía con el de depresión (se leía como episodio mixto con psicosis). En v1 estaban en secuencia. |
| 4 y 5 (fila 13) | «Activación subjetiva» y «Menor necesidad de sueño» pasan de «·» a **V**. | Son síntomas contrapolares del recuento DSM de «con características mixtas» (N4). |
| 6 (fila 10) | «Reactividad del ánimo» pasa de «·» a **V** (nota en p. 6 y p. 22). | En melancólica el criterio A se cumple con anhedonia generalizada *o* ausencia de reactividad; la columna no podía codificar «presente» en atípica y «ausente» en melancólica (N4). |
| 5 | Cabecera «Hipomanía umbral» → «Hipomanía (episodio)». | «Umbral» se confundía con «subumbral». |
| 8–18, 21 | Se dibujan las flechas ↑ → ↔ que el v2 pretendía y que no se veían. | Roboto no tiene esos glifos (en el v2 eran caracteres nulos). Ahora se usan glifos de DejaVu Sans incrustados. |

## B. Estructura y trazabilidad

- **p. 8** Se añade el matiz sobre P04/P05: P05 trata activación/inhibición como un eje más un componente emocional, así que no sostiene por sí solo la independencia de los dos ejes. El enunciado «comparten rangos de carga depresiva» se etiqueta E/I y se cita (P02, P12, P13).
- **p. 9** El eje «depresión» pasa a «síntomas depresivos» (coherente con p. 8).
- **p. 19** Recuadro discontinuo que agrupa cualquier fase del curso depresivo (incluido el primer episodio) con tres flechas hacia hipomanía, manía y características mixtas; sustituye a las flechas desde un solo nodo. Se añade la nota E sobre Angst et al. (P18). Las flechas hacia «Reevaluar diagnóstico» no cambian.
- **p. 22** Dos notas operativas nuevas (recuento DSM de rasgos mixtos; reactividad del ánimo).
- **p. 23** Matiz de P05/P04 en el recuadro de evidencia.
- **p. 24** «remisión posible» sale de la línea base.
- **p. 26** Las fuentes N1–N6 muestran ahora la URL abreviada y la fecha de corte (los hipervínculos originales se conservan); «17 artículos» → «18»; definiciones de la clave F/E/I/H/G unificadas con la p. 2.
- **p. 30** Nueva referencia **P18**: Angst J, Sellaro R, Stassen HH, Gamma A. *J Affect Disord* 2005;84(2-3):149-57. DOI 10.1016/S0165-0327(03)00195-2, PMID 15708412 (verificada en PubMed).
- **Todas** La línea de procedencia (F/E/I/H/G) bajo el título pasa de 8 a 9 pt.

## C. Láminas longitudinales (pp. 10–18)

- Las pastillas flotantes de la leyenda se sustituyen por **llaves de fase** sobre el primer panel y **franjas** translúcidas sobre todos los paneles (azul = depresión, rojo = activación, gris = remisión/intervalo). En la p. 16 se mantienen las notas definitorias («≥4 episodios / 12 meses», «No son cambios horarios»).
- **Línea de umbral esquemático** (discontinua, sin calibración) en las láminas 04–07, donde distingue ciclotimia, bipolar II, bipolar I y ciclación rápida. En la 07 los ocho episodios se numeran.
- La lámina 09 distingue «Depresión con psicosis», «¿Psicosis fuera de episodio?» (la pregunta de la p. 25), «Manía con psicosis» y «Depresión posterior».

## D. Cosas que NO he cambiado y por qué

- **Mapa de la p. 8**: no he colocado números de perfil (01–24) en las zonas. Asignar perfiles a zonas sería un juicio editorial nuevo (la matriz describe episodio índice e historia, no fases).
- **Lámina 06**: se mantiene la amplitud de picos (ya hay asimetría de duración a favor de la depresión).
- **Fila 09**: se conserva «anxious distress» en inglés (la p. 22 ya explica que no hay traducción oficial certificada).

## E. Pendiente de cotejo por la autoría

Estos elementos proceden de mi conocimiento del DSM-5 y no he podido contrastarlos con el texto en esta sesión:
1. Lista de síntomas contrapolares del recuento de «con características mixtas» y exclusión de irritabilidad, distractibilidad y agitación (filas 13; notas de p. 22).
2. Criterio A de melancólica (anhedonia generalizada o ausencia de reactividad) y reactividad como requisito de atípica (fila 10/11; nota de p. 22).
3. Duraciones y reglas de ciclotimia y recurrencia citadas en las láminas 02 y 04 (ya estaban en el v2).

Tampoco he verificado: el año de N4 («National Academies (2019)») porque NCBI bloqueó el acceso; y las páginas del CDDR citadas (170–176, 201–207, 212–224, 225–243, 235, 240).
Sí verificado en esta sesión: N2 (ficha APA, © 2022: se retira «dysthymia» del nombre y los especificadores superfluos; solo *anxious distress* y *atypical features* son aplicables) y los 18 PMID de la bibliografía.

"""Láminas de curso farmacológico del Atlas v3.6 (pp. 80–88): índice en miniatura y Cursos 17–24.

Viñetas ilustrativas (G) ancladas en cifras de los dosieres D01–D13. El panel inferior de la plantilla
(RESIDUO) se reetiqueta en cada lámina para representar una dimensión farmacológica: carga adversa,
litemia o exposición relativa; sin unidades ni calibración. No prescriptivo (p. 20)."""
from layout31 import (new_page, card, card_row, note, sw, text, rect_top, line_top, path, PURPLE, OCHRE, PILLFILL,
                      NOTEFILL, WARN, WHITE, NAVY, INK, GRAY, LINE, TEAL, BLUE, RED, Y, make_sheet, xi)
from pages32 import subtitle, X2
from pages33 import ctext, curve, lines_block

FOOT_G = 'Panel inferior reetiquetado (%s): intensidad relativa sin unidades.'

# id: (título, tag, subtítulo, curvas, filas, umbral, marcadores, alt, notas, etiqueta panel inferior, subetiqueta, nota pie)
C = {}
C[17] = dict(
    title='Curso 17 · Quetiapina: depresión aguda y continuación',
    tag='G · viñeta ilustrativa | E · D05 [T2, T7] | F · CIMA: depresión TB-I y TB-II | I · relación con pp. 59, 60 y 76',
    sub='Respuesta en BOLDER I del 57,6 % frente al 36,1 %; en la continuación, HR depresivo 0,43 y maníaco 0,75 (IC incluye 1).',
    curves={'dep': [0.30, 0.72, 0.82, 0.70, 0.48, 0.34, 0.30, 0.28, 0.30, 0.40, 0.31, 0.28],
            'act': [0.30, 0.30, 0.29, 0.30, 0.31, 0.30, 0.31, 0.32, 0.31, 0.30, 0.31, 0.30],
            'fun': [0.78, 0.48, 0.40, 0.48, 0.64, 0.74, 0.78, 0.80, 0.78, 0.74, 0.78, 0.80],
            'res': [0.10, 0.10, 0.58, 0.52, 0.44, 0.40, 0.40, 0.42, 0.44, 0.45, 0.46, 0.47]},
    rows=[(140.0, 134.0, [(0.0, 1.5, 'Basal', 'neu', False), (1.5, 5.0, 'Fase aguda · 8 semanas', 'neu', False),
                          (5.0, 11.4, 'Continuación tras respuesta', 'neu', False)]),
          (159.0, 153.0, [(0.8, 4.2, 'Episodio depresivo', 'dep'), (8.7, 9.8, 'Subumbral', 'dep', False)])],
    thr=(0.60, 0.60, 'umbral de manía'), markers=[(1.5, 'quetiapina 300 mg')],
    res=('CARGA ADVERSA', 'sedación, peso'),
    foot='Carga adversa: sedación inicial y peso lento.')
C[18] = dict(
    title='Curso 18 · Litio en depresión bipolar aguda: efecto incierto',
    tag='G · viñeta ilustrativa | E · D01 [T3, E7] | I · trayectoria gris: placebo en el mismo ensayo | relación con p. 59',
    sub='EMBOLDEN I: MADRS −13,60 con litio frente a −11,81 con placebo (p=0,123); RR de respuesta 1,18 [0,99–1,41].',
    curves={'dep': [0.30, 0.76, 0.80, 0.76, 0.70, 0.62, 0.56, 0.50, 0.44, 0.38, 0.34, 0.32],
            'act': [0.30, 0.30, 0.31, 0.30, 0.30, 0.31, 0.30, 0.31, 0.30, 0.31, 0.30, 0.30],
            'fun': [0.78, 0.46, 0.42, 0.44, 0.48, 0.54, 0.58, 0.62, 0.66, 0.70, 0.74, 0.76],
            'res': [0.02, 0.10, 0.45, 0.56, 0.62, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64]},
    rows=[(140.0, 134.0, [(0.0, 1.5, 'Basal', 'neu', False), (1.5, 8.0, 'Fase aguda con litio', 'neu', False),
                          (8.0, 11.4, 'Revisión de la estrategia', 'neu', False)]),
          (159.0, 153.0, [(0.8, 7.0, 'Episodio depresivo prolongado', 'dep')])],
    thr=(0.60, 0.60, 'umbral de manía'), markers=[(1.5, 'inicio del litio')],
    alt=[('dep', 2, [0.80, 0.78, 0.73, 0.67, 0.61, 0.55, 0.49, 0.44, 0.40, 0.37], GRAY)],
    res=('LITEMIA', 'nivel relativo'),
    foot='Trazo gris discontinuo: placebo en el mismo ensayo.')
C[19] = dict(
    title='Curso 19 · Aripiprazol: manía aguda y mantenimiento antimaníaco',
    tag='G · viñeta ilustrativa | E · D09 [T1, T4] | F · CIMA: manía TB-I y prevención maníaca | I · relación con pp. 60 y 76',
    sub='Manía: YMRS −12,0 frente a −9,7 (Young 2009). Mantenimiento: HR maníaco 0,35 [0,16–0,75]; depresivo 0,81 [0,36–1,81].',
    curves={'act': [0.30, 0.80, 0.86, 0.60, 0.42, 0.34, 0.31, 0.30, 0.31, 0.30, 0.32, 0.30],
            'dep': [0.26, 0.24, 0.25, 0.30, 0.34, 0.30, 0.28, 0.40, 0.70, 0.66, 0.40, 0.30],
            'fun': [0.80, 0.40, 0.32, 0.50, 0.66, 0.74, 0.78, 0.72, 0.48, 0.52, 0.70, 0.78],
            'res': [0.05, 0.05, 0.42, 0.46, 0.36, 0.26, 0.22, 0.20, 0.20, 0.20, 0.18, 0.16]},
    rows=[(140.0, 134.0, [(0.0, 3.2, 'Fase aguda', 'neu', False), (3.2, 11.4, 'Mantenimiento con aripiprazol', 'neu', False)]),
          (159.0, 153.0, [(0.6, 3.2, 'Manía', 'elev'), (7.8, 9.8, 'Depresión', 'dep')])],
    thr=(0.60, 0.60, 'umbral de manía'), markers=[(1.0, 'aripiprazol 15 mg')],
    res=('ACATISIA', 'intensidad'),
    foot='Depresión intercurrente: prevención sobre todo antimaníaca.')
C[20] = dict(
    title='Curso 20 · Olanzapina-fluoxetina en depresión bipolar I',
    tag='G · viñeta ilustrativa | E · D07 [T2, T5] | F · fuera de ficha en España; FDA: Symbyax | I · relación con pp. 31, 59 y 77',
    sub='Tohen 2003: respuesta 56,1 % frente a 30,4 %; manía emergente 6,4 % frente a 6,7 % (p=0,86); duración óptima abierta.',
    curves={'dep': [0.30, 0.76, 0.84, 0.62, 0.44, 0.36, 0.32, 0.30, 0.30, 0.31, 0.30, 0.30],
            'act': [0.30, 0.30, 0.30, 0.33, 0.36, 0.34, 0.32, 0.31, 0.30, 0.31, 0.30, 0.30],
            'fun': [0.78, 0.46, 0.40, 0.56, 0.68, 0.74, 0.78, 0.78, 0.78, 0.77, 0.77, 0.77],
            'res': [0.08, 0.08, 0.16, 0.30, 0.42, 0.52, 0.58, 0.62, 0.64, 0.66, 0.67, 0.68]},
    rows=[(140.0, 134.0, [(0.0, 1.5, 'Basal', 'neu', False), (1.5, 5.0, 'Fase aguda · 8 semanas', 'neu', False),
                          (5.0, 11.4, 'Continuación: duración por decidir', 'neu', False)]),
          (159.0, 153.0, [(0.8, 4.0, 'Episodio depresivo', 'dep')])],
    thr=(0.60, 0.60, 'umbral de manía'), markers=[(1.5, '6/25 mg')],
    res=('PESO', 'aumento relativo'),
    foot='Activación transitoria subumbral; peso sostenido.')
C[21] = dict(
    title='Curso 21 · Cariprazina: respuesta depresiva sin prevención demostrada',
    tag='G · viñeta ilustrativa | E · D10 [T3–T5] | F · fuera de ficha en España; FDA: Vraylar | I · relación con pp. 59, 60 y 74',
    sub='MD-56: diferencia MADRS −4,0 con 1,5 mg/d. MD-25: HR de recaída 0,89 [0,52–1,51] con 3 mg/d, sin superioridad.',
    curves={'dep': [0.30, 0.74, 0.80, 0.60, 0.46, 0.36, 0.32, 0.34, 0.66, 0.72, 0.44, 0.32],
            'act': [0.30, 0.30, 0.31, 0.32, 0.31, 0.30, 0.31, 0.30, 0.31, 0.30, 0.31, 0.30],
            'fun': [0.78, 0.46, 0.42, 0.56, 0.68, 0.74, 0.78, 0.74, 0.50, 0.46, 0.66, 0.76],
            'res': [0.05, 0.05, 0.30, 0.34, 0.28, 0.22, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20]},
    rows=[(140.0, 134.0, [(0.0, 1.5, 'Basal', 'neu', False), (1.5, 5.0, 'Fase aguda · 6 semanas', 'neu', False),
                          (5.0, 11.4, 'Continuación', 'neu', False)]),
          (159.0, 153.0, [(0.8, 3.6, 'Episodio depresivo', 'dep'), (7.6, 9.8, 'Recurrencia depresiva', 'dep')])],
    thr=(0.60, 0.60, 'umbral de manía'), markers=[(1.5, 'cariprazina 1,5 mg')],
    res=('ACATISIA', 'intensidad'),
    foot='La recurrencia ilustra MD-25, sin superioridad.')
C[22] = dict(
    title='Curso 22 · Risperidona de acción prolongada: prevención por polo',
    tag='G · viñeta ilustrativa | E · D08 [T2, T3] | F · LAI sin indicación bipolar en España; FDA: Uzedy | I · pp. 60–61',
    sub='Quiroz 2010: recurrencia con elevación del ánimo p<0,001, depresiva p=0,805. Latencia de liberación de unas 3 semanas.',
    curves={'act': [0.82, 0.40, 0.30, 0.84, 0.42, 0.30, 0.30, 0.31, 0.30, 0.32, 0.31, 0.30],
            'dep': [0.28, 0.30, 0.28, 0.30, 0.32, 0.30, 0.28, 0.30, 0.68, 0.42, 0.30, 0.30],
            'fun': [0.42, 0.62, 0.76, 0.40, 0.60, 0.74, 0.78, 0.78, 0.52, 0.66, 0.76, 0.78],
            'res': [0.20, 0.20, 0.20, 0.20, 0.22, 0.22, 0.30, 0.48, 0.54, 0.55, 0.55, 0.55]},
    rows=[(140.0, 134.0, [(0.0, 5.6, 'Manías recurrentes con mala adherencia oral', 'neu', False),
                          (5.6, 11.4, 'Inyectable cada 2 semanas', 'neu', False)]),
          (159.0, 153.0, [(0.0, 0.8, 'Manía', 'elev'), (2.6, 3.6, 'Manía', 'elev'), (5.6, 6.8, 'Latencia', 'neu'),
                          (7.8, 9.0, 'Depresión', 'dep')])],
    thr=(0.60, 0.60, 'umbral de manía'), markers=[(5.6, 'primera inyección')],
    res=('PROLACTINA', 'relativa'),
    foot='Cobertura oral en la latencia; depresión no prevenida.')
C[23] = dict(
    title='Curso 23 · Carbamazepina: autoinducción y exposición',
    tag='G · viñeta ilustrativa | E · D03 [R1, T3] | I · el panel inferior representa la exposición relativa | relación con pp. 64–65',
    sub='Semivida ≈36 h tras dosis única, 16–24 h en administración repetida y 9–10 h con otros inductores; respuesta ERC 52 % frente a 26 %.',
    curves={'act': [0.84, 0.76, 0.54, 0.40, 0.52, 0.58, 0.44, 0.34, 0.31, 0.30, 0.31, 0.30],
            'dep': [0.28, 0.27, 0.28, 0.30, 0.30, 0.29, 0.30, 0.31, 0.30, 0.31, 0.30, 0.30],
            'fun': [0.40, 0.46, 0.62, 0.72, 0.62, 0.56, 0.68, 0.76, 0.78, 0.78, 0.79, 0.80],
            'res': [0.05, 0.78, 0.76, 0.58, 0.46, 0.44, 0.66, 0.70, 0.70, 0.70, 0.70, 0.70]},
    rows=[(140.0, 134.0, [(0.0, 3.0, 'Inicio y respuesta', 'neu', False), (3.0, 5.5, 'Autoinducción', 'neu', False),
                          (5.5, 11.4, 'Exposición reajustada', 'neu', False)]),
          (159.0, 153.0, [(0.0, 2.2, 'Manía', 'elev'), (4.0, 5.6, 'Reactivación subumbral', 'elev', False)])],
    thr=(0.60, 0.60, 'umbral de manía'), markers=[(0.6, 'inicio'), (5.5, 'ajuste')],
    res=('EXPOSICIÓN', 'nivel relativo'),
    foot='La caída de exposición precede a la reactivación.')
C[24] = dict(
    title='Curso 24 · Litio e interacción: ascenso de la litemia',
    tag='G · viñeta ilustrativa | E · D01 [R1–R2, G4, S1] | I · el panel inferior representa la litemia relativa | pp. 65–66',
    sub='Tiazidas, IECA/ARA-II, AINE y deshidratación pueden elevar la litemia; vómitos, temblor grosero, ataxia o confusión: valoración urgente.',
    curves={'act': [0.30, 0.31, 0.30, 0.31, 0.30, 0.31, 0.30, 0.31, 0.30, 0.30, 0.31, 0.30],
            'dep': [0.28, 0.29, 0.28, 0.29, 0.28, 0.29, 0.30, 0.34, 0.36, 0.32, 0.30, 0.29],
            'fun': [0.80, 0.80, 0.80, 0.80, 0.80, 0.80, 0.74, 0.46, 0.38, 0.60, 0.74, 0.78],
            'res': [0.56, 0.56, 0.57, 0.56, 0.56, 0.57, 0.70, 0.88, 0.92, 0.50, 0.56, 0.56]},
    rows=[(140.0, 134.0, [(0.0, 6.0, 'Mantenimiento estable', 'neu', False), (6.0, 8.6, 'Interacción y toxicidad', 'neu', False),
                          (8.6, 11.4, 'Reajuste', 'neu', False)]),
          (159.0, 153.0, [(6.6, 8.6, 'Signos de toxicidad', 'neu')])],
    thr=(0.60, 0.60, 'umbral de manía'), markers=[(6.0, 'AINE o tiazida'), (8.6, 'suspensión y litemia urgente')],
    res=('LITEMIA', 'nivel relativo'),
    foot='El deterioro funcional representa toxicidad.')


def sheet(k, tpl, pageno):
    d = C[k]
    tag = d['tag'] + ' | G · panel inferior: %s' % d['res'][0].lower()
    it = make_sheet(tpl, pageno=pageno, title=d['title'], tag=tag, subtitle=d['sub'], curves=d['curves'], rows=d['rows'],
                    thr=d['thr'], markers=d['markers'], alt=d.get('alt', ()), extra_foot=d['foot'])
    for x in it:
        if x['k'] == 'text' and x['text'] == 'RESIDUO':
            x['text'] = d['res'][0]
        elif x['k'] == 'text' and x['text'].strip() == 'carga':
            x['text'] = d['res'][1]
    return it


# miniaturas de las láminas 15 y 16 (curvas de pages34/35)
MINI = {15: ('Litio · mantenimiento', 'p. 62', {'dep': [0.24, 0.74, 0.40, 0.26, 0.78, 0.36, 0.26, 0.30, 0.48, 0.30, 0.25, 0.26],
                                               'act': [0.30, 0.28, 0.82, 0.38, 0.30, 0.76, 0.36, 0.31, 0.30, 0.32, 0.31, 0.30]}, 6.0),
        16: ('Lamotrigina · titulación', 'p. 78', {'dep': [0.26, 0.76, 0.40, 0.28, 0.80, 0.42, 0.34, 0.30, 0.46, 0.30, 0.27, 0.26],
                                                  'act': [0.30, 0.29, 0.31, 0.30, 0.29, 0.31, 0.32, 0.31, 0.33, 0.64, 0.34, 0.31]}, 5.0)}
SHORT = {17: ('Quetiapina · depresión', 'p. 81'), 18: ('Litio · depresión aguda', 'p. 82'), 19: ('Aripiprazol · manía', 'p. 83'),
         20: ('Olanzapina-fluoxetina', 'p. 84'), 21: ('Cariprazina · depresión', 'p. 85'), 22: ('Risperidona LAI', 'p. 86'),
         23: ('Carbamazepina · autoinducción', 'p. 87'), 24: ('Litio · interacción', 'p. 88')}
KEY = {15: 'RR manía 0,52; depresión 0,78', 16: 'previene depresión, no manía', 17: 'HR depresivo 0,43 en continuación',
       18: 'p=0,123 frente a placebo', 19: 'HR maníaco 0,35; depresivo 0,81', 20: 'respuesta 56,1 % frente a 30,4 %',
       21: 'MD-25: HR 0,89, sin superioridad', 22: 'depresiva p=0,805', 23: 'semivida 36 a 16–24 h', 24: 'AINE, tiazidas, IECA'}


def p80():
    n = 80
    it = new_page('Láminas de curso farmacológico: índice en miniatura', 'LÁMINAS · ÍNDICE',
                  'G · miniaturas de las láminas 15–24 (depresión en azul, activación en rojo) | E · dato clave de cada dosier', n)
    subtitle(it, 'Diez cursos ilustrativos que traducen a la geometría del atlas el efecto por fase y por polo, la exposición y la seguridad.')
    items = []
    for k in (15, 16):
        lab, pg, cv, mk = MINI[k]
        items.append((k, lab, pg, cv, mk))
    for k in range(17, 25):
        d = C[k]
        lab, pg = SHORT[k]
        items.append((k, lab, pg, {'dep': d['curves']['dep'], 'act': d['curves']['act']}, d['markers'][0][0]))
    cw, ch = 212.0, 236.0
    for i, (k, lab, pg, cv, mk) in enumerate(items):
        col, row = i % 5, i // 5
        x0 = 50 + col * (cw + 6.5)
        t0 = 128 + row * (ch + 12)
        it.append(rect_top(x0, t0, x0 + cw, t0 + ch, 8, fill=WHITE, stroke=LINE, lw=1.0))
        it.append(rect_top(x0, t0, x0 + cw, t0 + 5, 3, fill=NAVY))
        it.append(text(x0 + 12, t0 + 26, 'Curso %d' % k, 'Roboto-Bold', 12, NAVY))
        it.append(text(x0 + cw - 12 - sw(pg, 'Roboto-Medium', 9.5), t0 + 26, pg, 'Roboto-Medium', 9.5, TEAL))
        it.append(text(x0 + 12, t0 + 42, lab, 'Roboto-Medium', 10, INK))
        gx0, gx1 = x0 + 12, x0 + cw - 12
        for p, (top, bot), colr in (('dep', (t0 + 56, t0 + 116), BLUE), ('act', (t0 + 126, t0 + 186), RED)):
            it.append(rect_top(gx0, top, gx1, bot, 3, fill=(0.98, 0.97, 0.95), stroke=LINE, lw=0.6))
            thr = bot - 0.60 * (bot - top)
            it.append(line_top(gx0, thr, gx1, thr, stroke=INK, lw=0.6, dash=([3.0, 2.0], 0.0)))
            xs = [gx0 + (gx1 - gx0) * j / 11.0 for j in range(12)]
            tops = [bot - v * (bot - top) for v in cv[p]]
            curve(it, xs, tops, colr, lw=1.8)
        xm = gx0 + (gx1 - gx0) * mk / 11.0
        it.append(line_top(xm, t0 + 52, xm, t0 + 190, stroke=INK, lw=0.9, dash=([3.0, 2.0], 0.0)))
        for m, ln in enumerate(lines_wrap(KEY[k], cw - 24)):
            it.append(text(x0 + 12, t0 + 206 + 13 * m, ln, 'Roboto-Regular', 9.5, GRAY))
    note(it, 50, 128 + 2 * (ch + 12) + 4, 1141, 'I · Cómo leer las miniaturas', [
        'Cada miniatura reproduce las curvas de depresión y activación de su lámina con el umbral esquemático (discontinuo) y la '
        'intervención (línea vertical). Son viñetas, no pacientes ni promedios: ilustran una cifra del dosier y sus límites.'],
         kind='info', where='p80')
    return it


def lines_wrap(s, width):
    from build_v3 import wrap
    return wrap(s, 'Roboto-Regular', 9.5, width)[:2]


NEW_PAGES36 = [p80] + ['c%d' % k for k in range(17, 25)]

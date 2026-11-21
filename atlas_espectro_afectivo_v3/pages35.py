"""Ampliación VI del Atlas v3.5 (pp. 72–79): grafismo comparado de farmacología del TB.

Datos de los dosieres D01–D13 y de P83–P91 (ya verificados). Los NNT son cálculos brutos del atlas
(1 / diferencia de proporciones publicadas), sin ajuste ni intervalos: G/I. No prescriptivo (p. 20)."""
import math

from layout31 import (new_page, card, card_row, note, sw, text, rect_top, line_top, path, rrect_ops, PURPLE, OCHRE,
                      PILLFILL, NOTEFILL, INFOFILL, WARN, WHITE, NAVY, INK, GRAY, LINE, TEAL, BLUE, RED, Y, make_sheet)
from pages32 import panel, subtitle, X2, X3
from pages33 import arrow, dot, tri, ctext, curve, lines_block
from pages34 import mark, legend_marks, lforest, dumbbell, axis_ticks, PALE

LINECOL = {1: (0.16, 0.42, 0.40), 2: (0.45, 0.66, 0.62), 3: (0.75, 0.85, 0.82), 'no': (0.80, 0.46, 0.38), None: None,
           'ne': (0.93, 0.91, 0.86)}


# ------------------------------------------------------------------ 72 · mapa de guías
CANMAT = [  # manía, dep TB-I, dep TB-II, mantenimiento ; 'no' = no recomendada; None = no consta; 'ne' = fuera de 1ª línea
    ('Litio', 1, 1, 2, 1), ('Valproato', 1, 2, 3, 1), ('Carbamazepina', 2, 3, None, 2), ('Lamotrigina', None, 1, 2, 1),
    ('Quetiapina', 1, 1, 1, 1), ('Lurasidona', None, 1, None, 2), ('Olanzapina', 2, None, None, 2),
    ('Olanzapina-fluoxetina', None, 2, None, None), ('Risperidona', 1, None, None, 2), ('Paliperidona', 1, None, None, 2),
    ('Aripiprazol', 1, 'no', None, 1), ('Cariprazina', 1, 1, None, 'ne'), ('Asenapina', 1, 3, None, 1),
    ('Ziprasidona', 2, 'no', None, 2), ('Haloperidol', 2, None, None, None)]
NICE = {  # manía, depresión, mantenimiento (CG185 según los dosieres)
    'Litio': (False, False, True), 'Quetiapina': (True, True, 'alt'), 'Olanzapina': (True, True, False),
    'Olanzapina-fluoxetina': (False, True, False), 'Risperidona': (True, False, 'alt'), 'Haloperidol': (True, False, False),
    'Lamotrigina': (False, True, False), 'Aripiprazol': (False, False, 'alt'), 'Asenapina': (False, False, 'alt')}
ADJ = {('Lurasidona', 4), ('Risperidona', 4), ('Asenapina', 2), ('Ziprasidona', 4)}  # celdas que la guía sitúa en adición o depot


def p72():
    n = 72
    it = new_page('Posición en las guías por fase', 'FARMACOLOGÍA · GUÍAS',
                  'F/I · CANMAT/ISBD 2023 y NICE CG185 según los dosieres D01–D13 (edición completa 2018: P91) | G · mapa de calor', n)
    subtitle(it, 'Las líneas de una guía integran eficacia, seguridad y experiencia; leerlas por fase evita trasladar una recomendación aguda al mantenimiento.')
    t0, t1 = 128.0, 690.0
    panel(it, 50, t0, 1141, t1, 'CANMAT/ISBD 2023 por fase y presencia en NICE CG185', accent=TEAL)
    cols = ['Manía', 'Depresión TB-I', 'Depresión TB-II', 'Mantenimiento']
    x0, cw = 270.0, 128.0
    for j, c in enumerate(cols):
        ctext(it, x0 + cw * j + cw / 2, t0 + 58, c, 'Roboto-Bold', 10.5, NAVY)
    nx = [850.0, 930.0, 1010.0]
    for c, lab in zip(nx, ('manía', 'depresión', 'mantenim.')):
        ctext(it, c, t0 + 58, lab, 'Roboto-Bold', 10, NAVY)
    ctext(it, 930, t0 + 44, 'NICE CG185', 'Roboto-Bold', 10.5, GRAY)
    ctext(it, x0 + cw * 2, t0 + 44, 'CANMAT/ISBD 2023 · línea de recomendación', 'Roboto-Bold', 10.5, GRAY)
    pitch = 30.0
    for i, row in enumerate(CANMAT):
        name, vals = row[0], row[1:]
        yt = t0 + 68 + pitch * i
        it.append(text(68, yt + 19, name, 'Roboto-Medium', 11, INK))
        for j, v in enumerate(vals):
            xa = x0 + cw * j + 4
            fill = LINECOL.get(v) if v is not None else None
            if fill is None:
                it.append(rect_top(xa, yt + 2, xa + cw - 8, yt + 27, 4, fill=WHITE, stroke=LINE, lw=0.8))
                ctext(it, xa + (cw - 8) / 2, yt + 18.5, 'sin línea', 'Roboto-Regular', 8.8, GRAY)
                continue
            it.append(rect_top(xa, yt + 2, xa + cw - 8, yt + 27, 4, fill=fill))
            lab = {1: '1.ª línea', 2: '2.ª línea', 3: '3.ª línea', 'no': 'no recomendada', 'ne': 'fuera de 1.ª'}[v]
            if (name, j + 1) in ADJ:
                lab += ' · adición' if name != 'Risperidona' else ' · depot'
            colt = WHITE if v in (1, 'no') else INK
            ctext(it, xa + (cw - 8) / 2, yt + 18.5, lab, 'Roboto-Medium', 9.5, colt)
        nv = NICE.get(name, (False, False, False))
        for c, v in zip(nx, nv):
            mark(it, c, yt + 14, 'full' if v is True else ('half' if v == 'alt' else 'ring'), NAVY, r=6.5)
    lb = t1 - 18
    x = 68
    for k, lab in ((1, '1.ª línea'), (2, '2.ª línea'), (3, '3.ª línea'), ('no', 'no recomendada'), ('ne', 'fuera de 1.ª línea')):
        it.append(rect_top(x, lb - 10, x + 22, lb + 2, 3, fill=LINECOL[k]))
        it.append(text(x + 28, lb, lab, 'Roboto-Regular', 9.5, INK))
        x += 50 + sw(lab, 'Roboto-Regular', 9.5)
    legend_marks(it, 760, lb, [('full', 'opción nombrada'), ('half', 'si el litio no procede')], NAVY)
    note(it, 50, t1 + 12, 1141, 'I · Cómo leer el mapa', [
        '«Sin línea» significa que el dosier no recoge una posición para esa casilla, no que la guía la desaconseje. Las celdas «adición» '
        'y «depot» corresponden a pautas añadidas a litio o divalproato o a la risperidona inyectable. NICE nombra pocas opciones por fase '
        'y prioriza el litio a largo plazo; la ausencia en su lista no equivale a una recomendación en contra.'], kind='info', where='p72')
    return it


# ------------------------------------------------------------------ 73 · titulación
TITR = [  # nombre, color, [(día, % de la dosis de referencia)], referencia, fuente
    ('Lamotrigina en monoterapia', BLUE, [(0, 12.5), (14, 25), (28, 50), (35, 100), (42, 100)], '200 mg/d', 'D04 · R1'),
    ('Lamotrigina con valproato', (0.45, 0.62, 0.80), [(0, 12.5), (14, 25), (28, 50), (35, 100), (42, 100)], '100 mg/d', 'D04 · R1'),
    ('Quetiapina en depresión', TEAL, [(0, 16.7), (1, 33.3), (2, 66.7), (3, 100), (42, 100)], '300 mg/d', 'D05 · R1'),
    ('Quetiapina IR en manía', (0.30, 0.62, 0.56), [(0, 25), (1, 50), (2, 75), (3, 100), (42, 100)], '400 mg/d', 'D05 · R1'),
    ('Quetiapina XR en manía', (0.55, 0.75, 0.70), [(0, 50), (1, 100), (42, 100)], '600 mg/d', 'D05 · R1'),
    ('Cariprazina en depresión', PURPLE, [(0, 50), (14, 50), (15, 100), (42, 100)], '3 mg/d (opcional)', 'D10 · R2'),
    ('Cariprazina en manía', (0.66, 0.56, 0.75), [(0, 50), (1, 100), (42, 100)], '3 mg/d (hasta 6)', 'D10 · R2'),
    ('Asenapina en manía', RED, [(0, 50), (42, 50)], '10 mg/12 h (si procede)', 'D11 · R1')]


def p73():
    n = 73
    it = new_page('Titulación: cuánto se tarda en llegar a la dosis de referencia', 'FARMACOLOGÍA · TITULACIÓN',
                  'F · pautas de ficha citadas en D04, D05, D10, D11 | G · escalones normalizados a una dosis de referencia', n)
    subtitle(it, 'La velocidad de titulación es una propiedad clínica: separa los fármacos útiles en urgencia de los que solo encajan en un plan preventivo.')
    t0, t1 = 128.0, 548.0
    panel(it, 50, t0, 1141, t1, 'Porcentaje de la dosis de referencia según el día de tratamiento', accent=BLUE)
    x0, x1, yt, yb = 120.0, 760.0, t0 + 56, t1 - 60

    def px(d):
        return x0 + math.sqrt(d) / math.sqrt(42) * (x1 - x0)

    def py(v):
        return yb - v / 100.0 * (yb - yt)
    for d in (0, 1, 2, 4, 7, 14, 21, 28, 35, 42):
        it.append(line_top(px(d), yt, px(d), yb, stroke=LINE, lw=0.5))
        it.append(text(px(d) - sw(str(d), 'Roboto-Regular', 9) / 2, yb + 14, str(d), 'Roboto-Regular', 9, GRAY))
    it.append(text(x1 - sw('días (escala de raíz cuadrada)', 'Roboto-Regular', 9), yb + 28, 'días (escala de raíz cuadrada)',
                   'Roboto-Regular', 9, GRAY))
    for v in (0, 25, 50, 75, 100):
        it.append(line_top(x0, py(v), x1, py(v), stroke=LINE, lw=0.5))
        s = '%d %%' % v
        it.append(text(x0 - 8 - sw(s, 'Roboto-Regular', 9), py(v) + 3, s, 'Roboto-Regular', 9, GRAY))
    for k, (name, col, pts, ref, src) in enumerate(TITR):
        ops = []
        for m, (d, v) in enumerate(pts):
            if m == 0:
                ops.append(('m', px(d), Y(py(v) + 1.2 * k - 4)))
            else:
                ops.append(('l', px(d), Y(py(pts[m - 1][1]) + 1.2 * k - 4)))
                ops.append(('l', px(d), Y(py(v) + 1.2 * k - 4)))
        it.append(path(ops, stroke=col, lw=2.6))
        yl = t0 + 64 + 41 * k
        it.append(rect_top(790, yl - 9, 808, yl - 3, 2, fill=col))
        it.append(text(816, yl - 2, name, 'Roboto-Medium', 10.5, INK))
        it.append(text(816, yl + 12, 'referencia %s [%s]' % (ref, src), 'Roboto-Regular', 9, GRAY))
    lines_block(it, 68, t1 - 24, ['G · Trazos ligeramente desplazados para que no se solapen. Asenapina parte de 5 mg/12 h y puede subir a 10 mg/12 h;',
                                   'lurasidona (20 mg/d), aripiprazol (15 mg/d) y olanzapina (15 mg/d) empiezan en dosis eficaz.'], size=9.2, lead=12.6)
    top = t1 + 14
    card_row(it, [
        dict(title='Lamotrigina: seis semanas obligadas', pill='F · D04', body=[
            'La pauta de ficha llega a 200 mg/d en la semana 6, y a la mitad con valproato. Una dosis inicial alta o un escalado rápido '
            'aumentan el riesgo de erupción grave; tras una pausa de más de cinco semividas se reescala desde el inicio. Por eso no '
            'tiene lugar en la urgencia maníaca ni suele priorizarse en la depresión aguda (IPS, según D04).']),
        dict(title='Antipsicóticos: dosis útil en días', pill='F · D05 · D10', body=[
            'Quetiapina alcanza 300 mg/d en depresión al cuarto día y 400 mg/d en manía con IR; la XR llega a 600 mg/d el segundo día. '
            'Cariprazina parte de 1,5 mg/d, pero su metabolito DDCAR tarda unas tres semanas en acercarse al equilibrio (p. 64): '
            'la dosis nominal se alcanza antes que la exposición estable.']),
    ], top, X2, where='p73', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 74 · tiempo hasta recaída y NNT de mantenimiento
def nnt(a, b):
    d = abs(a - b) / 100.0
    return 1.0 / d if d > 0 else float('inf')


def p74():
    n = 74
    it = new_page('Mantenimiento: tiempo hasta la recaída y NNT', 'FARMACOLOGÍA · MANTENIMIENTO II',
                  'E · medianas y proporciones de D01, D04, D07–D12 | G/I · NNT bruto calculado por el atlas, sin intervalo', n)
    subtitle(it, 'Dos maneras complementarias de leer un ensayo de mantenimiento: cuánto se retrasa la recaída y a cuántas personas hay que tratar para evitar una.')
    t0, t1 = 128.0, 484.0
    panel(it, 50, t0, 590, t1, 'Mediana hasta recaída o intervención (días)', accent=NAVY)
    med = [('Paliperidona ER · Berwaerts 2012', 558, 283, 'D08 · T8'), ('Litio · Bowden, tras manía', 292, 85, 'D01 · L2'),
           ('Lamotrigina · Calabrese, tras depresión', 200, 93, 'D04 · L2'), ('Olanzapina · Tohen 2006', 174, 22, 'D07 · T3'),
           ('Litio · Calabrese, tras depresión', 170, 93, 'D01 · L3')]
    x0, x1 = 330.0, 560.0

    def pos(v):
        return x0 + (math.log(v) - math.log(15)) / (math.log(700) - math.log(15)) * (x1 - x0)
    for t in (15, 30, 60, 120, 240, 480):
        it.append(line_top(pos(t), t0 + 50, pos(t), t0 + 66 + 44 * 4 + 14, stroke=LINE, lw=0.5))
        it.append(text(pos(t) - sw(str(t), 'Roboto-Regular', 9) / 2, t0 + 92 + 44 * 4, str(t), 'Roboto-Regular', 9, GRAY))
    for k, (lab, a, b, src) in enumerate(med):
        yb = t0 + 70 + 44 * k
        it.append(text(68, yb + 2, lab, 'Roboto-Regular', 10.5, INK))
        it.append(text(68, yb + 15, '[%s]' % src, 'Roboto-Regular', 8.5, GRAY))
        it.append(line_top(pos(b), yb, pos(a), yb, stroke=LINE, lw=3.0))
        dot(it, pos(b), yb, 5.5, WHITE, stroke=GRAY, lw=1.8)
        dot(it, pos(a), yb, 6.0, NAVY)
        it.append(text(pos(a) - sw(str(a), 'Roboto-Medium', 9) / 2, yb - 9, str(a), 'Roboto-Medium', 9, NAVY))
        it.append(text(pos(b) - sw(str(b), 'Roboto-Regular', 9) / 2, yb + 18, str(b), 'Roboto-Regular', 9, GRAY))
    lines_block(it, 68, t1 - 26, ['Escala logarítmica. Relleno: fármaco; anillo: placebo. Las medianas no permiten reconstruir una curva de',
                                   'Kaplan-Meier ni comparar ensayos con desenlaces distintos (recaída frente a intervención).'], size=9.2, lead=12.6)
    gx0 = 612.0
    panel(it, gx0, t0, 1141, t1, 'NNT bruto para evitar una recaída (proporciones publicadas)', accent=TEAL)
    rows = [('Olanzapina · 48 sem', 46.7, 80.1, 'D07 · T3'), ('Asenapina · 26 sem', 8.7, 33.3, 'D11 · T5'),
            ('Aripiprazol mensual · 52 sem', 26.5, 51.1, 'D09 · T5'), ('Risperidona LAI + TAU', 23.1, 45.8, 'D08 · T4'),
            ('Aripiprazol oral · 26 sem', 25.0, 43.0, 'D09 · T3'), ('Ziprasidona + Li/VPA', 19.7, 32.4, 'D12 · T3'),
            ('Lamotrigina · depresión al año', 43.0, 55.0, 'D04 · L2'), ('Cariprazina 3 mg · MD-25', 17.9, 19.7, 'D10 · T4')]
    x0, x1 = 900.0, 1100.0

    def npos(v):
        return x0 + (math.log(min(v, 80)) - math.log(2)) / (math.log(80) - math.log(2)) * (x1 - x0)
    for t in (2, 5, 10, 20, 50):
        it.append(line_top(npos(t), t0 + 50, npos(t), t0 + 60 + 31 * 7 + 12, stroke=LINE, lw=0.5))
        it.append(text(npos(t) - sw(str(t), 'Roboto-Regular', 9) / 2, t0 + 86 + 31 * 7, str(t), 'Roboto-Regular', 9, GRAY))
    for k, (lab, a, b, src) in enumerate(rows):
        yb = t0 + 66 + 31 * k
        v = nnt(a, b)
        it.append(text(gx0 + 18, yb + 2, lab, 'Roboto-Regular', 10.2, INK))
        it.append(text(gx0 + 18, yb + 14, '%s %% frente a %s %% [%s]' % (('%g' % a).replace('.', ','), ('%g' % b).replace('.', ','), src),
                       'Roboto-Regular', 8.5, GRAY))
        col = TEAL if v < 15 else GRAY
        it.append(line_top(x0, yb, npos(v), yb, stroke=col, lw=2.0))
        dot(it, npos(v), yb, 5.5, col)
        s = ('%.1f' % v).replace('.', ',')
        it.append(text(npos(v) + 9, yb + 3.5, s, 'Roboto-Medium', 9.5, INK))
    lines_block(it, gx0 + 18, t1 - 26, ['NNT = 1 / diferencia absoluta. Lamotrigina: proporción con intervención por depresión al año',
                                         '(100 − 57 y 100 − 45). Cariprazina: diferencia no significativa (HR 0,89 [0,52–1,51]).'], size=9.2, lead=12.6)
    top = t1 + 14
    card_row(it, [
        dict(title='Por qué el NNT de mantenimiento suele ser bajo', pill='I', body=[
            'En los diseños de retirada enriquecidos, la recaída en el brazo placebo es alta porque se retira un fármaco al que la persona '
            'ya respondía (80,1 % con placebo en Tohen 2006). Eso agranda la diferencia absoluta y abarata el NNT; no equivale al NNT '
            'de iniciar el fármaco en un paciente no seleccionado (p. 57).']),
        dict(title='Lo que añade el tiempo', pill='I', body=[
            'La mediana resume cuándo recae la mitad de la muestra; dos fármacos con NNT parecido pueden diferir en el ritmo. Ensayos '
            'con duración, episodio índice y definición de recaída distintos no se ordenan entre sí: el gráfico compara cada fármaco con '
            'su placebo, no fármacos entre sí.']),
    ], top, X2, where='p74', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 75 · NNT agudo
def p75():
    n = 75
    it = new_page('Fase aguda: número necesario a tratar', 'FARMACOLOGÍA · NNT',
                  'E · proporciones de respuesta de D02, D03, D05–D07, D12 y NNT de P85 | G/I · NNT bruto calculado por el atlas', n)
    subtitle(it, 'El NNT convierte una diferencia de respuesta en personas: cuántas hay que tratar para que una más responda que con placebo.')
    t0, t1 = 128.0, 590.0
    panel(it, 50, t0, 1141, t1, 'NNT para una respuesta adicional frente a placebo · escala logarítmica', accent=PURPLE)
    groups = [('MANÍA', RED, [('Carbamazepina ERC · análisis conjunto', 52, 26, 'D03 · T3'), ('Valproato · Cochrane', 45, 29, 'D02 · E5'),
                              ('Ziprasidona · Keck 2003', 50, 35, 'D12 · T1'), ('Valproato ER · Bowden 2006', 48, 34, 'D02 · T1')]),
              ('DEPRESIÓN', BLUE, [('Carbamazepina · Zhang 2007', 63.8, 34.8, 'D03 · T4'),
                                   ('Olanzapina-fluoxetina · Tohen 2003', 56.1, 30.4, 'D07 · T2'),
                                   ('Lurasidona 20–60 · PREVAIL 2', 53, 30, 'D06 · T1'), ('Quetiapina 300 · BOLDER I', 57.6, 36.1, 'D05 · T2'),
                                   ('Lurasidona 20–60 · Kato', 46.2, 31.0, 'D06 · T3'), ('Olanzapina sola · Tohen 2003', 39.0, 30.4, 'D07 · T2'),
                                   ('Ziprasidona 40–80 · Lombardo 1', 53, 49, 'D12 · T2')])]
    x0, x1 = 470.0, 1000.0

    def npos(v):
        return x0 + (math.log(min(v, 40)) - math.log(2)) / (math.log(40) - math.log(2)) * (x1 - x0)
    k = 0
    ybot = t0 + 58 + 29 * 12 + 10
    for t in (2, 3, 5, 10, 20, 40):
        it.append(line_top(npos(t), t0 + 46, npos(t), ybot, stroke=LINE, lw=0.5))
        it.append(text(npos(t) - sw(str(t), 'Roboto-Regular', 9) / 2, ybot + 13, str(t), 'Roboto-Regular', 9, GRAY))
    for gname, col, rows in groups:
        yb = t0 + 58 + 29 * k
        it.append(text(68, yb + 4, gname, 'Roboto-Bold', 10, col))
        k += 1
        for lab, a, b, src in rows:
            yb = t0 + 58 + 29 * k
            v = nnt(a, b)
            it.append(text(84, yb + 4, lab, 'Roboto-Regular', 10.5, INK))
            it.append(text(330, yb + 4, '%s %% frente a %s %%' % (('%g' % a).replace('.', ','), ('%g' % b).replace('.', ',')),
                           'Roboto-Regular', 9.5, GRAY))
            it.append(text(x1 + 50, yb + 4, '[%s]' % src, 'Roboto-Regular', 8.5, GRAY))
            c2 = col if v < 15 else GRAY
            # pictograma: barra segmentada
            it.append(line_top(x0, yb, npos(v), yb, stroke=c2, lw=2.0))
            dot(it, npos(v), yb, 6, c2)
            s = ('%.1f' % v).replace('.', ',')
            it.append(text(npos(v) + 10, yb + 4, s, 'Roboto-Medium', 10, INK))
            k += 1
    it.append(text(68, t1 - 12, 'G/I · NNT = 1 / (respuesta con fármaco − respuesta con placebo). Sin ajuste ni intervalo; definiciones de '
                   'respuesta, escalas y poblaciones distintas entre ensayos.', 'Roboto-Regular', 9.2, GRAY))
    top = t1 + 14
    t2 = card(it, 50, top, 584, title='NNT de una red bayesiana (P85)', pill='E · P85', body=[
        'En la red de antipsicóticos atípicos en depresión bipolar, el NNT para la respuesta fue 5 con lurasidona, 6 con quetiapina, 10 con '
        'olanzapina y 12 con cariprazina; aripiprazol y ziprasidona no fueron eficaces. El estudio está financiado por el fabricante de '
        'lurasidona.'], where='p75', bsize=11.5, lead=16.6)
    card(it, 607, top, 1141, t1=t2, title='I · Cómo leerlo', body=[
        'Un NNT bajo describe una diferencia grande frente a placebo en un ensayo concreto; no ordena los fármacos entre sí ni incorpora '
        'el número necesario para dañar. La carbamazepina en depresión procede de un único ensayo pequeño, y la ziprasidona fracasó en '
        'su objetivo primario.'], where='p75', bsize=11.5, lead=16.6, accent=OCHRE, fill=NOTEFILL)
    return it


# ------------------------------------------------------------------ 76 · brújula preventiva
def p76():
    n = 76
    it = new_page('Brújula preventiva: manía frente a depresión', 'FARMACOLOGÍA · POLARIDAD II',
                  'E · HR/RR por polo de D01, D05, D09, D11 y P88 | G · plano logarítmico | I · relación con pp. 45, 60 y 61', n)
    subtitle(it, 'Cada punto sitúa un ensayo según cuánto reduce la recaída maníaca (eje horizontal) y la depresiva (eje vertical) frente a placebo.')
    gx0, gx1, gt0, gt1 = 50.0, 700.0, 128.0, 700.0
    panel(it, gx0, gt0, gx1, gt1, 'Razón de riesgo por polo · más a la izquierda y abajo, más protección', accent=PURPLE)
    ax0, ax1, at0, at1 = gx0 + 80, gx1 - 40, gt0 + 60, gt1 - 70
    lo, hi = 0.1, 2.0

    def px(v):
        return ax0 + (math.log(v) - math.log(lo)) / (math.log(hi) - math.log(lo)) * (ax1 - ax0)

    def py(v):
        return at1 - (math.log(v) - math.log(lo)) / (math.log(hi) - math.log(lo)) * (at1 - at0)
    it.append(rect_top(px(lo), py(1.0), px(1.0), py(lo), 0, fill=TEAL, alpha=0.06))
    for t in (0.1, 0.2, 0.5, 1.0, 2.0):
        it.append(line_top(px(t), at0, px(t), at1, stroke=LINE if t != 1 else INK, lw=0.5 if t != 1 else 1.2))
        it.append(line_top(ax0, py(t), ax1, py(t), stroke=LINE if t != 1 else INK, lw=0.5 if t != 1 else 1.2))
        s = ('%g' % t).replace('.', ',')
        it.append(text(px(t) - sw(s, 'Roboto-Regular', 9) / 2, at1 + 14, s, 'Roboto-Regular', 9, GRAY))
        it.append(text(ax0 - 8 - sw(s, 'Roboto-Regular', 9), py(t) + 3, s, 'Roboto-Regular', 9, GRAY))
    it.append(line_top(px(lo), py(lo), px(hi), py(hi), stroke=GRAY, lw=1.0, dash=([4.0, 3.0], 0.0)))
    it.append(text(px(0.115), py(0.13) - 4, 'igual efecto en ambos polos', 'Roboto-Regular', 9, GRAY))
    ctext(it, (ax0 + ax1) / 2, at1 + 32, 'Prevención de manía o hipomanía (HR o RR)', 'Roboto-Medium', 10.5, RED)
    it.append(text(gx0 + 14, at0 - 14, 'Prevención de depresión', 'Roboto-Medium', 10.5, BLUE))
    pts = [('Quetiapina · ensayo 144', 0.29, (0.21, 0.40), 0.30, (0.20, 0.44), TEAL, 12, 18),
           ('Quetiapina · continuación', 0.75, (0.45, 1.24), 0.43, (0.30, 0.62), TEAL, 10, -10),
           ('Asenapina · Szegedi (pos hoc)', 0.16, (0.06, 0.43), 0.35, (0.12, 1.02), RED, 10, -10),
           ('Aripiprazol · Keck 2007', 0.35, (0.16, 0.75), 0.81, (0.36, 1.81), NAVY, 12, -12),
           ('Litio · Severus (RR)', 0.52, (0.38, 0.71), 0.78, (0.59, 1.03), BLUE, 12, 14)]
    for lab, m, mi, d, di, col, dx, dy in pts:
        cl = lambda v: min(max(v, lo), hi)
        it.append(line_top(px(cl(mi[0])), py(d), px(cl(mi[1])), py(d), stroke=col, lw=1.2))
        it.append(line_top(px(m), py(cl(di[0])), px(m), py(cl(di[1])), stroke=col, lw=1.2))
        dot(it, px(m), py(d), 7, col)
        it.append(text(px(m) + dx, py(d) + dy, lab, 'Roboto-Medium', 10, INK))
    it.append(text(gx0 + 18, gt1 - 14, 'G · Cruces: IC 95 % de cada eje. Aripiprazol y asenapina: el IC depresivo cruza 1. Ensayos enriquecidos con '
                   'episodios índice distintos.', 'Roboto-Regular', 9.2, GRAY))
    x0 = 722.0
    top = 128.0
    top = card(it, x0, top, 1141, title='Lo que muestra el plano', pill='E · I', body=[
        'Quetiapina en el ensayo 144 cae sobre la diagonal, con reducción parecida de ambos polos (HR 0,29 y 0,30). Asenapina y aripiprazol '
        'se desplazan hacia la protección maníaca, con intervalo depresivo que incluye 1. La continuación de quetiapina tras depresión '
        'invierte el patrón (depresión 0,43; manía 0,75), y el litio protege más de la manía que de la depresión.'],
        where='p76', bsize=11.5, lead=16.6) + 12
    top = card(it, x0, top, 1141, title='Relación con el índice de polaridad', pill='I · P89', body=[
        'El plano y el índice de polaridad (p. 61) expresan la misma idea con métricas distintas: el índice usa NNT y este gráfico, razones '
        'de riesgo. Ninguno elimina el sesgo del episodio índice, que condiciona qué polo se observa en el seguimiento (p. 57).'],
        where='p76', bsize=11.5, lead=16.6) + 12
    note(it, x0, top, 1141, 'I · Uso clínico', [
        'Ante una polaridad predominante depresiva (p. 45), interesa la mitad inferior del plano; ante una maníaca, la izquierda. La '
        'decisión integra además tolerabilidad, reproducción y comedicación (pp. 66–68).'], kind='info', t1=max(top + 100, gt1), where='p76')
    return it


# ------------------------------------------------------------------ 77 · carga metabólica
def p77():
    n = 77
    it = new_page('Carga metabólica y endocrina comparada', 'FARMACOLOGÍA · METABOLISMO',
                  'E · red de Kadakia (P85) y tablas de D06, D07, D11 | I · ensayos cortos; el peso a largo plazo no se infiere', n)
    subtitle(it, 'El aumento de peso es el efecto adverso que más condiciona la adherencia y el riesgo cardiovascular en el mantenimiento.')
    t0, t1 = 128.0, 430.0
    panel(it, 50, t0, 600, t1, 'Cambio de peso frente a placebo en depresión bipolar (kg; P85)', accent=OCHRE)
    rows = [('Olanzapina', 2.88, 2.40, 3.36, OCHRE), ('Quetiapina', 1.17, 0.84, 1.49, OCHRE), ('Cariprazina', 0.65, 0.34, 0.96, OCHRE),
            ('Lurasidona', 0.34, -0.22, 0.89, GRAY), ('Aripiprazol', 0.20, -0.59, 1.00, GRAY)]
    lforest(it, 200, 470, t0 + 76, 40.0, rows, -1, 4, [-1, 0, 1, 2, 3, 4], fmt='%.2f', lsize=11)
    lines_block(it, 68, t1 - 26, ['Ensayos de 6–8 semanas, ICr 95 %. Gris: intervalo que incluye 0. Red financiada por el fabricante de',
                                   'lurasidona (P85).'], size=9.2, lead=12.6)
    gx0 = 622.0
    panel(it, gx0, t0, 1141, t1, 'Otros indicadores de los dosieres', accent=NAVY)
    other = [('Aumento de peso ≥ 7 % · asenapina en manía', 6.5, 0.6, '%', 'D11 · R1', 0, 35),
             ('Ganancia ≥ 10 % · olanzapina (ENLIGHTEN-2)', 29.8, 17.8, '%', 'D07 · T7', 0, 35),
             ('Cambio de peso % · olanzapina a 24 semanas', 6.59, 4.21, '%', 'D07 · T7', 0, 35),
             ('Prolactina · lurasidona 80–120 mg (ng/mL)', 3.5, 0.3, '', 'D06 · R2', 0, 35)]
    x0, x1 = 900.0, 1110.0
    pos = None
    for k, (lab, a, b, u, src, lo, hi) in enumerate(other):
        yb = t0 + 74 + 50 * k
        it.append(text(gx0 + 18, yb + 2, lab, 'Roboto-Regular', 10, INK))
        it.append(text(gx0 + 18, yb + 15, '[%s]' % src, 'Roboto-Regular', 8.5, GRAY))
        pos = dumbbell(it, x0, x1, yb, lo, hi, a, b, NAVY)
        s = ('%g' % a).replace('.', ',') + (' %' if u else '')
        it.append(text(pos(a) - sw(s, 'Roboto-Medium', 9) / 2, yb - 10, s, 'Roboto-Medium', 9, NAVY))
    axis_ticks(it, pos, [0, 10, 20, 30], t0 + 52, t0 + 74 + 50 * 3 + 14)
    it.append(text(gx0 + 18, t1 - 12, 'Anillo: placebo u olanzapina con samidorfano (filas 2–3). Escalas distintas en cada fila.',
                   'Roboto-Regular', 9.2, GRAY))
    top = t1 + 14
    top = card_row(it, [
        dict(title='Calendario mínimo', pill='F · D05–D11 · G4', body=[
            'NICE: peso o IMC, pulso, tensión, glucemia o HbA1c y lípidos al inicio; peso semanal durante seis semanas; control '
            'metabólico en la semana 12 y después al menos anual (p. 66). Los dosieres añaden cintura y la revisión de la prolactina '
            'por síntomas (risperidona, paliperidona, haloperidol).']),
        dict(title='Lectura comparada', pill='E · I', body=[
            'En los ensayos cortos, la carga ponderal sigue un gradiente: olanzapina, quetiapina y cariprazina por encima de lurasidona y '
            'aripiprazol, cuyos intervalos incluyen 0. Olanzapina con samidorfano redujo la ganancia (+4,21 % frente a +6,59 %) en '
            'esquizofrenia, sin datos bipolares directos de esa diferencia.']),
    ], top, X2, where='p77', bsize=11.5, lead=16.6) + 12
    return it


# ------------------------------------------------------------------ 78 · lámina 16 lamotrigina
def p78(tpl):
    curves = {
        'dep': [0.26, 0.76, 0.40, 0.28, 0.80, 0.42, 0.34, 0.30, 0.46, 0.30, 0.27, 0.26],
        'act': [0.30, 0.29, 0.31, 0.30, 0.29, 0.31, 0.32, 0.31, 0.33, 0.64, 0.34, 0.31],
        'fun': [0.80, 0.48, 0.66, 0.78, 0.46, 0.62, 0.70, 0.76, 0.70, 0.72, 0.78, 0.80],
        'res': [0.26, 0.42, 0.38, 0.34, 0.46, 0.42, 0.38, 0.34, 0.34, 0.32, 0.30, 0.29]}
    rows = [(140.0, 134.0, [(0.0, 5.0, 'Predominio depresivo', 'neu', False), (5.0, 6.5, 'Titulación', 'neu', False),
                            (6.5, 11.4, 'Mantenimiento con lamotrigina', 'neu', False)]),
            (159.0, 153.0, [(0.6, 1.6, 'Depresión', 'dep'), (3.6, 4.8, 'Depresión', 'dep'), (5.0, 6.5, '6 semanas', 'neu'),
                            (8.6, 9.6, 'Hipomanía', 'elev')])]
    return make_sheet(tpl, pageno=78, title='Curso 16 · Lamotrigina: titulación y prevención depresiva',
                      tag='G · viñeta ilustrativa | E · D04 [L2, E2, E3] | I · relación con pp. 60, 61, 73 y 76',
                      subtitle='Ejemplo conceptual: la titulación retrasa la dosis eficaz; después se espacian las depresiones, pero la '
                               'hipomanía no queda prevenida.',
                      curves=curves, rows=rows, thr=(0.60, 0.55, 'umbral de hipomanía'), markers=[(5.0, 'inicio'), (6.5, '200 mg/d')],
                      extra_foot='Lamotrigina: RR de recurrencia maníaca frente a litio 2,13 [1,32–3,44] (D04 · E3).')


# ------------------------------------------------------------------ 79 · mapa de decisiones
def p79():
    n = 79
    it = new_page('Antes de elegir: un mapa de preguntas, no un algoritmo', 'FARMACOLOGÍA · SÍNTESIS',
                  'I · orden de preguntas que integra las Ampliaciones IV–VI | no prescriptivo; no sustituye guías ni fichas', n)
    subtitle(it, 'Cada caja remite a la página que la desarrolla; las flechas marcan un orden de lectura, no una secuencia obligada de fármacos.')
    t0, t1 = 128.0, 640.0
    panel(it, 50, t0, 1141, t1, 'Ocho preguntas encadenadas', accent=NAVY)
    Y1, Y2, YL = 250, 450, 560
    nodes = [  # (x, y, título, detalle, páginas, color)
        (180, Y1, 'Fase actual', 'manía o mixto · depresión · eutimia', 'pp. 3, 29, 56', RED),
        (440, Y1, 'Objetivo', 'respuesta aguda o prevención', 'p. 57', NAVY),
        (700, Y1, 'Polo a prevenir', 'polaridad predominante e índice', 'pp. 45, 61, 76', BLUE),
        (960, Y1, 'Evidencia por fase', 'magnitud, NNT y negativos', 'pp. 58–60, 74–75', TEAL),
        (960, Y2, 'Seguridad', 'metabólica, motora, órgano, QT', 'pp. 66–67, 77', OCHRE),
        (700, Y2, 'Reproducción', 'gestación, anticoncepción, periparto', 'pp. 32–33, 68', PURPLE),
        (440, Y2, 'Exposición', 'titulación, comedicación, comida', 'pp. 64–65, 73', GRAY),
        (180, Y2, 'Ficha y registro', 'autorización, fuera de ficha, hoja', 'pp. 56, 71, 72', NAVY)]
    W2, H2 = 112, 52
    for x, y, tt, dd, pp, col in nodes:
        it.append(rect_top(x - W2, y - H2, x + W2, y + H2, 10, fill=WHITE, stroke=col, lw=1.8))
        it.append(rect_top(x - W2, y - H2, x + W2, y - H2 + 6, 3, fill=col))
        ctext(it, x, y - 14, tt, 'Roboto-Bold', 13, NAVY)
        ctext(it, x, y + 6, dd, 'Roboto-Regular', 10, INK)
        pw = sw(pp, 'Roboto-Medium', 9.5) + 18
        it.append(rect_top(x - pw / 2, y + 20, x + pw / 2, y + 40, 10, fill=PILLFILL))
        ctext(it, x, y + 34, pp, 'Roboto-Medium', 9.5, TEAL)
    for a, bnd in ((0, 1), (1, 2), (2, 3)):
        arrow(it, nodes[a][0] + W2 + 4, Y1, nodes[bnd][0] - W2 - 4, Y1, color=INK, lw=1.4)
    arrow(it, 960, Y1 + H2 + 4, 960, Y2 - H2 - 4, color=INK, lw=1.4)
    for a, bnd in ((4, 5), (5, 6), (6, 7)):
        arrow(it, nodes[a][0] - W2 - 4, Y2, nodes[bnd][0] + W2 + 4, Y2, color=INK, lw=1.4)
    it.append(line_top(180, Y2 + H2 + 4, 180, YL, stroke=GRAY, lw=1.2, dash=([4.0, 3.0], 0.0)))
    it.append(line_top(180, YL, 1100, YL, stroke=GRAY, lw=1.2, dash=([4.0, 3.0], 0.0)))
    it.append(line_top(1100, YL, 1100, Y1, stroke=GRAY, lw=1.2, dash=([4.0, 3.0], 0.0)))
    arrow(it, 1100, Y1, 1076, Y1, color=GRAY, lw=1.2)
    ctext(it, 640, YL + 20, 'reevaluar en cada revisión: el episodio, la polaridad y la tolerabilidad cambian con el curso (lámina 15, p. 62)',
          'Roboto-Regular', 10, GRAY)
    it.append(text(68, t1 - 14, 'I · Esquema del atlas; el orden puede alterarse en urgencia, embarazo o toxicidad, que tienen prioridad.',
                   'Roboto-Regular', 9.5, GRAY))
    note(it, 50, t1 + 14, 1141, 'I · Por qué un mapa y no un algoritmo', [
        'Las guías jerarquizan opciones; las fichas delimitan el uso autorizado; los ensayos estiman efectos de grupo en poblaciones '
        'seleccionadas. El caso concreto combina las tres fuentes con la historia longitudinal y las preferencias de la persona, y deja '
        'constancia de la decisión y de su incertidumbre en la hoja de la p. 71.'], where='p79')
    return it


NEW_PAGES35 = [p72, p73, p74, p75, p76, p77, 'p78', p79]

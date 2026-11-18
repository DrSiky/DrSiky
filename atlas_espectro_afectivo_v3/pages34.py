"""Ampliación V del Atlas v3.4 (pp. 56–71): farmacología del trastorno bipolar.

Fuentes: dosieres monográficos D01–D13 (Atlas Glífico v1.0, 10–18 nov 2026; se conservan entre
corchetes sus códigos de fuente primaria) y síntesis transversales P83–P91 verificadas en PubMed el
18-nov-2026. Convención F/E/I/H/G del atlas. El bloque compara evidencia por fase; no es una pauta
de prescripción (p. 20)."""
import math

from layout31 import (new_page, card, card_row, note, hbars, sw, text, rect_top, line_top, path,
                      rrect_ops, PURPLE, OCHRE, PILLFILL, NOTEFILL, INFOFILL, WARN, WHITE, NAVY, INK,
                      GRAY, LINE, TEAL, BLUE, RED, Y, make_sheet, xi, PANEL)
from pages32 import panel, subtitle, X2, X3
from pages33 import arrow, dot, tri, ctext, curve, lines_block

GREEN = (0.30, 0.55, 0.36)
PALE = (0.97, 0.96, 0.93)
TAGD = 'Fuente: dosieres D01–D13 (códigos primarios entre corchetes) y P83–P91 | no prescriptivo (p. 20)'

DRUGS = ['Litio', 'Valproato', 'Carbamazepina', 'Lamotrigina', 'Quetiapina', 'Lurasidona', 'Olanzapina',
         'Olanzapina-fluoxetina', 'Risperidona', 'Paliperidona', 'Aripiprazol', 'Cariprazina', 'Asenapina',
         'Ziprasidona', 'Haloperidol']
DCODE = {'Litio': 'D01', 'Valproato': 'D02', 'Carbamazepina': 'D03', 'Lamotrigina': 'D04', 'Quetiapina': 'D05',
         'Lurasidona': 'D06', 'Olanzapina': 'D07', 'Olanzapina-fluoxetina': 'D07', 'Risperidona': 'D08',
         'Paliperidona': 'D08', 'Aripiprazol': 'D09', 'Cariprazina': 'D10', 'Asenapina': 'D11',
         'Ziprasidona': 'D12', 'Haloperidol': 'D13'}


# ------------------------------------------------------------------ utilidades gráficas
def mark(it, cx, ct, kind, col=TEAL, r=7.0):
    """kind: 'full' autorizado/sistemático · 'half' condicionado/según riesgo · 'ring' no · 'na' sin dato."""
    if kind == 'full':
        dot(it, cx, ct, r, col)
    elif kind == 'half':
        dot(it, cx, ct, r, WHITE, stroke=col, lw=1.6)
        it.append(path([('m', cx, Y(ct - r)), ('c', cx + r * 1.33, Y(ct - r), cx + r * 1.33, Y(ct + r), cx, Y(ct + r)),
                        ('h',)], fill=col))
    elif kind == 'ring':
        dot(it, cx, ct, r - 1, WHITE, stroke=LINE, lw=1.6)
    else:
        it.append(line_top(cx - 5, ct, cx + 5, ct, stroke=LINE, lw=1.6))


def legend_marks(it, x, base, items, col=TEAL):
    for kind, lab in items:
        mark(it, x + 7, base - 4, kind, col, r=6)
        it.append(text(x + 18, base, lab, 'Roboto-Regular', 10, INK))
        x += 30 + sw(lab, 'Roboto-Regular', 10)
    return x


def lforest(it, x0, x1, base0, pitch, rows, lo, hi, ticks, zero=0.0, fmt='%.2f', label_w=170, lsize=10.5,
            log=False, show_val=True):
    """rows: (etiqueta, est, l, h, color[, forma]). Escala lineal o log."""
    def pos(v):
        if log:
            return x0 + (math.log(v) - math.log(lo)) / (math.log(hi) - math.log(lo)) * (x1 - x0)
        return x0 + (v - lo) / (hi - lo) * (x1 - x0)
    ytop = base0 - 18
    ybot = base0 + pitch * (len(rows) - 1) + 12
    for t in ticks:
        it.append(line_top(pos(t), ytop, pos(t), ybot, stroke=LINE, lw=0.6))
        s = ('%g' % t).replace('.', ',').replace('-', '−')
        it.append(text(pos(t) - sw(s, 'Roboto-Regular', 9) / 2, ybot + 13, s, 'Roboto-Regular', 9, GRAY))
    it.append(line_top(pos(zero), ytop, pos(zero), ybot, stroke=INK, lw=1.2))
    for n, r in enumerate(rows):
        lab, est, l, h, col = r[:5]
        shape = r[5] if len(r) > 5 else 'sq'
        yb = base0 + n * pitch
        if lab:
            it.append(text(x0 - 10 - sw(lab, 'Roboto-Regular', lsize), yb + 3.5, lab, 'Roboto-Regular', lsize, INK))
        if l is not None:
            it.append(line_top(pos(l), yb, pos(h), yb, stroke=col, lw=2.0))
            for v in (l, h):
                it.append(line_top(pos(v), yb - 4, pos(v), yb + 4, stroke=col, lw=2.0))
        cx = pos(est)
        if shape == 'sq':
            it.append(path(rrect_ops(cx - 4.5, Y(yb + 4.5), cx + 4.5, Y(yb - 4.5), 0), fill=col, stroke=col))
        else:
            dot(it, cx, yb, 4.8, col)
        if show_val:
            vs = (fmt % est).replace('.', ',').replace('-', '−')
            if l is not None:
                vs += ' [%s a %s]' % ((fmt % l).replace('.', ',').replace('-', '−'), (fmt % h).replace('.', ',').replace('-', '−'))
            xr = pos(h if h is not None else est) + 8
            it.append(text(xr, yb + 3.5, vs, 'Roboto-Medium', 9.5, INK))
    return pos


def dumbbell(it, x0, x1, base, vmin, vmax, a, b, col_a, col_b=GRAY, lab_a=None, lab_b=None):
    def pos(v):
        return x0 + (v - vmin) / (vmax - vmin) * (x1 - x0)
    it.append(line_top(pos(a), base, pos(b), base, stroke=LINE, lw=3.0))
    dot(it, pos(b), base, 5.5, WHITE, stroke=col_b, lw=1.8)
    dot(it, pos(a), base, 6.0, col_a)
    if lab_a:
        it.append(text(pos(a) - sw(lab_a, 'Roboto-Medium', 9.5) / 2, base - 9, lab_a, 'Roboto-Medium', 9.5, col_a))
    if lab_b:
        it.append(text(pos(b) - sw(lab_b, 'Roboto-Regular', 9) / 2, base + 17, lab_b, 'Roboto-Regular', 9, GRAY))
    return pos


def axis_ticks(it, pos, ticks, top, bot, fmt='%g', suffix=''):
    for t in ticks:
        it.append(line_top(pos(t), top, pos(t), bot, stroke=LINE, lw=0.5))
        s = (fmt % t).replace('.', ',').replace('-', '−') + suffix
        it.append(text(pos(t) - sw(s, 'Roboto-Regular', 9) / 2, bot + 12, s, 'Roboto-Regular', 9, GRAY))


# ------------------------------------------------------------------ 56 · mapa de autorizaciones
AUTH = {  # España (CIMA): manía/mixto, depresión, prevención
    'Litio': ('full', 'half', 'full'), 'Valproato': ('half', 'ring', 'half'), 'Carbamazepina': ('full', 'ring', 'full'),
    'Lamotrigina': ('ring', 'ring', 'full'), 'Quetiapina': ('full', 'full', 'full'), 'Lurasidona': ('ring', 'ring', 'ring'),
    'Olanzapina': ('full', 'ring', 'full'), 'Olanzapina-fluoxetina': ('ring', 'ring', 'ring'),
    'Risperidona': ('full', 'ring', 'ring'), 'Paliperidona': ('ring', 'ring', 'ring'), 'Aripiprazol': ('full', 'ring', 'full'),
    'Cariprazina': ('ring', 'ring', 'ring'), 'Asenapina': ('full', 'ring', 'ring'), 'Ziprasidona': ('full', 'ring', 'ring'),
    'Haloperidol': ('full', 'ring', 'ring')}
CIMA_NOTE = {
    'Litio': 'Plenur: tratamiento y prevención de episodios maniacodepresivos [R1]',
    'Valproato': 'Depakine Crono: manía si litio contraindicado o no tolerado; continuación tras respuesta [R1]',
    'Carbamazepina': 'Tegretol: manía y profilaxis bipolar [R1]',
    'Lamotrigina': 'Lamictal: prevención depresiva en TB-I con predominio depresivo, desde 18 años [R1]',
    'Quetiapina': 'Seroquel IR/Prolong: manía, depresión TB-I y TB-II, prevención tras respuesta [R1–R2]',
    'Lurasidona': 'Latuda: solo esquizofrenia; TB fuera de ficha (RD 1015/2009) [R1, R4]',
    'Olanzapina': 'Zyprexa: manía moderada-grave; prevención tras respuesta en manía [R1]',
    'Olanzapina-fluoxetina': 'Sin presentación combinada en CIMA [R4]',
    'Risperidona': 'Risperdal oral: episodios maníacos moderados a graves; LAI solo esquizofrenia [R1–R3]',
    'Paliperidona': 'Invega y palmitatos: esquizofrenia/esquizoafectivo; TB fuera de ficha [R4–R7]',
    'Aripiprazol': 'Abilify: manía TB-I; prevención maníaca tras respuesta; Maintena solo esquizofrenia [R1–R2]',
    'Cariprazina': 'Reagila: solo esquizofrenia; TB fuera de ficha [R1]',
    'Asenapina': 'Sycrest SL: episodios maníacos TB-I; mantenimiento fuera de ficha [R1]',
    'Ziprasidona': 'Zeldox: episodios maníacos o mixtos moderados; sin prevención [R1]',
    'Haloperidol': 'Esteve oral: manía moderada-grave; IM: agitación aguda grave [R1–R2]'}
FDA_NOTE = {
    'Litio': 'manía/mixto y mantenimiento TB-I [R2]', 'Valproato': 'Depakote ER: manía/mixto [R2]',
    'Lamotrigina': 'mantenimiento TB-I [R2]', 'Lurasidona': 'depresión TB-I, sola o con Li/VPA [R2]',
    'Olanzapina': 'Lybalvi (con samidorfano): manía/mixto y mantenimiento [R3]',
    'Olanzapina-fluoxetina': 'Symbyax: depresión TB-I [R2]', 'Risperidona': 'Uzedy SC: mantenimiento TB-I (2025) [R8]',
    'Cariprazina': 'Vraylar: manía/mixto y depresión TB-I [R2]', 'Ziprasidona': 'Geodon: mantenimiento añadido a Li/VPA [R2]'}


def p56():
    n = 56
    it = new_page('Farmacología del TB: mapa de autorizaciones', 'FARMACOLOGÍA · I',
                  'F · fichas CIMA y FDA citadas en los dosieres D01–D13 | I · lectura por fase | no prescriptivo (p. 20)', n)
    subtitle(it, 'Quince principios activos, tres fases y dos agencias: la autorización delimita el uso de ficha, no la jerarquía de eficacia.')
    t0, t1 = 128.0, 690.0
    panel(it, 50, t0, 1141, t1, 'Indicación en España (CIMA) por fase y nota de la ficha estadounidense', accent=TEAL)
    cx = [250.0, 318.0, 386.0]
    for c, lab in zip(cx, ('Manía/mixto', 'Depresión', 'Prevención')):
        ctext(it, c, t0 + 52, lab, 'Roboto-Bold', 10, NAVY)
    it.append(text(430, t0 + 52, 'Ficha española (síntesis del dosier)', 'Roboto-Bold', 10, NAVY))
    it.append(text(860, t0 + 52, 'FDA (si consta en el dosier)', 'Roboto-Bold', 10, NAVY))
    pitch = 31.0
    for k, d in enumerate(DRUGS):
        yb = t0 + 78 + pitch * k
        if k % 2 == 0:
            it.append(rect_top(60, yb - 17, 1131, yb + 15, 3, fill=PALE))
        it.append(text(68, yb + 4, d, 'Roboto-Medium', 11, INK))
        it.append(text(196, yb + 4, DCODE[d], 'Roboto-Regular', 9, GRAY))
        for c, kind in zip(cx, AUTH[d]):
            mark(it, c, yb, kind)
        s = CIMA_NOTE[d]
        assert sw(s, 'Roboto-Regular', 9.5) < 420, s
        it.append(text(430, yb + 3.5, s, 'Roboto-Regular', 9.5, INK))
        f = FDA_NOTE.get(d, 'no consta en el dosier')
        it.append(text(860, yb + 3.5, f, 'Roboto-Regular', 9.5, INK if d in FDA_NOTE else GRAY))
    legend_marks(it, 68, t1 - 16, [('full', 'indicación de ficha'), ('half', 'condicionada o genérica'),
                                   ('ring', 'fuera de ficha o sin indicación bipolar')])
    note(it, 50, t1 + 12, 1141, 'I · Cómo se lee', [
        'Litio: ficha genérica sin especificar polo; valproato: reservado a contraindicación o intolerancia al litio. Fuera de ficha no '
        'significa sin evidencia: lurasidona, cariprazina y olanzapina-fluoxetina tienen ensayos positivos en depresión (p. 59).'], kind='info', where='p56')
    return it


# ------------------------------------------------------------------ 57 · cómo leer la evidencia
def p57():
    n = 57
    it = new_page('Cómo leer la evidencia farmacológica', 'FARMACOLOGÍA · MÉTODO',
                  'I · advertencias comunes a los trece dosieres | E · ejemplos de D05, D08, D11, D12 | G · esquema de diseño', n)
    subtitle(it, 'Afinidad, ocupación, respuesta aguda y prevención son cuatro preguntas distintas, y cada ensayo responde solo a una.')
    top = 130.0
    top = card_row(it, [
        dict(title='Ki no es ocupación, ni ocupación es respuesta', pill='E · I', body=[
            'La afinidad in vitro no predice la ocupación cerebral, que depende de la exposición, la fracción libre y el momento de la '
            'medida. En la PET de asenapina la ocupación D2 cae del 79 % a las 3–4 h al 38 % a las 15 h [D11 · P2]; la de quetiapina '
            'IR pasa del 50 % en el pico al 7 % en el valle [D05 · P3], y la de ziprasidona, del 65,6 % a las 5 h al 2 % a las 23 h '
            '[D12 · P2]. Ninguna de esas cifras define un umbral de eficacia en manía.']),
        dict(title='Episodio agudo y prevención no se miden igual', pill='I', body=[
            'Los ensayos agudos comparan el cambio en una escala (YMRS, MRS o MADRS) a las 3–8 semanas; los de mantenimiento miden el '
            'tiempo hasta una recurrencia o una intervención. Un fármaco puede ser eficaz en la manía y no prevenir la depresión, y la '
            'prevención global no implica protección de cada polo: por eso las pp. 60–61 separan siempre la polaridad.']),
    ], top, X2, where='p57', bsize=12, lead=17.6) + 14
    # esquema de diseño enriquecido
    t0, t1 = top, top + 210
    panel(it, 50, t0, 1141, t1, 'Diseño de retirada enriquecido: a quién se aplica el resultado', accent=PURPLE)
    yb = t0 + 100
    boxes = [(80, 300, 'Fase abierta con el fármaco', 'todos los incluidos', TEAL),
             (360, 560, 'Respondedores estables', 'solo quienes toleran y responden', TEAL),
             (640, 860, 'Continuar el fármaco', 'brazo activo', BLUE),
             (640, 860, 'Placebo o retirada', 'brazo control', GRAY)]
    for k, (a, bnd, l1, l2, col) in enumerate(boxes):
        dy = 0 if k < 2 else (-34 if k == 2 else 34)
        it.append(rect_top(a, yb - 24 + dy, bnd, yb + 24 + dy, 8, fill=WHITE, stroke=col, lw=1.6))
        ctext(it, (a + bnd) / 2, yb - 3 + dy, l1, 'Roboto-Bold', 11, NAVY)
        ctext(it, (a + bnd) / 2, yb + 13 + dy, l2, 'Roboto-Regular', 9.5, GRAY)
    arrow(it, 302, yb, 356, yb, color=INK)
    arrow(it, 562, yb, 636, yb - 34, color=INK)
    arrow(it, 562, yb, 636, yb + 34, color=INK)
    it.append(rect_top(84, t0 + 46, 304, t0 + 58, 3, fill=OCHRE, alpha=0.25))
    it.append(text(90, t0 + 56, 'abandonos y no respondedores salen', 'Roboto-Regular', 9, INK))
    lines_block(it, 890, yb - 36, ['El efecto estimado es el de', 'mantener el fármaco en quien ya', 'respondió a él; no se extrapola',
                                    'a no respondedores ni a otro', 'episodio índice.'], size=10.5, color=INK, lead=14.5)
    it.append(text(68, t1 - 12, 'G · Esquema común a Weisler 144, Szegedi, Keck, Quiroz, Tohen 2006, Berwaerts y MD-25 según los dosieres; '
                   'el episodio índice condiciona la polaridad que se previene.', 'Roboto-Regular', 9.5, GRAY))
    top = t1 + 14
    card_row(it, [
        dict(title='LOCF, MMRM y lecturas de figura', pill='I', body=[
            'LOCF arrastra la última observación y MMRM modela los datos ausentes; no se mezclan en una misma curva. Varias curvas de '
            'los dosieres son redibujos aproximados de figuras publicadas, y así se indica en cada lámina original.']),
        dict(title='SMD, RR, OR y HR', pill='I', body=[
            'La diferencia estandarizada permite comparar escalas distintas; RR y OR resumen proporciones; HR, el ritmo de eventos en '
            'el tiempo. Una cifra de una métrica no se traslada a otra, y las redes comparan también de forma indirecta.']),
        dict(title='Polaridad y episodio índice', pill='I', body=[
            'El polo que se previene depende en parte del episodio índice: lamotrigina dio perfiles distintos tras manía y tras '
            'depresión [D04 · L2–L3]. Las estimaciones por polo suelen ser secundarias o pos hoc.']),
    ], top, X3, where='p57', accent=OCHRE, fill=NOTEFILL, bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 58 · manía aguda
def p58():
    n = 58
    it = new_page('Manía aguda: magnitud comparada', 'FARMACOLOGÍA · MANÍA',
                  'E · red de Cipriani (P83) y ensayos pivotales de los dosieres | I · escalas distintas no se comparan en bruto', n)
    subtitle(it, 'Todos los antimaníacos estudiados superan al placebo, pero la magnitud varía; los antipsicóticos agrupados superaron a los estabilizadores.')
    t0, t1 = 128.0, 548.0
    panel(it, 50, t0, 560, t1, 'Diferencia de medias estandarizada frente a placebo (P83)', accent=RED)
    rows = [('Haloperidol', -0.56, -0.69, -0.43), ('Risperidona', -0.50, -0.63, -0.38), ('Olanzapina', -0.43, -0.54, -0.32),
            ('Litio', -0.37, -0.63, -0.11), ('Quetiapina', -0.37, -0.51, -0.23), ('Aripiprazol', -0.37, -0.51, -0.23),
            ('Carbamazepina', -0.36, -0.60, -0.11), ('Asenapina', -0.30, -0.53, -0.07), ('Valproato', -0.20, -0.37, -0.04),
            ('Ziprasidona', -0.20, -0.37, -0.03)]
    lforest(it, 180, 420, t0 + 68, 30.0, [(a, b, c, d, RED) for a, b, c, d in rows], -0.8, 0.1,
            [-0.8, -0.6, -0.4, -0.2, 0], zero=0.0, fmt='%.2f')
    lines_block(it, 68, t1 - 30, ['68 ensayos, 16.073 participantes, 3 semanas. Lamotrigina, gabapentina y topiramato',
                                   'no superaron al placebo. Valores negativos favorecen al fármaco.'], size=9.5, lead=13)
    # dumbbell de ensayos pivotales
    gx0 = 582.0
    panel(it, gx0, t0, 1141, t1, 'Cambio desde el basal en el ensayo pivotal del dosier', accent=NAVY)
    trials = [('Risperidona · Khanna 2005', -23.2, -10.8, 'YMRS', 'D08 · T1'),
              ('Olanzapina · Tohen 2000', -14.8, -8.1, 'YMRS', 'D07 · T1'),
              ('Quetiapina IR · Bowden', -14.6, -6.7, 'YMRS', 'D05 · T1'),
              ('Haloperidol · Young 2009', -12.8, -9.7, 'YMRS', 'D13 · T1'),
              ('Litio · CN138-135', -12.03, -9.01, 'YMRS', 'D01 · T1'),
              ('Aripiprazol · Young 2009', -12.0, -9.7, 'YMRS', 'D09 · T1'),
              ('Asenapina · A7501004', -11.5, -7.8, 'YMRS', 'D11 · B2'),
              ('Valproato ER · Bowden 2006', -11.5, -9.0, 'MRS', 'D02 · T1'),
              ('Ziprasidona · Keck 2003', -12.4, -7.8, 'MRS', 'D12 · T1')]
    x0, x1 = 800.0, 1110.0
    pos = None
    for k, (lab, a, b, sc, src) in enumerate(trials):
        yb = t0 + 70 + 33 * k
        it.append(text(gx0 + 18, yb + 4, lab, 'Roboto-Regular', 10.5, INK))
        it.append(text(gx0 + 18 + sw(lab, 'Roboto-Regular', 10.5) + 6, yb + 4, '%s [%s]' % (sc, src), 'Roboto-Regular', 8.5, GRAY))
        pos = dumbbell(it, x0, x1, yb, -25, 0, a, b, RED)
        s = ('%g' % a).replace('.', ',').replace('-', '−')
        it.append(text(pos(a) - sw(s, 'Roboto-Medium', 9) / 2, yb - 9, s, 'Roboto-Medium', 9, RED))
    axis_ticks(it, pos, [-25, -20, -15, -10, -5, 0], t0 + 50, t0 + 70 + 33 * 8 + 12)
    dot(it, gx0 + 24, t1 - 26, 5, RED)
    it.append(text(gx0 + 34, t1 - 22, 'fármaco', 'Roboto-Regular', 9.5, INK))
    dot(it, gx0 + 100, t1 - 26, 5, WHITE, stroke=GRAY, lw=1.6)
    it.append(text(gx0 + 110, t1 - 22, 'placebo · 3–4 semanas; YMRS y MRS no son intercambiables', 'Roboto-Regular', 9.5, INK))
    it.append(text(gx0 + 18, t1 - 8, 'E · Cifras literales de los dosieres; poblaciones, rescates y gravedad basal difieren.',
                   'Roboto-Regular', 9, GRAY))
    top = t1 + 14
    card_row(it, [
        dict(title='Respuesta en las síntesis de cada dosier', pill='E', body=[
            'Litio, respuesta OR 2,13 [1,73–2,63], seis ensayos, certeza alta [D01 · E1]. Valproato, RR 1,42 [1,19–1,71] [D02 · E1] y 45 % '
            'frente a 29 % en Cochrane. Carbamazepina ERC, 52 % frente a 26 % en el análisis conjunto [D03 · T3]. Asenapina, RR 1,28 '
            '[1,05–1,56] [D11 · E2]; ziprasidona, 50 % frente a 35 % [D12 · T1].']),
        dict(title='Lo que el gráfico no dice', pill='I', body=[
            'La red de Cipriani (P83) también encontró que olanzapina, risperidona y quetiapina tuvieron menos abandonos que litio y '
            'placebo. La elección integra tolerabilidad, riesgo de viraje, comorbilidad y plan preventivo: la manía es el episodio '
            'índice de un curso que continúa (pp. 60–62). Lamotrigina no está indicada en manía [D04 · G4].']),
    ], top, X2, where='p58', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 59 · depresión bipolar
def p59():
    n = 59
    it = new_page('Depresión bipolar: qué separa del placebo', 'FARMACOLOGÍA · DEPRESIÓN',
                  'E · redes P84–P86 y ensayos de los dosieres | I · el polo depresivo tiene menos opciones eficaces que el maníaco', n)
    subtitle(it, 'Pocas moléculas superan al placebo en depresión bipolar, y varias eficaces en manía fracasan en este polo.')
    t0, t1 = 128.0, 476.0
    panel(it, 50, t0, 600, t1, 'Respuesta (MADRS ≥ 50 %) en el ensayo de registro', accent=BLUE)
    trials = [('Olanzapina-fluoxetina · Tohen 2003', 56.1, 30.4, 'D07 · T2'),
              ('Quetiapina 300 mg · BOLDER I', 57.6, 36.1, 'D05 · T2'),
              ('Lurasidona 20–60 mg · PREVAIL 2', 53.0, 30.0, 'D06 · T1'),
              ('Lurasidona 20–60 mg · Kato', 46.2, 31.0, 'D06 · T3'),
              ('Olanzapina sola · Tohen 2003', 39.0, 30.4, 'D07 · T2'),
              ('Ziprasidona 40–80 mg · Lombardo 1', 53.0, 49.0, 'D12 · T2'),
              ('Carbamazepina · Zhang 2007', 63.8, 34.8, 'D03 · T4')]
    x0, x1 = 360.0, 570.0
    pos = None
    for k, (lab, a, b, src) in enumerate(trials):
        yb = t0 + 68 + 32 * k
        it.append(text(68, yb + 4, lab, 'Roboto-Regular', 10.5, INK))
        it.append(text(68 + sw(lab, 'Roboto-Regular', 10.5) + 6, yb + 4, '[%s]' % src, 'Roboto-Regular', 8.5, GRAY))
        pos = dumbbell(it, x0, x1, yb, 20, 70, a, b, BLUE if k < 5 else (GRAY if k == 5 else OCHRE))
        s = ('%g' % a).replace('.', ',') + ' %'
        it.append(text(pos(a) + 9, yb - 5, s, 'Roboto-Medium', 9, INK))
    axis_ticks(it, pos, [20, 30, 40, 50, 60, 70], t0 + 48, t0 + 68 + 32 * 6 + 12, suffix='')
    lines_block(it, 68, t1 - 26, ['Punto relleno: fármaco; anillo: placebo. Ziprasidona fracasó en el objetivo primario; el ensayo de',
                                   'carbamazepina es pequeño (124 personas en tres brazos) y criterio clínico propio.'], size=9.5, lead=13)
    # MADRS diferencias
    gx0 = 622.0
    panel(it, gx0, t0, 1141, t1, 'Diferencia MADRS frente a placebo', accent=BLUE)
    rows = [('Quetiapina (P85)', -4.80, -5.93, -3.72, BLUE, 'dot'), ('Lurasidona (P85)', -4.71, -6.98, -2.41, BLUE, 'dot'),
            ('Olanzapina (P85)', -4.57, -5.92, -3.20, BLUE, 'dot'), ('Cariprazina (P85)', -2.29, -3.47, -1.09, BLUE, 'dot'),
            ('Lurasidona · PREVAIL 2', -4.6, -6.9, -2.3, NAVY), ('Cariprazina 1,5 · MD-56', -4.0, -6.3, -1.6, NAVY),
            ('Cariprazina 1,5 · MD-54', -2.5, -4.6, -0.4, NAVY), ('Cariprazina 3 · MD-53', -1.8, -3.9, 0.4, GRAY)]
    lforest(it, 790, 990, t0 + 62, 28.0, rows, -8, 1, [-8, -6, -4, -2, 0], fmt='%.1f', lsize=10)
    lines_block(it, gx0 + 18, t1 - 26, ['P85: red bayesiana financiada por el fabricante de lurasidona (ICr 95 %). Cuadrados: ensayos de',
                                         'los dosieres [D06 · T1; D10 · T3–T5], IC 95 % nominal. Negativo favorece al fármaco.'], size=9.5, lead=13)
    top = t1 + 14
    top = card_row(it, [
        dict(title='La red más amplia', pill='E · P84', body=[
            'Yildiz y colaboradores (101 ECA, 20.081 participantes) encontraron, con confianza moderada, que olanzapina-fluoxetina, '
            'quetiapina, olanzapina, lurasidona, lumateperona, cariprazina y lamotrigina superan al placebo, con SMD de 0,41 para '
            'olanzapina-fluoxetina a 0,16 para lamotrigina. Los antidepresivos como clase parecían eficaces, con más viraje maníaco '
            'que los antipsicóticos.']),
        dict(title='Resultados negativos que importan', pill='E', body=[
            'Litio en EMBOLDEN I: −13,60 frente a −11,81 en MADRS, p=0,123 [D01 · T3]. Lamotrigina: ninguno de cinco ensayos superó al '
            'placebo en su objetivo primario, aunque los datos individuales dan RR de respuesta 1,22–1,27 [D04 · T2, E1]. Aripiprazol '
            '(dos ensayos de Thase) y ziprasidona (dos de Lombardo) fueron negativos [D09 · T2; D12 · T2].']),
        dict(title='Fuera de ficha en España', pill='F · I', body=[
            'De las opciones con mejor evidencia, solo quetiapina tiene indicación española en depresión bipolar. Lurasidona, '
            'cariprazina y la combinación olanzapina-fluoxetina requieren el procedimiento de uso fuera de ficha (p. 56). Antidepresivos '
            'y viraje: p. 31.']),
    ], top, X3, where='p59', bsize=11.2, lead=16.2) + 12
    return it


# ------------------------------------------------------------------ 60 · mantenimiento por polaridad
KISHI = [  # (fármaco, any, dep, manía, abandono)  True = superó a placebo en P87
    ('Aripiprazol', True, False, True, False), ('Aripiprazol mensual', True, False, True, False),
    ('Asenapina', True, False, True, True), ('Carbamazepina', False, False, False, False),
    ('Lamotrigina', True, True, False, False), ('Litio', True, True, True, True),
    ('Olanzapina', True, True, True, True), ('Paliperidona', False, False, True, False),
    ('Quetiapina', True, True, True, True), ('Risperidona inyectable', True, False, True, False),
    ('Valproato', True, False, True, True)]


def p60():
    n = 60
    it = new_page('Mantenimiento: prevención por polaridad', 'FARMACOLOGÍA · MANTENIMIENTO',
                  'E · red de Kishi (P87), Severus (P88) y ensayos de los dosieres | I · la prevención global no implica protección de cada polo', n)
    subtitle(it, 'La pregunta preventiva útil no es si un fármaco previene, sino qué polo previene en qué población estabilizada.')
    t0, t1 = 128.0, 590.0
    panel(it, 50, t0, 520, t1, 'Superioridad frente a placebo en monoterapia (P87)', accent=TEAL)
    cols = ['Cualquier', 'Depresión', 'Manía', 'Abandono']
    cxs = [262, 326, 390, 454]
    for c, lab in zip(cxs, cols):
        ctext(it, c, t0 + 52, lab, 'Roboto-Bold', 10, NAVY)
    for k, row in enumerate(KISHI):
        yb = t0 + 80 + 31 * k
        if k % 2 == 0:
            it.append(rect_top(60, yb - 15, 510, yb + 14, 3, fill=PALE))
        it.append(text(68, yb + 4, row[0], 'Roboto-Regular', 10.5, INK))
        for c, v in zip(cxs, row[1:]):
            mark(it, c, yb, 'full' if v else 'ring', TEAL if c != 326 else BLUE)
    lines_block(it, 68, t1 - 28, ['41 ECA, 9.821 participantes, 70,5 semanas de media. Anillo: sin superioridad demostrada, no',
                                   'ausencia de efecto. Abandono: por cualquier causa.'], size=9.5, lead=13)
    # forest triple por polo
    gx0 = 542.0
    panel(it, gx0, t0, 1141, t1, 'Estimaciones por polo en los ensayos de los dosieres', accent=NAVY)
    groups = [('Quetiapina · ensayo 144', 0.29, (0.23, 0.38), 0.29, (0.21, 0.40), 0.30, (0.20, 0.44), 'D05 · T6'),
              ('Quetiapina · continuación', 0.51, (0.38, 0.69), 0.75, (0.45, 1.24), 0.43, (0.30, 0.62), 'D05 · T7'),
              ('Asenapina · Szegedi', 0.22, (0.11, 0.43), 0.16, (0.06, 0.43), 0.35, (0.12, 1.02), 'D11 · T4'),
              ('Aripiprazol · Keck 2007', 0.53, (0.32, 0.87), 0.35, (0.16, 0.75), 0.81, (0.36, 1.81), 'D09 · T4'),
              ('Litio · Severus (RR)', 0.66, (0.53, 0.82), 0.52, (0.38, 0.71), 0.78, (0.59, 1.03), 'P88')]
    x0, x1 = 800.0, 1080.0

    def pos(v):
        return x0 + (math.log(v) - math.log(0.05)) / (math.log(2.0) - math.log(0.05)) * (x1 - x0)
    ytop, ybot = t0 + 48, t0 + 60 + 70 * 5
    for t in (0.1, 0.25, 0.5, 1.0, 2.0):
        it.append(line_top(pos(t), ytop, pos(t), ybot, stroke=LINE if t != 1.0 else INK, lw=0.6 if t != 1.0 else 1.2))
        s = ('%g' % t).replace('.', ',')
        it.append(text(pos(t) - sw(s, 'Roboto-Regular', 9) / 2, ybot + 12, s, 'Roboto-Regular', 9, GRAY))
    for g, (lab, a, ai, m, mi, d, di, src) in enumerate(groups):
        base = t0 + 74 + 70 * g
        it.append(text(gx0 + 18, base + 4, lab, 'Roboto-Medium', 10.5, INK))
        it.append(text(gx0 + 18, base + 18, '[%s]' % src, 'Roboto-Regular', 8.5, GRAY))
        for j, (v, ci, col, nm) in enumerate(((a, ai, NAVY, 'cualquier'), (m, mi, RED, 'manía'), (d, di, BLUE, 'depresión'))):
            yb = base - 8 + 16 * j
            it.append(line_top(pos(ci[0]), yb, pos(ci[1]), yb, stroke=col, lw=1.8))
            dot(it, pos(v), yb, 4, col)
            s = ('%.2f' % v).replace('.', ',')
            it.append(text(pos(ci[1]) + 6, yb + 3.5, s, 'Roboto-Regular', 8.5, col))
            it.append(text(718, yb + 3.5, nm, 'Roboto-Regular', 9, col))
    lines_block(it, gx0 + 18, t1 - 26, ['HR o RR frente a placebo, IC 95 %, escala logarítmica; <1 favorece al fármaco. Asenapina por',
                                         'polo: pos hoc. Todos son diseños enriquecidos o síntesis de ellos (p. 57).'], size=9.5, lead=13)
    top = t1 + 14
    card_row(it, [
        dict(title='Prevención negativa o incierta', pill='E', body=[
            'Cariprazina MD-25: HR 0,83 y 0,89, ambos IC cruzan 1 [D10 · T4]. Paliperidona: manía sí, depresión no, y redes no '
            'uniformes [D08 · T8]. Risperidona inyectable: elevación del ánimo p<0,001 y depresión p=0,805 en Quiroz [D08 · T2]. '
            'Lamotrigina previene la depresión (57 % frente a 45 % sin intervención al año), no la manía [D04 · L2].']),
        dict(title='I · Lectura clínica', body=[
            'La polaridad predominante (p. 45) y el episodio índice orientan la elección preventiva; Severus mostró, además, que el '
            'litio supera a los anticonvulsivos en la prevención de la manía (RR 0,66 [0,44–1,00]) sin diferencias en la depresiva '
            '(P88). Las pautas combinadas se leen aparte.']),
    ], top, X2, where='p60', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 61 · índice de polaridad
def p61():
    n = 61
    it = new_page('Índice de polaridad de los tratamientos de mantenimiento', 'FARMACOLOGÍA · POLARIDAD',
                  'E · Popovic et al. (P89) | E · validación naturalista negativa (P90) | I · enlace con la polaridad predominante (p. 45)', n)
    subtitle(it, 'Cociente entre el NNT para prevenir depresión y el NNT para prevenir manía: por encima de 1, perfil preventivo más antimaníaco.')
    t0, t1 = 128.0, 470.0
    panel(it, 50, t0, 1141, t1, 'Índice de polaridad por fármaco (P89) · escala logarítmica centrada en 1', accent=PURPLE)
    vals = [('Risperidona', 12.09), ('Aripiprazol', 4.38), ('Ziprasidona', 3.91), ('Olanzapina', 2.98), ('Litio', 1.39),
            ('Quetiapina', 1.14), ('Lamotrigina', 0.40)]
    x0, x1 = 260.0, 1060.0
    lo, hi = 0.25, 16.0

    def pos(v):
        return x0 + (math.log(v) - math.log(lo)) / (math.log(hi) - math.log(lo)) * (x1 - x0)
    for t in (0.25, 0.5, 1, 2, 4, 8, 16):
        it.append(line_top(pos(t), t0 + 50, pos(t), t0 + 60 + 34 * 7, stroke=LINE if t != 1 else INK, lw=0.6 if t != 1 else 1.4))
        s = ('%g' % t).replace('.', ',')
        it.append(text(pos(t) - sw(s, 'Roboto-Regular', 9) / 2, t0 + 74 + 34 * 7, s, 'Roboto-Regular', 9, GRAY))
    for k, (lab, v) in enumerate(vals):
        yb = t0 + 74 + 34 * k
        it.append(text(x0 - 12 - sw(lab, 'Roboto-Medium', 11.5), yb + 4, lab, 'Roboto-Medium', 11.5, INK))
        col = RED if v > 1 else BLUE
        a, bnd = sorted((pos(1), pos(v)))
        it.append(rect_top(a, yb - 9, bnd, yb + 7, 2, fill=col, alpha=1.0 if abs(v - 1) > 0.3 else 0.6))
        s = ('%.2f' % v).replace('.', ',')
        it.append(text((bnd + 6) if v > 1 else (a - 6 - sw(s, 'Roboto-Medium', 10)), yb + 4, s, 'Roboto-Medium', 10, INK))
    ctext(it, pos(0.5), t0 + 44, 'perfil antidepresivo', 'Roboto-Medium', 10, BLUE)
    ctext(it, pos(4), t0 + 44, 'perfil antimaníaco', 'Roboto-Medium', 10, RED)
    it.append(text(68, t1 - 14, 'E · Ensayos aleatorizados, doble ciego, de al menos 24 semanas frente a placebo. Valproato y oxcarbazepina no '
                   'se calcularon de forma fiable por el fracaso de sus ensayos de mantenimiento.', 'Roboto-Regular', 9.5, GRAY))
    top = t1 + 14
    card_row(it, [
        dict(title='Qué es y cómo se calcula', pill='E · P89', body=[
            'Popovic y colaboradores definen el índice como el cociente NNT de prevención depresiva / NNT de prevención maníaca '
            'obtenido de ensayos controlados con placebo. Un valor alto (risperidona, 12,09) indica que hay que tratar a muchas más '
            'personas para evitar una depresión que una manía; un valor bajo (lamotrigina, 0,40), lo contrario.']),
        dict(title='Su límite principal', pill='E · P90', body=[
            'En 653 pacientes italianos con curso bien caracterizado, el índice medio de los tratamientos prescritos no difirió entre '
            'polaridad predominante maníaca, depresiva o ausente, salvo con el método de Popovic y el criterio menos estricto. Los '
            'autores piden estudios prospectivos antes de usarlo para elegir.']),
        dict(title='I · Cómo lo usa el atlas', body=[
            'Como recordatorio de que la prevención tiene dirección, no como regla. Se lee junto con la polaridad predominante (p. 45), '
            'las estimaciones por polo de la p. 60 y la ficha de cada fármaco: el índice hereda los sesgos de los ensayos enriquecidos.']),
    ], top, X3, where='p61', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 62 · lámina 15 litio
def p62(tpl):
    curves = {
        'dep': [0.24, 0.74, 0.40, 0.26, 0.78, 0.36, 0.26, 0.30, 0.48, 0.30, 0.25, 0.26],
        'act': [0.30, 0.28, 0.82, 0.38, 0.30, 0.76, 0.36, 0.31, 0.30, 0.32, 0.31, 0.30],
        'fun': [0.80, 0.50, 0.44, 0.70, 0.48, 0.46, 0.66, 0.74, 0.68, 0.76, 0.78, 0.80],
        'res': [0.26, 0.40, 0.42, 0.36, 0.44, 0.46, 0.40, 0.34, 0.36, 0.32, 0.30, 0.29]}
    rows = [(140.0, 134.0, [(0.0, 6.0, 'Antes del litio: episodios de ambos polos', 'neu', False),
                            (6.0, 11.4, 'Con litio: intervalos más largos', 'neu', False)]),
            (159.0, 153.0, [(0.6, 1.5, 'Dep.', 'dep'), (1.5, 2.6, 'Manía', 'elev'), (3.6, 4.6, 'Dep.', 'dep'),
                            (4.6, 5.6, 'Manía', 'elev'), (7.6, 8.6, 'Subumbral', 'dep', False)])]
    it = make_sheet(tpl, pageno=62, title='Curso 15 · Mantenimiento con litio: antes y después',
                    tag='G · viñeta ilustrativa | E · D01 [E2, L1–L3], P88, P01 | I · relación con pp. 44, 60 y 61',
                    subtitle='Ejemplo conceptual: con litio desaparecen las manías y queda una depresión subumbral (RR 0,52 maníaco; 0,78 depresivo).',
                    curves=curves, rows=rows, thr=(0.60, 0.60, 'umbral de manía'), markers=[(6.0, 'inicio del litio')],
                    extra_foot='La línea vertical marca el inicio del litio; sin escala temporal ni litemias asignadas.')
    return it


# ------------------------------------------------------------------ 63 · receptores
REC_COLS = ['D2', 'D3', '5-HT1A', '5-HT2A', '5-HT2C', '5-HT7', 'H1', 'α1', 'M1', 'NET']
REC = {  # pKi (= 9 − log10 Ki en nM); None = no consta; 'b' = afinidad muy baja / >1000 nM
    'Asenapina [D11 · P1–P2]': [8.89, 9.40, 8.60, 10.20, 10.49, 9.89, 9.00, 8.89, 'b', None],
    'Cariprazina [D10 · P1]': [9.31, 10.07, 8.59, 7.73, 6.87, 6.95, 7.63, None, None, None],
    'Lurasidona [D06 · P1]': [9.00, None, 8.20, 9.33, None, 9.31, 'b', None, 'b', None],
    'Quetiapina [D05 · P1–P2]': [7.25, None, 5.74, 7.54, 5.55, None, 8.36, 7.84, 5.96, None],
    'Norquetiapina [D05 · P1]': [7.23, None, 6.24, 8.29, 7.12, None, 8.96, 7.33, 7.42, 7.54]}


def heat(v):
    f = max(0.0, min(1.0, (v - 5.5) / 5.0))
    return (0.95 - 0.70 * f, 0.94 - 0.55 * f, 0.92 - 0.30 * f)


def p63():
    n = 63
    it = new_page('Perfil receptorial y mecanismos', 'FARMACOLOGÍA · MECANISMO',
                  'E · afinidades in vitro de D05, D06, D10, D11 | E · mecanismos experimentales de D01–D04 | I · Ki ≠ ocupación ≠ respuesta', n)
    subtitle(it, 'La afinidad se expresa como pKi (a mayor valor, mayor afinidad); los ensayos, las especies y los radioligandos difieren entre fuentes.')
    t0, t1 = 128.0, 462.0
    panel(it, 50, t0, 1141, t1, 'Mapa de calor de afinidades (pKi) · solo moléculas con valores numéricos en los dosieres', accent=PURPLE)
    x0, cw = 300.0, 80.0
    for j, c in enumerate(REC_COLS):
        ctext(it, x0 + cw * j + cw / 2, t0 + 54, c, 'Roboto-Bold', 10.5, NAVY)
    for i, (dname, vals) in enumerate(REC.items()):
        yt = t0 + 66 + 44 * i
        it.append(text(68, yt + 26, dname, 'Roboto-Medium', 10.5, INK))
        for j, v in enumerate(vals):
            xa = x0 + cw * j + 3
            if v is None:
                it.append(rect_top(xa, yt + 4, xa + cw - 6, yt + 38, 4, fill=WHITE, stroke=LINE, lw=0.8))
                ctext(it, xa + (cw - 6) / 2, yt + 26, 'n. c.', 'Roboto-Regular', 9, GRAY)
            elif v == 'b':
                it.append(rect_top(xa, yt + 4, xa + cw - 6, yt + 38, 4, fill=(0.97, 0.96, 0.94), stroke=LINE, lw=0.8))
                ctext(it, xa + (cw - 6) / 2, yt + 26, '< 6', 'Roboto-Regular', 9.5, GRAY)
            else:
                col = heat(v)
                it.append(rect_top(xa, yt + 4, xa + cw - 6, yt + 38, 4, fill=col))
                s = ('%.1f' % v).replace('.', ',')
                ctext(it, xa + (cw - 6) / 2, yt + 26, s, 'Roboto-Medium', 10.5, WHITE if v > 8.3 else INK)
    lines_block(it, 68, t1 - 26, ['pKi calculado del Ki publicado (9 − log10 Ki en nM) salvo cariprazina, que el dosier da en pKi. α1: α1B en '
                                   'quetiapina; D2: D2L en cariprazina. n. c.: no consta;', '< 6: afinidad muy baja o Ki > 1.000 nM. Fármacos sin '
                                   'tabla de Ki en su dosier (aripiprazol, olanzapina, risperidona, ziprasidona, haloperidol) no se representan.'],
                size=9.2, lead=12.6)
    top = t1 + 14
    top = card_row(it, [
        dict(title='Litio', pill='E · D01', body=[
            'Inhibe GSK-3 por competencia con el Mg2+, con potencia dependiente del magnesio, e inhibe la inositol monofosfatasa en '
            'preparados cerebrales [P1, P2]. La espectroscopia de 7Li mide exposición cerebral en investigación [P3].']),
        dict(title='Valproato', pill='E · D02', body=[
            'Aumenta el recambio de GABA en la sustancia negra de la rata, reduce corrientes de sodio en preparaciones experimentales '
            'e inhibe histona-desacetilasas en sistemas celulares [P1–P3]. El peso de cada vía en el efecto bipolar sigue abierto.']),
        dict(title='Carbamazepina y lamotrigina', pill='E · D03 · D04', body=[
            'Ambas bloquean canales de sodio de forma dependiente del uso y del voltaje; carbamazepina tiene un 10,11-epóxido activo, '
            'y lamotrigina reduce la liberación evocada de glutamato en corteza de rata [D04 · P1–P2]. El mecanismo bipolar específico '
            'no está establecido.']),
    ], top, X3, where='p63', bsize=11.2, lead=16.2) + 12
    note(it, 50, top, 1141, 'I · Lectura', [
        'Asenapina muestra afinidad subnanomolar por varios receptores serotoninérgicos; cariprazina, preferencia D3 sobre D2 '
        '(10,07 frente a 9,31); lurasidona, afinidad alta por 5-HT7 y baja por H1 y M1; y la norquetiapina aporta la inhibición de NET '
        'que la quetiapina no tiene. Ninguna afinidad, por sí sola, explica el efecto antidepresivo o antimaníaco observado en los ensayos.'],
         kind='info', where='p63')
    return it


# ------------------------------------------------------------------ 64 · ocupación y exposición
def p64():
    n = 64
    it = new_page('Ocupación D2 y exposición en el tiempo', 'FARMACOLOGÍA · PK/PD',
                  'E · PET y fichas citadas en D01–D13 | I · umbrales de Kapur derivados de primer episodio psicótico | G · rangos', n)
    subtitle(it, 'La ocupación depende de la dosis, de la hora de la medida y de la semivida; los rangos proceden de poblaciones no bipolares.')
    t0, t1 = 128.0, 548.0
    panel(it, 50, t0, 580, t1, 'Ocupación D2 estriatal medida por PET (%)', accent=RED)
    occ = [('Haloperidol 1–5 mg', 38, 87, 'D13 · P1'), ('Risperidona 2–6 mg', 66, 79, 'D08 · P1'),
           ('Paliperidona 3–15 mg', 54.2, 85.5, 'D08 · P2'), ('Olanzapina 10–20 mg', 71, 80, 'D07 · P1'),
           ('Aripiprazol 10–30 mg', 87, 87, 'D09 · P1'), ('Cariprazina 1–3 mg', 45, 79, 'D10 · P2'),
           ('Lurasidona 10–80 mg', 41.3, 84.3, 'D06 · P2'), ('Asenapina 15 h a 3–4 h', 38, 79, 'D11 · P2'),
           ('Ziprasidona 23 h a 5 h', 2, 65.6, 'D12 · P2'), ('Quetiapina valle a pico', 7, 50, 'D05 · P3')]
    x0, x1 = 250.0, 540.0

    def pos(v):
        return x0 + v / 100.0 * (x1 - x0)
    for t in (0, 20, 40, 60, 80, 100):
        it.append(line_top(pos(t), t0 + 48, pos(t), t0 + 60 + 29 * 10, stroke=LINE, lw=0.5))
        it.append(text(pos(t) - sw(str(t), 'Roboto-Regular', 9) / 2, t0 + 72 + 29 * 10, str(t), 'Roboto-Regular', 9, GRAY))
    for thr, lab in ((65, '65'), (72, '72'), (78, '78')):
        it.append(line_top(pos(thr), t0 + 44, pos(thr), t0 + 60 + 29 * 10, stroke=OCHRE, lw=1.0, dash=([3.0, 2.5], 0.0)))
        ctext(it, pos(thr), t0 + 40, lab, 'Roboto-Medium', 8.5, OCHRE)
    for k, (lab, a, bnd, src) in enumerate(occ):
        yb = t0 + 64 + 29 * k
        it.append(text(68, yb + 4, lab, 'Roboto-Regular', 10, INK))
        it.append(text(68 + sw(lab, 'Roboto-Regular', 10) + 5, yb + 4, '[%s]' % src, 'Roboto-Regular', 8, GRAY))
        if bnd - a < 1:
            dot(it, pos(a), yb, 5.5, RED)
        else:
            it.append(rect_top(pos(a), yb - 6, pos(bnd), yb + 6, 6, fill=RED, alpha=0.55))
    lines_block(it, 68, t1 - 26, ['Líneas ocres: en Kapur 2000 (haloperidol), > 65 % se asoció a respuesta, > 72 % a hiperprolactinemia y',
                                   '> 78 % a SEP [D13 · P1]; no son objetivos para la manía. Aripiprazol: agonista parcial.'], size=9.2, lead=12.6)
    # semividas
    gx0 = 602.0
    panel(it, gx0, t0, 1141, t1, 'Semivida de eliminación (h) · escala logarítmica', accent=TEAL)
    hl = [('Risperidona (fracción activa)', 3, 24, 'D08'), ('Ziprasidona', 6.6, 6.6, 'D12'), ('Quetiapina / norquetiapina', 7, 12, 'D05'),
          ('Carbamazepina (inducida a única)', 9, 36, 'D03'), ('Lamotrigina (inductores a VPA)', 14, 70, 'D04'),
          ('Lurasidona', 18, 40, 'D06'), ('Litio', 18, 36, 'D01'), ('Asenapina', 24, 24, 'D11'),
          ('Aripiprazol (lentos 2D6)', 75, 146, 'D09'), ('Cariprazina total a DDCAR', 168, 456, 'D10'),
          ('Fluoxetina a norfluoxetina', 96, 384, 'D07')]
    x0, x1 = 830.0, 1110.0

    def hp(v):
        return x0 + (math.log(v) - math.log(2)) / (math.log(500) - math.log(2)) * (x1 - x0)
    for t in (2, 6, 24, 72, 168, 500):
        it.append(line_top(hp(t), t0 + 48, hp(t), t0 + 58 + 26 * 11, stroke=LINE, lw=0.5))
        it.append(text(hp(t) - sw(str(t), 'Roboto-Regular', 9) / 2, t0 + 70 + 26 * 11, str(t), 'Roboto-Regular', 9, GRAY))
    for k, (lab, a, bnd, src) in enumerate(hl):
        yb = t0 + 62 + 26 * k
        it.append(text(gx0 + 18, yb + 4, lab, 'Roboto-Regular', 10, INK))
        if bnd - a < 0.5:
            dot(it, hp(a), yb, 5, TEAL)
        else:
            it.append(rect_top(hp(a), yb - 5.5, hp(bnd), yb + 5.5, 5, fill=TEAL, alpha=0.6))
    lines_block(it, gx0 + 18, t1 - 26, ['Rangos de ficha o de contextos distintos (dosis única o repetida, inductores, metabolitos);',
                                         'cariprazina: ≈1 semana total, DDCAR terminal 13–19 días.'], size=9.2, lead=12.6)
    top = t1 + 14
    card_row(it, [
        dict(title='Exposición que cambia con el tiempo', pill='E', body=[
            'La carbamazepina induce su propio metabolismo: semivida ≈36 h tras dosis única, 16–24 h en administración repetida y 9–10 h '
            'con otros inductores [D03 · R1]. La fracción libre de valproato aumenta de ≈10 % a ≈18,5 % al subir la concentración total '
            '[D02 · R2], y la cariprazina tarda ≈3 semanas en alcanzar el 90 % de su equilibrio [D10 · R1].']),
        dict(title='Comida, formulación y hora de la muestra', pill='E', body=[
            'Ziprasidona con 250 kcal pierde el 60–90 % de la exposición frente a 500 kcal [D12 · P3]; lurasidona duplica el AUC con '
            'comida [D06 · R2]; asenapina tragada tiene biodisponibilidad < 2 % frente al 35 % sublingual [D11 · R1]. La litemia se '
            'interpreta a ≈12 h de la última toma [D01 · G5].']),
    ], top, X2, where='p64', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 65 · interacciones
INTER = [
    ('Carbamazepina (inductor CYP3A4)', [('Aripiprazol', 'AUC −73 %', False), ('Lamotrigina', 't½ ≈14 h', False),
                                          ('Paliperidona', 'Cmáx/AUC ≈−37 %', False), ('Quetiapina, olanzapina, haloperidol', 'exposición menor', False),
                                          ('Lurasidona, cariprazina', 'contraindicado', False), ('Anticonceptivos hormonales', 'fallo posible', False)], 'D03 · R1'),
    ('Valproato (inhibe UGT)', [('Lamotrigina', 't½ casi el doble', True), ('Paliperidona', 'Cmáx/AUC ≈+50 %', True),
                                ('Epóxido de carbamazepina', 'aumenta', True)], 'D02 · R1; D08'),
    ('Carbapenémicos', [('Valproato', '−60 a −100 % en ≈2 días', False)], 'D02 · R1'),
    ('Tiazidas, IECA/ARA-II, AINE, pérdida de sodio', [('Litio', 'litemia mayor', True)], 'D01 · R1–R2'),
    ('Inhibidores de CYP2D6 (fluoxetina, paroxetina)', [('Aripiprazol', 'como quinidina: AUC +107 %', True),
                                                         ('Risperidona, haloperidol', 'exposición mayor', True)], 'D09; D08; D13'),
    ('Inhibidores de CYP3A4', [('Aripiprazol', 'ketoconazol: AUC +63 %', True), ('Quetiapina, lurasidona, cariprazina', 'contraindicados (potentes)', True),
                               ('Carbamazepina', 'claritromicina, azoles: aumenta', True)], 'D09; D05; D06; D10; D03'),
    ('Fluvoxamina (CYP1A2)', [('Olanzapina', 'AUC +52 a +108 %', True), ('Asenapina', 'AUC +29 %', True)], 'D07; D11'),
    ('Estrógenos · tabaco', [('Lamotrigina', 'AUC ×0,48 con etinilestradiol', False), ('Olanzapina', 'tabaco acelera el aclaramiento', False)], 'D04 · P3; D07'),
]


def p65():
    n = 65
    it = new_page('Interacciones que cambian la exposición', 'FARMACOLOGÍA · INTERACCIONES',
                  'E · fichas e informes PK citados en los dosieres | I · selección de interacciones con efecto sobre la pauta | G · esquema', n)
    subtitle(it, 'Un cambio de concentración no se traduce en un porcentaje de efecto clínico, pero obliga a revisar dosis, niveles y síntomas.')
    t0 = 128.0
    pitch = 18.0
    rows = sum(len(v) for _, v, _ in INTER)
    t1 = t0 + 58 + sum(max(pitch * len(v), 30) for _, v, _ in INTER) + 10 * len(INTER) + 10
    panel(it, 50, t0, 1141, t1, 'Causa, fármaco afectado y efecto descrito', accent=OCHRE)
    it.append(text(68, t0 + 50, 'CAUSA', 'Roboto-Bold', 9.5, GRAY))
    it.append(text(500, t0 + 50, 'FÁRMACO AFECTADO', 'Roboto-Bold', 9.5, GRAY))
    it.append(text(800, t0 + 50, 'EFECTO', 'Roboto-Bold', 9.5, GRAY))
    yb = t0 + 74
    for cause, targets, src in INTER:
        it.append(line_top(60, yb - 14, 1131, yb - 14, stroke=LINE, lw=0.6))
        it.append(text(68, yb + 4, cause, 'Roboto-Medium', 10.5, INK))
        it.append(text(68, yb + 16, '[%s]' % src, 'Roboto-Regular', 8.5, GRAY))
        for k, (tg, eff, up) in enumerate(targets):
            y2 = yb + pitch * k
            arrow(it, 440, y2, 488, y2, color=GRAY, lw=1.0, head=5)
            it.append(text(500, y2 + 4, tg, 'Roboto-Regular', 10.5, INK))
            tri(it, 790, y2 - 1, 5.5, up, RED if up else BLUE)
            it.append(text(802, y2 + 4, eff, 'Roboto-Medium', 10.5, RED if up else BLUE))
        yb += max(pitch * len(targets), 30) + 10
    top = t1 + 14
    card_row(it, [
        dict(title='Interacciones farmacodinámicas', pill='E', body=[
            'Ziprasidona y haloperidol exigen revisar fármacos que prolongan el QT y corregir potasio y magnesio [D12 · R1; D13 · R1]. '
            'Valproato con topiramato o acetazolamida se ha vinculado a hiperamonemia [D02 · R1], y haloperidol con litio, a cuadros '
            'neurotóxicos raros [D13 · R1].']),
        dict(title='I · Introducir y retirar', body=[
            'La inducción y la inhibición también cambian al suspender: retirar carbamazepina eleva la exposición de los fármacos que '
            'inducía, y retirar valproato acorta la semivida de lamotrigina. Cada cambio de comedicación se fecha en la hoja de caso (p. 71).']),
    ], top, X2, where='p65', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 66 · monitorización
MON_COLS = ['Nivel', 'Renal', 'Tiroides', 'Calcio', 'Hemograma', 'Hepático', 'Sodio', 'Peso/IMC', 'Glucosa/lípidos', 'Prolactina',
            'ECG', 'HLA/piel', 'Embarazo']
MON = [
    ('Litio', 'D01 · G4', ['full', 'full', 'full', 'full', 'half', 'ring', 'full', 'full', 'ring', 'ring', 'half', 'ring', 'ring']),
    ('Valproato', 'D02 · R1, G3', ['half', 'ring', 'ring', 'ring', 'full', 'full', 'ring', 'full', 'ring', 'ring', 'ring', 'ring', 'full']),
    ('Carbamazepina', 'D03 · R1', ['half', 'half', 'ring', 'ring', 'full', 'full', 'half', 'ring', 'ring', 'ring', 'half', 'full', 'full']),
    ('Lamotrigina', 'D04 · G4', ['half', 'full', 'ring', 'ring', 'full', 'full', 'ring', 'ring', 'ring', 'ring', 'half', 'full', 'ring']),
    ('Antipsicóticos atípicos', 'D05–D11 · G4', ['ring', 'ring', 'ring', 'ring', 'half', 'ring', 'ring', 'full', 'full', 'half', 'half', 'ring', 'ring']),
    ('Ziprasidona', 'D12 · R1', ['ring', 'ring', 'ring', 'ring', 'ring', 'ring', 'ring', 'full', 'full', 'half', 'full', 'ring', 'ring']),
    ('Haloperidol', 'D13 · R1', ['ring', 'ring', 'ring', 'ring', 'ring', 'ring', 'ring', 'full', 'full', 'half', 'full', 'ring', 'ring'])]


def p66():
    n = 66
    it = new_page('Monitorización: qué se controla y cuándo', 'FARMACOLOGÍA · SEGUIMIENTO',
                  'F · NICE CG185 y fichas CIMA citadas en los dosieres | I · síntesis; la ficha y el riesgo individual mandan', n)
    subtitle(it, 'La monitorización no es un trámite: detecta toxicidad de margen estrecho, daño de órgano y carga metabólica antes de que limiten el tratamiento.')
    t0, t1 = 128.0, 462.0
    panel(it, 50, t0, 1141, t1, 'Controles basales y periódicos por fármaco o grupo', accent=TEAL)
    x0, cw = 300.0, 64.0
    for j, c in enumerate(MON_COLS):
        lab = c
        ctext(it, x0 + cw * j + cw / 2, t0 + 54, lab, 'Roboto-Bold', 8.8, NAVY)
    for i, (dname, src, vals) in enumerate(MON):
        yb = t0 + 82 + 34 * i
        if i % 2 == 0:
            it.append(rect_top(60, yb - 16, 1131, yb + 15, 3, fill=PALE))
        it.append(text(68, yb + 1, dname, 'Roboto-Medium', 11, INK))
        it.append(text(68, yb + 13, '[%s]' % src, 'Roboto-Regular', 8.5, GRAY))
        for j, v in enumerate(vals):
            mark(it, x0 + cw * j + cw / 2, yb, v)
    legend_marks(it, 68, t1 - 16, [('full', 'sistemático (basal y periódico)'), ('half', 'según riesgo, clínica o situación'),
                                   ('ring', 'no específico del fármaco')])
    # calendarios
    top = t1 + 14
    c0, c1 = top, top + 168
    panel(it, 50, c0, 1141, c1, 'Dos calendarios de referencia (NICE CG185, según los dosieres)', accent=NAVY)
    for r, (lab, steps, col) in enumerate((
            ('Litio [D01 · G4]', [('basal', 'renal, tiroides, calcio, ECG si riesgo'), ('semana 1', 'litemia tras inicio o ajuste'),
                                   ('hasta estable', 'litemia semanal'), ('primer año', 'litemia trimestral'),
                                   ('después', 'semestral; renal, calcio y tiroides cada 6 meses')], BLUE),
            ('Antipsicóticos [D05–D11 · G4]', [('basal', 'peso, pulso, TA, glucemia o HbA1c, lípidos, movimientos'),
                                               ('semanas 1–6', 'peso semanal; pulso y TA tras cada ajuste'),
                                               ('semana 12', 'peso, glucemia o HbA1c, lípidos'), ('anual', 'al menos anual según riesgo')], TEAL))):
        yb = c0 + 66 + 56 * r
        it.append(text(68, yb + 4, lab, 'Roboto-Bold', 10.5, NAVY))
        xs = 290.0
        w = (1120 - xs) / len(steps)
        it.append(line_top(xs, yb, 1110, yb, stroke=col, lw=2.0))
        for k, (s1, s2) in enumerate(steps):
            x = xs + w * k
            dot(it, x + 6, yb, 6, col)
            it.append(text(x + 16, yb - 6, s1, 'Roboto-Bold', 10, col))
            for m, ln in enumerate(_wrap2(s2, w - 22)):
                it.append(text(x + 16, yb + 9 + 12 * m, ln, 'Roboto-Regular', 9.2, INK))
    note(it, 50, c1 + 14, 1141, 'I · Alarmas que no esperan al calendario', [
        'Litio: vómitos o diarrea crecientes, temblor grosero, ataxia, disartria o confusión [D01 · G4]. Valproato: dolor abdominal con '
        'vómitos, ictericia, sangrado o cambio mental, también con perfil hepático normal (hiperamonemia) [D02 · R1]. Carbamazepina y '
        'lamotrigina: erupción con fiebre, mucosas o ampollas [D03 · R1; D04 · R1]. Ziprasidona y haloperidol: QTc > 500 ms [D12; D13].'],
         where='p66')
    return it


def _wrap2(s, width):
    from build_v3 import wrap
    return wrap(s, 'Roboto-Regular', 9.2, width)[:3]


# ------------------------------------------------------------------ 67 · seguridad
def p67():
    n = 67
    it = new_page('Seguridad: alertas por fármaco y carga motora', 'FARMACOLOGÍA · SEGURIDAD',
                  'E · tablas de acontecimientos adversos y fichas citadas en los dosieres | I · porcentajes de ensayo, no riesgo individual', n)
    subtitle(it, 'Cada molécula tiene su alerta dominante; la acatisia, frecuente con los agonistas parciales, se confunde con ansiedad, agitación o manía.')
    t0, t1 = 128.0, 430.0
    panel(it, 50, t0, 600, t1, 'Acatisia en ensayos de depresión o manía (%)', accent=RED)
    ak = [('Aripiprazol · Thase, estudio 1', 27.5, 4.8, 'D09 · T2'), ('Aripiprazol · Thase, estudio 2', 21.4, 2.8, 'D09 · T2'),
          ('Asenapina 10 mg/12 h · Landbloom', 15.1, 0.8, 'D11 · D1'), ('Lurasidona 80–120 mg · PREVAIL 2', 11.0, 2.0, 'D06 · R2'),
          ('Cariprazina 3 mg · depresión', 10.0, 2.0, 'D10 · R2'), ('Lurasidona 20–60 mg · PREVAIL 2', 8.0, 2.0, 'D06 · R2'),
          ('Cariprazina 1,5 mg · depresión', 6.0, 2.0, 'D10 · R2')]
    x0, x1 = 360.0, 560.0
    pos = None
    for k, (lab, a, b, src) in enumerate(ak):
        yb = t0 + 66 + 32 * k
        it.append(text(68, yb + 4, lab, 'Roboto-Regular', 10.2, INK))
        it.append(text(68, yb + 16, '[%s]' % src, 'Roboto-Regular', 8.2, GRAY))
        pos = dumbbell(it, x0, x1, yb, 0, 30, a, b, RED)
        s = ('%g' % a).replace('.', ',') + ' %'
        it.append(text(pos(a) + 9, yb - 5, s, 'Roboto-Medium', 9, INK))
    axis_ticks(it, pos, [0, 10, 20, 30], t0 + 48, t0 + 66 + 32 * 6 + 12)
    it.append(text(68, t1 - 12, 'Punto relleno: fármaco; anillo: placebo. Eventos notificados; categorías no excluyentes.', 'Roboto-Regular', 9.2, GRAY))
    # otras cifras
    gx0 = 622.0
    panel(it, gx0, t0, 1141, t1, 'Otras cifras de tolerabilidad en los dosieres', accent=NAVY)
    other = [('SEP a 12 semanas · haloperidol frente a aripiprazol', 53.3, 23.5, 'D13 · T1'),
             ('Boca seca · quetiapina 300 mg (TB-II)', 31.5, 9.8, 'D05'),
             ('Hipoestesia oral · asenapina 10 mg/12 h', 22.7, 1.6, 'D11 · D1'),
             ('Sedación · quetiapina 300 mg (TB-II)', 20.1, 5.6, 'D05'),
             ('Peso ≥ 10 % · olanzapina sola (ENLIGHTEN-2)', 29.8, 17.8, 'D07 · T7'),
             ('Peso ≥ 7 % · asenapina en manía', 6.5, 0.6, 'D11 · R1')]
    x0, x1 = 900.0, 1110.0
    for k, (lab, a, b, src) in enumerate(other):
        yb = t0 + 66 + 36 * k
        it.append(text(gx0 + 18, yb + 4, lab, 'Roboto-Regular', 9.8, INK))
        it.append(text(gx0 + 18, yb + 16, '[%s]' % src, 'Roboto-Regular', 8.2, GRAY))
        pos = dumbbell(it, x0, x1, yb, 0, 60, a, b, NAVY)
        s = ('%g' % a).replace('.', ',') + ' %'
        it.append(text(pos(a) + 9, yb - 5, s, 'Roboto-Medium', 9, INK))
    it.append(text(gx0 + 18, t1 - 12, 'Anillo: comparador (placebo, aripiprazol u olanzapina con samidorfano).', 'Roboto-Regular', 9.2, GRAY))
    top = t1 + 14
    card_row(it, [
        dict(title='Estabilizadores', pill='E', body=[
            'Litio: margen estrecho, riñón, tiroides y calcio [D01]. Valproato: hepatotoxicidad, hiperamonemia, plaquetas y '
            'contraindicaciones por POLG o ciclo de la urea [D02]. Carbamazepina: SSJ/NET, DRESS, HLA-B*15:02 en ascendencias de '
            'riesgo, hiponatremia y control de hemograma y función hepática [D03]. Lamotrigina: erupción grave 0,08 % en monoterapia inicial, sobre todo en 2–8 semanas [D04].']),
        dict(title='Antipsicóticos', pill='E', body=[
            'Olanzapina y quetiapina: carga metabólica y sedación [D05; D07]. Risperidona y paliperidona: prolactina y SEP [D08]. '
            'Aripiprazol: acatisia y control de impulsos (juego, sexo, compras, ingesta) [D09]. Ziprasidona y haloperidol: QTc; '
            'haloperidol, SEP y contraindicación en Parkinson y demencia con cuerpos de Lewy [D12; D13]. Lurasidona: peso casi neutro '
            '(+0,56 kg) [D06].']),
    ], top, X2, where='p67', bsize=11.2, lead=16.2)
    return it


# ------------------------------------------------------------------ 68 · reproducción
def p68():
    n = 68
    it = new_page('Seguridad reproductiva, anticoncepción y periparto', 'FARMACOLOGÍA · REPRODUCCIÓN',
                  'F · fichas CIMA, PRAC y AEMPS citadas en D02–D04, D10 | I · relación con pp. 32–33 | no prescriptivo', n)
    subtitle(it, 'La capacidad de gestación cambia la ecuación terapéutica desde la primera prescripción, no solo cuando se planifica un embarazo.')
    t0, t1 = 128.0, 410.0
    panel(it, 50, t0, 520, t1, 'Valproato: riesgos descritos en ficha [D02 · R1]', accent=RED)
    bars = [('Malformaciones mayores, población general', 2.5, '2–3 %', GRAY), ('Malformaciones mayores, monoterapia', 11, '≈11 %', RED),
            ('Retrasos del desarrollo temprano', 35, 'hasta 30–40 %', RED)]
    for k, (lab, v, s, col) in enumerate(bars):
        yb = t0 + 74 + 62 * k
        it.append(text(68, yb - 8, lab, 'Roboto-Regular', 10.5, INK))
        it.append(rect_top(68, yb, 68 + v * 9.5, yb + 18, 3, fill=col))
        it.append(text(76 + v * 9.5, yb + 13, s, 'Roboto-Medium', 10.5, INK))
    lines_block(it, 68, t1 - 40, ['Datos de madres con epilepsia en monoterapia; la ficha contraindica el embarazo en TB y exige',
                                   'plan de prevención de embarazos si hay capacidad de gestación.'], size=9.5, lead=13)
    gx0 = 542.0
    t = card(it, gx0, t0, 1141, title='Varones en tratamiento con valproato', pill='F · D02 · R3–R4', body=[
        'El PRAC concluyó en junio de 2026 que los estudios sobre neurodesarrollo tras exposición paterna son inconsistentes y la '
        'causalidad incierta, y mantuvo las medidas de 2024: informar y discutir anticoncepción eficaz, también para la pareja, '
        'durante la pauta y al menos tres meses después, y evitar la donación de esperma en ese periodo.'], where='p68', bsize=11.5,
        lead=16.6) + 12
    card(it, gx0, t, 1141, title='Carbamazepina', pill='F · D03 · R1, G2', t1=t1, body=[
        'La ficha advierte de daño fetal y limita el uso a situaciones en que el beneficio supere el riesgo tras valorar alternativas. '
        'Exige anticoncepción eficaz durante el tratamiento y dos semanas después, con atención al fallo de métodos hormonales por '
        'inducción. VA/DoD recomienda en contra en personas con capacidad de gestación.'], where='p68', bsize=11.5, lead=16.6)
    top = t1 + 14
    top = card_row(it, [
        dict(title='Lamotrigina y estrógenos', pill='E · D04 · P3', body=[
            'Con etinilestradiol y levonorgestrel, el AUC de lamotrigina bajó a 0,48 [0,44–0,53] y la Cmáx a 0,61; en la semana sin '
            'comprimidos los valles fueron aproximadamente el doble. Embarazo y posparto modifican la exposición y piden seguimiento '
            'especializado.']),
        dict(title='Cariprazina', pill='F · D10 · R1', body=[
            'La ficha exige anticoncepción muy eficaz durante el tratamiento y al menos 10 semanas después de la última dosis, por la '
            'persistencia de su metabolito DDCAR (semivida terminal de 13–19 días).']),
        dict(title='Lo que los dosieres no cubren', pill='I', body=[
            'No incluyen datos reproductivos específicos de litio ni de los antipsicóticos atípicos. Para el periparto, la ventana '
            'formal y el riesgo de recaída posparto se remiten a las pp. 32–33 (P40, P41).']),
    ], top, X3, where='p68', bsize=11.2, lead=16.2) + 12
    note(it, 50, top, 1141, 'I · Consecuencia clínica', [
        'La elección del estabilizador en una persona con capacidad de gestación se documenta desde el inicio: método anticonceptivo, '
        'interacciones con anticonceptivos hormonales (carbamazepina, lamotrigina), plan ante un embarazo y alternativas valoradas.'],
         kind='info', where='p68')
    return it


# ------------------------------------------------------------------ 69–70 · fichas sintéticas
FICHAS = [
    ('Litio', 'D01', 'Manía y prevención (CIMA)', 'CANMAT 1ª manía, depresión TB-I y mantenimiento',
     'Manía OR 2,13; prevención RR 0,66 (manía 0,52; depresión 0,78); EMBOLDEN I negativo en depresión aguda.',
     'Litemia 0,6–0,8 en mantenimiento (ISBD/IGSLI) a ≈12 h; tiazidas, IECA, AINE y deshidratación la elevan.'),
    ('Valproato', 'D02', 'Manía si litio no procede; continuación', 'CANMAT 1ª manía y mantenimiento TB-I',
     'Respuesta 48 % frente a 34 % (Bowden 2006); BALANCE: necesitó intervención el 69 % frente al 59 % con litio.',
     'Contraindicado en embarazo para TB; hepatotoxicidad, amonio, plaquetas; carbapenémicos lo anulan.'),
    ('Carbamazepina', 'D03', 'Manía y profilaxis (CIMA)', 'CANMAT 2ª manía y mantenimiento; 3ª depresión',
     'ERC: respuesta 52 % frente a 26 %; prevención con intervalo que incluye 1 (RR 0,68 [0,44–1,06]).',
     'Autoinducción, inductor potente de CYP3A4; HLA-B*15:02, SSJ/NET, sodio y hemograma.'),
    ('Lamotrigina', 'D04', 'Prevención depresiva en TB-I (CIMA)', 'CANMAT 1ª mantenimiento y depresión TB-I',
     'Depresión aguda: cinco ensayos negativos, RR de respuesta 1,22–1,27 en datos individuales; previene depresión, no manía.',
     'Titulación de 6 semanas, mitad con valproato; erupción grave en 2–8 semanas; estrógenos reducen la exposición.'),
    ('Quetiapina', 'D05', 'Manía, depresión TB-I/II, prevención', 'CANMAT 1ª en todas las fases; única 1ª en depresión TB-II',
     'BOLDER I respuesta 57,6 % frente a 36,1 %; ensayo 144 HR 0,29 para manía y 0,30 para depresión.',
     'Sedación, boca seca y carga metabólica; CYP3A4 (inhibidores potentes contraindicados).'),
    ('Lurasidona', 'D06', 'Fuera de ficha en España (FDA: depresión TB-I)', 'CANMAT 1ª depresión en monoterapia',
     'PREVAIL 2: diferencia MADRS −4,6 [−6,9 a −2,3]; sin eficacia en manía ni prevención en monoterapia.',
     'Tomar con ≥ 350 kcal; acatisia 8–11 %; peso casi neutro; CYP3A4 potente contraindicado.'),
    ('Olanzapina', 'D07', 'Manía y prevención tras respuesta', 'CANMAT 2ª manía y mantenimiento',
     'Manía −14,8 frente a −8,1; mantenimiento: recaída 46,7 % frente a 80,1 % a 48 semanas.',
     'Mayor carga metabólica; CYP1A2: fluvoxamina la eleva y el tabaco la reduce.'),
    ('Olanzapina-fluoxetina', 'D07', 'No comercializada en España (FDA: depresión TB-I)', 'CANMAT 2ª depresión; IPS 1ª',
     'Respuesta 56,1 % frente a 30,4 %; SMD 0,41 frente a placebo (P84); manía emergente 6,4 % frente a 6,7 %.',
     'Norfluoxetina persiste semanas; inhibición de CYP2D6; carga metabólica.'),
    ('Risperidona', 'D08', 'Manía moderada-grave (oral)', 'CANMAT 1ª manía; inyectable 2ª mantenimiento',
     'Manía −23,2 frente a −10,8; inyectable: prevención de elevación del ánimo, no de depresión (p=0,805).',
     'Prolactina y SEP; CYP2D6; LAI con latencia ≈3 semanas.'),
    ('Paliperidona', 'D08', 'Fuera de ficha en España', 'CANMAT 1ª manía (> 6 mg), 2ª mantenimiento',
     'Mantenimiento: mediana 558 frente a 283 días, HR placebo/PAL 1,43 [1,03–1,98]; dosis fijas: solo 12 mg separó.',
     'Eliminación renal (59 % inalterada): ajuste por aclaramiento; prolactina.'),
    ('Aripiprazol', 'D09', 'Manía TB-I y prevención maníaca', 'CANMAT 1ª manía y mantenimiento; no en depresión',
     'Manía −12,0 frente a −9,7; mantenimiento HR manía 0,35, depresión 0,81 (IC incluye 1).',
     'Acatisia (21–28 % en depresión); impulsos; CYP2D6/3A4 (CBZ −73 %).'),
    ('Cariprazina', 'D10', 'Fuera de ficha en España (FDA: manía y depresión TB-I)', 'CANMAT 1ª manía y depresión',
     'Depresión 1,5 mg superior a placebo en tres ensayos (−2,5 a −4,0 MADRS); mantenimiento MD-25 negativo.',
     'Metabolito DDCAR de semivida larga; acatisia; CYP3A4; anticoncepción 10 semanas.'),
    ('Asenapina', 'D11', 'Episodios maníacos TB-I (sublingual)', 'CANMAT 1ª manía y mantenimiento TB-I',
     'Manía −11,5 frente a −7,8; Szegedi HR 0,22 (manía 0,16; depresión 0,35, pos hoc).',
     'Hipoestesia oral, sedación, acatisia; no comer ni beber 10 minutos; Child-Pugh C: exposición ×7.'),
    ('Ziprasidona', 'D12', 'Episodios maníacos o mixtos moderados', 'CANMAT 2ª manía; 2ª mantenimiento añadida',
     'Manía −12,4 frente a −7,8 (MRS); depresión: dos ensayos negativos; mantenimiento solo como adyuvante.',
     'QTc (> 500 ms: interrumpir); tomar con ≥ 500 kcal; semivida 6,6 h.'),
    ('Haloperidol', 'D13', 'Manía moderada-grave; IM en agitación', 'CANMAT 2ª manía; NICE opción inicial',
     'Mayor SMD de la red (−0,56) y −12,8 frente a −9,7 en Young 2009; sin prevención establecida.',
     'SEP 53,3 % a 12 semanas; QTc y ECG con IM; contraindicado en Parkinson y cuerpos de Lewy.'),
]


def ficha_page(n, items, part):
    it = new_page('Fichas sintéticas por fármaco · %d' % part, 'FARMACOLOGÍA · FICHAS',
                  'F · indicación CIMA | F/I · CANMAT/ISBD 2023 según los dosieres (edición completa 2018: P91) | E · dato nuclear y alerta', n)
    subtitle(it, 'Cada ficha condensa el dosier correspondiente; las cifras completas, sus intervalos y las fuentes primarias están en cada dosier.')
    xs = [(50.0, 590.0), (601.0, 1141.0)]
    top = 128.0
    for k in range(0, len(items), 2):
        specs = []
        for d in items[k:k + 2]:
            name, code, ind, guide, ev, alert = d
            specs.append(dict(title=name, pill=code, body=['Ficha: ' + ind + '. Guía: ' + guide + '.', ev, alert]))
        xr = xs[:len(specs)]
        top = card_row(it, specs, top, xr, where='fichas%d' % part, bsize=10.8, lead=15.0, tsize=13) + 8
    return it


def p69():
    return ficha_page(69, FICHAS[:8], 1)


def p70():
    it = ficha_page(70, FICHAS[8:], 2)
    return it


# ------------------------------------------------------------------ 71 · hoja de caso
def p71():
    n = 71
    it = new_page('Hoja longitudinal farmacológica del caso', 'FARMACOLOGÍA · REGISTRO',
                  'I · plantilla sin puntuación validada | integra las hojas de caso de D01–D13 con las láminas del atlas', n)
    subtitle(it, 'Atribuir una mejoría, una recaída o un efecto adverso exige saber qué cambió, cuándo y con qué exposición medida.')
    blocks = [
        ('01 · Curso previo', 'Episodios fechados, polaridad predominante (p. 45), síntomas mixtos, residuo y funcionamiento entre '
         'episodios (p. 44). Respuestas y fracasos previos con dosis, duración y motivo de cambio.'),
        ('02 · Episodio índice y objetivo', 'Fase, gravedad, psicosis, sueño y riesgo suicida (p. 28). Separar el objetivo agudo del '
         'preventivo y anotar qué polo se pretende prevenir (pp. 60–61).'),
        ('03 · Pauta y exposición', 'Molécula, formulación, dosis, horario, comida cuando importa (ziprasidona, lurasidona), hora de la '
         'última toma y de la extracción, nivel y fecha de cada cambio de comedicación (p. 65).'),
        ('04 · Seguridad', 'Controles basales y periódicos (p. 66), alertas específicas (p. 67), anticoncepción y plan reproductivo (p. 68).'),
        ('05 · Curso en seguimiento', 'Síntomas residuales, nuevos episodios, intervenciones y funcionamiento, con los mismos criterios '
         'antes y después (lámina 15, p. 62).'),
        ('06 · Decisión y revisión', 'Fuente consultada (ficha, guía, ensayo), grado de incertidumbre, uso fuera de ficha y su '
         'procedimiento, y fecha de la próxima revisión. Retirada gradual en al menos cuatro semanas salvo toxicidad.'),
    ]
    top = 128.0
    for k in range(0, 6, 2):
        top = card_row(it, [dict(title=b[0], body=[b[1]]) for b in blocks[k:k + 2]], top, X2, where='p71', bsize=12,
                       lead=17.4, accent=NAVY) + 12
    note(it, 50, top, 1141, 'I · Por qué fechar cada cambio por separado', [
        'Si se introducen dos cambios a la vez, una mejoría o un efecto adverso no puede atribuirse a ninguno. Los dosieres insisten en '
        'registrar el motivo de cada modificación; el atlas añade la lectura dimensional (dominios ACE, p. 50) y el estadio clínico '
        '(p. 54) como contexto, sin convertirlos en criterio de elección.'], kind='info', where='p71')
    return it


NEW_PAGES34 = [p56, p57, p58, p59, p60, p61, 'p62', p63, p64, p65, p66, p67, p68, p69, p70, p71]

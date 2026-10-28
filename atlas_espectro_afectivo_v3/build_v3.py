"""Construye el Atlas clínico-geométrico v3 a partir del PDF v2.

Uso:  python3 build_v3.py ATLAS_..._v2.pdf ATLAS_..._v3.pdf

El PDF v2 es la única fuente: se lee su contenido (rutas y textos), se aplican
los cambios de la v3 (ver CAMBIOS_v3.md) y se vuelve a generar el PDF con
ReportLab y Roboto. Los hipervínculos del v2 se conservan."""
import copy
import sys
import os

import pypdf
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import replay
from replay import parse_pdf, register_fonts, draw_page, W, H

# ---------------------------------------------------------------- paleta (del v2)
NAVY = (0.062745, 0.14902, 0.211765)    # títulos
INK = (0.090196, 0.203922, 0.270588)    # texto y líneas de trazo
GRAY = (0.345098, 0.439216, 0.501961)   # texto secundario
LINE = (0.788235, 0.819608, 0.819608)   # reglas y rejillas
TEAL = (0.247059, 0.490196, 0.466667)
BLUE = (0.2, 0.46, 0.65)
RED = (0.72, 0.38, 0.28)
WHITE = (1.0, 1.0, 1.0)

PX0, PX1 = 175.0, 1095.0           # área de trazado de las láminas
STEP = (PX1 - PX0) / 11.0          # 12 puntos
PANEL = {'dep': (184.0, 263.0), 'act': (301.0, 380.0)}   # (top, base) top-based


# ---------------------------------------------------------------- utilidades
def Y(top):
    return H - top


def text(x, base, s, font='Roboto-Regular', size=12.0, fill=GRAY, alpha=1.0):
    return {'k': 'text', 'x': x, 'y': Y(base), 'font': font, 'size': size,
            'fill': fill, 'alpha': alpha, 'text': s}


def rrect_ops(x0, y0, x1, y1, r):
    if r <= 0:
        return [('m', x0, y0), ('l', x1, y0), ('l', x1, y1), ('l', x0, y1), ('h',)]
    k = 0.5522847498 * r
    return [('m', x0 + r, y0), ('l', x1 - r, y0),
            ('c', x1 - r + k, y0, x1, y0 + r - k, x1, y0 + r),
            ('l', x1, y1 - r),
            ('c', x1, y1 - r + k, x1 - r + k, y1, x1 - r, y1),
            ('l', x0 + r, y1),
            ('c', x0 + r - k, y1, x0, y1 - r + k, x0, y1 - r),
            ('l', x0, y0 + r),
            ('c', x0, y0 + r - k, x0 + r - k, y0, x0 + r, y0), ('h',)]


def path(ops, fill=None, stroke=None, lw=1.0, dash=None, alpha=1.0):
    return {'k': 'path', 'ops': ops, 'fill': fill, 'stroke': stroke, 'lw': lw,
            'dash': dash, 'alpha': alpha, 'eo': True}


def rect_top(x0, top0, x1, top1, r=0, **kw):
    return path(rrect_ops(x0, Y(top1), x1, Y(top0), r), **kw)


def line_top(x0, t0, x1, t1, stroke=INK, lw=1.0, dash=None):
    return path([('m', x0, Y(t0)), ('l', x1, Y(t1))], stroke=stroke, lw=lw, dash=dash)


def arrow_head_down(x, tip_top, size=10.0):
    y = Y(tip_top)
    return path([('m', x, y), ('l', x - 4.6, y + size), ('l', x + 4.6, y + size), ('h',)],
                fill=INK, stroke=INK, lw=1.0)


def bbox(ops):
    xs, ys = [], []
    for o in ops:
        if o[0] in ('m', 'l'):
            xs.append(o[1]); ys.append(o[2])
        elif o[0] == 'c':
            xs += [o[1], o[3], o[5]]; ys += [o[2], o[4], o[6]]
    return (min(xs), min(ys), max(xs), max(ys)) if xs else None


def shifted(it, dx=0.0, dy=0.0):
    n = copy.deepcopy(it)
    if n['k'] == 'text':
        n['x'] += dx; n['y'] += dy
    else:
        new = []
        for o in n['ops']:
            if o[0] in ('m', 'l'):
                new.append((o[0], o[1] + dx, o[2] + dy))
            elif o[0] == 'c':
                new.append(('c', o[1] + dx, o[2] + dy, o[3] + dx, o[4] + dy, o[5] + dx, o[6] + dy))
            else:
                new.append(o)
        n['ops'] = new
    return n


def find_text(items, s, nth=0, startswith=False):
    hits = [i for i, it in enumerate(items) if it['k'] == 'text' and
            ((it['text'].startswith(s)) if startswith else (it['text'] == s))]
    if len(hits) <= nth:
        raise KeyError('texto no encontrado: %r' % s)
    return hits[nth]


def replace_text(items, old, new, startswith=False):
    i = find_text(items, old, startswith=startswith)
    items[i]['text'] = new if not startswith else items[i]['text'].replace(old, new, 1)
    return i


def wrap(s, font, size, width):
    words, lines, cur = s.split(' '), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def add_paragraph(items, x, base, s, width, size=12.0, leading=17.4, font='Roboto-Regular', fill=GRAY):
    for n, ln in enumerate(wrap(s, font, size, width)):
        items.append(text(x, base + n * leading, ln, font, size, fill))
    return base + len(wrap(s, font, size, width)) * leading


def card_radius(it):
    b = bbox(it['ops'])
    return it['ops'][0][1] - b[0]


# ---------------------------------------------------------------- arreglos globales
ARROW = {  # texto exacto -> flecha prevista por el v2 (el glifo no existía en Roboto)
    'SÍNTOMAS DEPRESIVOS \x00': '→', '\x00 ACTIVACIÓN': '↑',
    'activación \x00': '↑', 'recurrencia \x00': '↑', 'impacto \x00': '↑', 'mejor \x00': '↑',
    'depresión \x00': '→', 'persistencia \x00': '→', 'carga residual \x00': '→',
    'TIEMPO RELATIVO \x00': '→', 'MESES 01–12 \x00': '→',
    'Un único eje “depresión \x00 manía”': '↔',
}


def fix_arrows(items):
    out = []
    for it in items:
        if it['k'] == 'text' and '\x00' in it['text']:
            arrow = ARROW[it['text']]
            pre, post = it['text'].split('\x00')
            bold = 'Bold' in it['font']
            afont = 'DejaVuSans-Bold' if bold else 'DejaVuSans'
            x = it['x']
            if pre:
                a = dict(it); a['text'] = pre; out.append(a)
                x += pdfmetrics.stringWidth(pre, it['font'], it['size'])
            g = dict(it); g['font'] = afont; g['text'] = arrow; g['x'] = x
            out.append(g)
            x += pdfmetrics.stringWidth(arrow, afont, it['size'])
            if post:
                a = dict(it); a['text'] = post; a['x'] = x; out.append(a)
        else:
            out.append(it)
    return out


def enlarge_tag(items):
    """Línea de procedencia bajo el encabezado (F/E/I/H/G): 8 pt -> 9 pt."""
    for it in items:
        if it['k'] == 'text' and it['size'] == 8.0 and abs(H - it['y'] - 49.0) < 0.5:
            it['size'] = 9.0
            it['y'] = Y(47.5)


# ---------------------------------------------------------------- matriz (pp. 4-6)
COLX0 = [404.0 + 103.0 * k for k in range(7)]


def rowbase(r):
    return 228.0 + 20.5 * (r - 1)


def cell_idx(items, r, k):
    rb, x0 = rowbase(r), COLX0[k]
    idx = []
    for i, it in enumerate(items):
        if it['k'] == 'text':
            if abs(H - it['y'] - rb) < 0.6 and x0 - 2 <= it['x'] <= x0 + 96 and it['text'] in ('R', 'V', '·'):
                idx.append(i)
        else:
            b = bbox(it['ops'])
            if abs(b[0] - x0) < 1.5 and abs((H - b[3]) - (rb - 11.0)) < 2.0 and abs(b[2] - b[0] - 94) < 1.5:
                idx.append(i)
    return idx


def set_cell(items, r, k, state):
    """state: 'V' o '·' ; clona el aspecto de otra celda de la misma página."""
    old = cell_idx(items, r, k)
    # fuente: otra celda con el estado pedido
    src = None
    for rr in range(1, 25):
        for kk in range(7):
            if (rr, kk) == (r, k):
                continue
            ids = cell_idx(items, rr, kk)
            texts = [items[i]['text'] for i in ids if items[i]['k'] == 'text']
            if state in texts and len(ids) == (2 if state == 'V' else 1):
                src = (rr, kk, ids)
                break
        if src:
            break
    assert src, 'sin celda modelo para %s' % state
    rr, kk, ids = src
    dx = COLX0[k] - COLX0[kk] if state == 'V' else (COLX0[k] - COLX0[kk])
    dy = -(rowbase(r) - rowbase(rr))
    new = [shifted(items[i], dx, dy) for i in ids]
    for i in sorted(old, reverse=True):
        del items[i]
    items.extend(new)


# ---------------------------------------------------------------- láminas (pp. 10-18)
def first_curve_index(items):
    for i, it in enumerate(items):
        if it['k'] == 'path' and it['stroke'] and it['lw'] == 3.0 and len(it['ops']) == 12:
            return i
    raise KeyError('curvas')


def curve_idx(items, color):
    for i, it in enumerate(items):
        if it['k'] == 'path' and it['stroke'] and it['lw'] == 3.0 and len(it['ops']) == 12 and \
                all(abs(a - b) < 0.01 for a, b in zip(it['stroke'], color)):
            return i
    raise KeyError('curva')


def set_curve(items, color, panel, vals):
    i = curve_idx(items, color)
    top, base = PANEL[panel]
    ops = []
    for n, v in enumerate(vals):
        y = Y(base - v * (base - top))
        ops.append(('m' if n == 0 else 'l', PX0 + n * STEP, y))
    items[i]['ops'] = ops


def xi(i):
    return min(max(PX0 + i * STEP, PX0), PX1)


KIND = {'dep': BLUE, 'elev': RED, 'neu': GRAY}

# lám: spans (a, b, rótulo, tipo); full=(rótulo) fila completa; thr=(valor_dep, valor_act, rótulo_act)
SHEETS = {
    10: dict(spans=[(1.5, 5.5, 'Episodio depresivo mayor', 'dep'), (6.5, 11.4, 'Remisión posible', 'neu')]),
    11: dict(spans=[(0.5, 2.5, 'Episodio depresivo', 'dep'), (2.5, 5.5, 'Intervalo', 'neu'),
                    (5.5, 7.5, 'Episodio depresivo', 'dep'), (7.5, 9.5, 'Intervalo', 'neu'),
                    (9.5, 11.4, 'Episodio depresivo', 'dep')]),
    12: dict(full='Curso persistente',
             spans=[(4.5, 6.5, 'Exacerbación posible', 'dep'), (8.5, 10.5, 'Exacerbación posible', 'dep')]),
    13: dict(spans=[(0.0, 11.0, 'Síntomas subumbrales · curso prolongado (≥2 años)', 'neu')],
             thr=(0.62, 0.68, 'umbral de hipomanía')),
    14: dict(spans=[(0.5, 1.5, 'Hipomanía', 'elev'), (1.5, 3.5, 'Depresión mayor', 'dep'),
                    (6.5, 8.5, 'Depresión mayor', 'dep'), (8.5, 9.5, 'Hipomanía', 'elev'),
                    (10.5, 11.4, 'Depresión mayor', 'dep')],
             thr=(0.60, 0.55, 'umbral de hipomanía')),
    15: dict(spans=[(1.5, 2.5, 'Manía', 'elev'), (3.5, 5.5, 'Depresión (opcional)', 'dep'),
                    (7.5, 8.5, 'Manía', 'elev'), (8.5, 10.5, 'Depresión (opcional)', 'dep')],
             thr=(0.60, 0.60, 'umbral de manía')),
    16: dict(spans=None, thr=(0.60, 0.55, 'umbral de elevación')),
    17: dict(spans=[(0.0, 11.0, 'Síntomas concurrentes · criterio formal aparte', 'neu')]),
    18: dict(spans=[(1.5, 4.5, 'Depresión con psicosis', 'dep'), (4.5, 6.5, '¿Psicosis fuera de episodio?', 'neu'),
                    (6.5, 8.5, 'Manía con psicosis', 'elev'), (8.5, 10.5, 'Depresión posterior', 'dep')]),
}


def ep_spans_16():
    # picos: depresión en i=1,4,7,10 ; elevación en i=2,5,8,11 -> 8 episodios numerados
    peaks = [(1, 'dep'), (2, 'elev'), (4, 'dep'), (5, 'elev'), (7, 'dep'), (8, 'elev'), (10, 'dep'), (11, 'elev')]
    return [(i - 0.5, min(i + 0.5, 11.4), 'ep. %d' % (n + 1), kind) for n, (i, kind) in enumerate(peaks)]


SHEETS[16]['spans'] = ep_spans_16()


def bracket(items, a, b, label, kind, line_top_y, label_base):
    x0, x1 = xi(a), xi(min(b, 11.0)) if b <= 11.0 else PX1
    col = KIND[kind]
    items.append(line_top(x0 + 1, line_top_y, x1 - 1, line_top_y, stroke=col, lw=1.6))
    items.append(line_top(x0 + 1, line_top_y, x0 + 1, line_top_y + 5, stroke=col, lw=1.6))
    items.append(line_top(x1 - 1, line_top_y, x1 - 1, line_top_y + 5, stroke=col, lw=1.6))
    items.append(text(x0 + 3, label_base, label, 'Roboto-Medium', 9.5, INK))


def patch_sheet(items, n):
    cfg = SHEETS[n]
    # --- corrección de contenido en curvas
    if n == 13:     # ciclotimia: la activación pasa a alternar con la depresión
        act = [0.53, 0.35, 0.59, 0.33, 0.55, 0.33, 0.53, 0.33, 0.57, 0.36, 0.53, 0.33]
        set_curve(items, RED, 'act', act)
    if n == 15:     # bipolar I: manía y depresión posmaníaca en secuencia (no coincidentes)
        set_curve(items, RED, 'act', [0.34, 0.35, 0.89, 0.37, 0.33, 0.33, 0.35, 0.33, 0.85, 0.34, 0.33, 0.34])
        set_curve(items, BLUE, 'dep', [0.24, 0.22, 0.27, 0.53, 0.88, 0.45, 0.24, 0.26, 0.26, 0.65, 0.83, 0.37])
        # el segundo recuadro «psicosis» acompaña al pico de manía desplazado una columna
        for i, it in enumerate(items):
            if it['k'] == 'text' and it['text'] == 'psicosis' and it['x'] > 900:
                items[i] = shifted(it, -STEP, 0)
        for i, it in enumerate(items):
            if it['k'] == 'path' and len(it['ops']) == 10 and it['fill'] is not None:
                b = bbox(it['ops'])
                if abs(b[0] - 927.7) < 3 and abs((b[3] - b[1]) - 27.0) < 2 and 396.0 < H - b[3] < 450.0:
                    items[i] = shifted(it, -STEP, 0)

    # --- quitar la leyenda flotante (salvo en la 16, cuyas notas son definitorias)
    leyenda = find_text(items, 'LEYENDA')
    if n == 16:
        items[leyenda]['text'] = 'NOTAS'
    else:
        del items[leyenda:leyenda + 5]       # rótulo + 2 recuadros + 2 textos

    # --- franjas de fase (detrás de las curvas)
    k0 = first_curve_index(items)
    bands = []
    for (a, b, label, kind) in cfg['spans']:
        x0 = xi(a)
        x1 = PX1 if b > 11.0 else xi(b)
        bands.append(rect_top(x0, 166.0, x1, 682.0, fill=KIND[kind], alpha=0.10 if kind != 'neu' else 0.07))
    items[k0:k0] = bands

    # --- llaves de fase sobre el primer panel
    if 'full' in cfg:
        bracket(items, 0.0, 11.0, cfg['full'], 'neu', 140.0, 134.0)
        row_line, row_label = 159.0, 153.0
    else:
        row_line, row_label = 159.0, 153.0
    for (a, b, label, kind) in cfg['spans']:
        bracket(items, a, b, label, kind, row_line, row_label)

    # --- umbral esquemático (solo 13-16)
    note2 = 'G · Franjas y llaves: fases ilustrativas, sin calibración.'
    if 'thr' in cfg:
        vd, va, lab = cfg['thr']
        for panel, v, name, base_lbl in (('dep', vd, 'umbral de episodio', 242.0), ('act', va, lab, 359.0)):
            top, base = PANEL[panel]
            ytop = base - v * (base - top)
            items.append(line_top(PX0, ytop, PX1, ytop, stroke=INK, lw=1.0, dash=([5.0, 3.0], 0.0)))
            items.append(line_top(68.0, base_lbl - 3.2, 84.0, base_lbl - 3.2, stroke=INK, lw=1.0,
                                  dash=([4.0, 2.5], 0.0)))
            items.append(text(88.0, base_lbl, name, 'Roboto-Regular', 8.0, GRAY))
        note2 += (' Línea discontinua: umbral esquemático de episodio, sin calibración; solo se dibuja '
                  'donde distingue el diagnóstico (láminas 04–07).')
    items.append(text(51.0, 787.0, note2, 'Roboto-Medium', 10.0, GRAY))


# ---------------------------------------------------------------- build
def build(src, out):
    register_fonts()
    pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
    pages = parse_pdf(src)
    links = {}
    rd = pypdf.PdfReader(src)
    for i, pg in enumerate(rd.pages):
        for a in pg.get('/Annots') or []:
            a = a.get_object()
            links.setdefault(i + 1, []).append(([float(v) for v in a['/Rect']], str(a['/A']['/URI'])))

    P = {n + 1: items for n, items in enumerate(pages)}

    # ---- p.9 rótulo de eje alineado con la p. 8 (antes de separar la flecha)
    j = find_text(P[9], 'depresión \x00')
    w_old = pdfmetrics.stringWidth('depresión ', P[9][j]['font'], P[9][j]['size'])
    w_new = pdfmetrics.stringWidth('síntomas depresivos ', P[9][j]['font'], P[9][j]['size'])
    P[9][j]['text'] = 'síntomas depresivos \x00'
    P[9][j]['x'] -= (w_new - w_old)
    ARROW['síntomas depresivos \x00'] = '→'

    # ---- global
    for n, items in P.items():
        P[n] = fix_arrows(items)
        enlarge_tag(P[n])

    # ---- p.1 portada
    replace_text(P[1], 'Modelo del atlas · edición revisada v2 · 28 octubre 2026',
                 'Modelo del atlas · edición revisada v3 · 28 octubre 2026')

    # ---- pp. 4-6 matriz
    set_cell(P[4], 13, 5, 'V')           # activación subjetiva (síntoma contrapolar DSM)
    set_cell(P[5], 13, 5, 'V')           # menor necesidad de sueño (síntoma contrapolar DSM)
    i = find_text(P[5], 'umbral')
    P[5][i]['text'] = '(episodio)'
    set_cell(P[6], 10, 5, 'V')           # reactividad del ánimo en melancólica: puede estar ausente
    replace_text(P[6],
                 'Tipo de entidad: D = diagnóstico base · S = especificador/presentación · O = otro especificado. Todas las celdas: I.',
                 'Tipo de entidad: D = diagnóstico base · S = especificador/presentación · O = otro especificado. Todas las celdas: I. '
                 'Reactividad del ánimo: R = conservada (fila 11); V en la fila 10 = puede estar ausente (p. 22).')

    # ---- p.8 cartografía
    i = find_text(P[8], 'G · El plano representa', startswith=True)
    add_paragraph(P[8], 51.0, 137.0,
                  'I · P04 respalda separar activación y valencia depresiva; P05 describe activación/inhibición como un '
                  'eje más un componente emocional, por lo que no sostiene por sí solo que ambos ejes sean independientes.',
                  1090.0, size=11.5, leading=15.0)
    # tarjeta «Fuera del plano»: más alta y con la nota E/I citada
    ci = [k for k, it in enumerate(P[8]) if it['k'] == 'path' and it['fill'] == WHITE and len(it['ops']) == 10
          and abs(bbox(it['ops'])[0] - 52.0) < 1 and abs(bbox(it['ops'])[2] - 1139.0) < 1][0]
    r_card = card_radius(P[8][ci])
    P[8][ci] = rect_top(52.0, 704.0, 1139.0, 790.0, r_card, fill=WHITE, stroke=LINE, lw=1.0)
    ai = ci + 1
    r_bar = card_radius(P[8][ai])
    P[8][ai] = rect_top(52.0, 704.0, 57.0, 790.0, r_bar, fill=INK)
    for s in ('Fuera del plano',):
        j = find_text(P[8], s); P[8][j]['y'] = Y(729.0)
    j = find_text(P[8], 'Persistencia, bipolaridad', startswith=True)
    del P[8][j]
    P[8].append(text(70.0, 748.0, 'Persistencia, bipolaridad y psicosis requieren historia y criterios propios.',
                     'Roboto-Regular', 11.5, GRAY))
    add_paragraph(P[8], 70.0, 763.0,
                  'E/I · Judd registra los mismos niveles semanales de gravedad (sindrómico, menor, subsindrómico) en '
                  'depresión unipolar (P02), bipolar I (P12) y bipolar II (P13): sostiene el solapamiento de rangos, '
                  'no su equivalencia clínica.', 1050.0, size=11.5, leading=15.0)

    # ---- sheets 10-18
    for n in range(10, 19):
        patch_sheet(P[n], n)

    # ---- p.19 transiciones
    it19 = P[19]
    drop = []
    for k, it in enumerate(it19):
        if it['k'] == 'path':
            b = bbox(it['ops'])
            top = H - b[3]
            # flechas diagonales/verticales antiguas desde «Primer episodio» y «Recurrencia»
            if (abs(b[0] - 130.0) < 1 and abs(b[1] - 396.0) < 1) or (abs(b[0] - 201.2) < 1 and abs(b[1] - 396.0) < 1) or \
               (abs(b[0] - 175.0) < 1 and abs(b[1] - 392.0) < 1) or (abs(b[0] - 469.0) < 1 and abs(b[1] - 392.0) < 1) or \
               (abs(b[0] - 740.0) < 1 and abs(b[1] - 397.0) < 1) or (abs(b[0] - 951.1) < 1 and abs(b[1] - 397.0) < 1):
                drop.append(k)
    assert len(drop) == 6, drop
    for k in reversed(drop):
        del it19[k]
    # recuadro que agrupa el curso depresivo y tres flechas hacia los fenómenos de elevación/mixtos
    it19.append(rect_top(62.0, 148.0, 1104.0, 318.0, 12, stroke=GRAY, lw=1.2, dash=([3.0, 3.0], 0.0)))
    it19.append(text(74.0, 164.0, 'Cualquier fase del curso depresivo, incluido el primer episodio',
                     'Roboto-Bold', 10.5, GRAY))
    for cx in (226.0, 517.0, 990.0):
        it19.append(line_top(cx, 318.0, cx, 431.0, stroke=INK, lw=1.5, dash=([5.0, 4.0], 0.0)))
        it19.append(arrow_head_down(cx, 441.0))
    k1 = find_text(it19, 'Círculo = estado', startswith=True)
    k2 = find_text(it19, 'bastan para reclasificar', startswith=True)
    for k in sorted((k1, k2), reverse=True):
        del it19[k]
    add_paragraph(it19, 69.0, 694.0,
                  'Círculo = estado o fenómeno observado. Rombo = acto de evaluación. El recuadro discontinuo agrupa '
                  'cualquier fase del curso depresivo, incluido el primer episodio: desde él puede observarse hipomanía, '
                  'manía o características mixtas, sin recurrencias intermedias. Los síntomas mixtos aislados no bastan '
                  'para reclasificar como bipolar. La persistencia puede incluir episodios mayores superpuestos.',
                  1060.0, size=12.0, leading=17.4)
    it19.append(text(51.0, 789.5,
                     'E · Angst et al. (P18): en una cohorte hospitalaria, cada nuevo episodio depresivo conlleva un riesgo '
                     'de manía a lo largo de la vida; aquí se dibuja como camino posible, no como probabilidad.',
                     'Roboto-Medium', 10.0, GRAY))
    # la nota previa sube un poco para dejar sitio
    j = find_text(it19, 'E · Fiedorowicz', startswith=True)
    it19[j]['y'] = Y(776.0)

    # ---- p.22 notas operativas añadidas
    add_paragraph(P[22], 625.0, 445.0,
                  'En la matriz, los síntomas contrapolares del recuento DSM (activación subjetiva, menor necesidad de '
                  'sueño, pensamiento acelerado) figuran como V; la agitación se muestra solo como rasgo descriptivo (N4).',
                  500.0, size=12.0, leading=17.4)
    add_paragraph(P[22], 68.0, 655.0,
                  'Reactividad del ánimo: R en atípica (fila 11, conservada). En melancólica (fila 10) figura como V '
                  'porque el criterio A se cumple con anhedonia generalizada o con ausencia de reactividad (N4).',
                  500.0, size=12.0, leading=17.4)

    # ---- p.23 matiz P04/P05
    k1 = find_text(P[23], 'Judd: síntomas depresivos', startswith=True)
    k2 = find_text(P[23], 'dimensional en 141 pacientes', startswith=True)
    for k in sorted((k1, k2), reverse=True):
        del P[23][k]
    add_paragraph(P[23], 69.0, 663.0,
                  'Judd: síntomas depresivos y subsindrómicos predominan en las cohortes de bipolar I y II (P12–13); '
                  'esto informa sobre tiempo sintomático, no sobre altura de picos. Henry (P05): validación dimensional en '
                  '141 pacientes dentro de un ensayo abierto con olanzapina; describe activación/inhibición como un eje y un '
                  'componente emocional aparte, por lo que no sostiene por sí sola la independencia de depresión y activación '
                  '(P04 sí separa la activación de la valencia emocional). La estructura factorial no calibra este atlas '
                  'ni establece una continuidad causal única.', 1030.0, size=12.0, leading=17.4)

    # ---- p.24 rótulo fuera de la línea base
    j = find_text(P[24], 'remisión posible')
    P[24][j]['y'] = Y(419.0)

    # ---- p.26 método y fuentes
    j = find_text(P[26], 'Se verificaron metadatos', startswith=True)
    P[26][j]['text'] = P[26][j]['text'].replace('17 artículos', '18 artículos')
    urls = [
        'psychiatry.org/psychiatrists/practice/dsm/updates-to-dsm/updates-to-dsm-5-tr-criteria-text',
        'psychiatry.org/getmedia/fd3dfaad-d409-4e94-8605-0350adec5b91/APA-DSM5TR-PersistentDepressive.pdf',
        'who.int/publications/i/item/9789240077263',
        'ncbi.nlm.nih.gov/books/NBK559511/',
        'nice.org.uk/guidance/cg185/chapter/recommendations',
        'veterans.gc.ca/…/entitlement-eligibility-guidelines/az-index/bipolar-and-related-disorders',
    ]
    for n, u in enumerate(urls):
        j = find_text(P[26], 'URL: fuente primaria / documento de criterios (enlace activo)', nth=0)
        P[26][j]['text'] = u + '  ·  corte 28-oct-2026  ·  enlace activo'
    j = find_text(P[26], 'F = criterio formal resumido', startswith=True)
    P[26][j]['text'] = ('F = criterio formal resumido, con alcance de cotejo declarado; E = hallazgo empírico atribuido a su '
                        'fuente; I = interpretación clínica (síntesis editorial); H = hipótesis o propuesta; '
                        'G = geometría editorial no calibrada. Fuente por bloque/página.')

    # ---- p.30 nueva referencia P18
    src_ids = [k for k, it in enumerate(P[30]) if (it['k'] == 'path' and abs(H - bbox(it['ops'])[3] - 245.0) < 1.5
               and abs(bbox(it['ops'])[2] - 1141.0) < 1.5) or
               (it['k'] == 'text' and 240 < H - it['y'] < 350 and it['x'] > 60)]
    dy = -124.0
    clone = [shifted(P[30][k], 0, dy) for k in src_ids]
    for it in clone:
        if it['k'] == 'text':
            t = it['text']
            if t == 'P17':
                it['text'] = 'P18'
            elif t.startswith('An organization'):
                it['text'] = ('Diagnostic conversion from depression to bipolar disorders: results of a long-term '
                              'prospective study of hospital admissions.')
            elif t.startswith('Michael B First'):
                it['text'] = ('Jules Angst, Robert Sellaro, Hans H Stassen et al. Journal of affective disorders. '
                              '2005 Feb;84(2-3):149-57.')
            elif t.startswith('DOI 10.1002'):
                it['text'] = 'DOI 10.1016/S0165-0327(03)00195-2  |  PMID 15708412'
    P[30].extend(clone)
    links.setdefault(30, []).append(([139.0, 492.0 + dy, 1125.0, 589.0 + dy],
                                     'https://pubmed.ncbi.nlm.nih.gov/15708412/'))

    # ---- render
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle('Atlas clínico-geométrico del espectro afectivo | Fernando José Segovia Vera')
    c.setAuthor('Fernando José Segovia Vera')
    c.setSubject('Edición revisada v3 · 28 octubre 2026')
    for n in range(1, 31):
        draw_page(c, P[n])
        for rect, uri in links.get(n, []):
            c.linkURL(uri, tuple(rect), relative=0, thickness=0)
        c.showPage()
    c.save()


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])

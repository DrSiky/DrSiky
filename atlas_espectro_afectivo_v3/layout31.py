"""Biblioteca de maquetación de las páginas nuevas del Atlas v3.1.

Reproduce el estilo del v2/v3: tarjetas blancas con barra de acento, etiquetas
de fuente (P##), cajas de nota (ocre) e informativas (azul), láminas
longitudinales con franjas y umbral esquemático. Coordenadas «top» medidas
desde el borde superior de la página (A3 apaisado, 1191 × 842 pt)."""
import copy
import math

from reportlab.pdfbase import pdfmetrics

import build_v3 as b
from build_v3 import (H, W, NAVY, INK, GRAY, LINE, TEAL, BLUE, RED, WHITE, Y, text, path,
                      rrect_ops, rect_top, line_top, bbox, shifted, find_text, wrap,
                      PANEL, PX0, PX1, STEP, xi, KIND, set_curve, first_curve_index)

BG = (0.956863, 0.945098, 0.913725)
OCHRE = (0.709804, 0.545098, 0.262745)
NOTEFILL = (0.960784, 0.929412, 0.862745)
INFOFILL = (0.894118, 0.933333, 0.952941)
PILLFILL = (0.894118, 0.937255, 0.92549)
PURPLE = (0.47, 0.37, 0.56)
FOOT = 'FERNANDO JOSÉ SEGOVIA VERA  ·  MODELO DEL ATLAS  ·  3 NOV 2026'

PANEL['fun'] = (478.0, 557.0)
PANEL['res'] = (595.0, 674.0)

WARN = []


def sw(s, font, size):
    return pdfmetrics.stringWidth(s, font, size)


# ----------------------------------------------------------------- página base
def new_page(title, right, tag, pageno):
    assert sw(title, 'Roboto-Bold', 30) < 1095, title
    it = [path(rrect_ops(0, 0, W, H, 0), fill=BG),
          path(rrect_ops(0, H - 10, W, H, 0), fill=NAVY),
          text(48, 32, 'ATLAS CLÍNICO-GEOMÉTRICO', 'Roboto-Bold', 10, GRAY),
          text(1143 - sw(right, 'Roboto-Medium', 10), 32, right, 'Roboto-Medium', 10, GRAY),
          text(48, 75, title, 'Roboto-Bold', 30, NAVY),
          line_top(48, 91, 1143, 91, LINE, 1.0),
          text(48, 47.5, tag, 'Roboto-Medium', 9, GRAY),
          line_top(48, 798, 1143, 798, LINE, 1.0),
          text(48, 814, FOOT, 'Roboto-Medium', 9, GRAY)]
    pn = '%02d' % pageno
    it.append(text(1143 - sw(pn, 'Roboto-Bold', 10), 814, pn, 'Roboto-Bold', 10, NAVY))
    assert sw(tag, 'Roboto-Medium', 9) < 1095, tag
    return it


# ----------------------------------------------------------------- tarjetas
def _lines(par_list, font, size, width):
    out = []
    for p in par_list:
        out.append(wrap(p, font, size, width))
    return out


def measure(title, body, width, tsize=14, bsize=12, lead=17.4, gap=5, pill=None, tfont='Roboto-Bold'):
    wtitle = width
    if pill:
        wtitle = width - (sw(pill, 'Roboto-Medium', 10) + 20) - 8
    tl = wrap(title, tfont, tsize, wtitle) if title else []
    pl = _lines(body or [], 'Roboto-Regular', bsize, width)
    h = 26 if not title else 27 + (len(tl) - 1) * (tsize + 4) + 23
    n = sum(len(x) for x in pl)
    h += (n - 1) * lead + gap * (len(pl) - 1) if n else 0
    return h + 16, tl, pl


def card(items, x0, t0, x1, title=None, body=None, t1=None, accent=INK, fill=WHITE, r=10,
         tsize=14, bsize=12, lead=17.4, pad=18, pill=None, gap=5, bcolor=GRAY, where=''):
    width = x1 - x0 - 2 * pad
    h, tl, pl = measure(title, body, width, tsize, bsize, lead, gap, pill)
    if t1 is None:
        t1 = t0 + h
    elif h > (t1 - t0) + 0.5:
        WARN.append('%s: tarjeta «%s» necesita %.0f pt y dispone de %.0f' % (where, (title or '')[:30], h, t1 - t0))
    items.append(rect_top(x0, t0, x1, t1, r, fill=fill, stroke=LINE, lw=1.0))
    if accent:
        items.append(rect_top(x0, t0, x0 + 5, t1, 2, fill=accent))
    base = t0 + 27
    if pill:
        pw = sw(pill, 'Roboto-Medium', 10) + 20
        items.append(rect_top(x1 - 12 - pw, t0 + 12, x1 - 12, t0 + 33, 10, fill=PILLFILL))
        items.append(text(x1 - 12 - pw + 10, t0 + 26.5, pill, 'Roboto-Medium', 10, TEAL))
    if title:
        for n, ln in enumerate(tl):
            items.append(text(x0 + pad, base + n * (tsize + 4), ln, 'Roboto-Bold', tsize, NAVY))
        base = base + (len(tl) - 1) * (tsize + 4) + 23
    else:
        base = t0 + 26
    first = True
    for lines in pl:
        for ln in lines:
            items.append(text(x0 + pad, base, ln, 'Roboto-Regular', bsize, bcolor))
            base += lead
        base += gap - 0
    return t1


def card_height(title, body, x0, x1, pad=18, pill=None, tsize=14, bsize=12, lead=17.4, gap=5):
    return measure(title, body, x1 - x0 - 2 * pad, tsize, bsize, lead, gap, pill)[0]


def card_row(items, specs, t0, xs, where='', **kw):
    """specs: lista de dict(title, body, pill, accent…); xs: lista de (x0,x1). Misma altura."""
    hs = [card_height(s.get('title'), s.get('body'), x0, x1, pill=s.get('pill'),
                      tsize=kw.get('tsize', 14), bsize=kw.get('bsize', 12), lead=kw.get('lead', 17.4))
          for s, (x0, x1) in zip(specs, xs)]
    t1 = t0 + max(hs)
    for s, (x0, x1) in zip(specs, xs):
        args = dict(kw); args.update({k: v for k, v in s.items()})
        card(items, x0, t0, x1, t1=t1, where=where, **args)
    return t1


def note(items, x0, t0, x1, title, body, kind='note', t1=None, where=''):
    fill, acc = (NOTEFILL, OCHRE) if kind == 'note' else (INFOFILL, BLUE)
    return card(items, x0, t0, x1, title=title, body=body, t1=t1, accent=acc, fill=fill, where=where)


# ----------------------------------------------------------------- gráficos
def hbars(items, x0, base0, pitch, rows, vmax, scale, label_w, color=TEAL, lsize=11, vsize=10.5):
    """rows: (etiqueta, valor, texto_valor)."""
    xb = x0 + label_w
    for n, (lab, v, vt) in enumerate(rows):
        yb = base0 + n * pitch
        items.append(text(x0, yb, lab, 'Roboto-Regular', lsize, INK))
        length = v * scale
        items.append(rect_top(xb, yb - 11.5, xb + length, yb + 3, 2, fill=color))
        items.append(text(xb + length + 6, yb, vt, 'Roboto-Medium', vsize, INK))
    items.append(line_top(xb, base0 - 17, xb, base0 + pitch * (len(rows) - 1) + 8, stroke=LINE, lw=1.0))


def forest(items, x0, x1, base0, pitch, rows, lo, hi, ticks, unit='HR', ci=False):
    """Gráfico de bosque en escala logarítmica. rows: (etiqueta, estimador, ic_lo, ic_hi)."""
    def pos(v):
        return x0 + (math.log(v) - math.log(lo)) / (math.log(hi) - math.log(lo)) * (x1 - x0)
    ytop = base0 - 22
    ybot = base0 + pitch * (len(rows) - 1) + 14
    for t in ticks:
        items.append(line_top(pos(t), ytop, pos(t), ybot, stroke=LINE, lw=0.6))
        s = ('%g' % t).replace('.', ',')
        items.append(text(pos(t) - sw(s, 'Roboto-Regular', 9) / 2, ybot + 14, s, 'Roboto-Regular', 9, GRAY))
    items.append(line_top(pos(1.0), ytop, pos(1.0), ybot, stroke=INK, lw=1.2))
    for n, (lab, est, l, h) in enumerate(rows):
        yb = base0 + n * pitch
        items.append(text(x0 - 4 - sw(lab, 'Roboto-Regular', 10.5), yb + 3, lab, 'Roboto-Regular', 10.5, INK))
        items.append(line_top(pos(l), yb, pos(h), yb, stroke=INK, lw=2.0))
        items.append(line_top(pos(l), yb - 4, pos(l), yb + 4, stroke=INK, lw=2.0))
        items.append(line_top(pos(h), yb - 4, pos(h), yb + 4, stroke=INK, lw=2.0))
        cx = pos(est)
        items.append(path(rrect_ops(cx - 4.5, Y(yb + 4.5), cx + 4.5, Y(yb - 4.5), 0), fill=INK, stroke=INK, lw=1.0))
        vs = ('%g' % est).replace('.', ',')
        items.append(text(pos(h) + 8, yb + 3.5, ('%s %s (%s–%s)' % (unit, ('%.2f' % est).replace('.', ','), ('%.2f' % l).replace('.', ','), ('%.2f' % h).replace('.', ',')) if ci else '%s %s' % (unit, vs)), 'Roboto-Medium', 10, INK))


# ----------------------------------------------------------------- láminas
def make_sheet(tpl, *, pageno, title, tag, subtitle, curves, rows, thr=None, markers=(),
               alt=(), notes_in=(), psych=None, extra_foot=''):
    """tpl: lista de primitivas de una lámina del v2 (ya con flechas corregidas).
    curves: dict panel-> lista de 12 valores. rows: [(line_top, label_base, [spans])] con spans
    (a, b, rótulo, tipo[, banda=True]). thr: (v_dep, v_act, rótulo_act)."""
    it = copy.deepcopy(tpl)
    # cabecera/pie
    i = [k for k, x in enumerate(it) if x['k'] == 'text' and x['text'].startswith('Curso 0')][0]
    it[i]['text'] = title
    assert sw(title, 'Roboto-Bold', 30) < 1095
    i = [k for k, x in enumerate(it) if x['k'] == 'text' and x['size'] == 8.0][0]
    it[i]['text'] = tag
    it[i]['size'] = 9.0
    it[i]['y'] = Y(47.5)
    i = [k for k, x in enumerate(it) if x['k'] == 'text' and x['font'] == 'Roboto-Regular' and abs(H - x['y'] - 119) < 3
         and x['size'] >= 12][0]
    it[i]['text'] = subtitle
    for k, x in enumerate(it):
        if x['k'] == 'text' and x['text'].startswith('FERNANDO'):
            x['text'] = FOOT
        if x['k'] == 'text' and abs(H - x['y'] - 814) < 1 and x['font'] == 'Roboto-Bold':
            x['text'] = '%02d' % pageno
            x['x'] = 1143 - sw(x['text'], 'Roboto-Bold', 10)
    # leyenda flotante fuera
    li = find_text(it, 'LEYENDA')
    del it[li:li + 5]
    # curvas
    colmap = {'dep': BLUE, 'act': RED, 'fun': TEAL, 'res': OCHRE}
    for pn, vals in curves.items():
        set_curve(it, colmap[pn], pn, vals)
    # recuadros de psicosis de la plantilla
    if psych is None:
        pass
    else:
        chips = [k for k, x in enumerate(it) if x['k'] == 'text' and x['text'] == 'psicosis']
        rects = []
        for k in chips:
            tx = it[k]['x']
            for j, y in enumerate(it):
                if y['k'] == 'path' and len(y['ops']) == 10 and y['fill'] is not None:
                    bb = bbox(y['ops'])
                    if abs(bb[0] - (tx - 19.0)) < 4 and abs((bb[3] - bb[1]) - 27) < 2:
                        rects.append(j)
        for k in sorted(chips + rects, reverse=True):
            del it[k]
        for (a, bnd) in psych:
            x0, x1 = xi(a), xi(bnd)
            it.append(rect_top(x0, 408, x1, 434, 6, fill=(0.93, 0.91, 0.95), stroke=PURPLE, lw=1.0))
            it.append(text((x0 + x1) / 2 - sw('psicosis', 'Roboto-Medium', 11) / 2, 426, 'psicosis',
                           'Roboto-Medium', 11, PURPLE))
    # franjas
    k0 = first_curve_index(it)
    bands = []
    for (lt, lb, spans) in rows:
        for sp in spans:
            a, bnd, lab, kind = sp[:4]
            band = sp[4] if len(sp) > 4 else True
            if not band:
                continue
            x0 = xi(a)
            x1 = PX1 if bnd > 11.0 else xi(bnd)
            bands.append(rect_top(x0, 166.0, x1, 682.0, fill=KIND[kind], alpha=0.10 if kind != 'neu' else 0.07))
    it[k0:k0] = bands
    # llaves
    for (lt, lb, spans) in rows:
        for sp in spans:
            a, bnd, lab, kind = sp[:4]
            b.bracket(it, a, bnd, lab, kind, lt, lb)
    # umbral
    note2 = 'G · Franjas y llaves: fases ilustrativas, sin calibración.'
    if thr:
        vd, va, lab = thr
        for panel, v, name, base_lbl in (('dep', vd, 'umbral de episodio', 242.0), ('act', va, lab, 359.0)):
            top, base = PANEL[panel]
            yt = base - v * (base - top)
            it.append(line_top(PX0, yt, PX1, yt, stroke=INK, lw=1.0, dash=([5.0, 3.0], 0.0)))
            it.append(line_top(68.0, base_lbl - 3.2, 84.0, base_lbl - 3.2, stroke=INK, lw=1.0, dash=([4.0, 2.5], 0.0)))
            it.append(text(88.0, base_lbl, name, 'Roboto-Regular', 8.0, GRAY))
        note2 += (' Línea discontinua: umbral esquemático de episodio, sin calibración; solo se dibuja '
                  'donde distingue el diagnóstico.')
    # trayectorias alternativas (discontinuas)
    for (panel, start, vals, colr) in alt:
        top, base = PANEL[panel]
        ops = []
        for n, v in enumerate(vals):
            ops.append(('m' if n == 0 else 'l', xi(start + n), Y(base - v * (base - top))))
        it.append(path(ops, stroke=colr, lw=3.0, dash=([6.0, 4.0], 0.0)))
    # marcadores verticales
    for (i, lab) in markers:
        x = xi(i)
        it.append(line_top(x, 166.0, x, 690.0, stroke=INK, lw=1.2, dash=([4.0, 3.0], 0.0)))
        it.append(text(x - sw(lab, 'Roboto-Bold', 9.5) / 2, 702.0, lab, 'Roboto-Bold', 9.5, INK))
    # rótulos dentro del gráfico
    for (x, base_y, s, colr) in notes_in:
        it.append(text(x, base_y, s, 'Roboto-Medium', 9.5, colr))
    if extra_foot:
        note2 += ' ' + extra_foot
    it.append(text(51.0, 787.0, note2, 'Roboto-Medium', 10.0, GRAY))
    return it

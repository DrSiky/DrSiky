"""Atlas clínico-geométrico del espectro afectivo — edición v3.2 (Ampliación III).

Uso:  python3 build_v32.py ATLAS_..._v2.pdf ATLAS_..._v3.pdf ATLAS_..._v3_2.pdf

Parte del PDF v3 (base) y del v2 (plantilla de láminas). Inserta la Ampliación II (pp. 26–41),
la Ampliación III (pp. 42–48) y la guía (p. 49); método en p. 50 y bibliografía P01–P71 en pp. 51–65."""
import re
import sys
import os

import pypdf
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_v3 as b
import replay
from replay import parse_pdf, register_fonts, draw_page, W, H
import layout31 as L
import pages31 as P31
import pages32 as P32
from layout31 import (new_page, text, rect_top, line_top, sw, card, note, FOOT, BG, PILLFILL,
                      NOTEFILL, INFOFILL, OCHRE)
from refs31 import REFS
from refs32 import REFS32

NEW_FIRST, NEW_LAST = 26, 49              # páginas nuevas de contenido (incluida la guía)
SHIFT = NEW_LAST - NEW_FIRST + 1          # 24: desplazamiento de las antiguas 26–30
OLD_METHOD, OLD_BIB = 26, (27, 28, 29, 30)
METHOD = OLD_METHOD + SHIFT               # 50
BIB0 = METHOD + 1                         # 51
NEWBIB0 = BIB0 + len(OLD_BIB)             # 55
TOTAL = 65
FOOT32 = 'FERNANDO JOSÉ SEGOVIA VERA  ·  MODELO DEL ATLAS  ·  13 NOV 2026'

BIB_FOOT = ('Verificación en PubMed: P01–P18, 28-10-2026; P19–P51, 03-11-2026; P52–P71, 13-11-2026. P11 examina DSM-IV; '
            'P25 sin resumen; P33 editorial. Cada entrada enlaza a PubMed.')


def bib_card(items, links, pageno, k, ref):
    pid, title, authors, jr, doi, pmid = ref
    top = 121.0 + 124.0 * k
    items.append(rect_top(51, top, 1141, top + 111, 8, fill=b.WHITE, stroke=b.LINE, lw=1.0))
    items.append(text(67, top + 26, pid, 'Roboto-Bold', 14, b.NAVY))
    tl = b.wrap(title, 'Roboto-Medium', 13, 986)
    assert len(tl) <= 2, title
    for n, ln in enumerate(tl):
        items.append(text(139, top + 25 + 16 * n, ln, 'Roboto-Medium', 13, b.INK))
    off = 16 * (len(tl) - 1)
    items.append(text(139, top + 48 + off, '%s %s' % (authors, jr), 'Roboto-Regular', 10.5, b.GRAY))
    assert sw('%s %s' % (authors, jr), 'Roboto-Regular', 10.5) < 986, pid
    items.append(text(139, top + 96, 'DOI %s  |  PMID %s' % (doi, pmid), 'Roboto-Regular', 10, b.TEAL))
    links.setdefault(pageno, []).append(([139.0, H - (top + 105), 1125.0, H - (top + 8)],
                                         'https://pubmed.ncbi.nlm.nih.gov/%s/' % pmid))


def bib_page(pageno, number, refs, links, tag, closing=False):
    it = new_page('Bibliografía verificada · %d' % number, 'P = PUBLICACIÓN / N = FUENTE NORMATIVA', tag, pageno)
    for k, r in enumerate(refs):
        bib_card(it, links, pageno, k, r)
    if closing:
        top = 121.0 + 124.0 * len(refs) + 8
        note(it, 51, top, 1141, 'Alcance de la verificación ampliada (3 y 13-nov-2026)',
             ['Se leyeron en PubMed los metadatos y resúmenes de P19–P71. Las cifras de las pp. 26–48 proceden de esos resúmenes y no se '
              'han contrastado con los textos completos. P25 (Hamilton, 1960) no tiene resumen disponible y P33 es un editorial; P53, '
              'P64 y P66 son trabajos teóricos o conceptuales. Las afirmaciones DSM-5-TR de la p. 22 siguen sujetas al cotejo con N4.'], kind='info',
             where='bibcierre')
    it.append(text(51, 777, BIB_FOOT, 'Roboto-Medium', 10, b.GRAY))
    return it


def build(v2, v3, out):
    register_fonts()
    L.FOOT = FOOT32
    pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

    base = {i + 1: it for i, it in enumerate(parse_pdf(v3))}
    tpl2 = {i + 1: it for i, it in enumerate(parse_pdf(v2))}
    tpl10 = b.fix_arrows(tpl2[10])
    tpl15 = b.fix_arrows(tpl2[15])

    # enlaces del v3 (renumerados)
    links = {}
    rd = pypdf.PdfReader(v3)
    for i, pg in enumerate(rd.pages):
        n = i + 1
        n = n + SHIFT if n in (OLD_METHOD,) + OLD_BIB else n
        for a in pg.get('/Annots') or []:
            a = a.get_object()
            links.setdefault(n, []).append(([float(v) for v in a['/Rect']], str(a['/A']['/URI'])))

    # ---------------- páginas base: pie con fecha nueva y pagination
    renum = {k: k + SHIFT for k in (OLD_METHOD,) + OLD_BIB}
    pages = {}
    for old, items in base.items():
        new = renum.get(old, old)
        for it in items:
            if it['k'] != 'text':
                continue
            if it['text'].startswith('FERNANDO JOSÉ SEGOVIA VERA'):
                it['text'] = FOOT32
            if abs(H - it['y'] - 814) < 1 and it['font'] == 'Roboto-Bold' and it['text'].isdigit():
                it['text'] = '%02d' % new
            it['text'] = re.sub(r'p\. (2[6-9]|30)\b', lambda m: 'p. %d' % (int(m.group(1)) + SHIFT), it['text'])
        pages[new] = items

    # portada
    b.replace_text(pages[1], 'Modelo del atlas · edición revisada v3 · 28 octubre 2026',
                   'Modelo del atlas · edición revisada y ampliada v3.2 · 13 noviembre 2026')

    # ---------------- índice (p. 2)
    it2 = pages[2]
    drop = []
    for k, it in enumerate(it2):
        if it['k'] == 'text' and 340 < H - it['y'] < 670 and it['font'] in ('Roboto-Bold', 'Roboto-Medium') and it['size'] in (17.0, 18.0):
            drop.append(k)
        if it['k'] == 'path' and it['lw'] == 0.7:
            drop.append(k)
    for k in sorted(drop, reverse=True):
        del it2[k]
    rows = [('04–07', 'Matriz fenomenológica · 24 perfiles × 21 variables'),
            ('08–09', 'Cartografía de dimensiones y proyecciones'),
            ('10–18', 'Nueve láminas longitudinales; cursos 10–14 en pp. 24, 33–35 y 43'),
            ('19–20', 'Transiciones, moduladores y fármacos'),
            ('21', 'Auditoría crítica de originales'),
            ('22–25', 'Ampliación clínica I: precisiones, espectro, curso inducido y psicosis'),
            ('26–41', 'Ampliación II: evaluación, riesgo, mixticidad, tratamiento, periparto, sustancias'),
            ('42–49', 'Ampliación III: pródromos, residuo, polaridad, vivencia, minorías, psicosis cicloide; guía'),
            ('50–65', 'Método, fuentes normativas y bibliografía verificada')]
    for n, (num, ttl) in enumerate(rows):
        bs = 359.0 + 45.0 * n
        it2.append(text(54.0, bs, num, 'Roboto-Bold', 18, b.TEAL))
        it2.append(text(160.0, bs, ttl, 'Roboto-Medium', 17, b.NAVY))
        it2.append(line_top(51.0, bs + 23.0, 1140.0, bs + 23.0, stroke=b.LINE, lw=0.7))
    k = b.find_text(it2, 'Clave epistemológica', startswith=True)
    it2[k]['y'] = b.Y(766.0)

    # ---------------- pies de enlace desde páginas antiguas hacia la ampliación
    def foot2(n, s):
        pages[n].append(text(51.0, 789.5, s, 'Roboto-Medium', 10, b.GRAY))
    foot2(20, 'Ampliación: riesgo suicida p. 28 · antidepresivos y viraje p. 31 · periparto pp. 32–33 · causas médicas y sustancias pp. 36–37.')
    foot2(24, 'Ampliación: antidepresivos y viraje p. 31 · lámina 13 (activación asociada al tratamiento) p. 35 · sustancias emergentes p. 37.')
    foot2(25, 'Ampliación: periparto pp. 32–33 · diferenciales p. 38 · vivencia y tiempo vivido p. 46 · psicosis cicloide p. 48.')

    # ---------------- método (antigua p. 26 → 50)
    m = pages[METHOD]
    i = b.find_text(m, 'CORTE: 28 OCTUBRE 2026')
    m[i]['text'] = 'CORTE: 13 NOVIEMBRE 2026'
    m[i]['x'] = 1143 - sw(m[i]['text'], 'Roboto-Medium', 10)
    i = b.find_text(m, 'Se verificaron metadatos', startswith=True)
    m[i]['text'] = m[i]['text'].replace('18 artículos', '71 artículos')
    m.append(text(69.0, 203.8, 'Las cifras de las pp. 26–48 se toman de los resúmenes de PubMed (P19–P51, 3-nov-2026; P52–P71, 13-nov-2026); '
                  'P25 no tiene resumen y P33 es un editorial.', 'Roboto-Regular', 12, b.GRAY))

    # ---------------- bibliografía: antigua p. 30 recibe P19 y P20
    PB = BIB0 + 3
    p47 = pages[PB]
    j = b.find_text(p47, 'Verificación en PubMed', startswith=True)
    p47[j]['text'] = BIB_FOOT
    # P16–P18 ya están (k = 0, 1, 2); P19 y P20 ocupan k = 3, 4
    bib_card(p47, links, PB, 3, REFS[0])
    bib_card(p47, links, PB, 4, REFS[1])

    # ---------------- páginas nuevas 26–42
    new = {}
    for off, fn in enumerate(P31.NEW_PAGES[:-1] + P32.NEW_PAGES32 + [P32.guide]):
        n = NEW_FIRST + off
        if fn == 'p33':
            new[n] = P31.p33(tpl15)
        elif fn == 'p34':
            new[n] = P31.p34(tpl10)
        elif fn == 'p35':
            new[n] = P31.p35(tpl10)
        elif fn == 'p43':
            new[n] = P32.p43(tpl10)
        else:
            new[n] = fn()
    # ---------------- bibliografía nueva 48–54 (P21–P51)
    rest = REFS[2:] + REFS32
    tag_src = next(it['text'] for it in base[27] if it['k'] == 'text' and it['text'].startswith('F criterio formal'))
    chunks = [rest[k:k + 5] for k in range(0, len(rest), 5)]
    for c, chunk in enumerate(chunks):
        n = NEWBIB0 + c
        new[n] = bib_page(n, 5 + c, chunk, links, tag_src, closing=(c == len(chunks) - 1 and len(chunk) < 5))
    assert NEWBIB0 + len(chunks) - 1 == TOTAL, (NEWBIB0 + len(chunks) - 1, TOTAL)
    pages.update(new)

    # ---------------- render
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle('Atlas clínico-geométrico del espectro afectivo | Fernando José Segovia Vera')
    c.setAuthor('Fernando José Segovia Vera')
    c.setSubject('Edición revisada y ampliada v3.2 · 13 noviembre 2026')
    for n in range(1, TOTAL + 1):
        draw_page(c, pages[n])
        for rect, uri in links.get(n, []):
            c.linkURL(uri, tuple(rect), relative=0, thickness=0)
        c.showPage()
    c.save()
    for w in L.WARN:
        print('AVISO:', w)


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2], sys.argv[3])

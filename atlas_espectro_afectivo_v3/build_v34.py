"""Atlas clínico-geométrico del espectro afectivo — edición v3.4 (Ampliación V: farmacología).

Uso:  python3 build_v34.py ATLAS_..._v2.pdf ATLAS_..._v3.pdf ATLAS_..._v3_4.pdf

Parte del PDF v3 (base) y del v2 (plantilla de láminas). Inserta las Ampliaciones II (pp. 26–41),
III (pp. 42–48) y IV (pp. 49–55), V (pp. 56–71, farmacología de 15 fármacos a partir de los dosieres D01–D13) y la
guía (p. 72); método en p. 73, bibliografía P01–P91 en pp. 74–92 y dosieres en pp. 93–95."""
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
import pages33 as P33
import pages34 as P34
from layout31 import (new_page, text, rect_top, line_top, sw, card, note, FOOT, BG, PILLFILL,
                      NOTEFILL, INFOFILL, OCHRE)
from refs31 import REFS
from refs32 import REFS32
from refs33 import REFS33
from refs34 import REFS34, DOSSIERS

NEW_FIRST, NEW_LAST = 26, 72              # páginas nuevas de contenido (incluida la guía)
SHIFT = NEW_LAST - NEW_FIRST + 1          # 47: desplazamiento de las antiguas 26–30
OLD_METHOD, OLD_BIB = 26, (27, 28, 29, 30)
METHOD = OLD_METHOD + SHIFT               # 73
BIB0 = METHOD + 1                         # 74
NEWBIB0 = BIB0 + len(OLD_BIB)             # 78
DOSS0 = 93
TOTAL = 95
FOOT32 = 'FERNANDO JOSÉ SEGOVIA VERA  ·  MODELO DEL ATLAS  ·  18 NOV 2026'

BIB_FOOT = ('Verificación en PubMed: P01–P18, 28-10-2026; P19–P51, 03-11-2026; P52–P71, 13-11-2026; P72–P82, 15-11; P83–P91, 18-11-2026. '
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
        note(it, 51, top, 1141, 'Alcance de la verificación ampliada (3, 13, 15 y 18-nov-2026)',
             ['Se leyeron en PubMed los metadatos y resúmenes de P19–P91. Las cifras de las pp. 26–71 que citan P## proceden de esos resúmenes y no se '
              'han contrastado con los textos completos. P25 (Hamilton, 1960) no tiene resumen disponible y P33 es un editorial; P53, '
              'P64, P66, P75–P77, P81 y P82 son trabajos teóricos o propuestas; P85 está financiado por un fabricante. Las cifras marcadas D## proceden de los dosieres (pp. 93–95). Las afirmaciones DSM-5-TR de la p. 22 siguen sujetas al cotejo con N4.'], kind='info',
             where='bibcierre')
    it.append(text(51, 777, BIB_FOOT, 'Roboto-Medium', 10, b.GRAY))
    return it


def dossier_page(pageno, number, items, tag, last=False):
    it = new_page('Dosieres monográficos · %d' % number, 'D = DOSIER DEL ATLAS GLÍFICO', tag, pageno)
    for k, (did, drug, nl, title) in enumerate(items):
        top = 121.0 + 124.0 * k
        it.append(rect_top(51, top, 1141, top + 111, 8, fill=b.WHITE, stroke=b.LINE, lw=1.0))
        it.append(text(67, top + 26, did, 'Roboto-Bold', 14, b.NAVY))
        it.append(text(139, top + 25, drug, 'Roboto-Medium', 13, b.INK))
        it.append(text(139, top + 48, title + '.', 'Roboto-Regular', 10.5, b.GRAY))
        it.append(text(139, top + 96, 'Atlas Glífico · monoterapias bipolares · v1.0 · noviembre 2026 · %d láminas · fuente aportada por el autor'
                       % nl, 'Roboto-Regular', 10, b.TEAL))
    if last:
        top = 121.0 + 124.0 * len(items) + 8
        note(it, 51, top, 1141, 'Cómo se citan los dosieres',
             ['Las páginas 56–71 citan cada dato como D## seguido, entre corchetes, del código de fuente primaria del dosier (R ficha '
              'técnica CIMA/FDA, G guía, T/L ensayo, E síntesis, P farmacología, S seguridad). Las fuentes primarias de los dosieres no se '
              'han verificado de nuevo en esta edición, salvo las síntesis transversales P83–P91. Varias curvas de los dosieres son '
              'redibujos aproximados de figuras publicadas, como indican sus propias láminas.'], kind='info', where='dosscierre')
    it.append(text(51, 777, 'Dosieres monográficos aportados por el autor del atlas (10–18 nov 2026). No son publicaciones indexadas; '
                   'su contenido se cita con su código interno.', 'Roboto-Medium', 10, b.GRAY))
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
                   'Modelo del atlas · edición revisada y ampliada v3.4 · 18 noviembre 2026')

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
            ('42–48', 'Ampliación III: pródromos, residuo, polaridad, vivencia, minorías, psicosis cicloide'),
            ('49–55', 'Ampliación IV: nosología dimensional, ACE, espectro, HiTOP, RDoC, estadios'),
            ('56–72', 'Ampliación V: farmacología de 15 fármacos por fase, seguridad y fichas; guía'),
            ('73–95', 'Método, fuentes normativas, bibliografía verificada y dosieres')]
    for n, (num, ttl) in enumerate(rows):
        bs = 359.0 + 38.0 * n
        it2.append(text(54.0, bs, num, 'Roboto-Bold', 18, b.TEAL))
        it2.append(text(160.0, bs, ttl, 'Roboto-Medium', 17, b.NAVY))
        it2.append(line_top(51.0, bs + 23.0, 1140.0, bs + 23.0, stroke=b.LINE, lw=0.7))
    k = b.find_text(it2, 'Clave epistemológica', startswith=True)
    it2[k]['y'] = b.Y(783.0)

    # ---------------- pies de enlace desde páginas antiguas hacia la ampliación
    def foot2(n, s):
        pages[n].append(text(51.0, 789.5, s, 'Roboto-Medium', 10, b.GRAY))
    foot2(20, 'Ampliación: riesgo p. 28 · antidepresivos p. 31 · periparto pp. 32–33 · sustancias pp. 36–37 · farmacología por fase y fármaco pp. 56–71.')
    foot2(24, 'Ampliación: antidepresivos y viraje p. 31 · lámina 13 (activación asociada al tratamiento) p. 35 · sustancias emergentes p. 37.')
    foot2(7, 'Ampliación: mixticidad según definiciones p. 29 · estados mixtos en el modelo ACE pp. 50–51.')
    foot2(9, 'Ampliación: categorías y dimensiones p. 49 · modelo ACE p. 50 · HiTOP y factor p, p. 53 · mapa de modelos p. 55.')
    foot2(25, 'Ampliación: periparto pp. 32–33 · diferenciales p. 38 · vivencia y tiempo vivido p. 46 · psicosis cicloide p. 48.')

    # ---------------- método (antigua p. 26 → 50)
    m = pages[METHOD]
    i = b.find_text(m, 'CORTE: 28 OCTUBRE 2026')
    m[i]['text'] = 'CORTE: 18 NOVIEMBRE 2026'
    m[i]['x'] = 1143 - sw(m[i]['text'], 'Roboto-Medium', 10)
    i = b.find_text(m, 'Se verificaron metadatos', startswith=True)
    m[i]['text'] = m[i]['text'].replace('18 artículos', '91 artículos')
    m.append(text(69.0, 203.8, 'Las cifras P## de las pp. 26–71 proceden de resúmenes de PubMed (P19–P91, 3–18 nov 2026); las cifras D## de las pp. 56–71, '
                  'de los dosieres D01–D13 (pp. 93–95).', 'Roboto-Regular', 12, b.GRAY))

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
    for off, fn in enumerate(P31.NEW_PAGES[:-1] + P32.NEW_PAGES32 + P33.NEW_PAGES33 + P34.NEW_PAGES34 + ['guide']):
        n = NEW_FIRST + off
        if fn == 'p33':
            new[n] = P31.p33(tpl15)
        elif fn == 'p34':
            new[n] = P31.p34(tpl10)
        elif fn == 'p35':
            new[n] = P31.p35(tpl10)
        elif fn == 'p43':
            new[n] = P32.p43(tpl10)
        elif fn == 'p62':
            new[n] = P34.p62(tpl10)
        elif fn == 'guide':
            new[n] = P32.guide(n, extra=[('¿Cómo se describiría el caso en clave dimensional: dominios ACE, espectro, estadio?', ['p. 49', 'pp. 50–52', 'pp. 53–55']),
                                         ('¿Qué fármaco, para qué fase y polo, con qué vigilancia?', ['p. 56', 'pp. 58–61', 'pp. 66–68', 'pp. 69–70'])], word='Dieciséis')
        else:
            new[n] = fn()
    # ---------------- bibliografía nueva 48–54 (P21–P51)
    rest = REFS[2:] + REFS32 + REFS33 + REFS34
    tag_src = next(it['text'] for it in base[27] if it['k'] == 'text' and it['text'].startswith('F criterio formal'))
    chunks = [rest[k:k + 5] for k in range(0, len(rest), 5)]
    for c, chunk in enumerate(chunks):
        n = NEWBIB0 + c
        new[n] = bib_page(n, 5 + c, chunk, links, tag_src, closing=(c == len(chunks) - 1 and len(chunk) < 5))
    assert NEWBIB0 + len(chunks) - 1 == DOSS0 - 1, (NEWBIB0 + len(chunks) - 1, DOSS0)
    dch = [DOSSIERS[k:k + 5] for k in range(0, len(DOSSIERS), 5)]
    for c, chunk in enumerate(dch):
        new[DOSS0 + c] = dossier_page(DOSS0 + c, c + 1, chunk, tag_src, last=(c == len(dch) - 1))
    assert DOSS0 + len(dch) - 1 == TOTAL
    pages.update(new)

    # ---------------- render
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle('Atlas clínico-geométrico del espectro afectivo | Fernando José Segovia Vera')
    c.setAuthor('Fernando José Segovia Vera')
    c.setSubject('Edición revisada y ampliada v3.4 · 18 noviembre 2026')
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

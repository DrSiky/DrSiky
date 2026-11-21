"""Atlas clínico-geométrico del espectro afectivo — edición v3.9 (textos completos: curso semanal, recaída, dinámica mixta, estadiaje MNF, genómica).

Uso:  python3 build_v39.py ATLAS_..._v2.pdf ATLAS_..._v3.pdf ATLAS_..._v3_9.pdf

Parte del PDF v3 (base) y del v2 (plantilla de láminas). Inserta las Ampliaciones II (pp. 26–41),
III (pp. 42–48) y IV (pp. 49–55), V (pp. 56–71), VI (pp. 72–79), láminas de curso farmacológico (pp. 80–88), VII (pp. 89–102), VIII (pp. 103–112), IX (pp. 113–124) y la guía (p. 125);
método, bibliografía P01–P192 y dosieres a continuación (numeración calculada)."""
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
import pages35 as P35
import pages36 as P36
import pages37 as P37
import pages38 as P38
import pages39 as P39
from layout31 import (new_page, text, rect_top, line_top, sw, card, note, FOOT, BG, PILLFILL,
                      NOTEFILL, INFOFILL, OCHRE)
from refs31 import REFS
from refs32 import REFS32
from refs33 import REFS33
from refs34 import REFS34, DOSSIERS
from refs37 import REFS37
from refs38 import REFS38
from refs39 import REFS39

NEW_FIRST, NEW_LAST = 26, 125              # páginas nuevas de contenido (incluida la guía)
SHIFT = NEW_LAST - NEW_FIRST + 1          # 64: desplazamiento de las antiguas 26–30
OLD_METHOD, OLD_BIB = 26, (27, 28, 29, 30)
METHOD = OLD_METHOD + SHIFT               # 90
BIB0 = METHOD + 1                         # 91
NEWBIB0 = BIB0 + len(OLD_BIB)             # 95
_NREST = len(REFS) - 2 + len(REFS32) + len(REFS33) + len(REFS34) + len(REFS37) + len(REFS38) + len(REFS39)
DOSS0 = NEWBIB0 + (_NREST + 4) // 5
TOTAL = DOSS0 + (len(DOSSIERS) + 4) // 5 - 1
FOOT32 = 'FERNANDO JOSÉ SEGOVIA VERA  ·  MODELO DEL ATLAS  ·  21 NOV 2026'

BIB_FOOT = ('Verificación en PubMed: P01–P18, 28-10-2026; P19–P111, del 3 al 19-11-2026; P112–P177, 20-11; P178–P192, 21-11-2026. '
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
        note(it, 51, top, 1141, 'Alcance de la verificación ampliada (3, 13, 15 y 18–21-nov-2026)',
             ['Se leyeron en PubMed los metadatos y resúmenes de P19–P192. Las cifras de las pp. 26–112 que citan P## proceden de esos resúmenes; las de las pp. 113–124, de '
              'los textos completos aportados por el autor. P25 (Hamilton, 1960) no tiene resumen disponible y P33 es un editorial; P53, '
              'P64, P66, P75–P77, P81 y P82 son trabajos teóricos o propuestas; P85 está financiado por un fabricante; P111 es transversal; P132, P140, P150, P154 y P158 carecen de resumen. Las cifras marcadas D## proceden de los dosieres (pp. ' + '%d–%d' % (DOSS0, TOTAL) + '); los NNT de las pp. 74–75 son cálculos brutos del atlas. Las afirmaciones DSM-5-TR de la p. 22 siguen sujetas al cotejo con N4.'], kind='info',
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
                   'Modelo del atlas · edición revisada y ampliada v3.9 · 21 noviembre 2026')

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
            ('10–18', 'Nueve láminas longitudinales; cursos 10–27 en pp. 24, 33–35, 43, 62, 78, 81–88, 93–94 y 97'),
            ('19–20', 'Transiciones, moduladores y fármacos'),
            ('21', 'Auditoría crítica de originales'),
            ('22–25', 'Ampliación clínica I: precisiones, espectro, curso inducido y psicosis'),
            ('26–41', 'Ampliación II: evaluación, riesgo, mixticidad, tratamiento, periparto, sustancias'),
            ('42–48', 'Ampliación III: pródromos, residuo, polaridad, vivencia, minorías, psicosis cicloide'),
            ('49–55', 'Ampliación IV: nosología dimensional, ACE, espectro, HiTOP, RDoC, estadios'),
            ('56–71', 'Ampliación V: farmacología de 15 fármacos por fase, seguridad y fichas'),
            ('72–79', 'Ampliación VI: guías, titulación, NNT, recaída, polaridad, metabolismo'),
            ('80–88', 'Láminas de curso farmacológico 15–24 (índice y cursos 17–24)'),
            ('89–102', 'Ampliación VII: poblaciones especiales, resistencia, suicidio y litio, genética'),
            ('103–112', 'Ampliación VIII: corpus del autor (mixticidad, espectro, esquizoafectivo, neurobiología)'),
            ('113–125', 'Ampliación IX: textos completos (curso semanal, recaída, dinámica mixta, estadios MNF, genómica); guía'),
            ('%d–%d' % (METHOD, TOTAL), 'Método, fuentes normativas, bibliografía verificada y dosieres')]
    for n, (num, ttl) in enumerate(rows):
        bs = 356.0 + 25.9 * n
        it2.append(text(54.0, bs, num, 'Roboto-Bold', 17, b.TEAL))
        it2.append(text(160.0, bs, ttl, 'Roboto-Medium', 16, b.NAVY))
        it2.append(line_top(51.0, bs + 8.0, 1140.0, bs + 8.0, stroke=b.LINE, lw=0.7))
    k = b.find_text(it2, 'Clave epistemológica', startswith=True)
    it2[k]['y'] = b.Y(783.0)

    # ---------------- pies de enlace desde páginas antiguas hacia la ampliación
    def foot2(n, s):
        pages[n].append(text(51.0, 789.5, s, 'Roboto-Medium', 10, b.GRAY))
    foot2(20, 'Ampliación: riesgo p. 28 · antidepresivos p. 31 · periparto pp. 32–33 · sustancias pp. 36–37 · farmacología pp. 56–79 · láminas pp. 80–88 · poblaciones a genética pp. 89–102 · corpus pp. 103–112 · textos completos pp. 113–124.')
    foot2(24, 'Ampliación: antidepresivos y viraje p. 31 · lámina 13 (activación asociada al tratamiento) p. 35 · sustancias emergentes p. 37.')
    foot2(7, 'Ampliación: mixticidad según definiciones p. 29 · estados mixtos en el modelo ACE pp. 50–51.')
    foot2(9, 'Ampliación: categorías y dimensiones p. 49 · modelo ACE p. 50 · HiTOP y factor p, p. 53 · mapa de modelos p. 55.')
    foot2(25, 'Ampliación: periparto pp. 32–33 · diferenciales p. 38 · vivencia y tiempo vivido p. 46 · psicosis cicloide p. 48.')

    # ---------------- método (antigua p. 26 → 50)
    m = pages[METHOD]
    i = b.find_text(m, 'CORTE: 28 OCTUBRE 2026')
    m[i]['text'] = 'CORTE: 21 NOVIEMBRE 2026'
    m[i]['x'] = 1143 - sw(m[i]['text'], 'Roboto-Medium', 10)
    i = b.find_text(m, 'Se verificaron metadatos', startswith=True)
    m[i]['text'] = m[i]['text'].replace('18 artículos', '192 artículos')
    m.append(text(69.0, 203.8, 'Cifras P## de las pp. 26–112: resúmenes de PubMed. Pp. 113–124: textos completos (21 nov 2026). Cifras D##: dosieres D01–D13 (pp. %d–%d).' % (DOSS0, TOTAL), 'Roboto-Regular', 12, b.GRAY))

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
    for off, fn in enumerate(P31.NEW_PAGES[:-1] + P32.NEW_PAGES32 + P33.NEW_PAGES33 + P34.NEW_PAGES34 + P35.NEW_PAGES35 + P36.NEW_PAGES36 + P37.NEW_PAGES37 + P38.NEW_PAGES38 + P39.NEW_PAGES39 + ['guide']):
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
        elif fn == 'p78':
            new[n] = P35.p78(tpl10)
        elif isinstance(fn, str) and fn.startswith('s'):
            new[n] = P37.sheet37(int(fn[1:]), tpl10, n)
        elif isinstance(fn, str) and fn.startswith('c'):
            new[n] = P36.sheet(int(fn[1:]), tpl10, n)
        elif fn == 'guide':
            new[n] = P32.guide(n, extra=[('¿Cómo se describiría el caso en clave dimensional: dominios ACE, espectro, estadio?', ['p. 49', 'pp. 50–52', 'pp. 53–55']),
                                         ('¿Qué fármaco, para qué fase y polo, con qué vigilancia?', ['p. 56', 'pp. 58–61', 'pp. 72–79', 'pp. 80–88']),
                                         ('¿Qué edad o estado especial, qué resistencia, qué riesgo suicida, qué base genética?', ['pp. 89–94', 'pp. 95–97', 'pp. 98–99', 'pp. 100–102']),
                                         ('¿Qué añade el corpus propio sobre mixticidad, espectro, esquizoafectivo y neurobiología?', ['pp. 103–105', 'pp. 106–107', 'pp. 108–109', 'pp. 110–112']),
                                         ('¿Qué precisan los textos completos sobre curso, recaída, dinámica mixta, estadios y genómica?', ['pp. 113–117', 'pp. 118–120', 'pp. 121–122', 'pp. 123–124'])], word='Diecinueve')
        else:
            new[n] = fn()
    # ---------------- bibliografía nueva 48–54 (P21–P51)
    rest = REFS[2:] + REFS32 + REFS33 + REFS34 + REFS37 + REFS38 + REFS39
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
    c.setSubject('Edición revisada y ampliada v3.9 · 21 noviembre 2026')
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

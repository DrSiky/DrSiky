"""Lee un PDF generado con ReportLab (el Atlas v2) y lo convierte en una lista
de primitivas editables (rutas y textos) por página, y las vuelve a dibujar.

Fuente de partida: el PDF v2 entregado; no se conserva ningún otro original."""
import re
import pypdf
from pypdf.generic import ContentStream
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color
from reportlab.pdfgen.pathobject import PDFPathObject

FONT_DIR = '/usr/share/fonts/truetype/roboto/unhinted/RobotoTTF/'
FONT_FILES = {
    'Roboto-Light': 'Roboto-Light.ttf',
    'Roboto-Regular': 'Roboto-Regular.ttf',
    'Roboto-Medium': 'Roboto-Medium.ttf',
    'Roboto-Bold': 'Roboto-Bold.ttf',
}
W, H = 1191, 842


def register_fonts():
    for name, fn in FONT_FILES.items():
        pdfmetrics.registerFont(TTFont(name, FONT_DIR + fn))


def _tounicode(font_obj):
    tu = font_obj['/ToUnicode'].get_object().get_data().decode('latin1')
    m = {}
    for code, uni in re.findall(r'<([0-9A-Fa-f]{2})>\s*<([0-9A-Fa-f]{4})>', tu):
        m[int(code, 16)] = chr(int(uni, 16))
    return m


def parse_pdf(path):
    r = pypdf.PdfReader(path)
    pages = []
    for page in r.pages:
        res = page['/Resources']
        fonts = {}
        for k, v in res['/Font'].items():
            fo = v.get_object()
            base = str(fo['/BaseFont']).split('+')[-1].lstrip('/')
            fonts[k] = (base, _tounicode(fo) if '/ToUnicode' in fo else None)
        gstates = {}
        if '/ExtGState' in res:
            for k, v in res['/ExtGState'].items():
                gstates[k] = float(v.get_object().get('/ca', 1))
        cs = ContentStream(page.get_contents(), r)
        items = []
        fill = (0, 0, 0)
        stroke = (0, 0, 0)
        lw = 1.0
        dash = None
        alpha = 1.0
        path = []
        font = None
        size = 12
        tm = (0, 0)
        gstack = []
        for operands, op in cs.operations:
            op = op.decode() if isinstance(op, bytes) else op
            if op == 'q':
                gstack.append((fill, stroke, lw, dash, alpha, font, size))
            elif op == 'Q':
                if gstack:
                    fill, stroke, lw, dash, alpha, font, size = gstack.pop()
            elif op == 'rg':
                fill = tuple(float(x) for x in operands)
            elif op == 'RG':
                stroke = tuple(float(x) for x in operands)
            elif op == 'w':
                lw = float(operands[0])
            elif op == 'd':
                arr = [float(x) for x in operands[0]]
                dash = (arr, float(operands[1])) if arr else None
            elif op == 'gs':
                alpha = gstates[str(operands[0])]
            elif op == 'n':
                path = []
            elif op in ('m', 'l', 'c'):
                path.append((op,) + tuple(float(x) for x in operands))
            elif op == 're':
                x, y, w, h = [float(v) for v in operands]
                path += [('m', x, y), ('l', x + w, y), ('l', x + w, y + h), ('l', x, y + h), ('h',)]
            elif op == 'h':
                path.append(('h',))
            elif op in ('f*', 'f', 'B*', 'B', 'S', 'b', 's'):
                items.append({
                    'k': 'path', 'ops': path,
                    'fill': fill if op in ('f*', 'f', 'B*', 'B', 'b') else None,
                    'stroke': stroke if op in ('B*', 'B', 'S', 'b', 's') else None,
                    'lw': lw, 'dash': dash, 'alpha': alpha,
                    'eo': op.endswith('*')})
                path = []
            elif op == 'Tf':
                font = fonts[str(operands[0])]
                size = float(operands[1])
            elif op == 'Tm':
                tm = (float(operands[4]), float(operands[5]))
            elif op == 'Tj':
                raw = operands[0]
                if hasattr(raw, 'original_bytes'):
                    raw = raw.original_bytes
                elif isinstance(raw, str):
                    raw = raw.encode('latin1')
                cmap = font[1]
                txt = ''.join(cmap.get(b, '?') for b in raw)
                items.append({'k': 'text', 'x': tm[0], 'y': tm[1], 'font': font[0],
                              'size': size, 'fill': fill, 'alpha': alpha, 'text': txt})
            elif op in ('cm',):
                assert [float(x) for x in operands] == [1, 0, 0, 1, 0, 0], operands
        pages.append(items)
    return pages


def draw_page(c, items):
    for it in items:
        if it['k'] == 'path':
            p = c.beginPath()
            for o in it['ops']:
                if o[0] == 'm':
                    p.moveTo(o[1], o[2])
                elif o[0] == 'l':
                    p.lineTo(o[1], o[2])
                elif o[0] == 'c':
                    p.curveTo(*o[1:])
                elif o[0] == 'h':
                    p.close()
            if it['fill'] is not None:
                c.setFillColorRGB(*it['fill'])
            if it['stroke'] is not None:
                c.setStrokeColorRGB(*it['stroke'])
            c.setLineWidth(it['lw'])
            if it['dash']:
                c.setDash(it['dash'][0], it['dash'][1])
            else:
                c.setDash([], 0)
            c.setFillAlpha(it['alpha'])
            c.setStrokeAlpha(1)
            c.drawPath(p, stroke=1 if it['stroke'] is not None else 0,
                       fill=1 if it['fill'] is not None else 0,
                       fillMode=0 if it['eo'] else 1)
            c.setDash([], 0)
            c.setFillAlpha(1)
            c.setStrokeAlpha(1)
        else:
            c.setFillColorRGB(*it['fill'])
            c.setFillAlpha(it.get('alpha', 1))
            c.setFont(it['font'], it['size'])
            c.drawString(it['x'], it['y'], it['text'])
            c.setFillAlpha(1)


def render(pages, out, title, author, subject=None):
    register_fonts()
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle(title)
    c.setAuthor(author)
    if subject:
        c.setSubject(subject)
    for items in pages:
        draw_page(c, items)
        c.showPage()
    c.save()


if __name__ == '__main__':
    import sys
    pg = parse_pdf(sys.argv[1])
    render(pg, sys.argv[2], 'Replay', 'x')

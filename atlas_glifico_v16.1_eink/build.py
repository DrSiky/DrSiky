"""Construye ATLAS_GLIFICO_VISUAL_v16.1_eink.html a partir de ATLAS_GLIFICO_VISUAL_v16.0.html.

Uso:  python3 build.py RUTA/ATLAS_GLIFICO_VISUAL_v16.0.html [SALIDA.html]
La v16.0 original no se modifica. Cada ancla debe ser única; si no, el script se detiene.
"""
import pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
if len(sys.argv) < 2:
    sys.exit(__doc__)
SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent / 'ATLAS_GLIFICO_VISUAL_v16.1_eink.html'
t = SRC.read_text(encoding='utf8')

def rep(old, new, count=1):
    global t
    n = t.count(old)
    assert n == count, ('Ancla no única o ausente', n, old[:90])
    t = t.replace(old, new)

css = ''.join((HERE / f).read_text(encoding='utf8') + '\n' for f in ('theme.css', 'newviews.css', 'v161.css'))
js = ''.join((HERE / f).read_text(encoding='utf8') + '\n' for f in ('v160.js', 'v161.js'))
rep('<title>ATLAS GLÍFICO · Atlas visual v16.0</title>', '<title>ATLAS GLÍFICO · Atlas visual v16.1 · edición e-ink</title>')
rep('<h1>ATLAS GLÍFICO · Atlas visual v16.0</h1>', '<h1>ATLAS GLÍFICO · Atlas visual v16.1 <span class="eink-tag">· edición e-ink</span></h1>')
rep("atlasVersion:'16.0'", "atlasVersion:'16.1'")
rep('Mapas clínicos, receptoroma y PK/PD; contexto del paciente y fuentes de cada señal.',
    'Mapas clínicos, receptoroma, PK/PD, red farmacodinámica y vectores clínicos; contexto del paciente y fuentes de cada señal.')
assert t.count('</head>') == 1
t = t.replace('</head>', '<style id="eink-theme">\n' + css + '\n</style></head>')
rep('</nav>\n<details class="tool-drawer"',
    '<button data-view="pdnet" data-tier="atlas"><span class="atlas-icon">PD</span><b>Red farmacodinámica</b><small>fármacos, dianas, convergencias y competencias</small></button>'
    '<button data-view="vectors" data-tier="atlas"><span class="atlas-icon">V</span><b>Vectores clínicos</b><small>áreas de los cuatro componentes por fármaco</small></button>'
    '</nav>\n<details class="tool-drawer"')
rep('<section class="view screen" id="report">',
    '<section class="view screen" id="pdnet"></section><section class="view screen" id="vectors"></section><section class="view screen" id="report">')
rep("const ATLAS_VIEWS=new Set(['fount','receptor','pk'])", "const ATLAS_VIEWS=new Set(['fount','receptor','pk','pdnet','vectors'])")
anchor = "$$('[data-view]').forEach(b=>b.onclick=()=>activateView(b.dataset.view));addEventListener('resize',renderAtlasContext);"
rep(anchor, js + '\n' + anchor)
OUT.write_text(t, encoding='utf8')
print(OUT, len(t), 'bytes')

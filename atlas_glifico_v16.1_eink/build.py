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

# --- capa O: política anti/pro de H1, α1 y M1 (v16.1) -------------------------------------------
OLD_VP = ("function vectorProfile(a){const agon=/\\bagonismo(?! inverso)|facilit/i,ant=/antagon|agonismo inverso|bloque|inhib/i,"
 "ad=Math.min(1,g(a,'NET')*.24+g(a,'SERT')*.14+actionSignal(a,'HT1A',agon)*.23+actionSignal(a,'D3',agon)*.16+g(a,'DAT')*.10+g(a,'MAOA')*.13),"
 "am=Math.min(1,actionSignal(a,'D2',ant)*.38+actionSignal(a,'D3',ant)*.20+actionSignal(a,'HT2A',ant)*.14+actionSignal(a,'H1',ant)*.14+actionSignal(a,'M1',ant)*.06),"
 "sed=Math.min(1,actionSignal(a,'H1',ant)*.58+actionSignal(a,'M1',ant)*.24+actionSignal(a,'A1',ant)*.18),"
 "act=Math.min(1,g(a,'NET')*.32+g(a,'DAT')*.25+actionSignal(a,'D3',agon)*.25+actionSignal(a,'HT1A',agon)*.10);"
 "return {x:(act-sed)*7,y:(ad-am)*7,ad,am,sed,act}}")
NEW_VP = r"""/* v16.1 · política anti/pro de H1, α1 y M1 en la capa operativa.
   Antagonismo (anti-): H1 → sedación (principal; también apetito), α1 → sedación secundaria (y ortostasis), M1 → sedación leve (y carga antimuscarínica).
   Agonismo (pro-): H1 y α1 → activación (vigilia); M1 → contención (procolinérgico, procognitivo-antipsicótico).
   Estas dianas siguen sin ser 'polares' en los datos; aquí se leen por su elegibilidad operativa, con dosis (value), sin PET ni cualitativos ni metabolitos,
   y descartando textos de baja afinidad, probables, indirectos o preclínicos (los ordinales débiles conservan su magnitud baja). */
const POL_NEG_B=/sin funci[oó]n|funci[oó]n no|no (se )?(infiere|inferible|resuelt|tipific|asign|fiable)|direcci[oó]n (funcional )?no|preclínic|experimental|propuest|hip[oó]tesis|accesori|contextual|indirect|no demostrad|probable|dato no humano|sin agonismo/i,POL_NEG_W=/baja afinidad|afinidad baja|muy baja|d[eé]bil/i;
function policySignal(a,t,re){const cs=(a[t]?.contrib||[]).filter(x=>['parent','component'].includes(x.entityType)&&x.operationalEligible!==false&&!x.petEligible&&!x.qualitative&&re.test(String(x.action))&&!POL_NEG_B.test(String(x.action))&&(x.evidence==='esqueleto ordinal'||x.potencyEligible===false||!POL_NEG_W.test(String(x.action))));return cs.length?1-cs.reduce((p,x)=>p*(1-Math.min(.98,x.value/10)),1):0}
function vectorProfile(a){const agon=/\bagonismo(?! inverso)|facilit/i,ant=/antagon|agonismo inverso|bloque|inhib/i,antH=/antagon|agonismo inverso|bloque|inhib|antihistam/i,P=(t,re)=>policySignal(a,t,re),
ad=Math.min(1,g(a,'NET')*.24+g(a,'SERT')*.14+actionSignal(a,'HT1A',agon)*.23+actionSignal(a,'D3',agon)*.16+g(a,'DAT')*.10+g(a,'MAOA')*.13),
am=Math.min(1,actionSignal(a,'D2',ant)*.38+actionSignal(a,'D3',ant)*.20+actionSignal(a,'HT2A',ant)*.14+P('H1',antH)*.14+P('M1',agon)*.24),
sed=Math.min(1,P('H1',antH)*.58+P('M1',ant)*.24+P('A1',ant)*.18),
act=Math.min(1,g(a,'NET')*.32+g(a,'DAT')*.25+actionSignal(a,'D3',agon)*.25+actionSignal(a,'HT1A',agon)*.10+P('H1',agon)*.58+P('A1',agon)*.18);
return {x:(act-sed)*7,y:(ad-am)*7,ad,am,sed,act}}"""
rep(OLD_VP, NEW_VP)
anchor = "$$('[data-view]').forEach(b=>b.onclick=()=>activateView(b.dataset.view));addEventListener('resize',renderAtlasContext);"
rep(anchor, js + '\n' + anchor)
OUT.write_text(t, encoding='utf8')
print(OUT, len(t), 'bytes')

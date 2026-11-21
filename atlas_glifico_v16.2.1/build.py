#!/usr/bin/env python3
"""ATLAS GLÍFICO v16.2.1 · fusión de la v16.1 e-ink (Claude) y la v16.2 (ChatGPT).

Uso: python3 build.py RUTA/ATLAS_GLIFICO_VISUAL_v16.0.html [SALIDA.html]

1. Reconstruye la v16.1 con ../atlas_glifico_v16.1_eink/build.py (incluye las correcciones de red,
   la política anti/pro en la capa O y las unidades del atlas).
2. Reaplica sobre ella los cambios de la v16.2 de ChatGPT (tema, modo foco de la red, proyecciones
   con base exclusiva P/O/Q, etiquetas descriptivas), con la política anti/pro y la columna de efectos asociados.
Las anclas son únicas y se comprueban; si una no coincide, el script aborta sin escribir.
"""
import pathlib, re, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
SRC = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent / 'ATLAS_GLIFICO_VISUAL_v16.2.1.html'

with tempfile.TemporaryDirectory() as tmp:
    base = pathlib.Path(tmp) / 'v161.html'
    subprocess.run([sys.executable, '-I', str(HERE.parent / 'atlas_glifico_v16.1_eink' / 'build.py'), str(SRC), str(base)], check=True, stdout=subprocess.DEVNULL)
    html = base.read_text(encoding='utf8')

def rep(old, new):
    global html
    n = html.count(old)
    if n != 1:
        raise SystemExit('Ancla no única (%d): %r' % (n, old[:120]))
    html = html.replace(old, new)

def block(start, end, replacement):
    global html
    i = html.find(start); j = html.find(end, i)
    if i < 0 or j < 0:
        raise SystemExit('Bloque no encontrado: ' + start[:80])
    html = html[:i] + replacement + '\n' + html[j:]

rep('<title>ATLAS GLÍFICO · Atlas visual v16.1 · edición e-ink</title>', '<title>ATLAS GLÍFICO · Atlas visual v16.2.1</title>')
rep('Atlas visual v16.1 <span class="eink-tag">· edición e-ink</span>', 'Atlas visual v16.2.1 <span class="eink-tag" id="themeTag">· edición e-ink</span>')
rep('Mapas clínicos, receptoroma, PK/PD, red farmacodinámica y vectores clínicos; contexto del paciente y fuentes de cada señal.', 'Atlas visual de mecanismos: Fountoulakis, receptoroma y PK/PD; contexto del paciente, relaciones y fuentes.')
rep("atlasVersion:'16.1'", "atlasVersion:'16.2.1'")
rep("a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.0.svg'", "a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.2.1.svg'")

# Tema: el CSS de maquetación compartida se separa del tema monocromo (que el selector puede desactivar)
theme = re.search(r'<style id="eink-theme">([\s\S]*?)</style>', html).group(1)
shared = theme[theme.index('/* ===== Vistas nuevas'):theme.index('svg .eink-node')]
rep('</head>', '<style id="v162-layout">:root{--sans:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}' + shared + (HERE / 'interface_v162.css').read_text(encoding='utf8') + '</style></head>')
rep('scroll-behavior:smooth', 'scroll-behavior:auto')
rep('<button data-view="vectors" data-tier="atlas"><span class="atlas-icon">V</span><b>Vectores clínicos</b><small>áreas de los cuatro componentes por fármaco</small></button>', '')
rep('<nav class="secondary-nav" aria-label="Herramientas complementarias">', '<nav class="secondary-nav" aria-label="Herramientas complementarias"><button data-view="vectors" data-tier="tool">Proyecciones · experimental</button>')
rep('fármacos, dianas, convergencias y competencias</small>', 'coincidencias y oposición de acciones</small>')
for a, b in [
  ('⇄ Competencia: acciones opuestas', '⇄ Oposición de acciones documentadas'),
  ('≈ Señal mixta fármaco/metabolito', '≈ Acciones distintas entre entidades'),
  ('▣ Suma de bloqueo', '▣ Coincidencia de bloqueo/inhibición'),
  ('▣ Suma de agonismo', '▣ Coincidencia de agonismo'),
  ('<h4>⇄ Competencia entre fármacos</h4>', '<h4>⇄ Oposición de acciones</h4>'),
  ('competencia (borde discontinuo)', 'oposición (borde discontinuo)'),
  ('fármacos, dianas, convergencias y competencias</h2>', 'fármacos, dianas y relaciones</h2>'),
  ('dónde coinciden y dónde compiten', 'dónde coinciden y dónde hay acciones de sentido distinto'),
  ('Solo dianas con convergencia o competencia', 'Solo dianas con coincidencia u oposición'),
  ('Dos o más fármacos actúan sobre la misma diana en el mismo sentido: la superposición no es lineal.', 'Dos o más fármacos comparten una diana. La coincidencia descriptiva no prueba suma, sinergia ni efecto neto.'),
]:
    rep(a, b)

# Red enfocable: aristas y nodos con atributos de foco
rep("svg+='<path d=\"M'+x1+','+y1+' C'", "svg+='<path class=\"pdn-edge\" data-pdn-entity=\"'+esc(e.entity)+'\" data-pdn-target=\"'+esc(e.t)+'\" d=\"M'+x1+','+y1+' C'")
rep("svg+='<rect x=\"'+x+'\" y=\"'+p.y+'\" width=\"'+w+'\" height=\"'+p.h", "svg+='<g class=\"pdn-node\" data-pdn-kind=\"entity\" data-pdn-id=\"'+esc(e.entity)+'\" role=\"button\" tabindex=\"0\" aria-pressed=\"false\" aria-label=\"Enfocar '+esc(e.entity)+'\"><rect x=\"'+x+'\" y=\"'+p.y+'\" width=\"'+w+'\" height=\"'+p.h")
rep("  });\n  // nodos diana", "    svg+='</g>';\n  });\n  // nodos diana")
rep("svg+='<rect x=\"'+RX+'\" y=\"'+y0+'\" width=\"'+RW+'\" height=\"'+h", "svg+='<g class=\"pdn-node\" data-pdn-kind=\"target\" data-pdn-id=\"'+esc(t)+'\" role=\"button\" tabindex=\"0\" aria-pressed=\"false\" aria-label=\"Enfocar '+esc(lab)+'\"><rect x=\"'+RX+'\" y=\"'+y0+'\" width=\"'+RW+'\" height=\"'+h")
rep("  });\n  svg+='</svg>';\n  // listas de lectura", "    svg+='</g>';\n  });\n  svg+='</svg>';\n  // listas de lectura")
rep("  const mt=$('#pdnMet');if(mt)mt.onclick=()=>{state.metabolites=!state.metabolites;evaluate()};\n}", "  const mt=$('#pdnMet');if(mt)mt.onclick=()=>{state.metabolites=!state.metabolites;evaluate()};\n  v162FocusNetwork(host);\n}")

# Proyecciones: sustituyen la vista de vectores (no el motor)
block('/* ===== v16.1 · vectores clínicos como áreas', '/* ===== Figuras: panel de pauta', (HERE / 'projections_v1621.js').read_text(encoding='utf8'))
rep('<button type="button" id="toggleAside" aria-pressed="false">☰ Ocultar panel de pauta</button>', '<button type="button" id="toggleAside" aria-pressed="false">☰ Ocultar panel de pauta</button><label>Tema <select id="atlasTheme" aria-label="Tema de la interfaz"><option value="eink">E-ink · alto contraste</option><option value="color">Color · blanco y azul</option></select></label>')
rep("  $('#toggleAside').onclick=", "  v162ThemeTools();\n  $('#toggleAside').onclick=")
rep("$$('[data-view]').forEach(b=>b.onclick=", (HERE / 'interface_v162.js').read_text(encoding='utf8') + "\n$$('[data-view]').forEach(b=>b.onclick=")

OUT.write_text(html, encoding='utf8')
print(OUT, len(html), 'caracteres')

"""Ampliación VIII del Atlas v3.8 (pp. 103–112): corpus de referencias aportado por el autor.

Cifras de resúmenes de PubMed verificados el 20-nov-2026 (refs38.py, P112–P177). Convención F/E/I/H/G.
Donde el resumen no respalda una cifra del documento de origen, se indica en la p. 112. No prescriptivo (p. 20)."""
from layout31 import (new_page, card, card_row, note, sw, text, rect_top, line_top, PURPLE, OCHRE, WHITE, NAVY, INK,
                      GRAY, LINE, TEAL, BLUE, RED, NOTEFILL)
from pages32 import panel, subtitle, X2, X3
from pages33 import arrow, dot, ctext, lines_block
from pages34 import mark, legend_marks, lforest, PALE
from pages37 import vbars

LILA = (0.80, 0.74, 0.86)
AZUL2 = (0.66, 0.76, 0.86)


def num(v, fmt='%g'):
    return (fmt % v).replace('.', ',')


def hrows(it, x0, base0, pitch, rows, scale, label_w, lsize=10.5, suffix=' %', h=12):
    """rows: (etiqueta, valor, color[, texto])."""
    for k, r in enumerate(rows):
        lab, v, col = r[0], r[1], r[2]
        yb = base0 + pitch * k
        it.append(text(x0, yb + 3, lab, 'Roboto-Regular', lsize, INK))
        xb = x0 + label_w
        it.append(rect_top(xb, yb - h / 2 - 1, xb + v * scale, yb + h / 2 - 1, 2, fill=col))
        it.append(text(xb + v * scale + 6, yb + 3, r[3] if len(r) > 3 else num(v) + suffix, 'Roboto-Medium', 9.8, INK))


def pairs(it, x0, base0, pitch, rows, scale, label_w, ca, cb, lsize=10.5):
    """rows: (etiqueta, a, b). Dos barras por fila."""
    for k, (lab, a, b) in enumerate(rows):
        yb = base0 + pitch * k
        it.append(text(x0, yb + 4, lab, 'Roboto-Regular', lsize, INK))
        xb = x0 + label_w
        for j, (v, c) in enumerate(((a, ca), (b, cb))):
            t = yb - 9 + 10 * j
            it.append(rect_top(xb, t, xb + v * scale, t + 8, 2, fill=c))
            it.append(text(xb + v * scale + 5, t + 7.5, num(v), 'Roboto-Medium', 8.8, INK))


def key2(it, x, base, la, ca, lb, cb):
    it.append(rect_top(x, base - 9, x + 12, base, 2, fill=ca))
    it.append(text(x + 17, base, la, 'Roboto-Regular', 9.8, INK))
    x2 = x + 30 + sw(la, 'Roboto-Regular', 9.8)
    it.append(rect_top(x2, base - 9, x2 + 12, base, 2, fill=cb))
    it.append(text(x2 + 17, base, lb, 'Roboto-Regular', 9.8, INK))


def split_bar(it, x0, x1, top, parts, h=22):
    """parts: (valor, color, etiqueta). Barra apilada con etiquetas debajo."""
    tot = float(sum(p[0] for p in parts))
    x = x0
    for v, c, lab in parts:
        w = (x1 - x0) * v / tot
        it.append(rect_top(x, top, x + w - 2, top + h, 3, fill=c))
        ctext(it, x + w / 2, top + h + 13, num(v) + ' %', 'Roboto-Medium', 9.8, INK)
        ctext(it, x + w / 2, top + h + 25, lab, 'Roboto-Regular', 9.2, GRAY)
        x += w


# ------------------------------------------------------------------ 103 · mixticidad I
def p103():
    n = 103
    it = new_page('Estados mixtos: genealogía y definiciones', 'CORPUS · MIXTICIDAD I',
                  'E · P137–P140, P143–P146, P148, P152, P154, P160, P176 | G · cronología | relación con pp. 7, 29 y 50–51', n)
    subtitle(it, 'La frecuencia de lo mixto depende casi por completo de la definición y de la muestra en que se mide.')
    t0, t1 = 128.0, 300.0
    panel(it, 50, t0, 1141, t1, 'Del manual de Kraepelin a los índices cuantitativos', accent=PURPLE)
    nodes = [('1883–1926', 'Nueve ediciones del', 'manual de Kraepelin', 'P138'),
             ('1973', 'Estadios de la manía', '(sin resumen en PubMed)', 'P154'),
             ('1999', 'Depresión agitada', 'como estado mixto', 'P139'),
             ('2000', 'Disforia como', 'tercera dimensión', 'P152 · P140'),
             ('2004', 'Dos tipos kraepelinianos', 'en bipolar II', 'P148'),
             ('2007–2008', 'Melancolía agitada;', 'validez diagnóstica', 'P176 · P146'),
             ('2009', 'Índice de estado', 'mixto (MSI)', 'P143')]
    xa, xb, yl = 110.0, 1080.0, t0 + 86
    it.append(line_top(xa, yl, xb, yl, stroke=GRAY, lw=1.6))
    for k, (yr, l1, l2, src) in enumerate(nodes):
        x = xa + (xb - xa) * k / (len(nodes) - 1)
        dot(it, x, yl, 6, PURPLE)
        ctext(it, x, yl - 16, yr, 'Roboto-Bold', 11.5, NAVY)
        ctext(it, x, yl + 24, l1, 'Roboto-Regular', 9.6, INK)
        ctext(it, x, yl + 37, l2, 'Roboto-Regular', 9.6, INK)
        ctext(it, x, yl + 52, src, 'Roboto-Medium', 9, TEAL)
    top = t1 + 14
    c1 = top + 244
    panel(it, 50, top, 640, c1, 'Proporción «mixta» según definición y muestra', accent=RED)
    rows = [('Rasgos mixtos DSM-5 · TDM recurrente (P160)', 4.6, BLUE),
            ('Manía mixta · pacientes bipolares (P145)', 30, RED, 'al menos 30 %'),
            ('Depresión mixta · episodios depresivos (P176)', 33, PURPLE),
            ('Bipolaridad subumbral · TDM comunitario (P144)', 41.4, TEAL),
            ('DMX3 · bipolar II deprimido (P148)', 62.5, OCHRE)]
    hrows(it, 68, top + 62, 30.0, rows, 3.6, 270)
    lines_block(it, 68, c1 - 26, ['Muestras: 3.000 mujeres coreanas (P160); 1.026 episodios depresivos índice, 346 mixtos (P176);',
                                   '488 con TDM de 2.210 jóvenes (P144); 320 ambulatorios bipolar II (P148). No son comparables entre sí.'],
                size=9.2, lead=12.6)
    t = card(it, 662, top, 1141, title='Criterios propuestos', pill='F · H · P139 · P143 · P148', body=[
        'Koukopoulos: episodio depresivo mayor con al menos dos de agitación motora, agitación psíquica o tensión interna intensa y '
        'pensamiento acelerado o agolpado. Swann: episodio depresivo o maníaco con tres o más síntomas del polo opuesto, aunque los '
        'rasgos mixtos emergen ya con dos. Akiskal y Benazzi: tres o más signos hipomaníacos dentro del episodio (DMX3).'],
             where='p103', bsize=11.0, lead=15.6) + 10
    card(it, 662, t, 1141, t1=c1, title='Validez', pill='E · P146 · P152', body=[
        'El validador más sólido es la historia familiar bipolar; la utilidad se apoya en el efecto negativo de los antidepresivos. La '
        'distribución no bimodal de los síntomas apoya una lectura dimensional. Los subtipos por disforia siguen pendientes de validación.'],
         where='p103', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 104 · mixticidad II
def p104():
    n = 104
    it = new_page('Estados mixtos: correlatos clínicos', 'CORPUS · MIXTICIDAD II',
                  'E · P119, P120, P137, P145, P160, P174 | I · asociaciones de grupo, sin predicción individual | relación con pp. 28–29', n)
    subtitle(it, 'Antecedente familiar, impulsividad, trauma y ansiedad acompañan a lo mixto en muestras muy distintas.')
    t0, t1 = 128.0, 440.0
    panel(it, 50, t0, 700, t1, 'Rasgos mixtos DSM-5 en TDM recurrente: asociaciones (P160) · escala log', accent=RED)
    rows = [('Antecedente familiar de manía', 3.36, 1.67, 6.36, RED),
            ('Uso actual de estabilizador', 2.53, 1.58, 3.92, PURPLE),
            ('Trastorno de pánico', 2.10, 1.46, 2.99, PURPLE),
            ('Ideación suicida en el peor episodio', 1.96, 1.04, 3.94, RED),
            ('Variación diurna del ánimo', 1.94, 1.34, 2.81, TEAL),
            ('Antecedente familiar de depresión', 1.90, 1.41, 2.55, TEAL)]
    lforest(it, 330, 590, t0 + 70, 36.0, rows, 0.5, 8.0, [0.5, 1, 2, 4, 8], zero=1.0, fmt='%.2f', log=True, lsize=10.5)
    lines_block(it, 68, t1 - 26, ['3.000 mujeres de 30 años o más con TDM recurrente, 47 hospitales de Corea del Sur. OR con IC 95 %.',
                                   'Prevalencia de rasgos mixtos en el peor episodio: 4,6 %.'], size=9.2, lead=12.6)
    t = card(it, 722, t0, 1141, title='Síntomas maníacos e impulsividad', pill='E · P137', body=[
        '56 personas con depresión bipolar I o II: la impulsividad y los antecedentes de abuso de alcohol e intento de suicidio '
        'aumentaron con la puntuación de manía, con un punto de inflexión en 6. Los síntomas maníacos se correlacionaron con ansiedad y '
        'psicosis, no con la depresión.'], where='p104', bsize=11.0, lead=15.6) + 10
    card(it, 722, t, 1141, t1=t1, title='Trauma infantil', pill='E · P119', body=[
        '220 pacientes eutímicos y 156 controles: la depresión mixta a lo largo de la vida (criterios de Koukopoulos) se asoció a mayor '
        'trauma total y, de forma específica, al abuso emocional. Diseño transversal.'], where='p104', bsize=11.0, lead=15.6)
    card_row(it, [
        dict(title='Antecedente familiar en la depresión unipolar', pill='E · P120', body=[
            'El 20 % de 135 pacientes unipolares tenía antecedente familiar bipolar: inicio más temprano y más estado mixto depresivo, '
            'sin diferencias con el bipolar II salvo en las recurrencias.']),
        dict(title='Manía con rasgos depresivos', pill='E · P174', body=[
            'Encuesta en línea IMPACT, 700 participantes: con más de tres síntomas depresivos hubo más retraso diagnóstico, periodos '
            'libres más cortos y más ansiedad con irritabilidad. Sesgo de recuerdo.']),
        dict(title='Curso de la manía mixta', pill='E · P145', body=[
            'Frente a la manía pura: más recurrencias, consumo de sustancias, ideación e intentos suicidas, ciclación rápida y '
            'comorbilidad médica, sobre todo tiroidea. Revisión narrativa.']),
    ], t1 + 14, X3, where='p104', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 105 · mixticidad III
YAT = [('Asenapina', 'half', 'ring', 'full', 'ring'), ('Aripiprazol', 'half', 'ring', 'full', 'ring'),
       ('Cariprazina', 'half', 'half', 'ring', 'ring'), ('Divalproato', 'half', 'ring', 'half', 'ring'),
       ('Lurasidona', 'ring', 'half', 'ring', 'ring'), ('Olanzapina', 'ring', 'ring', 'half', 'half'),
       ('Carbamazepina', 'ring', 'ring', 'half', 'ring'), ('Quetiapina', 'ring', 'ring', 'ring', 'full'),
       ('Litio', 'ring', 'ring', 'ring', 'half')]


def p105():
    n = 105
    it = new_page('Estados mixtos: tratamiento', 'CORPUS · MIXTICIDAD III',
                  'F · CANMAT/ISBD 2021 (P142) | E · P123, P124, P161 | H · evidencia escasa | relación con pp. 29, 59 y 72', n)
    subtitle(it, 'Ningún fármaco alcanzó la primera línea para los episodios con rasgos mixtos DSM-5; las recomendaciones dependen de la definición.')
    t0, t1 = 128.0, 500.0
    panel(it, 50, t0, 640, t1, 'Recomendaciones CANMAT/ISBD para presentaciones mixtas (P142)', accent=NAVY)
    cxs = [250, 345, 440, 550]
    heads = [('Manía +', 'rasgos mixtos', 'DSM-5'), ('Depresión +', 'rasgos mixtos', 'DSM-5'), ('Episodio mixto', 'DSM-IV', 'agudo'),
             ('Mantenimiento', 'tras mixto', 'DSM-IV')]
    for c, hd in zip(cxs, heads):
        for m, ln in enumerate(hd):
            ctext(it, c, t0 + 50 + 11 * m, ln, 'Roboto-Bold', 9, NAVY)
    for k, row in enumerate(YAT):
        yb = t0 + 100 + 28 * k
        if k % 2 == 0:
            it.append(rect_top(60, yb - 12, 630, yb + 12, 3, fill=PALE))
        it.append(text(68, yb + 4, row[0], 'Roboto-Medium', 10.5, INK))
        for c, v in zip(cxs, row[1:]):
            mark(it, c, yb, v, NAVY, r=6)
    legend_marks(it, 68, t1 - 26, [('full', 'primera línea'), ('half', 'segunda línea'), ('ring', 'no figura en el resumen')], NAVY)
    it.append(text(68, t1 - 10, 'Mantenimiento tras presentación mixta DSM-5: solo tercera línea, por opinión de expertos.',
                   'Roboto-Regular', 9.2, GRAY))
    gx0 = 662.0
    panel(it, gx0, t0, 1141, 330.0, 'Efecto frente a placebo (DME, IC 95 %)', accent=TEAL)
    rows = [('MADRS (P123) · −1,08 [−1,35 a −0,81]', -1.08, -1.35, -0.81, TEAL),
            ('YMRS (P123) · −0,74 [−1,20 a −0,28]', -0.74, -1.20, -0.28, TEAL),
            ('Lurasidona (P161) · −0,26 [−0,37 a −0,15]', -0.26, -0.37, -0.15, BLUE)]
    lforest(it, gx0 + 235, 1100, t0 + 68, 34.0, rows, -1.5, 0.25, [-1.5, -1, -0.5, 0], zero=0.0, fmt='%.2f', label_w=215, lsize=10,
            show_val=False)
    lines_block(it, gx0 + 18, 330.0 - 24, ['P123: depresión bipolar con rasgos mixtos; 7 estudios, 1.023 pacientes, antipsicóticos atípicos; exploratorio.',
                                            'P161: 14 ECA, 5.239 participantes de tres diagnósticos; riesgo de sesgo y heterogeneidad altos.'],
                size=9.0, lead=12.2)
    card(it, gx0, 344.0, 1141, t1=t1, title='Quetiapina sola o combinada', pill='E · P124', body=[
        'Piloto con 56 pacientes con depresión bipolar y rasgos mixtos DSM-5: cerca del 60 % respondió a la monoterapia en dos semanas, en '
        'una fase abierta sin grupo de control; 21 respondedores insuficientes se aleatorizaron a añadir valproato o litio, sin '
        'diferencia entre ambos.'], where='p105', bsize=11.0, lead=15.6)
    card_row(it, [
        dict(title='Antidepresivos y agitación', pill='E · P139 · P176', body=[
            'En la serie romana, de 346 depresiones mixtas, 173 comenzaron en asociación con antidepresivos. Los autores describen '
            'empeoramiento de la agitación y del insomnio con antidepresivos y proponen neurolépticos, anticonvulsivantes o terapia '
            'electroconvulsiva. Son series clínicas y revisiones narrativas, no ensayos (p. 31).']),
        dict(title='I · Límite de la evidencia', pill='I · P142 · P145', body=[
            'No hay ensayos controlados dedicados solo a la manía mixta: los datos proceden de subanálisis. La guía reconoce escasez de '
            'datos de calidad y dependencia de la opinión experta. La matriz ordena recomendaciones; no sustituye la ficha técnica ni la '
            'p. 20.']),
    ], t1 + 14, X2, where='p105', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 106 · espectro y carga depresiva
def p106():
    n = 106
    it = new_page('Espectro: epidemiología y carga depresiva', 'CORPUS · ESPECTRO',
                  'E · P118, P144, P147, P155–P157, P162, P163 | I · definiciones de subumbral | relación con pp. 22, 44 y 52', n)
    subtitle(it, 'La forma subumbral es la más frecuente del espectro y la depresión ocupa la mayor parte del tiempo enfermo.')
    t0, t1 = 128.0, 420.0
    panel(it, 50, t0, 520, t1, 'Prevalencia en adultos de EE. UU. · NCS-R (P155)', accent=TEAL)
    pairs(it, 68, t0 + 84, 56.0, [('Bipolar I', 1.0, 0.6), ('Bipolar II', 1.1, 0.8), ('Subumbral', 2.4, 1.4)], 110.0, 100, TEAL, AZUL2,
          lsize=11.5)
    key2(it, 68, t0 + 250, 'a lo largo de la vida (%)', TEAL, 'últimos 12 meses (%)', AZUL2)
    lines_block(it, 68, t1 - 26, ['9.282 adultos; entrevista CIDI, DSM-IV. Subumbral: hipomanía recurrente sin episodio depresivo',
                                   'mayor o con menos síntomas de los exigidos. El uso de antimaníacos fue infrecuente.'], size=9.2, lead=12.6)
    gx0 = 542.0
    panel(it, gx0, t0, 1141, t1, 'Bipolaridad subumbral dentro de la depresión mayor (P144)', accent=PURPLE)
    split_bar(it, gx0 + 30, 1110, t0 + 62, [(58.6, AZUL2, 'TDM puro (286)'), (41.4, PURPLE, 'TDM con síntomas maníacos subumbrales (202)')])
    lines_block(it, gx0 + 18, t0 + 140, ['Cohorte comunitaria de Múnich, 2.210 jóvenes seguidos diez años; 488 con TDM.',
                                          'El grupo subumbral mostró más antecedente familiar de manía, más alcohol y nicotina,',
                                          'el doble de trastorno de pánico y más conversión a trastorno bipolar.'], size=10.3, lead=14.4,
                color=INK)
    ctext(it, gx0 + 120, t0 + 236, '39 : 1', 'Roboto-Bold', 30, NAVY)
    ctext(it, gx0 + 120, t0 + 256, 'episodios depresivos por hipomaníaco', 'Roboto-Medium', 9.8, INK)
    ctext(it, gx0 + 120, t0 + 269, 'en el bipolar II (P118)', 'Roboto-Regular', 9.5, GRAY)
    lines_block(it, gx0 + 260, t0 + 226, ['Revisión de estado del arte: el bipolar II se', 'confunde a menudo con la depresión mayor y',
                                           'se solapa con el trastorno límite; su tasa de', 'suicidio consumado es al menos equivalente',
                                           'a la del bipolar I.'], size=10.3, lead=14.2, color=INK)
    card_row(it, [
        dict(title='Un espectro del ánimo', pill='E · P147', body=[
            '117 pacientes con depresión unipolar recurrente y 106 con bipolar I: los unipolares refirieron un número sustancial de '
            'síntomas maníacos o hipomaníacos a lo largo de la vida, relacionado con ideación suicida y pensamiento paranoide.']),
        dict(title='Duración de los episodios', pill='E · P157 · P156', body=[
            '1.130 pacientes tratados, 16,7 años de riesgo: los episodios depresivos fueron mucho más largos que los maníacos en todos '
            'los subtipos, salvo el psicótico. La depresión explica la mayor parte del tiempo enfermo y de la carga.']),
        dict(title='Redes de síntomas', pill='E · P162 · P163', body=[
            'En 322 pacientes con TDM y 516 bipolares, el afecto deprimido fue el nodo central y la estructura de la red no difirió. '
            'En otra cohorte de 143, la red bipolar estuvo guiada por la neurocognición. Asociación, no causalidad.']),
    ], t1 + 14, X3, where='p106', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 107 · alto riesgo y estadios
def p107():
    n = 107
    it = new_page('Descendencia de alto riesgo y estadios', 'CORPUS · CURSO',
                  'E · P121, P122, P154, P164, P172, P173 | H · el estadiaje sigue siendo un constructo | relación con pp. 42 y 54', n)
    subtitle(it, 'Los hijos de personas con trastorno bipolar muestran antecedentes inespecíficos antes de la manía; el estadio se valida a tres años.')
    t0, t1 = 128.0, 470.0
    panel(it, 50, t0, 600, t1, 'Hijos de progenitores bipolares frente a comunidad (P172)', accent=RED)
    rows = [('Trastornos de ansiedad', 39.9, 21.8), ('Episodio depresivo mayor', 32.0, 14.9), ('TDAH', 30.7, 18.1),
            ('Conducta disruptiva', 27.4, 15.3), ('Uso de sustancias', 19.9, 10.1), ('Manía o hipomanía subumbral', 13.3, 1.2),
            ('Episodio maníaco, mixto o hipomaníaco', 9.2, 0.8)]
    pairs(it, 68, t0 + 66, 34.0, rows, 6.0, 230, RED, AZUL2)
    key2(it, 68, t1 - 34, 'alto riesgo, n = 391 (%)', RED, 'comunidad, n = 248 (%)', AZUL2)
    it.append(text(68, t1 - 12, 'Edad 6–18 años; seguimiento medio 6,8 años. Prospectivamente, solo la manía subumbral predijo el episodio (HR 7,57).',
                   'Roboto-Regular', 9.2, GRAY))
    gx0 = 622.0
    panel(it, gx0, t0, 1141, 300.0, 'Cohorte canadiense a dos décadas (P173)', accent=PURPLE)
    ctext(it, gx0 + 80, t0 + 84, '24,5 %', 'Roboto-Bold', 26, NAVY)
    ctext(it, gx0 + 80, t0 + 102, 'incidencia acumulada', 'Roboto-Medium', 9.5, INK)
    ctext(it, gx0 + 80, t0 + 115, 'mediana de inicio 20,7 años', 'Roboto-Regular', 9.2, GRAY)
    hrows(it, gx0 + 180, t0 + 62, 22.0, [('Sueño infantil', 1.6, LILA), ('Ansiedad infantil', 1.8, LILA), ('Síntomas maníacos', 2.3, PURPLE),
                                          ('Síntomas depresivos', 2.7, PURPLE)], 48.0, 118, lsize=10, suffix=' ×')
    it.append(text(gx0 + 18, 300.0 - 12, '279 hijos de alto riesgo y 87 controles. Veces de aumento del riesgo de trastorno del ánimo.',
                   'Roboto-Regular', 9.2, GRAY))
    panel(it, gx0, 314.0, 1141, t1, 'Modelo empírico de cinco estadios a 3 años (P122)', accent=TEAL)
    split_bar(it, gx0 + 30, 1110, 314.0 + 54, [(23.3, TEAL, 'retrocede'), (49.6, AZUL2, 'mismo estadio'), (20.9, OCHRE, 'progresa')])
    it.append(text(gx0 + 18, t1 - 12, '224 pacientes; 129 (57,6 %) completaron los 3 años. Al progresar: deterioro funcional y más fármacos.',
                   'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Secuencia emergente', pill='E · P173', body=[
            'El modelo que mejor ajustó fue una progresión desde antecedentes infantiles inespecíficos a la depresión adolescente y de '
            'ahí al primer episodio maníaco o hipomaníaco. La depresión predominó al inicio del curso.']),
        dict(title='Nomenclatura de consenso', pill='F · H · P121', body=[
            'El grupo de trabajo de la ISBD unificó los términos de los modelos de estadiaje, desde el riesgo hasta los estadios '
            'clínicos. Advierte que en psiquiatría el estadiaje sigue siendo un constructo hipotético.']),
        dict(title='Estadio y conectividad', pill='E · H · P164 · P154', body=[
            '123 personas en estadios 0–4: la densidad de conexiones bajó del estadio 0 al 3 y subió en el 4. Hallazgo de grupo, sin '
            'prueba individual. Los estadios clásicos de la manía (P154) carecen de resumen en PubMed.']),
    ], t1 + 14, X3, where='p107', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 108 · esquizoafectivo
def p108():
    n = 108
    it = new_page('Trastorno esquizoafectivo: estabilidad, fiabilidad y parentesco', 'CORPUS · ESQUIZOAFECTIVO',
                  'E · P116, P125–P131, P177 | I · categoría de frontera | relación con pp. 25, 40, 48 y 101', n)
    subtitle(it, 'Es el diagnóstico menos estable y menos fiable del espectro psicótico-afectivo, y su biología no lo separa con nitidez.')
    t0, t1 = 128.0, 440.0
    panel(it, 50, t0, 600, t1, 'Cambio de diagnóstico en el seguimiento (P125)', accent=PURPLE)
    it.append(text(68, t0 + 58, 'Diagnosticados de esquizoafectivo al inicio: 36 % cambia', 'Roboto-Bold', 11, NAVY))
    split_bar(it, 68, 580, t0 + 68, [(64, PALE, 'mantiene'), (19, PURPLE, 'esquizofrenia'), (14, BLUE, 'afectivo'), (6, GRAY, 'otros')])
    it.append(text(68, t0 + 150, 'Esquizoafectivo en la segunda evaluación: 55 % tenía otro diagnóstico', 'Roboto-Bold', 11, NAVY))
    split_bar(it, 68, 580, t0 + 160, [(45, PALE, 'ya lo tenía'), (24, BLUE, 'afectivo'), (18, PURPLE, 'esquizofrenia'), (12, GRAY, 'otros')])
    lines_block(it, 68, t1 - 40, ['Metaanálisis de 31 estudios de rediagnóstico; intervalo mediano de dos años. Ligera tendencia hacia la',
                                   'esquizofrenia. Los tramos «mantiene» y «ya lo tenía» son el complemento (G); los porcentajes publicados',
                                   'suman 39 % y 54 % por redondeo.'], size=9.2, lead=12.6)
    gx0 = 622.0
    panel(it, gx0, t0, 1141, t1, 'Fiabilidad y heredabilidad', accent=NAVY)
    for k, (lab, v, lo, hi, src) in enumerate((('Entre evaluadores', 0.57, 0.41, 0.73, 'P126 · 25 estudios, 7.912 pacientes'),
                                               ('Test-retest', 0.50, 0.40, 0.59, 'P127 · 49 estudios'))):
        yb = t0 + 74 + 50 * k
        it.append(text(gx0 + 18, yb + 4, lab, 'Roboto-Medium', 10.8, INK))
        xa = gx0 + 150
        it.append(rect_top(xa, yb - 7, xa + 300, yb + 7, 3, fill=PALE))
        it.append(rect_top(xa, yb - 7, xa + 300 * v, yb + 7, 3, fill=NAVY))
        it.append(line_top(xa + 300 * lo, yb, xa + 300 * hi, yb, stroke=OCHRE, lw=2.2))
        it.append(text(xa + 308, yb + 4, 'κ ' + num(v, '%.2f'), 'Roboto-Bold', 10.5, INK))
        it.append(text(xa, yb + 21, src + ' · IC 95 % ' + num(lo, '%.2f') + '–' + num(hi, '%.2f'), 'Roboto-Regular', 9, GRAY))
    it.append(text(gx0 + 18, t0 + 182, 'En ambos casos, unos 0,2 puntos por debajo de esquizofrenia, bipolar y depresión unipolar.',
                   'Roboto-Regular', 10, INK))
    ctext(it, gx0 + 110, t0 + 240, '82–85 %', 'Roboto-Bold', 26, NAVY)
    ctext(it, gx0 + 110, t0 + 258, 'heredabilidad (P129)', 'Roboto-Medium', 9.8, INK)
    lines_block(it, gx0 + 230, t0 + 222, ['Serie gemelar del Maudsley, 224 probandos: las', 'estimaciones para esquizofrenia, esquizoafectivo',
                                           'y manía (RDC) no difirieron entre sí. En el', 'reanálisis de 2012 (P128), la fiabilidad del',
                                           'síndrome esquizoafectivo fue solo moderada.'], size=10, lead=13.8, color=INK)
    card_row(it, [
        dict(title='Cognición y neuroimagen', pill='E · P116', body=[
            'Revisión sistemática (22 artículos neuropsicológicos y 19 de neuroimagen): el rendimiento cognitivo y la pérdida de '
            'sustancia gris se parecen más a la esquizofrenia que al trastorno bipolar. Los autores hablan de tendencia general.']),
        dict(title='Debate nosológico', pill='H · P131 · P177', body=[
            'Malhi y colaboradores proponen dos modelos, comorbilidad de esquizofrenia y bipolar o punto medio de un continuo, y '
            'recomiendan suprimir la categoría. Marneros la sitúa entre ambos polos y subraya el tipo mixto como el más grave.']),
        dict(title='Tratamiento', pill='E · P130', body=[
            '33 estudios con criterios estandarizados, 14 de ellos aleatorizados: base pequeña y heterogénea que no permite '
            'recomendar de forma consistente antipsicóticos, estabilizadores o combinaciones.']),
    ], t1 + 14, X3, where='p108', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 109 · fenomenología y TLP
def p109():
    n = 109
    it = new_page('Fenomenología diferencial y frontera con el trastorno límite', 'CORPUS · FENOMENOLOGÍA',
                  'F · EASE (P132), EAWE (P133) | E · P117, P118, P134 | I · uso en el diferencial | relación con pp. 38, 43 y 46', n)
    subtitle(it, 'Las entrevistas fenomenológicas describen la experiencia; la comorbilidad límite cambia el curso agudo del bipolar I.')
    t0, t1 = 128.0, 430.0
    panel(it, 50, t0, 640, t1, 'EAWE: seis dominios de la experiencia del mundo (P133)', accent=PURPLE)
    doms = ['Espacio y objetos', 'Tiempo y sucesos', 'Otras personas', 'Lenguaje', 'Atmósfera', 'Orientación existencial']
    for k, d in enumerate(doms):
        xa = 68 + (k % 3) * 186
        ta = t0 + 56 + (k // 3) * 78
        it.append(rect_top(xa, ta, xa + 174, ta + 64, 8, fill=WHITE, stroke=PURPLE, lw=1.4))
        ctext(it, xa + 87, ta + 28, str(k + 1), 'Roboto-Bold', 15, PURPLE)
        ctext(it, xa + 87, ta + 48, d, 'Roboto-Medium', 10.5, INK)
    lines_block(it, 68, t0 + 232, ['Entrevista semiestructurada con 75 ítems. Se diseñó para experiencias frecuentes, y a veces distintivas,',
                                    'del espectro esquizofrénico, aunque puede usarse en otras poblaciones. El resumen no da datos psicométricos.',
                                    'La EASE (P132) explora las anomalías de la experiencia de sí; PubMed no ofrece resumen de ese artículo.'],
                size=10, lead=14, color=INK)
    it.append(text(68, t1 - 12, 'F · Instrumentos descriptivos; su valor discriminativo frente a la psicosis bipolar no consta en estos resúmenes.',
                   'Roboto-Regular', 9.2, GRAY))
    gx0 = 662.0
    panel(it, gx0, t0, 1141, t1, 'Bipolar I con trastorno límite comórbido (P117)', accent=RED)
    vbars(it, gx0 + 90, t1 - 96, 96, 70, [25, 74], 80, 140, [RED, AZUL2], ['Bipolar I + límite\n(3 de 12)', 'Bipolar I solo\n(43 de 58)'])
    ctext(it, gx0 + 240, t0 + 52, 'Estabilización del episodio agudo', 'Roboto-Bold', 11, NAVY)
    lines_block(it, gx0 + 18, t1 - 40, ['Mediana hasta la estabilización: 35 semanas en el grupo sin comorbilidad; dos de los tres',
                                         'estabilizados con comorbilidad tardaron más de 95. Estudio cuasiexperimental, con abandono',
                                         'alto en el grupo comórbido.'], size=9.2, lead=12.6)
    card_row(it, [
        dict(title='Más allá de las voces', pill='I · P134', body=[
            'Revisión conceptual: aislar la alucinación como fenómeno transdiagnóstico puede ocultar cambios simultáneos en la '
            'percepción, el sí mismo, la temporalidad, la corporalidad y la relación con otros. Propone la alucinación como desenlace '
            'común de procesos distintos. No aporta datos comparativos entre psicosis bipolar y esquizofrénica.']),
        dict(title='I · Lectura en el atlas', pill='I · P118', body=[
            'El atlas ya trata la vivencia del tiempo y del cuerpo (p. 46) y el diferencial con el trastorno límite (p. 38). Estas '
            'fuentes añaden instrumentos para describir, no umbrales para clasificar. El bipolar II es el punto de mayor solapamiento '
            'sintomático con el trastorno límite.']),
    ], t1 + 14, X2, where='p109', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 110 · genética compartida y neuroimagen
def p110():
    n = 110
    it = new_page('Genética compartida y neuroimagen', 'CORPUS · NEUROBIOLOGÍA',
                  'E · P112–P115, P159, P164–P170 | H · ningún hallazgo es prueba diagnóstica individual | relación con pp. 100–102', n)
    subtitle(it, 'El solapamiento poligénico alcanza a la toma de riesgos; la neuroimagen ofrece clasificadores de grupo aún sin validar.')
    t0, t1 = 128.0, 410.0
    panel(it, 50, t0, 560, t1, 'Loci compartidos con fenotipos de riesgo (P112)', accent=PURPLE)
    hrows(it, 68, t0 + 66, 32.0, [('Bipolar y fenotipos de riesgo', 206, PURPLE), ('Esquizofrenia y fenotipos de riesgo', 192, BLUE),
                                   ('Nuevos para bipolar o esquizofrenia', 124, LILA), ('Comunes a ambos fenotipos de riesgo', 68, LILA)],
          1.05, 215, suffix='')
    lines_block(it, 68, t0 + 204, ['De 8.600–8.700 variantes que influyen en el trastorno bipolar, se predice que 6.600 influyen en',
                                    'la toma de riesgos y 7.400 en las conductas de riesgo. «Fenotipos de riesgo» reúne ambos rasgos.'],
                size=10, lead=14, color=INK)
    it.append(text(68, t1 - 12, 'Análisis de estadísticos resumen de GWAS (n entre 82.315 y 466.751).', 'Roboto-Regular', 9.2, GRAY))
    gx0 = 582.0
    panel(it, gx0, t0, 1141, t1, 'Clasificador de conversión a bipolar por RM funcional (P114)', accent=TEAL)
    vbars(it, gx0 + 40, t1 - 86, 62, 28, [81, 82.6, 79, 74.6], 90, 150, [TEAL, TEAL, TEAL, AZUL2],
          ['Exactitud', 'Sensibilidad', 'Especificidad', 'AUC'], lsize=9.6)
    lines_block(it, gx0 + 400, t0 + 70, ['92 pacientes con TDM', 'seguidos más de dos', 'años: 23 pasaron a', 'bipolar.', '',
                                          'Conectividad de la', 'amígdala; máquina de', 'vectores de soporte.'], size=10, lead=14, color=INK)
    it.append(text(gx0 + 18, t1 - 12, 'Muestra única y pequeña; sin validación externa en el resumen.', 'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Pleiotropía y circuitos', pill='E · H · P113 · P115', body=[
            'Con cerca de un millón de casos de diez trastornos psiquiátricos y diez neurológicos, muchas variantes comunes afectan a '
            'varios trastornos, y las psiquiátricas implican de forma consistente biología neuronal. Una revisión propone tres '
            'circuitos (emocional, cognitivo y psicomotor) como hipótesis de taxonomía.']),
        dict(title='Conectividad y fenotipos', pill='E · P159 · P166 · P168–P170', body=[
            'Revisión de 51 estudios: menor conectividad intrínseca en las redes por defecto, de saliencia y ejecutiva. Estudios '
            'pequeños asocian la dinámica cerebral con impulsividad (48 bipolares I), el polo del primer episodio pediátrico (43) y '
            'un índice poligénico de conducta suicida con la corteza prefrontal ventral (376). El estudio de EEG no da cifras de '
            'rendimiento.']),
        dict(title='Modelos animales', pill='H · P165 · P167', body=[
            'En ratones con mutación de la Na+,K+-ATPasa α3, la melatonina y el ejercicio redujeron la conducta de tipo maníaco. Otro '
            'estudio describe firmas transcripcionales de la habénula según el fenotipo de tipo depresivo. Ninguno demuestra eficacia '
            'ni mecanismo en personas.']),
    ], t1 + 14, X3, where='p110', bsize=10.8, lead=15.2)
    return it


# ------------------------------------------------------------------ 111 · adherencia, ciclación rápida, instrumentos
def p111():
    n = 111
    it = new_page('Adherencia, ciclación rápida histórica e instrumentos', 'CORPUS · PRÁCTICA',
                  'E · P141, P149, P151, P153 | F · P135, P136 | sin resumen: P150, P158 | método: P171 | relación con pp. 16, 26 y 50', n)
    subtitle(it, 'Fuentes de contexto: la adherencia como condición de cualquier resultado y la ciclación rápida antes de los ensayos modernos.')
    t0, t1 = 128.0, 420.0
    panel(it, 50, t0, 560, t1, 'Ciclación rápida: litio o lamotrigina, un año (P149)', accent=OCHRE)
    pairs(it, 68, t0 + 96, 70.0, [('Menos de cuatro episodios', 43, 86), ('Cuatro o más episodios', 57, 14)],
          3.0, 180, BLUE, OCHRE, lsize=11)
    key2(it, 68, t0 + 240, 'litio, n = 7 (%)', BLUE, 'lamotrigina, n = 7 (%)', OCHRE)
    lines_block(it, 68, t1 - 40, ['Estudio abierto con 14 pacientes. Tres de los siete tratados con lamotrigina (43 %) no tuvieron ningún',
                                   'episodio; el resumen no da ese dato para el litio. Los autores lo consideran preliminar: no',
                                   'demuestra superioridad.'], size=9.2, lead=12.6)
    t = card(it, 582, t0, 1141, title='No adherencia', pill='E · P141', body=[
        'Revisión narrativa: en una gran base de datos estadounidense, cerca de la mitad de los pacientes no fue adherente al litio y a '
        'los fármacos de mantenimiento en 12 meses. Se asocia a recaída, hospitalización e intento de suicidio; la interrupción brusca '
        'del litio puede provocar rebote. Factores: efectos adversos, pautas complejas, baja conciencia de enfermedad, ciclación rápida, '
        'consumo de sustancias y mala alianza.'], where='p111', bsize=11.0, lead=15.6) + 10
    card(it, 582, t, 1141, t1=t1, title='Escala de estado interno', pill='E · P153', body=[
        '86 pacientes de cuatro centros de veteranos: el algoritmo revisado mostró acuerdo moderado con el clínico e hizo viable '
        'identificar episodios mixtos por autoinforme. Muestra sobre todo masculina.'], where='p111', bsize=11.0, lead=15.6)
    card_row(it, [
        dict(title='Ciclación rápida hacia el año 2000', pill='E · P151', body=[
            'Revisión selectiva: el litio resultaba insuficiente para la mayoría de los cicladores rápidos; valproato y carbamazepina '
            'como alternativas, y lamotrigina entre las opciones emergentes. Contexto histórico para las pp. 95–97.']),
        dict(title='Guía RANZCP 2020', pill='F · P135 · P136', body=[
            'Ordena cada fase en acciones (estilo de vida, psicoeducación, psicoterapia), fármacos de elección y alternativas; '
            'recomienda la terapia electroconvulsiva en las fases agudas, no en el mantenimiento. El modelo ACE está en la p. 50.']),
        dict(title='Fuentes sin contenido verificable', pill='P150 · P158 · P171', body=[
            'Un editorial de 2000 y un comentario de 2026 sobre adherencia carecen de resumen en PubMed: se citan solo como '
            'referencia. La comparación de cribado bibliográfico con modelos de lenguaje es metodológica y no aporta contenido clínico.']),
    ], t1 + 14, X3, where='p111', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 112 · auditoría del corpus
AUD = [('Mitad de los suicidios bipolares ocurre en estados mixtos', 'P175', 'no',
        'El resumen no lo dice: la «mitad a dos tercios» es la parte de todos los suicidios debida a trastornos del ánimo.'),
       ('Agitación más depresión: OR 4,2 de suicidio', 'P176', 'no', 'El resumen no contiene ninguna razón de odds ni datos de suicidio.'),
       ('Esquizoafectivo: heredabilidad cercana al 80 %; κ 0,58', 'P128', 'corr',
        'La heredabilidad (82–85 %) está en el estudio de 1999 (P129). El κ no figura en ningún resumen.'),
       ('Tratamiento del esquizoafectivo: 6 ensayos doble ciego', 'P130', 'corr', 'El resumen dice 33 estudios, 14 de ellos aleatorizados.'),
       ('Cambio diagnóstico del 36 %, 31 estudios, N = 1.866', 'P125', 'parc', 'El 36 % y los 31 estudios constan; el N no está en el resumen.'),
       ('Guía RANZCP: Bipolar Disord 2020;22:805–875', 'P135', 'corr',
        'Las páginas son 805–821 y es el resumen bipolar; la guía completa es P136.'),
       ('Escala de estado interno: título de la referencia', 'P153', 'corr', 'El DOI corresponde a otro título, que es el recogido en la bibliografía.'),
       ('Alteraciones de redes a gran escala: metaanálisis', 'P168', 'corr', 'Es una revisión de 51 estudios sin síntesis cuantitativa.'),
       ('Clasificador de RM funcional: 81 %, 82,6 %, 79 %', 'P114', 'ok', 'Confirmado; el AUC es 74,6 %.'),
       ('BIP y toma de riesgos: 206 loci compartidos', 'P112', 'parc', 'Confirmado para «fenotipos de riesgo», que suman dos rasgos.'),
       ('Prevalencias NCS-R, bipolar I con límite, DMX3, 4,6 % mixto', 'P155 · P117 · P148 · P160', 'ok', 'Confirmadas en los resúmenes.'),
       ('Uso de sustancias en 4.250 pacientes (Miola, 2026)', '—', 'no', 'El DOI no está indexado en PubMed: no se incorpora al atlas.')]


def p112():
    n = 112
    it = new_page('Cotejo del corpus aportado con PubMed', 'CORPUS · AUDITORÍA',
                  'E · 66 registros de PubMed leídos el 20-nov-2026 (P112–P177) | I · criterio de inclusión del atlas', n)
    subtitle(it, 'Cada cifra del documento de origen se comparó con el resumen de PubMed; solo entran en el atlas las que el resumen respalda.')
    t0 = 128.0
    pitch = 39.0
    t1 = t0 + 44 + pitch * len(AUD) + 8
    panel(it, 50, t0, 1141, t1, 'Afirmaciones del documento de origen y resultado del cotejo', accent=NAVY)
    cols = {'ok': (TEAL, 'confirmada'), 'parc': (OCHRE, 'parcial'), 'corr': (BLUE, 'corregida'), 'no': (RED, 'sin respaldo')}
    for k, (claim, src, st, txt) in enumerate(AUD):
        yb = t0 + 62 + pitch * k
        if k % 2 == 0:
            it.append(rect_top(60, yb - 17, 1131, yb + 18, 3, fill=PALE))
        col, lab = cols[st]
        it.append(rect_top(68, yb - 9, 150, yb + 9, 9, fill=col))
        ctext(it, 109, yb + 4, lab, 'Roboto-Bold', 9.2, WHITE)
        it.append(text(162, yb - 2, claim, 'Roboto-Medium', 10.8, INK))
        it.append(text(162, yb + 12, txt, 'Roboto-Regular', 9.8, GRAY))
        it.append(text(1121 - sw(src, 'Roboto-Medium', 9.5), yb - 2, src, 'Roboto-Medium', 9.5, TEAL))
    card_row(it, [
        dict(title='Balance', pill='E', body=[
            'De 63 referencias buscadas, 62 están indexadas en PubMed; cinco carecen de resumen (P132, P140, P150, P154, P158) y se '
            'citan sin atribuirles cifras. Se añadieron cuatro registros necesarios para situar bien los datos (P126, P127, P129, P136).']),
        dict(title='I · No cotejado', pill='I', body=[
            'Quedan fuera las afirmaciones del documento de origen sin referencia localizable: el riesgo atribuido a los antidepresivos '
            'en la depresión agitada (OR 4,8), la correlación genética de 0,70 atribuida al consorcio en 2019 y el metaanálisis de 2022 '
            'sobre trastornos del sí mismo.']),
    ], t1 + 12, X2, where='p112', bsize=10.8, lead=15.0, accent=OCHRE, fill=NOTEFILL)
    return it


NEW_PAGES38 = [p103, p104, p105, p106, p107, p108, p109, p110, p111, p112]

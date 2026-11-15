"""Ampliación IV del Atlas v3.3 (pp. 49–55): nosología y clasificación dimensional.

Redacción extensa (no telegráfica) y gráficos propios. Convención: F criterio formal · E hallazgo
empírico (P##) · I interpretación · H hipótesis o propuesta · G geometría editorial no calibrada.
Cifras y afirmaciones tomadas de los resúmenes de PubMed verificados el 15-nov-2026 (refs33.py)."""
import math

from layout31 import (new_page, card, card_row, note, hbars, sw, text, rect_top, line_top, path,
                      rrect_ops, PURPLE, OCHRE, PILLFILL, NOTEFILL, INFOFILL, WARN, WHITE, NAVY, INK,
                      GRAY, LINE, TEAL, BLUE, RED, Y)
from pages32 import panel, subtitle, X2, X3

GREEN = (0.30, 0.55, 0.36)
SOFT = {'A': RED, 'C': PURPLE, 'E': BLUE}


# ------------------------------------------------------------------ primitivas gráficas
def arrow(it, x0, t0, x1, t1, color=INK, lw=1.4, head=7.0, both=False):
    it.append(line_top(x0, t0, x1, t1, stroke=color, lw=lw))

    def tip(xa, ta, xb, tb):
        ang = math.atan2(Y(tb) - Y(ta), xb - xa)
        ops = [('m', xb, Y(tb))]
        for s in (+1, -1):
            a = ang + math.pi + s * 0.42
            ops.append(('l', xb + head * math.cos(a), Y(tb) + head * math.sin(a)))
        ops.append(('h',))
        it.append(path(ops, fill=color, stroke=color, lw=0.8))
    tip(x0, t0, x1, t1)
    if both:
        tip(x1, t1, x0, t0)


def dot(it, cx, ct, r, fill, stroke=None, lw=1.0):
    it.append(path(rrect_ops(cx - r, Y(ct + r), cx + r, Y(ct - r), r), fill=fill, stroke=stroke or fill, lw=lw))


def tri(it, cx, ct, s, up, fill):
    if up:
        ops = [('m', cx, Y(ct - s)), ('l', cx - s, Y(ct + s * 0.75)), ('l', cx + s, Y(ct + s * 0.75)), ('h',)]
    else:
        ops = [('m', cx, Y(ct + s)), ('l', cx - s, Y(ct - s * 0.75)), ('l', cx + s, Y(ct - s * 0.75)), ('h',)]
    it.append(path(ops, fill=fill, stroke=fill, lw=0.8))


def ctext(it, cx, base, s, font='Roboto-Medium', size=11, color=INK):
    it.append(text(cx - sw(s, font, size) / 2, base, s, font, size, color))


def curve(it, xs, tops, color, lw=2.4, dash=None, fill=None, base_top=None):
    ops = [('m' if k == 0 else 'l', x, Y(t)) for k, (x, t) in enumerate(zip(xs, tops))]
    if fill is not None:
        fops = ops + [('l', xs[-1], Y(base_top)), ('l', xs[0], Y(base_top)), ('h',)]
        it.append(path(fops, fill=fill, alpha=0.18))
    it.append(path(ops, stroke=color, lw=lw, dash=dash))


def lines_block(it, x, base, lines, size=11, color=GRAY, lead=15.5, font='Roboto-Regular'):
    for ln in lines:
        it.append(text(x, base, ln, font, size, color))
        base += lead
    return base


# ------------------------------------------------------------------ 49
def p49():
    n = 49
    it = new_page('Categorías y dimensiones: validez, utilidad y continuidad', 'NOSOLOGÍA · I',
                  'E · P72, P73 | G · distribuciones esquemáticas sin datos | I · consecuencias para la geometría del atlas', n)
    subtitle(it, 'Antes de comparar modelos conviene separar dos preguntas que a menudo se confunden: si una categoría es natural y si es útil.')
    left = (50.0, 640.0)
    top = 130.0
    top = card(it, left[0], top, left[1], title='Validez y utilidad no son lo mismo', pill='E · I · P72', body=[
        'Kendell y Jablensky proponen reservar la palabra «válida» para la categoría diagnóstica que haya demostrado ser una entidad '
        'discreta, separada de otros trastornos y de la normalidad por fronteras naturales o «zonas de rareza». Tras revisar la '
        'evidencia concluyen que, pese a lo que se ha supuesto histórica y recientemente, la mayoría de los trastornos mentales '
        'reconocidos no muestra esas fronteras, y que los investigadores tienden cada vez más a suponer una variación continua de '
        'los síntomas.',
        'Eso no las vuelve inservibles: muchas categorías tienen una utilidad alta porque transmiten información sobre la evolución, '
        'la respuesta al tratamiento y la etiología. Por eso los autores las consideran conceptos de trabajo valiosos para la clínica.'],
        where='p49', bsize=12, lead=17.6) + 14
    top = card(it, left[0], top, left[1], title='Qué muestran los estudios taxométricos', pill='E · P73', body=[
        'Los métodos taxométricos, desarrollados por Meehl, intentan decidir si una variable latente es categorial (un «taxón») o '
        'dimensional. La revisión cuantitativa de Haslam y colaboradores reunió 177 artículos, 311 hallazgos y 533.377 participantes. '
        'El 38,9 % de los hallazgos publicados era taxónico, pero esa proporción caía en los estudios más recientes y '
        'metodológicamente más sólidos; controlados los sesgos, la prevalencia real de hallazgos taxónicos se estimó en un 14 %.',
        'En particular, los trastornos del estado de ánimo no ofrecieron pruebas convincentes de taxones; la evidencia prometedora, '
        'aunque no definitiva, se limitó a la esquizotipia, los trastornos por uso de sustancias y el autismo.'],
        where='p49', bsize=12, lead=17.6) + 14
    # gráfico: dos modelos de variable latente
    gx0, gx1 = 662.0, 1141.0
    gt0, gt1 = 130.0, 494.0
    panel(it, gx0, gt0, gx1, gt1, 'Dos maneras de representar la misma población', accent=PURPLE)
    px0, px1 = gx0 + 28, gx1 - 28

    def dens(xn, mus, sds, ws):
        return sum(w * math.exp(-0.5 * ((xn - m) / s) ** 2) for m, s, w in zip(mus, sds, ws))
    for k, (lab, mus, sds, ws, note_s) in enumerate((
            ('Modelo categorial: dos poblaciones con una zona de rareza', (0.28, 0.76), (0.09, 0.08), (1.0, 0.55),
             'zona de rareza'),
            ('Modelo dimensional: un continuo con umbral convencional', (0.40,), (0.20,), (1.0,), 'umbral convencional'))):
        bt = gt0 + 158 + 158 * k
        ht = 92.0
        it.append(text(gx0 + 18, bt - ht - 14, lab, 'Roboto-Medium', 11, INK))
        xs = [px0 + (px1 - px0) * i / 80.0 for i in range(81)]
        vals = [dens(i / 80.0, mus, sds, ws) for i in range(81)]
        vm = max(vals)
        tops = [bt - ht * v / vm for v in vals]
        curve(it, xs, tops, PURPLE if k == 0 else TEAL, lw=2.2, fill=PURPLE if k == 0 else TEAL, base_top=bt)
        it.append(line_top(px0, bt, px1, bt, stroke=GRAY, lw=1.0))
        if k == 0:
            xr = px0 + (px1 - px0) * 0.56
            it.append(rect_top(xr - 22, bt - ht, xr + 22, bt, 0, fill=OCHRE, alpha=0.18))
            ctext(it, xr, bt - ht - 2, note_s, 'Roboto-Medium', 9.5, OCHRE)
        else:
            xr = px0 + (px1 - px0) * 0.70
            it.append(line_top(xr, bt - ht - 6, xr, bt, stroke=INK, lw=1.2, dash=([5.0, 3.0], 0.0)))
            it.append(text(xr + 6, bt - ht + 6, note_s, 'Roboto-Medium', 9.5, INK))
            it.append(text(xr + 6, bt - ht + 20, '(decisión, no frontera natural)', 'Roboto-Regular', 9, GRAY))
        it.append(text(px0, bt + 14, 'menos síntomas', 'Roboto-Regular', 9, GRAY))
        it.append(text(px1 - sw('más síntomas', 'Roboto-Regular', 9), bt + 14, 'más síntomas', 'Roboto-Regular', 9, GRAY))
    it.append(text(gx0 + 18, gt1 - 12, 'G · Curvas ilustrativas, no ajustadas a datos.', 'Roboto-Regular', 9.5, GRAY))
    # barras de Haslam
    bt0 = gt1 + 14
    bt1 = max(top - 14, bt0 + 150)
    panel(it, gx0, bt0, gx1, bt1, 'Hallazgos taxónicos (P73)', accent=TEAL)
    hbars(it, gx0 + 18, bt0 + 64, 34.0, [('Publicados', 38.9, '38,9 %'), ('Estimación corregida', 14.0, '14 %')],
          45.0, 6.0, 140.0, color=TEAL, lsize=11)
    lines_block(it, gx0 + 18, bt0 + 120, ['Proporción de resultados compatibles con un taxón, antes y',
                                           'después de controlar los factores metodológicos.'], size=10.5)
    top = max(top, bt1 + 14)
    note(it, 50, top, 1141, 'I · Consecuencia para el atlas', [
        'La geometría del atlas trata las variables clínicas como continuas y superpone a ellas los umbrales formales de DSM-5-TR e '
        'ICD-11 (F), que son decisiones convencionales y no fronteras descubiertas. Mantener las categorías se justifica por su utilidad '
        'clínica (P72), no por una supuesta discontinuidad natural que, en los trastornos del ánimo, no se ha demostrado (P73).'],
         kind='info', where='p49')
    return it


# ------------------------------------------------------------------ 50
def p50():
    n = 50
    it = new_page('El modelo ACE: actividad, cognición y emoción', 'NOSOLOGÍA · ACE',
                  'H · modelo de Malhi et al. (P75, P76) | E · antecedente histórico (P74) | I · correspondencias con el atlas | G · diagrama', n)
    subtitle(it, 'Una propuesta para devolver especificidad al diagnóstico: describir cada trastorno del ánimo en tres dominios que cambian con el tiempo.')
    left = (50.0, 600.0)
    top = 130.0
    top = card(it, left[0], top, left[1], title='El problema que intenta resolver', pill='H · P75', body=[
        'Malhi y colaboradores parten de una constatación: el tratamiento de los trastornos del ánimo sigue siendo subóptimo, en '
        'gran parte porque no se comprende bien la fisiopatología de la depresión y del trastorno bipolar, y el problema central es '
        'la falta de especificidad de los diagnósticos actuales. Revisan las obras históricas que fundaron la nosología afectiva y '
        'las influencias recientes que dieron forma a los diagnósticos modernos, y examinan la evidencia de que estos trastornos '
        'tienen perfiles de síntomas multidimensionales y longitudinales.'], where='p50', bsize=12, lead=17.6) + 14
    top = card(it, left[0], top, left[1], title='La propuesta', pill='H · P75 · P76', body=[
        'El modelo ACE considera cada trastorno del ánimo como una combinación de síntomas en tres dominios, actividad (A), cognición '
        '(C) y emoción (E), que varían a lo largo del tiempo. Cada dominio cambia de forma independiente y puede hacerlo en '
        'direcciones distintas, hacia la excitación o hacia la inhibición (P76). Esta perspectiva multidimensional y longitudinal '
        'es coherente con la frecuencia de presentaciones complejas, como los estados mixtos, y subraya la importancia de la '
        'recurrencia (P75).',
        'Los autores proponen caracterizar a cada paciente desde varias perspectivas igualmente importantes para añadir '
        'especificidad al tratamiento.'], where='p50', bsize=12, lead=17.6) + 14
    top = card(it, left[0], top, left[1], title='Un antecedente de hace más de un siglo', pill='E · P74', body=[
        'La monografía de Wilhelm Weygandt sobre los estados mixtos, nacida en la clínica de Kraepelin en Heidelberg, describió '
        'estados mixtos de ánimo, conducta y pensamiento. Kraepelin le reconoció en la sexta edición de su tratado (1899) la nueva '
        'sección sobre estados mixtos, y la idea de que una misma persona puede estar maníaca y deprimida no solo en momentos '
        'distintos, sino a la vez, pudo contribuir a la concepción unitaria de la enfermedad maníaco-depresiva.'],
        where='p50', bsize=12, lead=17.6) + 14
    # diagrama triangular
    gx0, gx1, gt0 = 622.0, 1141.0, 130.0
    gt1 = 560.0
    panel(it, gx0, gt0, gx1, gt1, 'Tres dominios, dos direcciones en cada uno', accent=PURPLE)
    cx, ct = (gx0 + gx1) / 2, 338.0
    R = 96.0
    pts = {}
    for key, ang, lab, hist in (('A', 90, 'Actividad', 'conducta'), ('C', 210, 'Cognición', 'pensamiento'),
                                ('E', 330, 'Emoción', 'ánimo')):
        a = math.radians(ang)
        pts[key] = (cx + R * math.cos(a), ct - R * math.sin(a), lab, hist)
    for k1, k2 in (('A', 'C'), ('C', 'E'), ('E', 'A')):
        x1, t1 = pts[k1][:2]
        x2, t2 = pts[k2][:2]
        it.append(line_top(x1, t1, x2, t2, stroke=LINE, lw=2.0, dash=([4.0, 3.0], 0.0)))
    for key, (x, t, lab, hist) in pts.items():
        col = SOFT[key]
        dot(it, x, t, 27, WHITE, stroke=col, lw=2.4)
        ctext(it, x, t + 8, key, 'Roboto-Bold', 22, col)
        lt = t - 52 if key == 'A' else t + 46
        ctext(it, x, lt, lab, 'Roboto-Bold', 12, col)
        ctext(it, x, lt + 15, 'Weygandt: %s (I)' % hist, 'Roboto-Regular', 9.5, GRAY)
    # ejes de excitación / inhibición
    for k, key in enumerate(('A', 'C', 'E')):
        yb = gt1 - 78 + 22 * k
        col = SOFT[key]
        it.append(text(gx0 + 22, yb + 4, key, 'Roboto-Bold', 12, col))
        xa, xb = gx0 + 150, gx1 - 150
        arrow(it, xa, yb, xb, yb, color=col, lw=1.6, head=7, both=True)
        it.append(text(gx0 + 44, yb + 4, 'inhibición', 'Roboto-Regular', 10, INK))
        it.append(text(xb + 12, yb + 4, 'excitación', 'Roboto-Regular', 10, INK))
    it.append(text(gx0 + 22, gt1 - 14, 'G · El triángulo solo agrupa los dominios; no representa magnitudes ni distancias.',
                   'Roboto-Regular', 9.5, GRAY))
    top = max(top, gt1 + 14)
    note(it, 50, top, 1141, 'I · Correspondencia con el atlas', [
        'Las láminas del atlas separan un panel de síntomas depresivos y otro de activación; ACE descompone ese espacio en tres '
        'dominios y añade la dirección de cada uno. Leídas con ACE, las curvas de depresión y de activación resumen la emoción y la '
        'actividad, mientras que la cognición queda implícita. La equivalencia ánimo-emoción, conducta-actividad y pensamiento-'
        'cognición con Weygandt es una lectura del atlas (I), no una tabla de los autores.'], kind='info', where='p50')
    return it


# ------------------------------------------------------------------ 51
def p51():
    n = 51
    it = new_page('Estados mixtos en ACE: dominios fuera de sincronía', 'NOSOLOGÍA · ACE · MIXTICIDAD',
                  'H · P76 | G · combinatoria derivada del modelo y curso ilustrativo | I · relación con pp. 16, 29 y 35', n)
    subtitle(it, 'Si cada dominio puede moverse por su cuenta, el estado mixto deja de ser una rareza y pasa a ser una combinación esperable.')
    top = 130.0
    top = card_row(it, [
        dict(title='Por qué reformular los estados mixtos', pill='H · P76', body=[
            'Según Malhi y colaboradores, la conceptualización actual, síntomas maníacos y depresivos concurrentes, no hace avanzar el '
            'conocimiento ni orienta la práctica: el DSM-5 ya no permite codificar episodios mixtos y el especificador «con '
            'características mixtas» no capta las presentaciones mixtas más comunes. La investigación sobre su naturaleza es escasa '
            'y la mayoría de las guías no ofrecen recomendaciones para su manejo.']),
        dict(title='La explicación que propone ACE', pill='H · P76', body=[
            'Al descomponer el trastorno en dominios, el estado mixto se explica como el producto de dominios que varían «fuera de '
            'sincronía». En la mayoría de los casos su etiología es desconocida (estados mixtos idiopáticos), pero los autores '
            'describen tres causas que conviene considerar: las transiciones entre polos, la ciclación ultradiana y los virajes '
            'afectivos emergentes con el tratamiento. Recomiendan vigilar los dominios ACE y el funcionamiento.']),
    ], top, X2, where='p51', bsize=12, lead=17.6) + 14
    # combinatoria
    t0, t1 = top, top + 196
    panel(it, 50, t0, 1141, t1, 'Ocho combinaciones posibles con dos direcciones por dominio', accent=PURPLE)
    combos = [(-1, -1, -1), (+1, -1, -1), (-1, +1, -1), (-1, -1, +1), (+1, +1, -1), (+1, -1, +1), (-1, +1, +1), (+1, +1, +1)]
    x0, w = 230.0, 112.0
    for r, key in enumerate(('A', 'C', 'E')):
        yb = t0 + 74 + 32 * r
        it.append(text(68, yb + 5, {'A': 'Actividad', 'C': 'Cognición', 'E': 'Emoción'}[key], 'Roboto-Medium', 11.5, SOFT[key]))
        it.append(line_top(200, yb + 16, 1120, yb + 16, stroke=LINE, lw=0.6))
    for c, cb in enumerate(combos):
        cx = x0 + w * c
        if c in (0, 7):
            it.append(rect_top(cx - 46, t0 + 46, cx + 46, t0 + 170, 8, fill=PILLFILL))
        for r, v in enumerate(cb):
            yb = t0 + 74 + 32 * r
            tri(it, cx, yb, 8.5, v > 0, RED if v > 0 else BLUE)
        lab = {0: 'depresión', 7: 'manía'}.get(c, 'mixta %d' % c)
        ctext(it, cx, t0 + 164, lab, 'Roboto-Bold' if c in (0, 7) else 'Roboto-Medium', 10.5,
              NAVY if c in (0, 7) else PURPLE)
    tri(it, 74, t1 - 16, 6, True, RED)
    it.append(text(86, t1 - 12, 'excitación', 'Roboto-Regular', 10, INK))
    tri(it, 168, t1 - 16, 6, False, BLUE)
    it.append(text(180, t1 - 12, 'inhibición', 'Roboto-Regular', 10, INK))
    it.append(text(270, t1 - 12, 'G · Combinatoria binaria derivada de la descripción del modelo (dos direcciones por dominio); los '
                   'autores no publican esta tabla ni nombran las seis formas mixtas.', 'Roboto-Regular', 10, GRAY))
    top = t1 + 14
    # curso: transición fuera de sincronía
    c0, c1 = top, top + 214
    panel(it, 50, c0, 700, c1, 'Una transición en la que los dominios cambian a destiempo', accent=TEAL)
    xs = [80 + 590 * i / 40.0 for i in range(41)]
    mid = c0 + 112

    def sig(i, center, sign):
        return mid - sign * 46 * math.tanh((i - center) / 3.2)
    curve(it, xs, [sig(i, 15, 1) for i in range(41)], SOFT['A'], lw=2.4)
    curve(it, xs, [sig(i, 21, 1) for i in range(41)], SOFT['E'], lw=2.4)
    curve(it, xs, [sig(i, 27, 1) for i in range(41)], SOFT['C'], lw=2.4)
    it.append(line_top(80, mid, 670, mid, stroke=GRAY, lw=0.8, dash=([3.0, 3.0], 0.0)))
    it.append(text(84, mid - 52, 'excitación', 'Roboto-Regular', 9.5, GRAY))
    it.append(text(84, mid + 60, 'inhibición', 'Roboto-Regular', 9.5, GRAY))
    xa, xb = xs[15], xs[27]
    it.append(rect_top(xa, c0 + 52, xb, c1 - 34, 0, fill=PURPLE, alpha=0.10))
    ctext(it, (xa + xb) / 2, c0 + 48, 'ventana mixta', 'Roboto-Medium', 10, PURPLE)
    for k, (key, lab) in enumerate((('A', 'actividad'), ('E', 'emoción'), ('C', 'cognición'))):
        it.append(rect_top(470 + 72 * k, c1 - 27, 486 + 72 * k, c1 - 23, 1, fill=SOFT[key]))
        it.append(text(490 + 72 * k, c1 - 21, lab, 'Roboto-Regular', 9.5, INK))
    it.append(text(68, c1 - 12, 'G · De la inhibición a la excitación: cada dominio cruza en un momento distinto.',
                   'Roboto-Regular', 9.5, GRAY))
    note(it, 722, c0, 1141, 'I · Dónde se cruza con el atlas', [
        'La ventana mixta de una transición enlaza con la mixticidad según definiciones (p. 29), la ciclación ultradiana con la '
        'ciclación rápida (p. 16) y los virajes emergentes con el tratamiento con la lámina 13 (p. 35).',
        'ACE no sustituye los criterios formales: ofrece un lenguaje para describir lo que esos criterios dejan fuera.'],
         kind='info', t1=c1, where='p51')
    return it


# ------------------------------------------------------------------ 52
def p52():
    n = 52
    it = new_page('El espectro bipolar: prototipos y prevalencias', 'NOSOLOGÍA · ESPECTRO',
                  'H · propuesta de Akiskal y Pinto (P77) | E · cohorte de Zúrich (P78) | G · banda continua | I · relación con pp. 26 y 30', n)
    subtitle(it, 'Entre la normalidad y el trastorno bipolar I hay un territorio extenso; su anchura depende de cómo se defina la hipomanía.')
    top = 130.0
    top = card_row(it, [
        dict(title='Una vuelta parcial a Kraepelin', pill='H · P77', body=[
            'Akiskal y Pinto defienden un retorno parcial al concepto amplio de enfermedad maníaco-depresiva de Kraepelin y proponen '
            'definiciones, ilustradas con casos prototípicos, para los subtipos bipolares I a IV. Reconocen que, aunque una evidencia '
            'considerable apoya extender la bipolaridad sobre el territorio del trastorno depresivo mayor, hace falta más '
            'investigación.',
            'Su razón práctica es terapéutica: la utilidad de los estabilizadores del ánimo en depresiones con rasgos bipolares '
            'suaves que no alcanzan los criterios estrictos de bipolar II e hipomanía del DSM-IV y la ICD-10.']),
        dict(title='Redefinir la bipolaridad subumbral', pill='E · H · P78', body=[
            'Angst y colaboradores analizaron 20 años de seguimiento prospectivo de una cohorte comunitaria de adultos jóvenes en '
            'Zúrich. Proponen incluir la hiperactividad en el criterio principal de la hipomanía, junto a la euforia y la '
            'irritabilidad; no exigir una duración mínima del episodio si están presentes tres de siete síntomas, y mantener como '
            'obligatorio el cambio en el funcionamiento.',
            'Por debajo de ese umbral, los síntomas hipomaníacos aislados asociados a depresión mayor o leve serían indicadores '
            'importantes de bipolaridad. Los autores piden confirmar las cifras en una cohorte nacional mayor.']),
    ], top, X2, where='p52', bsize=12, lead=17.6) + 14
    # barras de prevalencia (P78)
    t0, t1 = top, top + 296
    panel(it, 50, t0, 640, t1, 'Prevalencias acumuladas en la cohorte de Zúrich (P78)', accent=TEAL)
    rows = [('Espectro depresivo completo', 24.6, '24,6 %'), ('Espectro bipolar suave completo', 23.7, '23,7 %'),
            ('Depresión mayor, definición amplia', 11.4, '11,4 %'), ('Bipolar II, definición amplia', 10.9, '10,9 %'),
            ('Trastorno bipolar menor', 9.4, '9,4 %'), ('Hipomanía pura', 3.3, '3,3 %'), ('Ciclotimia', 2.0, '2,0 %')]
    cols = [BLUE, RED, BLUE, RED, RED, RED, RED]
    for k, ((lab, v, vt), col) in enumerate(zip(rows, cols)):
        yb = t0 + 62 + 28 * k
        it.append(text(68, yb, lab, 'Roboto-Regular', 11, INK))
        xb = 300.0
        it.append(rect_top(xb, yb - 11.5, xb + v * 11.5, yb + 3, 2, fill=col))
        it.append(text(xb + v * 11.5 + 6, yb, vt, 'Roboto-Medium', 10.5, INK))
    it.append(line_top(300, t0 + 44, 300, t0 + 62 + 28 * 6 + 8, stroke=LINE, lw=1.0))
    lines_block(it, 68, t1 - 28, ['E · Según el resumen, el 2,0 % correspondía a ciclotimia dentro del grupo bipolar menor.',
                                  'Azul: espectro depresivo; rojo: espectro bipolar.'], size=9.5, lead=13)
    # banda continua
    gx0 = 662.0
    panel(it, gx0, t0, 1141, t1, 'De la normalidad a la bipolaridad propiamente dicha', accent=RED)
    bx0, bx1, bt = gx0 + 26, 1141 - 26, t0 + 100
    nseg = 60
    for i in range(nseg):
        f = i / (nseg - 1)
        col = (0.95 - 0.23 * f, 0.93 - 0.55 * f, 0.90 - 0.62 * f)
        xa = bx0 + (bx1 - bx0) * i / nseg
        it.append(rect_top(xa, bt, xa + (bx1 - bx0) / nseg + 0.5, bt + 34, 0, fill=col))
    it.append(rect_top(bx0, bt, bx1, bt + 34, 4, stroke=LINE, lw=1.0))
    for f, lab in ((0.0, 'normalidad'), (1.0, 'bipolar I')):
        x = bx0 + (bx1 - bx0) * f
        s = lab
        it.append(text(min(max(x - sw(s, 'Roboto-Medium', 10.5) / 2, bx0), bx1 - sw(s, 'Roboto-Medium', 10.5)), bt - 8, s,
                       'Roboto-Medium', 10.5, INK))
    segs = [(0.30, 0.62, 'cerca del 13 %: expresión más suave', 'intermedia entre trastorno y normalidad'),
            (0.62, 0.98, 'casi el 11 %: espectro de', 'trastornos bipolares propiamente dichos')]
    for k, (a, bnd, l1, l2) in enumerate(segs):
        xa, xb = bx0 + (bx1 - bx0) * a, bx0 + (bx1 - bx0) * bnd
        it.append(line_top(xa, bt + 46, xb, bt + 46, stroke=INK, lw=1.2))
        for xe in (xa, xb):
            it.append(line_top(xe, bt + 41, xe, bt + 51, stroke=INK, lw=1.2))
        if k == 0:
            it.append(text(xa, bt + 68, l1, 'Roboto-Medium', 10.5, INK))
            it.append(text(xa, bt + 82, l2, 'Roboto-Regular', 10, GRAY))
        else:
            it.append(text(xb - sw(l1, 'Roboto-Medium', 10.5), bt + 108, l1, 'Roboto-Medium', 10.5, INK))
            it.append(text(xb - sw(l2, 'Roboto-Regular', 10), bt + 122, l2, 'Roboto-Regular', 10, GRAY))
    lines_block(it, gx0 + 18, t1 - 42, ['E · Proporciones de la conclusión de P78 sobre el 23,7 % del espectro suave.',
                                        'G · Posición de los tramos en la banda ilustrativa, no proporcional.'], size=9.5, lead=13)
    top = t1 + 14
    note(it, 50, top, 1141, 'I · Por qué importa la definición de hipomanía', [
        'La prevalencia de la bipolaridad crece o se contrae según los criterios de hipomanía: duración, síntoma principal y número de '
        'síntomas. El atlas registra por separado la hipomanía que cumple criterios formales y los síntomas subumbrales (pp. 22 y 30); los '
        'cribados de la p. 26 no sustituyen esa distinción. Los subtipos de Akiskal se citan como propuesta (H), no como categorías '
        'oficiales.'], where='p52')
    return it


# ------------------------------------------------------------------ 53
def p53():
    n = 53
    it = new_page('Modelos jerárquicos: HiTOP y el factor p', 'NOSOLOGÍA · TRANSDIAGNÓSTICO',
                  'E · H · P79, P80 | G · árbol esquemático | I · los resúmenes no sitúan los trastornos del ánimo', n)
    subtitle(it, 'En lugar de cajas yuxtapuestas, una jerarquía de dimensiones construida a partir de cómo se agrupan los síntomas en la población.')
    left = (50.0, 560.0)
    top = 130.0
    top = card(it, left[0], top, left[1], title='Los límites de las taxonomías tradicionales', pill='E · H · P79', body=[
        'Kotov y colaboradores atribuyen la fiabilidad y la validez limitadas de las taxonomías tradicionales a cinco problemas: '
        'fronteras arbitrarias entre psicopatología y normalidad, fronteras poco claras entre trastornos, coocurrencia frecuente, '
        'heterogeneidad dentro de cada trastorno e inestabilidad diagnóstica. Esas taxonomías fueron más allá de la evidencia sobre '
        'la estructura de la psicopatología y se moldearon por otras consideraciones.'], where='p53', bsize=12, lead=17.6) + 14
    top = card(it, left[0], top, left[1], title='Cómo se construye HiTOP', pill='E · H · P79', body=[
        'HiTOP agrupa los síntomas que covarían para formar componentes y síndromes, lo que reduce la heterogeneidad; reúne los '
        'síndromes que coocurren en espectros, lo que cartografía la comorbilidad, y describe todo ello de forma dimensional, lo que '
        'aborda los problemas de frontera y de inestabilidad. Cubre ya la mayor parte de la psicopatología y varios dominios están '
        'listos para la clínica y la investigación, aunque sigue siendo un trabajo en curso.'], where='p53', bsize=12, lead=17.6) + 14
    top = card(it, left[0], top, left[1], title='El factor p', pill='E · P80', body=[
        'En la cohorte de Dunedin, seguida durante 20 años desde la adolescencia hasta la mediana edad, los trastornos se explicaban '
        'primero con tres factores de orden superior (internalizante, externalizante y trastorno del pensamiento), pero mejor aún con '
        'una sola dimensión general de psicopatología, el factor p. Puntuaciones más altas se asociaron con más deterioro, mayor '
        'agregación familiar, peores historias del desarrollo y una función cerebral temprana más comprometida.'],
        where='p53', bsize=12, lead=17.6) + 14
    # árbol
    gx0, gx1, gt0 = 582.0, 1141.0, 130.0
    gt1 = top - 14
    panel(it, gx0, gt0, gx1, gt1, 'Una jerarquía de dimensiones', accent=PURPLE)
    levels = [('dimensión general', 180.0), ('espectros', 268.0), ('síndromes', 356.0), ('componentes', 444.0),
              ('síntomas', 524.0)]
    for lab, t in levels:
        it.append(text(gx0 + 18, t + 4, lab, 'Roboto-Regular', 9.5, GRAY))
        it.append(line_top(gx0 + 110, t, gx1 - 18, t, stroke=LINE, lw=0.5, dash=([2.0, 3.0], 0.0)))

    def box(cx, t, s, w=None, fill=WHITE, stroke=PURPLE, font='Roboto-Medium', size=10.5, color=INK):
        w = w or sw(s, font, size) + 20
        it.append(rect_top(cx - w / 2, t - 13, cx + w / 2, t + 13, 6, fill=fill, stroke=stroke, lw=1.2))
        ctext(it, cx, t + 4, s, font, size, color)
        return w
    cxm = (gx0 + 110 + gx1 - 18) / 2
    box(cxm, 180, 'factor p (P80)', fill=(0.93, 0.91, 0.95), font='Roboto-Bold')
    sp = [(cxm - 150, 'internalizante'), (cxm, 'externalizante'), (cxm + 150, 'trastorno del pensamiento')]
    for x, s in sp:
        it.append(line_top(cxm, 193, x, 255, stroke=PURPLE, lw=1.0))
        box(x, 268, s, size=10)
    # niveles inferiores genéricos
    for x, _ in sp:
        for dx in (-34, 34):
            it.append(line_top(x, 281, x + dx, 343, stroke=LINE, lw=1.0))
            box(x + dx, 356, 'síndrome', w=62, stroke=LINE, font='Roboto-Regular', size=9, color=GRAY)
            for ddx in (-14, 14):
                it.append(line_top(x + dx, 369, x + dx + ddx, 437, stroke=LINE, lw=0.8))
                dot(it, x + dx + ddx, 444, 5, WHITE, stroke=GRAY, lw=1.0)
                for d3 in (-6, 0, 6):
                    it.append(line_top(x + dx + ddx, 449, x + dx + ddx + d3, 518, stroke=LINE, lw=0.5))
    lines_block(it, gx0 + 18, gt1 - 40, ['E · Los tres espectros y el factor general proceden de P80; los niveles inferiores son',
                                          'genéricos (G). Los resúmenes de P79 y P80 no sitúan la depresión ni la manía:',
                                          'el atlas no las coloca en el árbol.'], size=9.5, lead=13)
    note(it, 50, top, 1141, 'I · Qué aporta y qué no aporta al clínico del ánimo', [
        'La jerarquía explica por qué la comorbilidad es la regla y por qué es difícil hallar causas, biomarcadores y tratamientos '
        'específicos de un trastorno (P80). No describe el curso episódico ni la polaridad, que son el eje del atlas; por eso aquí se '
        'presenta como marco estructural complementario y no como sustituto de las láminas longitudinales.'], kind='info', where='p53')
    return it


# ------------------------------------------------------------------ 54
def p54():
    n = 54
    it = new_page('RDoC y estadificación clínica', 'NOSOLOGÍA · MECANISMO Y CURSO',
                  'E · H · P81 (marco de investigación) | H · P82 (modelo de estadios) | G · diagramas esquemáticos', n)
    subtitle(it, 'Dos propuestas que miran fuera del síndrome actual: una hacia los sistemas biocomportamentales, otra hacia la progresión.')
    top = 130.0
    t1 = card(it, 50, top, 560, title='Research Domain Criteria', pill='E · H · P81', body=[
        'El Instituto Nacional de Salud Mental de Estados Unidos inició en 2009 el proyecto RDoC para desarrollar una clasificación de '
        'investigación basada en dimensiones de neurobiología y de conducta observable. Parte de que los sistemas actuales, apoyados '
        'en signos y síntomas, no reflejan adecuadamente los sistemas neurobiológicos y conductuales pertinentes, lo que dificulta '
        'investigar la etiología y desarrollar tratamientos nuevos.',
        'RDoC fomenta el estudio de dimensiones que atraviesan las categorías heterogéneas actuales. Cuthbert e Insel señalan siete '
        'diferencias de concepción respecto de las nosologías vigentes y presentan el proyecto como un marco para la investigación, '
        'no como un sistema diagnóstico clínico.'], where='p54', bsize=12, lead=17.6)
    # diagrama RDoC
    gx0 = 582.0
    panel(it, gx0, top, 1141, t1, 'Categorías atravesadas por dimensiones', accent=PURPLE)
    cats = ['categoría A', 'categoría B', 'categoría C', 'categoría D']
    cw = (1141 - gx0 - 60) / 4.0
    ct0, ct1 = top + 48, t1 - 30
    for k, c in enumerate(cats):
        xa = gx0 + 30 + cw * k + 6
        it.append(rect_top(xa, ct0, xa + cw - 12, ct1, 6, fill=(0.97, 0.96, 0.93), stroke=LINE, lw=1.0))
        ctext(it, xa + (cw - 12) / 2, ct0 + 18, c, 'Roboto-Medium', 10, GRAY)
    span = ct1 - ct0 - 40
    for k, (col, a, bnd) in enumerate(((TEAL, 0, 4), (BLUE, 1, 4), (OCHRE, 0, 3))):
        yb = ct0 + 40 + span * (k + 0.5) / 3
        xa = gx0 + 30 + cw * a + 14
        xb = gx0 + 30 + cw * bnd - 14
        arrow(it, xa, yb, xb, yb, color=col, lw=5.0, head=10, both=True)
        it.append(text(xa + 6, yb - 9, 'dimensión biocomportamental %d' % (k + 1), 'Roboto-Medium', 9.5, col))
    it.append(text(gx0 + 18, t1 - 12, 'G · Categorías y dimensiones genéricas; no reproduce la matriz de RDoC.', 'Roboto-Regular',
                   9.5, GRAY))
    top = t1 + 14
    # estadificación
    s0, s1 = top, top + 268
    panel(it, 50, s0, 1141, s1, 'Estadificación del trastorno bipolar según Kapczinski y colaboradores (P82)', accent=TEAL)
    stages = [('Latente', 'síntomas afectivos o ansiosos y mayor', 'riesgo de un trastorno bipolar umbral'),
              ('Estadio I', 'eutimia bien establecida entre episodios,', 'sin morbilidad manifiesta'),
              ('Estadio II', 'ciclación rápida o comorbilidad actual', 'de los ejes I o II'),
              ('Estadio III', 'deterioro cognitivo y funcional', 'relevante; biomarcadores alterados'),
              ('Estadio IV', 'incapacidad para vivir de forma autónoma;', 'neuroimagen y biomarcadores alterados')]
    sw_ = (1141 - 50 - 56) / 5.0
    base = s1 - 34
    for k, (lab, l1, l2) in enumerate(stages):
        xa = 78 + sw_ * k
        h = 42 + 26 * k
        shade = (0.86 - 0.10 * k, 0.93 - 0.08 * k, 0.92 - 0.07 * k)
        it.append(rect_top(xa, base - h, xa + sw_ - 8, base, 4, fill=shade, stroke=TEAL, lw=1.0))
        it.append(text(xa + 10, base - h + 20, lab, 'Roboto-Bold', 12, NAVY))
        it.append(text(xa + 2, base - h - 30, l1, 'Roboto-Regular', 9.5, INK))
        it.append(text(xa + 2, base - h - 16, l2, 'Roboto-Regular', 9.5, INK))
    it.append(text(68, s1 - 12, 'H · Modelo propuesto; la altura creciente solo ordena los estadios. El modelo pone el acento en la '
                   'evaluación entre episodios.', 'Roboto-Regular', 9.5, GRAY))
    top = s1 + 14
    card_row(it, [
        dict(title='I · Qué aporta la estadificación', body=[
            'Obliga a una valoración longitudinal de variables clínicas, de la neurocognición y de los biomarcadores en el periodo '
            'intercrisis, y subraya, según sus autores, la necesidad de intervenir pronto (P82). Enlaza con el residuo entre episodios de la p. 44.']),
        dict(title='I · Cautela', body=[
            'Ambas propuestas son marcos (H): RDoC no está pensado para diagnosticar a un paciente concreto, y los estadios no se han '
            'trasladado aquí a puntos de corte. El atlas los cita para situar sus láminas, no para clasificar.']),
    ], top, X2, where='p54', accent=OCHRE, fill=NOTEFILL, bsize=12, lead=17.4)
    return it


# ------------------------------------------------------------------ 55
def p55():
    n = 55
    it = new_page('Mapa de los modelos y lugar del atlas', 'NOSOLOGÍA · SÍNTESIS',
                  'I · posiciones interpretativas | G · mapa sin escala | remite a pp. 3, 10–18, 40 y 49–54', n)
    subtitle(it, 'Ningún modelo responde a todas las preguntas; situarlos en un mismo plano ayuda a ver qué ilumina cada uno y qué deja en sombra.')
    gx0, gx1, gt0, gt1 = 50.0, 700.0, 130.0, 640.0
    panel(it, gx0, gt0, gx1, gt1, 'Dos ejes: cómo se corta el territorio y qué tiempo se mira', accent=PURPLE)
    ax0, ax1, at0, at1 = gx0 + 70, gx1 - 30, gt0 + 50, gt1 - 60
    for i in range(1, 4):
        it.append(line_top(ax0 + (ax1 - ax0) * i / 4, at0, ax0 + (ax1 - ax0) * i / 4, at1, stroke=LINE, lw=0.5))
        it.append(line_top(ax0, at0 + (at1 - at0) * i / 4, ax1, at0 + (at1 - at0) * i / 4, stroke=LINE, lw=0.5))
    arrow(it, ax0, at1, ax1 + 6, at1, color=INK, lw=1.4)
    arrow(it, ax0, at1, ax0, at0 - 6, color=INK, lw=1.4)
    it.append(text(ax0, at1 + 18, 'categorial', 'Roboto-Medium', 10, INK))
    it.append(text(ax1 - sw('dimensional', 'Roboto-Medium', 10), at1 + 18, 'dimensional', 'Roboto-Medium', 10, INK))
    it.append(text(gx0 + 14, at1 + 4, 'estado', 'Roboto-Medium', 10, INK))
    it.append(text(gx0 + 14, at0 + 4, 'curso', 'Roboto-Medium', 10, INK))

    def place(fx, fy, label, ref, col, r=9, atlas=False, dx=14, dy=4):
        x = ax0 + (ax1 - ax0) * fx
        t = at1 - (at1 - at0) * fy
        if atlas:
            dot(it, x, t, 13, NAVY)
            dot(it, x, t, 6, WHITE)
        else:
            dot(it, x, t, r, col)
        if dx < 0:
            x0 = x + dx - sw(label, 'Roboto-Bold', 11)
            it.append(text(x0, t + dy, label, 'Roboto-Bold', 11, NAVY))
            it.append(text(x + dx - sw(ref, 'Roboto-Regular', 9.5), t + dy + 13, ref, 'Roboto-Regular', 9.5, GRAY))
        else:
            it.append(text(x + dx, t + dy, label, 'Roboto-Bold', 11, NAVY))
            it.append(text(x + dx, t + dy + 13, ref, 'Roboto-Regular', 9.5, GRAY))
    place(0.10, 0.22, 'DSM-5-TR · ICD-11', 'episodios y especificadores (F)', BLUE)
    place(0.12, 0.88, 'Kraepelin', 'enfermedad unitaria (p. 40)', GRAY)
    place(0.24, 0.58, 'Estadificación', 'estadios ordinales (P82)', TEAL)
    place(0.46, 0.74, 'Espectro bipolar', 'P77, P78', RED)
    place(0.84, 0.86, 'ACE', 'tres dominios en el tiempo (P75)', PURPLE, dx=-16)
    place(0.82, 0.20, 'HiTOP · factor p', 'estructura de covariación (P79, P80)', PURPLE, dx=-16)
    place(0.92, 0.42, 'RDoC', 'mecanismos (P81)', OCHRE, dx=-16)
    place(0.64, 0.62, 'Este atlas', 'geometría continua con umbrales F', NAVY, atlas=True, dx=20, dy=4)
    it.append(text(gx0 + 18, gt1 - 14, 'G · I · Posiciones aproximadas y discutibles; el mapa no mide distancias entre modelos.',
                   'Roboto-Regular', 9.5, GRAY))
    # texto lateral
    x0 = 722.0
    top = 130.0
    top = card(it, x0, top, 1141, title='Lo que ilumina cada modelo', body=[
        'Las clasificaciones oficiales ofrecen un lenguaje común y umbrales con valor pronóstico y terapéutico. El espectro bipolar '
        'recupera el territorio subumbral que esos umbrales dejan fuera. ACE describe la dirección de cada dominio y su desfase en el '
        'tiempo. HiTOP y el factor p explican la comorbilidad y la falta de especificidad. RDoC busca mecanismos que crucen las '
        'categorías, y la estadificación ordena la progresión.'], where='p55', bsize=12, lead=17.6) + 12
    top = card(it, x0, top, 1141, title='Por qué el atlas no elige uno solo', body=[
        'El atlas dibuja la clínica afectiva como un espacio continuo, con la polaridad y el curso como ejes, y conserva los criterios '
        'formales como líneas de decisión. Por eso se sitúa entre los modelos dimensionales y longitudinales, pero sin renunciar a la '
        'utilidad de las categorías (P72).'], where='p55', bsize=12, lead=17.6) + 12
    note(it, x0, top, 1141, 'I · Advertencia', [
        'Las posiciones del mapa son una lectura editorial. Otros autores podrían colocar los modelos de otro modo; el mapa sirve para '
        'orientar la lectura, no como resultado empírico.'], kind='info', t1=max(top + 100, gt1), where='p55')
    note(it, 50, gt1 + 14, 1141, 'I · Cómo usar esta ampliación', [
        'Las pp. 49–54 no cambian ningún criterio ni perfil del atlas. Ofrecen el contexto teórico para leer sus láminas: por qué se '
        'dibujan continuos (p. 49), cómo describir lo mixto (pp. 50–51), qué territorio subumbral existe (p. 52) y qué marcos '
        'transdiagnósticos y longitudinales compiten con las categorías (pp. 53–54).'], where='p55')
    return it


NEW_PAGES33 = [p49, p50, p51, p52, p53, p54, p55]

"""Ampliación VII del Atlas v3.7 (pp. 89–102): poblaciones especiales, resistencia, suicidio y genética.

Cifras de resúmenes de PubMed verificados el 19-nov-2026 (refs37.py), más P29, P35, P87 y dosieres
D01–D13 ya citados. Convención F/E/I/H/G. No prescriptivo (p. 20)."""
import math

from layout31 import (new_page, card, card_row, note, hbars, sw, text, rect_top, line_top, path, rrect_ops, PURPLE,
                      OCHRE, PILLFILL, NOTEFILL, INFOFILL, WARN, WHITE, NAVY, INK, GRAY, LINE, TEAL, BLUE, RED, Y,
                      make_sheet)
from pages32 import panel, subtitle, X2, X3
from pages33 import arrow, dot, tri, ctext, curve, lines_block
from pages34 import mark, legend_marks, lforest, dumbbell, axis_ticks, PALE


def vbars(it, x0, base, w, gap, vals, vmax, h, cols, labels, fmt='%g %%', lsize=10):
    for k, (v, c, lab) in enumerate(zip(vals, cols, labels)):
        xa = x0 + k * (w + gap)
        bh = v / vmax * h
        it.append(rect_top(xa, base - bh, xa + w, base, 3, fill=c))
        s = (fmt % v).replace('.', ',')
        ctext(it, xa + w / 2, base - bh - 6, s, 'Roboto-Medium', 10.5, INK)
        for m, ln in enumerate(lab.split('\n')):
            ctext(it, xa + w / 2, base + 15 + 12 * m, ln, 'Roboto-Regular', lsize, INK)
    it.append(line_top(x0 - 6, base, x0 + len(vals) * (w + gap) - gap + 6, base, stroke=GRAY, lw=1.0))


# ------------------------------------------------------------------ 89 · infancia y adolescencia
def p89():
    n = 89
    it = new_page('Infancia y adolescencia', 'POBLACIONES · I',
                  'E · P92, P93 | I · fenotipo pediátrico y definiciones | relación con pp. 16, 52 y 66', n)
    subtitle(it, 'La manía pediátrica existe con una prevalencia comparable entre países; su fenotipo y su tratamiento difieren del adulto.')
    t0, t1 = 128.0, 470.0
    panel(it, 50, t0, 400, t1, 'Prevalencia comunitaria (P93)', accent=TEAL)
    cx, ct = 225.0, t0 + 170
    for r, a in ((95, 0.10), (70, 0.16), (45, 0.30)):
        dot(it, cx, ct, r, TEAL)
        it[-1]['alpha'] = a
    ctext(it, cx, ct + 4, '1,8 %', 'Roboto-Bold', 30, NAVY)
    ctext(it, cx, ct + 26, 'IC 95 % 1,1–3,0', 'Roboto-Medium', 11, INK)
    lines_block(it, 68, t1 - 64, ['12 estudios, 16.222 jóvenes de 7 a 21 años.',
                                   'Sin diferencias entre EE. UU. y otros países ni aumento',
                                   'en el tiempo; las definiciones amplias (bipolar no',
                                   'especificado) dan las cifras más altas.'], size=10, lead=13.5, color=INK)
    gx0 = 422.0
    panel(it, gx0, t0, 1141, t1, 'TEAM: 279 niños y adolescentes de 6 a 15 años sin antimaníacos previos (P92)', accent=RED)
    vbars(it, gx0 + 50, t1 - 70, 70, 26, [68.5, 35.6, 24.0], 80, 210, [RED, BLUE, OCHRE],
          ['Risperidona', 'Litio', 'Divalproato'])
    ctext(it, gx0 + 50 + 135, t0 + 50, 'Respuesta a 8 semanas', 'Roboto-Bold', 11, NAVY)
    fx = gx0 + 380
    it.append(text(fx, t0 + 50, 'Fenotipo de la muestra', 'Roboto-Bold', 11, NAVY))
    feats = [('Ciclación rápida diaria', 99.3), ('Manía mixta', 97.5), ('Psicosis', 77.1)]
    for k, (lab, v) in enumerate(feats):
        yb = t0 + 90 + 52 * k
        it.append(text(fx, yb, lab, 'Roboto-Regular', 10.5, INK))
        it.append(rect_top(fx, yb + 6, fx + 280, yb + 18, 4, fill=PALE))
        it.append(rect_top(fx, yb + 6, fx + 2.8 * v, yb + 18, 4, fill=PURPLE))
        it.append(text(fx + 286, yb + 16, ('%g %%' % v).replace('.', ','), 'Roboto-Medium', 10, INK))
    it.append(text(fx, t0 + 90 + 52 * 3 + 6, 'Duración media de la manía: 4,9 años.', 'Roboto-Regular', 10.5, INK))
    it.append(text(gx0 + 18, t1 - 14, 'E · Risperidona superó a litio y a divalproato (p < 0,001); litio y divalproato no difirieron. '
                   'Niveles medios: litio 1,09 mEq/L; valproato 113,6 µg/mL; risperidona 2,57 mg.', 'Roboto-Regular', 9.2, GRAY))
    top = t1 + 14
    card_row(it, [
        dict(title='El precio metabólico', pill='E · P92', body=[
            'Con risperidona aumentaron el peso, el IMC y la prolactina frente a litio y divalproato; con litio subió la tirotropina y '
            'hubo más abandonos que con risperidona. La eficacia aguda se paga con una carga que pesa más en una vida con décadas de '
            'tratamiento por delante (pp. 66 y 77).']),
        dict(title='I · Lectura en el atlas', body=[
            'La muestra TEAM es extrema (ciclación diaria casi universal, psicosis en tres de cada cuatro): sus resultados no se trasladan '
            'a la adolescencia con episodios definidos. La anchura de la definición explica gran parte de la variación de prevalencias, '
            'como en el espectro adulto (p. 52). Lámina 25 en la p. 93.']),
    ], top, X2, where='p89', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 90 · mayores
def p90():
    n = 90
    it = new_page('Edad avanzada: manía en mayores de 60 años', 'POBLACIONES · II',
                  'E · P94 | E · D01, D11 (exposición en mayores) | I · riñón, interacciones y polifarmacia', n)
    subtitle(it, 'El primer ensayo aleatorizado específico de la manía tardía comparó litio y divalproato a concentraciones dirigidas.')
    t0, t1 = 128.0, 470.0
    panel(it, 50, t0, 760, t1, 'GERI-BD: 224 pacientes de 60 años o más, 9 semanas, doble ciego (P94)', accent=NAVY)
    rows = [('Respuesta a 9 semanas', 79, 73), ('Alcanzan la concentración diana', 57, 56), ('Abandono a la semana 9', 51, 44),
            ('Necesitan risperidona añadida', 17, 14)]
    x0, x1 = 360.0, 700.0
    pos = None
    for k, (lab, a, b) in enumerate(rows):
        yb = t0 + 82 + 52 * k
        it.append(text(68, yb + 4, lab, 'Roboto-Regular', 11, INK))
        pos = dumbbell(it, x0, x1, yb, 0, 100, a, b, BLUE, OCHRE)
        it.append(text(pos(a) - sw('%d %%' % a, 'Roboto-Medium', 9.5) / 2, yb - 10, '%d %%' % a, 'Roboto-Medium', 9.5, BLUE))
        it.append(text(pos(b) - sw('%d %%' % b, 'Roboto-Medium', 9.5) / 2, yb + 20, '%d %%' % b, 'Roboto-Medium', 9.5, OCHRE))
    axis_ticks(it, pos, [0, 25, 50, 75, 100], t0 + 56, t0 + 82 + 52 * 3 + 30, suffix='')
    dot(it, 70, t1 - 30, 5, BLUE)
    it.append(text(80, t1 - 26, 'litio (0,80–0,99 mEq/L)', 'Roboto-Regular', 10, INK))
    dot(it, 240, t1 - 30, 5, OCHRE)
    it.append(text(250, t1 - 26, 'divalproato (80–99 µg/mL)', 'Roboto-Regular', 10, INK))
    it.append(text(68, t1 - 10, 'E · Ninguna diferencia de proporciones fue significativa; la sedación no difirió y el litio dio más temblor.',
                   'Roboto-Regular', 9.2, GRAY))
    t = card(it, 782, t0, 1141, title='Cambio en YMRS', pill='E · P94', body=[
        'El modelo longitudinal favoreció al litio: 3,90 puntos de diferencia (IC 97,5 % 1,71–6,09). Ambos fármacos fueron tolerados y '
        'eficaces.'], where='p90', bsize=11.5, lead=16.6) + 12
    card(it, 782, t, 1141, t1=t1, title='Exposición en mayores', pill='E · D11 · D01', body=[
        'Asenapina: exposición un 30 % mayor entre 65 y 85 años [D11 · R1]. Litio: eliminación renal; tiazidas, IECA, ARA-II y AINE, '
        'frecuentes en esta edad, elevan la litemia [D01 · R1–R2] (p. 65).'], where='p90', bsize=11.5, lead=16.6)
    top = t1 + 14
    card_row(it, [
        dict(title='I · Por qué importa un ensayo propio', body=[
            'Los ensayos de manía en adultos excluyen o infrarrepresentan a los mayores. GERI-BD muestra que ambos estabilizadores son '
            'utilizables a concentraciones dirigidas, con abandono alto a las nueve semanas en los dos brazos, lo que obliga a planificar '
            'la tolerancia desde el inicio.']),
        dict(title='I · Qué vigilar', body=[
            'Función renal y tiroidea, sodio, interacciones y caídas por temblor, sedación u ortostatismo; la manía de inicio tardío exige '
            'además descartar causas médicas y neurológicas (p. 36). Lámina 26 en la p. 94.']),
    ], top, X2, where='p90', accent=OCHRE, fill=NOTEFILL, bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 91 · embarazo y lactancia
def p91():
    n = 91
    it = new_page('Embarazo y lactancia: litio y antipsicóticos', 'POBLACIONES · III',
                  'E · P95, P96, P109 | complementa la p. 68 (valproato, carbamazepina, lamotrigina) y las pp. 32–33', n)
    subtitle(it, 'Los datos que los dosieres no cubrían: malformaciones, morbilidad neonatal y exposición del lactante.')
    t0, t1 = 128.0, 480.0
    panel(it, 50, t0, 760, t1, 'Riesgo frente a gestaciones no expuestas con trastorno del ánimo o psiquiátrico · escala log', accent=RED)
    rows = [('Litio 1.er trim. · malformaciones mayores', 1.71, 1.07, 2.72, RED),
            ('Litio 1.er trim. · malformaciones cardiacas', 1.54, 0.64, 3.70, GRAY),
            ('Litio · reingreso neonatal ≤ 28 días', 1.62, 1.12, 2.33, RED),
            ('Antipsicóticos atípicos · bruto', 1.36, 1.24, 1.50, GRAY),
            ('Antipsicóticos atípicos · ajustado', 1.05, 0.96, 1.16, TEAL),
            ('Antipsicóticos típicos · ajustado', 0.90, 0.62, 1.31, TEAL),
            ('Risperidona · ajustado', 1.26, 1.02, 1.56, OCHRE)]
    lforest(it, 380, 640, t0 + 66, 34.0, rows, 0.5, 4.0, [0.5, 1, 2, 4], zero=1.0, fmt='%.2f', log=True, lsize=10.5)
    lines_block(it, 68, t1 - 26, ['Litio: aOR de seis cohortes (727 expuestos; P95). Antipsicóticos: RR en 1,34 millones de embarazos con',
                                   'estratificación por propensión (P96). Gris: intervalo que incluye 1 o estimación sin ajustar.'],
                size=9.2, lead=12.6)
    gx0 = 782.0
    panel(it, gx0, t0, 1141, t1, 'Lactancia con litio (P109)', accent=PURPLE)
    vb = [(85.7, 41.2, 'síntomas al\nnacer'), (28.6, 5.9, 'ingreso\nneonatal')]
    for k, (a, b, lab) in enumerate(vb):
        x = gx0 + 40 + k * 150
        for j, (v, c) in enumerate(((a, PURPLE), (b, (0.80, 0.74, 0.86)))):
            xa = x + j * 46
            bh = v / 100 * 170
            it.append(rect_top(xa, t0 + 230 - bh, xa + 38, t0 + 230, 3, fill=c))
            ctext(it, xa + 19, t0 + 224 - bh, ('%g' % v).replace('.', ','), 'Roboto-Medium', 9.5, INK)
        for m, ln in enumerate(lab.split('\n')):
            ctext(it, x + 42, t0 + 246 + 12 * m, ln, 'Roboto-Regular', 10, INK)
    it.append(rect_top(gx0 + 24, t0 + 282, gx0 + 36, t0 + 292, 2, fill=PURPLE))
    it.append(text(gx0 + 42, t0 + 291, 'litemia al nacer ≥ 0,6 (mediana 0,90)', 'Roboto-Regular', 9.5, INK))
    it.append(rect_top(gx0 + 24, t0 + 300, gx0 + 36, t0 + 310, 2, fill=(0.80, 0.74, 0.86)))
    it.append(text(gx0 + 42, t0 + 309, '< 0,6 mEq/L (mediana 0,40)', 'Roboto-Regular', 9.5, INK))
    it.append(text(gx0 + 18, t1 - 12, '25 díadas; diferencias no significativas (p 0,08 y 0,19).', 'Roboto-Regular', 9.2, GRAY))
    top = t1 + 14
    card_row(it, [
        dict(title='Litio: magnitud y momento', pill='E · P95', body=[
            'Malformaciones mayores 7,4 % frente a 4,3 % tras exposición en el primer trimestre; la diferencia cardiaca (2,1 % frente a '
            '1,6 %) no fue significativa. No hubo asociación con complicaciones del embarazo ni del parto. Los autores piden sopesar estos '
            'riesgos frente a la eficacia del litio para prevenir recaídas, alta en el posparto (P41).']),
        dict(title='Antipsicóticos y lactancia', pill='E · P96 · P109', body=[
            'Tras ajustar por la enfermedad de base, los antipsicóticos atípicos no aumentaron de forma relevante las malformaciones; '
            'risperidona mostró un aumento pequeño que requiere más estudio. Con lactancia y litio, una litemia alta al nacer predijo '
            'litemias mayores en el seguimiento: los autores aconsejan controlar pronto al lactante.']),
    ], top, X2, where='p91', bsize=11.2, lead=16.2)
    return it


# ------------------------------------------------------------------ 92 · comorbilidad médica
ORG = ['Riñón', 'Tiroides', 'Hígado', 'Sangre', 'Corazón (QT)', 'Metabolismo', 'Prolactina', 'Sodio']
ORGM = [('Litio', ['full', 'full', 'ring', 'ring', 'half', 'half', 'ring', 'half']),
        ('Valproato', ['ring', 'ring', 'full', 'full', 'ring', 'half', 'ring', 'ring']),
        ('Carbamazepina', ['ring', 'ring', 'full', 'full', 'half', 'ring', 'ring', 'full']),
        ('Olanzapina, quetiapina', ['ring', 'ring', 'ring', 'half', 'half', 'full', 'ring', 'ring']),
        ('Risperidona, paliperidona', ['half', 'ring', 'ring', 'ring', 'half', 'half', 'full', 'ring']),
        ('Ziprasidona, haloperidol', ['ring', 'ring', 'ring', 'ring', 'full', 'half', 'half', 'ring'])]


def p92():
    n = 92
    it = new_page('Comorbilidad médica y carga metabólica', 'POBLACIONES · IV',
                  'E · P97, P31 | E · dosieres D01–D13 (órganos diana) | G · matriz | relación con pp. 28, 36, 66 y 77', n)
    subtitle(it, 'Un tercio de las personas con trastorno mental grave cumple criterios de síndrome metabólico; el fármaco puede agravarlo.')
    t0, t1 = 128.0, 440.0
    panel(it, 50, t0, 470, t1, 'Síndrome metabólico en trastorno mental grave (P97)', accent=OCHRE)
    ctext(it, 160, t0 + 130, '32,6 %', 'Roboto-Bold', 34, NAVY)
    ctext(it, 160, t0 + 152, 'prevalencia agrupada', 'Roboto-Medium', 10.5, INK)
    ctext(it, 160, t0 + 168, '198 estudios · 52.678 personas', 'Roboto-Regular', 9.5, GRAY)
    ctext(it, 360, t0 + 130, '1,58', 'Roboto-Bold', 34, RED)
    ctext(it, 360, t0 + 152, 'RR frente a población', 'Roboto-Medium', 10.5, INK)
    ctext(it, 360, t0 + 168, 'IC 95 % 1,35–1,86', 'Roboto-Regular', 9.5, GRAY)
    lines_block(it, 68, t0 + 210, ['Sin diferencias entre esquizofrenia y trastorno bipolar ni',
                                    'entre bipolar y depresión mayor. Todos los antipsicóticos',
                                    'elevaron el riesgo frente a no expuestos; clozapina y',
                                    'olanzapina, más; aripiprazol, menos.'], size=10.5, lead=14.5, color=INK)
    it.append(text(68, t1 - 12, 'E · La edad y el IMC moderaron la prevalencia.', 'Roboto-Regular', 9.2, GRAY))
    gx0 = 492.0
    panel(it, gx0, t0, 1141, t1, 'Órgano diana que vigilar por fármaco (según las fichas de los dosieres)', accent=NAVY)
    x0, cw = 690.0, 56.0
    for j, o in enumerate(ORG):
        for m, ln in enumerate(o.split(' ')):
            ctext(it, x0 + cw * j + cw / 2, t0 + 50 + 11 * m, ln, 'Roboto-Bold', 9, NAVY)
    for i, (dname, vals) in enumerate(ORGM):
        yb = t0 + 92 + 36 * i
        if i % 2 == 0:
            it.append(rect_top(gx0 + 10, yb - 15, 1131, yb + 15, 3, fill=PALE))
        it.append(text(gx0 + 18, yb + 4, dname, 'Roboto-Medium', 10.5, INK))
        for j, v in enumerate(vals):
            mark(it, x0 + cw * j + cw / 2, yb, v, NAVY, r=6.5)
    legend_marks(it, gx0 + 18, t1 - 14, [('full', 'alerta principal'), ('half', 'según riesgo o asociación'), ('ring', 'no específica')], NAVY)
    top = t1 + 14
    card_row(it, [
        dict(title='Mortalidad y causa médica', pill='E · P31', body=[
            'Todos los trastornos mentales aumentan la mortalidad por cualquier causa (p. 28). En el trastorno bipolar, la carga '
            'cardiometabólica se suma a la enfermedad y al tratamiento: cribar y tratar, no solo vigilar.']),
        dict(title='Fármaco y enfermedad médica', pill='E · D01–D13', body=[
            'La insuficiencia renal pesa sobre el litio y la paliperidona; la hepática, sobre el valproato, la asenapina (Child-Pugh C, '
            'exposición multiplicada por siete) y la quetiapina; la cardiopatía con QT largo, sobre la ziprasidona y el haloperidol.']),
        dict(title='I · Infección por VIH y sustancias', body=[
            'La infección por VIH, la manía secundaria y el consumo de sustancias se cruzan en el chemsex (pp. 36–37); las interacciones '
            'por CYP3A4 de los antirretrovirales exigen revisar la tabla de la p. 65.']),
    ], top, X3, where='p92', bsize=11.2, lead=16.2)
    return it


# ------------------------------------------------------------------ 93–94, 97 · láminas
SHEETS37 = {
    25: dict(title='Curso 25 · Inicio en la adolescencia: manía mixta y ciclación',
             tag='G · viñeta ilustrativa | E · P92, P93 | I · relación con pp. 16, 52 y 89 | G · panel inferior: peso',
             sub='TEAM: 77,1 % con psicosis, 97,5 % mixta y 99,3 % con ciclación diaria; respuesta 68,5 % con risperidona y 35,6 % con litio.',
             curves={'dep': [0.30, 0.62, 0.42, 0.66, 0.44, 0.64, 0.38, 0.32, 0.30, 0.33, 0.30, 0.30],
                     'act': [0.40, 0.72, 0.58, 0.76, 0.62, 0.72, 0.46, 0.36, 0.32, 0.31, 0.31, 0.30],
                     'fun': [0.60, 0.32, 0.36, 0.28, 0.34, 0.30, 0.52, 0.66, 0.72, 0.74, 0.76, 0.76],
                     'res': [0.10, 0.10, 0.10, 0.10, 0.10, 0.12, 0.26, 0.40, 0.50, 0.56, 0.60, 0.62]},
             rows=[(140.0, 134.0, [(0.0, 5.5, 'Manía mixta con ciclación diaria', 'neu', False), (5.5, 11.4, 'Tras el antimaníaco', 'neu', False)]),
                   (159.0, 153.0, [(0.6, 5.5, 'Síntomas maníacos y depresivos concurrentes', 'elev')])],
             markers=[(5.5, 'risperidona')], psych=[(1.0, 4.2)], res=('PESO', 'aumento relativo'),
             foot='Ambos polos por encima del umbral a la vez: mixticidad.'),
    26: dict(title='Curso 26 · Manía de inicio tardío tratada con litio',
             tag='G · viñeta ilustrativa | E · P94 | I · relación con pp. 36, 65 y 90 | G · panel inferior: temblor',
             sub='GERI-BD (60 años o más): respuesta a 9 semanas del 79 % con litio y del 73 % con divalproato; más temblor con litio.',
             curves={'dep': [0.66, 0.40, 0.30, 0.28, 0.27, 0.28, 0.30, 0.32, 0.30, 0.29, 0.30, 0.30],
                     'act': [0.30, 0.30, 0.34, 0.78, 0.84, 0.78, 0.64, 0.50, 0.40, 0.34, 0.32, 0.31],
                     'fun': [0.56, 0.70, 0.76, 0.46, 0.38, 0.42, 0.52, 0.62, 0.70, 0.74, 0.76, 0.76],
                     'res': [0.05, 0.05, 0.05, 0.05, 0.30, 0.42, 0.46, 0.44, 0.40, 0.38, 0.36, 0.36]},
             rows=[(140.0, 134.0, [(0.0, 2.5, 'Antecedente depresivo', 'neu', False), (2.5, 8.0, 'Manía tardía · 9 semanas', 'neu', False),
                                   (8.0, 11.4, 'Continuación', 'neu', False)]),
                   (159.0, 153.0, [(0.0, 1.0, 'Depresión', 'dep'), (2.7, 6.5, 'Manía', 'elev')])],
             markers=[(3.5, 'litio 0,80–0,99')], res=('TEMBLOR', 'intensidad'),
             foot='Solo las 9 semanas del ensayo tienen base empírica; el resto es ilustrativo (G).'),
    27: dict(title='Curso 27 · Ciclación rápida y resistencia: de la combinación a la clozapina',
             tag='G · viñeta ilustrativa | E · P98, P99, D02 | H · clozapina con evidencia limitada | G · panel inferior: carga farmacológica',
             sub='Resistencia: sin remisión sostenida de 8 semanas tras dos ensayos adecuados (P98); clozapina: 15 estudios, 1.044 pacientes (P99).',
             curves={'dep': [0.68, 0.30, 0.66, 0.30, 0.64, 0.34, 0.62, 0.36, 0.40, 0.32, 0.30, 0.30],
                     'act': [0.30, 0.74, 0.32, 0.72, 0.34, 0.68, 0.36, 0.64, 0.42, 0.33, 0.31, 0.30],
                     'fun': [0.40, 0.40, 0.42, 0.42, 0.46, 0.46, 0.48, 0.50, 0.62, 0.70, 0.74, 0.76],
                     'res': [0.20, 0.20, 0.20, 0.40, 0.40, 0.40, 0.62, 0.62, 0.50, 0.42, 0.40, 0.40]},
             rows=[(140.0, 134.0, [(0.0, 3.0, 'Monoterapia', 'neu', False), (3.0, 6.0, 'Combinación', 'neu', False),
                                   (6.0, 8.0, 'Resistencia', 'neu', False), (8.0, 11.4, 'Clozapina', 'neu', False)]),
                   (159.0, 153.0, [(0.0, 8.0, 'Cuatro o más episodios al año', 'neu')])],
             markers=[(3.0, 'ensayo 2'), (8.0, 'clozapina')], res=('CARGA FARMACOLÓGICA', 'número de fármacos'),
             foot='Clozapina: evidencia limitada, solo series y estudios abiertos (P99).'),
}


def sheet37(k, tpl, pageno):
    d = SHEETS37[k]
    it = make_sheet(tpl, pageno=pageno, title=d['title'], tag=d['tag'], subtitle=d['sub'], curves=d['curves'], rows=d['rows'],
                    thr=(0.60, 0.60, 'umbral de manía'), markers=d['markers'], psych=d.get('psych'), extra_foot=d['foot'])
    if d.get('psych'):
        it[:] = [x for x in it if not (x['k'] == 'text' and x['text'].startswith('Síntomas psicóticos no representados'))]
    for x in it:
        if x['k'] == 'text' and x['text'] == 'RESIDUO':
            x['text'] = d['res'][0]
        elif x['k'] == 'text' and x['text'].strip() == 'carga':
            x['text'] = d['res'][1]
    return it


# ------------------------------------------------------------------ 95 · resistencia: definiciones
def p95():
    n = 95
    it = new_page('Resistencia al tratamiento: definiciones y niveles', 'RESISTENCIA · I',
                  'F/H · consenso Delphi (P98) | E · ciclación rápida (P11, P16) | G · escalera de niveles', n)
    subtitle(it, 'Llamar resistente a un cuadro exige antes comprobar diagnóstico, dosis, duración y adherencia; el consenso lo formaliza para la depresión bipolar.')
    t0, t1 = 128.0, 500.0
    panel(it, 50, t0, 1141, t1, 'Niveles de resistencia en la depresión bipolar (P98)', accent=PURPLE)
    steps = [('Pseudorresistencia', 'diagnóstico, dosis, duración,', 'adherencia o interacciones', GRAY),
             ('Un fracaso', 'un ensayo adecuado sin', 'remisión sostenida', (0.62, 0.66, 0.78)),
             ('Resistente (TRBD)', 'dos ensayos adecuados: ≥ 2 monoterapias', 'o 1 monoterapia + 1 combinación', PURPLE),
             ('Multirresistente (MTRBD)', 'TRBD + fracaso de un antidepresivo,', 'un tratamiento psicológico y TEC', NAVY)]
    base = t1 - 60
    w = 240.0
    for k, (lab, l1, l2, col) in enumerate(steps):
        xa = 80 + k * (w + 14)
        h = 70 + 50 * k
        it.append(rect_top(xa, base - h, xa + w, base, 6, fill=col))
        it.append(text(xa + 12, base - h + 24, lab, 'Roboto-Bold', 12.5, WHITE))
        it.append(text(xa + 12, base - h + 42, l1, 'Roboto-Regular', 10, WHITE))
        it.append(text(xa + 12, base - h + 56, l2, 'Roboto-Regular', 10, WHITE))
    arrow(it, 80, base + 20, 1100, base + 20, color=INK, lw=1.4)
    it.append(text(80, base + 38, 'Remisión sostenida = 8 semanas consecutivas; ensayos a dosis terapéuticas adecuadas.', 'Roboto-Regular', 10, INK))
    it.append(text(1100 - sw('mayor resistencia', 'Roboto-Medium', 10), base + 38, 'mayor resistencia', 'Roboto-Medium', 10, INK))
    top = t1 + 14
    card_row(it, [
        dict(title='Lo que define el consenso', pill='F · H · P98', body=[
            'Un panel de expertos (método Delphi modificado) definió la depresión bipolar resistente como la falta de remisión '
            'sintomática sostenida durante 8 semanas consecutivas tras dos ensayos a dosis adecuadas con al menos dos monoterapias '
            'recomendadas, o una monoterapia y una combinación. La multirresistencia añade el fracaso de un antidepresivo, un '
            'tratamiento psicológico y un curso de terapia electroconvulsiva.']),
        dict(title='Ciclación rápida', pill='F · E · P11 · P16', body=[
            'Cuatro o más episodios en 12 meses (p. 16). La ciclación rápida no equivale a resistencia, pero la acompaña a menudo y '
            'obliga a revisar antidepresivos, hipotiroidismo, sustancias y adherencia antes de concluir que un tratamiento fracasó '
            '(pp. 31, 36 y 37).']),
    ], top, X2, where='p95', bsize=11.5, lead=16.6)
    return it


# ------------------------------------------------------------------ 96 · estrategias
def p96():
    n = 96
    it = new_page('Estrategias en resistencia: combinación y clozapina', 'RESISTENCIA · II',
                  'E · BALANCE (D02), red de combinaciones (P87), clozapina (P99) | H · evidencia limitada en resistencia', n)
    subtitle(it, 'Cuando la monoterapia no basta, la combinación tiene ensayos controlados y la clozapina, series y estudios abiertos.')
    t0, t1 = 128.0, 450.0
    panel(it, 50, t0, 470, t1, 'BALANCE: intervención por episodio [D02 · T4]', accent=TEAL)
    vbars(it, 110, t1 - 76, 70, 34, [69, 59, 54], 80, 200, [OCHRE, BLUE, TEAL], ['Valproato', 'Litio', 'Litio +\nvalproato'])
    it.append(text(68, t1 - 12, '110 por brazo, hasta dos años; litio frente a valproato HR 0,71 [0,51–1,00].', 'Roboto-Regular', 9.2, GRAY))
    gx0 = 492.0
    panel(it, gx0, t0, 1141, t1, 'Antipsicótico añadido a litio o valproato frente a placebo añadido (P87)', accent=NAVY)
    comb = [('Aripiprazol + Li/VPA', True, False, True, False), ('Lurasidona + Li/VPA', True, True, False, True),
            ('Olanzapina + Li/VPA', False, False, False, False), ('Quetiapina + Li/VPA', True, True, True, True),
            ('Ziprasidona + Li/VPA', True, False, False, False)]
    cxs = [790, 870, 950, 1040]
    for c, lab in zip(cxs, ('Cualquier', 'Depresión', 'Manía', 'Abandono')):
        ctext(it, c, t0 + 54, lab, 'Roboto-Bold', 10, NAVY)
    for k, row in enumerate(comb):
        yb = t0 + 86 + 38 * k
        if k % 2 == 0:
            it.append(rect_top(gx0 + 10, yb - 16, 1131, yb + 16, 3, fill=PALE))
        it.append(text(gx0 + 18, yb + 4, row[0], 'Roboto-Medium', 11, INK))
        for c, v in zip(cxs, row[1:]):
            mark(it, c, yb, 'full' if v else 'ring', TEAL if c != 870 else BLUE)
    lines_block(it, gx0 + 18, t1 - 26, ['Relleno: superó al placebo añadido. Anillo: sin superioridad demostrada. Cualquier episodio,',
                                         'recaída depresiva, maníaca y abandono por cualquier causa.'], size=9.2, lead=12.6)
    top = t1 + 14
    c0, c1 = top, top + 196
    panel(it, 50, c0, 640, c1, 'Clozapina en el trastorno bipolar resistente: reacciones adversas (P99)', accent=RED)
    ae = [('Sedación', 12.0, OCHRE), ('Sialorrea', 5.2, OCHRE), ('Estreñimiento', 5.0, OCHRE), ('Peso', 4.0, OCHRE),
          ('Leucopenia', 2.0, RED), ('Convulsión', 0.5, RED), ('Agranulocitosis', 0.3, RED)]
    for k, (lab, v, col) in enumerate(ae):
        yb = c0 + 60 + 19 * k
        it.append(text(68, yb + 3, lab, 'Roboto-Regular', 10, INK))
        it.append(rect_top(190, yb - 7, 190 + v * 17, yb + 5, 2, fill=col))
        it.append(text(196 + v * 17, yb + 3, ('%g %%' % v).replace('.', ','), 'Roboto-Medium', 9.5, INK))
    lines_block(it, 456, c0 + 64, ['15 estudios, 1.044 pacientes:', 'ECA, abiertos y retrospectivos.', 'Ocre: frecuentes y molestas;',
                                    'rojo: graves, que exigen', 'control hematológico.'], size=10, lead=14, color=INK)
    card(it, 662, c0, 1141, t1=c1, title='Qué mejoró con clozapina', pill='E · H · P99', body=[
        'Manía, depresión, ciclación rápida y psicosis; menos hospitalizaciones; menos ideación suicida y agresividad. La mezcla de '
        'ECA, estudios abiertos y retrospectivos impide estimar el efecto: los autores califican la evidencia de limitada.'],
         where='p96', bsize=11.2, lead=16.2)
    return it


# ------------------------------------------------------------------ 98 · litio y suicidio
def p98():
    n = 98
    it = new_page('Litio y suicidio: qué dicen ensayos y registros', 'SUICIDIO · I',
                  'E · P100 (ECA), P102 (registro intraindividual), P101 (ECA Li+plus) | I · discrepancias | relación con p. 28', n)
    subtitle(it, 'La señal antisuicida del litio es robusta en los metaanálisis y en los registros, pero no se reprodujo al añadirlo en una población de alto riesgo.')
    t0, t1 = 128.0, 522.0
    panel(it, 50, t0, 1141, t1, 'Estimaciones frente a placebo o frente a periodos sin tratamiento · escala logarítmica', accent=RED)
    rows = [('Suicidio · ECA, litio frente a placebo (OR)', 0.13, 0.03, 0.66, RED),
            ('Muerte por cualquier causa · ECA (OR)', 0.38, 0.15, 0.95, RED),
            ('Autolesión · ECA (OR)', 0.60, 0.27, 1.32, GRAY),
            ('Suicidio en depresión unipolar · ECA (OR)', 0.36, 0.13, 0.98, RED),
            ('Eventos suicidas · registro, periodos con litio (HR)', 0.86, 0.78, 0.95, NAVY),
            ('Eventos suicidas · registro, periodos con valproato (HR)', 1.02, 0.89, 1.15, GRAY),
            ('Eventos suicidas repetidos · Li+plus, litio añadido (HR)', 1.10, 0.77, 1.55, GRAY),
            ('Conductas suicidas · transversal, exposición a litio (OR)', 0.55, 0.34, 0.89, OCHRE)]
    lforest(it, 520, 900, t0 + 72, 36.0, rows, 0.02, 2.0, [0.02, 0.05, 0.1, 0.25, 0.5, 1, 2], zero=1.0, fmt='%.2f', log=True,
            lsize=10.5)
    lines_block(it, 68, t1 - 26, ['P100: 48 ECA, 6.674 participantes. P102: 51.535 personas en Suecia, 2005–2013, 10.648 eventos. P101: 519 veteranos tras '
                                   'un evento reciente; detenido por futilidad.', 'P111: 585 pacientes de 12–45 años, 14 centros, diseño transversal (ocre: confusión por indicación no excluible). Gris: intervalo que incluye 1.'], size=9.2, lead=12.6)
    top = t1 + 14
    card_row(it, [
        dict(title='Lo que es sólido', pill='E · P100 · P102', body=[
            'En los ECA de mantenimiento, el litio redujo los suicidios y la mortalidad global frente a placebo. En el registro sueco, '
            'los periodos con litio tuvieron un 14 % menos de eventos suicidas que los periodos sin él, sin efecto del valproato; los '
            'autores estiman evitable el 12 % de los eventos si se hubiera tomado litio todo el seguimiento.']),
        dict(title='Lo que matiza Li+plus', pill='E · P101', body=[
            'Añadir litio al tratamiento habitual tras un evento suicida reciente no redujo los eventos repetidos (65 frente a 62). Las '
            'litemias fueron bajas (0,54 mEq/L en bipolares y 0,46 en depresión mayor) y la comorbilidad, alta: el resultado no anula el '
            'efecto preventivo a largo plazo, pero desaconseja confiar en el litio como intervención aislada de crisis.']),
        dict(title='I · Mecanismos propuestos', pill='I · P100 · P111', body=[
            'Prevención de recaídas y posible reducción de la agresividad y la impulsividad (P100). En un estudio transversal chino, la '
            'agresividad explicó estadísticamente un 21 % de la asociación entre litio y conductas suicidas (P111), sin inferencia causal. '
            'El riesgo suicida se evalúa siempre aparte del fármaco (p. 28).']),
    ], top, X3, where='p98', bsize=11.0, lead=15.8)
    return it


# ------------------------------------------------------------------ 99 · cronograma y plan de seguridad
def p99():
    n = 99
    it = new_page('Cronograma de riesgo y plan de seguridad', 'SUICIDIO · II',
                  'E · factores de riesgo (P29), mixticidad (P35), alta de urgencias (P103) | G · cronograma | I · no predice el caso', n)
    subtitle(it, 'El riesgo no es constante: se concentra en estados y periodos reconocibles, que el plan de seguridad debe anticipar.')
    t0, t1 = 128.0, 360.0
    panel(it, 50, t0, 1141, t1, 'Periodos de mayor riesgo a lo largo del curso (G, con apoyo empírico citado)', accent=RED)
    x0, x1, yb = 90.0, 1110.0, t0 + 150
    it.append(line_top(x0, yb, x1, yb, stroke=GRAY, lw=2.0))
    phases = [(0.02, 0.22, 'Episodio depresivo', 'gravedad y desesperanza (P29)', BLUE),
              (0.22, 0.40, 'Estado mixto', 'asociado a intentos previos (P35)', PURPLE),
              (0.40, 0.48, 'Alta hospitalaria', '', RED),
              (0.48, 0.78, '6 meses tras urgencias', 'periodo de alto riesgo (P103)', RED),
              (0.78, 0.98, 'Intento previo', 'OR 4,84 de suicidio (P29)', NAVY)]
    for k, (a, bnd, l1, l2, col) in enumerate(phases):
        xa, xb = x0 + (x1 - x0) * a, x0 + (x1 - x0) * bnd
        it.append(rect_top(xa, yb - 22, xb - 3, yb + 22, 5, fill=col, alpha=0.22 if col != RED else 0.32))
        tt = yb - 34 if k % 2 == 0 else yb + 40
        it.append(text(xa + 4, tt, l1, 'Roboto-Bold', 10.5, col))
        if l2:
            it.append(text(xa + 4, tt + 13, l2, 'Roboto-Regular', 9.2, INK))
    it.append(text(68, t1 - 14, 'G · Orden y anchura ilustrativos; los periodos se superponen en la clínica. El cronograma no asigna probabilidades.',
                   'Roboto-Regular', 9.2, GRAY))
    top = t1 + 14
    c0, c1 = top, top + 220
    panel(it, 50, c0, 560, c1, 'Factores asociados a suicidio en la depresión (P29) · OR', accent=NAVY)
    fr = [('Intento previo', 4.84), ('Mayor gravedad', 2.20), ('Desesperanza', 2.20), ('Alcohol o drogas', 2.17),
          ('Sexo masculino', 1.76), ('Ansiedad comórbida', 1.59), ('Antecedente familiar', 1.41)]
    for k, (lab, v) in enumerate(fr):
        yb2 = c0 + 58 + 22 * k
        it.append(text(68, yb2 + 3, lab, 'Roboto-Regular', 10.5, INK))
        it.append(rect_top(220, yb2 - 8, 220 + v * 60, yb2 + 5, 2, fill=NAVY if v > 2 else (0.45, 0.55, 0.65)))
        it.append(text(226 + v * 60, yb2 + 3, ('%.2f' % v).replace('.', ','), 'Roboto-Medium', 9.5, INK))
    gx0 = 582.0
    panel(it, gx0, c0, 1141, c1, 'Plan de seguridad con seguimiento telefónico (P103)', accent=TEAL)
    nodes = [(gx0 + 90, 'Urgencias', 'riesgo suicida'), (gx0 + 270, 'Plan de seguridad', 'estrategias priorizadas'),
             (gx0 + 450, 'Seguimiento', '≥ 2 llamadas')]
    for x, l1, l2 in nodes:
        it.append(rect_top(x - 78, c0 + 52, x + 78, c0 + 104, 8, fill=WHITE, stroke=TEAL, lw=1.6))
        ctext(it, x, c0 + 74, l1, 'Roboto-Bold', 11, NAVY)
        ctext(it, x, c0 + 90, l2, 'Roboto-Regular', 9.5, INK)
    for a, bnd in ((0, 1), (1, 2)):
        arrow(it, nodes[a][0] + 80, c0 + 78, nodes[bnd][0] - 80, c0 + 78, color=INK)
    for k, (lab, v, lo, hi) in enumerate((('Conducta suicida a 6 meses', 0.56, 0.33, 0.95), ('≥ 1 visita ambulatoria', 2.06, 1.57, 2.71))):
        yb3 = c0 + 140 + 28 * k
        it.append(text(gx0 + 18, yb3 + 4, lab, 'Roboto-Regular', 10.5, INK))
        xa, xb = gx0 + 240, gx0 + 480

        def lp(z):
            return xa + (math.log(z) - math.log(0.25)) / (math.log(4) - math.log(0.25)) * (xb - xa)
        it.append(line_top(lp(1), yb3 - 10, lp(1), yb3 + 10, stroke=INK, lw=1.0))
        it.append(line_top(lp(lo), yb3, lp(hi), yb3, stroke=TEAL, lw=2.0))
        dot(it, lp(v), yb3, 5, TEAL)
        it.append(text(lp(hi) + 8, yb3 + 4, ('OR %.2f' % v).replace('.', ','), 'Roboto-Medium', 9.5, INK))
    it.append(text(gx0 + 18, c1 - 12, '1.186 frente a 454 pacientes; 3,03 % frente a 5,29 %. Cohorte comparada, no ECA.', 'Roboto-Regular', 9.2, GRAY))
    note(it, 50, c1 + 14, 1141, 'I · Cómo se integra en el atlas', [
        'El riesgo suicida es una capa transversal (p. 28): se reevalúa en cada lámina y cada cambio de fase. El plan de seguridad y el '
        'seguimiento activo tras el alta tienen apoyo empírico propio y no dependen del fármaco elegido.'], kind='info', where='p99')
    return it


# ------------------------------------------------------------------ 100 · heredabilidad
def p100():
    n = 100
    it = new_page('Heredabilidad y arquitectura genética', 'GENÉTICA · I',
                  'E · P104 (familias), P105 (SNP), P106 (GWAS) | I · la heredabilidad no es un riesgo individual', n)
    subtitle(it, 'El trastorno bipolar es uno de los más heredables de la psiquiatría, pero su genética es poligénica y compartida.')
    t0, t1 = 128.0, 450.0
    panel(it, 50, t0, 520, t1, 'Cuánta varianza explican los genes', accent=PURPLE)
    vbars(it, 110, t1 - 80, 90, 60, [58, 23], 70, 220, [PURPLE, (0.70, 0.62, 0.80)],
          ['Familias suecas\n(P104)', 'SNP comunes\n(P105, 17–29 %)'])
    lines_block(it, 68, t1 - 26, ['La diferencia entre ambas cifras es la heredabilidad que los SNP comunes no capturan (I).',
                                   'La barra de SNP muestra el punto medio del rango 17–29 % (G).'], size=9.2, lead=12.6)
    gx0 = 542.0
    panel(it, gx0, t0, 1141, t1, 'Riesgo familiar y correlación con otros trastornos (P104)', accent=NAVY)
    ctext(it, gx0 + 150, t0 + 120, '5,8–7,9', 'Roboto-Bold', 30, NAVY)
    ctext(it, gx0 + 150, t0 + 142, 'riesgo relativo en familiares', 'Roboto-Medium', 10.5, INK)
    ctext(it, gx0 + 150, t0 + 157, 'de primer grado', 'Roboto-Medium', 10.5, INK)
    ctext(it, gx0 + 440, t0 + 120, '54.723', 'Roboto-Bold', 30, NAVY)
    ctext(it, gx0 + 440, t0 + 142, 'personas con trastorno bipolar', 'Roboto-Medium', 10.5, INK)
    ctext(it, gx0 + 440, t0 + 157, 'entre 8,1 millones de hijos', 'Roboto-Medium', 10.5, INK)
    for k, (lab, v) in enumerate((('Depresión', 0.62), ('Esquizofrenia', 0.44))):
        yb = t0 + 214 + 40 * k
        it.append(text(gx0 + 30, yb + 4, lab, 'Roboto-Medium', 11, INK))
        it.append(rect_top(gx0 + 160, yb - 9, gx0 + 160 + v * 500, yb + 7, 3, fill=BLUE if k == 0 else PURPLE))
        it.append(text(gx0 + 166 + v * 500, yb + 4, ('r = %.2f' % v).replace('.', ','), 'Roboto-Medium', 10, INK))
    lines_block(it, gx0 + 18, t1 - 26, ['Correlaciones tetracóricas con otros trastornos en el rango 0,37–0,62: el trastorno bipolar se coagrega en las',
                                         'familias tanto con la depresión como con la esquizofrenia.'],
                size=9.2, lead=12.6)
    top = t1 + 14
    card_row(it, [
        dict(title='GWAS de más de 40.000 casos', pill='E · P106', body=[
            '41.917 casos y 371.549 controles de ascendencia europea: 64 loci asociados. Los alelos de riesgo se concentran en genes de '
            'señalización sináptica expresados en neuronas de corteza prefrontal e hipocampo, y en dianas de antipsicóticos, '
            'antagonistas del calcio, antiepilépticos y anestésicos. Quince genes con vínculo robusto por expresión (HTR6, MCHR1, DCLK3, FURIN).']),
        dict(title='I · Lo que no permite', pill='I', body=[
            'Una heredabilidad del 58 % no significa que el 58 % del riesgo de una persona sea genético, ni que exista un test diagnóstico. '
            'Bipolar I y II difieren en heredabilidad SNP (0,35 frente a 0,25) y se correlacionan en 0,78; el tipo I y el esquizoafectivo '
            'bipolar acumulan más alelos de riesgo de esquizofrenia (P110, P106): un continuo con diferencias, coherente con la p. 52.']),
    ], top, X2, where='p100', bsize=11.2, lead=16.2)
    return it


# ------------------------------------------------------------------ 101 · correlación genética
RG = ['Esquizofrenia', 'Bipolar', 'Depresión mayor', 'Autismo', 'TDAH']
RGV = {(0, 1): 0.68, (0, 2): 0.43, (1, 2): 0.47, (2, 4): 0.32, (0, 3): 0.16}
RGSE = {(0, 1): 0.04, (0, 2): 0.06, (1, 2): 0.06, (2, 4): 0.07, (0, 3): 0.06}


def p101():
    n = 101
    it = new_page('Mapa de calor de la correlación genética entre trastornos', 'GENÉTICA · II',
                  'E · Cross-Disorder Group del PGC (P105) | G · mapa de calor | I · relación con HiTOP y factor p (p. 53)', n)
    subtitle(it, 'Con SNP comunes de cinco trastornos, la genética del bipolar se solapa sobre todo con la de la esquizofrenia y la depresión.')
    t0, t1 = 128.0, 640.0
    panel(it, 50, t0, 760, t1, 'Correlación genética (rg) estimada con SNP comunes (P105)', accent=PURPLE)
    x0, y0, cs = 236.0, t0 + 90, 74.0
    for j, lab in enumerate(RG):
        for m, ln in enumerate(lab.split(' ')):
            ctext(it, x0 + cs * j + cs / 2, y0 - 26 + 12 * m, ln, 'Roboto-Bold', 10.5, NAVY)
    for i, lab in enumerate(RG):
        it.append(text(68, y0 + cs * i + cs / 2 + 4, lab, 'Roboto-Bold', 10.5, NAVY))
        for j in range(5):
            xa, ya = x0 + cs * j, y0 + cs * i
            if i == j:
                it.append(rect_top(xa + 3, ya + 3, xa + cs - 3, ya + cs - 3, 6, fill=(0.85, 0.85, 0.85)))
                ctext(it, xa + cs / 2, ya + cs / 2 + 4, '1', 'Roboto-Medium', 12, GRAY)
                continue
            key = (min(i, j), max(i, j))
            v = RGV.get(key)
            if v is None:
                it.append(rect_top(xa + 3, ya + 3, xa + cs - 3, ya + cs - 3, 6, fill=WHITE, stroke=LINE, lw=1.0))
                ctext(it, xa + cs / 2, ya + cs / 2 + 4, 'n. s.', 'Roboto-Regular', 10, GRAY)
                continue
            f = v / 0.7
            col = (0.95 - 0.55 * f, 0.93 - 0.68 * f, 0.97 - 0.40 * f)
            it.append(rect_top(xa + 3, ya + 3, xa + cs - 3, ya + cs - 3, 6, fill=col))
            s = ('%.2f' % v).replace('.', ',')
            ctext(it, xa + cs / 2, ya + cs / 2 + 1, s, 'Roboto-Bold', 14, WHITE if v > 0.4 else INK)
            ctext(it, xa + cs / 2, ya + cs / 2 + 16, ('± %.2f' % RGSE[key]).replace('.', ','), 'Roboto-Regular', 9, WHITE if v > 0.4 else INK)
    lines_block(it, 68, t1 - 26, ['n. s.: correlación no significativa. Los SNP explicaron el 17–29 % de la varianza de la susceptibilidad;',
                                   'la enfermedad de Crohn, usada como control negativo, no se correlacionó con ningún trastorno.'], size=9.2, lead=12.6)
    x0 = 782.0
    top = 128.0
    top = card(it, x0, top, 1141, title='Lectura del mapa', pill='E · P105', body=[
        'La correlación más alta es entre esquizofrenia y trastorno bipolar (0,68); bipolar y depresión mayor comparten una fracción '
        'moderada (0,47), parecida a la de esquizofrenia y depresión (0,43). Autismo y TDAH apenas se correlacionan con el bipolar con '
        'esta metodología.'], where='p101', bsize=11.5, lead=16.6) + 12
    top = card(it, x0, top, 1141, title='Dos métodos, dos órdenes', pill='E · P104 · P105', body=[
        'En las familias suecas, el bipolar se correlacionó más con la depresión (0,62) que con la esquizofrenia (0,44); con SNP comunes '
        'ocurre lo contrario. Las cifras miden cosas distintas (agregación familiar total frente a variantes comunes) y no se comparan '
        'directamente.'], where='p101', bsize=11.5, lead=16.6) + 12
    note(it, x0, top, 1141, 'I · Relación con la nosología', [
        'La genética compartida es uno de los argumentos de los modelos transdiagnósticos y del factor p (p. 53), y matiza la frontera '
        'kraepeliniana entre psicosis afectiva y no afectiva (pp. 40 y 48).'], kind='info', t1=max(top + 100, t1), where='p101')
    return it


# ------------------------------------------------------------------ 102 · respuesta al litio y biomarcadores digitales
def p102():
    n = 102
    it = new_page('Respuesta al litio y biomarcadores digitales', 'GENÉTICA · III',
                  'E · ConLiGen (P107), actigrafía (P108) | G · ideograma y actograma esquemáticos | H · uso clínico no establecido', n)
    subtitle(it, 'La respuesta al litio es en parte heredable y el ritmo actividad-reposo se altera en todas las fases; ninguno es aún un test clínico.')
    t0, t1 = 128.0, 430.0
    panel(it, 50, t0, 590, t1, 'GWAS de respuesta al litio: un locus en el cromosoma 21 (P107)', accent=PURPLE)
    cy = t0 + 96
    it.append(rect_top(100, cy - 14, 540, cy + 14, 14, fill=(0.93, 0.92, 0.95), stroke=PURPLE, lw=1.2))
    for k, xa in enumerate((150, 200, 260, 330, 420, 480)):
        it.append(rect_top(xa, cy - 14, xa + 18, cy + 14, 0, fill=(0.80, 0.76, 0.86)))
    it.append(path(rrect_ops(170, Y(cy + 16), 182, Y(cy - 16), 0), fill=GRAY))
    xl = 380.0
    it.append(rect_top(xl - 4, cy - 20, xl + 4, cy + 20, 2, fill=RED))
    it.append(text(xl - 70, cy - 30, '4 SNP ligados', 'Roboto-Bold', 10.5, RED))
    it.append(text(xl - 120, cy + 38, 'ARN largos no codificantes', 'Roboto-Regular', 10, INK))
    it.append(text(xl - 120, cy + 52, 'AL157359.3 y AL157359.4', 'Roboto-Regular', 10, INK))
    it.append(text(100, cy - 30, 'cromosoma 21', 'Roboto-Medium', 10, GRAY))
    lines_block(it, 68, t0 + 186, ['2.563 pacientes de 22 centros; respuesta medida con la escala de Alda;',
                                    'significación genómica (p hasta 3,31 × 10⁻⁹).'], size=10.5, lead=14.5, color=INK)
    it.append(text(68, t0 + 228, 'Validación prospectiva en 73 pacientes (recaída):', 'Roboto-Medium', 10.5, NAVY))
    xa, xb = 120.0, 520.0

    def lp(z):
        return xa + (math.log(z) - math.log(0.5)) / (math.log(20) - math.log(0.5)) * (xb - xa)
    yb = t0 + 254
    it.append(line_top(lp(1), yb - 12, lp(1), yb + 12, stroke=INK, lw=1.0))
    it.append(line_top(lp(1.1), yb, lp(13.0), yb, stroke=PURPLE, lw=2.0))
    dot(it, lp(3.8), yb, 5.5, PURPLE)
    it.append(text(lp(13.0) + 8, yb + 4, 'HR 3,8 [1,1–13,0]', 'Roboto-Medium', 10, INK))
    it.append(text(68, t1 - 12, 'Los portadores de los alelos asociados a buena respuesta recayeron menos.', 'Roboto-Regular', 9.2, GRAY))
    gx0 = 612.0
    panel(it, gx0, t0, 1141, t1, 'Actigrafía: actividad y sueño (P108)', accent=TEAL)
    ax0, ax1 = gx0 + 30, 1110.0
    for r, (lab, amp, col) in enumerate((('control', 1.0, GRAY), ('trastorno bipolar', 0.72, TEAL))):
        base = t0 + 110 + 90 * r
        it.append(text(ax0, base - 52, lab, 'Roboto-Medium', 10.5, col))
        it.append(line_top(ax0, base, ax1, base, stroke=LINE, lw=0.8))
        xs, tops = [], []
        for i in range(97):
            hgt = i / 96.0 * 48
            day = 7 <= (hgt % 24) <= 22.5
            a = (0.85 if day else 0.06) * amp
            if r == 1 and (hgt % 24) > 23 or (r == 1 and (hgt % 24) < 1.5):
                a = 0.30 * amp
            a += 0.08 * math.sin(i * 1.7)
            xs.append(ax0 + (ax1 - ax0) * i / 96.0)
            tops.append(base - max(0.0, a) * 40)
        curve(it, xs, tops, col, lw=1.6, fill=col, base_top=base)
    for h, lab in ((0, '0 h'), (24, '24 h'), (48, '48 h')):
        x = ax0 + (ax1 - ax0) * h / 48
        it.append(text(x - sw(lab, 'Roboto-Regular', 9) / 2, t0 + 216, lab, 'Roboto-Regular', 9, GRAY))
    lines_block(it, gx0 + 18, t0 + 244, ['13 estudios, 821 participantes: menor actividad media y', 'patrón de sueño alterado frente a controles,',
                                          'en manía, depresión y eutimia.'], size=10.5, lead=14.5, color=INK)
    it.append(text(gx0 + 18, t1 - 12, 'G · Actograma esquemático de dos días; no reproduce datos individuales.', 'Roboto-Regular', 9.2, GRAY))
    top = t1 + 14
    card_row(it, [
        dict(title='I · Del gen al consultorio', pill='I · H', body=[
            'El locus de ConLiGen explica una parte pequeña de la respuesta y procede de un análisis retrospectivo con validación en 73 '
            'pacientes: no existe hoy un test genético de respuesta al litio. Su valor es orientar la biología (ARN no codificantes) y '
            'apoyar que la respuesta es un rasgo, coherente con la agregación familiar (p. 100).']),
        dict(title='I · Ritmos medibles', pill='I · P108', body=[
            'La actigrafía mide de forma objetiva la actividad y el sueño que el atlas trata como pródromo (pp. 42–43) y como dominio de '
            'actividad del modelo ACE (p. 50). La alteración persiste en eutimia, lo que la acerca a un rasgo y no solo a un estado.']),
    ], top, X2, where='p102', bsize=11.2, lead=16.2)
    return it


NEW_PAGES37 = [p89, p90, p91, p92, 's25', 's26', p95, p96, 's27', p98, p99, p100, p101, p102]

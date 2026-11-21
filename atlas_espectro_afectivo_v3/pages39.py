"""Ampliación IX del Atlas v3.9 (pp. 113–124): artículos a texto completo aportados por el autor.

Cifras tomadas del texto completo (tablas y resultados) de P01, P06, P13, P58 y P178–P192; fichas
verificadas en PubMed el 21-nov-2026. Convención F/E/I/H/G. No prescriptivo (p. 20)."""
from layout31 import (new_page, card, card_row, note, sw, text, rect_top, line_top, PURPLE, OCHRE, WHITE, NAVY, INK,
                      GRAY, LINE, TEAL, BLUE, RED, NOTEFILL)
from pages32 import panel, subtitle, X2, X3
from pages33 import arrow, dot, ctext, lines_block
from pages34 import mark, legend_marks, lforest, PALE
from pages37 import vbars
from pages38 import num, hrows, key2, split_bar, LILA, AZUL2


def pairs(it, x0, base0, pitch, rows, scale, label_w, ca, cb, lsize=10.5, fmt='%g', ref=None):
    """rows: (etiqueta, a, b); None omite la barra. ref: (valor, color) dibuja una línea vertical."""
    xb = x0 + label_w
    for k, (lab, a, b) in enumerate(rows):
        yb = base0 + pitch * k
        it.append(text(x0, yb + 4, lab, 'Roboto-Regular', lsize, INK))
        for j, (v, c) in enumerate(((a, ca), (b, cb))):
            if v is None:
                continue
            t = yb - 9 + 10 * j
            it.append(rect_top(xb, t, xb + v * scale, t + 8, 2, fill=c))
            it.append(text(xb + v * scale + 5, t + 7.5, num(v, fmt), 'Roboto-Medium', 8.8, INK))
    if ref:
        x = xb + ref[0] * scale
        it.append(line_top(x, base0 - 16, x, base0 + pitch * (len(rows) - 1) + 14, stroke=ref[1], lw=1.2))


# ------------------------------------------------------------------ 113 · curso semanal
def p113():
    n = 113
    it = new_page('Curso semanal a veinte años: bipolar I frente a bipolar II', 'TEXTOS · CURSO I',
                  'E · P01 (tablas 3–6), P13 (tablas 2–5) | I · cronicidad y gravedad son ejes distintos | relación con pp. 10–18 y 44', n)
    subtitle(it, 'Con valoraciones semanales durante trece años de media, el bipolar II resulta más crónico y casi siempre depresivo; el bipolar I, más grave y bipolar.')
    t0, t1 = 128.0, 440.0
    panel(it, 50, t0, 590, t1, 'Porcentaje de semanas por polaridad (P01, tabla 4)', accent=BLUE)
    pairs(it, 68, t0 + 72, 50.0, [('Sin síntomas', 53.4, 44.2), ('Depresión pura', 30.6, 51.9), ('Manía o hipomanía pura', 9.8, 1.4),
                                   ('Ciclado o mixto', 6.0, 2.5)], 5.0, 190, NAVY, OCHRE, lsize=11)
    key2(it, 68, t0 + 258, 'bipolar I, n = 135', NAVY, 'bipolar II, n = 71', OCHRE)
    lines_block(it, 68, t1 - 26, ['Razón de semanas depresivas a maníacas o hipomaníacas: 3 a 1 en el bipolar I y 37 a 1 en el II.',
                                   'El resumen del artículo da 59,1 % y 1,9 % para el bipolar II; la tabla y el texto, 51,9 % y 1,4 %.'],
                size=9.2, lead=12.6)
    gx0 = 612.0
    panel(it, gx0, t0, 1141, t1, 'Porcentaje de semanas por nivel de gravedad (P01, tabla 3)', accent=PURPLE)
    pairs(it, gx0 + 18, t0 + 72, 50.0, [('Subsindrómico', 14.1, 16.2), ('Menor o hipomaníaco', 20.1, 27.0), ('Mayor o maníaco', 12.3, 12.6)],
          9.0, 170, NAVY, OCHRE, lsize=11)
    lines_block(it, gx0 + 18, t0 + 226, ['Los síntomas menores y subsindrómicos fueron unas tres veces más frecuentes que los',
                                          'sindrómicos. Cambios de estado por año: 5,9 frente a 3,8; cambios de polaridad: 3,5 frente a 1,5.',
                                          'En la serie de 86 pacientes bipolar II (P13): 50,3 % de semanas depresivas, 1,3 % hipomaníacas.'],
                size=10, lead=14.2, color=INK)
    it.append(text(gx0 + 18, t1 - 12, 'Solo difirió el nivel menor (p = 0,036). Estudio naturalista del NIMH; muestra blanca, de centros académicos.',
                   'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Tratamiento prescrito', pill='E · P01 · P13', body=[
            'Semanas sin síntomas con algún tratamiento somático: 73,7 % en el bipolar I y 43,5 % en el II. En el bipolar II, el 26 % de '
            'las semanas transcurrió con antidepresivo sin estabilizador y el 0,9 % con estabilizador sin antidepresivo. El '
            'tratamiento no se correlacionó con la cronicidad.']),
        dict(title='Predictores de cronicidad', pill='E · P13', body=[
            'En el bipolar II: episodio índice de dos años o más (65,1 % de semanas con síntomas frente a 41,8 % si duró menos de seis '
            'meses), antecedente afectivo en familiares de primer grado y mal funcionamiento social previo. La hipomanía de 2–6 días '
            'no se distinguió de la de 7 o más.']),
        dict(title='I · Qué cambia en el atlas', pill='I', body=[
            'Las láminas 10–18 dibujan episodios; estos datos recuerdan que la mayor parte del curso transcurre por debajo del umbral '
            'sindrómico. Los autores advierten de que las reglas de codificación tienden a infraestimar las semanas subsindrómicas.']),
    ], t1 + 14, X3, where='p113', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 114 · episodios a diez años
def p114():
    n = 114
    it = new_page('Episodios a diez años: fenotipo, comorbilidad y tratamiento', 'TEXTOS · CURSO II',
                  'E · P178 (tablas 2–5) | I · ¿espectro o trastornos distintos? | relación con pp. 22, 52 y 113', n)
    subtitle(it, 'Los diez años posteriores al episodio índice muestran más episodios depresivos en el bipolar II y más ciclados en el bipolar I.')
    t0, t1 = 128.0, 450.0
    panel(it, 50, t0, 590, t1, 'Pacientes con al menos un episodio de cada tipo (%)', accent=NAVY)
    pairs(it, 68, t0 + 70, 44.0, [('Depresión mayor', 50.0, 73.9), ('Depresión menor', 32.9, 60.9), ('Ciclado o mixto', 51.2, 30.4),
                                   ('Hipomaníaco', 30.5, 17.4), ('Maníaco', 31.7, None)], 3.6, 150, NAVY, OCHRE, lsize=11)
    key2(it, 68, t0 + 276, 'bipolar I, n = 82', NAVY, 'bipolar II, n = 46', OCHRE)
    it.append(text(68, t1 - 12, 'Fin de episodio: ocho semanas consecutivas sin síntomas o con síntomas mínimos. Hipomaníaco: p = 0,14.',
                   'Roboto-Regular', 9.2, GRAY))
    gx0 = 612.0
    panel(it, gx0, t0, 1141, t1, 'Porcentaje de semanas en episodio, media (%)', accent=PURPLE)
    pairs(it, gx0 + 18, t0 + 70, 44.0, [('Depresión mayor', 5.8, 17.4), ('Depresión menor', 2.3, 8.2), ('Ciclado o mixto', 16.3, 7.8),
                                         ('Cualquier episodio', 26.5, 32.7)], 8.0, 150, NAVY, OCHRE, lsize=11)
    lines_block(it, gx0 + 18, t0 + 240, ['Duración mediana: depresión mayor 12 y 13 semanas; manía 6; episodio ciclado o mixto 45 y 56.',
                                          'Intervalo libre mediano: 50 semanas en el bipolar I y 42 en el II (p = 0,076).',
                                          'Con tratamiento entre episodios: 68,6 % de las semanas frente a 44,0 % (p = 0,0006).'],
                size=10, lead=14.2, color=INK)
    it.append(text(gx0 + 18, t1 - 12, 'Las distribuciones son muy asimétricas: las medianas son mucho menores que las medias.',
                   'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Episodio índice', pill='E · P178', body=[
            'Bipolar I: 91,8 % ingresados y 54,8 % con rasgos psicóticos; bipolar II: 54,9 % y 18,3 %. La duración mediana del episodio '
            'tras el ingreso fue de 18 semanas frente a 34. El primer episodio de la vida fue depresivo en el 60,7 % y el 63,4 %.']),
        dict(title='Comorbilidad', pill='E · P178', body=[
            'Algún trastorno de ansiedad: 23,7 % frente a 38,0 % (p = 0,036), sobre todo fobias. Alcoholismo, 41,5 % y 33,8 %, y otras '
            'sustancias, 21,5 % y 15,5 %, sin diferencias. Recuperación funcional completa entre episodios: 63,3 % frente a 47,5 %.']),
        dict(title='I · Espectro con dos subtipos', pill='I · P178', body=[
            'Los autores concluyen que la semejanza demográfica y de inicio apoya un espectro, y que las diferencias de curso '
            'justifican mantener dos subtipos. El bipolar II no es la forma leve: es más crónico y recibe menos tratamiento.']),
    ], t1 + 14, X3, where='p114', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 115 · discapacidad
def p115():
    n = 115
    it = new_page('Discapacidad psicosocial según el nivel de síntomas', 'TEXTOS · FUNCIÓN',
                  'E · P58 (figura y tablas 2–4, texto completo) | I · la depresión incapacita tanto como la manía | relación con p. 44', n)
    subtitle(it, 'La discapacidad sube peldaño a peldaño con la gravedad de los síntomas y vuelve casi a la normalidad en los meses sin síntomas.')
    t0, t1 = 128.0, 530.0
    panel(it, 50, t0, 760, t1, 'Deterioro LIFE-RIFT (4 = ninguno, 20 = grave) por estado mensual', accent=TEAL)
    rows = [('Sin síntomas', 8.8, 8.7), ('Hipomanía subsindrómica', 9.6, 7.4), ('Depresión subsindrómica', 10.3, 9.9),
            ('Hipomanía', 11.4, 8.6), ('Depresión menor o distimia', 12.7, 12.2), ('Manía', 14.0, None), ('Depresión mayor', 15.0, 14.7),
            ('Mixto: depresión mayor y manía', 15.4, 14.3)]
    pairs(it, 68, t0 + 66, 37.0, rows, 26.0, 220, NAVY, OCHRE, lsize=10.8, fmt='%.1f', ref=(7.4, TEAL))
    ctext(it, 68 + 220 + 7.4 * 26.0, t0 + 44, 'controles sanos 7,4', 'Roboto-Medium', 9, TEAL)
    key2(it, 68, t1 - 34, 'bipolar I, n = 158', NAVY, 'bipolar II, n = 133', OCHRE)
    it.append(text(68, t1 - 12, 'Seguimiento medio de 15 años. En el bipolar II, el último tramo es depresión mayor con síntomas hipomaníacos.',
                   'Roboto-Regular', 9.2, GRAY))
    t = card(it, 782, t0, 1141, title='Escalones significativos', pill='E · P58', body=[
        'Cada nivel depresivo superó al anterior en ambos subtipos (p < 0,001). La hipomanía subsindrómica no difirió del estado '
        'asintomático. La depresión menor incapacitó más que la hipomanía en los dos subtipos.'], where='p115', bsize=11.0, lead=15.6) + 10
    t = card(it, 782, t, 1141, title='Hipomanía del bipolar II', pill='E · P58', body=[
        'Con hipomanía, o con síntomas hipomaníacos subsindrómicos, los pacientes bipolar II no estuvieron más deteriorados que los '
        'controles sanos (p = 0,11 y 0,77). Solo en hipomanía el bipolar I estuvo más afectado que el II.'],
             where='p115', bsize=11.0, lead=15.6) + 10
    card(it, 782, t, 1141, t1=t1, title='Residuo sin síntomas', pill='E · P58', body=[
        'En los meses asintomáticos el funcionamiento fue bueno, pero algo peor que el de los controles (p < 0,001). El trabajo fue el '
        'dominio más sensible.'], where='p115', bsize=11.0, lead=15.6)
    card_row(it, [
        dict(title='Lectura', pill='I · P58', body=[
            'La correlación entre gravedad sintomática y deterioro fue de 0,70 y 0,67: los síntomas explican la mitad de la varianza o '
            'menos. Los meses mixtos no incapacitaron más que la depresión pura del mismo nivel; el componente depresivo parece '
            'dominar.']),
        dict(title='Cautelas', pill='I', body=[
            'El número de controles difiere dentro del artículo (1.817 en el método, 1.787 en la figura) y no se aplicó corrección por '
            'comparaciones múltiples. No se analizaron comorbilidad, psicosis ni tratamiento. La dirección causal entre síntomas y '
            'deterioro queda abierta.']),
    ], t1 + 14, X2, where='p115', bsize=11.0, lead=15.6, accent=OCHRE, fill=NOTEFILL)
    return it


# ------------------------------------------------------------------ 116 · síntomas maníacos subumbrales
def p116():
    n = 116
    it = new_page('Síntomas maníacos subumbrales en la depresión bipolar', 'TEXTOS · MIXTICIDAD',
                  'E · P179 (tablas 2–5) | H · subgrupos pequeños, sin corrección múltiple | relación con pp. 29, 98–99 y 103–104', n)
    subtitle(it, 'Tres de cada cuatro episodios depresivos bipolares tuvieron algún síntoma maníaco clínicamente apreciable, sobre todo irritabilidad y agitación.')
    t0, t1 = 128.0, 470.0
    panel(it, 50, t0, 540, t1, 'Síntomas maníacos en 142 episodios depresivos', accent=RED)
    hrows(it, 68, t0 + 62, 28.0, [('Irritabilidad manifiesta', 57.0, RED), ('Agitación psicomotriz', 39.4, RED), ('Ánimo elevado', 13.4, LILA),
                                   ('Energía aumentada', 11.3, LILA), ('Más actividad dirigida', 9.9, LILA), ('Menor necesidad de sueño', 8.5, LILA),
                                   ('Fuga de ideas', 7.7, LILA), ('Distraibilidad', 6.3, LILA), ('Grandiosidad', 4.9, LILA)], 4.2, 170)
    lines_block(it, 68, t1 - 26, ['76,1 % con al menos un síntoma (108 de 142); 23,9 % depresión pura.',
                                   'Bipolar I, 52 pacientes; bipolar II, 90. Seguimiento de hasta 27 años.'], size=9.2, lead=12.6)
    gx0 = 562.0
    panel(it, gx0, t0, 1141, t1, 'Intentos de suicidio con y sin síntomas maníacos (%)', accent=NAVY)
    pairs(it, gx0 + 18, t0 + 70, 44.0, [('Antes del episodio', 53.7, 32.3), ('Durante el episodio índice', 38.9, 11.8),
                                         ('Durante el seguimiento', 58.3, 35.3), ('Graves o consumados después', 40.7, 20.6)],
          5.0, 190, RED, AZUL2, lsize=11)
    key2(it, gx0 + 18, t0 + 232, 'con síntomas maníacos, n = 108', RED, 'depresión pura, n = 34', AZUL2)
    lines_block(it, gx0 + 18, t0 + 262, ['Duración mediana del episodio: 28 frente a 14,5 semanas (p = 0,077).',
                                          'Probabilidad de durar un año o más: 0,40 frente a 0,19.',
                                          'Suicidios consumados: 7 (6,5 %) y 2 (5,9 %).'], size=10, lead=14.2, color=INK)
    it.append(text(gx0 + 18, t1 - 12, 'Todas las diferencias de intentos, p < 0,05. Análisis exploratorio.', 'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Irritabilidad frente a agitación', pill='E · H · P179', body=[
            'Solo irritabilidad (37): episodio mediano de 39 semanas y más intentos graves posteriores. Solo agitación (17): mayor '
            'gravedad depresiva y más intentos durante el episodio. Ambas (21): 81 % con intento previo y mediana de 96 semanas.']),
        dict(title='Viraje dentro del episodio', pill='E · P179', body=[
            'Ningún paciente con depresión pura viró a manía o hipomanía durante el episodio índice. Los 17 episodios que ciclaron '
            'tenían síntomas maníacos concurrentes.']),
        dict(title='I · Lugar en el atlas', pill='I', body=[
            'Es la base empírica del «estado mixto depresivo» por debajo del umbral DSM (p. 103). No evalúa la adecuación del '
            'tratamiento; no permite inferir el efecto de los antidepresivos.']),
    ], t1 + 14, X3, where='p116', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 117 · riesgo de nuevo episodio
def p117():
    n = 117
    it = new_page('Riesgo de un nuevo episodio tras el episodio índice', 'TEXTOS · RECAÍDA',
                  'E · P180 (metaanálisis de 12 estudios naturalistas, 5.837 pacientes) | I · relación con pp. 45, 60–61 y 74', n)
    subtitle(it, 'El riesgo se concentra en el primer año, sigue la polaridad del episodio índice y se duplica con síntomas subsindrómicos.')
    t0, t1 = 128.0, 450.0
    panel(it, 50, t0, 400, t1, 'Riesgo acumulado en adultos', accent=RED)
    vbars(it, 96, t1 - 92, 76, 54, [44, 70], 80, 190, [RED, NAVY], ['primer año', 'cinco años'])
    lines_block(it, 68, t1 - 40, ['4.159 adultos reclutados en un episodio; mediana hasta', 'el nuevo episodio, 1,44 años. Sin episodio en el primer',
                                   'año: 19 % en el segundo; sin él en dos años: 21 %.'], size=9.4, lead=12.8)
    panel(it, 422, t0, 772, t1, 'Polaridad del siguiente episodio (bipolar I)', accent=PURPLE)
    for k, (lab, parts) in enumerate((('Tras manía', [(56.6, RED, 'manía'), (30.8, BLUE, 'depr.'), (12.5, PURPLE, 'mixto')]),
                                      ('Tras depresión', [(40.5, RED, 'manía'), (54.1, BLUE, 'depr.'), (5.4, PURPLE, '')]),
                                      ('Tras episodio mixto', [(26.1, RED, 'manía'), (28.0, BLUE, 'depr.'), (45.9, PURPLE, 'mixto')]))):
        ta = t0 + 56 + 84 * k
        it.append(text(440, ta, lab, 'Roboto-Bold', 10.8, NAVY))
        split_bar(it, 440, 754, ta + 8, parts, h=20)
    it.append(text(440, t1 - 12, 'Polaridad desconocida en el 20,2 % de los episodios.', 'Roboto-Regular', 9.2, GRAY))
    panel(it, 794, t0, 1141, t1, 'Razones de riesgo (escala log)', accent=NAVY)
    rows = [('Síntomas subsindrómicos', 2.17, 1.77, 2.65, RED), ('Bipolar II frente a I', 1.49, 1.21, 1.84, PURPLE),
            ('Índice depresivo frente a maníaco', 1.41, 1.16, 1.71, BLUE), ('Adolescentes frente a adultos', 0.67, 0.54, 0.83, TEAL),
            ('Reclutados en eutimia', 0.63, 0.58, 0.70, TEAL)]
    lforest(it, 1000, 1090, t0 + 82, 46.0, rows, 0.5, 4.0, [0.5, 1, 2, 4], zero=1.0, fmt='%.2f', label_w=190, lsize=9.6, log=True,
            show_val=False)
    for k, r in enumerate(rows):
        it.append(text(812, t0 + 82 + 46.0 * k + 17, num(r[1], '%.2f') + ' [' + num(r[2], '%.2f') + ' a ' + num(r[3], '%.2f') + ']',
                       'Roboto-Medium', 9, GRAY))
    card_row(it, [
        dict(title='Síntomas subsindrómicos', pill='E · P180', body=[
            'En 986 adultos, la mediana hasta el nuevo episodio fue de 0,75 años con síntomas residuales y de 2,30 sin ellos. Los '
            'autores proponen reservar «eutimia» para un estado mental positivo, no para la mera ausencia de episodio.']),
        dict(title='La polaridad llama a la polaridad', pill='E · P180', body=[
            'Tras un episodio mixto, el riesgo de otro mixto fue 4,26 veces el observado tras manía. El bipolar II recayó antes y sobre '
            'todo en depresión (HR 4,73 frente al bipolar I). Enlaza con la polaridad predominante (p. 45).']),
        dict(title='Cautelas', pill='I · P180', body=[
            'La mayoría de los datos del bipolar II procede de un solo estudio, con muchos ingresados. No se analizaron tratamiento ni '
            'comorbilidad; 63 de 75 estudios elegibles quedaron fuera. Dos estudios incluidos fueron patrocinados por un fabricante.']),
    ], t1 + 14, X3, where='p117', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 118 · dinámica momentánea
ST = [('Sin síntomas', 54.7, 4.4), ('Depresión subumbral', 49.7, 8.2), ('Depresión clínica', 26.7, 25.9),
      ('Hipomanía subclínica', 25.2, 10.0), ('Hipomanía o manía clínica', 16.4, 9.8), ('Cosíntomas subumbrales', 44.5, 20.2),
      ('Manía clínica + depr. subumbral', 14.7, 26.2), ('Mixto leve', 37.4, 60.1), ('Mixto moderado', 42.1, 68.4),
      ('Mixto de rango clínico', 37.0, 75.0)]


def p118():
    n = 118
    it = new_page('Dinámica momentánea de las configuraciones mixtas', 'TEXTOS · MIXTICIDAD DINÁMICA',
                  'E · P184 (evaluación ecológica momentánea, 50 personas, 9.676 registros) | G · estados definidos a priori | relación con pp. 29, 50–51 y 103', n)
    subtitle(it, 'Registros dos veces al día muestran que lo mixto nace y termina casi siempre en un contexto depresivo, y que rara vez dura días enteros.')
    t0, t1 = 128.0, 530.0
    panel(it, 50, t0, 690, t1, 'Diez estados: permanencia y paso a un estado mixto en el registro siguiente', accent=PURPLE)
    pairs(it, 68, t0 + 62, 30.6, ST, 4.2, 220, AZUL2, PURPLE, lsize=10.4, fmt='%.1f')
    key2(it, 68, t1 - 34, 'sigue en el mismo estado (%)', AZUL2, 'pasa a un estado mixto o sigue en él (%)', PURPLE)
    it.append(text(68, t1 - 12, '9.627 transiciones; intervalo mediano de 12,7 horas. Mixto: depresión de rango clínico más algún síntoma maníaco.',
                   'Roboto-Regular', 9.2, GRAY))
    gx0 = 712.0
    panel(it, gx0, t0, 1141, 316.0, 'Entrada en lo mixto frente a «sin síntomas» (OR)', accent=RED)
    rows = [('Depresión clínica', 4.37, 3.07, 6.21, RED), ('Manía clín. + depr. subumbral', 3.33, 2.10, 5.28, PURPLE),
            ('Cosíntomas subumbrales', 3.03, 2.17, 4.21, PURPLE), ('Hipomanía subclínica', 1.69, 1.10, 2.62, GRAY),
            ('Depresión subumbral', 1.68, 1.20, 2.36, BLUE), ('Manía clínica aislada', 1.30, 0.53, 3.21, GRAY)]
    lforest(it, gx0 + 190, 1030, t0 + 58, 22.0, rows, 0.5, 8.0, [0.5, 1, 2, 4, 8], zero=1.0, fmt='%.2f', label_w=175, lsize=9.4, log=True)
    panel(it, gx0, 330.0, 1141, t1, 'Días seguidos con estado mixto clínico', accent=NAVY)
    vbars(it, gx0 + 36, t1 - 52, 40, 22, [50.0, 32.7, 18.4, 14.3, 8.2, 6.1], 60, 70, [NAVY] * 6, ['2', '3', '4', '5', '6', '7'], lsize=9.5)
    it.append(text(gx0 + 18, t1 - 12, 'Porcentaje de participantes; ninguno llegó a 14 días.', 'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Contexto depresivo', pill='E · P184', body=[
            'El 88,6 % de las 925 entradas en lo mixto vino de estados con depresión, y el 88,6 % de las 932 salidas volvió a ellos. De 493 '
            'secuencias completas, el 77,7 % tuvo depresión a ambos lados.']),
        dict(title='Asimetría temporal', pill='E · P184', body=[
            'En registros separados por menos de 12 horas, la depresión predijo los síntomas maníacos posteriores (β 0,077) más que a la '
            'inversa (β 0,026, no significativo). Los autores no lo presentan como relación causal.']),
        dict(title='Cautelas', pill='I · P184', body=[
            'Diagnóstico autorreferido, reclutamiento por redes sociales y respuesta al 47,4 % de los avisos. La definición exige '
            'depresión clínica, lo que acerca por construcción los estados depresivos a lo mixto. No son estados DSM.']),
    ], t1 + 14, X3, where='p118', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 119 · pródromo dimensional
def p119():
    n = 119
    it = new_page('Pródromo dimensional en descendencia de riesgo', 'TEXTOS · PRÓDROMO',
                  'E · P181 (cohorte BIOS, tablas 2–3 y modelo de rutas) | H · solo riesgo familiar | relación con pp. 42 y 107', n)
    subtitle(it, 'Labilidad afectiva, ansiedad-depresión y síntomas maníacos subumbrales predicen el inicio mejor que los diagnósticos categoriales.')
    t0, t1 = 128.0, 470.0
    panel(it, 50, t0, 700, t1, 'Predictores de inicio del espectro bipolar, por desviación típica (escala log)', accent=PURPLE)
    it.append(text(68, t0 + 52, 'Al inicio del seguimiento (HR)', 'Roboto-Bold', 10.5, NAVY))
    rows = [('Internalización (progenitor)', 1.78, 1.37, 2.31, PURPLE), ('Externalización (hijo)', 1.78, 1.21, 2.63, PURPLE),
            ('Labilidad afectiva (hijo)', 1.66, 1.27, 2.18, PURPLE), ('Escala de manía', 1.21, 0.93, 1.58, GRAY),
            ('Problemas de sueño', 0.98, 0.75, 1.28, GRAY)]
    lforest(it, 300, 560, t0 + 72, 24.0, rows, 0.5, 4.0, [0.5, 1, 2, 4], zero=1.0, fmt='%.2f', lsize=10, log=True)
    it.append(text(68, t0 + 204, 'En la visita previa a la conversión (OR)', 'Roboto-Bold', 10.5, NAVY))
    rows2 = [('Escala de manía', 2.14, 1.55, 2.94, RED), ('Externalización (progenitor)', 1.91, 1.36, 2.68, RED),
             ('Labilidad afectiva (hijo)', 1.82, 1.31, 2.52, RED), ('Problemas de sueño', 1.40, 1.04, 1.88, OCHRE)]
    lforest(it, 300, 560, t0 + 224, 24.0, rows2, 0.5, 4.0, [0.5, 1, 2, 4], zero=1.0, fmt='%.2f', lsize=10, log=True)
    it.append(text(68, t1 - 12, '44 de 299 hijos de riesgo (14,7 %) desarrollaron el espectro en unos ocho años; 15 de ellos, bipolar I o II.',
                   'Roboto-Regular', 9.2, GRAY))
    gx0 = 722.0
    panel(it, gx0, t0, 1141, t1, 'Riesgo predicho de conversión', accent=RED)
    vbars(it, gx0 + 90, t1 - 120, 90, 60, [2, 49], 55, 170, [AZUL2, RED], ['perfil\nbajo', 'perfil\nalto'])
    lines_block(it, gx0 + 18, t1 - 66, ['Perfil alto: labilidad, ansiedad-depresión y síntomas', 'maníacos una desviación típica por encima de la media,',
                                         'y progenitor con inicio precoz del trastorno del ánimo.', 'Edad de inicio parental: 11 frente a 29 años.'],
                size=9.6, lead=13.2)
    card_row(it, [
        dict(title='Dos tiempos', pill='E · H · P181', body=[
            'Un pródromo inicial, con ansiedad-depresión y labilidad afectiva, y otro proximal, con síntomas maníacos subumbrales en '
            'ascenso y labilidad persistente. La labilidad inicial conduce a más síntomas maníacos proximales y estos, a la conversión.']),
        dict(title='Qué no predijo', pill='E · P181', body=[
            'Al inicio, ni los síntomas maníacos ni el sueño predijeron la conversión; lo hicieron solo en la visita proximal. Dentro de '
            'la escala de manía pesaron irritabilidad, hiperactividad y distraibilidad; la euforia, no en el modelo conjunto.']),
        dict(title='Cautelas', pill='I · P181', body=[
            'Más de la mitad de los jóvenes con el perfil alto no convirtió. Visitas cada dos años; pocos casos de bipolar I o II; edad '
            'media inicial inferior a 12 años. Los tamaños muestrales difieren entre el manuscrito y el resumen publicado.']),
    ], t1 + 14, X3, where='p119', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 120 · estadiaje MNF
MNF = [('0', ['Riesgo: familiar de 1.er o 2.º', 'grado con trastorno bipolar,', 'sin síntomas afectivos'], ['Sin síntomas no afectivos'],
        ['Sin deterioro']),
       ('1', ['Con riesgo familiar: 1a síntomas', 'subsindrómicos homotípicos; 1b primera', 'depresión mayor; 1c depresión recurrente.',
              '1d espectro bipolar subumbral'], ['Síntomas no afectivos', 'subsindrómicos (heterotípicos)'], ['Deterioro leve']),
       ('2', ['Primer episodio maníaco o', 'hipomaníaco con diagnóstico', 'de bipolar I o II'], ['Un trastorno no afectivo'],
        ['Deterioro moderado']),
       ('3', ['Recurrencias: 3a sin síntomas', 'entre episodios; 3b con síntomas', 'subsindrómicos entre episodios'],
        ['Dos trastornos no afectivos'], ['Deterioro marcado']),
       ('4', ['Trastorno bipolar crónico,', 'sin remisión (incluye ciclación', 'rápida de dos años o más)'],
        ['Tres o más trastornos', 'no afectivos'], ['Deterioro grave'])]


def p120():
    n = 120
    it = new_page('Estadiaje tridimensional MNF del consenso ISBD', 'TEXTOS · ESTADIOS',
                  'F/H · consenso de expertos (P182, tabla 1) | H · sin validar | continúa P121 (p. 107) y la p. 54', n)
    subtitle(it, 'El grupo de trabajo de la ISBD propone puntuar por separado el ánimo (M), la psicopatología no afectiva (N) y el funcionamiento (F).')
    t0, t1 = 128.0, 568.0
    panel(it, 50, t0, 1141, t1, 'Tres dimensiones, cinco estadios cada una, en cualquier combinación', accent=PURPLE)
    cx = [(120.0, 520.0, 'M · Psicopatología afectiva', PURPLE), (540.0, 820.0, 'N · Psicopatología no afectiva', BLUE),
          (840.0, 1123.0, 'F · Deterioro funcional', TEAL)]
    for xa, xb, lab, col in cx:
        it.append(rect_top(xa, t0 + 46, xb, t0 + 70, 5, fill=col))
        ctext(it, (xa + xb) / 2, t0 + 63, lab, 'Roboto-Bold', 11, WHITE)
    rh = 68.0
    for k, (st, m, nn, f) in enumerate(MNF):
        ta = t0 + 78 + rh * k
        it.append(rect_top(68, ta, 108, ta + rh - 6, 6, fill=NAVY))
        ctext(it, 88, ta + rh / 2 + 3, st, 'Roboto-Bold', 18, WHITE)
        for (xa, xb, lab, col), lines in zip(cx, (m, nn, f)):
            it.append(rect_top(xa, ta, xb, ta + rh - 6, 5, fill=PALE))
            lines_block(it, xa + 10, ta + 17, lines, size=9.8, lead=12.6, color=INK)
    it.append(text(68, t1 - 12, 'M0 y M1a–c solo se aplican a personas con riesgo familiar. F se valora fuera del episodio agudo. Clasificación según DSM-5-TR o CIE-11.',
                   'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Ejemplos del consenso', pill='F · P182', body=[
            'Mujer de 46 años, dos depresiones y una manía, bien con litio: M3a–N0–F0. Varón de 51, bipolar I desde los 21, ciclación '
            'rápida de cuatro años, alcohol y pánico, en residencia: M4–N3–F4. Los estadios pueden retroceder.']),
        dict(title='Lo que queda sin acuerdo', pill='H · P182', body=[
            'Situar la depresión mayor de personas con riesgo como estadio previo, incluir la enfermedad somática y separar la cognición '
            'del funcionamiento. Respondieron 14 y 18 de 27 miembros a las dos encuestas; el consenso fue por mayoría simple.']),
        dict(title='I · Uso en el atlas', pill='I', body=[
            'Es una notación, no una escala validada: carece de puntos de corte para F y no pondera la gravedad en N. Complementa los '
            'estadios empíricos de la p. 107 y ordena la comorbilidad de las pp. 36–39.']),
    ], t1 + 14, X3, where='p120', bsize=11.0, lead=15.6)
    return it


# ------------------------------------------------------------------ 121 · genómica 2025
GL = ['Clínico', 'Comunitario', 'Autoinforme', 'Bipolar I', 'Bipolar II']
GV = {(0, 1): 0.95, (1, 2): 0.79, (0, 2): 0.47, (3, 4): 0.88, (1, 3): 0.85, (1, 4): 0.95, (2, 3): 0.42, (2, 4): 0.76}


def p121():
    n = 121
    it = new_page('Genómica multiancestral del trastorno bipolar', 'TEXTOS · GENÉTICA',
                  'E · P183 (158.036 casos, 2,8 millones de controles) | I · la arquitectura depende de cómo se identifica el caso | relación con pp. 100–102 y 110', n)
    subtitle(it, 'El mayor estudio hasta la fecha cuadruplica los loci y muestra que los casos autorreferidos se parecen genéticamente más al bipolar II.')
    t0, t1 = 128.0, 520.0
    panel(it, 50, t0, 600, t1, 'Correlación genética según origen del caso y subtipo', accent=PURPLE)
    x0, y0, cs = 170.0, t0 + 78, 56.0
    for j, lab in enumerate(GL):
        ctext(it, x0 + cs * j + cs / 2, y0 - 10, lab, 'Roboto-Bold', 8.2, NAVY)
        it.append(text(68, y0 + cs * j + cs / 2 + 4, lab, 'Roboto-Bold', 9.6, NAVY))
        for i in range(5):
            xa, ya = x0 + cs * j, y0 + cs * i
            if i == j:
                it.append(rect_top(xa + 2, ya + 2, xa + cs - 2, ya + cs - 2, 5, fill=(0.85, 0.85, 0.85)))
                continue
            v = GV.get((min(i, j), max(i, j)))
            if v is None:
                it.append(rect_top(xa + 2, ya + 2, xa + cs - 2, ya + cs - 2, 5, fill=WHITE, stroke=LINE, lw=1.0))
                ctext(it, xa + cs / 2, ya + cs / 2 + 4, 'n. d.', 'Roboto-Regular', 9, GRAY)
                continue
            f = (v - 0.3) / 0.7
            col = (0.95 - 0.55 * f, 0.93 - 0.68 * f, 0.97 - 0.40 * f)
            it.append(rect_top(xa + 2, ya + 2, xa + cs - 2, ya + cs - 2, 5, fill=col))
            ctext(it, xa + cs / 2, ya + cs / 2 + 5, num(v, '%.2f'), 'Roboto-Bold', 12.5, WHITE if v > 0.6 else INK)
    lines_block(it, 466, t0 + 100, ['n. d.: el texto', 'no da el valor.', '', 'Errores típicos', 'entre 0,02 y 0,06.'], size=9.4, lead=13,
                color=INK)
    it.append(text(68, t1 - 12, 'Clínico–autoinforme 0,47 frente a comunitario–autoinforme 0,79 (p = 7,4 × 10⁻²⁸).', 'Roboto-Regular', 9.2, GRAY))
    gx0 = 622.0
    panel(it, gx0, t0, 1141, 316.0, 'Heredabilidad por SNP, escala de susceptibilidad', accent=TEAL)
    hrows(it, gx0 + 18, t0 + 60, 24.0, [('Casos clínicos', 22, TEAL), ('Bipolar I', 21, TEAL), ('Bipolar II', 11, AZUL2),
                                         ('Autoinforme', 8, AZUL2), ('Casos comunitarios', 5, AZUL2)], 11.0, 150)
    panel(it, gx0, 330.0, 1141, t1, 'Loci significativos', accent=NAVY)
    hrows(it, gx0 + 18, 330.0 + 62, 28.0, [('Estudio previo (P106)', 64, AZUL2), ('Europeos sin autoinforme', 88, AZUL2),
                                            ('Europeos con autoinforme', 221, NAVY), ('Multiancestral', 298, NAVY)], 1.0, 170, suffix='')
    it.append(text(gx0 + 18, t1 - 12, '267 de los 298 son nuevos. Ascendencia europea: 82,3 % del tamaño efectivo.', 'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Genes y tipos celulares', pill='E · P183', body=[
            '36 genes creíbles, apoyados por tres o más de siete métodos (SP4, TTC12, MED24, entre otros); ocho con función sináptica. '
            'La heredabilidad se concentra en interneuronas GABAérgicas y neuronas espinosas medianas, sin señal en células no '
            'neuronales. Los genes de mapeo fino acumulan variantes raras dañinas (OR 1,16).']),
        dict(title='Puntuación poligénica', pill='E · P183', body=[
            'Explica el 9,0 % de la varianza en europeos sin datos autorreferidos y el 5,8 % con ellos; quintil superior frente al '
            'intermedio, OR 7,06; AUC mediana 0,70. Los autores afirman que aún no alcanza utilidad clínica.']),
        dict(title='I · Lectura nosológica', pill='I · P183', body=[
            'Con autoinforme, el trastorno que más se correlaciona es la depresión mayor; sin él, la esquizofrenia. La composición de '
            'subtipos de cada muestra decide qué «frontera» parece más cercana: coherente con el gradiente de la p. 100.']),
    ], t1 + 14, X3, where='p121', bsize=10.8, lead=15.2)
    return it


# ------------------------------------------------------------------ 122 · viraje y sistemas dinámicos
def p122():
    n = 122
    it = new_page('Viraje entre estados: disparadores y modelos', 'TEXTOS · VIRAJE',
                  'E/H · revisión narrativa, con base preclínica (P185) | H · sistemas dinámicos (P186) | relación con pp. 24, 31, 42–43 y 102', n)
    subtitle(it, 'Los disparadores conocidos empujan mucho más hacia la manía que hacia la depresión; los modelos explicativos siguen siendo hipótesis.')
    t0, t1 = 128.0, 470.0
    panel(it, 50, t0, 660, t1, 'Hacia la manía o la hipomanía', accent=RED)
    up = [('Antidepresivos tricíclicos', '9–69 %'), ('Bupropión', 'hasta 19 %'), ('Corticoides y eje suprarrenal', '30–80 %'),
          ('Privación total de sueño', 'hasta 30 %'), ('Anfetamina, levodopa', 'descrito'), ('Primavera y verano', '23 de 29 estudios'),
          ('Ruptura de ritmos sociales, sucesos vitales', 'descrito')]
    for k, (lab, v) in enumerate(up):
        yb = t0 + 64 + 36 * k
        it.append(rect_top(68, yb - 14, 642, yb + 14, 6, fill=PALE))
        it.append(text(80, yb + 4, lab, 'Roboto-Medium', 10.8, INK))
        wv = sw(v, 'Roboto-Bold', 10.5) + 20
        it.append(rect_top(630 - wv, yb - 10, 630, yb + 10, 10, fill=RED))
        ctext(it, 630 - wv / 2, yb + 4, v, 'Roboto-Bold', 10.5, WHITE)
    it.append(text(68, t1 - 12, 'Cifras citadas por la revisión, de estudios heterogéneos; no son tasas comparables entre sí.', 'Roboto-Regular', 9.2, GRAY))
    gx0 = 682.0
    panel(it, gx0, t0, 1141, 300.0, 'Hacia la depresión', accent=BLUE)
    dn = ['Fisostigmina (aumento de acetilcolina)', 'Estrés e hiperactividad del eje suprarrenal', 'Otoño e invierno (fotoperiodo corto)']
    for k, lab in enumerate(dn):
        yb = t0 + 64 + 36 * k
        it.append(rect_top(gx0 + 18, yb - 14, 1123, yb + 14, 6, fill=PALE))
        it.append(text(gx0 + 30, yb + 4, lab, 'Roboto-Medium', 10.8, INK))
    panel(it, gx0, 314.0, 1141, t1, 'Sin asociación descrita con el viraje', accent=TEAL)
    lines_block(it, gx0 + 18, 314.0 + 58, ['Lamotrigina y riluzol no aumentaron el viraje en la', 'depresión bipolar; no se describen virajes a manía',
                                            'con ketamina. La revisión considera improbable', 'una vía glutamatérgica del viraje.'],
                size=10.4, lead=14.4, color=INK)
    it.append(text(gx0 + 18, t1 - 12, 'La tabla original no pudo leerse: listas tomadas del texto.', 'Roboto-Regular', 9.2, GRAY))
    card_row(it, [
        dict(title='Modelo catecolaminérgico-colinérgico', pill='H · P185', body=[
            'Manía como fallo de la homeostasis catecolaminérgica y depresión como exceso colinérgico. En ratas, una semana de '
            'fotoperiodo alterado cambió el neurotransmisor de neuronas hipotalámicas (dopamina por somatostatina, y a la inversa). '
            'Es un modelo animal: su traslado a personas es una hipótesis.']),
        dict(title='Sistemas dinámicos', pill='H · P186', body=[
            'Los trastornos como estados alternativos estables. Antes de un cambio, el sistema se recupera más despacio: aumentan la '
            'varianza y la autocorrelación del ánimo. Propone medir esa resiliencia con registros momentáneos (p. 118) y aprovechar '
            'ventanas de oportunidad. Revisión conceptual, casi sin datos.']),
        dict(title='I · Lectura en el atlas', pill='I', body=[
            'Aporta mecanismos posibles para el curso inducido (pp. 24 y 31) y los pródromos de sueño (pp. 42–43). En un estudio '
            'prospectivo citado, sexo, edad y antecedente familiar no predijeron el viraje; el número de hospitalizaciones previas, sí.']),
    ], t1 + 14, X3, where='p122', bsize=10.8, lead=15.2)
    return it


# ------------------------------------------------------------------ 123 · rasgos límite y sustancias
def p123():
    n = 123
    it = new_page('Rasgos límite elevados y trayectorias de consumo', 'TEXTOS · COMORBILIDAD',
                  'E · P188 (520 pacientes, Corea del Sur), P187 (primer tratamiento, Noruega) | I · asociación, no causalidad | relación con pp. 36–38 y 109', n)
    subtitle(it, 'Los rasgos límite elevan la carga depresiva sin cambiar el ritmo de mejoría; seguir con el alcohol casi duplica las recaídas.')
    t0, t1 = 128.0, 480.0
    panel(it, 50, t0, 600, t1, 'Rasgos límite elevados: asociaciones ajustadas (OR, escala log)', accent=PURPLE)
    rows = [('Agorafobia', 3.12, 1.43, 6.79, PURPLE), ('Trastorno por alcohol', 2.65, 1.35, 5.22, PURPLE),
            ('Violencia alguna vez', 2.58, 1.34, 4.99, PURPLE), ('Intento de suicidio', 2.12, 1.39, 3.22, RED),
            ('Autolesión', 1.98, 1.28, 3.07, RED), ('Ideación fuera de los episodios', 1.68, 1.11, 2.56, RED),
            ('Respuesta a 6 meses', 0.40, 0.18, 0.91, TEAL)]
    lforest(it, 290, 480, t0 + 64, 32.0, rows, 0.125, 8.0, [0.125, 0.5, 1, 2, 8], zero=1.0, fmt='%.2f', lsize=10, log=True)
    lines_block(it, 68, t1 - 40, ['237 de 520 pacientes (45,5 %) superaron el punto de corte de un cuestionario (PAI-BOR de 38 o más):',
                                   'no es un diagnóstico de trastorno límite. Eran más jóvenes, más a menudo bipolar II (78,9 % frente a 47,0 %)',
                                   'y estaban más a menudo deprimidos al evaluarse, lo que puede inflar la puntuación.'], size=9.2, lead=12.6)
    gx0 = 622.0
    panel(it, gx0, t0, 1141, 300.0, 'Depresión (MADRS) a lo largo de seis meses', accent=NAVY)
    xs = [gx0 + 80, gx0 + 250, gx0 + 420]
    base, sc = 300.0 - 40, 4.8
    for vals, col in (((23.29, 18.37, 16.82), PURPLE), ((19.28, 12.85, 11.84), AZUL2)):
        for a in range(2):
            it.append(line_top(xs[a], base - (vals[a] - 8) * sc, xs[a + 1], base - (vals[a + 1] - 8) * sc, stroke=col, lw=2.2))
        for x, v in zip(xs, vals):
            dot(it, x, base - (v - 8) * sc, 4.5, col)
            ctext(it, x, base - (v - 8) * sc - 9, num(v, '%.1f'), 'Roboto-Medium', 9, INK)
    for x, lab in zip(xs, ('inicio', '8 semanas', '6 meses')):
        ctext(it, x, base + 14, lab, 'Roboto-Regular', 9.2, GRAY)
    it.append(line_top(gx0 + 40, base, gx0 + 470, base, stroke=GRAY, lw=1.0))
    key2(it, gx0 + 18, 300.0 - 8, 'con rasgos elevados', PURPLE, 'sin ellos · 302 deprimidos al inicio; eje desde 8 (G)', AZUL2)
    panel(it, gx0, 314.0, 1141, t1, 'Recaída a un año según el consumo de alcohol (P187)', accent=RED)
    vbars(it, gx0 + 60, t1 - 54, 70, 40, [46, 44, 79], 90, 62, [AZUL2, TEAL, RED], ['sin consumo\nde riesgo', 'lo abandona', 'continúa'],
          lsize=9.2)
    lines_block(it, gx0 + 400, 314.0 + 56, ['Continuar frente a', 'no consumir:', 'OR 3,51', '[1,20 a 10,25]'], size=10, lead=13.6, color=INK)
    card_row(it, [
        dict(title='Trayectorias paralelas', pill='E · P188', body=[
            'La diferencia de MADRS se mantuvo en los tres momentos (4,0 puntos en el modelo) sin interacción con el tiempo. La '
            'respuesta a seis meses fue menor (26,1 % frente a 48,7 %); la remisión no difirió de forma significativa. También hubo más '
            'trauma infantil.']),
        dict(title='Alcohol y cannabis', pill='E · P187', body=[
            'De 220 pacientes en primer tratamiento se siguió a 112. Quienes dejaron el consumo de riesgo de alcohol recayeron como '
            'quienes nunca lo tuvieron. Con cannabis la diferencia no fue significativa (46 %, 71 % y 71 %; p = 0,058).']),
        dict(title='Cautelas', pill='I', body=[
            'En P187 se perdió al 49 % de la muestra y varias tablas tienen porcentajes incoherentes con sus denominadores, por lo que '
            'solo se usan las cifras concordantes con el texto. En P188, la pérdida fue diferencial entre grupos.']),
    ], t1 + 14, X3, where='p123', bsize=10.8, lead=15.2)
    return it


# ------------------------------------------------------------------ 124 · predictores, marcadores, bienestar
def p124():
    n = 124
    it = new_page('Predictores de bipolaridad, marcadores y bienestar', 'TEXTOS · MISCELÁNEA',
                  'E · P06 (texto completo), P189–P192 | H · estudios pequeños o preclínicos | relación con pp. 22–23, 26–27, 38 y 110', n)
    subtitle(it, 'Los predictores clásicos del desenlace bipolar son muy específicos y poco sensibles; los marcadores de laboratorio, aún modestos.')
    t0, t1 = 128.0, 502.0
    panel(it, 50, t0, 640, t1, 'Predictores de desenlace bipolar en la depresión (P06, tabla 7)', accent=PURPLE)
    pairs(it, 68, t0 + 66, 40.0, [('Hipomanía farmacológica', 32, 100), ('Antecedente familiar bipolar', 56, 98),
                                   ('Genealogía cargada', 32, 95), ('Depresión con hipersomnia e inhibición', 59, 88),
                                   ('Depresión psicótica', 42, 85), ('Inicio en el posparto', 58, 84), ('Inicio antes de los 26 años', 71, 68)],
          2.6, 250, PURPLE, AZUL2, lsize=10.6)
    key2(it, 68, t1 - 34, 'sensibilidad (%)', PURPLE, 'especificidad (%)', AZUL2)
    it.append(text(68, t1 - 12, 'Revisión narrativa de 2000; valores recopilados de estudios anteriores, sin intervalos.', 'Roboto-Regular', 9.2, GRAY))
    gx0 = 662.0
    panel(it, gx0, t0, 1141, 316.0, 'Analítica habitual: depresión bipolar frente a unipolar (P189)', accent=TEAL)
    hrows(it, gx0 + 18, t0 + 60, 24.0, [('Modelo combinado', 0.724, TEAL), ('Creatina cinasa', 0.621, AZUL2), ('Bilirrubina total', 0.609, AZUL2),
                                         ('Plaquetas', 0.569, AZUL2), ('Tiroxina (T4)', 0.554, AZUL2)], 330.0, 130, suffix='',
          h=11)
    it.append(text(gx0 + 18, 316.0 - 12, 'Área bajo la curva. 87 y 87 pacientes ingresados; retrospectivo, sin validación externa.',
                   'Roboto-Regular', 9.2, GRAY))
    card(it, gx0, 330.0, 1141, t1=t1, title='Estados mixtos en la revisión clásica', pill='E · P06', body=[
        'Trece estudios con 1.167 pacientes: 43 % con estado mixto, con extremos del 14 % al 67 % según criterio. En manía '
        'hospitalizada, 6,7 % con el criterio DSM-IV estricto y 37 % con dos o más síntomas depresivos. Enlaza con la p. 103.'],
         where='p124', bsize=10.8, lead=15.2)
    card_row(it, [
        dict(title='Bienestar: escala WELL-B', pill='E · P190', body=[
            'Codiseñada con pacientes; 192 participantes. Tres factores (bienestar, tiempo, trabajo; alfa 0,95, 0,87 y 0,86). El '
            'bienestar se asoció a menos depresión y ansiedad, no a la manía. Ajuste factorial imperfecto y muestra poco diversa.']),
        dict(title='Exoma y neuroimagen', pill='H · P191', body=[
            '93 pacientes y 161 controles coreanos: carga de variantes raras dañinas en GNB3, y un polimorfismo de KMT2C asociado al '
            'grosor cortical y a la sustancia blanca. Sin réplica; los propios autores piden cautela por la distribución anómala de '
            'genotipos.']),
        dict(title='Estrés y glucosa en ratones', pill='H · P192', body=[
            'El estrés social crónico atenuó la respuesta glucémica y produjo conductas de tipo depresivo; gliburida y liraglutida las '
            'previnieron en parte. Solo machos; sin datos humanos ni relación directa con el trastorno bipolar.']),
    ], t1 + 14, X3, where='p124', bsize=10.8, lead=15.2)
    return it


NEW_PAGES39 = [p113, p114, p115, p116, p117, p118, p119, p120, p121, p122, p123, p124]

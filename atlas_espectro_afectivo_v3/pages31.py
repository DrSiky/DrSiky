"""Contenido de las páginas nuevas (26–42) del Atlas v3.1.

Convención de procedencia: F criterio formal · E hallazgo empírico (con su P##) · I interpretación
· H hipótesis o propuesta · G geometría editorial no calibrada. Las cifras citadas proceden de los
resúmenes de PubMed verificados (refs31.py)."""
from layout31 import *          # noqa: F401,F403
from layout31 import (new_page, card, card_row, card_height, note, hbars, forest, make_sheet, sw,
                      text, rect_top, line_top, path, rrect_ops, PURPLE, OCHRE, BG, PILLFILL,
                      NOTEFILL, INFOFILL, WARN)

X2 = [(50.0, 584.0), (607.0, 1141.0)]
FULL = (50.0, 1141.0)


def subtitle(it, s, base=119.0):
    it.append(text(51.0, base, s, 'Roboto-Regular', 12.5, GRAY))


# ------------------------------------------------------------------ 26
def p26():
    n = 26
    it = new_page('Cribado de bipolaridad: qué detecta cada instrumento', 'EVALUACIÓN · I',
                  'E · propiedades psicométricas atribuidas a P19–P21 | I · uso en el atlas; sin trasladar puntuaciones a la geometría', n)
    subtitle(it, 'Los cribados orientan la entrevista; no diagnostican ni asignan un perfil de la matriz.')
    rows = [
        ('MDQ', 'Mood Disorder Questionnaire', 'P19',
         'Autoinforme breve de cribado del espectro bipolar (bipolar I, II y no especificado). Se validó en 198 pacientes de '
         'cinco clínicas ambulatorias de trastornos del ánimo, con una entrevista telefónica ciega a la puntuación (módulo '
         'bipolar del SCID-IV): con 7 o más ítems, sensibilidad 0,73 y especificidad 0,90.',
         'E · El estudio concluye que es útil en población psiquiátrica ambulatoria. I · Su rendimiento en otros ámbitos '
         'requiere evidencia propia.'),
        ('HCL-32', 'Hypomania Checklist de 32 ítems', 'P20',
         'Lista autoaplicada de síntomas hipomaníacos. En 266 pacientes bipolares frente a 160 con depresión mayor (muestras '
         'de Italia y Suecia) mostró dos factores, «activo/elevado» y «asunción de riesgos/irritable», y distinguió bipolar de '
         'depresión mayor con sensibilidad del 80 % y especificidad del 51 %.',
         'E · Sensible para síntomas hipomaníacos, pero con especificidad baja; no distingue bipolar I de bipolar II. '
         'I · Sirve para abrir la anamnesis de hipomanía, no para clasificar.'),
        ('BSDS', 'Bipolar Spectrum Diagnostic Scale', 'P21',
         'Autoinforme basado en un relato descriptivo de rasgos bipolares sutiles (creado por Ronald Pies). En 68 pacientes '
         'bipolares y 27 con depresión mayor unipolar: sensibilidad 0,76 (0,75 en bipolar I y 0,79 en bipolar II/NOS); '
         'identificó como no bipolares al 85 % de los unipolares. Con un umbral modificado, la especificidad pasó de 0,85 '
         'a 0,93 sin pérdida significativa de sensibilidad.',
         'E · Muestra pequeña y clínica; el umbral modificado procede del mismo estudio. I · Requiere replicación antes '
         'de usarlo como criterio.'),
    ]
    top = 136.0
    for name, sub, pill, bt, ct in rows:
        lb = wrap(bt, 'Roboto-Regular', 12, 470)
        lc = wrap(ct, 'Roboto-Regular', 12, 335)
        h = max(len(lb), len(lc)) * 17.4 + 62
        it.append(rect_top(50, top, 1141, top + h, 10, fill=WHITE, stroke=LINE, lw=1.0))
        it.append(rect_top(50, top, 55, top + h, 2, fill=INK))
        it.append(text(70, top + 34, name, 'Roboto-Bold', 20, NAVY))
        it.append(text(70, top + 54, sub, 'Roboto-Regular', 11, GRAY))
        pw = sw(pill, 'Roboto-Medium', 10) + 20
        it.append(rect_top(70, top + 68, 70 + pw, top + 89, 10, fill=PILLFILL))
        it.append(text(80, top + 82.5, pill, 'Roboto-Medium', 10, TEAL))
        it.append(text(300, top + 28, 'EVIDENCIA ATRIBUIDA', 'Roboto-Bold', 10, TEAL))
        for k, ln in enumerate(lb):
            it.append(text(300, top + 50 + k * 17.4, ln, 'Roboto-Regular', 12, GRAY))
        it.append(text(790, top + 28, 'LÍMITE Y USO', 'Roboto-Bold', 10, TEAL))
        for k, ln in enumerate(lc):
            it.append(text(790, top + 50 + k * 17.4, ln, 'Roboto-Regular', 12, GRAY))
        top += h + 16
    note(it, 50, top + 4, 1141, 'I · Un cribado positivo no es un diagnóstico',
         ['Un cribado positivo justifica evaluar los marcadores de bipolaridad (p. 30) y la historia de hipomanía (p. 19); '
          'un cribado negativo no excluye, porque las sensibilidades son inferiores a 1. Los umbrales proceden de muestras '
          'clínicas concretas.'], where='p26')
    return it


# ------------------------------------------------------------------ 27
def p27():
    n = 27
    it = new_page('Escalas de gravedad y de temperamento', 'EVALUACIÓN · II',
                  'E · propiedades psicométricas atribuidas a P22–P28 | I · límites de uso; las puntuaciones no entran en la geometría', n)
    subtitle(it, 'Miden intensidad o rasgo, no polaridad ni temporalidad: esas se establecen en la entrevista.')
    cards = [
        dict(title='YMRS · escala de manía', pill='P22', body=[
            'Escala de 11 ítems administrada por el clínico (el artículo la presenta como «Mania Rating Scale»). Fiabilidad '
            'interevaluador de 0,93 para la puntuación total; correlacionó con una valoración global independiente y con otras '
            'dos escalas de manía, y distinguió antes y después de dos semanas de tratamiento.',
            'I · Mide manía; no mide depresión ni mixticidad.']),
        dict(title='MADRS · gravedad depresiva', pill='P23', body=[
            'Diez ítems elegidos entre los 17 síntomas más frecuentes de la depresión primaria por su cambio con el tratamiento. '
            'Correlacionó con la escala de Hamilton y diferenció respondedores de no respondedores mejor que ella.',
            'I · Mide gravedad; no discrimina polaridad.']),
        dict(title='HAM-D · referencia histórica', pill='P25', body=[
            'Hamilton (1960): escala clínica de valoración de la depresión, de la que derivan las versiones posteriores (en P24 '
            'se comparan las de 17 y 24 ítems).',
            'PubMed no ofrece resumen del artículo original, por lo que aquí no se atribuyen datos psicométricos.']),
        dict(title='QIDS-SR16 · autoinforme', pill='P24', body=[
            'Versión de 16 ítems derivada del IDS de 30 ítems. En 596 adultos ambulatorios con depresión mayor crónica no '
            'psicótica: alfa de Cronbach 0,86; correlación de 0,96 con el IDS-SR30 y de 0,86 con la HAM-D de 24 ítems; igual '
            'de sensible al cambio que ambas.']),
        dict(title='PHQ-9 · gravedad depresiva', pill='P26', body=[
            'Nueve ítems (criterios DSM-IV) puntuados de 0 a 3, en 6.000 pacientes de atención primaria y de ginecología-obstetricia. '
            'Con una puntuación ≥10: sensibilidad y especificidad del 88 % para depresión mayor; los cortes 5, 10, 15 y 20 '
            'equivalen a depresión leve, moderada, moderadamente grave y grave.',
            'I · No evalúa polaridad: una puntuación alta no distingue depresión unipolar de bipolar.']),
        dict(title='TEMPS-A corto · temperamento', pill='P28', body=[
            '510 voluntarios (284 con trastornos del ánimo, 131 familiares de probandos bipolares y 95 controles): 39 de los 110 '
            'ítems originales se agrupan en cinco factores —ciclotímico, depresivo, irritable, hipertímico y ansioso—, con alfa '
            'de 0,91 a 0,67.',
            'I · Mide temperamento, no trastorno (p. 39).']),
    ]
    top = 130.0
    for k in range(3):
        top = card_row(it, cards[2 * k:2 * k + 2], top, X2, where='p27', bsize=12, lead=17.4) + 14
    note(it, 50, top + 2, 1141, 'I · Las escalas cuantifican',
         ['Polaridad, temporalidad y atribución se establecen en la entrevista. Ninguna puntuación se traslada a la '
          'geometría del atlas (G).'], where='p27')
    return it


# ------------------------------------------------------------------ 28
def p28():
    n = 28
    it = new_page('Riesgo suicida: evaluación independiente en toda fase', 'CAPA TRANSVERSAL',
                  'E · P27, P29–P32, P35 | I · el atlas no asigna riesgo a ningún perfil; no es una guía de intervención', n)
    subtitle(it, 'Capa transversal: aparece en todas las matrices y láminas como recordatorio, no como variable de un perfil.')
    top = 130.0
    top = card_row(it, [
        dict(title='Depresión · factores asociados a suicidio', pill='P29', body=[
            'Revisión sistemática con metaanálisis (19 estudios, 28 publicaciones). Asociados a suicidio: sexo masculino '
            '(OR 1,76), antecedentes familiares de trastorno psiquiátrico (1,41), intento previo (4,84), mayor gravedad de la '
            'depresión (2,20), desesperanza (2,20), ansiedad comórbida (1,59) y abuso de alcohol o drogas (2,17).',
            'Limitaciones señaladas: pocos estudios; no se examinó la interdependencia entre factores.']),
        dict(title='Bipolar · correlatos de intentos y de muertes', pill='P30', body=[
            'Metaanálisis del grupo de trabajo de la ISBD. Asociados a intentos: sexo femenino, inicio más temprano, polaridad '
            'depresiva del primer episodio y del actual o más reciente, ansiedad comórbida, cualquier trastorno por uso de '
            'sustancias, trastorno por uso de alcohol, cualquier consumo de sustancias ilícitas, trastorno de personalidad del grupo '
            'B/límite y antecedente familiar de suicidio. Asociados a muertes: sexo masculino y antecedente familiar de suicidio.',
            'Heterogeneidad considerable; no implica causalidad.']),
    ], top, X2, where='p28', bsize=12.5, lead=18) + 14
    top = card_row(it, [
        dict(title='Mortalidad y suicidio en trastornos mentales', pill='P31', body=[
            'Meta-revisión de 20 revisiones (más de 1,7 millones de pacientes y más de 250.000 muertes). Todos los trastornos '
            'aumentan la mortalidad por todas las causas. El trastorno límite de la personalidad, la anorexia nerviosa, la '
            'depresión y el trastorno bipolar presentan los mayores riesgos de suicidio. La calidad de las revisiones era, '
            'en general, baja.']),
        dict(title='Mixticidad e intentos de suicidio previos', pill='P35', body=[
            'En BRIDGE-II-MIX (2.811 episodios depresivos mayores), el estado mixto depresivo definido por criterios de '
            'investigación se asoció, entre otras variables, con intentos de suicidio a lo largo de la vida. La definición '
            'DSM-5 identificó el 7,5 % de los casos y la de investigación el 29,1 % (p. 29).']),
    ], top, X2, where='p28', bsize=12.5, lead=18) + 14
    top = card(it, 50, top, 1141, title='Instrumentos y límites de la predicción', pill='P27 · P32', body=[
        'C-SSRS (P27): cuantifica la ideación y la conducta suicidas. En tres estudios multicéntricos (124 adolescentes con '
        'intento, 312 adolescentes deprimidos y 237 adultos en urgencias psiquiátricas) mostró buena validez convergente, y la '
        'ideación más grave (intención o plan) elevó las probabilidades de intento durante el estudio.',
        'Carter et al. (P32): en un metaanálisis de valores predictivos positivos de escalas de riesgo, el VPP agrupado fue del '
        '5,5 % para suicidio y del 26,3 % para autolesión; los autores concluyen que ninguna clasificación de «alto riesgo» '
        'fue clínicamente útil.'], where='p28', bsize=12.5, lead=18) + 14
    note(it, 50, top, 1141, 'I · Qué hace y qué no hace el atlas',
         ['No asigna riesgo a ningún perfil: se evalúa en todos (matrices pp. 4–6 y láminas pp. 10–18). Los factores de P29–P31 '
          'orientan la exploración; ninguna escala predice el suicidio individual (P32).'], where='p28')
    return it


# ------------------------------------------------------------------ 29
def p29():
    n = 29
    it = new_page('Mixticidad: cuatro definiciones, cuatro conjuntos de casos', 'ESPECTRO · MIXTICIDAD',
                  'F · DSM-5-TR (p. 22) | E · P35, P36 | H · Koukopoulos (P10, P33) | I · por qué el atlas no las convierte unas en otras', n)
    subtitle(it, 'La misma depresión con síntomas contrapolares entra o no en el constructo según la definición empleada.')
    left = (50.0, 692.0)
    top = 130.0
    specs = [
        dict(title='DSM-5-TR · especificador «con características mixtas»', pill='F', body=[
            'Síntomas contrapolares seleccionados; en la depresión, la irritabilidad, la distractibilidad y la agitación no bastan para '
            'el recuento (p. 22). En BRIDGE-II-MIX lo cumplió el 7,5 % de los episodios depresivos mayores (P35).']),
        dict(title='ICD-11 · episodio mixto', pill='F', body=[
            'Reconocido en bipolar I (p. 3). La comparación sistemática de ICD-11 y DSM-5 por categorías figura en P17.']),
        dict(title='Koukopoulos · depresión mixta', pill='H', body=[
            'Síndrome de larga duración con ánimo disfórico, labilidad emocional, agitación psíquica o motora, locuacidad, '
            'pensamientos apiñados o acelerados, rumiación e insomnio inicial o medio (P10). Validación limitada (P10). Los '
            'autores sostienen que los criterios DSM-5 llevarían a más errores diagnósticos (P33, editorial).']),
        dict(title='Criterios de investigación (RBDC)', pill='E · H', body=[
            'Criterios de investigación definidos a priori a partir de síntomas, curso de la enfermedad y antecedentes familiares: los '
            'cumplió el 29,1 % de los episodios depresivos mayores (cuatro veces más que con DSM-5) y se asociaron con más variables '
            'propias de la bipolaridad (P35). En un análisis posterior, el criterio DSM-5 de al menos tres síntomas se asoció con mayor '
            'gravedad aguda y deterioro, con independencia del diagnóstico unipolar o bipolar, y las definiciones menos restrictivas no '
            'mostraron esa asociación (P36).']),
    ]
    for s in specs:
        top = card(it, left[0], top, left[1], where='p29', bsize=11.5, lead=16.4, **s) + 12
    # gráfico de barras (P35)
    cx0, cx1 = 712.0, 1141.0
    it.append(rect_top(cx0, 130, cx1, 538, 10, fill=WHITE, stroke=LINE, lw=1.0))
    it.append(rect_top(cx0, 130, cx0 + 5, 538, 2, fill=BLUE))
    it.append(text(cx0 + 18, 157, 'Síntomas maníacos/hipomaníacos en episodios', 'Roboto-Bold', 13, NAVY))
    it.append(text(cx0 + 18, 174, 'depresivos mayores (BRIDGE-II-MIX, n = 2.811; P35)', 'Roboto-Bold', 13, NAVY))
    data = [('Irritabilidad', 32.6), ('Labilidad emocional', 29.8), ('Distractibilidad', 24.4),
            ('Agitación psicomotriz', 16.1), ('Impulsividad', 14.5), ('Agresividad', 14.2),
            ('Pensamiento acelerado', 11.8), ('Presión del habla', 11.4), ('Euforia', 4.6),
            ('Grandiosidad', 3.7), ('Hipersexualidad', 2.6)]
    rows = [(a, v, ('%.1f %%' % v).replace('.', ',')) for a, v in data]
    hbars(it, cx0 + 18, 214.0, 28.0, rows, 35.0, 6.0, 140.0, color=BLUE, lsize=11)
    it.append(text(cx0 + 18, 520, 'E · Porcentaje de pacientes con cada síntoma (P35).', 'Roboto-Regular', 10.5, GRAY))
    b1 = note(it, 50, top, 692, 'I · Qué se observa',
              ['Los síntomas más frecuentes (irritabilidad, labilidad, distractibilidad, agitación) son justamente los que no cuentan '
               'para el recuento DSM de la depresión (p. 22).'], kind='info', where='p29')
    note(it, 50, max(b1, 538.0) + 14, 1141, 'I · Cada definición identifica una población distinta',
         ['7,5 % frente a 29,1 % en la misma muestra. Por eso el atlas mantiene la fila 13 (DSM) separada del constructo amplio (H) '
          'y no convierte una definición en otra.'], where='p29')
    return it


# ------------------------------------------------------------------ 30
def p30():
    n = 30
    it = new_page('Marcadores de bipolaridad en el episodio depresivo', 'ESPECTRO · RECLASIFICACIÓN',
                  'E · P14, P18, P34, P37 | I · justifican seguimiento y reevaluación; ninguno diagnostica por sí solo', n)
    subtitle(it, 'Qué datos transversales, longitudinales y de respuesta a tratamiento se asocian con una evolución bipolar.')
    xs = [(50.0, 395.0), (417.0, 772.0), (794.0, 1141.0)]
    top = card_row(it, [
        dict(title='Transversal · BRIDGE', pill='P34', body=[
            '5.635 adultos con un episodio depresivo mayor en curso: 903 (16,0 %) cumplían criterios DSM-IV-TR de bipolar y 2.647 '
            '(47,0 %) cumplían los criterios del «especificador de bipolaridad».',
            'Con ambas definiciones se asociaron (OR > 2) el antecedente familiar de manía o hipomanía y los múltiples episodios '
            'previos. El especificador añadió estados maníacos o hipomaníacos durante el tratamiento antidepresivo, síntomas '
            'mixtos actuales y trastorno por uso de sustancias comórbido.',
            'I · La definición amplia no es un diagnóstico: señala a quién reevaluar.']),
        dict(title='Longitudinal · P14 y P18', pill='P14 · P18', body=[
            'Fiedorowicz (P14): 550 personas con depresión mayor, seguidas 17,5 años de media; el 19,6 % tuvo hipomanía o manía '
            '(12,2 % pasó a bipolar II y 7,5 % a bipolar I). Predijeron la progresión el número de síntomas hipomaníacos subumbral, '
            'la psicosis y la edad de inicio.',
            'Angst (P18): 406 pacientes con ingresos por trastorno del ánimo, seguidos en promedio unos 20 años desde el inicio: cambio diagnóstico a bipolar I '
            'en torno al 1 % anual y a bipolar II en torno al 0,5 %; cada episodio depresivo conlleva un riesgo de manía que se '
            'mantiene constante. Muestra hospitalaria: generalización limitada.']),
        dict(title='Respuesta a antidepresivos · AIM', pill='P37', body=[
            'En 1.329 pacientes con depresión mayor (BRIDGE-II-MIX), 404 tenían resistencia al tratamiento y 184, antecedente de '
            'irritabilidad y labilidad del ánimo inducidas por antidepresivos (AIM).',
            'AIM se asoció con antecedente familiar de bipolar, resistencia previa, rasgos atípicos y mixtos, comorbilidad '
            'psiquiátrica, intentos de suicidio a lo largo de la vida e inicio más temprano; entre los síntomas, con '
            'distractibilidad, impulsividad e hipersexualidad.',
            'H · Los autores lo interpretan como posible diátesis bipolar subyacente; estudio transversal.']),
    ], 130.0, xs, where='p30', bsize=12, lead=17.4) + 16
    top = card(it, 50, top, 1141, title='Qué preguntar (I · derivado de los marcadores de P34)', body=[
        '•  Antecedente familiar de manía o hipomanía.',
        '•  Número de episodios previos y su curso.',
        '•  Episodios de activación o euforia durante el tratamiento antidepresivo: fármaco, momento y duración.',
        '•  Síntomas contrapolares actuales y la definición con que se evalúan (p. 29).',
        '•  Trastorno por uso de sustancias y su cronología (p. 37).'], where='p30', bsize=12, lead=19, gap=2) + 16
    note(it, 50, top, 1141, 'I · Reevaluar, no reclasificar a ciegas',
         ['Estos marcadores justifican seguimiento y reevaluación diagnóstica (pp. 19 y 34); ninguno diagnostica bipolaridad por sí '
          'solo. Las cifras proceden de cohortes con definiciones y ámbitos distintos y no son probabilidades individuales (G).'],
         where='p30')
    return it


# ------------------------------------------------------------------ 31
def p31():
    n = 31
    it = new_page('Antidepresivos, activación y reclasificación', 'MODULADORES · TRATAMIENTO',
                  'E · P37, P38, P39 | F · regla de atribución N4 (p. 24) | I · no prescriptivo: riesgos descritos, no pautas', n)
    subtitle(it, 'Qué describen los metaanálisis y los registros sobre manía asociada a antidepresivos, y qué regla ordena la atribución.')
    bodyA = [
        '73 informes (109 ensayos; 114.521 adultos). La manía asociada a antidepresivos fue más frecuente en bipolar que en depresión '
        'mayor, pero aumentó proporcionalmente más en depresión mayor. Los tricíclicos fueron más arriesgados que los ISRS; para otros '
        'tipos de antidepresivos los datos no fueron concluyentes. Los estabilizadores tuvieron efectos menores, probablemente '
        'confundidos por su uso preferente en pacientes propensos a la manía.']
    bodyB = [
        '3.240 pacientes bipolares que iniciaron un antidepresivo; diseño intraindividual. La monoterapia antidepresiva se asoció '
        'con más riesgo de manía; con estabilizador concurrente no hubo cambio agudo en los primeros 3 meses y el riesgo fue menor '
        'a los 3–9 meses. Los autores destacan evitar la monoterapia antidepresiva en bipolar.']
    hA = card_height('Metaanálisis · riesgo global de manía', bodyA, 50, 584, pill='P39', bsize=11.5, lead=16.4)
    hB = card_height('Registros suecos · antidepresivo y estabilizador', bodyB, 607, 1141, pill='P38', bsize=11.5, lead=16.4)
    top0 = 130.0
    t1 = top0 + max(hA, hB) + 150
    card(it, 50, top0, 584, title='Metaanálisis · riesgo global de manía', pill='P39', body=bodyA, t1=t1, where='p31', bsize=11.5, lead=16.4)
    card(it, 607, top0, 1141, title='Registros suecos · antidepresivo y estabilizador', pill='P38', body=bodyB, t1=t1, where='p31', bsize=11.5, lead=16.4)
    yb = top0 + max(hA, hB) + 18
    it.append(text(68, yb, 'Riesgo global de manía (P39)', 'Roboto-Bold', 11, NAVY))
    hbars(it, 68, yb + 30, 30.0, [('Con antidepresivo', 12.5, '12,5 %'), ('Sin antidepresivo', 7.5, '7,5 %')],
          15.0, 16.0, 130.0, color=TEAL)
    it.append(text(625, yb, 'Cociente de riesgo de manía (HR, IC 95 %; escala logarítmica; P38)', 'Roboto-Bold', 11, NAVY))
    forest(it, 800.0, 1080.0, yb + 32, 28.0,
           [('Monoterapia', 2.83, 1.12, 7.19), ('Con estabilizador, 0–3 m', 0.79, 0.54, 1.15),
            ('Con estabilizador, 3–9 m', 0.63, 0.42, 0.93)], 0.25, 8.0, [0.25, 0.5, 1, 2, 4, 8])
    top = t1 + 16
    top = card_row(it, [
        dict(title='Atribución · regla del atlas (F · N4)', pill='F', body=[
            'Un síndrome hipomaníaco o maníaco completo que persiste más allá del efecto del antidepresivo tiene relevancia '
            'diagnóstica; uno o dos signos de activación no bastan (N4; p. 24). La lámina 13 (p. 35) ilustra ambas trayectorias.']),
        dict(title='AIM y diátesis bipolar (P37)', pill='P37', body=[
            'La irritabilidad y la labilidad inducidas por antidepresivos se asocian con rasgos mixtos y con una posible diátesis '
            'bipolar (p. 30). El atlas las recoge como pregunta de entrevista: exposición, respuesta, efectos adversos y posible '
            'activación (p. 20).']),
    ], top, X2, where='p31', bsize=12, lead=17.4) + 14
    note(it, 50, top, 1141, 'I · No es una pauta terapéutica',
         ['Se exponen riesgos descritos en cohortes y metaanálisis y la regla de atribución (p. 20). Los porcentajes y los cocientes '
          'de riesgo no son probabilidades individuales.'], where='p31')
    return it


# ------------------------------------------------------------------ 32
def p32():
    n = 32
    it = new_page('Periparto: ventana, riesgo y vigilancia', 'MODULADORES · PERIPARTO',
                  'F · ventana según el sistema (N1, N3) | E · P40, P41 | I · qué registra el atlas; no es una pauta de manejo', n)
    subtitle(it, 'El periodo perinatal concentra riesgo de episodios graves; la lámina 11 (p. 33) lo ilustra sin calibrarlo.')
    top = card_row(it, [
        dict(title='Ventana y definiciones (F)', pill='N1 · N3', body=[
            'DSM-5-TR: especificador «con inicio en el periparto» para episodios del estado de ánimo. ICD-11: categoría específica '
            'para los trastornos asociados al embarazo, el parto o el puerperio. Las ventanas exactas dependen del sistema y se toman '
            'del texto oficial.',
            'La vigilancia clínica no se limita a una casilla temporal (p. 25).']),
        dict(title='Riesgo perinatal (E)', pill='P40', body=[
            'Revisión en Lancet: el periodo perinatal se asocia con mayor riesgo de trastornos mentales graves; el suicidio es una de '
            'las principales causas de muerte materna. Hay pocos estudios que guíen el manejo de las mujeres con trastornos mentales '
            'graves en el embarazo y el posparto, y se subraya el análisis individual de riesgo y beneficio. Cubre bipolar, psicosis '
            'afectiva y esquizofrenia, con enfermedad crónica o con inicio de psicosis posparto.']),
    ], 130.0, X2, where='p32', bsize=12.5, lead=18) + 14
    top = card_row(it, [
        dict(title='Recaída posparto (E)', pill='P41', body=[
            'Metaanálisis de 37 artículos (5.700 partos en 4.023 pacientes): riesgo global de recaída posparto del 35 % (IC 95 % 29–41). '
            'En bipolar, episodios graves posparto: 17 % (13–21); con antecedente de psicosis posparto: 29 % (20–41).',
            'En mujeres con bipolar, la recaída fue del 66 % (57–75) si no tomaban medicación durante el embarazo y del 23 % (14–37) '
            'si recibían profilaxis; los autores concluyen que continuarla parece muy protector.']),
        dict(title='Qué registra el atlas (I)', pill='I', body=[
            'Relación temporal con el embarazo y el posparto; historia afectiva previa; sueño; síntomas psicóticos y su relación con '
            'el episodio (pp. 18 y 25).',
            'La lámina 11 (p. 33) muestra, a modo de ejemplo, una elevación con psicosis tras el parto y una depresión posterior sobre '
            'un curso bipolar previo.']),
    ], top, X2, where='p32', bsize=12.5, lead=18) + 14
    note(it, 50, top, 1141, 'I · Límites de las cifras',
         ['Los porcentajes agrupan cohortes heterogéneas y no son probabilidades individuales; no se trasladan a la geometría de la '
          'lámina (G). Las decisiones terapéuticas perinatales requieren evaluación individual (P40).'], where='p32')
    return it


# ------------------------------------------------------------------ láminas 33–35
def p33(tpl):
    curves = {
        'dep': [0.28, 0.26, 0.24, 0.23, 0.25, 0.27, 0.30, 0.26, 0.27, 0.45, 0.74, 0.70],
        'act': [0.33, 0.32, 0.34, 0.33, 0.34, 0.36, 0.40, 0.86, 0.90, 0.52, 0.36, 0.34],
        'fun': [0.84, 0.85, 0.83, 0.82, 0.83, 0.80, 0.74, 0.40, 0.34, 0.56, 0.45, 0.50],
        'res': [0.26, 0.26, 0.27, 0.27, 0.28, 0.29, 0.31, 0.45, 0.50, 0.46, 0.48, 0.47]}
    rows = [(140.0, 134.0, [(0.0, 6.0, 'Embarazo', 'neu', False), (6.0, 11.4, 'Posparto', 'neu', False)]),
            (159.0, 153.0, [(6.5, 8.5, 'Manía con psicosis', 'elev'), (9.5, 11.4, 'Depresión posterior', 'dep')])]
    return make_sheet(tpl, pageno=33, title='Curso 11 · Periparto',
                      tag='G · viñeta ilustrativa | E · contexto perinatal P40–P41 | F · ventana: p. 32',
                      subtitle='Ejemplo: elevación con psicosis tras el parto y depresión posterior sobre un curso bipolar; la ventana '
                               'formal depende del sistema (p. 32).',
                      curves=curves, rows=rows, thr=(0.60, 0.60, 'umbral de manía'), markers=[(6.0, 'parto')],
                      psych=[(6.9, 8.6)], extra_foot='La línea vertical discontinua marca el parto.')


def p34(tpl):
    curves = {
        'dep': [0.22, 0.55, 0.84, 0.46, 0.25, 0.52, 0.80, 0.40, 0.24, 0.28, 0.30, 0.66],
        'act': [0.32, 0.30, 0.29, 0.31, 0.33, 0.30, 0.28, 0.31, 0.34, 0.62, 0.36, 0.30],
        'fun': [0.82, 0.66, 0.50, 0.70, 0.80, 0.66, 0.52, 0.73, 0.80, 0.74, 0.76, 0.58],
        'res': [0.26, 0.31, 0.38, 0.34, 0.30, 0.35, 0.41, 0.36, 0.31, 0.32, 0.34, 0.40]}
    rows = [(140.0, 134.0, [(0.0, 8.5, 'Diagnóstico vigente: depresión recurrente', 'neu', False),
                            (9.5, 11.4, 'Reevaluación diagnóstica', 'neu', False)]),
            (159.0, 153.0, [(1.5, 2.5, 'Episodio', 'dep'), (5.5, 6.5, 'Episodio', 'dep'),
                            (8.5, 9.5, 'Hipomanía observada', 'elev'), (10.5, 11.4, 'Episodio', 'dep')])]
    return make_sheet(tpl, pageno=34, title='Curso 12 · Reclasificación tras hipomanía observada',
                      tag='G · viñeta ilustrativa | E · P14, P18 | I · relación con pp. 19 y 30',
                      subtitle='Tras una hipomanía observada puede reclasificarse un curso depresivo recurrente, si cumple criterios y no '
                               'se atribuye a otra causa (p. 19).',
                      curves=curves, rows=rows, thr=(0.60, 0.55, 'umbral de hipomanía'), markers=[(9.5, 'reevaluar')])


def p35(tpl):
    curves = {
        'dep': [0.22, 0.55, 0.82, 0.78, 0.60, 0.42, 0.30, 0.26, 0.24, 0.24, 0.22, 0.22],
        'act': [0.32, 0.30, 0.31, 0.33, 0.40, 0.46, 0.42, 0.34, 0.31, 0.30, 0.31, 0.30],
        'fun': [0.82, 0.64, 0.48, 0.50, 0.62, 0.74, 0.80, 0.80, 0.82, 0.82, 0.83, 0.83],
        'res': [0.26, 0.33, 0.42, 0.40, 0.35, 0.31, 0.28, 0.27, 0.26, 0.26, 0.25, 0.25]}
    rows = [(159.0, 153.0, [(2.5, 7.0, 'Exposición al antidepresivo', 'neu'),
                            (7.0, 11.4, 'Retirada y seguimiento', 'neu')])]
    alt = [('act', 5, [0.46, 0.62, 0.70, 0.66, 0.62, 0.58, 0.55], RED)]
    notes_in = [(xi(7.2), 347.0, 'activación subumbral que cede: no basta (N4)', RED),
                (xi(7.4), 313.0, 'síndrome completo que persiste: relevancia diagnóstica (N4)', RED)]
    return make_sheet(tpl, pageno=35, title='Curso 13 · Activación asociada al tratamiento',
                      tag='G · viñeta ilustrativa | F · regla de atribución N4 | E · P38, P39',
                      subtitle='Dos trayectorias posibles tras la exposición a un antidepresivo: activación subumbral que cede, o síndrome '
                               'completo que persiste más allá del efecto fisiológico (pp. 24 y 31).',
                      curves=curves, rows=rows, thr=(0.60, 0.55, 'umbral de hipomanía'), alt=alt, notes_in=notes_in,
                      extra_foot='Línea de trazos gruesos: trayectoria alternativa.')


# ------------------------------------------------------------------ 36
def p36():
    n = 36
    it = new_page('Causas médicas y farmacológicas de síndromes afectivos', 'DIFERENCIAL · MÉDICO',
                  'E · P42, P44 | I · preguntas abiertas de entrevista | H · propuestas de los autores marcadas', n)
    subtitle(it, 'Un síndrome maníaco o depresivo puede ser secundario; descartarlo forma parte de leer cualquier perfil del atlas.')
    top = card_row(it, [
        dict(title='Manía secundaria · clásico', pill='P42', body=[
            'Krauthammer y Klerman (1978): la manía puede presentarse en personas sin historia afectiva asociada a disfunción orgánica, '
            'médica y farmacológica. Se describe secundaria a fármacos, infecciones, neoplasias, epilepsia y alteraciones metabólicas.',
            'Proponen que la manía, como la hipertensión, es un síndrome de causas múltiples y recomiendan buscar causas secundarias '
            'cuando las condiciones lo justifiquen. El registro indexa, entre otros, corticoides, isoniazida, levodopa y procarbazina.']),
        dict(title='Infección por VIH', pill='P44', body=[
            'Las personas con VIH tienen mayor riesgo de enfermedad psiquiátrica: la depresión mayor y subsindrómica, la ansiedad y el '
            'abuso de sustancias son más prevalentes que en la población general.',
            'La manía y la psicosis secundarias pueden ser el primer síntoma clínico de la demencia asociada al VIH; los autores '
            'proponen usarlas como indicador para iniciar tratamiento antirretroviral con independencia del recuento de CD4 (H). '
            'Revisión narrativa de la literatura de 1980–2008.']),
    ], 130.0, X2, where='p36', bsize=12.5, lead=18) + 16
    top = card(it, 50, top, 1141, title='Preguntas que el atlas deja abiertas (I)', body=[
        '•  ¿Hubo cambios recientes de medicación o exposición a fármacos con efecto sobre el ánimo (pp. 24 y 31)?',
        '•  ¿Existen antecedentes neurológicos, infecciosos o metabólicos, o síntomas cognitivos acompañantes?',
        '•  ¿Cómo encaja la edad y la forma de inicio con la historia afectiva previa?',
        '•  ¿El síndrome persiste tras corregir la causa sospechada?'], where='p36', bsize=12, lead=19, gap=2) + 16
    top = note(it, 50, top, 1141, 'I · Secundario no significa ajeno',
         ['Un síndrome secundario no excluye una vulnerabilidad previa, pero tampoco la confirma: que la manía o la depresión '
          'aparezcan después de un fármaco, una infección o una lesión orienta la atribución, aunque la secuencia por sí sola no '
          'demuestra causalidad (p. 24). Por eso el atlas pide reconstruir la cronología con cuidado y volver a evaluar el cuadro '
          'cuando la causa sospechada se ha corregido.',
          'En la práctica, la infección por VIH y el consumo de sustancias comparten a menudo el mismo escenario clínico, el del '
          'chemsex (p. 37), y en esa encrucijada conviene explorar a la vez la causa médica, la tóxica y la afectiva primaria.'],
         where='p36') + 14
    note(it, 50, top, 1141, 'I · Por qué el diagnóstico médico va primero',
         ['Krauthammer y Klerman propusieron entender la manía, como la hipertensión, como un síndrome de causas múltiples (P42). '
          'Leída así, la pregunta por la causa secundaria no es un trámite previo al diagnóstico psiquiátrico, sino parte de él: '
          'cambia el pronóstico, el tratamiento y la manera de explicar a la persona lo que le ocurre.'], kind='info', where='p36')
    return it


# ------------------------------------------------------------------ 37
def p37():
    n = 37
    it = new_page('Sustancias emergentes, chemsex y episodios afectivos', 'MODULADORES · SUSTANCIAS',
                  'E · P45–P51 | F · atribución por cronología (p. 24) | I · no prescriptivo: fenómenos descritos para ordenar la entrevista', n)
    subtitle(it, 'La cronología de exposición, intoxicación y abstinencia se reconstruye por sustancia; no existe una regla común de duración.')
    top = card(it, 50, 130, 1141, title='Contexto · chemsex y salud mental', pill='P48 · P49', accent=BLUE, fill=INFOFILL, body=[
        'Chemsex: uso de drogas antes o durante encuentros sexuales planificados; se asocian metanfetamina, GHB/GBL, mefedrona, '
        'cocaína y ketamina (revisión de 38 estudios publicados entre 2000 y 2018; los hombres con VIH participaron con más frecuencia '
        'que los VIH negativos; P48). En una revisión sistemática de 12 estudios, quienes practicaban uso sexualizado de drogas '
        'presentaron con más frecuencia depresión, ansiedad o dependencia, aunque no en todos los estudios; los síntomas fueron más '
        'graves entre quienes se inyectaban (slamsex) (P49).'], where='p37', bsize=11.5, lead=16.4) + 14
    rows = [
        ('Metanfetamina', 'P45',
         '309 consumidores regulares (Sídney): 13 % con cribado positivo de psicosis y 23 % con algún síntoma clínicamente '
         'significativo (suspicacia, ideas inusuales o alucinaciones) en el último año; los dependientes tuvieron tres veces más '
         'probabilidad de haber presentado síntomas psicóticos. Prevalencia 11 veces la de la población general australiana.',
         'Último año; estudio transversal'),
        ('GHB / GBL · retirada', 'P46 · P47',
         'Serie de 8 pacientes tras uso crónico: todos psicóticos y con agitación intensa, con delirium y alucinaciones auditivas y '
         'visuales; dependencia tras tomas cada 1–3 horas. La revisión describe inestabilidad autonómica relativamente leve y breve '
         'con síntomas psicóticos prolongados.',
         'Inicio 1–6 h tras la última dosis; duración 5–15 días'),
        ('Cannabis', 'P50',
         'Revisión de 6 estudios prospectivos (2.391 personas con síntomas maníacos; seguimiento medio de 3,9 años): asociación con '
         'la exacerbación de síntomas maníacos en bipolar; en un metaanálisis de dos estudios, OR 2,97 (1,80–4,90) para el inicio de '
         'síntomas maníacos. Conclusiones preliminares.',
         'Seguimiento medio 3,9 años'),
        ('Mefedrona y catinonas', 'P51',
         'Efectos estimulantes y empatógenos similares a anfetamina, metanfetamina, cocaína y MDMA; por su acción simpaticomimética '
         'puede asociarse con efectos adversos físicos y psicopatológicos. Evidencia limitada: parte de la información procede de '
         'informes de usuarios.',
         'No establecida en la revisión'),
    ]
    it.append(text(70, top + 6, 'SUSTANCIA', 'Roboto-Bold', 10, TEAL))
    it.append(text(250, top + 6, 'FENÓMENOS DESCRITOS (E)', 'Roboto-Bold', 10, TEAL))
    it.append(text(905, top + 6, 'CRONOLOGÍA', 'Roboto-Bold', 10, TEAL))
    top += 14
    for name, pill, bt, chrono in rows:
        lb = wrap(bt, 'Roboto-Regular', 11.5, 620)
        lc = wrap(chrono, 'Roboto-Regular', 11.5, 215)
        h = max(len(lb), len(lc)) * 16.4 + 24
        it.append(rect_top(50, top, 1141, top + h, 8, fill=WHITE, stroke=LINE, lw=1.0))
        it.append(text(70, top + 24, name, 'Roboto-Bold', 13, NAVY))
        pw = sw(pill, 'Roboto-Medium', 10) + 20
        it.append(rect_top(70, top + 34, 70 + pw, top + 55, 10, fill=PILLFILL))
        it.append(text(80, top + 48.5, pill, 'Roboto-Medium', 10, TEAL))
        for k, ln in enumerate(lb):
            it.append(text(250, top + 22 + k * 16.4, ln, 'Roboto-Regular', 11.5, GRAY))
        for k, ln in enumerate(lc):
            it.append(text(905, top + 22 + k * 16.4, ln, 'Roboto-Regular', 11.5, GRAY))
        top += h + 8
    note(it, 50, top + 4, 1141, 'I · Atribución y límites',
         ['El consumo no excluye un trastorno afectivo primario ni lo confirma; no hay un plazo universal de un mes (p. 24). Esta página '
          'no es una pauta de manejo: recoge fenómenos descritos y su cronología.'], where='p37')
    return it


# ------------------------------------------------------------------ 38
def p38():
    n = 38
    it = new_page('Diagnóstico diferencial y comorbilidad: preguntas clave', 'DIFERENCIAL',
                  'E · P29, P30, P35, P37, P42–P44 | I · preguntas de entrevista | F · esquizoafectivo: p. 25', n)
    subtitle(it, 'Un diferencial no excluye al otro: la comorbilidad es frecuente y la atribución se hace por cronología e historia.')
    cards = [
        dict(title='Trastorno límite de la personalidad', pill='P43 · P35 · P30', body=[
            'Coexiste con el trastorno bipolar, pero la relación no es consistente ni específica; hay solapamientos y diferencias '
            'importantes en fenomenología, respuesta a fármacos y curso; los estudios familiares sugieren distinciones claras y es '
            'inusual que evolucione a bipolar (P43). La comorbilidad con límite se asoció con el estado mixto depresivo de '
            'investigación (P35) y, en bipolar, con intentos de suicidio (P30).',
            'I · Registrar duración, desencadenantes y curso longitudinal de los cambios de ánimo.']),
        dict(title='TDAH', pill='P35 · P37', body=[
            'La distractibilidad y la impulsividad figuran entre los síntomas contrapolares frecuentes en los episodios depresivos '
            '(24,4 % y 14,5 %), y el TDAH comórbido se asoció con el estado mixto de investigación (P35); distractibilidad e '
            'impulsividad se asociaron con la irritabilidad inducida por antidepresivos (P37).',
            'I · Preguntar por inicio en la infancia y persistencia entre episodios.']),
        dict(title='Trastornos por uso de sustancias', pill='P30 · P45–P51', body=[
            'La comorbilidad con sustancias se asoció con intentos de suicidio en bipolar (P30). La cronología de la exposición orienta '
            'la atribución (pp. 24 y 37).']),
        dict(title='Causas médicas y farmacológicas', pill='P42 · P44', body=[
            'Manía secundaria a drogas, infecciones, neoplasias, epilepsia y alteraciones metabólicas (P42); infección por VIH (P44). '
            'Véase p. 36.']),
        dict(title='Esquizoafectivo y psicosis primaria', pill='F', body=[
            'Registrar si la psicosis se limita a episodios afectivos o aparece también fuera de ellos; el diagnóstico esquizoafectivo '
            'usa relaciones temporales distintas en DSM e ICD (p. 25).']),
        dict(title='Ansiedad comórbida y malestar ansioso', pill='P29 · P30', body=[
            'La ansiedad comórbida se asoció con suicidio en depresión (OR 1,59; P29) y con intentos en bipolar (P30). La fila 09 recoge '
            'el malestar ansioso como especificador (p. 22).']),
    ]
    top = 128.0
    for k in range(3):
        top = card_row(it, cards[2 * k:2 * k + 2], top, X2, where='p38', bsize=12.5, lead=18) + 14
    top = note(it, 50, top + 2, 1141, 'I · Comorbilidad frente a diferencial',
         ['Varias de estas condiciones son a la vez diagnóstico alternativo y comorbilidad. El trastorno límite, el TDAH o el uso de '
          'sustancias pueden imitar la inestabilidad afectiva, pero también coexistir con un trastorno bipolar y modificar su curso, '
          'su riesgo suicida y su respuesta al tratamiento (P30, P35, P37, P43). Por eso el atlas las recoge como preguntas abiertas '
          'y no como exclusiones automáticas: descartar una no obliga a aceptar la otra.'], where='p38') + 14
    note(it, 50, top, 1141, 'I · Cómo ordenar la entrevista',
         ['Ayuda separar tres planos: la duración y la forma de los cambios de ánimo (episódicos o reactivos y breves), su relación '
          'con desencadenantes y sustancias, y la historia longitudinal desde la infancia. La lectura dimensional de las pp. 49–55 '
          'explica por qué la comorbilidad es la regla y no la excepción (P80).'], kind='info', where='p38')
    return it


# ------------------------------------------------------------------ 39
def p39():
    n = 39
    it = new_page('Temperamentos afectivos', 'ESPECTRO · TEMPERAMENTO',
                  'E · P28 (TEMPS-A) | H · Akiskal (P06) | I · rasgos de base, no diagnósticos ni ejes de la matriz', n)
    subtitle(it, 'Cinco factores de temperamento en el TEMPS-A corto (510 voluntarios); consistencia interna entre paréntesis.')
    spec = [
        ('Ciclotímico', 'alfa 0,91',
         ['Correlación positiva con búsqueda de novedad y, como el resto salvo el hipertímico, con evitación del daño (P28).',
          'Correlacionó, junto con el depresivo, con el factor «depresión» de la manía (P04). Las depresiones sobre oscilaciones '
          'ciclotímicas se describen como una variante más grave de bipolar II (P06).']),
        ('Depresivo', 'alfa 0,81',
         ['Correlación positiva con evitación del daño y negativa con búsqueda de novedad (P28).',
          'Correlacionó con el factor «depresión» de la manía (P04).']),
        ('Irritable', 'alfa 0,77',
         ['Correlación positiva con evitación del daño y negativa con búsqueda de novedad (P28).']),
        ('Hipertímico', 'alfa 0,76',
         ['Rasgos hipomaníacos de por vida sin episodios hipomaníacos discretos (P06).',
          'Correlación positiva con búsqueda de novedad, dependencia de la recompensa, persistencia y autodirección; no se '
          'correlacionó con evitación del daño (P28).']),
        ('Ansioso', 'alfa 0,67',
         ['Escala añadida después de las otras cuatro; evaluada solo en 345 sujetos (P28).',
          'Correlación positiva con evitación del daño y con autotrascendencia.']),
    ]
    top = 128.0
    xs = [(48.0 + k * 222.0, 48.0 + k * 222.0 + 207.0) for k in range(5)]
    specs = [dict(title=nm, pill=None, body=['Consistencia interna: %s' % al] + bd) for nm, al, bd in spec]
    top = card_row(it, specs, top, xs, where='p39', bsize=12.5, lead=18, pad=14, tsize=16) + 18
    top = note(it, 50, top, 1141, 'H · Naturaleza dual del temperamento (P28)',
               ['Los autores muestran, para cada temperamento, atributos positivos con sentido evolutivo y rasgos que hacen vulnerable a los '
                'cambios del ánimo; proponen esa dualidad como endofenotipo conductual en un modelo oligogénico de la herencia bipolar. '
                'Es una hipótesis.'], kind='info', where='p39') + 14
    note(it, 50, top, 1141, 'I · Cómo se usa en el atlas',
         ['El temperamento se anota como pregunta abierta de entrevista, junto con la vivencia (p. 25); no es un diagnóstico, no '
          'es un eje de la matriz y no se confunde con la ciclotimia DSM (fila 15, p. 13).'], where='p39')
    return it


# ------------------------------------------------------------------ 40
def p40():
    n = 40
    it = new_page('Línea histórica del concepto', 'ESPECTRO · HISTORIA',
                  'E · cada hito con su fuente (P06–P11, P17, P33; N2) | H · selección: no reconstruye toda la historia del concepto', n)
    subtitle(it, 'Del concepto amplio de Kraepelin a la separación bipolar/unipolar y al regreso del espectro.')
    nodes = [
        ('Origen · Kraepelin', 'Concepto amplio de enfermedad maníaco-depresiva, con episodios de ambos polos y estados mixtos.', 'P07 · P10'),
        ('1978–1980', 'Los RDC (1978) y el DSM-III (1980) operacionalizan los estados mixtos maníacos y dejan fuera las depresiones '
                      'mixtas. El DSM-III divide el concepto en bipolar y unipolar, siguiendo a Leonhard.', 'P07 · P10'),
        ('1992', 'Koukopoulos describe el síndrome depresivo mixto.', 'P10'),
        ('DSM-IV / ICD-10', 'La manía mixta (disfórica) se incluye formalmente. La hipomanía exige ≥4 días, aunque su duración '
                            'habitual sea de 1–3 días.', 'P06'),
        ('2000–2005', 'Espectro bipolar de Akiskal y de Angst: umbrales de hipomanía más amplios y síntomas subumbrales. Akiskal '
                      'propone representar el curso con gráficos de colores (life charting).', 'P06 · P08'),
        ('2008', 'Revisión de la ciclación rápida: especificador de curso (≥4 episodios al año) sin otras características clínicas '
                 'que la definan.', 'P11'),
        ('2013', 'Se publica el DSM-5, con el especificador «con características mixtas»; su definición recibe críticas desde el '
                 'espectro.', 'P17 · P33'),
        ('2019–2022', 'La Asamblea Mundial de la Salud aprueba la ICD-11 (2019); la APA publica el DSM-5-TR en 2022.', 'P17 · N2'),
    ]
    ymid = 432.0
    it.append(line_top(60, ymid, 1131, ymid, stroke=INK, lw=2.5))
    cw = 220.0
    for k, (head, body, pill) in enumerate(nodes):
        cx = 170.0 + k * 120.0
        x0 = min(max(cx - cw / 2, 50.0), 1141.0 - cw)
        h = card_height(head, [body], x0, x0 + cw, pad=14, pill=None, tsize=15, bsize=11.5, lead=16.0)
        h += 22
        if k % 2 == 0:       # por encima de la línea
            t0 = 400.0 - h
            it.append(line_top(cx, 400.0, cx, ymid - 9, stroke=INK, lw=1.2))
        else:
            t0 = 464.0
            it.append(line_top(cx, ymid + 9, cx, 464.0, stroke=INK, lw=1.2))
        card(it, x0, t0, x0 + cw, title=head, body=[body], accent=TEAL if k % 2 == 0 else BLUE, tsize=15, bsize=11.5,
             lead=16.0, pad=14, r=8, where='p40-%d' % k, t1=t0 + h - 22 + 22)
        pw = sw(pill, 'Roboto-Medium', 10) + 20
        it.append(rect_top(x0 + 14, t0 + h - 22, x0 + 14 + pw, t0 + h - 3, 9, fill=PILLFILL))
        it.append(text(x0 + 24, t0 + h - 9, pill, 'Roboto-Medium', 10, TEAL))
        it.append(rect_top(cx - 9, ymid - 9, cx + 9, ymid + 9, 9, fill=NAVY, stroke=WHITE, lw=2.0))
    note(it, 50, 664, 1141, 'I · Una tensión que el atlas hereda',
         ['La historia del concepto oscila entre la amplitud de Kraepelin y la precisión de las categorías operativas. Desde 2009 '
          'ese vaivén se ha enriquecido con propuestas dimensionales y longitudinales: la estadificación (P82), RDoC (P81), HiTOP '
          '(P79) y el modelo ACE (P75), que retoma la intuición de Weygandt sobre los estados mixtos (P74). El atlas no zanja la '
          'discusión: la trata como pregunta abierta (p. 23) y la desarrolla en las pp. 49–55.'],
         where='p40', t1=790)
    return it


# ------------------------------------------------------------------ 41
def p41():
    n = 41
    it = new_page('Glosario bilingüe y equivalencias de términos', 'REFERENCIA',
                  'F · términos de los sistemas | I · traducciones descriptivas del atlas, no ediciones oficiales (p. 22)', n)
    subtitle(it, 'Para leer la bibliografía en inglés y las fichas oficiales sin perder el matiz.')
    rows = [
        ('mixed features', 'características mixtas', 'Especificador DSM; p. 22 (fila 13).'),
        ('mixed state / mixed episode', 'estado mixto / episodio mixto', 'ICD-11: episodio mixto en bipolar I (p. 3).'),
        ('anxious distress', 'malestar ansioso (término inglés conservado)', 'Sin traducción oficial certificada (p. 22; fila 09).'),
        ('melancholic features', 'características melancólicas', 'Especificador DSM (fila 10).'),
        ('atypical features', 'características atípicas', 'Especificador DSM (fila 11).'),
        ('with psychotic features', 'con características psicóticas', 'Fila 12; pp. 18 y 25.'),
        ('seasonal pattern', 'patrón estacional', 'Fila 08.'),
        ('rapid cycling', 'ciclación rápida', 'Especificador de curso: ≥4 episodios en 12 meses (p. 16).'),
        ('peripartum onset', 'inicio en el periparto', 'Pp. 32 y 33.'),
        ('persistent depressive disorder', 'trastorno depresivo persistente', 'DSM-5-TR retira «dysthymia» del nombre (N2).'),
        ('cyclothymic disorder', 'trastorno ciclotímico', 'Fila 15; p. 13.'),
        ('subthreshold', 'subumbral', 'Síntomas que no alcanzan criterios de episodio.'),
        ('full / partial remission', 'remisión completa / parcial', '«Residuo» no equivale automáticamente a remisión parcial (p. 22).'),
        ('treatment-emergent mania (switch)', 'manía emergente con el tratamiento (viraje)', 'Pp. 24, 31 y 35.'),
        ('antidepressant-induced irritability and mood lability (AIM)', 'irritabilidad y labilidad inducidas por antidepresivos', 'P37; p. 30.'),
        ('bipolar spectrum', 'espectro bipolar', 'Akiskal, Angst y Ghaemi (P06–P08; p. 23).'),
        ('bipolar III', 'bipolar III (denominación de espectro)', 'Hipomanía asociada a antidepresivos; ausente de ICD-10 y DSM-IV (P06).'),
        ('agitated depression', 'depresión agitada', 'Koukopoulos (P09); p. 29.'),
        ('temperament', 'temperamento', 'TEMPS-A (P28); p. 39.'),
        ('life chart', 'cronograma vital', 'Representación gráfica del curso, como las láminas 01–13 (P06).'),
    ]
    xs = (68.0, 400.0, 760.0)
    top = 134.0
    it.append(text(xs[0], top + 10, 'TÉRMINO EN INGLÉS', 'Roboto-Bold', 10, TEAL))
    it.append(text(xs[1], top + 10, 'TÉRMINO EN EL ATLAS', 'Roboto-Bold', 10, TEAL))
    it.append(text(xs[2], top + 10, 'NOTA Y FUENTE', 'Roboto-Bold', 10, TEAL))
    top += 20
    for k, (en, es, nt) in enumerate(rows):
        lines_en = wrap(en, 'Roboto-Medium', 11, 312)
        lines_es = wrap(es, 'Roboto-Medium', 11, 340)
        lines_nt = wrap(nt, 'Roboto-Regular', 11, 380)
        nl = max(len(lines_en), len(lines_es), len(lines_nt))
        h = nl * 14 + 12
        if k % 2 == 0:
            it.append(rect_top(48, top, 1143, top + h, 0, fill=(0.976, 0.98, 0.973)))
        for j, ln in enumerate(lines_en):
            it.append(text(xs[0], top + 16 + j * 14, ln, 'Roboto-Medium', 11, INK))
        for j, ln in enumerate(lines_es):
            it.append(text(xs[1], top + 16 + j * 14, ln, 'Roboto-Medium', 11, NAVY))
        for j, ln in enumerate(lines_nt):
            it.append(text(xs[2], top + 16 + j * 14, ln, 'Roboto-Regular', 11, GRAY))
        top += h
    it.append(line_top(48, top, 1143, top, stroke=LINE, lw=1.0))
    it.append(text(51, top + 24, 'Las traducciones son descriptivas del atlas; cotejar con la edición española oficial del DSM-5-TR '
                   'y con la traducción de la ICD-11.', 'Roboto-Medium', 10, GRAY))
    return it


# ------------------------------------------------------------------ 42
def p42():
    n = 42
    it = new_page('Guía de lectura de un caso', 'GUÍA',
                  'I · orden de lectura del atlas; no es un algoritmo diagnóstico ni sustituye la entrevista', n)
    subtitle(it, 'Once preguntas, en el orden en que suelen abrirse, con las páginas donde el atlas las desarrolla.')
    qs = [
        ('¿Es un episodio actual o un seguimiento?', ['pp. 4–6 (marco temporal)', 'p. 22']),
        ('¿Hubo alguna vez hipomanía o manía observadas, y con qué calidad de observación?', ['p. 3', 'p. 5', 'p. 19', 'p. 34']),
        ('¿Qué polaridad y qué frecuencia de episodios hay? ¿Cuatro o más en 12 meses?', ['pp. 10–18', 'p. 16']),
        ('¿Hay síntomas contrapolares concurrentes, y según qué definición?', ['p. 7', 'p. 8', 'p. 29']),
        ('¿Hay psicosis? ¿Solo durante los episodios afectivos?', ['p. 18', 'p. 25']),
        ('¿Hubo exposición a antidepresivos, otros fármacos o sustancias? ¿Con qué cronología?', ['pp. 24, 31, 35–37']),
        ('¿Existe relación con el embarazo o el posparto?', ['pp. 32–33']),
        ('¿Cómo se evalúa el riesgo suicida? (en todas las fases)', ['p. 28']),
        ('¿Qué instrumentos pueden ayudar y qué no miden?', ['pp. 26–27']),
        ('¿Qué diferenciales y comorbilidades quedan abiertas?', ['p. 36', 'p. 38', 'p. 39']),
        ('¿Qué incertidumbre persiste y qué se reevaluará?', ['p. 9', 'p. 19', 'p. 30']),
    ]
    top = 132.0
    for k, (q, dest) in enumerate(qs):
        h = 44.0
        it.append(rect_top(50, top, 1141, top + h, 8, fill=WHITE, stroke=LINE, lw=1.0))
        it.append(rect_top(62, top + 8, 90, top + 36, 14, fill=NAVY))
        num = str(k + 1)
        it.append(text(76 - sw(num, 'Roboto-Bold', 12) / 2, top + 26, num, 'Roboto-Bold', 12, WHITE))
        it.append(text(106, top + 27, q, 'Roboto-Medium', 13.5, INK))
        x = 1128.0
        for d in reversed(dest):
            wd = sw(d, 'Roboto-Medium', 10.5) + 20
            x -= wd
            it.append(rect_top(x, top + 11, x + wd, top + 33, 10, fill=PILLFILL))
            it.append(text(x + 10, top + 26, d, 'Roboto-Medium', 10.5, TEAL))
            x -= 8
        assert x > 106 + sw(q, 'Roboto-Medium', 13.5) + 12, ('guía solapa', k)
        top += h + 6
    note(it, 50, top + 6, 1141, 'I · Qué es y qué no es esta guía',
         ['Ordena la lectura del atlas. No es un algoritmo diagnóstico: las atribuciones se establecen con entrevista, duración, '
          'deterioro, exclusiones y contexto (p. 3).'], where='p42')
    return it


NEW_PAGES = [p26, p27, p28, p29, p30, p31, p32, 'p33', 'p34', 'p35', p36, p37, p38, p39, p40, p41, p42]

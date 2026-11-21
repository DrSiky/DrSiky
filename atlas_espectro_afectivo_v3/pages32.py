"""Ampliación III del Atlas v3.2 (pp. 42–48) y guía de lectura actualizada (p. 49).

Convención: F criterio formal · E hallazgo empírico (con su P##) · I interpretación · H hipótesis o
propuesta · G geometría editorial no calibrada. Las cifras proceden de los resúmenes de PubMed
verificados el 13-nov-2026 (refs32.py)."""
from layout31 import (new_page, card, card_row, card_height, note, hbars, forest, make_sheet, sw,
                      text, rect_top, line_top, path, rrect_ops, PURPLE, OCHRE, PILLFILL, WARN,
                      WHITE, NAVY, INK, GRAY, LINE, TEAL, BLUE, RED, xi, PANEL)

X2 = [(50.0, 584.0), (607.0, 1141.0)]
X3 = [(50.0, 395.0), (417.0, 772.0), (794.0, 1141.0)]


def subtitle(it, s, base=119.0):
    it.append(text(51.0, base, s, 'Roboto-Regular', 12.5, GRAY))


def panel(it, x0, t0, x1, t1, title, accent=BLUE):
    it.append(rect_top(x0, t0, x1, t1, 10, fill=WHITE, stroke=LINE, lw=1.0))
    it.append(rect_top(x0, t0, x0 + 5, t1, 2, fill=accent))
    it.append(text(x0 + 18, t0 + 27, title, 'Roboto-Bold', 14, NAVY))
    assert sw(title, 'Roboto-Bold', 14) < x1 - x0 - 30, title


# ------------------------------------------------------------------ 42
def p42():
    n = 42
    it = new_page('Pródromos, sueño y ritmos', 'CURSO · RECAÍDA',
                  'E · P52, P54, P55 | H · P53 | I · firma prodrómica individual; G · lámina 14 en p. 43', n)
    subtitle(it, 'Los síntomas que preceden a la recaída son identificables en la mayoría de los casos; el sueño es el más constante antes de la manía.')
    top = 130.0
    top = card_row(it, [
        dict(title='Pródromos maníacos y depresivos', pill='E · P52', body=[
            'Revisión sistemática: 17 estudios (n = 1.191). Al menos el 80 % de las personas con un trastorno del ánimo identifica uno '
            'o más síntomas prodrómicos. En el trastorno bipolar, los pródromos de manía se reconocen con más frecuencia que los de '
            'depresión; el síntoma precoz de manía más robusto es la alteración del sueño (prevalencia mediana del 77 %). Los '
            'síntomas precoces de depresión son inconsistentes.',
            'Datos limitados en trastornos unipolares; pocos estudios prospectivos.']),
        dict(title='Reducción del sueño como vía final común', pill='H · P53', body=[
            'Modelo propuesto por Wehr, Sack y Rosenthal: diversos desencadenantes convergerían en la pérdida de sueño, que '
            'puede inducir el viraje a manía; la manía, a su vez, produce insomnio, de modo que el proceso tiende a '
            'autoperpetuarse.',
            'Es un modelo (H), no una regla causal individual; el atlas lo usa para ordenar preguntas, no para atribuir.']),
    ], top, X2, where='p42', bsize=12, lead=17.4) + 14
    top2 = card_row(it, [
        dict(title='Sueño y ritmos circadianos', pill='E · H · P54', body=[
            'Revisión de Harvey: la alteración del sueño figura entre los correlatos más prominentes de los episodios y de la '
            'recuperación insuficiente, y contribuye a la recaída. Propone un modelo bidireccional entre la regulación '
            'afectiva diurna y el sueño nocturno (H).']),
        dict(title='Enseñar a reconocer síntomas precoces', pill='E · P55', body=[
            'Ensayo aleatorizado, simple ciego (n = 69; 7–12 sesiones con psicólogo más tratamiento habitual): percentil 25 del '
            'tiempo hasta la primera recaída maníaca, 65 frente a 17 semanas; 30 % menos recaídas maníacas en 18 meses (IC 95 % '
            '8–52 %). Sin efecto sobre las recaídas depresivas; mejoría del funcionamiento social y del empleo.']),
    ], top, X2, where='p42', bsize=12, lead=17.4) + 14
    # gráfico de rangos de duración (P52)
    t0, t1 = top2, top2 + 168
    panel(it, 50, t0, 692, t1, 'Duración de los pródromos (P52)')
    x0, x1 = 196.0, 664.0

    def px(d):
        return x0 + d / 365.0 * (x1 - x0)
    for d in (0, 30, 60, 90, 120, 180, 240, 300, 365):
        it.append(line_top(px(d), t0 + 44, px(d), t0 + 124, stroke=LINE, lw=0.6))
        s = str(d)
        it.append(text(px(d) - sw(s, 'Roboto-Regular', 9) / 2, t0 + 138, s, 'Roboto-Regular', 9, GRAY))
    it.append(text(x1 - sw('días', 'Roboto-Regular', 9), t0 + 152, 'días', 'Roboto-Regular', 9, GRAY))
    for k, (lab, lo, hi, mean, col) in enumerate((('Pródromo maníaco', 1, 120, 'media > 20 días', RED),
                                                  ('Pródromo depresivo', 2, 365, 'media < 19 días', BLUE))):
        yb = t0 + 70 + 36 * k
        it.append(text(68, yb + 4, lab, 'Roboto-Medium', 11, INK))
        it.append(rect_top(px(lo), yb - 6, px(hi), yb + 6, 6, fill=col, alpha=0.35))
        it.append(text(px(hi) + 6 if hi < 300 else px(255), yb - 9 if hi >= 300 else yb + 4,
                       'rango %d–%d' % (lo, hi), 'Roboto-Regular', 9.5, INK))
        mx = px(20)
        it.append(line_top(mx, yb - 9, mx, yb + 9, stroke=col, lw=2.2))
        it.append(text(mx + 6, yb + 17, mean, 'Roboto-Medium', 9, col))
    it.append(text(68, t1 - 12, 'E · Rangos entre individuos y medias señaladas en la revisión; marca vertical aproximada.', 'Roboto-Regular', 9.5, GRAY))
    note(it, 714, t0, 1141, 'I · Firma prodrómica individual', [
        'El pródromo se reconstruye con cada persona y con terceros: qué cambió primero (sueño, energía, sociabilidad, gasto, '
        'irritabilidad) y con qué antelación. En la manía, la pregunta por el sueño encabeza la lista (P52, P53).',
        'Lámina 14 (p. 43): ilustración no calibrada.'], kind='info', t1=t1, where='p42')
    note(it, 50, t1 + 14, 1141, 'I · Qué hace y qué no hace el atlas', [
        'Recoge la cronología previa a cada episodio como dato del curso. No convierte el insomnio aislado en pródromo ni '
        'propone un plan de intervención: el ensayo P55 muestra un efecto de grupo sobre la recaída maníaca, no un umbral individual.'],
         where='p42')
    return it


# ------------------------------------------------------------------ 43 (lámina 14)
def p43(tpl):
    curves = {
        'dep': [0.24, 0.23, 0.24, 0.25, 0.26, 0.24, 0.23, 0.30, 0.40, 0.36, 0.28, 0.25],
        'act': [0.32, 0.31, 0.33, 0.40, 0.52, 0.82, 0.86, 0.62, 0.40, 0.34, 0.32, 0.31],
        'fun': [0.82, 0.83, 0.82, 0.78, 0.70, 0.40, 0.34, 0.50, 0.62, 0.72, 0.78, 0.80],
        'res': [0.22, 0.22, 0.24, 0.50, 0.72, 0.86, 0.84, 0.55, 0.35, 0.28, 0.26, 0.25]}
    rows = [(140.0, 134.0, [(0.0, 2.7, 'Eutimia', 'neu', False), (2.7, 4.7, 'Pródromo', 'elev', False),
                            (4.7, 7.3, 'Episodio maníaco', 'elev', False), (7.3, 11.4, 'Recuperación', 'neu', False)]),
            (159.0, 153.0, [(2.7, 4.7, 'Sueño · activación', 'elev'), (4.7, 7.3, 'Manía', 'elev')])]
    alt = [('act', 4, [0.52, 0.50, 0.42, 0.36, 0.33], RED)]
    top_, base_ = PANEL['act']
    notes_in = [(xi(7.1), base_ - 0.13 * (base_ - top_), 'trazos: pródromo reconocido, sin episodio (H; efecto de grupo en P55)', RED)]
    it = make_sheet(tpl, pageno=43, title='Curso 14 · Pródromo y recaída maníaca',
                    tag='G · viñeta ilustrativa | E · P52, P54, P55 | H · P53 | I · relación con p. 42',
                    subtitle='La alteración del sueño precede a la activación y al umbral de manía; la trayectoria discontinua ilustra un '
                             'pródromo reconocido que no llega a episodio.',
                    curves=curves, rows=rows, thr=(0.60, 0.60, 'umbral de manía'), markers=[(3.0, 'primer signo')],
                    alt=alt, notes_in=notes_in,
                    extra_foot='Panel inferior: sueño. Trazos gruesos: alternativa.')
    for x in it:
        if x['k'] == 'text' and x['text'] == 'RESIDUO':
            x['text'] = 'SUEÑO'
        elif x['k'] == 'text' and x['text'].strip() == 'carga':
            x['text'] = 'alteración'
    return it


# ------------------------------------------------------------------ 44
def p44():
    n = 44
    it = new_page('Residuo funcional y cognitivo entre episodios', 'CURSO · INTERVALO',
                  'E · P56–P60 | I · el panel RESIDUO de las láminas representa esta carga sin unidades', n)
    subtitle(it, 'La remisión sintomática no equivale a recuperación completa: función y cognición pueden mantener déficits entre episodios.')
    top = 130.0
    top = card_row(it, [
        dict(title='Cognición según el estado', pill='E · P56', body=[
            'Grupos deprimido (30), maníaco o hipomaníaco (34), eutímico con 6 meses de remisión (44) y controles (30). Todos los '
            'grupos bipolares mostraron déficits de memoria verbal y de función ejecutiva; el bajo rendimiento se asoció con peor '
            'evolución funcional. La memoria verbal se relacionó con la duración de la enfermedad, el número de episodios maníacos, '
            'las hospitalizaciones y los intentos de suicidio.']),
        dict(title='Eutimia bipolar · datos individuales', pill='E · P57', body=[
            'Metaanálisis de datos individuales: 31 conjuntos, N = 2.876. Déficits en las 11 medidas (tamaños del efecto '
            '0,26–0,63) tras controlar edad, CI y sexo. Los síntomas residuales confunden pero no explican el efecto, que no se '
            'relacionó con el tratamiento. Los déficits podrían ser menores que los descritos antes.']),
        dict(title='Depresión · remisión', pill='E · P60', body=[
            'Metaanálisis con CANTAB: en la depresión, déficits de d −0,34 a −0,65. En remisión persisten los de función ejecutiva '
            'y atención (d −0,52 a −0,61); los de memoria no fueron significativos (−0,22 a −0,54).']),
    ], top, X3, where='p44', bsize=11.5, lead=16.6) + 14
    t0 = top
    t1 = t0 + 238.0
    card(it, 50, t0, 692, t1=t1, title='Discapacidad psicosocial a lo largo del curso', pill='E · P58', body=[
        'Seguimiento prospectivo de 158 pacientes con bipolar I y 133 con bipolar II durante una media de 15 años. El deterioro aumenta '
        'con cada incremento de la gravedad depresiva; los síntomas depresivos son al menos tan incapacitantes como los maníacos '
        'o hipomaníacos de gravedad equivalente. Los síntomas depresivos subsindrómicos se asocian con deterioro significativo; '
        'los hipomaníacos subsindrómicos en bipolar II no lo hacen e incluso podrían mejorar el funcionamiento.',
        'Asintomáticos, los pacientes funcionan bien, aunque no tanto como los controles.'], where='p44', bsize=12, lead=17.4)
    # FAST (P59)
    panel(it, 714, t0, 1141, t1, 'FAST: puntuación media por estado (P59)', accent=TEAL)
    hbars(it, 732, t0 + 74, 34.0, [('Eutímicos', 18.55, '18,55'), ('Maníacos', 40.44, '40,44'),
                                   ('Depresivos', 43.21, '43,21')], 45.0, 5.2, 92.0, color=TEAL, lsize=11)
    yb = t0 + 74 + 34 * 2 + 32
    for ln in ('24 ítems en seis áreas: autonomía, trabajo, cognición, finanzas,',
               'relaciones y ocio. 101 pacientes y 61 controles; α = 0,909;',
               'r = −0,903 con la GAF; CCI test-retest 0,98; unos 6 minutos.',
               'Mayor puntuación = más dificultad funcional.'):
        if yb < t1 - 8:
            it.append(text(732, yb, ln, 'Roboto-Regular', 10.5, GRAY))
        else:
            WARN.append('p44: FAST texto desborda')
        yb += 15
    top = t1 + 14
    top = card_row(it, [
        dict(title='I · Lectura en el atlas', body=[
            'El panel RESIDUO de las láminas (pp. 10–18, 33–35) dibuja esta carga intercrisis sin unidades. Que exista residuo no '
            'cambia la polaridad ni el diagnóstico: describe la recuperación.']),
        dict(title='I · Qué preguntar en el intervalo', body=[
            'Síntomas depresivos subumbrales (P58), quejas de memoria o concentración, rendimiento laboral y autonomía (áreas de '
            'la FAST, P59). La exploración cognitiva formal requiere instrumentos y profesionales propios.']),
    ], top, X2, where='p44', accent=OCHRE, fill=(0.960784, 0.929412, 0.862745), bsize=12, lead=17.4)
    return it


# ------------------------------------------------------------------ 45
def p45():
    n = 45
    it = new_page('Polaridad predominante y depresión bipolar o unipolar', 'CURSO · POLARIDAD',
                  'E · P61–P63 | H · propuesta probabilística (P63) | I · ningún rasgo es patognomónico', n)
    subtitle(it, 'Dos preguntas longitudinales distintas: hacia qué polo tiende un curso bipolar y qué hace más probable que una depresión sea bipolar.')
    top = 130.0
    left = (50.0, 584.0)
    t = card(it, *left[:1], top, left[1], title='Polaridad predominante', pill='E · P61', body=[
        'n = 224: polaridad depresiva en 135 (60,3 %) y maníaca en 89 (39,7 %). La maníaca predominó en bipolar I. La depresiva se '
        'asoció con inicio depresivo y con intentos de suicidio a lo largo de la vida (y más intentos). Los patrones de tratamiento '
        'diferían; los autores la proponen como parámetro pronóstico válido.'], where='p45', bsize=12, lead=17.4) + 14
    t = card(it, 50, t, 584, title='Índice de polaridad', pill='E · P62', body=[
        'De 604 pacientes, 257 (43 %) cumplieron criterios de polaridad predominante: depresiva 143 (55,6 %), maníaca 114 (44,4 %). '
        'Maníaca: bipolar I, sexo masculino, menor edad, inicio y primera hospitalización más tempranos, más hospitalizaciones, uso '
        'de sustancias y psicosis. Depresiva: bipolar II, inicio depresivo, acontecimientos vitales, melancolía e intentos de suicidio.'],
        where='p45', bsize=12, lead=17.4) + 14
    # barras comparativas
    t1 = t + 132
    panel(it, 50, t, 584, t1, 'Reparto de la polaridad predominante', accent=BLUE)
    for k, (lab, dep, man) in enumerate((('P61 · n = 224', 60.3, 39.7), ('P62 · n = 257', 55.6, 44.4))):
        yb = t + 64 + 32 * k
        it.append(text(68, yb + 4, lab, 'Roboto-Medium', 11, INK))
        xa, xb = 190.0, 560.0
        xm = xa + (xb - xa) * dep / 100.0
        it.append(rect_top(xa, yb - 9, xm, yb + 9, 2, fill=BLUE))
        it.append(rect_top(xm, yb - 9, xb, yb + 9, 2, fill=RED))
        s1 = ('depresiva %.1f %%' % dep).replace('.', ',')
        s2 = ('maníaca %.1f %%' % man).replace('.', ',')
        it.append(text(xa + 8, yb + 4, s1, 'Roboto-Medium', 10, WHITE))
        it.append(text(xb - 8 - sw(s2, 'Roboto-Medium', 10), yb + 4, s2, 'Roboto-Medium', 10, WHITE))
    it.append(text(68, t1 - 14, 'E · En P62 solo el 43 % de la muestra cumplió criterios de predominio.', 'Roboto-Regular', 9.5, GRAY))
    # tabla probabilística (P63)
    x0, x1 = 607.0, 1141.0
    tt1 = t1
    panel(it, x0, top, x1, tt1, 'Depresión bipolar I frente a unipolar (P63)', accent=PURPLE)
    it.append(text(x0 + 18, top + 48, 'Revisión: no hay rasgos patognomónicos; hay diferencias de frecuencia replicadas.', 'Roboto-Regular', 10.5, GRAY))
    cols = [(x0 + 18, 'Más frecuente en depresión bipolar I', BLUE,
             ['Rasgos «atípicos»: hipersomnia, hiperfagia,', 'parálisis plúmbea', 'Enlentecimiento psicomotor',
              'Síntomas psicóticos o culpa patológica', 'Labilidad del ánimo', 'Inicio más temprano',
              'Más episodios depresivos previos', 'Episodios más breves', 'Antecedente familiar de bipolaridad']),
            (x0 + 278, 'Más frecuente en depresión unipolar', GRAY,
             ['Insomnio inicial o sueño reducido', 'Pérdida de apetito o de peso', 'Actividad normal o aumentada',
              'Quejas somáticas', 'Inicio más tardío', 'Episodios prolongados', 'Sin antecedente familiar', 'de bipolaridad'])]
    for (cx, head, col, lines) in cols:
        yb = top + 82
        it.append(rect_top(cx, yb - 14, cx + 240, yb + 6, 4, fill=PILLFILL))
        it.append(text(cx + 8, yb, head, 'Roboto-Bold', 10.5, col if col != GRAY else INK))
        yb += 28
        for ln in lines:
            cont = ln[0].islower()
            if not cont:
                it.append(rect_top(cx + 2, yb - 7, cx + 7, yb - 2, 2, fill=col))
            it.append(text(cx + 14, yb, ln, 'Roboto-Regular', 11, INK))
            yb += 19 if not cont else 19
        assert yb < tt1 - 120, ('tabla P63', yb, tt1)
    yb = tt1 - 104
    for ln in ('Los rasgos de la primera columna también son más frecuentes en las',
               'depresiones unipolares que más tarde «convierten» a bipolar.',
               'H · Los autores proponen un enfoque probabilístico, no una distinción',
               'categórica: no hay «punto de rareza» entre ambas presentaciones.',
               'Sus detalles operativos están por explorar (P63).'):
        it.append(text(x0 + 18, yb, ln, 'Roboto-Regular', 11, GRAY))
        yb += 17
    note(it, 50, tt1 + 14, 1141, 'I · Uso en el atlas', [
        'La polaridad predominante describe el curso de un trastorno bipolar ya establecido; la tabla de P63 orienta la sospecha en una '
        'depresión sin hipomanía conocida. Ninguna de las dos asigna un perfil de la matriz: se suman a los marcadores de la p. 30 y a '
        'la reevaluación de la lámina 12 (p. 34).'], where='p45')
    return it


# ------------------------------------------------------------------ 46
def p46():
    n = 46
    it = new_page('Vivencia y tiempo vivido en la depresión', 'FENOMENOLOGÍA',
                  'I · fenomenología (P64, P66) | E · estudio cualitativo (P65) | H · desincronización (P64); responde a la p. 25', n)
    subtitle(it, 'Lo que la p. 25 dejó como capa descriptiva: el tiempo, el cuerpo y la relación con los otros, con bibliografía propia.')
    top = 130.0
    top = card_row(it, [
        dict(title='Melancolía como desincronización', pill='H · I · P64', body=[
            'Fuchs describe procesos continuos de sincronización, biológicos y sociales, que permiten compensar carencias, adaptarse, '
            'cerrar el pasado y reconectar con el presente: regeneración, sueño, sueños, olvido, remordimiento o duelo.',
            'La melancolía se interpreta como un desacoplamiento temporal entre organismo y entorno, o entre individuo y sociedad: al '
            'fallar la resincronización, la persona «cae» del tiempo común. Permite un paralelo entre hallazgos cronobiológicos y '
            'psicosociales, y esboza una «terapia resincronizadora».']),
        dict(title='Experiencias temporales anómalas', pill='E · P65', body=[
            'Estudio cualitativo (550 pacientes con trastornos afectivos y esquizofrénicos). De 100 con depresión mayor, 96 refirieron '
            'al menos una experiencia temporal anómala: retardo vital, estancamiento de los procesos vitales endógenos (37); presente y '
            'futuro dominados por el pasado (29); enlentecimiento del flujo del tiempo (25).',
            'A diferencia de la esquizofrenia, no hay desarticulación de la síntesis temporal, sino un trastorno de la conación: '
            '«inhibición del devenir». La entrevista no era cuantitativa (no se excluyen falsos negativos).']),
        dict(title='Depresión y empatía', pill='I · P66', body=[
            'Ratcliffe sostiene que la depresión implica una pérdida de la capacidad de relación interpersonal de la que depende la '
            'empatía mutua: la persona se siente separada de los demás.',
            'Propone entender la empatía como una exploración de tipo perceptivo de la experiencia ajena, más que como simulación. '
            'Es un análisis filosófico, no un estudio empírico.']),
    ], top, X3, where='p46', bsize=11.5, lead=16.6) + 14
    top = card(it, 50, top, 1141, title='I · Preguntas abiertas de entrevista (no es una escala)', body=[
        'Tiempo: «¿Cómo pasan las horas y los días?», «¿Puede imaginarse dentro de unos meses?», «¿Siente que el pasado lo ocupa todo?» '
        '(categorías de P65).   Ritmo y cuerpo: «¿Su cuerpo va a otro ritmo que el de los demás?»; sueño y despertar (P64).',
        'Relación: «¿Se siente alcanzado por los demás, o separado?», «¿Puede sentir lo que otros sienten?» (P66).   Las respuestas '
        'enriquecen la descripción; no se puntúan ni se toman como indicio de bipolaridad (p. 25).'], where='p46', bsize=12, lead=17.4) + 14
    note(it, 50, top, 1141, 'I · Por qué figura aquí y con qué límites', [
        'La fenomenología describe cómo se vive el episodio y ayuda a distinguir formas de depresión (P65 lo apunta para el diagnóstico '
        'diferencial), pero sus hallazgos son cualitativos o conceptuales. El atlas no los traduce a la geometría ni a las curvas.'],
         kind='info', where='p46')
    return it


# ------------------------------------------------------------------ 47
def p47():
    n = 47
    it = new_page('Estrés de minorías: personas LGTB y salud mental', 'CONTEXTO · MINORÍAS',
                  'E · P67–P69 | H · modelo de estrés de minorías (P67) | I · el atlas sitúa el riesgo en el contexto, no en la orientación', n)
    subtitle(it, 'Mayor prevalencia de trastornos mentales y de conducta suicida en personas LGB; el modelo de Meyer la atribuye al estrés social, no a la orientación.')
    top = 130.0
    t = card(it, 50, top, 584, title='Modelo de estrés de minorías', pill='H · E · P67', body=[
        'Meyer revisa metaanálisis que muestran mayor prevalencia de trastornos mentales en personas lesbianas, gais y bisexuales, '
        'y la explica con un modelo de estrés de minorías: el estigma, el prejuicio y la discriminación crean un entorno social '
        'hostil y estresante.',
        'Procesos del modelo: acontecimientos de prejuicio, expectativas de rechazo, ocultación, homofobia interiorizada y '
        'afrontamiento compensador.'], where='p47', bsize=12, lead=17.4)
    t2 = card(it, 607, top, 1141, title='Revisión sistemática con metaanálisis', pill='E · P68', body=[
        '25 estudios poblacionales: 214.344 participantes heterosexuales y 11.971 no heterosexuales. Rangos de riesgo relativo: '
        'depresión y trastornos de ansiedad (12 meses o toda la vida) 1,54–2,58; dependencia de alcohol u otras sustancias '
        '(12 meses) 1,51–4,00. Resultados similares en ambos sexos.',
        'Limitación: solo un estudio cumplió los cuatro criterios de calidad.'], where='p47', bsize=12, lead=17.4)
    t = max(t, t2) + 14
    # gráfico de bosque (P68)
    t1 = t + 168
    panel(it, 50, t, 1141, t1, 'Riesgos relativos seleccionados frente a personas heterosexuales (P68), IC 95 %', accent=RED)
    forest(it, 470.0, 960.0, t + 66, 32.0, [('Intento de suicidio, vida · personas LGB', 2.47, 1.87, 3.28),
                                            ('Intento de suicidio, vida · hombres gais y bisexuales', 4.28, 2.32, 7.88),
                                            ('Dependencia de alcohol, 12 meses · mujeres lesbianas y bisexuales', 4.00, 2.85, 5.61)],
           0.8, 10.0, [1, 2, 4, 8], unit='RR', ci=True)
    t = t1 + 14
    t = card_row(it, [
        dict(title='Trastorno mental grave en población LGTB', pill='E · P69', body=[
            'Revisión de alcance (27 publicaciones): menor satisfacción con los servicios y evidencia mínima sobre intervenciones. El '
            'mayor riesgo se asoció con la discriminación; se describe el beneficio de espacios donde las personas pueden mostrarse '
            'abiertamente («estar fuera del armario»).']),
        dict(title='I · Lectura en el atlas', body=[
            'Preguntar por discriminación, ocultación y apoyo forma parte de la historia, sin presuponer patología. Enlaza con el riesgo '
            'suicida (p. 28) y con el chemsex (p. 37). No se localizaron datos específicos de trastorno bipolar en personas LGTB que '
            'cumplieran los criterios de selección del atlas.']),
    ], t, X2, where='p47', bsize=12, lead=17.4)
    return it


# ------------------------------------------------------------------ 48
def p48():
    n = 48
    it = new_page('Psicosis cicloide (Leonhard) en el diferencial', 'DIFERENCIAL · PSICOSIS',
                  'E · P71 | I · P70 (revisión conceptual) | G · posición ordinal, sin escala | I · relación con pp. 25 y 38', n)
    subtitle(it, 'Una tradición nosológica no recogida por los sistemas actuales, a medio camino entre la esquizofrenia y los trastornos del ánimo.')
    top = 130.0
    top = card_row(it, [
        dict(title='Concepto e historia', pill='I · P70', body=[
            'Las psicosis cicloides se basan en los fenotipos descritos por Leonhard, en la tradición de Wernicke y Kleist. Según los '
            'autores, resuelven el dilema de las «psicosis atípicas» kraepelinianas, aunque el concepto aún no tiene reconocimiento '
            'general.']),
        dict(title='Estudio clínico y nosológico', pill='E · P71', body=[
            '660 pacientes psicóticos ingresados; 68 (10,3 %) cumplían los criterios de Perris y Brockington. Buena validez '
            'discriminante (95 % de casos bien clasificados) y escasa concordancia con DSM-III-R, DSM-IV o ICD-10 (κ < 0,22). '
            'Subgrupos afectivo (38) y no afectivo (30), con mejor evolución global del no afectivo.']),
    ], top, X2, where='p48', bsize=12, lead=17.4) + 14
    # diagrama ordinal
    t0, t1 = top, top + 262
    panel(it, 50, t0, 1141, t1, 'Dónde se sitúa la psicosis cicloide respecto de sus vecinos (P71)', accent=PURPLE)
    xa, xb = 420.0, 1060.0
    it.append(text(xa - sw('Esquizofrenia', 'Roboto-Bold', 11) / 2, t0 + 58, 'Esquizofrenia', 'Roboto-Bold', 11, INK))
    it.append(text(xb - sw('Trastornos del ánimo', 'Roboto-Bold', 11) / 2, t0 + 58, 'Trastornos del ánimo', 'Roboto-Bold', 11, INK))
    rows = [('Síntomas psicóticos, desorganización y de primer rango', 0.0, 'comparables a la esquizofrenia'),
            ('Síntomas afectivos', 0.5, 'intermedios'),
            ('Mayoría de variables clínicas', 0.82, 'más próxima a los trastornos del ánimo'),
            ('Riesgo de trastornos del ánimo en familiares', 0.82, 'más próxima a los trastornos del ánimo')]
    for k, (lab, pos, desc) in enumerate(rows):
        yb = t0 + 90 + 34 * k
        it.append(text(68, yb + 4, lab, 'Roboto-Regular', 11, INK))
        it.append(line_top(xa, yb, xb, yb, stroke=LINE, lw=1.4))
        for xe in (xa, xb):
            it.append(line_top(xe, yb - 5, xe, yb + 5, stroke=GRAY, lw=1.2))
        cx = xa + pos * (xb - xa)
        it.append(path(rrect_ops(cx - 6, 842 - (yb + 6), cx + 6, 842 - (yb - 6), 6), fill=PURPLE, stroke=PURPLE, lw=1.0))
        dx = cx + 12 if pos < 0.7 else cx - 12 - sw(desc, 'Roboto-Medium', 9.5)
        it.append(text(dx, yb - 8, desc, 'Roboto-Medium', 9.5, PURPLE))
    it.append(text(68, t1 - 24, 'Además, mayores estresores psicosociales que en la esquizofrenia y en los trastornos del ánimo.',
                   'Roboto-Regular', 10.5, INK))
    it.append(text(68, t1 - 9, 'G · Posiciones ordinales que resumen la comparación del resumen; no son distancias medidas.',
                   'Roboto-Regular', 9.5, GRAY))
    top = t1 + 14
    top = card_row(it, [
        dict(title='I · Relevancia para el atlas', body=[
            'Una psicosis aguda y remitente con carga afectiva plantea a la vez el diferencial con la manía o la depresión con '
            'psicosis (p. 25) y con otras psicosis (p. 38). La categoría cicloide no se corresponde con ninguna categoría DSM o ICD y '
            'no está bien representada por las definiciones formales de psicosis remitentes (P71).']),
        dict(title='I · Límite', body=[
            'El atlas la cita como concepto histórico y de investigación. No la incorpora a la matriz ni propone criterios: los de '
            'Perris y Brockington se mencionan solo como los usados en P71.']),
    ], top, X2, where='p48', accent=OCHRE, fill=(0.960784, 0.929412, 0.862745), bsize=12, lead=17.4)
    return it


# ------------------------------------------------------------------ 49 (guía)
def guide(n=49, extra=(), word='Catorce'):
    it = new_page('Guía de lectura de un caso', 'GUÍA',
                  'I · orden de lectura del atlas; no es un algoritmo diagnóstico ni sustituye la entrevista', n)
    subtitle(it, word + ' preguntas, en el orden en que suelen abrirse, con las páginas donde el atlas las desarrolla.')
    qs = [
        ('¿Es un episodio actual o un seguimiento?', ['pp. 4–6 (marco temporal)', 'p. 22']),
        ('¿Hubo alguna vez hipomanía o manía observadas, y con qué calidad de observación?', ['p. 3', 'p. 5', 'p. 19', 'p. 34']),
        ('¿Qué polaridad y qué frecuencia de episodios hay? ¿Cuatro o más en 12 meses?', ['pp. 10–18', 'p. 16', 'p. 45']),
        ('¿Hay síntomas contrapolares concurrentes, y según qué definición?', ['p. 7', 'p. 8', 'p. 29']),
        ('¿Hay psicosis? ¿Solo durante los episodios afectivos?', ['p. 18', 'p. 25', 'p. 48']),
        ('¿Hubo exposición a antidepresivos, otros fármacos o sustancias? ¿Con qué cronología?', ['pp. 24, 31, 35–37']),
        ('¿Existe relación con el embarazo o el posparto?', ['pp. 32–33']),
        ('¿Qué precedió a cada episodio? ¿Cambió primero el sueño?', ['pp. 42–43']),
        ('¿Cómo funciona la persona entre episodios? ¿Qué residuo queda?', ['p. 44']),
        ('¿Cómo vive el tiempo, el cuerpo y la relación con los otros?', ['p. 46']),
        ('¿Cómo se evalúa el riesgo suicida (en todas las fases) y qué estresores de contexto lo modulan?', ['p. 28', 'p. 47']),
        ('¿Qué instrumentos pueden ayudar y qué no miden?', ['pp. 26–27']),
        ('¿Qué diferenciales y comorbilidades quedan abiertas?', ['p. 36', 'p. 38', 'p. 39', 'p. 48']),
        ('¿Qué incertidumbre persiste y qué se reevaluará?', ['p. 9', 'p. 19', 'p. 30', 'p. 45']),
    ] + list(extra)
    top = 130.0
    h, gap = (36.0, 4.0) if len(qs) <= 14 else ((34.0, 3.0) if len(qs) == 15 else ((32.0, 2.5) if len(qs) == 16 else ((30.0, 2.0) if len(qs) == 17 else ((28.4, 1.8) if len(qs) == 18 else (27.0, 1.6)))))
    for k, (q, dest) in enumerate(qs):
        it.append(rect_top(50, top, 1141, top + h, 8, fill=WHITE, stroke=LINE, lw=1.0))
        it.append(rect_top(62, top + h / 2 - 13, 88, top + h / 2 + 13, 13, fill=NAVY))
        num = str(k + 1)
        it.append(text(75 - sw(num, 'Roboto-Bold', 12) / 2, top + h / 2 + 4.5, num, 'Roboto-Bold', 12, WHITE))
        it.append(text(104, top + h / 2 + 5, q, 'Roboto-Medium', 13.5, INK))
        x = 1128.0
        for d in reversed(dest):
            wd = sw(d, 'Roboto-Medium', 10.5) + 20
            x -= wd
            it.append(rect_top(x, top + h / 2 - 11, x + wd, top + h / 2 + 11, 10, fill=PILLFILL))
            it.append(text(x + 10, top + h / 2 + 4, d, 'Roboto-Medium', 10.5, TEAL))
            x -= 8
        assert x > 104 + sw(q, 'Roboto-Medium', 13.5) + 12, ('guía solapa', k)
        top += h + gap
    note(it, 50, top + 4, 1141, 'I · Qué es y qué no es esta guía',
         ['Ordena la lectura del atlas. No es un algoritmo diagnóstico: las atribuciones se establecen con entrevista, duración, '
          'deterioro, exclusiones y contexto (p. 3).'], where='guía')
    return it


NEW_PAGES32 = [p42, 'p43', p44, p45, p46, p47, p48]

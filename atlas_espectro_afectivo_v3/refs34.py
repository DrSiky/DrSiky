"""Atlas v3.4 · Ampliación V (farmacología del trastorno bipolar).

P83–P91: síntesis transversales verificadas en PubMed el 18-nov-2026 (metadatos y resúmenes).
D01–D13: dosieres monográficos del Atlas Glífico (v1.0, 10-nov-2026) aportados por el autor; cada
lámina cita sus fuentes primarias con códigos propios (R fichas técnicas, G guías, T/L ensayos,
E síntesis, P farmacología, S seguridad), que el atlas conserva entre corchetes."""

REFS34 = [
    ('P83', 'Comparative efficacy and acceptability of antimanic drugs in acute mania: a multiple-treatments meta-analysis.',
     'Andrea Cipriani, Corrado Barbui, Georgia Salanti et al.', 'Lancet (London, England). 2011;378(9799):1306-15.',
     '10.1016/S0140-6736(11)60873-8', '21851976'),
    ('P84', 'Comparative efficacy and tolerability of pharmacological interventions for acute bipolar depression in adults: a systematic review and network meta-analysis.',
     'Ayşegül Yildiz, Spyridon Siafis, Dimitris Mavridis et al.', 'The lancet. Psychiatry. 2023 Sep;10(9):693-705.',
     '10.1016/S2215-0366(23)00199-2', '37595997'),
    ('P85', 'Efficacy and tolerability of atypical antipsychotics for acute bipolar depression: a network meta-analysis.',
     'Aditi Kadakia, Carole Dembek, Vincent Heller et al.', 'BMC psychiatry. 2021 May 11;21(1):249.',
     '10.1186/s12888-021-03220-3', '33975574'),
    ('P86', 'Comparative efficacy and tolerability of pharmacological treatments for the treatment of acute bipolar depression: a systematic review and network meta-analysis.',
     'Anees Bahji, Dylan Ermacora, Callum Stephenson et al.', 'Journal of affective disorders. 2020;269:154-184.',
     '10.1016/j.jad.2020.03.030', '32339131'),
    ('P87', 'Mood stabilizers and/or antipsychotics for bipolar disorder in the maintenance phase: a systematic review and network meta-analysis of randomized controlled trials.',
     'Taro Kishi, Toshikazu Ikuta, Yuki Matsuda et al.', 'Molecular psychiatry. 2021;26(8):4146-4157.',
     '10.1038/s41380-020-00946-6', '33177610'),
    ('P88', 'Lithium for prevention of mood episodes in bipolar disorders: systematic review and meta-analysis.',
     'Emanuel Severus, Matthew J Taylor, Cathrin Sauer et al.', 'International journal of bipolar disorders. 2014;2:15.',
     '10.1186/s40345-014-0015-8', '25530932'),
    ('P89', 'Polarity index of pharmacological agents used for maintenance treatment of bipolar disorder.',
     'Dina Popovic, Maria Reinares, Jose Manuel Goikolea et al.', 'European neuropsychopharmacology. 2012;22(5):339-46.',
     '10.1016/j.euroneuro.2011.09.008', '22000157'),
    ('P90', 'Predominant Polarity and Polarity Index of Maintenance Treatments for Bipolar Disorder: A Validation Study in a Large Naturalistic Sample in Italy.',
     'Umberto Albert, Mirko Manchia, Sofia Burato et al.', 'Medicina (Kaunas, Lithuania). 2021;57(6):598.',
     '10.3390/medicina57060598', '34200746'),
    ('P91', 'Canadian Network for Mood and Anxiety Treatments (CANMAT) and International Society for Bipolar Disorders (ISBD) 2018 guidelines for the management of patients with bipolar disorder.',
     'Lakshmi N Yatham, Sidney H Kennedy, Sagar V Parikh et al.', 'Bipolar disorders. 2018;20(2):97-170.',
     '10.1111/bdi.12609', '29536616'),
]

# Dosieres monográficos (fuente interna; sin PMID). (id, fármaco, láminas, título del dosier)
DOSSIERS = [
    ('D01', 'Litio', 15, 'Litio en monoterapia · estabilización aguda y prevención longitudinal'),
    ('D02', 'Valproato', 15, 'Valproato en monoterapia · fase maníaca, continuación y lugar en depresión'),
    ('D03', 'Carbamazepina', 15, 'Carbamazepina en monoterapia · oxcarbazepina y eslicarbazepina en anexos'),
    ('D04', 'Lamotrigina', 15, 'Lamotrigina en monoterapia · prevención depresiva y evidencia por fase'),
    ('D05', 'Quetiapina', 15, 'Quetiapina en monoterapia'),
    ('D06', 'Lurasidona', 15, 'Lurasidona en monoterapia'),
    ('D07', 'Olanzapina y olanzapina-fluoxetina', 17, 'Olanzapina y combinación olanzapina-fluoxetina'),
    ('D08', 'Risperidona y paliperidona', 30, 'Risperidona y paliperidona'),
    ('D09', 'Aripiprazol', 15, 'Aripiprazol en monoterapia'),
    ('D10', 'Cariprazina', 15, 'Cariprazina en monoterapia'),
    ('D11', 'Asenapina', 15, 'Asenapina en monoterapia'),
    ('D12', 'Ziprasidona', 15, 'Ziprasidona en monoterapia'),
    ('D13', 'Haloperidol', 10, 'Haloperidol en monoterapia'),
]

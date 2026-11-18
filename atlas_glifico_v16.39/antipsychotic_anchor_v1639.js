/* v16.39 · Ancla clínica de los 14 antipsicóticos que quedaban «sin ancla revisada».
   Decisión del usuario: la eficacia demostrada solo frente a comparador activo (sin placebo) se acredita con etiqueta propia.
   Agitación aguda ≠ eficacia antimaníaca (la sedación tiene su eje); sin ECA en manía aguda → no se acredita. */
Object.assign(V1637_SRC,{
 torres:['Torres 2024','https://doi.org/10.4088/JCP.23m14966'],
 takahashi:['Takahashi 1975','https://doi.org/10.1001/archpsyc.1975.01760280108010'],
 shopsin:['Shopsin 1975','https://doi.org/10.1001/archpsyc.1975.01760190036004'],
 ishizuka:['Ishizuka 2022','https://doi.org/10.1002/pcn5.60'],
 barbini:['Barbini 1997','https://doi.org/10.1097/00004850-199703000-00006'],
 thomasAmi:['Thomas 2008','https://doi.org/10.2147/ndt.s3135'],
 kwentus:['Kwentus 2012','https://doi.org/10.1111/j.1399-5618.2011.00975.x'],
 khokhar:['Khokhar 2016 (Cochrane)','https://doi.org/10.1002/14651858.CD002830.pub3'],
 zarate:['Zarate 2004','https://doi.org/10.1176/appi.ajp.161.1.169'],
 christie:['Christie 1989','https://doi.org/10.1016/0165-0327(89)90064-5'],
 carpenter:['Carpenter 2001 (Cochrane)','https://doi.org/10.1002/14651858.CD002304'],
 largactilFT:['FT Largactil 4.1','https://cima.aemps.es/cima/dochtml/ft/42934/FT_42934.html'],
 adasuveFT:['FT Adasuve 4.1','https://cima.aemps.es/cima/dochtml/ft/113823002/FT_113823002.html'],
 droperidolFT:['FT droperidol 4.1','https://cima.aemps.es/cima/dochtml/ft/90791/FT_90791.html']
});
Object.assign(V1637_CAT,{
 comparador:'eficacia solo frente a comparador activo (sin placebo) · se acredita',
 agitacion:'eficacia solo en agitación aguda · no se acredita como antimaníaco',
 'sin-eca':'sin ECA en manía aguda localizados (PubMed, nov. 2026) · no se acredita'
});
const V1639_NOECA='Búsqueda en PubMed (noviembre de 2026) sin ensayos controlados en manía aguda; una búsqueda no prueba la ausencia.';
Object.assign(V1637_ANCHOR,{
 Iloperidona:{cat:'demostrada',src:['torres'],note:'ECA fase 3 frente a placebo (n = 414, 4 semanas; YMRS −4,0). Sin comercialización en España.'},
 Clorpromazina:{cat:'comparador',src:['takahashi','shopsin','ishizuka','largactilFT'],note:'ECA doble ciego frente a litio y haloperidol, sin placebo: inferior al litio (Takahashi 1975). El metaanálisis en red de Asia oriental no halló diferencia frente a placebo (tampoco para haloperidol ni litio). La ficha incluye las crisis maníacas entre los estados de agitación.'},
 Clozapina:{cat:'comparador',src:['barbini'],note:'ECA abierto frente a clorpromazina, ambos con litio (n = 30): mejor a las 2 semanas, sin diferencia al final. Resto: estudios abiertos en manía refractaria.'},
 Amisulprida:{cat:'comparador',src:['thomasAmi'],note:'ECA abierto frente a haloperidol, ambos con valproato (n = 123): sin diferencia en respuesta.'},
 Loxapina:{cat:'agitacion',src:['kwentus','adasuveFT'],note:'ECA frente a placebo en agitación del trastorno bipolar I (inhalada; n = 314). La ficha la autoriza para la agitación, no para la manía.'},
 Droperidol:{cat:'agitacion',src:['khokhar','droperidolFT'],note:'ECA en agitación con diagnósticos mezclados, sin datos propios de manía. La ficha española solo autoriza náuseas y vómitos.'},
 Perfenazina:{cat:'sin-eca',src:['zarate'],note:'Único ECA frente a placebo: continuación tras la remisión, con más recaída depresiva y síntomas extrapiramidales.'},
 Sulpirida:{cat:'sin-eca',src:['christie'],note:'Solo un estudio abierto con 8 pacientes.'},
 Clotiapina:{cat:'sin-eca',src:['carpenter'],note:'La revisión Cochrane de psicosis aguda no incluye placebo ni datos propios de manía.'},
 Levosulpirida:{cat:'sin-eca',src:[],note:V1639_NOECA},
 Tiaprida:{cat:'sin-eca',src:[],note:V1639_NOECA},
 Sertindol:{cat:'sin-eca',src:[],note:V1639_NOECA},
 Flufenazina:{cat:'sin-eca',src:[],note:V1639_NOECA},
 Periciazina:{cat:'sin-eca',src:[],note:V1639_NOECA}
});
const v1639AnchorBase=v1637Anchor;
v1637Anchor=function(drug,dose){const x=v1639AnchorBase(drug,dose);return x.cat==='comparador'?{...x,credit:1}:x};

/* v16.35 · Ampliación de las alertas de interacción (combinaciones de dos o más fármacos).
   Mismos niveles y presentación que v16.34. Fuentes: fichas técnicas CIMA (4.3/4.4/4.5), consulta 12-11-2026. */
Object.assign(V1634_SRC,{
 lurasidona:[V1634_FT(89405),'FT lurasidona 4.3'],cariprazina:[V1634_FT(1171209001),'FT Reagila 4.3'],quetiapina:[V1634_FT(84518),'FT quetiapina 4.5'],aripiprazol:[V1634_FT(80788),'FT aripiprazol 4.5'],
 lamotrigina:[V1634_FT(64462),'FT lamotrigina 4.4/4.5'],valproato:[V1634_FT(68033),'FT ácido valproico 4.5'],oxcarbazepina:[V1634_FT(77722),'FT oxcarbazepina 4.4'],carbamazepina:[V1634_FT(62620),'FT carbamazepina 4.4'],
 oxicodona:[V1634_FT(70687),'FT oxicodona 4.4'],zolpidem:[V1634_FT(65400),'FT zolpidem 4.4'],gabapentina:[V1634_FT(67970),'FT gabapentina 4.4'],pregabalina:[V1634_FT(104279015),'FT Lyrica 4.4'],diazepam:[V1634_FT(80699),'FT diazepam 4.5'],
 metilfenidato:[V1634_FT(86553),'FT metilfenidato 4.3'],amisulprida:[V1634_FT(69796),'FT amisulprida 4.4'],tetrabenazina:[V1634_FT(70142),'FT Nitoman 4.3/4.4'],sertralina:[V1634_FT(59718),'FT Besitran 4.4'],prazosina:[V1634_FT(55064),'FT Minipres 4.4']
});
const V1635_BZD=['Alprazolam','Bromazepam','Brotizolam','Clobazam','Clorazepato dipotásico','Clordiazepóxido','Clonazepam','Diazepam','Flurazepam','Ketazolam','Loprazolam','Lorazepam','Lormetazepam','Midazolam','Triazolam','Clometiazol','Zolpidem','Zopiclona'];
const V1635_GABA=['Gabapentina','Pregabalina'];
const V1635_INDUCERS=['Carbamazepina','Fenitoína','Fenobarbital','Primidona'];
const V1635_STIM=['Metilfenidato','Lisdexanfetamina','Dexanfetamina'];
const V1635_AINE=['Tramadol + dexketoprofeno','Tramadol + celecoxib'];
let V1635_FAM=null;
function v1635Families(){
 if(V1635_FAM)return V1635_FAM;
 const all=Object.keys(DRUGS),rule=t=>all.filter(n=>(DRUGS[n].curated?.rules||[]).includes(t));
 const antipsychotic=[...new Set([...all.filter(n=>{const d=DRUGS[n],t=d.targets?.D2;return /Antipsic/i.test(d.spain?.family||'')&&t&&/antagon|parcial/i.test(String(t[1]))}),'Quetiapina','Zuclopentixol','Pimozida','Tioridazina','Periciazina'])].filter(v1634Has);
 const a1=all.filter(n=>{const t=DRUGS[n].targets?.A1;return t&&/antagon|bloque|adrenol/i.test(String(t[1]))&&!/d[eé]bil|baja|m[ií]nima|probable/i.test(String(t[1]))&&(t[0]||0)>=6});
 V1635_FAM={opioid:[...new Set([...rule('opioid'),'Petidina','Tramadol + paracetamol','Tramadol + dexketoprofeno','Tramadol + celecoxib','Oxicodona + naloxona'])].filter(v1634Has),
  antipsychotic,hypoNa:[...new Set([...rule('hyponatremia'),'Oxcarbazepina','Eslicarbazepina'])].filter(v1634Has),bleeding:rule('bleeding'),metabolic:rule('metabolic'),prolactin:rule('prolactin'),eps:rule('eps'),
  ortho:[...new Set([...a1,'Prazosina','Clonidina','Guanfacina'])].filter(v1634Has)};
 return V1635_FAM;
}
const v1635RulesBase=v1634Rules;
v1634Rules=function(){
 const out=v1635RulesBase();
 const rows=state.rows.filter(r=>v1634Has(r.drug)),names=[...new Set(rows.map(r=>r.drug))],has=n=>names.includes(n),pick=xs=>names.filter(n=>xs.includes(n)),F=v1635Families();
 const add=(level,title,drugs,text,src)=>out.push({level,title,drugs:[...new Set(drugs)],text,src:(src||[]).map(k=>V1634_SRC[k]).filter(Boolean),extra:''});
 // A · Depresión del SNC y respiratoria
 const op=pick(F.opioid),bz=pick(V1635_BZD),gb=pick(V1635_GABA);
 if(op.length&&bz.length)add('mayor','Opioide + benzodiacepina o hipnótico Z',[...op,...bz],'Riesgo de sedación profunda, depresión respiratoria, coma y muerte. Las fichas reservan la asociación a pacientes sin alternativa, con la dosis y la duración mínimas y vigilancia de la respiración.',['oxicodona','zolpidem']);
 if(op.length&&gb.length)add('mayor','Opioide + gabapentinoide',[...op,...gb],'Vigilar depresión del SNC y respiratoria; con pregabalina, además, estreñimiento o íleo.',['gabapentina','pregabalina']);
 if(has('Clozapina')&&bz.length)add('mayor','Clozapina + benzodiacepina',['Clozapina',...bz],'La ficha de clozapina pide especial precaución al iniciarla en pacientes con benzodiacepinas: mayor riesgo de colapso circulatorio, que raramente puede llevar a paro cardíaco o respiratorio.',['clozapina']);
 if(bz.length>=2)add('vigilar','Duplicidad de benzodiacepinas o hipnóticos Z',bz,'Sedación, deterioro psicomotor y caídas aditivos; revisar si la duplicidad es intencionada.',['diazepam']);
 if(bz.length&&gb.length&&!op.length)add('vigilar','Benzodiacepina/Z + gabapentinoide',[...bz,...gb],'Depresión del SNC aditiva: vigilar sedación y respiración.',['gabapentina']);
 // B · Eutimizantes y antiepilépticos
 if(has('Valproato')&&has('Lamotrigina'))add('mayor','Valproato + lamotrigina',['Valproato','Lamotrigina'],'El valproato inhibe la glucuronidación de la lamotrigina y casi duplica su semivida; el uso concomitante se asocia a mayor riesgo de exantema grave. Usar el escalado específico con valproato (ficha 4.2).',['lamotrigina']);
 if(has('Valproato')&&has('Topiramato'))add('mayor','Valproato + topiramato',['Valproato','Topiramato'],'Asociado a encefalopatía y/o hiperamonemia: vigilar signos de encefalopatía hiperamoniémica.',['valproato']);
 if(has('Valproato')&&has('Carbamazepina'))add('mayor','Valproato + carbamazepina',['Valproato','Carbamazepina'],'Toxicidad clínica descrita: el valproato puede aumentar la carbamazepina y su epóxido activo. Vigilar niveles y clínica.',['valproato']);
 const ap=pick(F.antipsychotic);if(has('Litio')&&ap.length)add('mayor','Litio + antipsicótico',['Litio',...ap],'La ficha española del litio (Plenur) no recomienda la asociación con antipsicóticos típicos y atípicos y pide vigilar reacciones adversas neurológicas (neurotoxicidad). Si se asocia, control clínico y de litemia.',['litio']);
 const aine=pick(V1635_AINE);if(has('Litio')&&aine.length)add('mayor','Litio + AINE',['Litio',...aine],'Los AINE, incluidos los inhibidores de la COX-2, pueden elevar la litemia: controlar niveles.',['litio']);
 // C · Inductores enzimáticos
 const ind=pick(V1635_INDUCERS);
 if(ind.length){
  if(has('Lurasidona'))add('contra','Inductor potente de CYP3A4 + lurasidona',[...ind,'Lurasidona'],'Contraindicado en la ficha de lurasidona (carbamazepina, fenobarbital, fenitoína…).',['lurasidona']);
  if(has('Cariprazina'))add('contra','Inductor de CYP3A4 + cariprazina',[...ind,'Cariprazina'],'La ficha de Reagila contraindica la administración con inductores potentes o moderados de CYP3A4.',['cariprazina']);
  if(has('Quetiapina'))add('mayor','Inductor + quetiapina',[...ind,'Quetiapina'],'La carbamazepina aumenta significativamente el aclaramiento de quetiapina y reduce su exposición: posible pérdida de eficacia.',['quetiapina']);
  if(has('Aripiprazol'))add('mayor','Inductor + aripiprazol',[...ind,'Aripiprazol'],'La carbamazepina reduce la exposición a aripiprazol; la ficha indica ajustar (aumentar) la dosis y revertir al retirar el inductor.',['aripiprazol']);
  if(has('Lamotrigina'))add('mayor','Inductor + lamotrigina',[...ind,'Lamotrigina'],'Fenitoína, carbamazepina, fenobarbital y primidona inducen la glucuronidación y reducen la lamotrigina: usar la pauta para inductores (ficha 4.2).',['lamotrigina']);
 }
 // D · IMAO con estimulantes, bupropión y tetrabenazina
 const maoAny=pick([...V1634_MAOI_NS,...V1634_MAOB]);
 const st=pick(V1635_STIM);if(st.length&&pick(['Tranilcipromina']).length)add('contra','IMAO irreversible + estimulante',['Tranilcipromina',...st],'Contraindicado durante el tratamiento con IMAO irreversibles no selectivos y en los 14 días siguientes, por riesgo de crisis hipertensiva.',['metilfenidato']);
 if(has('Bupropión')&&maoAny.length)add('contra','Bupropión + IMAO',['Bupropión',...maoAny],'Contraindicado en la ficha de bupropión: al menos 14 días tras un IMAO irreversible.',['bupropion']);
 if(has('Tetrabenazina')){
  if(maoAny.length)add('contra','Tetrabenazina + IMAO',['Tetrabenazina',...maoAny],'No debe administrarse en las dos semanas posteriores a un IMAO (crisis hipertensiva).',['tetrabenazina']);
  if(ap.length)add('mayor','Tetrabenazina + antipsicótico',['Tetrabenazina',...ap],'Pueden exagerarse la prolongación del QTc, el síndrome neuroléptico maligno y los trastornos extrapiramidales.',['tetrabenazina']);
 }
 // E · Hiponatremia y sangrado
 const na=pick(F.hypoNa);if(na.length>=2)add('vigilar','Hiponatremia · '+na.length+' fármacos',na,'ISRS/IRSN (SIADH) y carbamazepina/oxcarbazepina pueden bajar el sodio; el riesgo aumenta en mayores, con diuréticos o depleción de volumen. Controlar natremia.',['sertralina','carbamazepina','oxcarbazepina']);
 const bl=pick(F.bleeding),blx=pick([...V1635_AINE,'Valproato']);if(bl.length&&blx.length)add('mayor','Riesgo de sangrado',[...bl,...blx],'Los ISRS/IRSN aumentan el riesgo de hemorragia, sobre todo con AINE o fármacos que alteran la función plaquetaria (valproato: trombocitopenia).',['sertralina']);
 // F · Cargas de efectos de clase
 const met=pick(F.metabolic);if(met.length>=2)add('vigilar','Riesgo metabólico · '+met.length+' fármacos',met,'Peso, glucemia y lípidos: control basal y periódico (la ficha de olanzapina describe hiperglucemia, diabetes y cetoacidosis ocasional).',['olanzapina']);
 const pr=pick(F.prolactin);if(pr.length>=2)add('vigilar','Hiperprolactinemia · '+pr.length+' fármacos',pr,'Efecto aditivo sobre la prolactina: síntomas sexuales, galactorrea, amenorrea y densidad ósea a largo plazo.',['amisulprida']);
 const ep=pick(F.eps);if(ep.length>=2)add('vigilar','Síntomas extrapiramidales · '+ep.length+' fármacos',ep,'Bloqueo D2 aditivo: acatisia, parkinsonismo, distonía y discinesia tardía; vigilar también síndrome neuroléptico maligno.',['tetrabenazina']);
 const or=pick(F.ortho);if(or.length>=2)add('vigilar','Hipotensión ortostática · '+or.length+' fármacos',or,'Bloqueo α1 y agonismo α2 aditivos: mareo y caídas, sobre todo al inicio y en mayores (la ficha de prazosina describe hipotensión ortostática de primera dosis).',['prazosina']);
 // Evitar duplicados: una contraindicación pareja a pareja heredada se retira si otra regla la cubre con su ficha
 const pairOnly=o=>o.level==='contra'&&o.src.length===1&&o.src[0][1]==='Ficha técnica'&&o.drugs.length===2;
 const dedup=out.filter(o=>!(pairOnly(o)&&out.some(x=>x!==o&&!pairOnly(x)&&x.level==='contra'&&o.drugs.every(d=>x.drugs.includes(d)))));
 const order={contra:0,mayor:1,vigilar:2};return dedup.sort((a,b)=>order[a.level]-order[b.level]);
};
V1634_FAM=null;

/* v16.34 · Alertas de interacción por familia, siempre visibles bajo la pauta.
   Tres niveles: contraindicación · precaución mayor · vigilancia. Cada regla cita el apartado de ficha técnica
   (CIMA, consulta 12-11-2026) o la fuente bibliográfica que la sostiene. Avisos por presencia en la pauta:
   no calculan exposición, lavado ni dosis compensatoria. Las familias se construyen con los datos del atlas. */
const V1634_FT=n=>'https://cima.aemps.es/cima/dochtml/ft/'+n+'/FT_'+n+'.html';
const V1634_SRC={
 fluvoxamina:[V1634_FT(63277),'FT fluvoxamina 4.3/4.5'],duloxetina:[V1634_FT(88002),'FT duloxetina 4.3/4.5'],agomelatina:[V1634_FT(83546),'FT agomelatina 4.3/4.5'],
 olanzapina:[V1634_FT(85116),'FT olanzapina 4.5'],clomipramina:[V1634_FT(49656),'FT Anafranil 4.5'],citalopram:[V1634_FT(66483),'FT citalopram 4.3'],escitalopram:[V1634_FT(71430),'FT escitalopram 4.3'],
 bupropion:[V1634_FT(81595),'FT bupropión 4.3/4.4/4.5'],rasagilina:[V1634_FT(80951),'FT rasagilina 4.3/4.4/4.5'],safinamida:[V1634_FT(114984008),'FT Xadago 4.3/4.4'],selegilina:[V1634_FT(58113),'FT Plurimen 4.3/4.5'],
 clozapina:[V1634_FT(88019),'FT clozapina 4.4/4.5'],litio:[V1634_FT(48932),'FT Plenur 4.4'],tramadol:[V1634_FT(61784),'FT Adolonta 4.4'],fluoxetina:[V1634_FT(63499),'FT fluoxetina 4.5'],paroxetina:[V1634_FT(59466),'FT Frosinor 4.5'],
 ondansetron:[V1634_FT(69378),'FT ondansetrón 4.4'],metadona:[V1634_FT(69909),'FT Eptadone 4.4'],
 chiew:['https://doi.org/10.1111/bcp.16152','Chiew e Isbister, Br J Clin Pharmacol 2025;91:654-61'],king:['https://doi.org/10.1111/1742-6723.14554','King y Rotella, Emerg Med Australas 2025;37:e14554'],
 claessens:['https://doi.org/10.1124/dmd.110.033878','Claessens et al., Drug Metab Dispos 2010;38:1393-6']
};
const V1634_MAOI_NS=['Tranilcipromina','Moclobemida'],V1634_MAOB=['Selegilina','Rasagilina','Safinamida'];
const V1634_SER_EXTRA=['Litio','Fentanilo','Petidina','Vilazodona','Tranilcipromina','Moclobemida','Selegilina','Rasagilina','Safinamida'];
const V1634_ANTICHOL_EXTRA=['Biperideno','Prociclidina','Trihexifenidilo','Difenhidramina','Hidroxizina','Ciproheptadina','Tioridazina','Imipramina','Doxepina','Trimipramina','Maprotilina'];
/* QT: además de la marca del atlas, fichas CIMA que advierten de prolongación de QT (4.4/4.5). Alto riesgo: QT en 4.3 de su ficha o advertencia de torsades. */
const V1634_QT_EXTRA=['Quetiapina','Olanzapina','Clozapina','Paroxetina','Ondansetrón','Hidroxizina'];
const V1634_QT_HIGH=['Citalopram','Escitalopram','Clomipramina','Haloperidol','Hidroxizina','Pimozida','Ziprasidona','Sertindol','Tioridazina','Metadona','Quinidina'];
const V1634_1A2_SUBSTRATES=['Clozapina','Olanzapina','Quetiapina','Clomipramina','Imipramina','Amitriptilina','Propranolol','Ropinirol'];
function v1634Has(n){return Object.prototype.hasOwnProperty.call(DRUGS,n)}
let V1634_FAM=null;
function v1634Families(){
 if(V1634_FAM)return V1634_FAM;
 const all=Object.keys(DRUGS),rule=t=>all.filter(n=>(DRUGS[n].curated?.rules||[]).includes(t));
 const sert=all.filter(n=>{const t=DRUGS[n].targets?.SERT;return t&&/inhib|recapt/i.test(String(t[1]))&&!/d[eé]bil|baja|m[ií]nima|uni[oó]n/i.test(String(t[1]))});
 const mAnt=all.filter(n=>{const t=DRUGS[n].targets||{};return ['M1','M3','MACH'].some(k=>t[k]&&/antagon/i.test(String(t[k][1]))&&!/d[eé]bil|baja|m[ií]nima|probable/i.test(String(t[k][1]))&&(t[k][0]||0)>=6)});
 V1634_FAM={ser:[...new Set([...rule('serotonergic'),...sert,...V1634_SER_EXTRA])].filter(v1634Has),qt:[...new Set([...rule('qt'),...V1634_QT_EXTRA])].filter(v1634Has),seizure:rule('seizure'),
  antichol:[...new Set([...mAnt,...V1634_ANTICHOL_EXTRA])].filter(v1634Has),cyp2d6:rule('cyp2d6'),cyp3a4:rule('cyp3a4')};
 return V1634_FAM;
}
const V1634_SS_MANAGEMENT='Manejo descrito en la bibliografía: retirar los agentes serotoninérgicos, medidas de soporte y benzodiacepinas para agitación, temblor o rigidez; en casos graves, soporte intensivo con control de la hipertermia. En casos moderados o graves se han usado antagonistas 5-HT2A (ciproheptadina; también clorpromazina u olanzapina), con evidencia procedente de casos y series y sin eficacia demostrada. La ciproheptadina tiene en el atlas antagonismo H1, 5-HT2A y muscarínico (ficha CIMA); su antagonismo 5-HT1A no está documentado en el atlas.';
function v1634Rules(){
 const rows=state.rows.filter(r=>v1634Has(r.drug)),names=[...new Set(rows.map(r=>r.drug))],has=n=>names.includes(n),pick=xs=>names.filter(n=>xs.includes(n));
 const F=v1634Families(),out=[],add=(level,title,drugs,text,src,extra)=>out.push({level,title,drugs:[...new Set(drugs)],text,src:(src||[]).map(k=>V1634_SRC[k]).filter(Boolean),extra:extra||''});
 // 1 · Síndrome serotoninérgico
 const ser=pick(F.ser),ns=pick(V1634_MAOI_NS),others=ser.filter(n=>!V1634_MAOI_NS.includes(n)&&!V1634_MAOB.includes(n));
 if(ns.length&&ser.filter(n=>!ns.includes(n)).length||ns.length>1)add('contra','IMAO no selectivo + serotoninérgico',[...ns,...ser.filter(n=>!ns.includes(n))],'Combinación contraindicada en las fichas de los ISRS/IRSN e IMAO por riesgo de síndrome serotoninérgico. Respetar los intervalos de cambio de cada ficha (p. ej., 2 semanas tras un IMAO irreversible; 1 semana tras fluvoxamina; 5 semanas tras fluoxetina).',['fluvoxamina','duloxetina','citalopram'],V1634_SS_MANAGEMENT);
 if(has('Selegilina')){const x=pick(F.ser).filter(n=>n!=='Selegilina'&&!['Litio'].includes(n));if(x.length)add('contra','Selegilina + ISRS/IRSN/tricíclicos/opioides',['Selegilina',...x],'La ficha de Plurimen indica que selegilina no debe usarse con ISRS, IRSN, tricíclicos, simpaticomiméticos, otros IMAO ni opioides como petidina; evitarla durante las 5 semanas siguientes a fluoxetina.',['selegilina'],V1634_SS_MANAGEMENT)}
 for(const b of ['Rasagilina','Safinamida'])if(has(b)){
  const src=b==='Rasagilina'?'rasagilina':'safinamida',imao=pick([...V1634_MAOI_NS,...V1634_MAOB,'Petidina']).filter(n=>n!==b);
  if(imao.length)add('contra',b+' + otro IMAO o petidina',[b,...imao],'Contraindicado en la ficha (4.3).',[src]);
  const ff=pick(['Fluoxetina','Fluvoxamina']);if(ff.length)add('mayor',b+' + fluoxetina/fluvoxamina',[b,...ff],'La ficha indica que debe evitarse la asociación (fluoxetina: 5 semanas de separación antes de iniciar '+b.toLowerCase()+').',[src],V1634_SS_MANAGEMENT);
  if(b==='Rasagilina'&&has('Dextrometorfano'))add('mayor','Rasagilina + dextrometorfano',[b,'Dextrometorfano'],'Administración concomitante desaconsejada en la ficha.',[src]);
  const ad=others.filter(n=>!ff.includes(n)&&n!=='Dextrometorfano'&&n!=='Petidina');if(ad.length)add('vigilar',b+' + antidepresivos serotoninérgicos',[b,...ad],b==='Rasagilina'?'La ficha pide precaución con ISRS, IRSN y antidepresivos tricíclicos/tetracíclicos.':'La ficha permite ISRS a la menor dosis eficaz, con precaución por síntomas serotoninérgicos.',[src],V1634_SS_MANAGEMENT);
 }
 if(!ns.length&&others.length>=2)add('vigilar','Carga serotoninérgica · '+others.length+' agentes',others,'Riesgo de síndrome serotoninérgico al combinar agentes serotoninérgicos (ISRS, IRSN, tricíclicos, tramadol, buprenorfina, litio, triptanes…), descrito en las fichas como potencialmente mortal. Vigilar al iniciar o subir dosis.',['fluvoxamina','litio','tramadol'],V1634_SS_MANAGEMENT);
 // 2 · QT
 const qt=pick(F.qt);
 for(const c of ['Citalopram','Escitalopram'])if(has(c)&&qt.filter(n=>n!==c).length)add('contra',c+' + otro fármaco que prolonga QT',[c,...qt.filter(n=>n!==c)],'La ficha contraindica su uso con medicamentos que prolongan el intervalo QT.',[c==='Citalopram'?'citalopram':'escitalopram']);
 if(qt.length>=2&&!['Citalopram','Escitalopram'].some(has)){const high=qt.filter(n=>V1634_QT_HIGH.includes(n));add(high.length?'mayor':'vigilar','Prolongación de QT · '+qt.length+' fármacos',qt,(high.length?'Incluye fármaco(s) con QT en contraindicaciones o con advertencia de torsades en su ficha ('+high.join(', ')+'). ':'')+'Efecto aditivo sobre el QT: ECG basal y de control; corregir potasio y magnesio; evitar en QT largo congénito.',['ondansetron','metadona'])}
 // 3 · Umbral convulsivo
 const sz=pick([...F.seizure,'Bupropión']);
 if(has('Bupropión')&&sz.filter(n=>n!=='Bupropión').length)add('mayor','Bupropión + fármacos que reducen el umbral convulsivo',sz,'La ficha pide precaución con medicamentos que bajan el umbral convulsivo (antipsicóticos, antidepresivos, tramadol, teofilina…); la incidencia de convulsiones es dosis-dependiente.',['bupropion']);
 else if(sz.length>=2)add('vigilar','Umbral convulsivo · '+sz.length+' fármacos',sz,'Varios fármacos con advertencia de convulsiones en ficha: vigilar dosis y factores de riesgo.',['tramadol','bupropion']);
 // 4 · Carga anticolinérgica
 const ac=pick(F.antichol);
 if(ac.length>=2)add(has('Clozapina')?'mayor':'vigilar','Carga anticolinérgica · '+ac.length+' fármacos',ac,'Suma de antagonismo muscarínico: xerostomía, estreñimiento/íleo, retención urinaria, visión borrosa y delirium, sobre todo en mayores.'+(has('Clozapina')?' Con clozapina, mayor riesgo de hipomotilidad intestinal grave (actividad anticolinérgica descrita en su ficha).':''),['clozapina']);
 // 5 · Agranulocitosis
 if(has('Clozapina')&&has('Carbamazepina'))add('contra','Clozapina + carbamazepina',['Clozapina','Carbamazepina'],'La ficha de clozapina indica que carbamazepina no debe utilizarse concomitantemente por su potencial mielosupresor (además, es inductor enzimático).',['clozapina']);
 // 6 · Fluvoxamina · CYP1A2
 if(has('Fluvoxamina')){
  if(has('Duloxetina'))add('contra','Fluvoxamina + duloxetina',['Fluvoxamina','Duloxetina'],'Contraindicado en la ficha de duloxetina: la fluvoxamina (inhibidor potente de CYP1A2) aumenta unas 6 veces la exposición a duloxetina.',['duloxetina']);
  if(has('Agomelatina'))add('contra','Fluvoxamina + agomelatina',['Fluvoxamina','Agomelatina'],'Contraindicado en la ficha de agomelatina: exposición unas 60 veces mayor (rango 12-412).',['agomelatina']);
  const s=pick(V1634_1A2_SUBSTRATES);if(s.length)add('mayor','Fluvoxamina · inhibición de CYP1A2',['Fluvoxamina',...s],'La ficha describe aumento de niveles de tricíclicos (clomipramina, imipramina, amitriptilina), neurolépticos (clozapina, olanzapina, quetiapina), propranolol y ropinirol: vigilar y reducir dosis si es necesario.',['fluvoxamina','olanzapina','clomipramina']);
  if(has('Clonidina'))add('vigilar','Fluvoxamina + clonidina',['Fluvoxamina','Clonidina'],'Interacción de relevancia probablemente baja: CYP1A2 es una vía menor de la clonidina (CYP2D6 ≈ 2/3 de su 4-hidroxilación in vitro). No figura en la ficha de fluvoxamina consultada.',['claessens']);
  add('vigilar','Fluvoxamina · xantinas',['Fluvoxamina'],'Aumenta los niveles de cafeína (reducir su consumo si aparece temblor, palpitaciones, náuseas, inquietud o insomnio) y de teofilina (estrecho margen terapéutico: monitorizar). Ninguna de las dos está en el catálogo del atlas.',['fluvoxamina']);
 }
 // 7 · Inhibidores potentes de CYP2D6
 const inh=pick(['Fluoxetina','Paroxetina','Bupropión']),sub=pick(F.cyp2d6).filter(n=>!inh.includes(n));
 if(inh.length&&sub.length)add('mayor','Inhibición potente de CYP2D6',[...inh,...sub],inh.join(', ')+' inhibe(n) CYP2D6 de forma potente: puede aumentar la exposición a los sustratos de la pauta (y reducir la activación de profármacos como tramadol o codeína). Revisar ajuste de dosis en la ficha de cada sustrato.',inh.map(n=>({Fluoxetina:'fluoxetina',Paroxetina:'paroxetina','Bupropión':'bupropion'})[n]));
 // 8 · Contraindicaciones pareja a pareja ya existentes (tranilcipromina, moclobemida, pimozida)
 try{for(const r of v1613Safety())if(r.severity==='contraindicated'&&!out.some(o=>o.level==='contra'&&o.drugs.includes(r.a)&&o.drugs.includes(r.b)))out.push({level:'contra',title:r.a+' + '+r.b,drugs:[r.a,r.b],text:r.text,src:[[r.source,'Ficha técnica']],extra:''})}catch(e){}
 const order={contra:0,mayor:1,vigilar:2};return out.sort((a,b)=>order[a.level]-order[b.level]);
}
const V1634_LEVEL={contra:['⛔','Contraindicación'],mayor:['⚠','Precaución mayor'],vigilar:['◇','Vigilancia']};
function v1634Render(){
 const aside=document.querySelector('.explore-aside');if(!aside)return;
 let box=document.getElementById('v1634-alerts');
 if(!box){box=document.createElement('section');box.id='v1634-alerts';box.className='v1634-alerts';box.setAttribute('aria-label','Alertas de interacción');const anchor=aside.querySelector('.actions');(anchor||aside.lastElementChild).after(box)}
 let rules=[];try{rules=v1634Rules()}catch(e){rules=[]}
 const sig=JSON.stringify(rules.map(r=>[r.level,r.title,r.drugs]));if(box.dataset.sig===sig)return;box.dataset.sig=sig;
 if(!rules.length){box.innerHTML='<h3>Alertas de interacción</h3><p class="v1634-none">Sin alertas por familia para esta pauta. No sustituye la revisión de las fichas.</p>';return}
 const n=l=>rules.filter(r=>r.level===l).length;
 box.innerHTML='<h3>Alertas de interacción <small>'+['contra','mayor','vigilar'].filter(n).map(l=>V1634_LEVEL[l][0]+' '+n(l)).join(' · ')+'</small></h3>'
  +rules.map(r=>'<details class="v1634-item v1634-'+r.level+'"'+(r.level==='contra'?' open':'')+'><summary><span class="v1634-badge">'+V1634_LEVEL[r.level][0]+' '+V1634_LEVEL[r.level][1]+'</span> '+esc(r.title)+'</summary>'
   +'<p class="v1634-drugs">'+esc(r.drugs.join(' · '))+'</p><p>'+esc(r.text)+'</p>'+(r.extra?'<p class="v1634-extra">'+esc(r.extra)+(r.extra===V1634_SS_MANAGEMENT?' <a href="'+V1634_SRC.chiew[0]+'" target="_blank" rel="noopener noreferrer">'+esc(V1634_SRC.chiew[1])+'</a> · <a href="'+V1634_SRC.king[0]+'" target="_blank" rel="noopener noreferrer">'+esc(V1634_SRC.king[1])+'</a>':'')+'</p>':'')
   +'<p class="v1634-src">'+r.src.map(([u,l])=>'<a href="'+esc(u)+'" target="_blank" rel="noopener noreferrer">'+esc(l)+'</a>').join(' · ')+'</p></details>').join('')
  +'<p class="v1634-foot">Avisos por presencia en la pauta; no calculan exposición ni sustituyen la ficha técnica.</p>';
}
const v1634EvaluateBase=evaluate;
evaluate=function(...args){const r=v1634EvaluateBase.apply(this,args);try{v1634Render()}catch(e){}return r};
setTimeout(()=>{try{v1634Render()}catch(e){}},0);

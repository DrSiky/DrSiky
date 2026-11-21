/* v16.41 · Componente antidepresivo con ancla clínica, con el mismo esquema que el antimaníaco.
   Decisiones del usuario: (1c) el ancla depende de la lente: depresión bipolar en la lente bipolar, unipolar en las demás;
   (2b) la eficacia solo como coadyuvante se acredita siempre, con etiqueta; (3) el término clínico de los eficaces sin
   magnitud en el vector se escala por el tamaño de efecto de los metaanálisis.
   Escala común: diferencia de medias estandarizada (DME); las razones de probabilidades se convierten con ln(OR)/1,81 (Chinn 2000).
   Referencia máxima: amitriptilina, OR 2,13 (Cipriani 2018) → DME 0,418. Peso del término clínico: 0,24 (el mayor peso monoaminérgico). */
const V1641_K=1.81,v1641OR=o=>Math.log(o)/V1641_K,V1641_ES_MAX=v1641OR(2.13),V1641_ES_MIN=v1641OR(1.37),V1641_W=.24;
const v1641FT=n=>'https://cima.aemps.es/cima/dochtml/ft/'+n+'/FT_'+n+'.html';
Object.assign(V1637_SRC,{
 cipriani18:['Cipriani 2018 (Lancet)','https://doi.org/10.1016/S0140-6736(17)32802-7'],
 yildiz:['Yildiz 2023','https://doi.org/10.1016/S2215-0366(23)00199-2'],
 kadakia:['Kadakia 2021','https://doi.org/10.1186/s12888-021-03220-3'],
 vazquez:['Vázquez 2015','https://doi.org/10.1016/j.jad.2015.05.016'],
 yan:['Yan 2022','https://doi.org/10.1017/S0033291722001246'],
 nunez:['Nuñez 2022','https://doi.org/10.1016/j.jad.2021.12.134'],
 wang23:['Wang 2023','https://doi.org/10.1097/MD.0000000000034670'],
 ricken:['Ricken 2017','https://doi.org/10.1016/j.euroneuro.2017.04.003'],
 lotufo:['Lotufo-Neto 1999','https://doi.org/10.1016/S0893-133X(98)00075-X'],
 naudet:['Naudet 2025','https://doi.org/10.1186/s12916-025-04435-x'],
 suppes:['Suppes 2016','https://doi.org/10.1176/appi.ajp.2015.15060770'],
 brown:['Brown 2019','https://doi.org/10.1016/j.jad.2019.02.056'],
 chinn:['Chinn 2000','https://doi.org/10.1002/1097-0258(20001130)19:22<3127::aid-sim784>3.0.co;2-m'],
 ftImi:['FT Tofranil 4.1',v1641FT(31004)],ftNor:['FT nortriptilina 4.1',v1641FT(48462)],ftDox:['FT Sinequan 4.1',v1641FT(49028)],
 ftTri:['FT Surmontil 4.1',v1641FT(40115)],ftMia:['FT Lantanon 4.1',v1641FT(54407)],ftMoc:['FT Manerix 4.1',v1641FT(59169)],
 ftTia:['FT tianeptina 4.1',v1641FT(78980)],ftEsk:['FT Spravato 4.1',v1641FT(1191410001)],ftQue:['FT quetiapina LP 4.1',v1641FT(84518)],
 ftLit:['FT Plenur 4.1',v1641FT(48932)],ftLam:['FT lamotrigina 4.1',v1641FT(64462)]
});
const V1641_CAT={
 demostrada:'eficacia antidepresiva demostrada',
 ficha:'indicación en ficha técnica española · se acredita',
 coadyuvante:'eficacia solo como coadyuvante de un antidepresivo · se acredita',
 negativa:'estudiada y negativa · no se acredita',
 clase:'antidepresivos en depresión bipolar: eficaces como clase con confianza baja y más viraje · no se acredita',
 insuficiente:'evidencia insuficiente · no se acredita',
 'sin-ancla':'sin ancla localizada en esta indicación · no se acredita',
 'sin-revisar':'sin ancla revisada'
};
const V1641_CREDIT={demostrada:1,ficha:1,coadyuvante:1,'sin-revisar':1};
const v1641N=x=>String(x).replace('.',',');
const v1641C=or=>({cat:'demostrada',es:v1641OR(or),eff:'OR '+v1641N(or.toFixed(2))+' frente a placebo',src:['cipriani18']});
const v1641F=k=>({cat:'ficha',src:[k],note:'No incluido en Cipriani 2018; ancla por indicación autorizada en depresión.'});
/* Depresión unipolar (lentes no bipolares) */
const V1641_UNI={
 Amitriptilina:v1641C(2.13),Mirtazapina:v1641C(1.89),Duloxetina:v1641C(1.85),Venlafaxina:v1641C(1.78),Paroxetina:v1641C(1.75),Fluvoxamina:v1641C(1.69),
 Escitalopram:v1641C(1.68),Sertralina:v1641C(1.67),Vortioxetina:v1641C(1.66),Agomelatina:v1641C(1.65),Vilazodona:v1641C(1.60),Levomilnacipran:v1641C(1.59),
 'Bupropión':v1641C(1.58),Fluoxetina:v1641C(1.52),Citalopram:v1641C(1.52),Trazodona:v1641C(1.51),Clomipramina:v1641C(1.49),Desvenlafaxina:v1641C(1.49),Reboxetina:v1641C(1.37),
 Tranilcipromina:{cat:'demostrada',es:.509/V1641_K,eff:'log OR 0,509 frente a placebo (4 estudios)',src:['ricken'],note:'Sin presentación comercializada en España.'},
 Moclobemida:{cat:'demostrada',src:['lotufo','ftMoc'],note:'Metaanálisis: superior a placebo; el resumen no da la cifra agrupada.'},
 Imipramina:v1641F('ftImi'),Nortriptilina:v1641F('ftNor'),Doxepina:v1641F('ftDox'),Trimipramina:v1641F('ftTri'),Mianserina:v1641F('ftMia'),Tianeptina:v1641F('ftTia'),
 Esketamina:{cat:'coadyuvante',src:['naudet','ftEsk'],eff:'−2,94 puntos MADRS a 4 semanas',note:'Indicada en combinación con un ISRS o IRSN. El metaanálisis de datos individuales califica la ventaja de pequeña y de relevancia clínica incierta.'},
 Desipramina:{cat:'sin-ancla',note:'Sin presentación comercializada en España ni metaanálisis frente a placebo localizado en depresión mayor no complicada (PubMed, nov. 2026).'},
 Maprotilina:{cat:'sin-ancla',note:'Sin presentación comercializada en España ni metaanálisis frente a placebo localizado (PubMed, nov. 2026).'},
 Aripiprazol:{cat:'coadyuvante',es:.28,eff:'DME 0,28 como coadyuvante',src:['wang23','yan']},
 Brexpiprazol:{cat:'coadyuvante',es:.25,eff:'DME 0,25 como coadyuvante',src:['wang23','yan']},
 Cariprazina:{cat:'coadyuvante',es:v1641OR(1.34),eff:'OR 1,34 de respuesta como coadyuvante',src:['yan'],note:'No fue eficaz en remisión.'},
 Quetiapina:{cat:'coadyuvante',es:.40,eff:'DME 0,40 como coadyuvante',src:['wang23','ftQue']},
 Olanzapina:{cat:'coadyuvante',es:.35,eff:'DME 0,35 como coadyuvante',src:['wang23','yan']},
 Risperidona:{cat:'coadyuvante',es:v1641OR(2.17),eff:'OR 2,17 de respuesta como coadyuvante',src:['yan']},
 Litio:{cat:'coadyuvante',src:['nunez','ftLit'],note:'Tratamiento adicional en la depresión mayor resistente.'},
 Modafinilo:{cat:'coadyuvante',src:['nunez'],note:'Respuesta superior a placebo como coadyuvante en depresión resistente.'},
 Lisdexanfetamina:{cat:'coadyuvante',src:['nunez'],note:'Respuesta superior a placebo como coadyuvante en depresión resistente.'},
 Lurasidona:{cat:'demostrada',es:.80,eff:'tamaño de efecto 0,80 (un ECA)',src:['suppes'],note:'Un único ECA, en depresión mayor con rasgos mixtos.'},
 Ziprasidona:{cat:'negativa',src:['yan'],note:'Único antipsicótico de segunda generación que no superó a placebo como coadyuvante.'}
};
/* Depresión bipolar (lente bipolar) */
const V1641_MID=(.16+.41)/2;
const V1641_BIP={
 Quetiapina:{cat:'demostrada',es:V1641_MID,eff:'−4,80 puntos MADRS (Kadakia 2021)',src:['yildiz','kadakia','ftQue'],midpoint:true},
 Olanzapina:{cat:'demostrada',es:V1641_MID,eff:'−4,57 puntos MADRS (Kadakia 2021)',src:['yildiz','kadakia'],midpoint:true},
 Lurasidona:{cat:'demostrada',eff:'−4,71 puntos MADRS (Kadakia 2021)',src:['yildiz','kadakia'],note:'En España la ficha solo autoriza esquizofrenia.'},
 Cariprazina:{cat:'demostrada',eff:'−2,29 puntos MADRS (Kadakia 2021)',src:['yildiz','kadakia'],note:'En España la ficha solo autoriza esquizofrenia.'},
 Lamotrigina:{cat:'demostrada',es:.16,eff:'DME 0,16',src:['yildiz','ftLam'],note:'La ficha española la autoriza para prevenir episodios depresivos, no para el tratamiento agudo.'},
 Aripiprazol:{cat:'negativa',src:['vazquez','kadakia'],note:'Ineficaz en depresión bipolar.'},
 Ziprasidona:{cat:'negativa',src:['vazquez','kadakia'],note:'Ineficaz en depresión bipolar.'},
 Brexpiprazol:{cat:'sin-ancla',src:['brown'],note:'Solo un estudio piloto abierto con 21 pacientes.'},
 Litio:{cat:'insuficiente',src:['vazquez'],note:'Poco eficaz en el único ensayo frente a placebo recogido.'}
};
const V1641_T6=['NET','SERT','HT1A','D3','DAT','MAOA'];
function v1641Basis(){return state.lens==='bipolar'?'bip':'uni'}
function v1641Anchor(drug,basis,names){
 const fam=/Antidepresivos/i.test(DRUGS[drug]?.spain?.family||'');
 let x=(basis==='bip'?V1641_BIP:V1641_UNI)[drug];
 if(!x)x=fam?(basis==='bip'?{cat:'clase',src:['yildiz']}:{cat:'sin-ancla',note:'Sin ancla localizada.'}):{cat:'sin-revisar'};
 x={src:[],note:'',eff:'',...x};
 if(x.midpoint)x.note=(x.note?x.note+' ':'')+'Yildiz 2023 la sitúa entre las eficaces con confianza moderada, pero su resumen no da la DME por fármaco: se usa el punto medio del intervalo publicado (0,16–0,41).';
 if(basis==='bip'&&names&&names.has('Olanzapina')&&names.has('Fluoxetina')){
  if(drug==='Olanzapina')x={...x,es:.41,eff:'DME 0,41 (olanzapina + fluoxetina)',note:'Combinación olanzapina + fluoxetina: la de mayor efecto en Yildiz 2023.'};
  if(drug==='Fluoxetina')x={...x,note:'En combinación con olanzapina: el crédito lo lleva el término clínico de la combinación.'};
 }
 x.credit=V1641_CREDIT[x.cat]||0;
 if(x.es==null&&x.credit&&x.cat!=='sin-revisar'){x.es=V1641_ES_MIN;x.esFloor=true}
 return x;
}
function v1641G(x,t){const cs=(x[t]?.contrib||[]).filter(c=>c.operationalEligible!==false);return cs.length?1-cs.reduce((p,c)=>p*(1-Math.min(.98,(c.value||0)/10)),1):0}
function v1641Sub(a,keep){const o={};V1641_T6.forEach(t=>{o[t]={contrib:(a[t]?.contrib||[]).filter(c=>keep(c.drug))}});return o}
function v1641Sig(x){return [['NET',.24,v1641G(x,'NET')],['SERT',.14,v1641G(x,'SERT')],['5-HT1A agonismo',.23,actionSignal(x,'HT1A',V1637_AGON)],['D3 agonismo',.16,actionSignal(x,'D3',V1637_AGON)],['DAT',.10,v1641G(x,'DAT')],['MAO-A',.13,v1641G(x,'MAOA')]].map(s=>({label:s[0],v:s[1]*s[2]}))}
function v1641Model(a){
 const basis=v1641Basis(),doses=v1637Doses(a),names=new Set(doses.keys());
 V1641_T6.forEach(t=>(a[t]?.contrib||[]).forEach(c=>{if(c.drug)names.add(c.drug)}));
 const anc=new Map([...names].map(d=>[d,v1641Anchor(d,basis,names)]));
 const tot=v1641Sig(a),cred=v1641Sig(v1641Sub(a,d=>anc.get(d)?.credit));
 const rows=[],cl=[];let excess=0;
 names.forEach(d=>{const x=anc.get(d),solo=Math.min(1,v1641Sig(v1641Sub(a,n=>n===d)).reduce((s,t)=>s+t.v,0)),dose=doses.get(d),D=DRUGS[d];let cap=null,ex=0,n=0;
  if(x.credit&&x.cat==='coadyuvante'&&solo>.0005){cap=V1641_W*Math.min(1,x.es/V1641_ES_MAX);ex=Math.max(0,solo-cap);excess+=ex}
  if(x.credit&&x.cat!=='sin-revisar'&&solo<=.0005&&dose>0&&D){const f=Math.min(1.22,Math.max(.05,(dose/Math.max(1,D.max||dose))*1.55));n=Math.min(1,(x.es/V1641_ES_MAX)*Math.pow(f,.55));cl.push(n)}
  if(solo>.0005||n>0||x.cat!=='sin-revisar')rows.push({drug:d,solo,cap,ex,n,anchor:x,credited:x.credit?Math.max(0,solo-ex)+V1641_W*n:0});
 });
 const N=cl.length?1-cl.reduce((p,n)=>p*(1-n),1):0,C=V1641_W*N,sumTot=tot.reduce((s,t)=>s+t.v,0),sumCred=cred.reduce((s,t)=>s+t.v,0),cut=Math.min(excess,sumCred);
 const terms=tot.map((t,i)=>({label:t.label,mech:t.v,cred:cred[i].v,origin:'h'}));
 if(cut>.0005)terms.push({label:'Tope por tamaño de efecto (coadyuvantes)',mech:0,cred:-cut,origin:'t'});
 if(C>.0005)terms.push({label:'Antidepresivo clínico (tamaño de efecto)',mech:C,cred:C,origin:'k2'});
 return {basis,rows,terms,adMech:Math.min(1,sumTot+C),adClin:Math.min(1,Math.max(0,sumCred-cut)+C)};
}
/* Capa O: el punto usa los dos componentes acreditados. yMech = extremo antimaníaco; yAdMech = extremo antidepresivo */
const v1641VectorBase=vectorProfile;
vectorProfile=function(a){const v=v1641VectorBase(a),m=v1641Model(a);
 return {...v,ad:m.adClin,adMech:m.adMech,y:(m.adClin-v.am)*7,yMech:(m.adClin-v.amMech)*7,yAdMech:(m.adMech-v.am)*7,antidep:m}};
Object.assign(V1637_ORIGIN,{t:'tope v16.41 · tamaño de efecto como coadyuvante',k2:'ancla clínica · tamaño de efecto del metaanálisis'});
const v1641TermsBase=v1636Terms;
v1636Terms=function(a){const m=v1641Model(a);
 return v1641TermsBase(a).filter(t=>t.comp!=='ad').concat(m.terms.map(t=>({comp:'ad',label:t.label,v:t.cred,vm:t.mech,origin:t.origin})).filter(t=>Math.abs(t.v)>.0005||t.vm>.0005))};
const V1641_LENS={bip:'depresión bipolar (lente bipolar)',uni:'depresión unipolar (lentes no bipolares)'};
const v1641BreakdownBase=v1636BreakdownHtml;
v1636BreakdownHtml=function(a){
 let html=v1641BreakdownBase(a);
 try{const v=vectorProfile(a),m=v.antidep,open='<tr class="v1636-comp"><th colspan="4">',i=html.indexOf(open+V1636_COMP.ad),j=html.indexOf(open+V1636_COMP.am);
  if(i<0||j<i)return html;
  const ts=m.terms.filter(t=>Math.abs(t.cred)>.0005||t.mech>.0005);
  const block=open+V1636_COMP.ad+' · acreditado '+v.ad.toFixed(2)+' · mecanístico '+v.adMech.toFixed(2)+' · ancla: '+V1641_LENS[m.basis]+'</th></tr>'+(ts.length?ts.map(t=>'<tr><td>'+esc(t.label)+'</td><td>'+t.cred.toFixed(3).replace('-','−')+'</td><td>'+t.mech.toFixed(3)+'</td><td>'+esc(V1637_ORIGIN[t.origin]||'')+'</td></tr>').join(''):'<tr><td colspan="4" class="mut">sin términos activos</td></tr>');
  html=html.slice(0,i)+block+html.slice(j);
  html=html.replace('vertical = 7 × (antidepresivo − antimaníaco acreditado). El segmento del mapa llega hasta el antimaníaco mecanístico.','vertical = 7 × (antidepresivo acreditado − antimaníaco acreditado). Los segmentos del mapa llegan hasta los valores mecanísticos.');
  if(m.rows.length){const rows=m.rows.map(r=>{const x=r.anchor;return '<tr><td>'+esc(r.drug)+'</td><td>'+(r.solo>.0005?r.solo.toFixed(3):'—')+'</td><td>'+(r.n>0?(V1641_W*r.n).toFixed(3)+(x.esFloor?' (mínimo)':''):'—')+'</td><td>'+r.credited.toFixed(3)+(r.ex>.0005?' (tope '+r.cap.toFixed(3)+')':'')+'</td><td>'+esc(V1641_CAT[x.cat])+(x.eff?' · '+esc(x.eff):'')+(x.note?'<br><span class="small">'+esc(x.note)+'</span>':'')+(x.src.length?'<br><span class="small">'+v1637SrcLinks(x.src)+'</span>':'')+'</td></tr>'}).join('');
   html=html.replace(/<\/section>$/,'<h4>Ancla antidepresiva por fármaco · '+V1641_LENS[m.basis]+'</h4><div class="tw"><table class="v1636-table v1637-table"><thead><tr><th>Fármaco</th><th>Mecanístico (vector)</th><th>Término clínico</th><th>Acreditado</th><th>Ancla clínica</th></tr></thead><tbody>'+rows+'</tbody><tfoot><tr><td colspan="5" class="small">El ancla cambia con la lente: en la bipolar cuenta la evidencia en depresión bipolar aguda ('+v1637SrcLinks(['yildiz'])+'); en las demás, la de depresión unipolar ('+v1637SrcLinks(['cipriani18'])+'). Término clínico: solo para fármacos acreditados cuyo vector no tiene magnitud antidepresiva; vale 0,24 × (DME ÷ 0,418) × escala de dosis, con 0,418 = amitriptilina, la mayor de Cipriani 2018. Las razones de probabilidades se convierten en DME con ln(OR) ÷ 1,81 ('+v1637SrcLinks(['chinn'])+'). «Mínimo»: sin tamaño de efecto publicado en la fuente; se usa el menor de Cipriani 2018 (reboxetina, OR 1,37). Tope: en los coadyuvantes con magnitud en el vector, lo acreditado no supera 0,24 × (DME ÷ 0,418). Los fármacos acreditados con magnitud propia conservan su valor mecanístico, sin escalar por tamaño de efecto.</td></tr></tfoot></table></div></section>')}
 }catch(e){}
 return html;
};
/* Mapa: segundo segmento, hacia el antidepresivo mecanístico */
const v1641PolarityBase=polarity;
polarity=function(a){
 const r=v1641PolarityBase.apply(this,arguments);
 try{const svg=document.querySelector('#polarity svg.clinical-map');if(!svg)return r;const p=clinicalPosition(),v=vectorProfile(a),sx=x=>500+x*34,sy=y=>330-y*25,cl=z=>Math.max(-10,Math.min(10,z));
  const dx=sx(cl(p.horizontal+v.x)),dy=sy(cl(p.vertical+v.y)),ay=sy(cl(p.vertical+v.yAdMech));
  if(Math.abs(ay-dy)>=2&&!svg.querySelector('.v1641-seg')){const NS='http://www.w3.org/2000/svg',ln=document.createElementNS(NS,'line'),c=document.createElementNS(NS,'circle'),t=document.createElementNS(NS,'text');
   ln.setAttribute('x1',dx);ln.setAttribute('y1',dy);ln.setAttribute('x2',dx);ln.setAttribute('y2',ay);ln.setAttribute('class','v1637-seg v1641-seg');
   c.setAttribute('cx',dx);c.setAttribute('cy',ay);c.setAttribute('r','7');c.setAttribute('class','v1637-mech v1641-mech');
   t.setAttribute('x',dx+14);t.setAttribute('y',ay+4);t.setAttribute('class','v1637-mech-label');t.textContent='mecanismo sin eficacia antidepresiva acreditada';
   svg.append(ln,c,t);
   svg.closest('.map-pair')?.querySelector('.vector-key')?.insertAdjacentHTML('beforeend','<span><i class="v1637-key"></i>segmento: antidepresivo mecanístico no acreditado</span>')}
  const aside=svg.closest('.map-pair')?.querySelector('aside');
  if(aside&&!aside.querySelector('.v1641-card')){const card='<div class="logic-card v1641-card" style="margin-top:8px"><b>Componente antidepresivo</b><span>acreditado '+v.ad.toFixed(2)+' · mecanístico '+v.adMech.toFixed(2)+'<br>ancla: '+esc(V1641_LENS[v.antidep.basis])+'</span></div>';
   const am=aside.querySelector('.v1637-card');if(am)am.insertAdjacentHTML('beforebegin',card);else aside.insertAdjacentHTML('beforeend',card)}
 }catch(e){}
 return r;
};

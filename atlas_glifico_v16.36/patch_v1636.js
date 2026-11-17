/* v16.36 · Correcciones tras revisión externa.
   1) Inductores moderados de CYP3A4 (modafinilo) en las reglas de cariprazina y lurasidona (FT Reagila 4.3/4.5; FT lurasidona 4.5).
   2) Cada alerta distingue «activa en la pauta» de «presente en el borrador» (alguna fila sin dosis activa).
   3) «Sin alertas» pasa a decir que ninguna regla cubierta se activó, no que la combinación sea segura.
   4) Desglose del vector O: qué término mueve cada componente y de qué regla procede. */
const V1636_MODERATE_INDUCERS=['Modafinilo'];
const v1636RulesBase=v1634Rules;
v1634Rules=function(){
 const out=v1636RulesBase();
 const rows=state.rows.filter(r=>v1634Has(r.drug)),names=[...new Set(rows.map(r=>r.drug))],has=n=>names.includes(n),pick=xs=>names.filter(n=>xs.includes(n));
 const mod=pick(V1636_MODERATE_INDUCERS);
 if(mod.length&&has('Cariprazina'))out.push({level:'contra',title:'Inductor moderado de CYP3A4 + cariprazina',drugs:[...mod,'Cariprazina'],text:'La ficha de Reagila contraindica los inductores potentes o moderados de CYP3A4 y nombra el modafinilo: disminución significativa de la exposición a cariprazina total.',src:[V1634_SRC.cariprazina],extra:''});
 if(mod.length&&has('Lurasidona'))out.push({level:'vigilar',title:'Inductor moderado de CYP3A4 + lurasidona',drugs:[...mod,'Lurasidona'],text:'La ficha de lurasidona prevé con inductores moderados (p. ej., modafinilo) una reducción de la exposición menor de 2 veces, durante la coadministración y hasta dos semanas después.',src:[V1634_SRC.lurasidona],extra:''});
 // Estado de la combinación: activa o presente solo en el borrador
 const active=new Set(state.rows.filter(r=>v1634Has(r.drug)&&v140Active(r)).map(r=>r.drug));
 for(const r of out){const inactive=r.drugs.filter(d=>names.includes(d)&&!active.has(d));r.draft=inactive.length>0;r.inactive=inactive}
 const order={contra:0,mayor:1,vigilar:2};
 return out.sort((a,b)=>order[a.level]-order[b.level]||(a.draft?1:0)-(b.draft?1:0));
};
/* Presentación: estado de cada tarjeta y mensaje vacío preciso */
const v1636RenderBase=v1634Render;
v1634Render=function(){
 v1636RenderBase();
 const box=document.getElementById('v1634-alerts');if(!box)return;
 let rules=[];try{rules=v1634Rules()}catch(e){}
 const none=box.querySelector('.v1634-none');
 if(none&&!rules.length){none.textContent='Ninguna de las reglas cubiertas se activó con esta pauta. No significa que la combinación sea segura: el bloque solo cubre las familias descritas y no sustituye la ficha técnica.';return}
 const items=[...box.querySelectorAll('.v1634-item')];
 rules.forEach((r,i)=>{const it=items[i];if(!it||it.dataset.v1636)return;it.dataset.v1636='1';
  const tag=document.createElement('span');tag.className='v1636-state '+(r.draft?'draft':'live');tag.textContent=r.draft?'en el borrador':'activa en la pauta';it.querySelector('summary')?.append(' ',tag);
  if(r.draft){it.classList.add('v1636-draft');const p=document.createElement('p');p.className='v1636-draftnote';p.textContent='Combinación presente en el borrador: '+r.inactive.join(', ')+' sin dosis activa. El aviso se mantiene por presencia; se confirmará al activar la dosis.';it.querySelector('.v1634-drugs')?.after(p)}
 });
 const foot=box.querySelector('.v1634-foot');if(foot)foot.textContent='Avisos por presencia en la pauta; «activa» = todos los fármacos implicados con dosis activa. Que no aparezca un aviso significa que ninguna regla cubierta se activó, no que la combinación sea segura.';
};
/* Desglose del vector O (vectorProfile): qué término aporta a cada componente */
const V1636_ORIGIN={h:'heredado v16.0',u:'política anti/pro del usuario',e:'factor editorial sin calibrar'};
function v1636Terms(a){
 const agon=/\bagonismo(?! inverso)|facilit/i,ant=/antagon|agonismo inverso|bloque|inhib/i,antH=/antagon|agonismo inverso|bloque|inhib|antihistam/i,antA=/antagon|agonismo inverso|bloque|inhib|adrenol[ií]tic/i,P=(t,re)=>policySignal(a,t,re);
 const T=(comp,label,sig,w,origin)=>({comp,label,v:sig*w,w,origin});
 return [
  T('act','NET',g(a,'NET'),.32,'h'),T('act','DAT',g(a,'DAT'),.25,'h'),T('act','D3 agonismo',actionSignal(a,'D3',agon),.25,'h'),T('act','5-HT1A agonismo',actionSignal(a,'HT1A',agon),.10,'h'),T('act','H1 agonismo',P('H1',agon),.58,'u'),T('act','α1 agonismo',P('A1',agon),.18,'u'),
  T('sed','H1 antagonismo',P('H1',antH),.58,'u'),T('sed','M1 antagonismo',P('M1',ant),.24,'u'),T('sed','α1 antagonismo',P('A1',antA),.18,'u'),
  T('ad','NET',g(a,'NET'),.24,'h'),T('ad','SERT',g(a,'SERT'),.14,'h'),T('ad','5-HT1A agonismo',actionSignal(a,'HT1A',agon),.23,'h'),T('ad','D3 agonismo',actionSignal(a,'D3',agon),.16,'h'),T('ad','DAT',g(a,'DAT'),.10,'h'),T('ad','MAO-A',g(a,'MAOA'),.13,'h'),
  T('am','D2 antagonismo',actionSignal(a,'D2',ant),.38,'h'),T('am','D2 agonismo parcial (× 0,5)',P('D2',/agonismo parcial|agonista parcial/i),.38*.5,'e'),T('am','D3 antagonismo',actionSignal(a,'D3',ant),.20,'h'),T('am','5-HT2A antagonismo',actionSignal(a,'HT2A',ant),.14,'h'),T('am','M1 agonismo',P('M1',agon),.24,'u')
 ].filter(t=>t.v>0.0005);
}
const V1636_COMP={act:'Activación',sed:'Sedación',ad:'Antidepresivo / pro-monoaminérgico',am:'Antimaníaco / contención D2'};
function v1636BreakdownHtml(a){
 const v=vectorProfile(a),terms=v1636Terms(a);
 const body=['act','sed','ad','am'].map(k=>{const ts=terms.filter(t=>t.comp===k),sum=ts.reduce((s,t)=>s+t.v,0);
  return '<tr class="v1636-comp"><th colspan="3">'+V1636_COMP[k]+' · '+v[k].toFixed(2)+(sum>1?' (tope 1; suma '+sum.toFixed(2)+')':'')+'</th></tr>'+(ts.length?ts.map(t=>'<tr><td>'+esc(t.label)+'</td><td>'+t.v.toFixed(3)+'</td><td>'+esc(V1636_ORIGIN[t.origin])+'</td></tr>').join(''):'<tr><td colspan="3" class="mut">sin términos activos</td></tr>')}).join('');
 return '<section class="v1636-breakdown"><h3>Qué mueve el vector · capa O</h3><p class="small">Horizontal = 7 × (activación − sedación); vertical = 7 × (antidepresivo − antimaníaco). La sedación solo actúa en el eje horizontal. Cada término es señal × peso; los pesos son editoriales, no tamaños de efecto clínico.</p><div class="tw"><table class="v1636-table"><thead><tr><th>Término</th><th>Aporte</th><th>Origen de la regla</th></tr></thead><tbody>'+body+'</tbody></table></div></section>';
}
function v1636Attach(){
 for(const id of ['polarity','vectors']){const host=document.getElementById(id);if(!host||!host.classList.contains('active'))continue;
  if(id==='vectors'&&typeof V161!=='undefined'&&V161.basis!=='O'){host.querySelector('.v1636-breakdown')?.remove();continue}
  const html=v1636BreakdownHtml(aggregate()),old=host.querySelector('.v1636-breakdown');if(old&&old.outerHTML===html)continue;
  if(old)old.outerHTML=html;else(host.querySelector('.panel')||host).insertAdjacentHTML('beforeend',html)}
}
const v1636ActivateBase=activateView;activateView=function(...args){const r=v1636ActivateBase.apply(this,args);try{v1636Attach()}catch(e){}return r};
const v1636EvaluateBase=evaluate;evaluate=function(...args){const r=v1636EvaluateBase.apply(this,args);try{v1636Attach()}catch(e){}return r};

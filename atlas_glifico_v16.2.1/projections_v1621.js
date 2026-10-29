/* v16.2.1 · proyecciones experimentales con bases de evidencia mutuamente excluyentes (diseño de v16.2).
   P nunca usa el valor ajustado por dosis; Q nunca tiene longitud ni área.
   Política anti/pro (v16.2.1): H1⊣/α1⊣/M1⊣ → sedación; H1⊕/α1⊕ → activación; M1⊕ → contención. Los pesos de agonistas son espejo, sin calibrar.
   La columna «Efectos asociados» es cualitativa y no es un eje ni una base. */
const V161={basis:'P',show:{kites:true,joint:true,centroid:false},filter:'',status:'todos'};
const V161_S=7,V161_AX=['act','sed','ad','am'];
const V161_LBL={act:'Activación · proyección',sed:'Sedación · proyección',ad:'Pro-monoaminérgico · proyección',am:'Contención · proyección'};
const V161_BASE={P:'P · proyección de afinidad',O:'O · heurística operativa del atlas',Q:'Q · relaciones cualitativas'};
const V161_AGON=/\bagonismo(?! inverso)|facilit/i,V161_ANT=/antagon|agonismo inverso|bloque|inhib/i,V161_ANT_H1=/antagon|agonismo inverso|bloque|inhib|antihistam/i,V161_INH=/inhib|recaptaci|captaci|liberaci|facilit/i;
const V161_NEG=/sin funci[oó]n|funci[oó]n no|no (se )?(infiere|inferible|resuelt|tipific|asign|fiable)|direcci[oó]n (funcional )?no|preclínic|experimental|propuest|hip[oó]tesis|accesori|contextual|indirect|baja afinidad|afinidad baja|muy baja|d[eé]bil|no demostrad|probable|dato no humano|sin agonismo/i;
const V161_DASH=['','9 4','2 4','10 3 2 3','15 5','5 2 1 2'];
function v161Eligible(c){return ['parent','component'].includes(c.entityType)&&!c.petEligible&&!c.qualitative&&c.evidence!=='esqueleto ordinal'&&c.potencyEligible!==false}
function v161Take(a,t,re){
  const cs=(a[t]?.contrib||[]).filter(c=>v161Eligible(c)&&re.test(String(c.action))&&!V161_NEG.test(String(c.action)));
  return cs.length?Math.max(...cs.map(c=>Math.max(0,Math.min(10,Number(c.potencyValue)||0))))/10:0;
}
function v161P(a){
  const T=(t,re)=>v161Take(a,t,re);
  const s={NET:T('NET',V161_INH),DAT:T('DAT',V161_INH),SERT:T('SERT',V161_INH),MAOA:T('MAOA',/inhib/i),HT1Aa:T('HT1A',V161_AGON),D3a:T('D3',V161_AGON),D2n:T('D2',V161_ANT),D3n:T('D3',V161_ANT),HT2An:T('HT2A',V161_ANT),H1n:T('H1',V161_ANT_H1),M1n:T('M1',V161_ANT),A1n:T('A1',V161_ANT),H1a:T('H1',V161_AGON),A1a:T('A1',V161_AGON),M1a:T('M1',V161_AGON)};
  // Coeficientes editoriales heredados; los de los agonistas H1/α1/M1 son espejo de los de sedación. No son tamaños de efecto clínico.
  return {act:Math.min(1,s.NET*.32+s.DAT*.25+s.D3a*.25+s.HT1Aa*.10+s.H1a*.58+s.A1a*.18),sed:Math.min(1,s.H1n*.58+s.M1n*.24+s.A1n*.18),ad:Math.min(1,s.NET*.24+s.SERT*.14+s.HT1Aa*.23+s.D3a*.16+s.DAT*.10+s.MAOA*.13),am:Math.min(1,s.D2n*.38+s.D3n*.20+s.HT2An*.14+s.H1n*.14+s.M1a*.24)};
}
function v161QDir(t,action){
  const s=String(action||'');if(!s||V161_NEG.test(s))return [];
  const ag=V161_AGON.test(s)&&!/antagon/i.test(s),an=V161_ANT.test(s);
  switch(t){
    case'NET':case'DAT':return V161_INH.test(s)?['act','ad']:[];
    case'SERT':return /inhib|recaptaci|liberaci/i.test(s)?['ad']:[];
    case'MAOA':return /inhib/i.test(s)?['ad']:[];
    case'HT1A':return ag?['act','ad']:[];
    case'D3':return ag?['act','ad']:(an?['am']:[]);
    case'D2':return an?['am']:[];
    case'HT2A':return an?['am']:[];
    case'H1':return (an||/antihistam/i.test(s))?['sed','am']:(ag?['act']:[]);
    case'M1':return an?['sed']:(ag?['am']:[]);
    case'A1':return an?['sed']:(ag?['act']:[]);
    case'GABAA':return /modulaci[oó]n alost[eé]rica positiva|potenciaci[oó]n|facilitaci[oó]n|modulaci[oó]n gaba-a/i.test(s)?['sed']:[];
    default:return [];
  }
}
function v161Q(a){
  const q={act:[],sed:[],ad:[],am:[]};
  Object.entries(a).forEach(([t,x])=>(x.contrib||[]).forEach(c=>{
    if(!['parent','component'].includes(c.entityType)||c.petEligible||(!c.qualitative&&c.evidence!=='esqueleto ordinal'))return;
    v161QDir(t,c.action).forEach(k=>{const lab=(TARGET_META[t]?.[0]||t)+': '+String(c.action);if(!q[k].includes(lab))q[k].push(lab)});
  }));return q;
}
function v161Reason(a,d){
  const ts=new Set();Object.entries(a).forEach(([t,x])=>(x.contrib||[]).forEach(c=>{if(['parent','component'].includes(c.entityType)&&!c.petEligible)ts.add(TARGET_META[t]?.[0]||t)}));
  return ts.size?'Sin proyección en los cuatro ejes de esta base; dianas presentes: '+[...ts].slice(0,6).join(', ')+'.':(d?.mech?'Mecanismo descrito en el catálogo; sin proyección aplicable.':'Sin datos aplicables a estos cuatro ejes.');
}
const V161_EFF=[
  {t:['H1'],re:V161_ANT_H1,lab:'H1 ⊣',txt:'sedación y apetito/aumento de peso'},
  {t:['A1'],re:V161_ANT,lab:'α1 ⊣',txt:'ortostasis/hipotensión; somnolencia añadida (secundaria: por sí solo es poco sedante)'},
  {t:['M1','M3','MACH'],re:V161_ANT,lab:'M ⊣',txt:'antimuscarínico: xerostomía, antiperistaltismo/íleo, prodelirium; sedación leve; leve ↑ dopamina secundaria'},
  {t:['H1'],re:V161_AGON,lab:'H1 ⊕',txt:'vigilia'},
  {t:['A1'],re:V161_AGON,lab:'α1 ⊕',txt:'vigilia; ↑ presión arterial'},
  {t:['M1'],re:V161_AGON,lab:'M1 ⊕',txt:'↑ peristaltismo, sialorrea; procognitivo-antipsicótico'}];
function v161Eff(a){
  const out=[],par=c=>['parent','component'].includes(c.entityType)&&!c.petEligible;
  V161_EFF.forEach(e=>{
    const cs=e.t.flatMap(t=>(a[t]?.contrib||[]).filter(c=>par(c)&&e.re.test(String(c.action))&&!V161_NEG.test(String(c.action))));
    let b='',who='';
    if(cs.some(c=>v161Eligible(c)))b='afinidad documentada';
    else if(cs.some(c=>!c.qualitative&&(c.evidence==='esqueleto ordinal'||c.potencyEligible===false)))b='ordinal clínico';
    else if(cs.length)b='cualitativo';
    else{const m=[];e.t.forEach(t=>(a[t]?.contrib||[]).forEach(c=>{if(c.entityType==='metabolite'&&e.re.test(String(c.action))&&!V161_NEG.test(String(c.action))&&!m.includes(c.entity))m.push(c.entity)}));if(m.length){b='metabolito';who=m.join(', ')}}
    if(b)out.push({lab:e.lab,txt:e.txt,b,who});
  });return out;
}
function v161EffHtml(list){
  if(!list||!list.length)return '<span class="mut">—</span>';
  return '<ul class="vec-eff">'+list.map(e=>'<li><b>'+e.lab+'</b> <sup class="bas">'+esc(e.b)+'</sup> '+esc(e.txt)+(e.who?' <i>('+esc(e.who)+')</i>':'')+'</li>').join('')+'</ul>';
}
function v161Comp(row){
  const d=DRUGS[row.drug]||{},a=aggregate([row]);
  return {drug:row.drug,row,doseLabel:v154DoseLabel(row),fam:d.spain?.family||'',stab:!!d.stabilizer,active:v140Active(row),O:v140Active(row)?vectorProfile(a):null,P:v161P(a),Q:v161Q(a),eff:v161Eff(a),reason:v161Reason(a,d)};
}
function v161Project(c,basis=V161.basis){
  const out={...c,basis,area:null,numeric:0,dir:0};
  V161_AX.forEach(k=>{
    if(basis==='Q'){out[k]={v:null,b:c.Q[k].length?'Q':'—',why:c.Q[k].join('; ')};if(c.Q[k].length)out.dir++;}
    else{const v=c[basis]?.[k];out[k]={v:Number.isFinite(v)&&v>.004?v:null,b:Number.isFinite(v)&&v>.004?basis:'—'};if(out[k].v!=null)out.numeric++;}
  });
  if(basis!=='Q'&&out.numeric)out.area=.5*((out.act.v||0)+(out.sed.v||0))*((out.ad.v||0)+(out.am.v||0))*V161_S**2;
  out.status=out.numeric?'numeric':out.dir?'direction':'none';
  out.reason=basis==='O'&&!c.active?'Sin referencia de dosis/contexto: O no calculada.':out.numeric||out.dir?'':c.reason;
  return out;
}
function v161Val(c,k){return c[k]?.v??0}
function v161Kite(P,c){return [[P.x+(c.act||0)*V161_S,P.y],[P.x,P.y+(c.ad||0)*V161_S],[P.x-(c.sed||0)*V161_S,P.y],[P.x,P.y-(c.am||0)*V161_S]]}
function v162Centroid(points){
  let crossSum=0,x=0,y=0;
  points.forEach((p,i)=>{const q=points[(i+1)%points.length],cross=p[0]*q[1]-q[0]*p[1];crossSum+=cross;x+=(p[0]+q[0])*cross;y+=(p[1]+q[1])*cross});
  return Math.abs(crossSum)<1e-10?null:{x:x/(3*crossSum),y:y/(3*crossSum)};
}
function v161Cell(x){
  if(x.v!=null)return '<span class="vec-barbox"><i style="width:'+Math.round(x.v*100)+'%"></i></span>'+x.v.toFixed(2)+' <sup class="bas">'+x.b+'</sup>';
  if(x.b==='Q')return '<span title="'+esc(x.why)+'">Relación Q · sin magnitud</span>';
  return '<span class="mut" title="Sin valor aplicable en esta base; no equivale a ausencia de actividad">—</span>';
}
function v161Area(c){return c.area==null?'—':c.area<.05?'segmento':c.area.toFixed(1)}
function v161Matrix(){return Object.keys(DRUGS).map(drug=>v161Comp({drug,dose:defaultDose(drug)}))}
function v161Csv(matrix,basis=V161.basis){
  const q=s=>'"'+String(s??'').replace(/"/g,'""')+'"';
  const h=['fármaco','familia','base_exclusiva','referencia_dosis_O','act','sed','ad','am','área_geométrica_u2','estado','efectos_asociados','nota'];
  return [h.join(','),...matrix.map(raw=>{const c=v161Project(raw,basis);return [c.drug,c.fam,basis,basis==='O'?c.doseLabel:'No aplicada',...V161_AX.map(k=>basis==='Q'?(c[k].why||''):(c[k].v??'')),c.area??'',c.status,(c.eff||[]).map(e=>e.lab+' ['+e.b+'] '+e.txt+(e.who?' ('+e.who+')':'')).join(' | '),c.reason].map(q).join(',')})].join('\n');
}
function v161MatrixHtml(matrix){
  const f=V161.filter.toLowerCase(),m=matrix.map(c=>v161Project(c)),rows=m.filter(c=>(!f||(c.drug+' '+c.fam).toLowerCase().includes(f))&&(V161.status==='todos'||c.status===V161.status));
  const select=[['todos','Todos'],['numeric','Con proyección numérica'],['direction','Solo relaciones Q'],['none','Sin proyección aplicable']].map(([v,l])=>'<option value="'+v+'"'+(V161.status===v?' selected':'')+'>'+l+'</option>').join('');
  return '<p class="small">'+matrix.length+' entidades · '+esc(V161_BASE[V161.basis])+'. Una sola base en cada tabla y exportación. En O se usa la referencia del catálogo únicamente si no exige contexto adicional.</p><div class="pdn-controls"><label>Buscar <input id="vecQ" type="search" value="'+esc(V161.filter)+'" placeholder="fármaco o familia"></label><label>Mostrar <select id="vecB">'+select+'</select></label><button type="button" id="vecCsv">Exportar CSV · '+V161.basis+'</button></div><div class="tw"><table class="vec-table vec-matrix"><thead><tr><th>Entidad</th><th>Referencia O</th>'+V161_AX.map(k=>'<th>'+esc(V161_LBL[k])+'</th>').join('')+'<th>Área geométrica u²</th><th>Efectos asociados</th><th>Detalle</th></tr></thead><tbody>'+rows.map(c=>'<tr><td><b>'+esc(c.drug)+'</b><br><small>'+esc(c.fam)+'</small></td><td>'+esc(V161.basis==='O'?c.doseLabel:'No aplicada')+'</td>'+V161_AX.map(k=>'<td>'+v161Cell(c[k])+'</td>').join('')+'<td>'+v161Area(c)+'</td><td class="rs">'+v161EffHtml(c.eff)+'</td><td>'+esc(c.reason||V161_AX.map(k=>c[k].why).filter(Boolean).join(' · '))+'</td></tr>').join('')+'</tbody></table></div>';
}
function v162ProjectionSvg(per,U){
  const P={x:0,y:0},sx=x=>500+x*46,sy=y=>340-y*35,pts=ps=>ps.map(p=>sx(p[0]).toFixed(2)+','+sy(p[1]).toFixed(2)).join(' '),joint=v161Kite(P,U),centroid=v162Centroid(joint);
  let svg='<svg xmlns="http://www.w3.org/2000/svg" class="vec-svg" viewBox="0 0 1000 700" role="img" aria-labelledby="vecT vecD"><title id="vecT">Proyección experimental · '+esc(V161_BASE[V161.basis])+'</title><desc id="vecD">Una sola base. Los cuatro ejes usan coeficientes editoriales heredados, no unidades clínicas. La envolvente reúne máximos por eje; no estima efecto conjunto. Origen geométrico, no estado del paciente.</desc><defs><pattern id="vecHatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="10" stroke="#173f6b" stroke-width="1"/></pattern></defs><rect width="1000" height="700" fill="#fff"/><rect x="155" y="77" width="690" height="526" fill="#fff" stroke="#38536a"/><line x1="155" y1="340" x2="845" y2="340" stroke="#6a8092"/><line x1="500" y1="77" x2="500" y2="603" stroke="#6a8092"/>';
  for(const v of [-6,-3,3,6])svg+='<text x="'+sx(v)+'" y="357" text-anchor="middle" font-size="11">'+v+'</text><text x="487" y="'+(sy(v)+4)+'" text-anchor="end" font-size="11">'+v+'</text>';
  svg+='<text x="500" y="49" text-anchor="middle" font-size="14" font-weight="700">Proyección pro-monoaminérgica (ad)</text><text x="500" y="631" text-anchor="middle" font-size="14" font-weight="700">Proyección de contención (am)</text><text x="143" y="344" text-anchor="end" font-size="13">Sedación (sed)</text><text x="857" y="344" font-size="13">Activación (act)</text>';
  if(V161.show.joint&&per.some(x=>x.c.numeric))svg+='<polygon data-vec-basis="'+V161.basis+'" data-vec-envelope="max" points="'+pts(joint)+'" fill="url(#vecHatch)" stroke="#173f6b" stroke-width="3"/>';
  if(V161.show.kites)per.forEach((x,i)=>{
    if(!x.c.numeric)return;const c=Object.fromEntries(V161_AX.map(k=>[k,v161Val(x.c,k)])),vertices=v161Kite(P,c);
    svg+='<polygon data-vec-basis="'+V161.basis+'" data-vec-drug="'+esc(x.r.drug)+'" points="'+pts(vertices)+'" fill="#173f6b" fill-opacity=".045" stroke="#152f43" stroke-width="2"'+(V161_DASH[i%6]?' stroke-dasharray="'+V161_DASH[i%6]+'"':'')+'><title>'+esc((i+1)+'. '+x.r.drug+' · '+V161.basis)+'</title></polygon>';
    const index=[['act',0],['ad',1],['sed',2],['am',3]].sort((a,b)=>c[b[0]]-c[a[0]])[0][1],v=vertices[index],dx=v[0]>=0?15:-15,dy=-16-(i%3)*20,xp=sx(v[0])+dx,yp=sy(v[1])+dy;
    svg+='<g><title>'+esc(x.r.drug)+'</title><rect x="'+(xp-10)+'" y="'+(yp-10)+'" width="20" height="20" fill="#fff" stroke="#173f6b"/><text x="'+xp+'" y="'+(yp+4)+'" text-anchor="middle" font-size="12" font-weight="700">'+(i+1)+'</text></g>';
  });
  if(V161.show.centroid&&centroid)svg+='<circle data-vec-centroid="true" cx="'+sx(centroid.x)+'" cy="'+sy(centroid.y)+'" r="6" fill="#fff" stroke="#173f6b" stroke-width="2"/><text x="'+(sx(centroid.x)+12)+'" y="'+(sy(centroid.y)-10)+'" font-size="12">centroide geométrico</text>';
  svg+='<circle cx="500" cy="340" r="4" fill="#173f6b"/><text x="500" y="664" font-size="12" text-anchor="middle">'+esc(V161_BASE[V161.basis])+' · origen geométrico · unidades editoriales, no clínicas</text></svg>';
  return {svg,centroid};
}
function vectorsView(a){
  const host=$('#vectors');if(!host)return;
  const basis=V161.basis,rows=state.rows.filter(r=>basis!=='O'||v140Active(r)),per=rows.map(r=>({r,c:v161Project(v161Comp(r))}));
  const U=Object.fromEntries(V161_AX.map(k=>[k,Math.max(0,...per.map(x=>v161Val(x.c,k)))]));
  const drawing=basis==='Q'?null:v162ProjectionSvg(per,U),area=.5*(U.act+U.sed)*(U.ad+U.am)*V161_S**2;
  const basisButtons=Object.entries(V161_BASE).map(([b,l])=>'<button type="button" data-vec-basis-select="'+b+'" aria-pressed="'+(b===basis)+'">'+l+'</button>').join('');
  const ch=(k,l)=>'<label><input type="checkbox" data-vs="'+k+'"'+(V161.show[k]?' checked':'')+'> '+l+'</label>';
  const table=per.length?'<div class="tw"><table class="vec-table"><thead><tr><th>#</th><th>Componente</th><th>Dosis/contexto de la pauta</th>'+V161_AX.map(k=>'<th>'+esc(V161_LBL[k])+'</th>').join('')+'<th>Área geométrica u²</th><th>Efectos asociados</th><th>Detalle</th></tr></thead><tbody>'+per.map((x,i)=>'<tr><td>'+(i+1)+'</td><td><b>'+esc(x.r.drug)+'</b></td><td>'+esc(x.c.doseLabel)+(basis==='P'?' · no aplicada a P':'')+'</td>'+V161_AX.map(k=>'<td>'+v161Cell(x.c[k])+'</td>').join('')+'<td>'+v161Area(x.c)+'</td><td class="rs">'+v161EffHtml(x.c.eff)+'</td><td>'+esc(x.c.reason||V161_AX.map(k=>x.c[k].why).filter(Boolean).join(' · '))+'</td></tr>').join('')+'</tbody></table></div>':'<p class="vec-empty">No hay componentes aplicables a esta base. O exige dosis/contexto definidos; P y Q no necesitan una dosis para mostrar los datos disponibles.</p>';
  const centroid=drawing?.centroid;
  host.innerHTML='<div class="panel"><h2>Proyecciones de mecanismos · experimental</h2><p class="pdn-lead">Comparación complementaria de cuatro ejes editoriales. <b>Una sola base cada vez</b>: no se completa la heurística con afinidad ni se asigna intensidad a lo cualitativo. Las áreas no son eficacia ni utilidad terapéutica.</p><div class="vec-basis" role="group" aria-label="Base exclusiva de proyección">'+basisButtons+'</div>'
    +(basis==='Q'?'<p>Q conserva las relaciones cualitativas tipificadas y muestra su dirección como texto. Sin longitud, área o centroide.</p>':'<div class="pdn-controls">'+ch('kites','Perfiles individuales')+ch('joint','Envolvente de máximos')+ch('centroid','Centroide geométrico')+'</div>'+(rows.length?'<div class="pdn-svgwrap">'+drawing.svg+'</div>':'')+'<p class="small">La envolvente toma el <b>máximo por eje</b>, no suma fármacos ni modela interacción. '+(per.some(x=>x.c.numeric)?'Área geométrica: '+area.toFixed(2)+' u². '+(centroid?'Centroide: ('+centroid.x.toFixed(2)+'; '+centroid.y.toFixed(2)+').':'Polígono degenerado: no hay centroide de área.'):'Sin valores numéricos aplicables en esta base.')+'</p>')
    +table+'<details class="vec-formula"><summary>Base, alcance y cálculo</summary><p>P proyecta la potencia intrínseca documentada, sin dosis ni exposición. Usa solo dianas con acción explícita; sus coeficientes son editoriales heredados. O es el vectorProfile del atlas con la política anti/pro de H1, α1 y M1 (v16.2.1): lee esas dianas por elegibilidad operativa, con dosis, incluidos los ordinales con su magnitud clínica; <b>no es PET ni respuesta observada</b>. P no rellena las ausencias de O. Q expresa relaciones de clase sin magnitud. Ninguna base incluye cuantificación operativa de metabolitos. «Efectos asociados» (apetito, ortostasis, carga antimuscarínica, vigilia, procolinérgico) es una lectura cualitativa por dirección y procedencia, sin cifras, que no entra en las áreas.</p><p>Escala geométrica = 7 × componente. Área = ½ × (act + sed) × (ad + am) × 7². El centroide se calcula sobre los vértices del polígono por la fórmula de área orientada; no es el balance (act − sed, ad − am), ni un desplazamiento clínico del paciente. Los perfiles que no caben en estos cuatro ejes permanecen en receptoroma, mapas y catálogo.</p></details><details class="vec-all" id="vecAll"><summary>Matriz completa · '+Object.keys(DRUGS).length+' entidades · '+basis+'</summary><div id="vecAllBody">Abrir para calcular la base seleccionada.</div></details></div>';
  host.querySelectorAll('[data-vec-basis-select]').forEach(el=>el.onclick=()=>{V161.basis=el.dataset.vecBasisSelect;vectorsView(a)});
  host.querySelectorAll('[data-vs]').forEach(el=>el.onchange=()=>{V161.show[el.dataset.vs]=el.checked;vectorsView(a)});
  let matrix=null;const fill=()=>{matrix??=v161Matrix();$('#vecAllBody').innerHTML=v161MatrixHtml(matrix);const q=$('#vecQ'),b=$('#vecB');q.oninput=()=>{V161.filter=q.value;const p=q.selectionStart;fill();$('#vecQ').focus();$('#vecQ').setSelectionRange(p,p)};b.onchange=()=>{V161.status=b.value;fill()};$('#vecCsv').onclick=()=>{const blob=new Blob(['\uFEFF'+v161Csv(matrix)],{type:'text/csv;charset=utf-8'}),u=URL.createObjectURL(blob),link=document.createElement('a');link.href=u;link.download='atlas_proyecciones_'+basis+'_v16.2.csv';document.body.appendChild(link);link.click();link.remove();setTimeout(()=>URL.revokeObjectURL(u),500)}};
  $('#vecAll').ontoggle=()=>{if($('#vecAll').open)fill()};
}


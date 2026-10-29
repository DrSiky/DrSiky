/* ===== v16.1 · vectores clínicos como áreas, componentes por capas, figuras ampliables y limpieza de avisos =====
   Capa O: cálculo operativo del atlas (vectorProfile; desde v16.1 incluye la política anti/pro de H1, α1 y M1, ver build.py).
   Capa P: misma fórmula y pesos con la potencia documentada intrínseca (independiente de la dosis y de la exposición), solo para dianas con dirección explícita en el texto de la acción.
   Capa C: ordinal clínico/regulatorio (CIMA, familia) con dirección explícita; la magnitud es la ordinal que ya figura en el atlas, no una afinidad. Solo rellena un eje que P deja vacío.
   Capa Q: dirección cualitativa sin magnitud (inferencia de clase); no aporta área.
   Política anti/pro de H1, α1 y M1: antagonismo → sedación (H1 principal, M1 y α1 secundarios) y efectos asociados; agonismo → vigilia (H1, α1) o contención/procolinérgico (M1). Los efectos asociados (apetito, ortostasis, carga antimuscarínica…) no son ejes.
   No se añaden constantes receptoriales ni magnitudes nuevas. */
const V161={show:{kites:true,joint:true,hull:false,net:false,dir:true,damp:true,layerO:true,layerP:true,layerC:true},filter:'',basis:'todos'};
const V161_S=7;
const V161_AX=['act','sed','ad','am'];
const V161_LBL={act:'Activación',sed:'Sedación',ad:'Pro-monoaminérgico',am:'Contención'};
const V161_AGON=/\bagonismo(?! inverso)|facilit/i,V161_ANT=/antagon|agonismo inverso|bloque|inhib/i,V161_INH=/inhib|recaptaci|captaci|liberaci|facilit/i;
const V161_NEG_B=/sin funci[oó]n|funci[oó]n no|no (se )?(infiere|inferible|resuelt|tipific|asign|fiable)|direcci[oó]n (funcional )?no|preclínic|experimental|propuest|hip[oó]tesis|accesori|contextual|indirect|no demostrad|probable|dato no humano|sin agonismo/i;
const V161_NEG=new RegExp(V161_NEG_B.source+'|baja afinidad|afinidad baja|muy baja|d[eé]bil','i'),V161_NEG_C=V161_NEG_B;
const V161_ANT_H1=new RegExp(V161_ANT.source+'|antihistam','i');
const V161_DASH=['','9 4','2 4','10 3 2 3','15 5','5 2 1 2'];

function v161Eligible(c){return ['parent','component'].includes(c.entityType)&&!c.petEligible&&!c.qualitative&&c.evidence!=='esqueleto ordinal'&&c.potencyEligible!==false}
function v161Ord(c){return ['parent','component'].includes(c.entityType)&&!c.petEligible&&!c.qualitative&&(c.evidence==='esqueleto ordinal'||c.potencyEligible===false)}
function v161Take(a,t,re,act,mode){const cs=(a[t]?.contrib||[]).filter(c=>{const x=String(c.action);if(!re.test(x))return false;if(v161Eligible(c))return !V161_NEG.test(x);return mode==='c'&&v161Ord(c)&&!V161_NEG_C.test(x)});return cs.length?Math.max(...cs.map(c=>Math.min(10,Number(c.potencyValue)||0)))/10:0}
function v161P(a,act,mode){
  const T=(t,re)=>v161Take(a,t,re,act,mode);
  const s={NET:T('NET',V161_INH),DAT:T('DAT',V161_INH),SERT:T('SERT',V161_INH),MAOA:T('MAOA',/inhib/i),
    HT1Aa:T('HT1A',V161_AGON),D3a:T('D3',V161_AGON),D2n:T('D2',V161_ANT),D3n:T('D3',V161_ANT),HT2An:T('HT2A',V161_ANT),H1n:T('H1',V161_ANT_H1),M1n:T('M1',V161_ANT),A1n:T('A1',V161_ANT),
    H1a:T('H1',V161_AGON),A1a:T('A1',V161_AGON),M1a:T('M1',V161_AGON)};
  /* Política anti/pro: pesos espejo de los de la sedación para los agonistas (H1 .58 y α1 .18 hacia activación; M1 .24 hacia contención); M1 antagonista ya no suma contención (su efecto secundario es un leve aumento dopaminérgico). */
  return {act:Math.min(1,s.NET*.32+s.DAT*.25+s.D3a*.25+s.HT1Aa*.10+s.H1a*.58+s.A1a*.18),sed:Math.min(1,s.H1n*.58+s.M1n*.24+s.A1n*.18),
    ad:Math.min(1,s.NET*.24+s.SERT*.14+s.HT1Aa*.23+s.D3a*.16+s.DAT*.10+s.MAOA*.13),am:Math.min(1,s.D2n*.38+s.D3n*.20+s.HT2An*.14+s.H1n*.14+s.M1a*.24)}
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
  }
  return [];
}
function v161Q(a){
  const q={act:[],sed:[],ad:[],am:[]};
  Object.entries(a).forEach(([t,x])=>(x.contrib||[]).forEach(c=>{
    if(!['parent','component'].includes(c.entityType)||c.petEligible)return;
    v161QDir(t,c.action).forEach(k=>{const lab=(TARGET_META[t]?TARGET_META[t][0]:t)+': '+String(c.action).slice(0,48);if(!q[k].includes(lab))q[k].push(lab)})
  }));
  return q;
}
function v161Reason(a,d){
  const ts=new Set();Object.entries(a).forEach(([t,x])=>(x.contrib||[]).forEach(c=>{if(['parent','component'].includes(c.entityType)&&!c.petEligible)ts.add(TARGET_META[t]?TARGET_META[t][0]:t)}));
  if(!ts.size)return d&&d.mech?'Sin dianas en el atlas; mecanismo descrito en texto, ajeno a los cuatro ejes.':'Sin dianas ni relaciones en el atlas (asociación fija o dato pendiente).';
  return 'Mecanismo ajeno a los cuatro ejes del modelo: '+[...ts].slice(0,5).join(', ')+(ts.size>5?'…':'')+'.';
}
const V161_EFF=[
  {id:'h1n',t:['H1'],re:V161_ANT_H1,lab:'H1 ⊣',txt:'sedación y apetito/aumento de peso'},
  {id:'a1n',t:['A1'],re:V161_ANT,lab:'α1 ⊣',txt:'ortostasis/hipotensión; somnolencia añadida (secundaria: por sí solo es poco sedante)'},
  {id:'m1n',t:['M1','M3','MACH'],re:V161_ANT,lab:'M ⊣',txt:'antimuscarínico: xerostomía, antiperistaltismo/íleo, prodelirium; sedación leve; leve ↑ dopamina secundaria'},
  {id:'h1a',t:['H1'],re:V161_AGON,lab:'H1 ⊕',txt:'vigilia'},
  {id:'a1a',t:['A1'],re:V161_AGON,lab:'α1 ⊕',txt:'vigilia; ↑ presión arterial'},
  {id:'m1a',t:['M1'],re:V161_AGON,lab:'M1 ⊕',txt:'↑ peristaltismo, sialorrea; procognitivo-antipsicótico'}];
function v161Eff(a,act){
  const out=[];
  V161_EFF.forEach(e=>{
    let v=0,b='';e.t.forEach(t=>{const n=v161Take(a,t,e.re,act,'c');if(n>v)v=n;});
    if(v>0){const num=e.t.some(t=>v161Take(a,t,e.re,act)>0);b=num?'P':'C'}
    let who='';
    if(!b){const q=e.t.some(t=>(a[t]?.contrib||[]).some(c=>['parent','component'].includes(c.entityType)&&!c.petEligible&&e.re.test(String(c.action))&&!V161_NEG.test(String(c.action))));if(q)b='Q'}
    if(!b){const m=[];e.t.forEach(t=>(a[t]?.contrib||[]).forEach(c=>{if(c.entityType==='metabolite'&&e.re.test(String(c.action))&&!V161_NEG_C.test(String(c.action))&&!m.includes(c.entity))m.push(c.entity)}));if(m.length){b='m';who=m.join(', ')}}
    if(b)out.push({id:e.id,lab:e.lab,txt:e.txt,v:v>0?v:null,b,who});
  });
  return out;
}
function v161EffHtml(list){
  if(!list||!list.length)return '<span class="mut">—</span>';
  return '<ul class="vec-eff">'+list.map(e=>'<li><b>'+e.lab+'</b>'+' <sup class="bas">'+e.b+'</sup> '+esc(e.txt)+(e.who?' <i>(metabolito: '+esc(e.who)+')</i>':'')+'</li>').join('')+'</ul>';
}
function v161Comp(row){
  const d=DRUGS[row.drug]||{},a=aggregate([row]),O=vectorProfile(a),act=v140Active(row),P=v161P(a,act),PC=v161P(a,act,'c'),Q=v161Q(a),out={drug:row.drug,dose:row.dose,fam:d.spain?.family||'',stab:!!d.stabilizer};
  V161_AX.forEach(k=>{
    if(O[k]>0.004)out[k]={v:O[k],b:'O'};
    else if(P[k]>0.004)out[k]={v:P[k],b:'P'};
    else if(PC[k]>0.004)out[k]={v:PC[k],b:'C'};
    else if(Q[k].length)out[k]={v:null,b:'Q',why:Q[k].join('; ')};
    else out[k]={v:null,b:'—'};
    out[k].alt={O:O[k],P:P[k],C:PC[k]>P[k]+0.004?PC[k]:0};
  });
  out.O=O;out.P=P;out.eff=v161Eff(a,act);
  out.area=0.5*((out.act.v||0)+(out.sed.v||0))*((out.ad.v||0)+(out.am.v||0))*V161_S*V161_S;
  out.numeric=V161_AX.filter(k=>out[k].v!=null).length;out.dir=V161_AX.filter(k=>out[k].b==='Q').length;
  out.status=out.numeric?'area':(out.dir?'direccion':(out.stab?'amortiguacion':'sin-eje'));
  out.reason=out.numeric||out.dir?'':(out.stab?'Estabilizador de acción no receptorial: el atlas lo trata como amortiguación, no como vector.':v161Reason(a,d));
  return out;
}
function v161Val(c,k){const x=c[k];if(!x.alt)return 0;for(const b of ['O','P','C']){if(V161.show['layer'+b]&&x.alt[b]>0.004)return x.alt[b]}return 0}
function v161Kite(P,c){return [[P.x+(c.act||0)*V161_S,P.y],[P.x,P.y+(c.ad||0)*V161_S],[P.x-(c.sed||0)*V161_S,P.y],[P.x,P.y-(c.am||0)*V161_S]]}
function v161Hull(pts){const p=[...pts].sort((a,b)=>a[0]-b[0]||a[1]-b[1]);if(p.length<3)return p;const cr=(o,a,b)=>(a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0]);const lo=[];p.forEach(q=>{while(lo.length>=2&&cr(lo[lo.length-2],lo[lo.length-1],q)<=0)lo.pop();lo.push(q)});const up=[];[...p].reverse().forEach(q=>{while(up.length>=2&&cr(up[up.length-2],up[up.length-1],q)<=0)up.pop();up.push(q)});return lo.slice(0,-1).concat(up.slice(0,-1))}

function v161Area(c){return c.area<0.05?'<span title="un solo eje (o dos opuestos): el polígono se reduce a un segmento">segmento</span>':c.area.toFixed(1)}
function v161Cell(x){
  if(x.b==='O'||x.b==='P'||x.b==='C')return '<span class="vec-barbox"><i style="width:'+Math.round(Math.min(1,x.v)*100)+'%"></i></span>'+x.v.toFixed(2)+' <sup class="bas">'+x.b+'</sup>';
  if(x.b==='Q')return '<span title="'+esc(x.why)+'">● dirección <sup class="bas">Q</sup></span>';
  return '<span class="mut">—</span>';
}
function v161Matrix(){
  const out=[];Object.keys(DRUGS).forEach(n=>{const d=DRUGS[n];const dose=d.dose>0?d.dose:(MIN_DEFAULT_DOSE[n]??1),row={drug:n,dose};
    const fd=typeof V156_FORMS!=='undefined'&&V156_FORMS[n];if(fd){row.formulationId=Object.keys(fd)[0];row.dailyUnits=1}
    try{const c=v161Comp(row);if(fd){c.cfg=(fd[row.formulationId]||{}).label||row.formulationId;c.reason=(c.reason?c.reason+' ':'')+'Evaluado con la presentación de referencia «'+c.cfg+'», 1 unidad/día; depende de la presentación y las unidades que configures en la pauta.'}out.push(c)}catch(e){}});return out;
}
function v161Csv(m){
  const h=['fármaco','familia','activación','base_act','sedación','base_sed','pro-monoaminérgico','base_ad','contención','base_am','área_u2','estado','efectos_asociados','motivo_o_dirección'];
  const q=s=>'"'+String(s??'').replace(/"/g,'""')+'"';
  return [h.join(',')].concat(m.map(c=>[q(c.drug),q(c.fam),...V161_AX.flatMap(k=>[c[k].v==null?'':c[k].v.toFixed(3),c[k].b]),c.area.toFixed(2),c.status,q((c.eff||[]).map(e=>e.lab+' ['+e.b+'] '+e.txt+(e.who?' (metabolito: '+e.who+')':'')).join(' | ')),q(c.reason||V161_AX.filter(k=>c[k].why).map(k=>V161_LBL[k]+' ← '+c[k].why).join(' | '))].join(','))).join('\n');
}
function v161MatrixHtml(){
  const m=v161Matrix(),f=V161.filter.toLowerCase(),b=V161.basis;
  const rows=m.filter(c=>(!f||(c.drug+' '+c.fam).toLowerCase().includes(f))&&(b==='todos'||c.status===b));
  const cnt=k=>m.filter(c=>c.status===k).length;
  const sum='<p class="small"><b>'+m.length+' fármacos.</b> Con área (≥ 1 componente numérico): '+cnt('area')+' · solo dirección cualitativa: '+cnt('direccion')+' · estabilizador (amortiguación): '+cnt('amortiguacion')+' · sin eje aplicable: '+cnt('sin-eje')+'. Dosis nominal del atlas para la capa O.</p>';
  const sel=['todos','area','direccion','amortiguacion','sin-eje'].map(v=>'<option value="'+v+'"'+(b===v?' selected':'')+'>'+({todos:'Todos',area:'Con área',direccion:'Solo dirección',amortiguacion:'Amortiguación',['sin-eje']:'Sin eje aplicable'})[v]+'</option>').join('');
  const body=rows.map(c=>'<tr><td><b>'+esc(c.drug)+'</b><br><small>'+esc(c.fam)+'</small></td>'+V161_AX.map(k=>'<td>'+v161Cell(c[k])+'</td>').join('')+'<td>'+(c.numeric?v161Area(c):'—')+'</td><td class="rs">'+v161EffHtml(c.eff)+'</td><td class="rs">'+esc(c.reason||V161_AX.filter(k=>c[k].why).map(k=>V161_LBL[k]+' ← '+c[k].why).join(' · '))+'</td></tr>').join('');
  return sum+'<div class="pdn-controls"><label>Buscar <input id="vecQ" type="search" value="'+esc(V161.filter)+'" placeholder="fármaco o familia"></label><label>Mostrar <select id="vecB">'+sel+'</select></label><button type="button" id="vecCsv">Exportar CSV</button></div>'
   +'<div class="tw"><table class="vec-table vec-matrix"><thead><tr><th>Fármaco</th><th>Activación</th><th>Sedación</th><th>Pro-monoaminérgico</th><th>Contención</th><th>Área u²</th><th>Efectos asociados</th><th>Base · motivo</th></tr></thead><tbody>'+body+'</tbody></table></div>'
   +'<p class="small"><b>Base:</b> O = cálculo operativo del atlas · P = afinidad documentada con dirección explícita (no operativa; efecto no inferible) · C = ordinal clínico/regulatorio con dirección explícita (magnitud ordinal del atlas, no afinidad) · Q = dirección cualitativa sin magnitud (inferencia de clase) · — = sin eje aplicable.</p>';
}

function vectorsView(a){
  const host=$('#vectors');if(!host)return;
  const rows=state.rows.filter(v140Active),inactive=state.rows.filter(r=>!v140Active(r)).map(r=>r.drug);
  const per=rows.map(r=>({r,c:v161Comp(r)})),pos=v160Position(),P=pos||{x:0,y:0};
  const U={};V161_AX.forEach(k=>U[k]=1-per.reduce((p,x)=>p*(1-v161Val(x.c,k)),1));
  const joint=v161Kite(P,U),jointArea=0.5*(U.act+U.sed)*(U.ad+U.am)*V161_S*V161_S;
  const net={x:(U.act-U.sed)*V161_S,y:(U.ad-U.am)*V161_S};
  const kites=per.map(x=>v161Kite(P,{act:v161Val(x.c,'act'),sed:v161Val(x.c,'sed'),ad:v161Val(x.c,'ad'),am:v161Val(x.c,'am')}));
  const all=[...joint,...kites.flat(),[P.x,P.y]];
  const ext=Math.max(...all.map(p=>Math.max(Math.abs(p[0]),Math.abs(p[1])))),R=ext<=4.2?5:Math.ceil(ext/5)*5;
  const sx=x=>500+Math.max(-R,Math.min(R,x))*(350/R),sy=y=>340-Math.max(-R,Math.min(R,y))*(260/R);
  const pts=ps=>ps.map(p=>sx(p[0]).toFixed(1)+','+sy(p[1]).toFixed(1)).join(' ');
  let svg='<svg class="vec-svg" viewBox="0 0 1000 700" role="img" aria-labelledby="vecT vecD"><title id="vecT">Áreas de los componentes de vector de la pauta</title><desc id="vecD">Plano con eje horizontal de sedación a activación y eje vertical de contención a empuje pro-monoaminérgico. Cada fármaco genera un polígono cuyos vértices son sus cuatro componentes; el polígono rayado es el área conjunta de la pauta. Los anillos discontinuos señalan estabilizadores y los segmentos punteados direcciones cualitativas sin magnitud.</desc>'
   +'<defs><pattern id="vecHatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="9" stroke="#000" stroke-width="1.5"/></pattern><marker id="vecArrow" markerUnits="userSpaceOnUse" viewBox="0 -8 14 16" markerWidth="14" markerHeight="16" refX="13" refY="0" orient="auto"><path d="M0,-6 L13,0 L0,6 Z" fill="#000"/></marker></defs>'
   +'<rect x="0" y="0" width="1000" height="700" fill="#fff"/><rect x="150" y="80" width="700" height="520" fill="#fff" stroke="#000" stroke-width="2"/>'
   +'<line x1="150" y1="340" x2="850" y2="340" stroke="#000" stroke-width="1.5"/><line x1="500" y1="80" x2="500" y2="600" stroke="#000" stroke-width="1.5"/>';
  const step=R===5?1:5;for(let u=-R+step;u<=R-step;u+=step){if(!u)continue;svg+='<line x1="'+sx(u)+'" y1="334" x2="'+sx(u)+'" y2="346" stroke="#000"/><line x1="494" y1="'+sy(u)+'" x2="506" y2="'+sy(u)+'" stroke="#000"/><text x="'+sx(u)+'" y="362" font-size="11" text-anchor="middle">'+u+'</text><text x="486" y="'+(sy(u)+4)+'" font-size="11" text-anchor="end">'+u+'</text>'}
  svg+='<text x="500" y="62" font-size="13" text-anchor="middle" font-weight="700">↑ EMPUJE PRO-MONOAMINÉRGICO (ad)</text><text x="500" y="626" font-size="13" text-anchor="middle" font-weight="700">↓ CONTENCIÓN (am)</text>'
   +'<text x="140" y="344" font-size="13" text-anchor="end" font-weight="700">◀ sedación (sed)</text><text x="860" y="344" font-size="13" font-weight="700">activación (act) ▶</text>'
   +'<text x="500" y="662" font-size="12" text-anchor="middle" fill="#222">Cada vértice = un componente (0–1 × '+V161_S+'). Escala del atlas, plano ±'+R+'; sin unidades clínicas.</text>';
  if(V161.show.joint&&per.length)svg+='<polygon points="'+pts(joint)+'" fill="url(#vecHatch)" stroke="#000" stroke-width="4"/>';
  if(V161.show.hull&&per.length){const h=v161Hull(all.slice(0,-1));if(h.length>2)svg+='<polygon points="'+pts(h)+'" fill="none" stroke="#000" stroke-width="1.6" stroke-dasharray="2 7"/>'}
  if(V161.show.kites)per.forEach((x,i)=>{
    if(!x.c.numeric)return;const k=kites[i],big=[['act',0],['ad',1],['sed',2],['am',3]].sort((p,q)=>v161Val(x.c,q[0])-v161Val(x.c,p[0]))[0][1],vx=sx(k[big][0]),vy=sy(k[big][1]),dx=vx>=500?14:-14,dy=vy>=340?14:-14;
    svg+='<polygon points="'+pts(k)+'" fill="#000" fill-opacity=".08" stroke="#000" stroke-width="2.4"'+(V161_DASH[i%6]?' stroke-dasharray="'+V161_DASH[i%6]+'"':'')+'/>'
      +'<rect x="'+(vx+dx-11)+'" y="'+(vy+dy-11)+'" width="22" height="22" fill="#fff" stroke="#000" stroke-width="'+(V161_AX.some(c=>x.c[c].b==='P'||x.c[c].b==='C')?'3.4':'1.8')+'"'+(V161_AX.some(c=>x.c[c].b==='C')&&!V161_AX.some(c=>x.c[c].b==='P')?' stroke-dasharray="4 2"':'')+'/><text x="'+(vx+dx)+'" y="'+(vy+dy+4.5)+'" font-size="13" font-weight="700" text-anchor="middle" style="stroke:none">'+(i+1)+'</text>';
  });
  if(V161.show.dir)per.forEach((x,i)=>{
    const off=(i%4)*.35,ends={act:[1,0],sed:[-1,0],ad:[0,1],am:[0,-1]};
    V161_AX.forEach(k=>{if(x.c[k].b!=='Q')return;const e=ends[k],x1=P.x+(e[1]?off:0),y1=P.y+(e[0]?off:0),x2=x1+e[0]*2.1,y2=y1+e[1]*2.1;
      svg+='<line x1="'+sx(x1)+'" y1="'+sy(y1)+'" x2="'+sx(x2)+'" y2="'+sy(y2)+'" stroke="#000" stroke-width="3" stroke-dasharray="1 5" stroke-linecap="round"/><circle cx="'+sx(x2)+'" cy="'+sy(y2)+'" r="8" fill="#fff" stroke="#000" stroke-width="1.6"/><text x="'+sx(x2)+'" y="'+(sy(y2)+4)+'" font-size="10.5" font-weight="700" text-anchor="middle" style="stroke:none">'+(i+1)+'</text>'});
  });
  if(V161.show.damp){let n=0;per.forEach((x,i)=>{if(!x.c.stab)return;const r=(1.3+.55*n++)*(350/R);svg+='<circle cx="'+sx(P.x)+'" cy="'+sy(P.y)+'" r="'+r+'" fill="none" stroke="#000" stroke-width="2" stroke-dasharray="3 6"/><text x="'+(sx(P.x)+r*.72)+'" y="'+(sy(P.y)-r*.72)+'" font-size="11.5" font-weight="700">≈ amortiguación · '+esc(x.r.drug)+'</text>'})}
  if(V161.show.net&&per.length)svg+='<line x1="'+sx(P.x)+'" y1="'+sy(P.y)+'" x2="'+sx(P.x+net.x)+'" y2="'+sy(P.y+net.y)+'" stroke="#000" stroke-width="4.5" stroke-dasharray="12 7" marker-end="url(#vecArrow)"/><text x="'+(sx(P.x+net.x)+10)+'" y="'+(sy(P.y+net.y)-10)+'" font-size="13" font-weight="700">vector neto del área</text>';
  svg+='<circle cx="'+sx(P.x)+'" cy="'+sy(P.y)+'" r="8" fill="#000"/><text x="'+(sx(P.x)-14)+'" y="'+(sy(P.y)-14)+'" font-size="12.5" font-weight="700" text-anchor="end">'+(pos?'estado declarado':'origen (sin estado declarado)')+'</text></svg>';
  const chk=(id,lab,on)=>'<label><input type="checkbox" data-vs="'+id+'"'+(on?' checked':'')+'> '+lab+'</label>';
  const trs=per.map((x,i)=>'<tr><td><b>'+(i+1)+'</b></td><td>'+esc(x.r.drug)+'</td><td>'+esc(v160DoseTxt(x.r))+'</td>'+V161_AX.map(k=>'<td>'+v161Cell(x.c[k])+'</td>').join('')+'<td>'+(x.c.numeric?v161Area(x.c):'—')+'</td><td class="rs">'+v161EffHtml(x.c.eff)+'</td><td class="rs">'+esc(x.c.reason||'')+'</td></tr>').join('');
  const ref=vectorProfile(a);
  const sum='<tr class="sumr"><td><b>Σ</b></td><td>Área conjunta (unión no lineal por componente)</td><td></td><td>'+U.act.toFixed(2)+'</td><td>'+U.sed.toFixed(2)+'</td><td>'+U.ad.toFixed(2)+'</td><td>'+U.am.toFixed(2)+'</td><td>'+jointArea.toFixed(1)+'</td><td></td><td class="rs">Balance heurístico de componentes (no es el centroide del área): ('+(net.x>=0?'+':'')+net.x.toFixed(1)+' ; '+(net.y>=0?'+':'')+net.y.toFixed(1)+'). Es la diferencia entre componentes opuestos, no la información completa.</td></tr>'
    +'<tr><td><b>Σ</b></td><td>Referencia: capa operativa del atlas (vectorProfile)</td><td></td><td>'+ref.act.toFixed(2)+'</td><td>'+ref.sed.toFixed(2)+'</td><td>'+ref.ad.toFixed(2)+'</td><td>'+ref.am.toFixed(2)+'</td><td>'+(0.5*(ref.act+ref.sed)*(ref.ad+ref.am)*V161_S*V161_S).toFixed(1)+'</td><td></td><td class="rs">Capa O, con las dianas agregadas y la política anti/pro de v16.1: antagonismo H1 (principal), M1 y α1 (secundarios) → sedación; agonismo H1/α1 → activación; agonismo M1 → contención. Las capas P y C solo rellenan un eje cuando O no lo cubre.</td></tr>';
  const hi=pos?Object.entries(state.dims).filter(([k,v])=>pos.used.includes(k)&&v>=7).map(([k,v])=>k+' '+v+'/10'):[];
  host.innerHTML='<div class="panel"><h2>Vectores clínicos · áreas de los cuatro componentes</h2>'
   +'<p class="pdn-lead">Cada fármaco aporta cuatro componentes (activación, sedación, empuje pro-monoaminérgico y contención). En lugar de reducirlos a una flecha, se dibujan como un <b>polígono</b> cuyo tamaño y forma muestran el perfil completo; el <b>área conjunta</b> de la pauta se obtiene por unión no lineal de cada componente.</p>'
   +'<div class="pdn-controls vec-toggles" role="group" aria-label="Capas de la figura">'+chk('kites','Áreas por fármaco',V161.show.kites)+chk('joint','Área conjunta',V161.show.joint)+chk('hull','Envolvente',V161.show.hull)+chk('net','Vector neto',V161.show.net)+chk('dir','Direcciones cualitativas (Q)',V161.show.dir)+chk('damp','Amortiguación',V161.show.damp)+chk('layerO','Capa O · operativa',V161.show.layerO)+chk('layerP','Capa P · afinidad documentada',V161.show.layerP)+chk('layerC','Capa C · ordinal clínico',V161.show.layerC)+'</div>'
   +(rows.length?'<div class="pdn-svgwrap">'+svg+'</div>':'<div class="pdn-note">No hay componentes con dosis. Añade fármacos y dosis en «Pauta a explorar».</div>')
   +'<div class="pdn-legend vec-legend" aria-label="Leyenda"><span class="lg"><svg viewBox="0 0 64 20"><polygon points="32,2 62,10 32,18 4,10" fill="#000" fill-opacity=".08" stroke="#000" stroke-width="2" stroke-dasharray="9 4"/></svg>Área del fármaco (n.º en recuadro)</span><span class="lg"><svg viewBox="0 0 64 20"><polygon points="32,2 62,10 32,18 4,10" fill="url(#vecHatch)" stroke="#000" stroke-width="3"/></svg>Área conjunta</span><span class="lg"><svg viewBox="0 0 64 20"><rect x="22" y="3" width="18" height="14" fill="#fff" stroke="#000" stroke-width="3.4"/></svg>Recuadro grueso = componente de capa P (discontinuo: C)</span><span class="lg"><svg viewBox="0 0 64 20"><line x1="4" y1="10" x2="52" y2="10" stroke="#000" stroke-width="3" stroke-dasharray="1 5" stroke-linecap="round"/><circle cx="56" cy="10" r="6" fill="#fff" stroke="#000" stroke-width="1.6"/></svg>Dirección sin magnitud (Q)</span><span class="lg"><svg viewBox="0 0 64 20"><circle cx="32" cy="10" r="8" fill="none" stroke="#000" stroke-width="2" stroke-dasharray="3 5"/></svg>Amortiguación (radio simbólico)</span></div>'
   +'<h3>Componentes de la pauta</h3>'+(rows.length?'<div class="tw"><table class="vec-table"><thead><tr><th>#</th><th>Fármaco</th><th>Dosis</th><th>Activación</th><th>Sedación</th><th>Pro-monoaminérgico</th><th>Contención</th><th>Área u²</th><th>Efectos asociados</th><th>Nota</th></tr></thead><tbody>'+trs+sum+'</tbody></table></div>':'')
   +(inactive.length?'<p class="small"><b>Sin dosis (excluidos de la figura):</b> '+esc(inactive.join(', '))+'.</p>':'')
   +'<div class="vec-card"><h4>Estado declarado</h4>'+(pos?'<p>Posición calculada solo con las dimensiones que la lente aplica ('+pos.used.length+'): <b>('+(pos.x>=0?'+':'')+pos.x.toFixed(1)+' ; '+(pos.y>=0?'+':'')+pos.y.toFixed(1)+')</b>.'+(hi.length?' Dimensiones ≥ 7: '+esc(hi.join(', '))+'.':'')+'</p><details class="vec-formula"><summary>Cómo se calcula</summary><p>Vertical = 1,2 × (media de mixticidad, síntomas positivos, desorganización, impulsividad y activación − media de depresión, anhedonia y síntomas negativos). Horizontal = 1,2 × (media de activación, impulsividad, ansiedad e insomnio − media de somnolencia diurna, depresión y anhedonia). Solo entran las dimensiones disponibles en la lente. Heurística editorial: no es una escala validada ni se deriva de la pauta.</p></details>':'<p>La lente actual no aplica contexto clínico declarado: las áreas parten del origen y describen solo el perfil receptorial. Elige una lente clínica para situar un estado declarado.</p>')+'</div>'
   +'<details class="vec-all" id="vecAll"><summary>Matriz completa · componentes de los 167 fármacos del atlas</summary><div id="vecAllBody"><p class="small">Pulsa para calcular.</p></div></details>'
   +'<p class="small">Lectura exploratoria. O = cálculo operativo del atlas; P = afinidad documentada con dirección explícita, no operativa (Ki ≠ ocupación ≠ respuesta); C = ordinal clínico/regulatorio con dirección explícita; Q = dirección cualitativa por inferencia de clase, sin magnitud. Un área no es eficacia ni cobertura terapéutica.</p></div>';
  host.querySelectorAll('[data-vs]').forEach(el=>el.onchange=()=>{V161.show[el.dataset.vs]=el.checked;vectorsView(a)});
  const det=$('#vecAll');
  const fill=()=>{const body=$('#vecAllBody');body.innerHTML=v161MatrixHtml();const q=$('#vecQ'),b=$('#vecB');q.oninput=()=>{V161.filter=q.value;const pos=q.selectionStart;fill();const nq=$('#vecQ');nq.focus();nq.setSelectionRange(pos,pos)};b.onchange=()=>{V161.basis=b.value;fill()};$('#vecCsv').onclick=()=>{const blob=new Blob(['﻿'+v161Csv(v161Matrix())],{type:'text/csv;charset=utf-8'}),u=URL.createObjectURL(blob),l=document.createElement('a');l.href=u;l.download='atlas_vectores_componentes_v16.1.csv';document.body.appendChild(l);l.click();l.remove();setTimeout(()=>URL.revokeObjectURL(u),500)}};
  det.ontoggle=()=>{if(det.open)fill()};if(det.open)fill();
}

/* ===== Figuras: panel de pauta plegable, zoom, pantalla completa ===== */
const V161_FIGS=[['#receptor svg.receptor-tree','receptor'],['#fount svg.fount-map','fount'],['#supplement .cm-canvas svg','supplement'],['#psychosis svg','psychosis'],['#polarity svg.clinical-map','polarity'],['#trajectory svg.landscape','trajectory'],['#pdnet svg.pdn-svg','pdnet'],['#vectors svg.vec-svg','vectors']];
const V161_FIGVIEWS=new Set(['receptor','fount','supplement','psychosis','polarity','trajectory','pdnet','vectors']);
const V161Z={};let v161Manual=false;
try{Object.assign(V161Z,JSON.parse(localStorage.getItem('atlas-fig-zoom')||'{}'))}catch(e){}
function v161SaveZ(){try{localStorage.setItem('atlas-fig-zoom',JSON.stringify(V161Z))}catch(e){}}
function v161AutoZoom(svg,wrap){
  const vb=svg.viewBox.baseVal;if(!vb||!vb.width)return 1;
  const sz=[...svg.querySelectorAll('text')].map(t=>parseFloat(t.getAttribute('font-size'))||0).filter(x=>x>0).sort((a,b)=>a-b);if(!sz.length)return 1;
  const med=sz[Math.floor(sz.length/2)],need=(10/med)*vb.width,w=Math.max(300,wrap.clientWidth||svg.parentElement.clientWidth||800);
  return Math.max(1,Math.min(1.5,need/w));
}
function v161ApplyZ(wrap,svg,id){const z=V161Z[id]||v161AutoZoom(svg,wrap);wrap.dataset.z=z;svg.style.width=(z*100)+'%';svg.style.maxWidth='none';svg.style.minWidth='0';const o=wrap.querySelector('output');if(o)o.textContent=Math.round(z*100)+' %'}
function v161Figures(){
  v161SyncOpen();
  V161_FIGS.forEach(([sel,id])=>document.querySelectorAll(sel).forEach(svg=>{
    if(svg.closest('.fig-scroll'))return;
    const wrap=document.createElement('div');wrap.className='fig-scroll';wrap.dataset.fig=id;
    svg.parentNode.insertBefore(wrap,svg);wrap.appendChild(svg);
    const bar=document.createElement('div');bar.className='fig-bar';bar.innerHTML='<span class="fig-t">Figura</span><button type="button" data-z="-" aria-label="Reducir figura">−</button><output aria-live="polite">100 %</output><button type="button" data-z="+" aria-label="Ampliar figura">+</button><button type="button" data-z="0">Ajustar</button><button type="button" data-z="full" aria-pressed="false">⤢ Pantalla completa</button>';
    wrap.insertBefore(bar,svg);
    bar.addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;const k=b.dataset.z,cur=+wrap.dataset.z||1;
      if(k==='-'||k==='+'){V161Z[id]=Math.max(.7,Math.min(3,cur+(k==='+'?.2:-.2)));v161SaveZ();v161ApplyZ(wrap,svg,id)}
      else if(k==='0'){delete V161Z[id];v161SaveZ();v161ApplyZ(wrap,svg,id)}
      else if(k==='full'){const on=wrap.classList.toggle('fig-full');document.body.classList.toggle('fig-open',on);b.setAttribute('aria-pressed',on?'true':'false');b.textContent=on?'✕ Cerrar':'⤢ Pantalla completa';if(on&&!V161Z[id])v161ApplyZ(wrap,svg,id)}});
    v161ApplyZ(wrap,svg,id);
  }));
}
function v161SyncOpen(){document.body.classList.toggle('fig-open',!!document.querySelector('.fig-scroll.fig-full'))}
document.addEventListener('keydown',e=>{if(e.key==='Escape'){const f=document.querySelector('.fig-scroll.fig-full');if(f){f.querySelector('[data-z="full"]').click()}}});
function v161SetAside(hidden,manual){
  if(manual)v161Manual=true;document.body.classList.toggle('pauta-oculta',hidden);
  const b=$('#toggleAside');if(b){b.setAttribute('aria-pressed',hidden?'true':'false');b.textContent=hidden?'☰ Mostrar panel de pauta':'☰ Ocultar panel de pauta'}
  setTimeout(()=>document.querySelectorAll('.fig-scroll').forEach(w=>{const s=w.querySelector('svg');if(s&&!V161Z[w.dataset.fig])v161ApplyZ(w,s,w.dataset.fig)}),30);
}

/* Nodos de los mapas heredados: relleno claro, borde y texto negros (la forma sigue codificando el sistema) */
function v161Nodes(){
  document.querySelectorAll('.workspace svg:not(.pdn-svg):not(.vec-svg) text[fill="#fff"],.workspace svg:not(.pdn-svg):not(.vec-svg) text[fill="#ffffff"]').forEach(t=>{
    const g=t.parentNode;if(!g||String(g.tagName).toLowerCase()!=='g'||t.classList.contains('eink-nt')||g.closest('#polarity,#trajectory'))return;
    t.classList.add('eink-nt');
    g.querySelectorAll(':scope>path,:scope>circle,:scope>ellipse,:scope>rect,:scope>polygon').forEach(s=>{const f=s.getAttribute('fill');if(f&&f!=='none'&&!f.startsWith('url'))s.classList.add('eink-node')})
  });
}
/* ===== Avisos heredados: se ocultan los que no tienen función; reversible ===== */
const V161_LEGACY=[
  ['#fount','.v138-frame-note',null],
  ['#fount','.notice',/^Núcleo: conserva la geometría/],
  ['#pk','.notice',/^Límite del modelo/],
  ['#polarity','.notice',/^La mixticidad se representa/],
  ['#psychosis','.notice',/^Límite: un receptor/],
  ['#report','.notice',/^No es una recomendación/],
  ['#design','.notice',/^No genera una prescripción/],
  ['#evidence,#catalog','.notice',/^(Regla de esta tanda|Consecuencia visual|Cierre de cola|Histórico v|Revisión dirigida v|Primera tanda|Reglas preservadas|Seis perfiles|11 perfiles|15 perfiles|16 de los|90\/167|\d+ perfiles)/],
];
function v161Legacy(){
  let n=0;
  V161_LEGACY.forEach(([views,sel,re])=>views.split(',').forEach(v=>document.querySelectorAll(v+' '+sel).forEach(el=>{
    if(re&&!re.test(el.innerText.trim()))return;el.classList.add('legacy-notice');n++})));
  document.querySelectorAll('#receptor .direct-study-note details[open],#fount .direct-study-note details[open],#receptor .molecular-only-note details[open],#fount .molecular-only-note details[open]').forEach(d=>{if(!d.dataset.closed){d.dataset.closed='1';d.open=false}});
  const c=$('#legacyCount');if(c)c.textContent=document.querySelectorAll('.legacy-notice').length;
}
function v161Tools(){
  if($('#viewTools'))return;const g=document.querySelector('.grid');if(!g)return;
  g.insertAdjacentHTML('beforebegin','<div id="viewTools" class="view-tools" role="group" aria-label="Opciones de visualización"><button type="button" id="toggleAside" aria-pressed="false">☰ Ocultar panel de pauta</button><label class="legacy-sw"><input type="checkbox" id="toggleLegacy"><span>Mostrar avisos heredados (<b id="legacyCount">0</b> ocultos)</span></label></div>');
  const ac=$('#atlasContext'),ab=$('#mapComparisonControls');
  if(ac&&ab&&!$('#ctxFold')){const d=document.createElement('details');d.id='ctxFold';d.className='ctx-fold';d.innerHTML='<summary>Contexto de lectura, pauta representada y comparación A → B</summary>';ac.parentNode.insertBefore(d,ac);d.appendChild(ac);d.appendChild(ab)}
  $('#toggleAside').onclick=()=>v161SetAside(!document.body.classList.contains('pauta-oculta'),true);
  $('#toggleLegacy').onchange=e=>document.body.classList.toggle('show-legacy',e.target.checked);
}
const activateViewBaseV161=activateView;
activateView=function(view,writeUrl=true){v161Tools();if(!v161Manual)v161SetAside(V161_FIGVIEWS.has(view),false);activateViewBaseV161(view,writeUrl);v161Figures();v161Nodes();v161Legacy()};
const evaluateBaseV161=evaluate;
evaluate=function(){evaluateBaseV161();v161Figures();v161Nodes();v161Legacy()};
(function(){let t=null;const run=()=>{t=null;v161Figures();v161Nodes();v161Legacy()};
  const start=()=>{const w=document.querySelector('.workspace');if(!w){setTimeout(start,50);return}new MutationObserver(()=>{if(t)return;t=requestAnimationFrame(run)}).observe(w,{childList:true,subtree:true})};start()})();

/* ===== v16.0 · Red farmacodinámica y vectores clínicos =====
   Se alimentan de aggregate() y vectorProfile() del propio atlas; no añaden pesos ni dianas nuevas.
   Lectura exploratoria: potencia 0–10 de la escala del atlas; Ki ≠ exposición cerebral ≠ ocupación ≠ respuesta. */
const V160={thr:5,onlyConv:false};
const V160_SYS=['Serotonina','Dopamina','Adrenérgico','Histamina','Muscarínico','Transportador','Enzima','Glutamato','Opioide','Melatonina','Vesicular','Otras'];
const V160_LBL={ant:'Antagonismo / bloqueo',inv:'Agonismo inverso',inh:'Inhibición (transportador o enzima)',pag:'Agonismo parcial',ag:'Agonismo',mod:'Modulación, señal indirecta u ordinal',low:'Afinidad muy baja'};
const V160_DASH={ant:'',inv:'10 3 2 3',inh:'',pag:'7 4',ag:'',mod:'2 4',low:'2 4'};
const V160_CAP={ant:'pdnBar',inv:'pdnBar',inh:'pdnSq',pag:'pdnOpen',ag:'pdnArrow',mod:'pdnDot',low:'pdnDot'};

function v160Class(action){
  const s=String(action||'').toLowerCase().trim();
  if(/^(muy )?baja\b|^nula|^m[ií]nima|exploratorio/.test(s))return 'low';
  if(/inverso/.test(s))return 'inv';
  if(/antagon|bloque/.test(s))return 'ant';
  if(/parcial/.test(s))return 'pag';
  if(/inhib|captaci|recaptaci/.test(s))return 'inh';
  if(/agonis|agonista|facilit|apertura/.test(s))return 'ag';
  return 'mod';
}
function v160Target(t){const m=TARGET_META[t];return {label:m?m[0]:t,sys:m?m[1]:'Otras'}}
function v160Edges(a){
  const best={};
  Object.entries(a).forEach(([t,x])=>(x.contrib||[]).forEach(c=>{
    if(c.petEligible)return;
    const ord=c.evidence==='esqueleto ordinal'||c.potencyEligible===false,qual=!!c.qualitative;
    const pot=(ord||qual)?null:(Number(c.potencyValue)||0);
    const e={t,entity:c.entity||c.drug,parent:c.drug,meta:c.entityType==='metabolite',comp:c.entityType==='component',cls:v160Class(c.action),pot,ord,qual,action:c.action||'',evidence:c.evidence||'',metric:c.metric||''};
    const k=e.parent+'|'+e.entity+'|'+t,old=best[k];
    if(!old||(e.pot||0)>(old.pot||0))best[k]=e;
  }));
  return Object.values(best);
}
function v160Flags(list){
  const parents=new Set(list.map(e=>e.parent)),cls=new Set(list.map(e=>e.cls));
  const block=['ant','inv','inh'].filter(c=>cls.has(c)).length>0,stim=['ag','pag'].filter(c=>cls.has(c)).length>0;
  let opp='';
  list.forEach(e1=>list.forEach(e2=>{if(['ant','inv'].includes(e1.cls)&&['ag','pag'].includes(e2.cls)&&e1.entity!==e2.entity){opp=e1.parent!==e2.parent?'compet':(opp||'mixto')}}));
  const conv=parents.size>=2;
  let text='',kind='';
  if(opp==='compet'){kind='compet';text='⇄ Competencia: acciones opuestas'}
  else if(opp==='mixto'){kind='mixto';text='≈ Señal mixta fármaco/metabolito'}
  else if(conv&&block&&!stim){kind='conv';text='▣ Suma de bloqueo'}
  else if(conv&&stim&&!block){kind='conv';text='▣ Suma de agonismo'}
  else if(conv){kind='conv';text='▣ Convergencia'}
  return {kind,text,conv,parents:parents.size};
}
function v160Fmt(n){return (Math.round(n*10)/10).toFixed(1)}

function pdnet(a){
  const host=$('#pdnet');if(!host)return;
  const rows=state.rows.filter(v140Active),inactive=state.rows.filter(r=>!v140Active(r)).map(r=>r.drug);
  const thr=V160.thr;
  let edges=v160Edges(a).filter(e=>rows.some(r=>r.drug===e.parent)).filter(e=>e.ord||e.qual||(thr===0)||(e.cls!=='low'&&e.pot>=thr));
  const byT={};edges.forEach(e=>(byT[e.t]=byT[e.t]||[]).push(e));
  const flags={};Object.entries(byT).forEach(([t,l])=>flags[t]=v160Flags(l));
  if(V160.onlyConv){Object.keys(byT).forEach(t=>{if(!flags[t].kind){delete byT[t];delete flags[t]}});edges=edges.filter(e=>byT[e.t])}
  // entidades (fármaco y metabolitos) en orden de la pauta
  const ents=[];
  rows.forEach(r=>{ents.push({entity:r.drug,parent:r.drug,meta:false,row:r});[...new Set(edges.filter(e=>e.parent===r.drug&&e.comp&&e.entity!==r.drug).map(e=>e.entity))].forEach(n=>ents.push({entity:n,parent:r.drug,meta:false,comp:true,row:r}));[...new Set(edges.filter(e=>e.parent===r.drug&&e.meta).map(e=>e.entity))].forEach(n=>ents.push({entity:n,parent:r.drug,meta:true,row:r}))});
  const ek=e=>e.parent+'|'+e.entity,entIdx={};ents.forEach((e,i)=>entIdx[ek(e)]=i);
  // dianas agrupadas por sistema, ordenadas por baricentro
  const sysOf=t=>v160Target(t).sys,groups={};
  Object.keys(byT).forEach(t=>{const s=sysOf(t);(groups[s]=groups[s]||[]).push(t)});
  const bc=t=>byT[t].reduce((s,e)=>s+(entIdx[ek(e)]??0),0)/byT[t].length;
  const order=[...V160_SYS.filter(s=>groups[s]),...Object.keys(groups).filter(s=>!V160_SYS.includes(s))];
  const LX=24,LW=290,RX=830,RW=246,W=1100,TOP=70;
  let y=TOP;const tpos={},heads=[];
  order.forEach(s=>{heads.push({s,y});y+=24;groups[s].sort((p,q)=>bc(p)-bc(q)).forEach(t=>{tpos[t]=y+12;y+=26});y+=10});
  const rightH=y;
  const hs=ents.map(e=>e.meta||e.comp?44:62),sumH=hs.reduce((p,q)=>p+q,0),H=Math.max(rightH,sumH+TOP+ents.length*14)+10;
  const gap=ents.length?Math.max(12,(H-TOP-10-sumH)/Math.max(1,ents.length)):0;
  let ly=TOP;const npos=ents.map((e,i)=>{const o={y:ly,h:hs[i],cy:ly+hs[i]/2};ly+=hs[i]+gap;return o});
  const cnt={};edges.forEach(e=>cnt[ek(e)]=(cnt[ek(e)]||0)+1);
  let svg='<svg class="pdn-svg" viewBox="0 0 '+W+' '+H+'" role="img" aria-labelledby="pdnT pdnD"><title id="pdnT">Red farmacodinámica de la pauta</title><desc id="pdnD">Cada fármaco de la pauta se une a las dianas donde el atlas tiene datos. El tipo de línea y su remate indican la acción; el grosor, la potencia en la escala 0–10 del atlas. Las dianas con doble borde reciben acción de varios fármacos; las de borde discontinuo reciben acciones opuestas.</desc>'
   +'<defs>'
   +'<marker id="pdnBar" markerUnits="userSpaceOnUse" viewBox="0 -8 12 16" markerWidth="12" markerHeight="16" refX="10" refY="0" orient="auto"><path d="M10,-7 L10,7" stroke="#000" stroke-width="3" fill="none"/></marker>'
   +'<marker id="pdnSq" markerUnits="userSpaceOnUse" viewBox="0 -8 12 16" markerWidth="12" markerHeight="16" refX="11" refY="0" orient="auto"><rect x="3" y="-5" width="9" height="10" fill="#000"/></marker>'
   +'<marker id="pdnArrow" markerUnits="userSpaceOnUse" viewBox="0 -8 14 16" markerWidth="14" markerHeight="16" refX="13" refY="0" orient="auto"><path d="M0,-6 L13,0 L0,6 Z" fill="#000"/></marker>'
   +'<marker id="pdnOpen" markerUnits="userSpaceOnUse" viewBox="0 -8 14 16" markerWidth="14" markerHeight="16" refX="13" refY="0" orient="auto"><path d="M1,-6 L13,0 L1,6 Z" fill="#fff" stroke="#000" stroke-width="1.8"/></marker>'
   +'<marker id="pdnDot" markerUnits="userSpaceOnUse" viewBox="0 -8 12 16" markerWidth="12" markerHeight="16" refX="10" refY="0" orient="auto"><circle cx="6" cy="0" r="4" fill="#fff" stroke="#000" stroke-width="1.8"/></marker></defs>'
   +'<rect x="0" y="0" width="'+W+'" height="'+H+'" fill="#fff"/>'
   +'<text x="'+LX+'" y="30" font-size="12.5" font-weight="700" letter-spacing="1.2">FÁRMACOS Y METABOLITOS</text><text x="'+RX+'" y="30" font-size="12.5" font-weight="700" letter-spacing="1.2">DIANAS POR SISTEMA</text>'
   +'<text x="'+LX+'" y="48" font-size="11.5" fill="#222">Grosor = potencia 0–10 del atlas · sin dosis ni exposición</text>';
  heads.forEach(h=>{svg+='<line x1="'+RX+'" y1="'+(h.y+4)+'" x2="'+(RX+RW)+'" y2="'+(h.y+4)+'" stroke="#000" stroke-width="1.2"/><text x="'+RX+'" y="'+(h.y+19)+'" font-size="11.5" font-weight="700" letter-spacing="1">'+esc(h.s.toUpperCase())+'</text>'});
  // aristas
  edges.forEach(e=>{
    const i=entIdx[ek(e)];if(i==null||tpos[e.t]==null)return;
    const x1=LX+LW,y1=npos[i].cy,x2=RX-7,y2=tpos[e.t],mx=(x1+x2)/2,w=(e.ord||e.qual)?1.5:(1.2+Math.max(0,Math.min(10,e.pot))/10*3.4);
    svg+='<path d="M'+x1+','+y1+' C'+(mx+60)+','+y1+' '+(mx-60)+','+y2+' '+x2+','+y2+'" fill="none" stroke="#000" stroke-width="'+w.toFixed(2)+'"'+((e.ord||e.qual)?' stroke-dasharray="'+V160_DASH.mod+'"':(V160_DASH[e.cls]?' stroke-dasharray="'+V160_DASH[e.cls]+'"':''))+' marker-end="url(#'+V160_CAP[e.cls]+')"><title>'+esc(e.entity+' → '+v160Target(e.t).label+' · '+e.action+(e.pot!=null?' · potencia '+v160Fmt(e.pot)+'/10':' · sin magnitud (ordinal o cualitativo)')+(e.evidence?' · '+e.evidence:''))+'</title></path>';
  });
  // nodos fármaco
  ents.forEach((e,i)=>{
    const p=npos[i],d=DRUGS[e.entity]||DRUGS[e.parent]||{},n=cnt[ek(e)]||0,x=LX+(e.meta||e.comp?22:0),w=LW-(e.meta||e.comp?22:0);
    svg+='<rect x="'+x+'" y="'+p.y+'" width="'+w+'" height="'+p.h+'" fill="#fff" stroke="#000" stroke-width="'+(e.meta||e.comp?1.5:2.4)+'"'+(e.meta||e.comp?' stroke-dasharray="5 3"':'')+'/>'
      +'<text x="'+(x+12)+'" y="'+(p.y+(e.meta||e.comp?19:24))+'" font-size="'+(e.meta||e.comp?12.5:15)+'" font-weight="700">'+esc((e.meta?'m · ':e.comp?'c · ':'')+e.entity)+'</text>';
    if(e.comp){
      svg+='<text x="'+(x+12)+'" y="'+(p.y+35)+'" font-size="11">'+esc('componente de '+e.parent+' · '+n+' diana'+(n===1?'':'s'))+'</text>';
    }else if(!e.meta){
      svg+='<text x="'+(x+12)+'" y="'+(p.y+42)+'" font-size="12">'+esc((e.row.dose!==''&&e.row.dose!=null?e.row.dose+' mg':'dosis por definir')+' · '+n+' diana'+(n===1?'':'s')+' con este umbral')+'</text>';
      if(!n&&d.mech)svg+='<text x="'+(x+12)+'" y="'+(p.y+57)+'" font-size="10.5" fill="#222">'+esc(String(d.mech).slice(0,52))+'…</text>';
    }else{
      svg+='<text x="'+(x+12)+'" y="'+(p.y+35)+'" font-size="11">'+esc('metabolito de '+e.parent+' · '+n+' diana'+(n===1?'':'s'))+'</text>';
    }
  });
  // nodos diana
  Object.entries(tpos).forEach(([t,ty])=>{
    const f=flags[t],lab=v160Target(t).label,h=22,y0=ty-h/2;
    svg+='<rect x="'+RX+'" y="'+y0+'" width="'+RW+'" height="'+h+'" fill="#fff" stroke="#000" stroke-width="'+(f.kind==='compet'?2.8:1.6)+'"'+(f.kind==='compet'?' stroke-dasharray="6 3"':'')+'/>';
    if(f.conv)svg+='<rect x="'+(RX+3)+'" y="'+(y0+3)+'" width="'+(RW-6)+'" height="'+(h-6)+'" fill="none" stroke="#000" stroke-width="1"/>';
    svg+='<text x="'+(RX+9)+'" y="'+(ty+4.5)+'" font-size="13" font-weight="700">'+esc(lab)+'</text>'
      +(f.kind?'<text x="'+(RX+RW-8)+'" y="'+(ty+4.5)+'" font-size="12" font-weight="700" text-anchor="end">'+(f.kind==='compet'?'⇄':f.kind==='mixto'?'≈':'▣')+(f.parents>1?' ×'+f.parents:'')+'</text>':'');
  });
  svg+='</svg>';
  // listas de lectura
  const listFlag=k=>Object.entries(flags).filter(([t,f])=>f.kind===k).map(([t])=>v160Target(t).label);
  const comp=listFlag('compet'),mix=listFlag('mixto'),conv=listFlag('conv');
  const noData=ents.filter(e=>!e.meta&&!e.comp&&!(cnt[ek(e)]||0)).map(e=>e.entity);
  const li=xs=>xs.length?'<ul>'+xs.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul>':'<p class="small">Ninguna con este umbral.</p>';
  const cards='<div class="pdn-flags">'
    +'<div class="pdn-card"><h4>⇄ Competencia entre fármacos</h4>'+li(comp)+'<p class="small">Acciones opuestas (bloqueo frente a agonismo) sobre la misma diana: el efecto neto no se infiere de la afinidad.</p></div>'
    +'<div class="pdn-card"><h4>▣ Convergencia</h4>'+li(conv)+'<p class="small">Dos o más fármacos actúan sobre la misma diana en el mismo sentido: la superposición no es lineal.</p></div>'
    +'<div class="pdn-card"><h4>Sin dianas con este umbral</h4>'+(noData.length?'<ul>'+noData.map(n=>'<li><b>'+esc(n)+'</b>'+(DRUGS[n]?.mech?': '+esc(String(DRUGS[n].mech).slice(0,150)):'')+'</li>').join('')+'</ul><p class="small">Sin edge no significa sin efecto: el mecanismo puede ser no receptorial, estar sin Ki en el atlas o quedar bajo el umbral.</p>':'<p class="small">Todos los componentes tienen al menos una diana.</p>')+(inactive.length?'<p class="small"><b>Sin dosis (excluidos):</b> '+esc(inactive.join(', '))+'</p>':'')+'</div></div>';
  const legendItems=['ant','inh','pag','ag','mod'].map(c=>'<span class="lg"><svg viewBox="0 0 64 16"><path d="M2,8 L'+(c==='ant'||c==='inh'?'52':'50')+',8" fill="none" stroke="#000" stroke-width="2.4"'+(V160_DASH[c]?' stroke-dasharray="'+V160_DASH[c]+'"':'')+' marker-end="url(#'+V160_CAP[c]+')"/></svg>'+esc(V160_LBL[c])+'</span>').join('');
  const legend='<div class="pdn-legend" aria-label="Leyenda de acciones">'+legendItems+'<span class="lg"><b>▣ ×n</b> convergencia (doble borde)</span><span class="lg"><b>⇄</b> competencia (borde discontinuo)</span><span class="lg"><b>m ·</b> metabolito</span></div>';
  // tabla textual equivalente
  const trows=order.flatMap(s=>groups[s].map(t=>{const f=flags[t],l=byT[t];return '<tr><td><b>'+esc(v160Target(t).label)+'</b></td><td>'+esc(s)+'</td><td>'+l.map(e=>esc(e.entity)+': '+esc(e.action||'—')+(e.pot!=null?' · '+v160Fmt(e.pot)+'/10':' · sin magnitud')+(e.evidence?' ('+esc(e.evidence)+')':'')).join('<br>')+'</td><td class="flag">'+esc(f.text||'—')+'</td></tr>'}));
  const table='<details open><summary>Tabla equivalente del grafo (accesible, sin depender del dibujo)</summary><div class="tw"><table class="pdn-table"><thead><tr><th>Diana</th><th>Sistema</th><th>Fármacos · acción · potencia 0–10</th><th>Lectura</th></tr></thead><tbody>'+(trows.join('')||'<tr><td colspan="4">Sin dianas con este umbral.</td></tr>')+'</tbody></table></div></details>';
  const sel=v=>'<option value="'+v[0]+'"'+(V160.thr===v[0]?' selected':'')+'>'+v[1]+'</option>';
  host.innerHTML='<div class="panel"><h2>Red farmacodinámica · fármacos, dianas, convergencias y competencias</h2>'
    +'<p class="pdn-lead">Grafo fármaco–diana construido con los datos que el atlas ya tiene para la pauta seleccionada. Muestra <b>dónde coinciden y dónde compiten</b> los componentes; no estima ocupación, exposición cerebral ni respuesta clínica.</p>'
    +'<div class="pdn-controls"><label>Potencia mínima <select id="pdnThr">'+[[7,'alta · ≥ 7'],[5,'media · ≥ 5'],[3,'baja · ≥ 3'],[0,'todas']].map(sel).join('')+'</select></label>'
    +'<label><input type="checkbox" id="pdnConv"'+(V160.onlyConv?' checked':'')+'> Solo dianas con convergencia o competencia</label>'
    +'<button type="button" id="pdnMet" class="entity-toggle'+(state.metabolites?' active':'')+'" aria-pressed="'+(state.metabolites?'true':'false')+'">Incluir metabolitos</button></div>'
    +(rows.length?cards+'<div class="pdn-svgwrap">'+svg+'</div>'+legend+table:'<div class="pdn-note">No hay componentes con dosis. Añade fármacos y dosis en «Pauta a explorar».</div>')
    +'<p class="small">Potencia: escala 0–10 del atlas (menor concentración de unión, mayor valor). Línea punteada: dato ordinal o cualitativo sin magnitud. Ki ≠ ocupación ≠ respuesta.</p></div>';
  const thrSel=$('#pdnThr');if(thrSel)thrSel.onchange=()=>{V160.thr=+thrSel.value;pdnet(a)};
  const cv=$('#pdnConv');if(cv)cv.onchange=()=>{V160.onlyConv=cv.checked;pdnet(a)};
  const mt=$('#pdnMet');if(mt)mt.onclick=()=>{state.metabolites=!state.metabolites;evaluate()};
}

/* ----- Vectores clínicos ----- */
function v160Position(){
  const cfg=(typeof lensConfig==='function'?lensConfig():null),avail=new Set((cfg&&cfg.dims)||[]);
  if(!avail.size)return null;
  const mean=ks=>{const v=ks.filter(k=>avail.has(k)).map(k=>+state.dims[k]||0);return v.length?v.reduce((p,q)=>p+q,0)/v.length:null};
  const exc=mean(['mixticidad','síntomas positivos','desorganización','impulsividad','activación']),def=mean(['depresión','anhedonia','síntomas negativos']);
  const act=mean(['activación','impulsividad','ansiedad','insomnio']),inh=mean(['somnolencia diurna','depresión','anhedonia']);
  const cl=v=>Math.max(-10,Math.min(10,v));
  return {x:cl(((act??0)-(inh??0))*1.2),y:cl(((exc??0)-(def??0))*1.2),used:[...avail]};
}
function v160Render(){const a=aggregate();pdnet(a);vectorsView(a)}
const evaluateBaseV160=evaluate;
evaluate=function(){evaluateBaseV160();v160Render()};
const activateViewBaseV160=activateView;
activateView=function(view,writeUrl=true){if(view==='pdnet'||view==='vectors')v160Render();activateViewBaseV160(view,writeUrl)};

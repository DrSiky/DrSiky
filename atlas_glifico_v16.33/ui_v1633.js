/* v16.33 · Interfaz centrada en los atlas por indicación y mecanismo.
   - Indicaciones como pestañas (sustituyen al desplegable «Contexto»).
   - Tres vistas principales: Receptoroma · Atlas de la indicación · Mecanismo.
   - Las funciones secundarias pasan a un único menú «Más»; los controles de tema y avisos, a «Ajustes».
   - La pauta queda siempre visible; los paneles de patrones y estabilizadores solo se muestran en «Mecanismo».
   - Las alertas de pimozida, coadministración y el contexto/comparación A→B siguen sobre el área de trabajo.
   Solo reubica nodos existentes (conservan id y manejadores) y oculta la navegación antigua; no cambia cálculos. */
const V1633_LENS=[['molecular','Molecular'],['bipolar','Bipolar'],['depression','Depresión · ansiedad'],['psychosis','Psicosis'],['attention','Atención'],['addiction','Adicciones · dolor'],['sleep','Sueño']];
const V1633_MORE=[['pk','PK / PD e interacciones'],['strategy','Mapas estratégicos'],['vectors','Proyecciones P/O/Q'],['report','Informe de la pauta'],['comparison','Comparador A → B'],['design','Contraste previo'],['polarity','Polaridad clínica','bipolar'],['trajectory','Trayectoria','bipolar'],['psychosis','Mapa de psicosis · beta','psychosis'],['attribution','Atribución'],['evidence','Evidencia'],['catalog','Catálogo']];
const v1633AtlasView=()=>state.lens==='bipolar'?'fount':state.lens==='molecular'?null:'supplement';
const v1633LensLabel=()=>(V1633_LENS.find(([k])=>k===state.lens)||[,''])[1];
const v1633Active=()=>document.querySelector('section.view.active')?.id||'';
let v1633Built=false;

function v1633Build(){
 if(v1633Built||!document.querySelector('.shell .header'))return;v1633Built=true;
 document.body.classList.add('v1633');
 const bar=document.createElement('div');bar.id='v1633-bar';bar.className='v1633-bar';
 bar.innerHTML='<div class="v1633-row"><span class="v1633-k">Indicación</span><div class="v1633-lenses" role="group" aria-label="Indicación">'
  +V1633_LENS.map(([k,l])=>'<button type="button" data-v1633-lens="'+k+'" aria-pressed="false">'+esc(l)+'</button>').join('')+'</div></div>'
  +'<div class="v1633-row"><span class="v1633-k">Atlas</span><div class="v1633-views" role="group" aria-label="Vista principal">'
  +'<button type="button" data-v1633-view="receptor" aria-pressed="false">Receptoroma</button>'
  +'<button type="button" data-v1633-view="atlas" aria-pressed="false">Atlas · <span id="v1633AtlasLabel"></span></button>'
  +'<button type="button" data-v1633-view="pdnet" aria-pressed="false">Mecanismo</button></div>'
  +'<label class="v1633-more">Más <select id="v1633More" aria-label="Otras vistas"><option value="">elige una vista…</option>'+V1633_MORE.map(([v,l,lens])=>'<option value="'+v+'"'+(lens?' data-lens="'+lens+'"':'')+'>'+esc(l)+'</option>').join('')+'</select></label>'
  +'<div class="v1633-side"></div><details class="v1633-settings" id="v1633Settings"><summary>Ajustes</summary><div class="v1633-settings-body"></div></details></div>'
  +'<p class="v1633-note">Lectura exploratoria, no prescriptiva · Ki ≠ exposición ≠ ocupación ≠ respuesta · la combinación no es lineal.</p>';
 document.querySelector('.shell .header').after(bar);
 const side=bar.querySelector('.v1633-side'),settings=bar.querySelector('.v1633-settings-body');
 const safety=document.getElementById('safetyOverlay');if(safety)side.appendChild(safety);
 bar.querySelectorAll('[data-v1633-lens]').forEach(b=>b.onclick=()=>{const lens=b.dataset.v1633Lens;if(lens!==state.lens)setLens(lens,false);activateView(v1633AtlasView()||'receptor')});
 bar.querySelectorAll('[data-v1633-view]').forEach(b=>b.onclick=()=>{const v=b.dataset.v1633View;activateView(v==='atlas'?(v1633AtlasView()||'receptor'):v)});
 const more=bar.querySelector('#v1633More');more.onchange=()=>{if(more.value)activateView(more.value)};
 // Pauta siempre visible
 if(typeof v161SetAside==='function'){v161SetAside(false,true)}
 v1633Move();
}
function v1633Move(){
 // Solo se reubican los controles de tema y avisos (fuera del área de trabajo). Los paneles de patrones y
 // estabilizadores no se mueven, porque otros módulos los anclan junto al contexto; se muestran solo en «Mecanismo».
 const tools=document.getElementById('viewTools'),settings=document.querySelector('#v1633Settings .v1633-settings-body');if(tools&&settings&&tools.parentElement!==settings)settings.appendChild(tools);
 const fold=document.querySelector('#v166-patterns > details.v1613-fold');if(fold&&!fold.dataset.v1633){fold.open=true;fold.dataset.v1633='1'}
}
function v1633Sync(){
 if(!v1633Built)return;v1633Move();
 const view=v1633Active(),atlas=v1633AtlasView();
 document.querySelectorAll('[data-v1633-lens]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.v1633Lens===state.lens)));
 const lab=document.getElementById('v1633AtlasLabel');if(lab)lab.textContent=v1633LensLabel();
 const atlasBtn=document.querySelector('[data-v1633-view="atlas"]');if(atlasBtn)atlasBtn.hidden=!atlas;
 document.querySelectorAll('[data-v1633-view]').forEach(b=>{const v=b.dataset.v1633View,on=v==='atlas'?(!!atlas&&(view==='fount'||view==='supplement')):view===v;b.setAttribute('aria-pressed',String(on))});
 const more=document.getElementById('v1633More');
 if(more){[...more.options].forEach(o=>{if(o.dataset.lens)o.hidden=o.disabled=o.dataset.lens!==state.lens});more.value=V1633_MORE.some(([v])=>v===view)?view:''}
 document.body.classList.toggle('v1633-on-pdnet',view==='pdnet');
}
const v1633ActivateBase=activateView;
activateView=function(...args){const r=v1633ActivateBase.apply(this,args);v1633Build();v1633Sync();return r};
const v1633EvaluateBase=evaluate;
evaluate=function(...args){const r=v1633EvaluateBase.apply(this,args);v1633Build();v1633Sync();return r};
setTimeout(()=>{v1633Build();v1633Sync()},0);

/* v16.2: bounded UI controls. No pharmacological data or aggregate modification. */
const V162_UI={theme:'eink',focus:null};
try{const saved=localStorage.getItem('atlas-theme-v162');if(['eink','color'].includes(saved))V162_UI.theme=saved}catch(e){}
function v162SetTheme(theme,persist=true){
  V162_UI.theme=theme==='color'?'color':'eink';
  document.getElementById('eink-theme').media=V162_UI.theme==='eink'?'all':'not all';
  document.body.classList.toggle('theme-eink',V162_UI.theme==='eink');
  document.body.classList.toggle('theme-color',V162_UI.theme==='color');
  const sel=document.getElementById('atlasTheme');if(sel)sel.value=V162_UI.theme;
  const tag=document.getElementById('themeTag');if(tag)tag.textContent=V162_UI.theme==='eink'?'· edición e-ink':'· blanco y azul';
  if(persist)try{localStorage.setItem('atlas-theme-v162',V162_UI.theme)}catch(e){}
}
function v162ThemeTools(){
  v162SetTheme(V162_UI.theme,false);
  const sel=document.getElementById('atlasTheme');if(sel)sel.onchange=()=>v162SetTheme(sel.value);
}
function v162FocusNetwork(host){
  const nodes=[...host.querySelectorAll('.pdn-node')],edges=[...host.querySelectorAll('.pdn-edge')];
  const svg=host.querySelector('svg.pdn-svg');if(!svg)return;
  const focusValid=f=>f&&nodes.some(n=>n.dataset.pdnKind===f.kind&&n.dataset.pdnId===f.id);
  if(!focusValid(V162_UI.focus))V162_UI.focus=null;
  const options=kind=>nodes.filter(n=>n.dataset.pdnKind===kind).map(n=>'<option value="'+esc(n.dataset.pdnId)+'">'+esc(kind==='target'?v160Target(n.dataset.pdnId).label:n.dataset.pdnId)+'</option>').join('');
  const controls=document.createElement('div');controls.className='pdn-focus-controls';
  controls.innerHTML='<label>Enfocar entidad <select id="pdnEntityFocus"><option value="">Todas</option>'+options('entity')+'</select></label><label>Enfocar diana <select id="pdnTargetFocus"><option value="">Todas</option>'+options('target')+'</select></label><button type="button" id="pdnFocusReset">Ver toda la red</button>';
  const status=document.createElement('p');status.className='pdn-focus-status';status.setAttribute('aria-live','polite');
  const wrap=svg.closest('.pdn-svgwrap');wrap.before(controls,status);
  const sels={entity:controls.querySelector('#pdnEntityFocus'),target:controls.querySelector('#pdnTargetFocus')};
  const apply=()=>{
    const f=V162_UI.focus,related=new Set();let count=0;
    edges.forEach(e=>{const on=!f||(f.kind==='entity'?e.dataset.pdnEntity===f.id:e.dataset.pdnTarget===f.id);e.classList.toggle('pdn-muted',!on);e.classList.toggle('pdn-emphasis',on&&!!f);if(on){count++;related.add('entity|'+e.dataset.pdnEntity);related.add('target|'+e.dataset.pdnTarget)}});
    nodes.forEach(n=>{const selected=!!f&&n.dataset.pdnKind===f.kind&&n.dataset.pdnId===f.id;n.classList.toggle('pdn-selected',selected);n.classList.toggle('pdn-muted',!!f&&!selected&&!related.has(n.dataset.pdnKind+'|'+n.dataset.pdnId));n.setAttribute('aria-pressed',String(selected))});
    for(const kind of ['entity','target'])sels[kind].value=f?.kind===kind?f.id:'';
    status.textContent=f?'Foco: '+(f.kind==='target'?v160Target(f.id).label:f.id)+' · '+count+' relaciones destacadas. Las demás siguen visibles de forma tenue.':'Pulsa una entidad o diana (también con Intro o espacio) para destacar solo sus relaciones.';
  };
  for(const kind of ['entity','target'])sels[kind].onchange=()=>{V162_UI.focus=sels[kind].value?{kind,id:sels[kind].value}:null;apply()};
  controls.querySelector('#pdnFocusReset').onclick=()=>{V162_UI.focus=null;apply()};
  nodes.forEach(n=>{const choose=()=>{const next={kind:n.dataset.pdnKind,id:n.dataset.pdnId};V162_UI.focus=V162_UI.focus?.kind===next.kind&&V162_UI.focus?.id===next.id?null:next;apply()};n.onclick=choose;n.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();choose()}}});
  // Preserve complete text in title while fitting long product/route labels inside boxes.
  nodes.filter(n=>n.dataset.pdnKind==='entity').forEach(n=>n.querySelectorAll('text').forEach(t=>{
    const max=Number(n.querySelector('rect')?.getAttribute('width')||290)-24;
    if(t.textContent.length*Number(t.getAttribute('font-size')||12)*.54>max){t.setAttribute('textLength',max);t.setAttribute('lengthAdjust','spacingAndGlyphs');const title=document.createElementNS('http://www.w3.org/2000/svg','title');title.textContent=t.textContent;n.prepend(title)}
  }));
  apply();
}
v162SetTheme(V162_UI.theme,false);

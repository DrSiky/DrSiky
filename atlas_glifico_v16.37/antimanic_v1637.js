/* v16.37 · Componente antimaníaco: competición por D2/D3, actividad intrínseca y ancla clínica.
   Capa A · ocupación operativa por fármaco (escala Ki × dosis del atlas, la misma para todos) → razón r = o/(1−o);
            en combinación θi = ri/(1+Σr) (competición simple en equilibrio).
   Capa B · bloqueo funcional neto B = Σ θi·(1−εi); ε = 0 en antagonistas, editorial en agonistas parciales.
   Capa C · ancla clínica por fármaco y dosis (ECA/metaanálisis). Solo lo acreditado mueve el punto;
            el resto se dibuja como segmento hacia el valor mecanístico. Litio, valproato y carbamazepina
            reciben un término antimaníaco clínico no D2 (ordinal).
   Las series PET se muestran como contraste, no entran en el cálculo: mezclar PET (10 fármacos) con la escala
   operativa (el resto) daría magnitudes no comparables entre fármacos. */
const V1637_ANT=/antagon|agonismo inverso|bloque|inhib/i,V1637_PART=/agonismo parcial|agonista parcial/i,V1637_AGON=/\bagonismo(?! inverso)|facilit/i;
const V1637_EPS={Aripiprazol:.30,Cariprazina:.30,Brexpiprazol:.20},V1637_EPS_DEFAULT=.30;
const V1637_SRC={
 cipriani:['Cipriani 2011 (Lancet)','https://doi.org/10.1016/S0140-6736(11)60873-8'],
 romeo:['Romeo 2018','https://doi.org/10.1177/0269881118760661'],
 fornaro:['Fornaro 2026','https://doi.org/10.1016/j.jad.2026.122329'],
 vieta:['Vieta 2021','https://doi.org/10.1177/0269881120985102'],
 ali:['Ali 2020','https://doi.org/10.1080/14656566.2019.1695777'],
 durgam:['Durgam 2015','https://doi.org/10.1111/bdi.12238'],
 kiss:['Kiss 2010','https://doi.org/10.1124/jpet.109.160432'],
 maeda:['Maeda 2014','https://doi.org/10.1124/jpet.114.213793'],
 shim:['Shim 2007','https://doi.org/10.1176/appi.ajp.2007.06071075'],
 ariFT:['FT aripiprazol 4.1/4.2','https://cima.aemps.es/cima/dochtml/ft/80788/FT_80788.html'],
 lurFT:['FT lurasidona 4.1','https://cima.aemps.es/cima/dochtml/ft/89405/FT_89405.html'],
 carFT:['FT Reagila 4.1','https://cima.aemps.es/cima/dochtml/ft/1171209001/FT_1171209001.html'],
 brexFT:['FT Rxulti 4.1','https://cima.aemps.es/cima/dochtml/ft/1181294002/FT_1181294002.html']
};
const V1637_ANCHOR={
 Haloperidol:{cat:'demostrada',smd:'−0,56',src:['cipriani']},
 Risperidona:{cat:'demostrada',smd:'−0,50',src:['cipriani']},
 Olanzapina:{cat:'demostrada',smd:'−0,43',src:['cipriani']},
 Quetiapina:{cat:'demostrada',smd:'−0,37',src:['cipriani']},
 Asenapina:{cat:'demostrada',smd:'−0,30',src:['cipriani']},
 Ziprasidona:{cat:'demostrada',smd:'−0,20',src:['cipriani']},
 Paliperidona:{cat:'demostrada',src:['fornaro'],note:'Paliperidona de liberación prolongada en el metaanálisis por dosis.'},
 Aripiprazol:{cat:'demostrada',minDose:15,smd:'−0,37',src:['cipriani','romeo','ariFT'],low:'Por debajo de 15 mg: la ficha fija 15 mg como inicio en manía del adulto y Romeo 2018 no halla eficacia a dosis bajas.'},
 Cariprazina:{cat:'demostrada',minDose:3,src:['durgam','romeo','carFT'],low:'Por debajo de 3 mg: los ECA de manía usaron 3–12 mg (media 8,8 mg).',note:'ECA fuera de la UE; en España la ficha solo autoriza esquizofrenia.'},
 Litio:{cat:'demostrada',smd:'−0,37',src:['cipriani'],nonD2:true},
 Carbamazepina:{cat:'demostrada',smd:'−0,36',src:['cipriani'],nonD2:true},
 Valproato:{cat:'demostrada',smd:'−0,20',src:['cipriani'],nonD2:true},
 Brexpiprazol:{cat:'negativa',src:['vieta','brexFT'],note:'Dos ECA de manía aguda de 3 semanas negativos; en España la ficha solo autoriza esquizofrenia.'},
 Lamotrigina:{cat:'negativa',src:['cipriani']},
 Gabapentina:{cat:'negativa',src:['cipriani']},
 Topiramato:{cat:'negativa',src:['cipriani']},
 Lurasidona:{cat:'no-estudiada',src:['ali','lurFT'],note:'No estudiada en manía ni en psicosis bipolar (ausencia de evidencia, no evidencia de ausencia); en España la ficha solo autoriza esquizofrenia.'}
};
const V1637_CAT={demostrada:'eficacia antimaníaca demostrada','dosis-baja':'dosis por debajo del rango probado',negativa:'estudiada y negativa','no-estudiada':'no estudiada en manía','sin-revisar':'sin ancla revisada · se conserva el mecanismo'};
function v1637Anchor(drug,dose){
 const x=V1637_ANCHOR[drug];
 if(!x)return {cat:'sin-revisar',credit:1,src:[],smd:'',note:''};
 if(x.cat==='demostrada'&&x.minDose&&(dose||0)<x.minDose)return {...x,cat:'dosis-baja',credit:0,note:x.low||''};
 return {...x,credit:x.cat==='demostrada'?1:0,note:x.note||''};
}
function v1637Eps(drug){return Object.prototype.hasOwnProperty.call(V1637_EPS,drug)?V1637_EPS[drug]:V1637_EPS_DEFAULT}
/* Agrupa por fármaco las contribuciones de una diana y devuelve un sub-agregado por fármaco */
function v1637ByDrug(a,t){const m=new Map();(a[t]?.contrib||[]).forEach(c=>{if(!c.drug)return;if(!m.has(c.drug))m.set(c.drug,[]);m.get(c.drug).push(c)});return m}
/* aggregate() adjunta (no enumerable) las dosis de las filas activas: las dianas cualitativas, como las del litio, no llevan dosis */
const v1637AggregateBase=aggregate;
aggregate=function(rows=state.rows){const out=v1637AggregateBase(rows);try{Object.defineProperty(out,'__v1637doses',{value:new Map((rows||[]).filter(v140Active).map(r=>[r.drug,r.dose])),enumerable:false})}catch(e){}return out};
function v1637Doses(a){const m=new Map(a.__v1637doses||[]);Object.values(a).forEach(x=>(x.contrib||[]).forEach(c=>{if(c.drug&&!m.has(c.drug)){const d=c.dose??c.parentDose;if(d!=null)m.set(c.drug,d)}}));return m}
function v1637Compete(list){const R=list.reduce((s,x)=>s+x.r,0);list.forEach(x=>x.theta=x.r/(1+R));return list}
/* Bloqueo que darían solos los fármacos indicados (competición entre ellos) */
function v1637Block(list,antagOnly){const R=list.reduce((s,x)=>s+x.r,0);return list.reduce((s,x)=>s+(antagOnly&&!x.antag?0:(x.r/(1+R))*(1-(x.eps||0))),0)}
function v1637SubAgg(a,t,keep){return {[t]:{contrib:(a[t]?.contrib||[]).filter(c=>keep(c.drug))}}}
function v1637Odds(o){const c=Math.min(.98,Math.max(0,o));return c/(1-c)}
function v1637Model(a){
 const doses=v1637Doses(a),anc=d=>v1637Anchor(d,doses.get(d));
 // D2: antagonistas y agonistas parciales compiten
 const d2=[];v1637ByDrug(a,'D2').forEach((cs,drug)=>{const sub={D2:{contrib:cs}},oA=actionSignal(sub,'D2',V1637_ANT),oP=policySignal(sub,'D2',V1637_PART);if(oA<=0&&oP<=0)return;
  const o=1-(1-oA)*(1-oP),partial=oP>0,eps=partial?v1637Eps(drug):0;d2.push({drug,o,r:v1637Odds(o),partial,eps,anchor:anc(drug)})});
 v1637Compete(d2);d2.forEach(x=>x.b=x.theta*(1-x.eps));
 // Acreditado = min(B total, B de los fármacos acreditados solos): un antagonista no acreditado no resta;
 // un agonista parcial no acreditado sí resta, porque desplaza al antagonista acreditado.
 const B=d2.reduce((s,x)=>s+x.b,0),Bc=Math.min(B,v1637Block(d2.filter(x=>x.anchor.credit)));
 // D3: todos los ligandos compiten; solo el antagonismo suma al término antimaníaco (el agonismo D3 sigue en ad/act)
 const d3=[];v1637ByDrug(a,'D3').forEach((cs,drug)=>{const sub={D3:{contrib:cs}},oA=actionSignal(sub,'D3',V1637_ANT),oG=actionSignal(sub,'D3',V1637_AGON);if(oA<=0&&oG<=0)return;
  const o=1-(1-oA)*(1-oG);d3.push({drug,o,r:v1637Odds(o),antag:oA>0&&oA>=oG,anchor:anc(drug)})});
 v1637Compete(d3);const B3=d3.filter(x=>x.antag).reduce((s,x)=>s+x.theta,0),B3c=Math.min(B3,v1637Block(d3.filter(x=>x.anchor.credit),true));
 // 5-HT2A antagonismo y M1 agonismo: señal combinada heredada; la acreditada es la de los fármacos acreditados solos
 const share=(t,re,pol)=>{const sig=x=>pol?policySignal(x,t,re):actionSignal(x,t,re);return {S:sig(a),Sc:sig(v1637SubAgg(a,t,d=>anc(d).credit))}};
 const h2a=share('HT2A',V1637_ANT,false),m1=share('M1',V1637_AGON,true);
 // Antimaníaco clínico no D2 (litio, valproato, carbamazepina): ordinal, escalado por dosis como en aggregate()
 const nd=[];doses.forEach((dose,drug)=>{const x=anc(drug),d=DRUGS[drug];if(!x.nonD2||!x.credit||!(dose>0)||!d)return;const f=Math.min(1.22,Math.max(.05,(dose/Math.max(1,d.max))*1.55));nd.push({drug,dose,n:Math.min(1,Math.pow(f,.55)),anchor:x})});
 const N=nd.length?1-nd.reduce((p,x)=>p*(1-x.n),1):0;
 const terms=[
  {label:'D2 bloqueo neto (competición + ε)',mech:B*.38,cred:Bc*.38,origin:'c'},
  {label:'D3 antagonismo (en competición)',mech:B3*.20,cred:B3c*.20,origin:'c3'},
  {label:'5-HT2A antagonismo',mech:h2a.S*.14,cred:h2a.Sc*.14,origin:'h'},
  {label:'M1 agonismo',mech:m1.S*.24,cred:m1.Sc*.24,origin:'u'},
  {label:'Antimaníaco clínico no D2',mech:N*.38,cred:N*.38,origin:'k'}
 ];
 const amMech=Math.min(1,terms.reduce((s,t)=>s+t.mech,0)),amClin=Math.min(1,terms.reduce((s,t)=>s+t.cred,0));
 return {d2,d3,nd,B,Bc,B3,B3c,N,terms,amMech,amClin,competition:d2.some(x=>x.partial)&&d2.some(x=>!x.partial)};
}
/* Capa O: el punto usa el componente acreditado; yMech es el extremo mecanístico del segmento */
const v1637VectorBase=vectorProfile;
vectorProfile=function(a){const v=v1637VectorBase(a),m=v1637Model(a);return {...v,am:m.amClin,y:(v.ad-m.amClin)*7,amMech:m.amMech,yMech:(v.ad-m.amMech)*7,antimanic:m}};
/* Capa P (potencia intrínseca, un fármaco por ficha): ε en lugar del × 0,5; sin ancla clínica (capa mecanística) */
const v1637PBase=v161P;
v161P=function(a){const p=v1637PBase(a),T=(t,re)=>v161Take(a,t,re),dr=[...v1637ByDrug(a,'D2').keys()].filter(d=>Object.prototype.hasOwnProperty.call(V1637_EPS,d)),eps=dr.length?dr.reduce((s,d)=>s+V1637_EPS[d],0)/dr.length:V1637_EPS_DEFAULT;
 return {...p,am:Math.min(1,T('D2',V161_ANT)*.38+T('D2',V1637_PART)*.38*(1-eps)+T('D3',V161_ANT)*.20+T('HT2A',V161_ANT)*.14+T('M1',V161_AGON)*.24)}};
/* Series PET como contraste (no entran en el cálculo) */
function v1637PetText(drug){
 const ps=DRUGS[drug]?.petSeries,arr=Array.isArray(ps)?ps:(ps?[ps]:[]),out=[];
 arr.forEach(s=>{if(!/D2/.test(s?.target||''))return;[...(s.points||[]),...(s.ranges||[])].forEach(p=>{const v=p.value??p.mean??p.d2??p.values?.D2??p.D2;let txt=null;
  if(Number.isFinite(v))txt=(p.approx?'≈':'')+String(Math.round(v*10)/10).replace('.',',')+' %';else if(Number.isFinite(p.low)&&Number.isFinite(p.high))txt=String(p.low).replace('.',',')+'–'+String(p.high).replace('.',',')+' %';
  if(txt&&p.dose!=null)out.push(txt+' a '+String(p.dose).replace('.',',')+' mg')});
  if(out.length&&s.source)out.push('<a href="'+esc(s.source)+'" target="_blank" rel="noreferrer">fuente</a>')});
 return out.length?out.join(' · '):'—';
}
function v1637SrcLinks(keys){return (keys||[]).map(k=>V1637_SRC[k]?'<a href="'+esc(V1637_SRC[k][1])+'" target="_blank" rel="noreferrer">'+esc(V1637_SRC[k][0])+'</a>':'').filter(Boolean).join(', ')}
function v1637Pct(x){return Math.round(x*100)+' %'}
/* Términos del vector: v = aporte que mueve el vector; vm = aporte mecanístico (solo en am) */
const V1637_ORIGIN={h:'heredado v16.0',u:'política anti/pro del usuario',c:'competición v16.37 · ε editorial',c3:'competición v16.37 (sin ε)',k:'ancla clínica (ECA/metaanálisis) · magnitud ordinal'};
v1636Terms=function(a){
 const agon=V1637_AGON,ant=V1637_ANT,antH=/antagon|agonismo inverso|bloque|inhib|antihistam/i,antA=/antagon|agonismo inverso|bloque|inhib|adrenol[ií]tic/i,P=(t,re)=>policySignal(a,t,re);
 const T=(comp,label,sig,w,origin)=>({comp,label,v:sig*w,vm:sig*w,w,origin});
 const m=v1637Model(a);
 return [
  T('act','NET',g(a,'NET'),.32,'h'),T('act','DAT',g(a,'DAT'),.25,'h'),T('act','D3 agonismo',actionSignal(a,'D3',agon),.25,'h'),T('act','5-HT1A agonismo',actionSignal(a,'HT1A',agon),.10,'h'),T('act','H1 agonismo',P('H1',agon),.58,'u'),T('act','α1 agonismo',P('A1',agon),.18,'u'),
  T('sed','H1 antagonismo',P('H1',antH),.58,'u'),T('sed','M1 antagonismo',P('M1',ant),.24,'u'),T('sed','α1 antagonismo',P('A1',antA),.18,'u'),
  T('ad','NET',g(a,'NET'),.24,'h'),T('ad','SERT',g(a,'SERT'),.14,'h'),T('ad','5-HT1A agonismo',actionSignal(a,'HT1A',agon),.23,'h'),T('ad','D3 agonismo',actionSignal(a,'D3',agon),.16,'h'),T('ad','DAT',g(a,'DAT'),.10,'h'),T('ad','MAO-A',g(a,'MAOA'),.13,'h'),
  ...m.terms.map(t=>({comp:'am',label:t.label,v:t.cred,vm:t.mech,origin:t.origin}))
 ].filter(t=>t.v>0.0005||t.vm>0.0005);
};
v1636BreakdownHtml=function(a){
 const v=vectorProfile(a),terms=v1636Terms(a),m=v.antimanic;
 const body=['act','sed','ad','am'].map(k=>{const ts=terms.filter(t=>t.comp===k),sum=ts.reduce((s,t)=>s+t.v,0);
  const head=k==='am'?V1636_COMP[k]+' · acreditado '+v.am.toFixed(2)+' · mecanístico '+v.amMech.toFixed(2):V1636_COMP[k]+' · '+v[k].toFixed(2)+(sum>1?' (tope 1; suma '+sum.toFixed(2)+')':'');
  return '<tr class="v1636-comp"><th colspan="4">'+head+'</th></tr>'+(ts.length?ts.map(t=>'<tr><td>'+esc(t.label)+'</td><td>'+t.v.toFixed(3)+'</td><td>'+(k==='am'?t.vm.toFixed(3):'')+'</td><td>'+esc(V1637_ORIGIN[t.origin]||'')+'</td></tr>').join(''):'<tr><td colspan="4" class="mut">sin términos activos</td></tr>')}).join('');
 const rows=m.d2.map(x=>'<tr><td>'+esc(x.drug)+'</td><td>'+(x.partial?'agonista parcial · ε '+String(x.eps).replace('.',','):'antagonista')+'</td><td>'+v1637Pct(x.o)+'</td><td>'+v1637Pct(x.theta)+'</td><td>'+x.b.toFixed(2)+'</td><td>'+esc(V1637_CAT[x.anchor.cat])+(x.anchor.smd?' · DME '+x.anchor.smd:'')+(x.anchor.note?'<br><span class="small">'+esc(x.anchor.note)+'</span>':'')+(x.anchor.src?.length?'<br><span class="small">'+v1637SrcLinks(x.anchor.src)+'</span>':'')+'</td><td class="small">'+v1637PetText(x.drug)+'</td></tr>').join('');
 const nd=m.nd.map(x=>'<tr><td>'+esc(x.drug)+'</td><td>sin acción D2</td><td colspan="3">término no D2 '+x.n.toFixed(2)+' × 0,38</td><td>'+esc(V1637_CAT.demostrada)+(x.anchor.smd?' · DME '+x.anchor.smd:'')+'<br><span class="small">'+v1637SrcLinks(x.anchor.src)+'</span></td><td>—</td></tr>').join('');
 const comp=m.competition?'<p class="v1637-comp-note"><b>Competición agonista parcial–antagonista en la pauta.</b> El agonista parcial desplaza al antagonista del receptor y aporta solo (1 − ε) de bloqueo por receptor ocupado; el bloqueo neto puede quedar por debajo del antagonista solo. En un ECA, añadir aripiprazol a haloperidol normalizó la prolactina sin cambiar BPRS ni síntomas extrapiramidales ('+v1637SrcLinks(['shim'])+').</p>':'';
 const d2=(m.d2.length||m.nd.length)?'<h4>Bloqueo D2 en la pauta y ancla clínica</h4>'+comp+'<div class="tw"><table class="v1636-table v1637-table"><thead><tr><th>Fármaco</th><th>Acción D2</th><th>Ocupación sola (operativa)</th><th>Ocupación en la pauta</th><th>Aporte a B</th><th>Ancla clínica</th><th>PET D2 (contraste)</th></tr></thead><tbody>'+rows+nd+'</tbody><tfoot><tr><td colspan="7" class="small">B = '+m.B.toFixed(2)+' (acreditado '+m.Bc.toFixed(2)+'). Acreditado = mínimo entre B y el bloqueo que darían solos los fármacos con eficacia demostrada: añadir un antagonista no acreditado no lo reduce; un agonista parcial sí, porque desplaza al antagonista. Ocupación operativa: escala Ki × dosis del atlas, común a todos los fármacos, sin corregir por fracción libre ni penetración; no es ocupación PET. ε editorial: aripiprazol y cariprazina 0,30 (del orden del Emax 30 % de cariprazina en fosfatos de inositol, '+v1637SrcLinks(['kiss'])+'); brexpiprazol 0,20, menor que aripiprazol ('+v1637SrcLinks(['maeda'])+'). La actividad intrínseca depende del ensayo y del tejido; no es un valor estriatal humano. Las series PET se muestran con el estado de verificación que tengan en la ficha del fármaco y no entran en el cálculo.</td></tr></tfoot></table></div>':'';
 return '<section class="v1636-breakdown"><h3>Qué mueve el vector · capa O</h3><p class="small">Horizontal = 7 × (activación − sedación); vertical = 7 × (antidepresivo − antimaníaco acreditado). El segmento del mapa llega hasta el antimaníaco mecanístico. Cada término es señal × peso; los pesos son editoriales, no tamaños de efecto clínico.</p><div class="tw"><table class="v1636-table"><thead><tr><th>Término</th><th>Aporte al vector</th><th>Mecanístico</th><th>Origen de la regla</th></tr></thead><tbody>'+body+'</tbody></table></div>'+d2+'</section>';
};
/* Mapa de polaridad: segmento desde el punto acreditado hasta el mecanístico */
const v1637PolarityBase=polarity;
polarity=function(a){
 const r=v1637PolarityBase.apply(this,arguments);
 try{const svg=document.querySelector('#polarity svg.clinical-map');if(!svg)return r;const p=clinicalPosition(),v=vectorProfile(a),sx=x=>500+x*34,sy=y=>330-y*25,cl=z=>Math.max(-10,Math.min(10,z));
  const dx=sx(cl(p.horizontal+v.x)),dy=sy(cl(p.vertical+v.y)),my=sy(cl(p.vertical+v.yMech));
  if(Math.abs(my-dy)>=2){const NS='http://www.w3.org/2000/svg',ln=document.createElementNS(NS,'line'),c=document.createElementNS(NS,'circle'),t=document.createElementNS(NS,'text');
   ln.setAttribute('x1',dx);ln.setAttribute('y1',dy);ln.setAttribute('x2',dx);ln.setAttribute('y2',my);ln.setAttribute('class','v1637-seg');
   c.setAttribute('cx',dx);c.setAttribute('cy',my);c.setAttribute('r','7');c.setAttribute('class','v1637-mech');
   t.setAttribute('x',dx+14);t.setAttribute('y',my+4);t.setAttribute('class','v1637-mech-label');t.textContent='mecanismo sin eficacia antimaníaca acreditada';
   svg.append(ln,c,t);
   svg.closest('.map-pair')?.querySelector('.vector-key')?.insertAdjacentHTML('beforeend','<span><i class="v1637-key"></i>segmento: antimaníaco mecanístico no acreditado</span>')}
  svg.closest('.map-pair')?.querySelector('aside')?.insertAdjacentHTML('beforeend','<div class="logic-card v1637-card" style="margin-top:8px"><b>Componente antimaníaco</b><span>acreditado '+v.am.toFixed(2)+' · mecanístico '+v.amMech.toFixed(2)+'</span></div>');
 }catch(e){}
 try{v1636Attach()}catch(e){}  // los botones de objetivo redibujan el panel: se repone el desglose
 return r;
};

/* v16.40 · El antagonismo 5-HT2A queda solo en la capa mecanística del componente antimaníaco.
   Decisión del usuario (opción b): no hay ECA de antagonistas 5-HT2A selectivos en monoterapia para la manía; solo un ECA
   coadyuvante de ritanserina (Akhondzadeh 2003). En Cipriani 2011 el haloperidol, sin antagonismo 5-HT2A, tiene la mayor DME.
   El término nunca mueve el punto (acreditado 0) y se dibuja en el segmento mecanístico. Capa P sin cambios. */
Object.assign(V1637_SRC,{akhondzadeh:['Akhondzadeh 2003','https://doi.org/10.1186/1471-244X-3-7']});
V1637_ORIGIN.m='solo mecanístico · no acreditado (v16.40: sin ECA antimaníaco propio)';
const v1640ModelBase=v1637Model;
v1637Model=function(a){
 const m=v1640ModelBase(a);
 m.terms=m.terms.map(t=>/^5-HT2A/.test(t.label)?{...t,cred:0,origin:'m'}:t);
 m.amClin=Math.min(1,m.terms.reduce((s,t)=>s+t.cred,0));
 return m;
};
/* Nota en el desglose */
const v1640BreakdownBase=v1636BreakdownHtml;
v1636BreakdownHtml=function(a){
 const html=v1640BreakdownBase(a);
 return html.includes('5-HT2A antagonismo')?html.replace('<h4>','<p class="small v1640-note">El antagonismo 5-HT2A figura solo como mecanismo: no hay ensayos de antagonistas 5-HT2A selectivos en monoterapia para la manía; el único ECA controlado es coadyuvante ('+v1637SrcLinks(['akhondzadeh'])+'). En '+v1637SrcLinks(['cipriani'])+' el haloperidol, sin antagonismo 5-HT2A, tiene la mayor diferencia frente a placebo.</p><h4>'):html;
};
/* Mapa: aviso cuando el vector supera el borde del campo (±10) y el recorte superpone punto y segmento */
const v1640PolarityBase=polarity;
polarity=function(a){
 const r=v1640PolarityBase.apply(this,arguments);
 try{const p=clinicalPosition(),v=vectorProfile(a),yc=p.vertical+v.y,ym=p.vertical+v.yMech,xc=p.horizontal+v.x;
  if([yc,ym,xc].some(z=>Math.abs(z)>10)){const card=document.querySelector('#polarity .v1637-card span');if(card&&!card.querySelector('.v1640-clip'))card.insertAdjacentHTML('beforeend','<br><i class="v1640-clip">El vector supera el borde del campo y se recorta'+(Math.abs(yc)>10&&Math.abs(ym)>10&&Math.abs(v.yMech-v.y)>.01?': punto y segmento quedan superpuestos en el borde':'')+'.</i>')}
 }catch(e){}
 return r;
};

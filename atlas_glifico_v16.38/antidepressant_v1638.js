/* v16.38 · Crédito antimaníaco del antagonismo 5-HT2A en antidepresivos.
   Ningún antidepresivo tiene eficacia antimaníaca demostrada; las fichas de mirtazapina y trazodona (4.4) advierten
   del viraje a fase maníaca y ordenan retirar el fármaco si ocurre. Se les aplica el ancla clínica de la v16.37:
   su antagonismo 5-HT2A deja de mover el punto y queda como segmento mecanístico. Regla de familia: cualquier
   antidepresivo (familia N06) sin ancla propia recibe la misma categoría. */
Object.assign(V1637_SRC,{
 mirFT:['FT mirtazapina 4.4','https://cima.aemps.es/cima/dochtml/ft/86890/FT_86890.html'],
 trzFT:['FT trazodona 4.4','https://cima.aemps.es/cima/dochtml/ft/83568/FT_83568.html'],
 bhanji:['Bhanji 2002 (casos)','https://doi.org/10.1097/00004850-200211000-00009'],
 warren:['Warren y Bick 1984 (casos)','https://doi.org/10.1176/ajp.141.9.1103']
});
V1637_CAT.antidepresivo='antidepresivo · sin eficacia antimaníaca; no se acredita';
Object.assign(V1637_ANCHOR,{
 Mirtazapina:{cat:'antidepresivo',src:['mirFT','bhanji'],note:'La ficha advierte del viraje a fase maníaca en la depresión bipolar y ordena retirar el fármaco si ocurre; hay casos publicados de manía inducida.'},
 Trazodona:{cat:'antidepresivo',src:['trzFT','warren'],note:'La ficha advierte del viraje a fase maníaca y ordena retirar el fármaco si ocurre; hay casos publicados de manía inducida.'}
});
const v1638AnchorBase=v1637Anchor;
v1637Anchor=function(drug,dose){
 if(!V1637_ANCHOR[drug]&&/Antidepresivos/i.test(DRUGS[drug]?.spain?.family||''))return {cat:'antidepresivo',credit:0,src:[],smd:'',note:'Sin eficacia antimaníaca demostrada; su mecanismo no se acredita como antimaníaco.'};
 return v1638AnchorBase(drug,dose);
};
/* Desglose: la tabla por fármaco incluye también a quien aporta al antimaníaco sin acción D2 (5-HT2A, M1, D3) */
const v1638BreakdownBase=v1636BreakdownHtml;
v1636BreakdownHtml=function(a){
 let html=v1638BreakdownBase(a).replace('<h4>Bloqueo D2 en la pauta y ancla clínica</h4>','<h4>Bloqueo D2 y ancla clínica por fármaco</h4>');
 try{const m=vectorProfile(a).antimanic,seen=new Set([...m.d2.map(x=>x.drug),...m.nd.map(x=>x.drug)]),doses=v1637Doses(a),rows=[];
  const parts=[['HT2A',V1637_ANT,false,'5-HT2A antagonismo',.14],['M1',V1637_AGON,true,'M1 agonismo',.24],['D3',V1637_ANT,false,'D3 antagonismo',.20]];
  const drugs=new Set();parts.forEach(([t])=>v1637ByDrug(a,t).forEach((cs,d)=>{if(!seen.has(d))drugs.add(d)}));
  drugs.forEach(d=>{const terms=parts.map(([t,re,pol,lab,w])=>{const sub=v1637SubAgg(a,t,x=>x===d),s=pol?policySignal(sub,t,re):actionSignal(sub,t,re);return s>0.0005?lab+' '+(s*w).toFixed(3):''}).filter(Boolean);if(!terms.length)return;
   const x=v1637Anchor(d,doses.get(d));
   rows.push('<tr><td>'+esc(d)+'</td><td>sin acción D2</td><td colspan="3">'+esc(terms.join(' · '))+(x.credit?'':' · no acreditado')+'</td><td>'+esc(V1637_CAT[x.cat]||x.cat)+(x.note?'<br><span class="small">'+esc(x.note)+'</span>':'')+(x.src?.length?'<br><span class="small">'+v1637SrcLinks(x.src)+'</span>':'')+'</td><td>—</td></tr>')});
  if(!rows.length)return html;
  if(html.includes('</tbody><tfoot>'))return html.replace('</tbody><tfoot>',rows.join('')+'</tbody><tfoot>');
  return html.replace(/<\/section>$/,'<h4>Ancla clínica por fármaco</h4><div class="tw"><table class="v1636-table v1637-table"><thead><tr><th>Fármaco</th><th>Acción D2</th><th colspan="3">Aporte antimaníaco mecanístico</th><th>Ancla clínica</th><th>PET D2</th></tr></thead><tbody>'+rows.join('')+'</tbody></table></div></section>');
 }catch(e){return html}
};

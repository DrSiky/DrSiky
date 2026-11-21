// ATLAS GLÍFICO v16.33 · uso: node build_v1633.mjs RUTA/ATLAS_GLIFICO_VISUAL_v16.32.html [SALIDA.html]
// La v16.32 se obtiene con ../atlas_glifico_v16.32/build_v1632.mjs a partir de la v16.31.
import fs from 'node:fs';import vm from 'node:vm';import crypto from 'node:crypto';
const here=f=>new URL(f,import.meta.url),read=f=>fs.readFileSync(here(f),'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const src=process.argv[2];if(!src)throw Error('Falta la ruta de ATLAS_GLIFICO_VISUAL_v16.32.html');
const out=process.argv[3]||new URL('../ATLAS_GLIFICO_VISUAL_v16.33.html',import.meta.url).pathname;
let html=fs.readFileSync(src,'utf8');const ancestor=hash(html);
if(ancestor!=='c3a08f3171d6a9eccdbc747be0a6e7aebb3117dd683d7d28cc33c0dd570d5c58')throw Error('El ancestro no es la v16.32 del paquete: '+ancestor);
function once(a,b){const n=html.split(a).length-1;if(n!==1)throw Error('Ancla no única ('+n+'): '+a.slice(0,140));html=html.replace(a,()=>b)}
for(const s of ['Atlas visual v16.32</title>','Atlas visual v16.32 <span',"atlasVersion:'16.32'","a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.32.svg'","link.download='atlas_proyecciones_'+basis+'_v16.32.csv'",'ATLAS GLÍFICO · v16.32 · pauta representada',"ATLAS_ESTRATEGICO_'+key+'_v16.32.svg","el.download='ATLAS_mapa_'+state.lens+'_v16.32.svg'","a.download='ATLAS_espacial_'+state.lens+'_v16.32.svg'"])once(s,s.replace('16.32','16.33'));

// Agonismo parcial D2 → contención con factor editorial 0,5 (actividad intrínseca no incorporada; sin calibrar)
once("am=Math.min(1,actionSignal(a,'D2',ant)*.38+actionSignal(a,'D3',ant)*.20+actionSignal(a,'HT2A',ant)*.14+P('H1',antH)*.14+P('M1',agon)*.24),",
 "am=Math.min(1,actionSignal(a,'D2',ant)*.38+P('D2',/agonismo parcial|agonista parcial/i)*.38*.5+actionSignal(a,'D3',ant)*.20+actionSignal(a,'HT2A',ant)*.14+P('H1',antH)*.14+P('M1',agon)*.24),");
once("D2n:T('D2',V161_ANT),","D2n:T('D2',V161_ANT),D2p:T('D2',/agonismo parcial|agonista parcial/i),");
once("am:Math.min(1,s.D2n*.38+s.D3n*.20+s.HT2An*.14+s.H1n*.14+s.M1a*.24)};","am:Math.min(1,s.D2n*.38+s.D2p*.38*.5+s.D3n*.20+s.HT2An*.14+s.H1n*.14+s.M1a*.24)};");
once("Los pesos de agonistas son espejo de los de sedación, sin calibrar.","Los pesos de agonistas son espejo de los de sedación, sin calibrar. El agonismo parcial D2 suma contención con un factor editorial de 0,5 (sin calibrar; la actividad intrínseca no se incorpora).");

once('</head>','<style id="ui-v1633">'+read('ui_v1633.css')+'</style></head>');
const boot="$$('[data-view]').forEach(b=>b.onclick=";
once(boot,read('curation_v1633.js')+'\n'+read('ui_v1633.js')+'\n'+boot);
new vm.Script(html.match(/<script>([\s\S]*?)<\/script>/)[1]);
fs.writeFileSync(out,html);
console.log(JSON.stringify({version:'16.33',ancestor,sha256:hash(html),bytes:Buffer.byteLength(html)}));

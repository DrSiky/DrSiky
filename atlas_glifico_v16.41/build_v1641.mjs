// ATLAS GLÍFICO v16.41 · uso: node build_v1641.mjs RUTA/ATLAS_GLIFICO_VISUAL_v16.40.html [SALIDA.html]
import fs from 'node:fs';import vm from 'node:vm';import crypto from 'node:crypto';
const here=f=>new URL(f,import.meta.url),read=f=>fs.readFileSync(here(f),'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const src=process.argv[2];if(!src)throw Error('Falta la ruta de ATLAS_GLIFICO_VISUAL_v16.40.html');
const out=process.argv[3]||new URL('../ATLAS_GLIFICO_VISUAL_v16.41.html',import.meta.url).pathname;
let html=fs.readFileSync(src,'utf8');const ancestor=hash(html);
if(ancestor!=='36a223e8aa56fc256ecb14b4392e804b4d58db2388cca6514ec25d2c575f5358')throw Error('El ancestro no es la v16.40 del paquete: '+ancestor);
function once(a,b){const n=html.split(a).length-1;if(n!==1)throw Error('Ancla no única ('+n+'): '+a.slice(0,140));html=html.replace(a,()=>b)}
for(const s of ['Atlas visual v16.40</title>','Atlas visual v16.40 <span',"atlasVersion:'16.40'","a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.40.svg'","link.download='atlas_proyecciones_'+basis+'_v16.40.csv'",'ATLAS GLÍFICO · v16.40 · pauta representada',"ATLAS_ESTRATEGICO_'+key+'_v16.40.svg","el.download='ATLAS_mapa_'+state.lens+'_v16.40.svg'","a.download='ATLAS_espacial_'+state.lens+'_v16.40.svg'"])once(s,s.replace('16.40','16.41'));
const boot="$$('[data-view]').forEach(b=>b.onclick=";
once(boot,read('antidepressant_anchor_v1641.js')+'\n'+boot);
new vm.Script(html.match(/<script>([\s\S]*?)<\/script>/)[1]);
fs.writeFileSync(out,html);
console.log(JSON.stringify({version:'16.41',ancestor,sha256:hash(html),bytes:Buffer.byteLength(html)}));

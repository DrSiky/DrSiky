// ATLAS GLÍFICO v16.39 · uso: node build_v1639.mjs RUTA/ATLAS_GLIFICO_VISUAL_v16.38.html [SALIDA.html]
import fs from 'node:fs';import vm from 'node:vm';import crypto from 'node:crypto';
const here=f=>new URL(f,import.meta.url),read=f=>fs.readFileSync(here(f),'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const src=process.argv[2];if(!src)throw Error('Falta la ruta de ATLAS_GLIFICO_VISUAL_v16.38.html');
const out=process.argv[3]||new URL('../ATLAS_GLIFICO_VISUAL_v16.39.html',import.meta.url).pathname;
let html=fs.readFileSync(src,'utf8');const ancestor=hash(html);
if(ancestor!=='e92b3e4d1c896dc3751387b18bb9a0b784c13537fe63a65ec97f3ec7291f771d')throw Error('El ancestro no es la v16.38 del paquete: '+ancestor);
function once(a,b){const n=html.split(a).length-1;if(n!==1)throw Error('Ancla no única ('+n+'): '+a.slice(0,140));html=html.replace(a,()=>b)}
for(const s of ['Atlas visual v16.38</title>','Atlas visual v16.38 <span',"atlasVersion:'16.38'","a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.38.svg'","link.download='atlas_proyecciones_'+basis+'_v16.38.csv'",'ATLAS GLÍFICO · v16.38 · pauta representada',"ATLAS_ESTRATEGICO_'+key+'_v16.38.svg","el.download='ATLAS_mapa_'+state.lens+'_v16.38.svg'","a.download='ATLAS_espacial_'+state.lens+'_v16.38.svg'"])once(s,s.replace('16.38','16.39'));
const boot="$$('[data-view]').forEach(b=>b.onclick=";
once(boot,read('antipsychotic_anchor_v1639.js')+'\n'+boot);
new vm.Script(html.match(/<script>([\s\S]*?)<\/script>/)[1]);
fs.writeFileSync(out,html);
console.log(JSON.stringify({version:'16.39',ancestor,sha256:hash(html),bytes:Buffer.byteLength(html)}));

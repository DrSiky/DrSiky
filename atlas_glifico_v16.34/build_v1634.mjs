// ATLAS GLÍFICO v16.34 · uso: node build_v1634.mjs RUTA/ATLAS_GLIFICO_VISUAL_v16.33.html [SALIDA.html]
import fs from 'node:fs';import vm from 'node:vm';import crypto from 'node:crypto';
const here=f=>new URL(f,import.meta.url),read=f=>fs.readFileSync(here(f),'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const src=process.argv[2];if(!src)throw Error('Falta la ruta de ATLAS_GLIFICO_VISUAL_v16.33.html');
const out=process.argv[3]||new URL('../ATLAS_GLIFICO_VISUAL_v16.34.html',import.meta.url).pathname;
let html=fs.readFileSync(src,'utf8');const ancestor=hash(html);
if(ancestor!=='c633e642af521f79a893a1e8f1b5608270fae03f0386137e15d11d24743d2f39')throw Error('El ancestro no es la v16.33 del paquete: '+ancestor);
function once(a,b){const n=html.split(a).length-1;if(n!==1)throw Error('Ancla no única ('+n+'): '+a.slice(0,140));html=html.replace(a,()=>b)}
for(const s of ['Atlas visual v16.33</title>','Atlas visual v16.33 <span',"atlasVersion:'16.33'","a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.33.svg'","link.download='atlas_proyecciones_'+basis+'_v16.33.csv'",'ATLAS GLÍFICO · v16.33 · pauta representada',"ATLAS_ESTRATEGICO_'+key+'_v16.33.svg","el.download='ATLAS_mapa_'+state.lens+'_v16.33.svg'","a.download='ATLAS_espacial_'+state.lens+'_v16.33.svg'"])once(s,s.replace('16.33','16.34'));
once('</head>','<style id="interactions-v1634">'+read('interactions_v1634.css')+'</style></head>');
const boot="$$('[data-view]').forEach(b=>b.onclick=";
once(boot,read('interactions_v1634.js')+'\n'+boot);
new vm.Script(html.match(/<script>([\s\S]*?)<\/script>/)[1]);
fs.writeFileSync(out,html);
console.log(JSON.stringify({version:'16.34',ancestor,sha256:hash(html),bytes:Buffer.byteLength(html)}));

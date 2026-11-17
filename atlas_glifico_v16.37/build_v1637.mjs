// ATLAS GLÍFICO v16.37 · uso: node build_v1637.mjs RUTA/ATLAS_GLIFICO_VISUAL_v16.36.html [SALIDA.html]
import fs from 'node:fs';import vm from 'node:vm';import crypto from 'node:crypto';
const here=f=>new URL(f,import.meta.url),read=f=>fs.readFileSync(here(f),'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const src=process.argv[2];if(!src)throw Error('Falta la ruta de ATLAS_GLIFICO_VISUAL_v16.36.html');
const out=process.argv[3]||new URL('../ATLAS_GLIFICO_VISUAL_v16.37.html',import.meta.url).pathname;
let html=fs.readFileSync(src,'utf8');const ancestor=hash(html);
if(ancestor!=='1d4e99f34c21ccc84d7fdfff6cc389ea59acfa5fae137848c2eb6cc22499a039')throw Error('El ancestro no es la v16.36 del paquete: '+ancestor);
function once(a,b){const n=html.split(a).length-1;if(n!==1)throw Error('Ancla no única ('+n+'): '+a.slice(0,140));html=html.replace(a,()=>b)}
for(const s of ['Atlas visual v16.36</title>','Atlas visual v16.36 <span',"atlasVersion:'16.36'","a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.36.svg'","link.download='atlas_proyecciones_'+basis+'_v16.36.csv'",'ATLAS GLÍFICO · v16.36 · pauta representada',"ATLAS_ESTRATEGICO_'+key+'_v16.36.svg","el.download='ATLAS_mapa_'+state.lens+'_v16.36.svg'","a.download='ATLAS_espacial_'+state.lens+'_v16.36.svg'"])once(s,s.replace('16.36','16.37'));
const boot="$$('[data-view]').forEach(b=>b.onclick=";
once('</head>','<style id="patch-v1637">'+read('antimanic_v1637.css')+'</style></head>');
once(boot,read('antimanic_v1637.js')+'\n'+boot);
new vm.Script(html.match(/<script>([\s\S]*?)<\/script>/)[1]);
fs.writeFileSync(out,html);
console.log(JSON.stringify({version:'16.37',ancestor,sha256:hash(html),bytes:Buffer.byteLength(html)}));

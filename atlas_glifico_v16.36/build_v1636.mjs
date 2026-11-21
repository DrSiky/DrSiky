// ATLAS GLÍFICO v16.36 · uso: node build_v1636.mjs RUTA/ATLAS_GLIFICO_VISUAL_v16.35.html [SALIDA.html]
import fs from 'node:fs';import vm from 'node:vm';import crypto from 'node:crypto';
const here=f=>new URL(f,import.meta.url),read=f=>fs.readFileSync(here(f),'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const src=process.argv[2];if(!src)throw Error('Falta la ruta de ATLAS_GLIFICO_VISUAL_v16.35.html');
const out=process.argv[3]||new URL('../ATLAS_GLIFICO_VISUAL_v16.36.html',import.meta.url).pathname;
let html=fs.readFileSync(src,'utf8');const ancestor=hash(html);
if(ancestor!=='8b2a713cbd915fdf25e226b39750754260e39302a0a6224bf529285b40d5651b')throw Error('El ancestro no es la v16.35 del paquete: '+ancestor);
function once(a,b){const n=html.split(a).length-1;if(n!==1)throw Error('Ancla no única ('+n+'): '+a.slice(0,140));html=html.replace(a,()=>b)}
for(const s of ['Atlas visual v16.35</title>','Atlas visual v16.35 <span',"atlasVersion:'16.35'","a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.35.svg'","link.download='atlas_proyecciones_'+basis+'_v16.35.csv'",'ATLAS GLÍFICO · v16.35 · pauta representada',"ATLAS_ESTRATEGICO_'+key+'_v16.35.svg","el.download='ATLAS_mapa_'+state.lens+'_v16.35.svg'","a.download='ATLAS_espacial_'+state.lens+'_v16.35.svg'"])once(s,s.replace('16.35','16.36'));
const boot="$$('[data-view]').forEach(b=>b.onclick=";
// H1 solo en sedación: deja de sumar al componente antimaníaco (O y P) y a la dirección Q de contención
once("+P('H1',antH)*.14+P('M1',agon)*.24),","+P('M1',agon)*.24),");
once("+s.HT2An*.14+s.H1n*.14+s.M1a*.24)};","+s.HT2An*.14+s.M1a*.24)};");
once("case'H1':return (an||/antihistam/i.test(s))?['sed','am']:(ag?['act']:[]);","case'H1':return (an||/antihistam/i.test(s))?['sed']:(ag?['act']:[]);");
once('</head>','<style id="patch-v1636">'+read('patch_v1636.css')+'</style></head>');
once(boot,read('patch_v1636.js')+'\n'+boot);
new vm.Script(html.match(/<script>([\s\S]*?)<\/script>/)[1]);
fs.writeFileSync(out,html);
console.log(JSON.stringify({version:'16.36',ancestor,sha256:hash(html),bytes:Buffer.byteLength(html)}));

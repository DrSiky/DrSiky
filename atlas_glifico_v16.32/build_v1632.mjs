// ATLAS GLÍFICO v16.32 · uso: node build_v1632.mjs RUTA/ATLAS_GLIFICO_VISUAL_v16.31.html [SALIDA.html]
// Anclas únicas comprobadas; si una no coincide, aborta sin escribir.
import fs from 'node:fs';import vm from 'node:vm';import crypto from 'node:crypto';
const here=f=>new URL(f,import.meta.url),read=f=>fs.readFileSync(here(f),'utf8');
const hash=s=>crypto.createHash('sha256').update(s).digest('hex');
const src=process.argv[2];if(!src)throw Error('Falta la ruta de ATLAS_GLIFICO_VISUAL_v16.31.html');
const out=process.argv[3]||new URL('../ATLAS_GLIFICO_VISUAL_v16.32.html',import.meta.url).pathname;
let html=fs.readFileSync(src,'utf8');const ancestor=hash(html);
if(ancestor!=='8bfd2fd620c4cb8a72ebb5c7cc06205471bf890901de959aff757f5dca8a45d2')throw Error('El ancestro no es la v16.31 del paquete: '+ancestor);
function once(a,b){const n=html.split(a).length-1;if(n!==1)throw Error('Ancla no única ('+n+'): '+a.slice(0,140));html=html.replace(a,()=>b)}

// 0 · Versión
for(const s of ['Atlas visual v16.31</title>','Atlas visual v16.31 <span',"atlasVersion:'16.31'","a.download='ATLAS_AB_'+el.dataset.abExport+'_v16.31.svg'","link.download='atlas_proyecciones_'+basis+'_v16.31.csv'",'ATLAS GLÍFICO · v16.31 · pauta representada',"ATLAS_ESTRATEGICO_'+key+'_v16.31.svg","el.download='ATLAS_mapa_'+state.lens+'_v16.31.svg'","a.download='ATLAS_espacial_'+state.lens+'_v16.31.svg'"])once(s,s.replace('16.31','16.32'));

// 1 · Capa O: política anti/pro de H1, α1 y M1 (decisión del usuario)
once("function vectorProfile(a){const agon=/\\bagonismo(?! inverso)|facilit/i,ant=/antagon|agonismo inverso|bloque|inhib/i,ad=Math.min(1,g(a,'NET')*.24+g(a,'SERT')*.14+actionSignal(a,'HT1A',agon)*.23+actionSignal(a,'D3',agon)*.16+g(a,'DAT')*.10+g(a,'MAOA')*.13),am=Math.min(1,actionSignal(a,'D2',ant)*.38+actionSignal(a,'D3',ant)*.20+actionSignal(a,'HT2A',ant)*.14+actionSignal(a,'H1',ant)*.14+actionSignal(a,'M1',ant)*.06),sed=Math.min(1,actionSignal(a,'H1',ant)*.58+actionSignal(a,'M1',ant)*.24+actionSignal(a,'A1',ant)*.18),act=Math.min(1,g(a,'NET')*.32+g(a,'DAT')*.25+actionSignal(a,'D3',agon)*.25+actionSignal(a,'HT1A',agon)*.10);return {x:(act-sed)*7,y:(ad-am)*7,ad,am,sed,act}}",
 read('vectorprofile_v1632.js'));

// 2 · Proyecciones P y Q con la misma política
once("const V161_AGON=/\\bagonismo(?! inverso)|facilit/i,V161_ANT=/antagon|agonismo inverso|bloque|inhib/i,V161_INH=",
 "const V161_AGON=/\\bagonismo(?! inverso)|facilit/i,V161_ANT=/antagon|agonismo inverso|bloque|inhib/i,V161_ANT_H1=/antagon|agonismo inverso|bloque|inhib|antihistam/i,V161_ANT_A1=/antagon|agonismo inverso|bloque|inhib|adrenol[ií]tic/i,V161_INH=");
{const a=html.indexOf('function v161P(a){'),b=html.indexOf('function v161QDir',a);if(a<0||b<0)throw Error('v161P no encontrado');html=html.slice(0,a)+read('projectionP_v1632.js')+html.slice(b)}
once("    case'H1':return (an||/antihistam/i.test(s))?['sed','am']:[];\n    case'M1':return an?['sed','am']:[];\n    case'A1':return an?['sed']:[];",
 "    case'H1':return (an||/antihistam/i.test(s))?['sed','am']:(ag?['act']:[]);\n    case'M1':return an?['sed']:(ag?['am']:[]);\n    case'A1':return (an||/adrenol[ií]tic/i.test(s))?['sed']:(ag?['act']:[]);");
once("O · heurística heredada","O · heurística operativa del atlas");
once("O conserva vectorProfile del atlas: una heurística restringida por elegibilidad polar, <b>no PET ni respuesta observada</b>. Por esa restricción puede omitir señales como H1, α1 o M1; P no rellena esas ausencias.",
 "O es vectorProfile del atlas con la política anti/pro de H1, α1 y M1 (v16.32): lee esas dianas por elegibilidad operativa, con dosis, incluidos los ordinales con su magnitud clínica; <b>no es PET ni respuesta observada</b>. P no rellena las ausencias de O. Los pesos de agonistas son espejo de los de sedación, sin calibrar.");

// 3 · Panel funcional H1/α1/M: lectura de agonismo según la política
once("else reading='Se conserva la acción descrita; no se le asigna automáticamente el efecto contrario al bloqueo ni eficacia clínica.';",
 "else if(/\\bagonismo(?! inverso)|\\bagonista|facilit/i.test(action)&&!/antagon/i.test(action))reading=V1632_PRO[group];\n   else reading='Se conserva la acción descrita; no se le asigna automáticamente el efecto contrario al bloqueo ni eficacia clínica.';");

// 4 · Panel de ocupación: correcciones verificadas en la fuente primaria
once(" rab:'https://www.nature.com/articles/1395517.pdf',"," rab:'https://pubmed.ncbi.nlm.nih.gov/10942852/',");
once("Techo fijado al 100 %; no se alcanzó el 50 % dentro del intervalo de dosis. No se mezcla con el seguimiento longitudinal.",
 "Techo fijado al 100 %; no se alcanzó el 50 % dentro del intervalo de dosis (máximo individual 46,7 %). PET 6 h tras dosis única; referencia en sustancia blanca.");
once("Medias por dosis en tálamo; cohortes distintas para SERT y NET.",
 "Valores por dosis en tálamo; cohortes distintas para SERT y NET (6 pacientes cada una). Varios puntos proceden de un solo sujeto (NET 25, 125 y 200 mg; SERT 50 y 200 mg, según la tabla 1).");

// 5 · Módulos nuevos, al final para quedar como capa externa
const boot="$$('[data-view]').forEach(b=>b.onclick=";
once(boot,read('effects_v1632.js')+'\n'+read('memo_v1632.js')+'\n'+boot);

new vm.Script(html.match(/<script>([\s\S]*?)<\/script>/)[1]);
fs.writeFileSync(out,html);
console.log(JSON.stringify({version:'16.32',ancestor,sha256:hash(html),bytes:Buffer.byteLength(html)}));

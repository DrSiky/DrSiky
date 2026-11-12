/* v16.32 · política anti/pro de H1, α1 y M1 en la capa operativa.
   Antagonismo (anti-): H1 → sedación (principal; también apetito), α1 → sedación secundaria (y ortostasis), M1 → sedación leve (y carga antimuscarínica).
   Agonismo (pro-): H1 y α1 → activación (vigilia); M1 → contención (procolinérgico, procognitivo-antipsicótico).
   Estas dianas siguen sin ser 'polares' en los datos; aquí se leen por su elegibilidad operativa, con dosis (value), sin PET ni cualitativos ni metabolitos,
   y descartando textos de baja afinidad, probables, indirectos o preclínicos (los ordinales débiles conservan su magnitud baja). */
const POL_NEG_B=/sin funci[oó]n|funci[oó]n no|no (se )?(infiere|inferible|resuelt|tipific|asign|fiable)|direcci[oó]n (funcional )?no|preclínic|experimental|propuest|hip[oó]tesis|accesori|contextual|indirect|no demostrad|probable|dato no humano|sin agonismo/i,POL_NEG_W=/baja afinidad|afinidad baja|muy baja|d[eé]bil/i;
function policySignal(a,t,re){const cs=(a[t]?.contrib||[]).filter(x=>['parent','component'].includes(x.entityType)&&x.operationalEligible!==false&&!x.petEligible&&!x.qualitative&&re.test(String(x.action))&&!POL_NEG_B.test(String(x.action))&&(x.evidence==='esqueleto ordinal'||x.potencyEligible===false||!POL_NEG_W.test(String(x.action))));return cs.length?1-cs.reduce((p,x)=>p*(1-Math.min(.98,x.value/10)),1):0}
function vectorProfile(a){const agon=/\bagonismo(?! inverso)|facilit/i,ant=/antagon|agonismo inverso|bloque|inhib/i,antH=/antagon|agonismo inverso|bloque|inhib|antihistam/i,antA=/antagon|agonismo inverso|bloque|inhib|adrenol[ií]tic/i,P=(t,re)=>policySignal(a,t,re),
ad=Math.min(1,g(a,'NET')*.24+g(a,'SERT')*.14+actionSignal(a,'HT1A',agon)*.23+actionSignal(a,'D3',agon)*.16+g(a,'DAT')*.10+g(a,'MAOA')*.13),
am=Math.min(1,actionSignal(a,'D2',ant)*.38+actionSignal(a,'D3',ant)*.20+actionSignal(a,'HT2A',ant)*.14+P('H1',antH)*.14+P('M1',agon)*.24),
sed=Math.min(1,P('H1',antH)*.58+P('M1',ant)*.24+P('A1',antA)*.18),
act=Math.min(1,g(a,'NET')*.32+g(a,'DAT')*.25+actionSignal(a,'D3',agon)*.25+actionSignal(a,'HT1A',agon)*.10+P('H1',agon)*.58+P('A1',agon)*.18);
return {x:(act-sed)*7,y:(ad-am)*7,ad,am,sed,act}}
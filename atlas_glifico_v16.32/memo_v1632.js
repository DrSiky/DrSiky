/* v16.32 · Memoización de la resolución de dianas del reconocedor de patrones.
   v1616TargetMatch(slot,target) es una función pura de la definición del patrón y del nombre de la diana,
   pero se recalculaba (normalización de cadenas y alias) para cada patrón × relación en cada evaluate():
   ~60 % del tiempo de evaluate() con 8 fármacos. Se guarda el resultado por (slot, diana) y se devuelve
   una copia superficial, de modo que ningún consumidor comparte el objeto. No cambia ningún resultado. */
const V1632_MATCH=new WeakMap();
const v1632TargetMatchBase=v1616TargetMatch;
v1616TargetMatch=function(slot,target){
 if(!slot||typeof slot!=='object')return v1632TargetMatchBase(slot,target);
 let bySlot=V1632_MATCH.get(slot);if(!bySlot){bySlot=new Map();V1632_MATCH.set(slot,bySlot)}
 const key=String(target);let r=bySlot.get(key);
 if(!r){r=v1632TargetMatchBase(slot,target);bySlot.set(key,r)}
 return {...r};
};

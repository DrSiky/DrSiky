/* v16.33 · Curación de la situación en España contra CIMA (AEMPS), consulta REST del 12-11-2026.
   Corrige contradicciones entre la fuente citada y el estado registrado, y completa la familia que faltaba.
   No toca dianas, potencias, dosis ni PK. */
const V1633_CIMA='consulta CIMA 12-11-2026';
const v1633Cima=q=>'https://cima.aemps.es/cima/rest/medicamentos?'+q;
const V1633_SPAIN={
 Selegilina:{family:'Antiparkinsonianos N04 · IMAO-B',status:'CIMA: Plurimen 5 mg comercializado · '+V1633_CIMA,source:v1633Cima('practiv1=selegilina'),inventory:true,inventoryName:'Selegilina'},
 Rasagilina:{family:'Antiparkinsonianos N04 · IMAO-B',status:'CIMA: 27 presentaciones comercializadas (Azilect y EFG) · '+V1633_CIMA,source:v1633Cima('practiv1=rasagilina'),inventory:true,inventoryName:'Rasagilina'},
 Safinamida:{family:'Antiparkinsonianos N04 · IMAO-B',status:'CIMA: 13 presentaciones comercializadas (Xadago y EFG) · '+V1633_CIMA,source:v1633Cima('practiv1=safinamida'),inventory:true,inventoryName:'Safinamida'},
 Maprotilina:{family:'Antidepresivos N06',status:'CIMA: Ludiomil 25 y 75 mg autorizados con comercialización suspendida · '+V1633_CIMA+'; fuera del inventario activo',source:v1633Cima('practiv1=maprotilina'),inventory:false,inventoryName:'Maprotilina'},
 'Ondansetrón':{status:'CIMA: 30 presentaciones comercializadas · '+V1633_CIMA,inventory:true,inventoryName:'Ondansetrón'},
 'Clorazepato dipotásico':{status:'CIMA: 8 presentaciones comercializadas (Tranxilium y EFG) · '+V1633_CIMA,inventory:true},
 Trihexifenidilo:{status:'CIMA: Artane 2 y 5 mg comercializados · '+V1633_CIMA,inventory:true},
 Flufenazina:{status:'CIMA: sin presentaciones localizadas por principio activo ni por Modecate · '+V1633_CIMA,inventory:false},
 Xanomelina:{status:'Referencia internacional FDA; sin registro en CIMA ('+V1633_CIMA+').',inventory:false}
};
const V1633_FAMILY={Iloperidona:'Antipsicóticos y sedantes N05',Tioridazina:'Antipsicóticos y sedantes N05',Pimavanserina:'Antipsicóticos y sedantes N05',Levomilnacipran:'Antidepresivos N06',Desipramina:'Antidepresivos N06',Vilazodona:'Antidepresivos N06',Tranilcipromina:'Antidepresivos N06'};
for(const [n,patch] of Object.entries(V1633_SPAIN))if(DRUGS[n])DRUGS[n].spain={...(DRUGS[n].spain||{}),...patch};
for(const [n,family] of Object.entries(V1633_FAMILY))if(DRUGS[n]&&!DRUGS[n].spain?.family)DRUGS[n].spain={...(DRUGS[n].spain||{}),family};

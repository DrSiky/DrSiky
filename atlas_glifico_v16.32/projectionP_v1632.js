function v161P(a){
  const T=(t,re)=>v161Take(a,t,re);
  const s={NET:T('NET',V161_INH),DAT:T('DAT',V161_INH),SERT:T('SERT',V161_INH),MAOA:T('MAOA',/inhib/i),HT1Aa:T('HT1A',V161_AGON),D3a:T('D3',V161_AGON),D2n:T('D2',V161_ANT),D3n:T('D3',V161_ANT),HT2An:T('HT2A',V161_ANT),H1n:T('H1',V161_ANT_H1),M1n:T('M1',V161_ANT),A1n:T('A1',V161_ANT_A1),H1a:T('H1',V161_AGON),A1a:T('A1',V161_AGON),M1a:T('M1',V161_AGON)};
  // Coeficientes editoriales heredados; los de los agonistas H1/α1/M1 son espejo de los de sedación. No son tamaños de efecto clínico.
  return {act:Math.min(1,s.NET*.32+s.DAT*.25+s.D3a*.25+s.HT1Aa*.10+s.H1a*.58+s.A1a*.18),sed:Math.min(1,s.H1n*.58+s.M1n*.24+s.A1n*.18),ad:Math.min(1,s.NET*.24+s.SERT*.14+s.HT1Aa*.23+s.D3a*.16+s.DAT*.10+s.MAOA*.13),am:Math.min(1,s.D2n*.38+s.D3n*.20+s.HT2An*.14+s.H1n*.14+s.M1a*.24)};
}

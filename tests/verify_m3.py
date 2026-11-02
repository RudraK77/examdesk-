"""Independent arithmetic/provenance checks for the supplied M3 papers."""
import math,json,hashlib
from fractions import Fraction as F
from pathlib import Path
r=Path(__file__).resolve().parents[1];d=json.loads((r/'assets/m3-data.json').read_text())
assert len(d['papers'])==4 and len(d['questions'])==37
assert {p['date'] for p in d['papers']}=={'10/10/2024','17/10/2024','09/12/2024','06/10/2025'}
assert next(p for p in d['papers'] if p['year']==2025)['type']=='CT2'
assert len({q['id'] for q in d['questions']})==37
assert sum(q['marksInferred'] for q in d['questions'])==19
assert sum(q['marks']==6 for q in d['questions'])==3
assert sum(q['marks']==3 for q in d['questions'])==3
for p in d['papers']:
 for f in p['files']:
  assert (r/'assets/papers'/f).is_file()
  assert f not in ('m3/page-1.png','m3/page-2.png')
for q in d['questions']:
 for k in q['answers']:
  assert len(d['answers'][k]['sections'])>=3
  for s in d['answers'][k]['sections']:
   if s.get('diagram'):assert s['diagram'] in d['diagrams']
# Exact normalisation and moment identities independent of the content generator.
assert F(7,3)*(F(1,9)+2*F(1,18))==F(14,27)
assert F(24)-F(17)**2<0
m1,m2,m3,m4=F(-3,2),F(17),F(-30),F(108)
v=m2-m1*m1;c3=m3-3*m1*m2+2*m1**3;c4=m4-4*m1*m3+6*m1*m1*m2-3*m1**4
assert (v,c3,c4)==(F(59,4),F(159,4),F(2277,16)) and c4<v*v
assert F(6,29)*(F(7,3)+F(5,2))==1
# Regression must pass through the means and leave zero x-weighted residual sum.
x=[5,6,7,8,9,10,11];y=[11,14,14,15,12,17,16];b=F(19,28);a=F(61,7)
assert sum(F(j)-a-b*i for i,j in zip(x,y))==0
assert sum(i*(F(j)-a-b*i) for i,j in zip(x,y))==0
text=d['answers']['regression']['text'];assert '19/28' in text and 'Σxy=811' in text
obs=[38,144,342,287,164,25];p=F(sum(i*f for i,f in enumerate(obs)),5*sum(obs));assert p==F(247,500)
expected=[1000*math.comb(5,k)*float(p)**k*(1-float(p))**(5-k) for k in range(6)]
chi=sum((o-e)**2/e for o,e in zip(obs,expected));assert abs(chi-8.16162743206)<1e-9 and chi<9.488
assert math.isclose(math.exp(-100+4*math.log(100)-math.lgamma(5)),1.5500316566753483e-37,rel_tol=1e-12)
assert math.isclose(1200*.5*math.erfc((70-55)/4.5/math.sqrt(2)),.5148723998362048)
assert 800*(1-1/32)==775
assert math.isclose(sum(math.comb(240,k)*.03**k*.97**(240-k) for k in range(6)),.2718636828123408)
assert hashlib.sha256((r/'assets/data.json').read_bytes()).hexdigest()=='4fa4a6e0b06d08c6a6ba3d5971c604f48e7171ae2714a7b18550ba41300e373b'
print('PASS: M3 sources/marks, invalid-density checks, moments, regression, binomial fit, tails, and unchanged OS data.')

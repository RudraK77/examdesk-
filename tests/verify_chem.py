import json, math
from pathlib import Path
from collections import Counter
r=Path(__file__).resolve().parents[1];a=r/'assets';d=json.loads((a/'chem-data.json').read_text())
assert len(d['questions'])==46 and len(d['papers'])==5 and len(d['diagrams'])==15
assert Counter(q['paper'] for q in d['questions'])=={'chem-ct1-23':5,'chem-ct2-23':5,'chem-end-23':15,'chem-ct1-24':6,'chem-end-25':15}
assert len({q['id'] for q in d['questions']})==46
assert len(d['notes'])==7
papers={p['id']:p for p in d['papers']};notes={n['id']:n for n in d['notes']}
for p in d['papers']:
 for f in p['files']:assert (a/'papers'/f).is_file(),f
for n in d['notes']:assert (a/'notes/chem'/n['file']).is_file()
for q in d['questions']:
 assert q['page'] in papers[q['paper']]['sourcePages']
 assert q['marks'] in (3,4,6)
 for k in q['answers']:
  ans=d['answers'][k];assert ans['sections'] and ans['text']
  for s in ans['sections']:
   assert isinstance(s['paragraphs'],list) and isinstance(s['bullets'],list)
   if 'diagram' in s:assert s['diagram'] in d['diagrams']
   if 'table' in s:assert all(len(row)==len(s['table']['headers']) for row in s['table']['rows'])
  for ref in ans['references']:assert ref['note'] in notes
assert sum(q['marksInferred'] for q in d['questions'])==9
assert papers['chem-end-25']['year']==2025
js=(a/'chem-data.js').read_text();assert json.loads(js.removeprefix('window.CHEM_DATA=').strip().removesuffix(';'))==d
# Independently calculated expected calorimeter results (cal/g).
expected={'cal23ct':(6040,6004.646271510516),'cal23a':(6531.578947368421,6135.353947368421),'cal23b':(7168.478260869565,7168.165060869565),'cal25':(7168.478260869565,6851.498260869565)}
for k,(g,n) in expected.items():
 text=d['answers'][k]['text'];assert f'{g:.2f}' in text,(k,g);assert f'{n:.2f}' in text,(k,n)
assert '17.65%' in d['answers']['atom']['text'] and '45.90%' in d['answers']['atom']['text']
assert '+0.75 V' in d['answers']['emf24']['text'] and '−1.800 V' in d['answers']['emf24']['text']
# Cell reaction atom counts, electrons and charge, checked from explicit species vectors.
# Each vector: atoms relevant to that system followed by electric charge.
checks=[
 ({'Cd':1,'OH':2},{'CdOH2':1,'e':2},{'Cd':(1,0,0,0),'OH':(0,1,1,-1),'CdOH2':(1,2,2,0),'e':(0,0,0,-1)}),
 ({'NiOOH':2,'H2O':2,'e':2},{'NiOH2':2,'OH':2},{'NiOOH':(1,2,1,0),'H2O':(0,1,2,0),'e':(0,0,0,-1),'NiOH2':(1,2,2,0),'OH':(0,1,1,-1)}),
 ({'H2':2,'OH':4},{'H2O':4,'e':4},{'H2':(2,0,0),'OH':(1,1,-1),'H2O':(2,1,0),'e':(0,0,-1)}),
 ({'O2':1,'H2O':2,'e':4},{'OH':4},{'O2':(0,2,0),'H2O':(2,1,0),'e':(0,0,-1),'OH':(1,1,-1)})]
for lhs,rhs,v in checks:
 for i in range(len(next(iter(v.values())))):assert sum(n*v[k][i] for k,n in lhs.items())==sum(n*v[k][i] for k,n in rhs.items())
print('PASS: chemistry source coverage, marks, references, all assets, bundle consistency, independent numerical results and half-reaction balances.')

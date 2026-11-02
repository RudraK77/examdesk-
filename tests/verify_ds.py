"""Validate provenance, distinct-paper counts, answer references and examples."""
import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
d=json.loads((root/'assets/ds-data.json').read_text())
assert len(d['papers'])==6 and len(d['questions'])==38
assert len({q['id'] for q in d['questions']})==38
assert len(d['answers'])==26 and len(d['diagrams'])==10
for p in d['papers']:
 assert all((root/'assets/papers'/f).is_file() for f in p['files'])
 if p['type']!='End Semester':assert p['year'] is None and p['date'] is None
 else:assert p['date']=='16/12/2024' and p['files']==['ds/page-3.png','ds/page-2.png']
for q in d['questions']:
 assert q['marks']==(6 if q['paper']=='ds-end-24' else 5)
 for k in q['answers']:
  for section in d['answers'][k]['sections']:
   if section.get('diagram'):assert section['diagram'] in d['diagrams']
assert len({q['paper'] for q in d['questions'] if q['family']=='queue-array'})==3
assert len({q['paper'] for q in d['questions'] if q['family']=='notation'})==3
assert hashlib.sha256((root/'assets/data.json').read_bytes()).hexdigest()=='4fa4a6e0b06d08c6a6ba3d5971c604f48e7171ae2714a7b18550ba41300e373b'
# Independently evaluate the traversal example.
t=('A',('B',('D',None,None),('E',None,None)),('C',None,('F',None,None)))
def order(t,mode):
 if not t:return ''
 a,l,r=t
 return a+order(l,mode)+order(r,mode) if mode=='pre' else order(l,mode)+a+order(r,mode) if mode=='in' else order(l,mode)+order(r,mode)+a
assert [order(t,m) for m in ('pre','in','post')]==['ABDECF','DBEACF','DEBFCA']
# Verify the shown order-4 B-tree: capacity, sorted ranges, final keys.
rootkeys=[10,20];children=[[5,6,7],[12,17],[30]]
assert all(1<=len(c)<=3 and c==sorted(c) for c in children)
assert max(children[0])<10<min(children[1])<=max(children[1])<20<min(children[2])
assert sorted(rootkeys+sum(children,[]))==sorted([10,20,5,6,12,30,7,17])
print('PASS: DS provenance, source references, marks, recurrence, diagrams, traversal and B-tree examples; OS checksum preserved.')

"""Evidence integrity and independent numerical checks. Run from project root."""
import json
from pathlib import Path
D=json.loads(Path('assets/data.json').read_text())
ps={p['id']:p for p in D['papers']}
assert len(ps)==6 and len(D['questions'])==34
assert ps['ct1-u']['year'] is None and ps['ct1-u']['date'] is None
assert ps['end-24']['date'] is None and len(ps['end-24']['files'])==2
assert len({q['id'] for q in D['questions']})==34
for q in D['questions']:
    assert q['paper'] in ps
    assert q['marks']==(6 if q['paper']=='end-24' else 5)
    assert q['original'] and all(k in D['answers'] for k in q['answers'])
for p in ps.values():
    assert all((Path('assets/papers')/f).is_file() for f in p['files'])
# Confirm JS bundle exactly matches editable JSON.
assert json.loads(Path('assets/data.js').read_text().removeprefix('window.EXAM_DATA = ').strip().removesuffix(';'))==D
# LRU: independent recency list simulation, oldest first.
resident=[];faults=0
for v in [6,1,1,2,0,3,4,6,0,2,1,2,3,2]:
    if v in resident: resident.remove(v)
    else:
        faults+=1
        if len(resident)==3: resident.pop(0)
    resident.append(v)
assert faults==11
# SSTF from the printed end-sem data.
head=53;pending=[98,183,37,122,14,124,65,67];movement=0
while pending:
    nxt=min(pending,key=lambda x:abs(x-head));movement+=abs(nxt-head);head=nxt;pending.remove(nxt)
assert movement==236
assert (4//2,4%2,5*2+4%2)==(2,0,10)
# Priority, larger number first; FCFS ties.
rows=[(0,4,2),(1,3,3),(2,1,4),(3,5,5),(4,2,5)]
t=0;remaining=list(range(5));finish={}
while remaining:
    ready=[i for i in remaining if rows[i][0]<=t]
    i=min(ready,key=lambda i:(-rows[i][2],rows[i][0],i))
    t+=rows[i][1];finish[i]=t;remaining.remove(i)
tat=[finish[i]-r[0] for i,r in enumerate(rows)]
assert sum(tat)/5==8.2
assert sum(tat[i]-r[1] for i,r in enumerate(rows))/5==5.2
# FCFS / nonpreemptive SJF / SRTF, stable ties.
rows=[(3,1),(1,4),(4,2),(0,6),(2,3)]
for mode,expected in [('fcfs',9.8),('sjf',8.0),('srtf',7.0)]:
    left=[r[1] for r in rows];end={};t=0;current=None
    while len(end)<5:
        ready=[i for i in range(5) if rows[i][0]<=t and left[i]>0]
        if not ready:t+=1;continue
        if mode=='fcfs':pick=min(ready,key=lambda i:(rows[i][0],i))
        else:pick=min(ready,key=lambda i:(left[i],0 if i==current else 1,rows[i][0],i))
        if mode!='srtf' and current in ready:pick=current
        current=pick;left[pick]-=1;t+=1
        if left[pick]==0:end[pick]=t;current=None
    assert sum(end[i]-rows[i][0] for i in range(5))/5==expected
print('PASS: provenance, bundle consistency, LRU, SSTF, paging, priority, FCFS, SJF and SRTF.')

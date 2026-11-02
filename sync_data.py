import json
from pathlib import Path
root=Path(__file__).resolve().parent/'assets'
data=json.loads((root/'data.json').read_text())
(root/'data.js').write_text('window.EXAM_DATA = '+json.dumps(data,ensure_ascii=False)+';\n')
print('Updated local content bundle.')

# Keep the additional subject bundle in sync too.
ds=Path(__file__).resolve().parent/"assets"/"ds-data.json"
if ds.exists():
    ds.with_suffix(".js").write_text("window.DS_DATA="+json.dumps(json.loads(ds.read_text()),ensure_ascii=False)+";\n")

m3=root/"m3-data.json"
if m3.exists():
    m3.with_suffix(".js").write_text("window.M3_DATA="+json.dumps(json.loads(m3.read_text()),ensure_ascii=False)+";\n")

chem=root/'chem-data.json'
if chem.exists():
    chem.with_suffix('.js').write_text('window.CHEM_DATA='+json.dumps(json.loads(chem.read_text()),ensure_ascii=False)+';\n')

pps=root/'pps-data.json'
if pps.exists():
    pps.with_suffix('.js').write_text('window.PPS_DATA='+json.dumps(json.loads(pps.read_text()),ensure_ascii=False)+';\n')

iks=root/'iks-data.json'
if iks.exists():
    iks.with_suffix('.js').write_text('window.IKS_DATA='+json.dumps(json.loads(iks.read_text()),ensure_ascii=False)+';\n')

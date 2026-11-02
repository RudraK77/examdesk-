import base64,json
from pathlib import Path
root=Path(__file__).resolve().parent
assets=root/'assets'
html=(assets/'index.html').read_text()
theme=(assets/'theme.css').read_text()
for font in (assets/'fonts').glob('*.ttf'):
    theme=theme.replace('fonts/'+font.name,'data:font/ttf;base64,'+base64.b64encode(font.read_bytes()).decode())
css=(assets/'style.css').read_text().replace("@import url('theme.css');",theme)
html=html.replace('<link rel="stylesheet" href="style.css">','<style>'+css+'</style>')
scans={p.relative_to(assets/'papers').as_posix():'data:image/'+('png' if p.suffix=='.png' else 'jpeg')+';base64,'+base64.b64encode(p.read_bytes()).decode() for p in (assets/'papers').rglob('*') if p.suffix.lower() in ('.png','.jpg','.jpeg')}
js=(assets/'app.js').read_text().replace('src="papers/${f}"','src="${window.SCAN_FILES[f]}"')
notes={p.name:base64.b64encode(p.read_bytes()).decode() for p in (assets/'notes'/'chem').glob('*.pdf')}
script='window.NOTE_FILES='+json.dumps(notes)+';\n'+'window.SCAN_FILES='+json.dumps(scans)+';\n'+(assets/'data.js').read_text()+'\n'+(assets/'m3-data.js').read_text()+'\n'+(assets/'ds-data.js').read_text()+'\n'+(assets/'chem-data.js').read_text()+'\n'+(assets/'pps-data.js').read_text()+'\n'+(assets/'iks-data.js').read_text()+'\n'+(assets/'components.js').read_text()+'\n'+js
html=html.replace('<script src="data.js"></script><script src="ds-data.js"></script><script src="m3-data.js"></script><script src="chem-data.js"></script><script src="pps-data.js"></script><script src="iks-data.js"></script><script src="components.js"></script><script src="app.js"></script>','<script>'+script.replace('</script','<\\/script')+'</script>')
(root.parent/'Exam-Desk-Offline.html').write_text(html)
print('Created self-contained offline app.')

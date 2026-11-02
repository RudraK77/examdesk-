"""Generate Android platform files without overwriting the application sources."""
from pathlib import Path
import shutil, subprocess, tempfile, sys
root = Path(__file__).resolve().parent
if not shutil.which('flutter'):
    raise SystemExit('Flutter is not on PATH. Install Flutter stable and Android SDK first.')
if not (root / 'android').exists():
    with tempfile.TemporaryDirectory(prefix='exam-desk-') as tmp:
        shell = Path(tmp) / 'exam_desk'
        subprocess.run(['flutter','create','--platforms=android','--org=dev.examdesk',
                        '--project-name=exam_desk',str(shell)],check=True)
        shutil.copytree(shell/'android', root/'android')
subprocess.run([sys.executable,str(root/'prepare_android.py')],cwd=root,check=True)
subprocess.run(['flutter','pub','get'],cwd=root,check=True)
print('Ready. Run: flutter analyze && flutter build apk --debug')

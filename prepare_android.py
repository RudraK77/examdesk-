"""Run after flutter create --platforms=android --project-name exam_desk ."""
from pathlib import Path
import re
p = Path('android/app/build.gradle.kts')
if not p.exists():
    raise SystemExit('Run flutter create --platforms=android --project-name exam_desk . first.')
s = p.read_text()
s, n = re.subn(r'minSdk\s*=\s*flutter.minSdkVersion', 'minSdk = 24', s)
if not n and not re.search(r'minSdk\s*=\s*(2[4-9]|[3-9][0-9])', s):
    raise SystemExit('Set minSdk to at least 24 in android/app/build.gradle.kts.')
p.write_text(s)
p = Path('android/app/src/main/AndroidManifest.xml')
s = p.read_text().replace('android:label="exam_desk"', 'android:label="Exam Desk"')
p.write_text(s)
print('Android minimum SDK: 24. App label: Exam Desk.')

from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
files=[root/'index.html',root/'about.html',root/'insights.html',root/'contact.html']+list((root/'sectors').glob('*.html'))
for path in files:
    text=path.read_text(encoding='utf-8')
    if '<title>' not in text or 'viewport' not in text: raise SystemExit(f'Missing metadata: {path}')
    for ref in re.findall(r'(?:src|href)=["\']([^"\']+)["\']',text):
        if ref.startswith(('http','#','mailto:','tel:','javascript:')): continue
        target=(path.parent/ref).resolve()
        if not target.exists(): raise SystemExit(f'Missing local reference {ref} in {path}')
print(f'Validated {len(files)} HTML pages and local references.')

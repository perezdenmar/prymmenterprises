from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
for page in [root/'index.html',root/'about.html',root/'contact.html',root/'journal.html']+list((root/'sectors').glob('*.html')):
    if not page.exists(): continue
    text=page.read_text(encoding='utf-8')
    if '<title>' not in text or 'viewport' not in text: raise SystemExit(f'Metadata missing: {page}')
    for ref in re.findall(r'(?:src|href)=["\']([^"\']+)["\']',text):
        if ref.startswith(('http','#','mailto:','tel:','javascript:')): continue
        if not (page.parent/ref).exists(): raise SystemExit(f'Missing reference {ref} in {page}')
print('Dark Industrial Modernism site checks passed.')

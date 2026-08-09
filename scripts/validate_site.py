from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
refs=re.findall(r'(?:src|href)=["\']([^"\']+)["\']',html)
missing=[]
for ref in refs:
    if ref.startswith(('http','#','mailto:','javascript:')): continue
    if not (root/ref).exists(): missing.append(ref)
if missing: raise SystemExit('Missing local references: '+', '.join(missing))
for image in (root/'assets/images').glob('*'):
    if image.is_file() and image.stat().st_size < 1024: raise SystemExit(f'Image is unexpectedly small: {image}')
for required in ['alt=','loading="lazy"','fetchpriority="high"','color-scheme','prefers-reduced-motion']:
    if required not in html: raise SystemExit(f'Missing requirement: {required}')
print('Site reference, asset-size, accessibility, and motion checks passed.')

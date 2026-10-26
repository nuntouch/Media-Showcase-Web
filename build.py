"""Prepare Cloudflare Pages output; keep originals in the source project."""
from pathlib import Path
import shutil
root=Path(__file__).resolve().parent
out=root/'dist'
if out.exists(): shutil.rmtree(out)
out.mkdir()
for name in ('index.html','styles.css','app.js','data.js'):
    shutil.copy2(root/name,out/name)
shutil.copytree(root/'assets',out/'assets',ignore=shutil.ignore_patterns('.DS_Store'))
(out/'Pic').mkdir()
for name in ('01.jpg','02.jpg','03.jpg','04.jpg'):
    shutil.copy2(root/'Pic'/name,out/'Pic'/name)
shutil.copytree(root/'Pic'/'Enlivening',out/'Pic'/'Enlivening',ignore=shutil.ignore_patterns('*.mov','.DS_Store'))
shutil.copytree(root/'Pic'/'Home-Shelf',out/'Pic'/'Home-Shelf',ignore=shutil.ignore_patterns('.DS_Store'))
shutil.copytree(root/'Pic'/'Top-Aisle',out/'Pic'/'Top-Aisle',ignore=shutil.ignore_patterns('*.mp4','.DS_Store'))
shutil.copytree(root/'Pic'/'Special',out/'Pic'/'Special',ignore=shutil.ignore_patterns('.DS_Store'))
for path in out.rglob('*'):
    if path.is_file() and path.stat().st_size>25*1024*1024:
        raise RuntimeError(f'Asset too large: {path.name}')
print('Static output ready in dist/')

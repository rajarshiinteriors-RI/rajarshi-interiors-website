#!/usr/bin/env python3
"""Compile Pages CMS JSON content into the static website data file."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
site=json.loads((root/'content/site.json').read_text(encoding='utf-8'))
projects=[]
for file in sorted((root/'content/projects').glob('*.json')):
    item=json.loads(file.read_text(encoding='utf-8'))
    if item.get('published',True):
        projects.append(item)
site['projects']=projects
payload=json.dumps(site,ensure_ascii=False).replace('<','\u003c').replace('>','\u003e').replace('&','\u0026')
(root/'site-data.js').write_text('window.SITE = '+payload+';\n',encoding='utf-8')
print('Built',len(projects),'project entries')

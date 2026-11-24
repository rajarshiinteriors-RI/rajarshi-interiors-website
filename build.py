
#!/usr/bin/env python3
"""Build Rajarshi Interiors website data."""

import json
from pathlib import Path

root = Path(__file__).resolve().parent

site = json.loads(
    (root / "site.json").read_text(encoding="utf-8")
)

projects = []

for filename in ["kitchen.json", "living.json", "wardrobe.json"]:
    file = root / filename
    if file.exists():
        item = json.loads(file.read_text(encoding="utf-8"))
        if item.get("published", True):
            projects.append(item)

site["projects"] = projects

payload = json.dumps(
    site, ensure_ascii=False
).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")

(root / "site-data.js").write_text(
    "window.SITE = " + payload + ";\n",
    encoding="utf-8"
)

print(f"Built {len(projects)} project entries")

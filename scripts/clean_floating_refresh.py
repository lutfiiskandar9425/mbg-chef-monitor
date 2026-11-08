# -*- coding: utf-8 -*-
import os
import re

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove floating-refresh-btn
    pattern = r'<!-- FLOATING QUICK REFRESH BUTTON.*?<button onclick="forceRefreshApp\(\)" id="floating-refresh-btn".*?</button>'
    content = re.sub(pattern, '', content, flags=re.DOTALL)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{fn}] Removed floating refresh button.")

print("Done.")

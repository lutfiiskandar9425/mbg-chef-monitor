# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'sheet' in line.lower() or 'sync' in line.lower() or 'gas' in line.lower() or 'exec' in line.lower():
        print(f"{i+1}: {line.strip()[:100]}")


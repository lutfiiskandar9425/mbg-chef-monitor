# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'aslap' in line.lower() or 'penerimaan' in line.lower():
        print(f"{i+1}: {line.strip()[:100]}")


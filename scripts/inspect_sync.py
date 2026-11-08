# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(2690, min(2750, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')


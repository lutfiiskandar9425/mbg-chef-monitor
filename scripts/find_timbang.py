# -*- coding: utf-8 -*-
import re

with open('preview.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

timbang_lines = []
for i, line in enumerate(lines):
    if any(k in line.lower() for k in ['timbang', 'foto', 'kamera', 'camera', 'capture', 'file']):
        timbang_lines.append((i+1, line.strip()[:120]))

print(f"Found {len(timbang_lines)} matching lines. Showing sample around features:")
for lno, text in timbang_lines[:40]:
    print(f"{lno}: {text}")

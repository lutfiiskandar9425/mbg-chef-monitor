# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== HTML around line 330-410 ===")
for i in range(330, min(420, len(lines))):
    print(f"{i+1}: {lines[i]}", end='')

print("\n=== triggerCameraOCR search ===")
for i, line in enumerate(lines):
    if 'triggerCameraOCR' in line or 'function triggerCameraOCR' in line or 'OCR' in line:
        print(f"{i+1}: {line.strip()[:100]}")


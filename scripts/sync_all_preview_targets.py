# -*- coding: utf-8 -*-
import os
import shutil

source = os.path.abspath('preview.html')
targets = [
    r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html',
    r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\preview.html',
    r'C:\Users\HP\Projects\APlikasi MBG\mbg_kitchen_monitor_preview.html'
]

print(f"Source: {source} (Size: {os.path.getsize(source)} bytes)")

for t in targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    shutil.copyfile(source, t)
    print(f"Copied to: {t} (Size: {os.path.getsize(t)} bytes)")

print("All preview files synchronized successfully!")

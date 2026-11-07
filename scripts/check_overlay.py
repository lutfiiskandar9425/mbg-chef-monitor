import re

with open(r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html', encoding='utf-8') as f:
    html = f.read()

for m in re.findall(r'class="[^"]*(?:fixed|absolute|z-\d+)[^"]*"', html):
    print(m)


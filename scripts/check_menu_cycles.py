import re

with open('preview.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'let weeklyMenuCycles = (\{.*?\n  \});', text, re.DOTALL)
if m:
    content = m.group(1)
    for line in content.splitlines():
        if 'title:' in line or 'senin:' in line or 'selasa:' in line or 'rabu:' in line or 'kamis:' in line or 'jumat:' in line or 'name:' in line:
            print(line[:90])


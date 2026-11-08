# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'onclick="([^"]*station[^"]*)"', c, re.IGNORECASE)
print("Station onclicks:", set(matches))

matches2 = re.findall(r'function \w*station\w*', c, re.IGNORECASE)
print("Station functions:", set(matches2))


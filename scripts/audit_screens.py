# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re

screens = re.findall(r'<section id="(screen-[^"]+)"', c)
print("Defined screens:", screens)

# Check screen-stock content
idx_stock = c.find('id="screen-stock"')
if idx_stock != -1:
    print("\n=== screen-stock snippet ===")
    print(c[idx_stock:idx_stock+1200])

# Check tabs
tabs = re.findall(r'id="(tab-btn-[^"]+)"', c)
print("\nDefined tab buttons:", tabs)


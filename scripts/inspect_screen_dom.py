# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('DIGITAL SCALE READOUT DISPLAY')
print(c[idx:idx+2000])

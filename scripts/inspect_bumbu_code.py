# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx1 = c.find('function updateStickyNoteContent')
print(c[idx1+7000:idx1+9000])

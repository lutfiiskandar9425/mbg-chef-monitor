# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx1 = c.find('function updateStickyNoteContent')
print('=== updateStickyNoteContent ===')
print(c[idx1:idx1+1400])

idx2 = c.find('function openFullDirectiveModal')
print('=== openFullDirectiveModal ===')
print(c[idx2:idx2+2000])


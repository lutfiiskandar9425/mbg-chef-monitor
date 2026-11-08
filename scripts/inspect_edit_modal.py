# -*- coding: utf-8 -*-
with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="edit-cart-modal"')
print(c[idx+1000:idx+2500])

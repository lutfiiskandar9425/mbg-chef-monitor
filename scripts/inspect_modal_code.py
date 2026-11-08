# -*- coding: utf-8 -*-
files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    has_sb = 'const schoolBatchesData = {' in c
    has_wm = 'weeklyMenuCycles = {' in c
    has_usnc = 'function updateStickyNoteContent' in c
    has_ofdm = 'function openFullDirectiveModal' in c
    print(f"{fn}: sb={has_sb}, wm={has_wm}, usnc={has_usnc}, ofdm={has_ofdm}, len={len(c)}")

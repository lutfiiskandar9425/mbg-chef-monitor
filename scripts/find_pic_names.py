import re

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']
pattern = re.compile(r'(Yudi|Ikbal|Rizal|Ricky|Linda|Faiz|Abidin)', re.IGNORECASE)

for fpath in files:
    print('='*50)
    print('FILE:', fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
            if pattern.search(line):
                print(f'{idx}: {line.strip()[:110]}')

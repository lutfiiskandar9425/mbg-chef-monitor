with open('preview.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[625:720], start=626):
    print(f'{i}: {l}', end='')


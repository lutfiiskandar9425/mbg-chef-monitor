with open('preview.html', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f, start=1):
        if 'arahan' in line.lower():
            print(f'{idx}: {line.strip()[:100]}')


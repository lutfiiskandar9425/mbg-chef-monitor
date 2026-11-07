from bs4 import BeautifulSoup
with open(r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

imgs = soup.find_all('img')
print(f'Total img tags found: {len(imgs)}')
for i, img in enumerate(imgs):
    src = img.get('src', '')
    print(f'Img {i}: alt={img.get("alt")}, src_prefix={src[:40]}... (len {len(src)})')


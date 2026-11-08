import urllib.request
import re

html = urllib.request.urlopen('https://lutfiiskandar9425.github.io/mbg-chef-monitor/').read().decode('utf-8')
print("Cycle buttons in live HTML:")
for b in re.findall(r'<button[^>]*>(.*?)</button>', html):
    if 'Siklus' in b:
        print(" -", re.sub(r'<[^>]+>', '', b).strip())

print("\nCycle titles in JS:")
for t in re.findall(r'title:\s*"(.*?)"', html)[:5]:
    print(" -", t)

print("\nHero title:")
m = re.search(r'<h2[^>]*id="hero-menu-title"[^>]*>(.*?)</h2>', html, re.DOTALL)
if m:
    print(" - Hero:", re.sub(r'<[^>]+>', '', m.group(1)).strip())


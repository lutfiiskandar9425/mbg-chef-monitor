path = r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

s_idx = c.rfind('<script>')
e_idx = c.rfind('</script>')
js_code = c[s_idx+8:e_idx]
print('JS length:', len(js_code))

# Print last 500 chars of JS
print('Tail of JS:\n', js_code[-500:])

with open('scripts/extracted.js', 'w', encoding='utf-8') as f_out:
    f_out.write(js_code)
print('Wrote scripts/extracted.js')

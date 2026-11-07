import re

with open(r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html', encoding='utf-8') as f:
    html = f.read()

# Find all onclick
onclicks = re.findall(r'onclick="([^"]+)"', html)
print('Total onclick attributes:', len(onclicks))

# Find all function definitions in <script>
script_match = re.search(r'<script>(.*?)</script>', html, re.DOTALL)
if script_match:
    script = script_match.group(1)
    func_names = set(re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', script))
    print('Defined functions:', sorted(list(func_names)))
    
    for oc in set(onclicks):
        # Extract function call name
        m = re.match(r'([a-zA-Z0-9_]+)\s*\(', oc)
        if m:
            fname = m.group(1)
            if fname not in func_names and fname not in ['document', 'alert']:
                print('MISSING FUNCTION:', fname, 'in', oc)
        else:
            print('Inline JS in onclick:', oc)


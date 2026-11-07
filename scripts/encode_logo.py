import base64
import os

root_dir = r'C:\Users\HP\Projects\APlikasi MBG'
logo_path = os.path.join(root_dir, 'bgn_logo_master.png')
html_path = r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html'

with open(logo_path, 'rb') as f:
    b64_data = base64.b64encode(f.read()).decode('utf-8')

data_uri = f'data:image/png;base64,{b64_data}'

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace any occurrence of ./bgn_logo.png or bgn_logo.png with the inline data URI
if './bgn_logo.png' in html_content:
    html_content = html_content.replace('./bgn_logo.png', data_uri)
    print('Replaced ./bgn_logo.png with base64 data URI')
elif 'bgn_logo.png' in html_content:
    html_content = html_content.replace('bgn_logo.png', data_uri)
    print('Replaced bgn_logo.png with base64 data URI')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated mbg_kitchen_monitor_preview.html with self-contained inline logo!')


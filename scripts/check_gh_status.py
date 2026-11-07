import urllib.request, json, os
token = os.environ.get('GH_TOKEN', '')
req = urllib.request.Request('https://api.github.com/user', headers={'Authorization': f'token {token}', 'User-Agent': 'PowerShell'})
try:
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode())
except Exception as e:
    print('Error:', e)
    if hasattr(e, 'read'):
        print(e.read().decode())


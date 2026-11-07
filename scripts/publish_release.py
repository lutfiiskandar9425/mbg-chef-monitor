import urllib.request
import json
import os
import sys

token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN') or (sys.argv[1] if len(sys.argv) > 1 else '')
if not token:
    print('Warning: No GITHUB_TOKEN provided. Set GITHUB_TOKEN environment variable or pass as argument.')
repo = 'lutfiiskandar888-svg/mbg-chef-monitor'
apk_path = r'C:\Users\HP\Projects\APlikasi MBG\apk_output\app-release.apk'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'Python-Release-Uploader'
}

# 1. Create or get Release
url = f'https://api.github.com/repos/{repo}/releases'
payload = json.dumps({
    'tag_name': 'v1.0.0',
    'target_commitish': 'main',
    'name': 'MBG Chef Monitor v1.0.0',
    'body': 'Aplikasi Android MBG Kitchen Monitor (Release APK siap pakai)',
    'draft': False,
    'prerelease': False
}).encode('utf-8')

upload_url = None
try:
    req = urllib.request.Request(url, data=payload, headers=headers)
    with urllib.request.urlopen(req) as resp:
        rel = json.loads(resp.read().decode())
        upload_url = rel['upload_url'].split('{')[0]
        print('Created release:', rel['html_url'])
except Exception as e:
    print('Release might exist, fetching:', e)
    req_get = urllib.request.Request(f'https://api.github.com/repos/{repo}/releases/tags/v1.0.0', headers=headers)
    with urllib.request.urlopen(req_get) as resp:
        rel = json.loads(resp.read().decode())
        upload_url = rel['upload_url'].split('{')[0]
        print('Found release:', rel['html_url'])

# 2. Upload APK Asset
upload_url_with_name = f'{upload_url}?name=mbg-chef-monitor.apk'
print(f'Reading APK from {apk_path} ({os.path.getsize(apk_path)} bytes)...')
with open(apk_path, 'rb') as f:
    apk_data = f.read()

upload_headers = {
    'Authorization': f'token {token}',
    'Content-Type': 'application/vnd.android.package-archive',
    'User-Agent': 'Python-Release-Uploader'
}

req_upload = urllib.request.Request(upload_url_with_name, data=apk_data, headers=upload_headers)
with urllib.request.urlopen(req_upload) as resp:
    asset = json.loads(resp.read().decode())
    print('Uploaded APK successfully!')
    print('Direct Download URL:', asset.get('browser_download_url'))


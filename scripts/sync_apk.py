import urllib.request, json, zipfile, io, os

token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN') or (sys.argv[1] if len(sys.argv) > 1 else '')
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'PowerShell'
}

artifact_url = 'https://api.github.com/repos/lutfiiskandar888-svg/mbg-chef-monitor/actions/artifacts/13369751194/zip'
print('Downloading artifact zip...')
class NoAuthRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new_req = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new_req and 'blob.core.windows.net' in newurl:
            if 'Authorization' in new_req.headers:
                del new_req.headers['Authorization']
        return new_req

opener = urllib.request.build_opener(NoAuthRedirectHandler)
req = urllib.request.Request(artifact_url, headers=headers)
with opener.open(req) as resp:
    zip_bytes = resp.read()

out_dir = r'C:\Users\HP\Projects\APlikasi MBG\apk_output'
os.makedirs(out_dir, exist_ok=True)
with zipfile.ZipFile(io.BytesIO(zip_bytes)) as z:
    z.extractall(out_dir)

apk_file = os.path.join(out_dir, 'app-release.apk')
print(f'Extracted APK: {apk_file}, size: {os.path.getsize(apk_file):,} bytes')

rel_url = 'https://api.github.com/repos/lutfiiskandar888-svg/mbg-chef-monitor/releases/tags/v1.0.0'
req = urllib.request.Request(rel_url, headers=headers)
with urllib.request.urlopen(req) as resp:
    rel = json.loads(resp.read().decode())
    upload_url = rel['upload_url'].split('{')[0]
    for asset in rel.get('assets', []):
        if asset['name'] == 'mbg-chef-monitor.apk':
            del_url = asset['url']
            print('Deleting old release asset:', asset['id'])
            del_req = urllib.request.Request(del_url, headers=headers, method='DELETE')
            urllib.request.urlopen(del_req)

upload_url_with_name = f'{upload_url}?name=mbg-chef-monitor.apk'
print('Uploading new APK to release...')
with open(apk_file, 'rb') as f:
    apk_data = f.read()

up_headers = {
    'Authorization': f'token {token}',
    'Content-Type': 'application/vnd.android.package-archive',
    'User-Agent': 'PowerShell'
}
up_req = urllib.request.Request(upload_url_with_name, data=apk_data, headers=up_headers)
with urllib.request.urlopen(up_req) as resp:
    res = json.loads(resp.read().decode())
    print('Release asset successfully updated!')
    print('Download URL:', res.get('browser_download_url'))

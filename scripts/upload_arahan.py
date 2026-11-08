import glob
import subprocess
import os

folder_id = "14ry1XubijGmI7BhIfvDPXFf02lOrQy8c"
pdf_files = sorted(glob.glob(r"C:\Users\HP\Projects\APlikasi MBG\arahan_senin\*.pdf"))

for pdf in pdf_files:
    fname = os.path.basename(pdf)
    print(f"Uploading {fname}...")
    cmd = ["gdrive", "mutate", "upload", pdf, "--parent", folder_id]
    res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    print(res.stdout)
    if res.stderr:
        print("ERR:", res.stderr)

import shutil
zip_file_local = r"C:\Users\HP\Projects\APlikasi MBG\arahan_senin\senin_09-11.zip"
shutil.copy(r"C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\.user_uploaded\media_1794100631876_b7599e36.zip", zip_file_local)
print("Uploading zip archive...")
cmd = ["gdrive", "mutate", "upload", zip_file_local, "--parent", folder_id]
res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
print(res.stdout)
if res.stderr:
    print("ERR:", res.stderr)
print("Done!")

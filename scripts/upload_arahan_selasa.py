# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

local_dir = r"C:\Users\HP\Projects\APlikasi MBG\arahan_selasa"
os.makedirs(local_dir, exist_ok=True)

uploaded_files = {
    r"C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\.user_uploaded\media_1794166080528_af62e38e.pdf": "Arahan_Selasa_SMK_1_Kedungwuni.pdf",
    r"C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\.user_uploaded\media_1794166080530_20588b76.pdf": "Arahan_Selasa_MTs_Salafiyah_Syafiiyah.pdf",
    r"C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\.user_uploaded\media_1794166080530_a77a1011.pdf": "Arahan_Selasa_Posyandu_Ambokembang.pdf",
    r"C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\.user_uploaded\media_1794166080526_e982c146.pdf": "Arahan_Selasa_Posyandu_Panjomblangan.pdf"
}

folder_id = "1unodAt2RR0z8zoSBmzUMUjlQ_OZues06"

for src, name in uploaded_files.items():
    dst = os.path.join(local_dir, name)
    shutil.copyfile(src, dst)
    print(f"Copied {name} locally.")
    
    cmd = ["gdrive", "mutate", "upload", dst, "--parent", folder_id]
    res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    print(f"Uploaded {name}: {res.stdout.strip()}")
    if res.stderr:
        print(f"Err {name}: {res.stderr.strip()}")

print("All Tuesday PDFs copied and uploaded successfully!")


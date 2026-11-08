import pypdf
import glob
import os

pdf_files = sorted(glob.glob(r'C:\Users\HP\Projects\APlikasi MBG\arahan_senin\*.pdf'))
for pf in pdf_files:
    print('='*50)
    print('FILE:', os.path.basename(pf))
    reader = pypdf.PdfReader(pf)
    for i, page in enumerate(reader.pages):
        print(f'--- PAGE {i+1} ---')
        print(page.extract_text())


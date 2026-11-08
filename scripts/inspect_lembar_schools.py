import pypdf
import glob
import os

pdf_files = sorted(glob.glob(r'C:\Users\HP\Projects\APlikasi MBG\arahan_senin\Lembar_*.pdf'))
for pf in pdf_files:
    fname = os.path.basename(pf)
    print('='*70)
    print('FILE:', fname)
    reader = pypdf.PdfReader(pf)
    for i, p in enumerate(reader.pages):
        print(f'--- PAGE {i+1} ---')
        print(p.extract_text())


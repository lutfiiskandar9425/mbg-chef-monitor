import pypdf
import glob
import os

pdf_files = sorted(glob.glob(r'C:\Users\HP\Projects\APlikasi MBG\arahan_senin\*.pdf'))
for pf in pdf_files:
    fname = os.path.basename(pf)
    print('='*60)
    print('FILE:', fname)
    reader = pypdf.PdfReader(pf)
    full_text = '\n'.join([f'--- Page {idx+1} ---\n' + page.extract_text() for idx, page in enumerate(reader.pages)])
    print(full_text)


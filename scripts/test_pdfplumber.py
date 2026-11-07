import pdfplumber

with pdfplumber.open('SOP_Menu_Mingguan_SPPG_Pekajangan04.pdf') as pdf:
    print('Total pages:', len(pdf.pages))
    for i, p in enumerate(pdf.pages):
        text = p.extract_text()
        print(f'Page {i+1} characters:', len(text))
        print(f'Page {i+1} preview:', text.split('\n')[0:3])


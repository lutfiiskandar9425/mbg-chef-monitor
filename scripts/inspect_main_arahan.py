import pypdf

reader = pypdf.PdfReader(r'C:\Users\HP\Projects\APlikasi MBG\arahan_senin\00_Arahan_Tim_Persiapan_Senin_9Nov2026.pdf')
for i, page in enumerate(reader.pages):
    print(f'=== MAIN ARAHAN PAGE {i+1} ===')
    print(page.extract_text())


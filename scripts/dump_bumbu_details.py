import pypdf

reader = pypdf.PdfReader(r'C:\Users\HP\Projects\APlikasi MBG\arahan_senin\00_Arahan_Tim_Persiapan_Senin_9Nov2026.pdf')
for i, p in enumerate(reader.pages):
    print(f'=== PAGE {i+1} ===')
    print(p.extract_text())


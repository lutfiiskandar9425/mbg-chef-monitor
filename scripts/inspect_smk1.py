import pypdf

reader = pypdf.PdfReader(r'C:\Users\HP\Projects\APlikasi MBG\arahan_senin\Lembar_Tim_Persiapan_SMK_1_Kedungwuni_Senin_9Nov2026.pdf')
for i, page in enumerate(reader.pages):
    print(f'=== SMK 1 KEDUNGWUNI PAGE {i+1} ===')
    print(page.extract_text())


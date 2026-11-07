"""
Script lengkap untuk membuat 5 sheet harian (Senin - Jumat), Master Template,
Menu_Mingguan, Log_Timbangan, dan Stok_Gudang dengan formula resmi BGN.
"""
import openpyxl
from copy import copy

def build_complete_workbook():
    wb = openpyxl.load_workbook('live_monitoring.xlsx')
    
    # Ambil sheet template asli
    orig_template = wb['Monitoring Alur Bahan Baku']
    
    days_config = [
        {
            "name": "Senin",
            "date_str": "Senin, 09 November 2026",
            "menu_str": "Nasi Putih + Daging Ayam Semur Kecap + Tahu Goreng Gurih + Tumis Buncis Jagung Manis + Pisang Cavendish",
            "items": [
                ("Protein Hewani", "Daging Ayam Fillet", "kg"),
                ("Protein Nabati", "Tahu Putih Segar", "kg"),
                ("Sayuran", "Buncis & Jagung Manis", "kg"),
                ("Buah", "Pisang Cavendish", "pcs"),
                ("Karbohidrat", "Beras Putih Premium", "kg"),
                ("Bumbu", "Bumbu Rempah Semur", "kg"),
                ("Bumbu", "Minyak Goreng Sawit", "kg")
            ]
        },
        {
            "name": "Selasa",
            "date_str": "Selasa, 10 November 2026",
            "menu_str": "Nasi Putih + Daging Sapi Teriyaki Lada Hitam + Tempe Goreng Tepung + Capcay Sayur Segar + Jeruk Manis",
            "items": [
                ("Protein Hewani", "Daging Sapi Slice", "kg"),
                ("Protein Nabati", "Tempe Kedelai Murni", "kg"),
                ("Sayuran", "Capcay Sayur Segar", "kg"),
                ("Buah", "Jeruk Manis Medan", "pcs"),
                ("Karbohidrat", "Beras Putih Premium", "kg"),
                ("Bumbu", "Saus Teriyaki & Lada Hitam", "kg"),
                ("Bumbu", "Minyak Goreng Sawit", "kg")
            ]
        },
        {
            "name": "Rabu",
            "date_str": "Rabu, 11 November 2026",
            "menu_str": "Nasi Putih + Ikan Kembung Asam Manis + Tempe Mendoan + Sayur Bayam Jagung Bening + Semangka Merah",
            "items": [
                ("Protein Hewani", "Ikan Kembung Fillet", "kg"),
                ("Protein Nabati", "Tempe Mendoan", "kg"),
                ("Sayuran", "Sayur Bayam & Jagung Manis", "kg"),
                ("Buah", "Semangka Merah Segar", "kg"),
                ("Karbohidrat", "Beras Putih Premium", "kg"),
                ("Bumbu", "Bumbu Asam Manis Nanas", "kg"),
                ("Bumbu", "Minyak Goreng Sawit", "kg")
            ]
        },
        {
            "name": "Kamis",
            "date_str": "Kamis, 12 November 2026",
            "menu_str": "Nasi Putih + Ayam Panggang Bumbu Madu + Rolade Tahu Telur + Sayur Labu Siam Wortel Gurih + Melon Cantaloupe",
            "items": [
                ("Protein Hewani", "Ayam Panggang Madu", "kg"),
                ("Protein Nabati", "Rolade Tahu Telur", "kg"),
                ("Sayuran", "Labu Siam & Wortel", "kg"),
                ("Buah", "Melon Cantaloupe", "kg"),
                ("Karbohidrat", "Beras Putih Premium", "kg"),
                ("Bumbu", "Madu & Bumbu Oles", "kg"),
                ("Bumbu", "Minyak Goreng Sawit", "kg")
            ]
        },
        {
            "name": "Jumat",
            "date_str": "Jumat, 13 November 2026",
            "menu_str": "Nasi Putih + Telur Balado Pedas Manis + Perkedel Kentang Daging + Sayur Lodeh Labu + Pepaya California",
            "items": [
                ("Protein Hewani", "Telur Ayam Balado", "butir"),
                ("Protein Nabati", "Perkedel Kentang Daging", "kg"),
                ("Sayuran", "Sayur Lodeh Labu Siam", "kg"),
                ("Buah", "Pepaya California", "kg"),
                ("Karbohidrat", "Beras Putih Premium", "kg"),
                ("Bumbu", "Bumbu Sambal Balado Manis", "kg"),
                ("Bumbu", "Minyak Goreng Sawit", "kg")
            ]
        }
    ]

    # Buat 5 sheet hari dengan copy template
    for cfg in days_config:
        day_name = cfg["name"]
        if day_name in wb.sheetnames:
            ws = wb[day_name]
        else:
            ws = wb.copy_worksheet(orig_template)
            ws.title = day_name
            
        # Isi Header
        ws['D9'] = cfg["date_str"]
        ws['D10'] = cfg["menu_str"]
        ws['K12'] = 1200 # PM Porsi Kecil
        ws['K13'] = 1800 # PM Porsi Besar
        ws['K14'] = '=K12+K13' # TOTAL PM 3000
        ws['D14'] = 'Petugas QC / ASLAP Pekajangan 4'

        # Isi Item Bahan Baku (Baris 17 s/d 23)
        for idx, (kat, item_name, satuan) in enumerate(cfg["items"]):
            r = 17 + idx
            ws[f'A{r}'] = idx + 1
            ws[f'B{r}'] = kat
            ws[f'C{r}'] = item_name
            ws[f'D{r}'] = satuan
            
            # Formula alur timbangan
            ws[f'G{r}'] = f'=IFERROR(E{r}-F{r},"")'
            ws[f'H{r}'] = f'=IFERROR(G{r}/E{r},"")'
            ws[f'J{r}'] = f'=IFERROR(F{r}-I{r},"")'
            ws[f'K{r}'] = f'=IFERROR(J{r}/F{r},"")'
            ws[f'M{r}'] = f'=IFERROR(I{r}-L{r},"")'

        # Formula Ringkasan
        ws['E26'] = '=SUM(E17:E23)'
        ws['E27'] = '=SUM(G17:G23)'
        ws['E28'] = '=SUM(J17:J23)'
        ws['E29'] = '=SUM(M17:M23)'
        ws['E30'] = '=E29-K14'

        # Tanda Tangan
        ws['K38'] = '( ASLAP / Chef Lutfi )'

        print(f"Sheet '{day_name}' berhasil disiapkan: {cfg['date_str']}")

    # Bersihkan sheet duplikat lama
    for old_name in ['Monitoring Alur Bahan Baku (2)', 'Monitoring Alur Bahan Baku (3)']:
        if old_name in wb.sheetnames:
            del wb[old_name]
            print(f"Sheet lama '{old_name}' dibersihkan.")

    # Pastikan template asli dinamai Master Template jika perlu
    if 'Monitoring Alur Bahan Baku' in wb.sheetnames:
        orig_template.title = 'Master Template'
        print("Template utama dinamai 'Master Template'.")

    # Tambahkan sheet Menu_Mingguan jika belum ada
    if 'Menu_Mingguan' not in wb.sheetnames:
        menu_ws = wb.create_sheet(title='Menu_Mingguan')
        menu_ws.append([
            "Hari", "Nama Menu Lengkap", "Kategori Komponen", "Nama Bahan Baku",
            "Standar Porsi", "Target Porsi", "Arahan Persiapan", "Arahan Pengolahan",
            "Arahan Pemorsian", "Catatan Gizi"
        ])
        for cfg in days_config:
            for kat, it, sat in cfg["items"]:
                menu_ws.append([
                    cfg["name"], cfg["menu_str"], kat, it,
                    "Standar BGN", "3.000 Porsi",
                    "Kupas bersih, potong seragam, bilas 3x",
                    "Suhu inti minimal 75°C, bumbu matang tanak",
                    "Suhu saji 60°C, sekat ompreng higienis",
                    "Lolos verifikasi gizi SPPG"
                ])
        print("Sheet 'Menu_Mingguan' berhasil dibuat.")

    # Tambahkan sheet Log_Timbangan jika belum ada
    if 'Log_Timbangan' not in wb.sheetnames:
        log_ws = wb.create_sheet(title='Log_Timbangan')
        log_ws.append([
            "Waktu Server", "Hari", "Tanggal Log", "Waktu", "Tim Kerja / Stasiun",
            "Kategori", "Item Bahan Baku", "Tahapan Alur", "Netto (kg)", "Bruto (kg)",
            "Tara (kg)", "Catatan", "Petugas / Chef"
        ])
        print("Sheet 'Log_Timbangan' berhasil dibuat.")

    # Tambahkan sheet Stok_Gudang jika belum ada
    if 'Stok_Gudang' not in wb.sheetnames:
        stok_ws = wb.create_sheet(title='Stok_Gudang')
        stok_ws.append([
            "Nama Bahan Baku", "Kategori", "Total Masuk (kg)", "Total Keluar (kg)",
            "Stok Sisa (kg)", "Satuan", "Status Stok"
        ])
        stok_items = [
            ("Daging Ayam Fillet", "Protein Hewani", 210.0, 164.8, 45.2, "kg", "Aman"),
            ("Daging Sapi Slice", "Protein Hewani", 180.0, 140.0, 40.0, "kg", "Aman"),
            ("Tahu Putih Segar", "Protein Nabati", 150.0, 120.0, 30.0, "kg", "Aman"),
            ("Tempe Kedelai Murni", "Protein Nabati", 135.0, 100.0, 35.0, "kg", "Aman"),
            ("Wortel Brastagi Segar", "Sayuran", 120.0, 101.5, 18.5, "kg", "Sedang"),
            ("Buncis & Jagung Manis", "Sayuran", 180.0, 150.0, 30.0, "kg", "Aman"),
            ("Pisang Cavendish", "Buah", 3000, 2400, 600, "pcs", "Siap Saji"),
            ("Beras Putih Premium", "Karbohidrat", 500.0, 300.0, 200.0, "kg", "Aman")
        ]
        for it in stok_items:
            stok_ws.append(list(it))
        print("Sheet 'Stok_Gudang' berhasil dibuat.")

    # Atur urutan sheet: Senin, Selasa, Rabu, Kamis, Jumat, Master Template, Menu_Mingguan, Log_Timbangan, Stok_Gudang
    order = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Master Template', 'Menu_Mingguan', 'Log_Timbangan', 'Stok_Gudang']
    sheet_objs = [wb[s] for s in order if s in wb.sheetnames]
    wb._sheets = sheet_objs

    out_file = 'live_monitoring_updated.xlsx'
    wb.save(out_file)
    wb.save('live_monitoring.xlsx')
    print(f"\nSemua sheet berhasil disimpan ke '{out_file}' dan 'live_monitoring.xlsx'!")
    print(f"Urutan sheet sekarang: {wb.sheetnames}")

if __name__ == '__main__':
    build_complete_workbook()


import openpyxl

wb = openpyxl.load_workbook('live_monitoring.xlsx')
if 'Menu_Mingguan' in wb.sheetnames:
    ws = wb['Menu_Mingguan']
    # Clear old rows
    for r in range(2, 50):
        for c in range(1, 7):
            ws.cell(r, c).value = None

    menu_data = [
        # SENIN
        ("09-13 Nov 2026", "SENIN", "KARBO", "Nasi Putih", "100 g matang per porsi (1 kg beras = 19 porsi)", "2.742 Porsi"),
        ("09-13 Nov 2026", "SENIN", "PROHE", "Ayam Rica (PB) / Ayam Kecap (PK)", "5 dadu seragam +-2x2 cm (60 g matang). PB Rica, PK Kecap", "2.742 Porsi"),
        ("09-13 Nov 2026", "SENIN", "PRONA", "Tahu Goreng", "1 potong 30 g matang, ditekan/dikeringkan sebelum digoreng", "2.742 Porsi"),
        ("09-13 Nov 2026", "SENIN", "SAYUR", "Tumis Putren Wortel", "30 g matang, irisan seragam, empuk renyah tidak berair", "2.742 Porsi"),
        ("09-13 Nov 2026", "SENIN", "BUAH", "Jeruk Medan", "1 buah per porsi (isi 10-12/kg, cadangan +3%)", "2.742 Pcs"),

        # SELASA
        ("09-13 Nov 2026", "SELASA", "KARBO", "Nasi Putih", "100 g matang pulen standar BGN", "2.742 Porsi"),
        ("09-13 Nov 2026", "SELASA", "PROHE", "Ayam Katsu Sambal Geprek", "Ayam fillet dada balur tepung panir krispi + sambal geprek", "2.742 Porsi"),
        ("09-13 Nov 2026", "SELASA", "PRONA", "Tahu Goreng", "1 potong 30 g tahu goreng gurih berkulit", "2.742 Porsi"),
        ("09-13 Nov 2026", "SELASA", "SAYUR", "Mix Vegetable (Jagung, Polong, Wortel)", "30 g tumis sayur mentega cerah gurih", "2.742 Porsi"),
        ("09-13 Nov 2026", "SELASA", "BUAH", "Pisang Segar", "1 buah pisang standar BGN", "2.742 Pcs"),

        # RABU
        ("09-13 Nov 2026", "RABU", "KARBO", "Nasi Putih", "100 g matang pulen", "2.742 Porsi"),
        ("09-13 Nov 2026", "RABU", "PROHE", "Telur Fuyunghai + Saus", "Fuyunghai telur tebal gurih + siraman saus asam manis", "2.742 Porsi"),
        ("09-13 Nov 2026", "RABU", "PRONA", "Tempe Goreng", "Tempe kedelai murni goreng gurih", "2.742 Porsi"),
        ("09-13 Nov 2026", "RABU", "SAYUR", "Tumis Polong Wortel Kol", "30 g tumis sayuran segar renyah", "2.742 Porsi"),
        ("09-13 Nov 2026", "RABU", "BUAH", "Anggur Muscat", "Anggur muscat manis segar", "2.742 Porsi"),

        # KAMIS
        ("09-13 Nov 2026", "KAMIS", "KARBO", "Nasi Putih", "100 g matang pulen", "2.742 Porsi"),
        ("09-13 Nov 2026", "KAMIS", "PROHE", "Ikan Lele Crispy + Sambal Bawang", "Lele goreng krispi renyah matang sempurna", "2.742 Porsi"),
        ("09-13 Nov 2026", "KAMIS", "PRONA", "Edamame Rebus", "Edamame rebus garam ringan", "2.742 Porsi"),
        ("09-13 Nov 2026", "KAMIS", "SAYUR", "Kakiage (Bakwan Sayur)", "Bakwan sayur jepang wortel kol krispi", "2.742 Porsi"),
        ("09-13 Nov 2026", "KAMIS", "BUAH", "Kelengkeng Manis", "Kelengkeng manis segar", "2.742 Pcs"),

        # JUMAT
        ("09-13 Nov 2026", "JUMAT", "KARBO", "Nasi Putih", "100 g matang pulen", "2.094 Porsi"),
        ("09-13 Nov 2026", "JUMAT", "PROHE", "Ayam Crispy Sambal Bajak", "Ayam goreng tepung krispi + sambal bajak tanak gurih", "2.094 Porsi"),
        ("09-13 Nov 2026", "JUMAT", "PRONA", "Tempe Goreng", "Tempe kedelai goreng gurih", "2.094 Porsi"),
        ("09-13 Nov 2026", "JUMAT", "SAYUR", "Mix Vegetable", "30 g tumis jagung wortel polong", "2.094 Porsi"),
        ("09-13 Nov 2026", "JUMAT", "BUAH", "Anggur Red Globe", "Anggur merah segar", "2.094 Porsi"),
    ]

    for idx, row in enumerate(menu_data, start=2):
        for col_idx, val in enumerate(row, start=1):
            ws.cell(idx, col_idx).value = val

    wb.save('live_monitoring.xlsx')
    print('Updated Menu_Mingguan sheet!')


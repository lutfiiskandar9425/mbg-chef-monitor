"""
Update live_monitoring.xlsx dengan Rencana Menu Resmi Mas Lutfi 16-27 November 2026.
Memperbarui sheet Senin, Selasa, Rabu, Kamis, Jumat, dan Menu_Mingguan.
"""
import openpyxl

wb = openpyxl.load_workbook('live_monitoring.xlsx')

# Data Menu Minggu 1 (16-20 Nov 2026)
menu_w1 = {
    "Senin": {
        "date_str": "Senin, 16 November 2026",
        "menu_str": "Nasi Gurih + Telur Rollade Bulat + Sambal Bawang + Edamame + Kakiage + Jeruk",
        "items": [
            ("Protein Hewani", "Telur Ayam Rollade Bulat", "butir / kg"),
            ("Karbohidrat", "Beras Putih (Nasi Gurih)", "kg"),
            ("Protein Nabati", "Edamame Segar Rebus", "kg"),
            ("Sayuran", "Sayur Kakiage (Wortel, Bawang, Kol)", "kg"),
            ("Buah", "Jeruk Manis Segar", "pcs"),
            ("Bumbu", "Bumbu Sambal Bawang", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    },
    "Selasa": {
        "date_str": "Selasa, 17 November 2026",
        "menu_str": "Nasi Putih + Chicken Drum Stick + Saus BBQ + Stik Tempe Tepung + Mix Vigie + Semangka",
        "items": [
            ("Protein Hewani", "Chicken Drum Stick (Ayam)", "kg"),
            ("Karbohidrat", "Beras Putih Premium", "kg"),
            ("Protein Nabati", "Stik Tempe Tepung Krispi", "kg"),
            ("Sayuran", "Mix Vigie (Jagung, Polong, Wortel)", "kg"),
            ("Buah", "Semangka Merah Potong", "kg"),
            ("Bumbu", "Saus BBQ Racikan Dapur", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    },
    "Rabu": {
        "date_str": "Rabu, 18 November 2026",
        "menu_str": "Nasi Putih + Bola Bakso Daging Isi 3 + Saus Bangkok + Tahu Goreng + Kol Wortel + Pisang",
        "items": [
            ("Protein Hewani", "Bola Bakso Daging Sapi (Isi 3)", "butir / kg"),
            ("Karbohidrat", "Beras Putih Premium", "kg"),
            ("Protein Nabati", "Tahu Putih Goreng Gurih", "kg"),
            ("Sayuran", "Tumis Sayur Kol & Wortel", "kg"),
            ("Buah", "Pisang Cavendish", "pcs"),
            ("Bumbu", "Saus Bangkok Manis Pedas", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    },
    "Kamis": {
        "date_str": "Kamis, 19 November 2026",
        "menu_str": "Roti Tawar (2 Tangkup) + Telor Ceplok + Saus Mayo Pedas + Stik Tempe + Timun Selada + Pisang",
        "items": [
            ("Protein Hewani", "Telur Ayam Negeri (Ceplok)", "butir"),
            ("Karbohidrat", "Roti Tawar Lembaran (2 pcs)", "pcs"),
            ("Protein Nabati", "Stik Tempe Tepung", "kg"),
            ("Sayuran", "Lalapan Timun & Selada Segar", "kg"),
            ("Buah", "Pisang Cavendish", "pcs"),
            ("Bumbu", "Saus Mayo Pedas Gurih", "kg"),
            ("Bumbu", "Margarin / Minyak Goreng", "kg")
        ]
    },
    "Jumat": {
        "date_str": "Jumat, 20 November 2026",
        "menu_str": "Nasi Gurih + Telur Katsu Krispi + Sambal Bawang + Tahu Goreng + Tumis Labu Jagung + Melon",
        "items": [
            ("Protein Hewani", "Telur Katsu Krispi Tepung Panir", "butir / kg"),
            ("Karbohidrat", "Beras Putih (Nasi Gurih)", "kg"),
            ("Protein Nabati", "Tahu Putih Goreng", "kg"),
            ("Sayuran", "Tumis Labu Siam & Jagung Manis", "kg"),
            ("Buah", "Melon Cantaloupe Segar", "kg"),
            ("Bumbu", "Sambal Bawang Gurih", "kg"),
            ("Bumbu", "Minyak Goreng Sawit", "kg")
        ]
    }
}

# Update 5 sheets harian
for day_name, cfg in menu_w1.items():
    if day_name in wb.sheetnames:
        ws = wb[day_name]
        ws['D9'] = cfg["date_str"]
        ws['D10'] = cfg["menu_str"]
        ws['K12'] = 1200
        ws['K13'] = 1800
        ws['K14'] = '=K12+K13'
        ws['D14'] = 'Petugas QC / ASLAP Kedungwuni 4'
        ws['K38'] = '( ASLAP / Chef Lutfi )'

        for idx, (kat, it, sat) in enumerate(cfg["items"]):
            r = 17 + idx
            ws[f'A{r}'] = idx + 1
            ws[f'B{r}'] = kat
            ws[f'C{r}'] = it
            ws[f'D{r}'] = sat
            ws[f'G{r}'] = f'=IFERROR(E{r}-F{r},"")'
            ws[f'H{r}'] = f'=IFERROR(G{r}/E{r},"")'
            ws[f'J{r}'] = f'=IFERROR(F{r}-I{r},"")'
            ws[f'K{r}'] = f'=IFERROR(J{r}/F{r},"")'
            ws[f'M{r}'] = f'=IFERROR(I{r}-L{r},"")'

        ws['E26'] = '=SUM(E17:E23)'
        ws['E27'] = '=SUM(G17:G23)'
        ws['E28'] = '=SUM(J17:J23)'
        ws['E29'] = '=SUM(M17:M23)'
        ws['E30'] = '=E29-K14'
        print(f"Updated Sheet '{day_name}': {cfg['menu_str'][:50]}...")

# Update Menu_Mingguan dengan 2 Siklus Lengkap (16-20 Nov & 23-27 Nov)
if 'Menu_Mingguan' in wb.sheetnames:
    del wb['Menu_Mingguan']

menu_ws = wb.create_sheet(title='Menu_Mingguan')
menu_ws.append([
    "Periode", "Hari", "Komponen", "Nama Olahan / Bahan",
    "Detail Resep", "Target Porsi", "Arahan Stasiun Tim Kerja"
])

# Siklus 1
siklus_1 = [
    ("16-20 Nov 2026", "SENIN", "KARBO", "Nasi Gurih", "Nasi gurih harum pandan & santan encer", "3.000 Porsi", "Tim Pengolahan: aron & kukus"),
    ("16-20 Nov 2026", "SENIN", "PROHE", "Telur Rollade (Bulat)", "Rollade telur dadar gulung potong bulat rapi", "3.000 Porsi", "Tim Pengolahan: goreng keemasan"),
    ("16-20 Nov 2026", "SENIN", "SIDE", "Sambal Bawang", "Cabai & bawang ditumis wangi gurih", "3.000 Porsi", "Tim Pengolahan: bumbu tanak"),
    ("16-20 Nov 2026", "SENIN", "PRONA", "Edamame", "Edamame segar rebus garam ringan", "3.000 Porsi", "Tim Persiapan: cuci bersih"),
    ("16-20 Nov 2026", "SENIN", "SAYUR", "Kakiage", "Bakwan sayur jepang (wortel, bawang, kol krispi)", "3.000 Porsi", "Tim Persiapan: potong korek api"),
    ("16-20 Nov 2026", "SENIN", "BUAH", "Jeruk", "Jeruk manis segar", "3.000 Pcs", "Tim Pemorsian: lap steril sejuk"),

    ("16-20 Nov 2026", "SELASA", "KARBO", "Nasi", "Nasi putih pulen standar BGN", "3.000 Porsi", "Tim Pengolahan: takar air presisi"),
    ("16-20 Nov 2026", "SELASA", "PROHE", "Chicken Drum Stick", "Paha ayam bawah balur bumbu krispi", "3.000 Porsi", "Tim Pengolahan: suhu inti 75°C"),
    ("16-20 Nov 2026", "SELASA", "SIDE", "Saus BBQ", "Saus gurih asam manis lada", "3.000 Porsi", "Tim Pengolahan: saus hangat"),
    ("16-20 Nov 2026", "SELASA", "PRONA", "Stik Tempe (Tempe Tepung)", "Tempe potong memanjang balur tepung renyah", "3.000 Porsi", "Tim Persiapan: potong stik 6x1 cm"),
    ("16-20 Nov 2026", "SELASA", "SAYUR", "Mix Vigie", "Jagung manis pipil, wortel dadu, polong", "3.000 Porsi", "Tim Pengolahan: tumis butter cepat"),
    ("16-20 Nov 2026", "SELASA", "BUAH", "Semangka", "Semangka merah potong juring tebal 2 cm", "3.000 Porsi", "Tim Pemorsian: talenan kuning steril"),

    ("16-20 Nov 2026", "RABU", "KARBO", "Nasi", "Nasi putih pulen", "3.000 Porsi", "Tim Pengolahan"),
    ("16-20 Nov 2026", "RABU", "PROHE", "Bola Bakso Daging Isi 3", "3 butir bakso daging sapi kenyal gurih", "3.000 Porsi", "Tim Pengolahan: kuah kaldu 75°C"),
    ("16-20 Nov 2026", "RABU", "SIDE", "Saus Bangkok", "Saus asam manis pedas ala bangkok", "3.000 Porsi", "Tim Pengolahan"),
    ("16-20 Nov 2026", "RABU", "PRONA", "Tahu Goreng", "Tahu putih goreng gurih berkulit", "3.000 Porsi", "Tim Pengolahan: minyak 160°C"),
    ("16-20 Nov 2026", "RABU", "SAYUR", "Kol Wortel", "Tumis kol dan wortel koin iris tipis", "3.000 Porsi", "Tim Persiapan: bilas 3x"),
    ("16-20 Nov 2026", "RABU", "BUAH", "Pisang", "Pisang cavendish matang standar BGN", "3.000 Pcs", "Tim Pemorsian: sekat buah kering"),

    ("16-20 Nov 2026", "KAMIS", "KARBO", "Roti 2", "2 lembar roti tawar sandwich empuk", "3.000 Porsi", "Tim Pemorsian: susun rapi"),
    ("16-20 Nov 2026", "KAMIS", "PROHE", "Telor Ceplok", "Telur mata sapi matang sempurna", "3.000 Butir", "Tim Pengolahan: kuning matang"),
    ("16-20 Nov 2026", "KAMIS", "SIDE", "Mayo Pedas", "Saus mayones pedas lembut", "3.000 Porsi", "Tim Pemorsian: olesan roti"),
    ("16-20 Nov 2026", "KAMIS", "PRONA", "Stik Tempe (Tempe Tepung)", "Tempe stik krispi", "3.000 Porsi", "Tim Pengolahan"),
    ("16-20 Nov 2026", "KAMIS", "SAYUR", "Timun Selada", "Irisan timun segar & selada hijau higienis", "3.000 Porsi", "Tim Persiapan: cuci air es steril"),
    ("16-20 Nov 2026", "KAMIS", "BUAH", "Pisang", "Pisang cavendish", "3.000 Pcs", "Tim Pemorsian"),

    ("16-20 Nov 2026", "JUMAT", "KARBO", "Nasi Gurih", "Nasi gurih harum kelapa pandan", "3.000 Porsi", "Tim Pengolahan"),
    ("16-20 Nov 2026", "JUMAT", "PROHE", "Telur Katsu", "Telur balur tepung katsu krispi emas", "3.000 Porsi", "Tim Pengolahan: tiris minyak"),
    ("16-20 Nov 2026", "JUMAT", "SIDE", "Sambal Bawang", "Sambal bawang pedas gurih", "3.000 Porsi", "Tim Pengolahan"),
    ("16-20 Nov 2026", "JUMAT", "PRONA", "Tahu Goreng", "Tahu goreng gurih", "3.000 Porsi", "Tim Pengolahan"),
    ("16-20 Nov 2026", "JUMAT", "SAYUR", "Tumis Labu Jagung", "Labu siam serut & jagung manis pipil", "3.000 Porsi", "Tim Persiapan: buang getah labu"),
    ("16-20 Nov 2026", "JUMAT", "BUAH", "Melon", "Melon segar potong dingin", "3.000 Porsi", "Tim Pemorsian")
]

# Siklus 2
siklus_2 = [
    ("23-27 Nov 2026", "SENIN", "KARBO", "Nasi Gurih", "Nasi gurih lezat", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "SENIN", "PROHE", "Lele Crispy", "Ikan lele fillet crispy tanpa duri", "3.000 Porsi", "Tim Pengolahan: goreng garing"),
    ("23-27 Nov 2026", "SENIN", "SIDE", "Sambal Bajak", "Sambal bajak matang gurih terasi", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "SENIN", "PRONA", "Tempe Orek Kacang Panjang", "Orek tempe manis gurih kacang panjang", "3.000 Porsi", "Tim Persiapan & Pengolahan"),
    ("23-27 Nov 2026", "SENIN", "SAYUR", "Lalap Timun + Labu", "Lalapan timun dan labu siam kukus", "3.000 Porsi", "Tim Persiapan"),
    ("23-27 Nov 2026", "SENIN", "BUAH", "Jeruk", "Jeruk manis", "3.000 Pcs", "Tim Pemorsian"),

    ("23-27 Nov 2026", "SELASA", "KARBO", "Nasi", "Nasi putih", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "SELASA", "PROHE", "Telor Ceplok", "Telor ceplok mata sapi", "3.000 Butir", "Tim Pengolahan"),
    ("23-27 Nov 2026", "SELASA", "SIDE", "Sambal Kecap", "Sambal kecap cabai rawit bawang", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "SELASA", "PRONA", "Edamame", "Edamame rebus", "3.000 Porsi", "Tim Persiapan"),
    ("23-27 Nov 2026", "SELASA", "SAYUR", "Kakiage", "Bakwan sayur jepang krispi", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "SELASA", "BUAH", "Pisang", "Pisang cavendish", "3.000 Pcs", "Tim Pemorsian"),

    ("23-27 Nov 2026", "RABU", "KARBO", "Nasi", "Nasi putih", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "RABU", "PROHE", "Ayam Bumbu Hitam", "Ayam ungkep bumbu hitam madura kaya rempah", "3.000 Porsi", "Tim Pengolahan: suhu inti 75°C"),
    ("23-27 Nov 2026", "RABU", "SIDE", "Sambal Bawang", "Sambal bawang", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "RABU", "PRONA", "Tahu Goreng", "Tahu goreng gurih", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "RABU", "SAYUR", "Lalap Timun Selada", "Timun & selada segar", "3.000 Porsi", "Tim Persiapan"),
    ("23-27 Nov 2026", "RABU", "BUAH", "Kelengkeng", "Kelengkeng manis segar", "3.000 Porsi", "Tim Pemorsian"),

    ("23-27 Nov 2026", "KAMIS", "KARBO", "Nasi", "Nasi putih", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "KAMIS", "PROHE", "Telur Fuyunghai", "Dadar telur tebal sayur & ayam cincang", "3.000 Porsi", "Tim Pengolahan: dadar tebal"),
    ("23-27 Nov 2026", "KAMIS", "SIDE", "Saus Fuyunghai", "Saus asam manis kacang polong wortel", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "KAMIS", "PRONA", "Tempe Goreng", "Tempe goreng ketumbar", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "KAMIS", "SAYUR", "Polong + Wortel", "Kacang polong & wortel rebus saus", "3.000 Porsi", "Tim Persiapan"),
    ("23-27 Nov 2026", "KAMIS", "BUAH", "Buah Naga", "Buah naga merah potong dadu", "3.000 Porsi", "Tim Pemorsian"),

    ("23-27 Nov 2026", "JUMAT", "KARBO", "Nasi Gurih", "Nasi gurih", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "JUMAT", "PROHE", "Semur Telur Dadar", "Telur dadar gulung semur kuah kecap gurih", "3.000 Porsi", "Tim Pengolahan: kuah meresap"),
    ("23-27 Nov 2026", "JUMAT", "SIDE", "Sambal Bawang", "Sambal bawang", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "JUMAT", "PRONA", "Tahu Goreng", "Tahu goreng gurih", "3.000 Porsi", "Tim Pengolahan"),
    ("23-27 Nov 2026", "JUMAT", "SAYUR", "Gyoza Sayur Wortel Kol", "Gyoza isi sayur wortel kol kukus/pan fry", "3.000 Porsi", "Tim Persiapan: lipat gyoza"),
    ("23-27 Nov 2026", "JUMAT", "BUAH", "Pisang", "Pisang cavendish", "3.000 Pcs", "Tim Pemorsian")
]

for row in siklus_1 + siklus_2:
    menu_ws.append(list(row))

# Simpan
wb.save('live_monitoring.xlsx')
print("live_monitoring.xlsx berhasil diperbarui dengan Menu Resmi 16-27 November 2026!")


"""
Memperbarui live_monitoring.xlsx dengan Menu Resmi 09-13 November 2026 SPPG Pekajangan 04
sesuai dokumen bertandatangan Ahli Gizi (Maudyfara YPD) dan Kepala SPPG (Danang Nurhidayatullah).
"""
import openpyxl

wb = openpyxl.load_workbook('live_monitoring.xlsx')

menu_data = {
    "Senin": {
        "date_str": "Senin, 9 November 2026",
        "menu_str": "Nasi + Ayam Rica-Rica + Ayam Kecap + Tumis Putren Wortel + Tahu Goreng + Jeruk",
        "porsi_besar": 2550,
        "porsi_kecil": 192,
        "items": [
            ("Buah", "Jeruk Medan (isi 10-12)", 242, "kg", "2783 butir jeruk isi 11/kg"),
            ("Protein Nabati", "Tahu Putih Besar", 2772, "pcs", "Tahu pcs-an buffer 30 pcs"),
            ("Protein Hewani", "Ayam Dada Fillet", 174, "kg", "Ayam fillet rica-rica & kecap"),
            ("Karbohidrat", "Beras Putih", 150, "kg", "Nasi putih standar pulen"),
            ("Sayuran", "Wortel Segar", 48, "kg", "Sayur tumis putren wortel"),
            ("Sayuran", "Putren (Jagung Muda)", 48, "kg", "Sayur tumis putren wortel"),
            ("Bahan Kering", "Tepung Jagung Maizenaku", 30, "kg", "Pengental saus"),
            ("Minyak", "Minyak Goreng Sawit", 120, "liter", "Minyak goreng botol 1L"),
            ("Saus & Bumbu", "Saus Tiram Saori 1L", 7, "botol", "Bumbu ayam rica & kecap"),
            ("Bumbu Basah", "Bawang Putih", 2, "kg", "Bumbu dapur"),
            ("Bumbu Basah", "Bawang Bombai", 2, "kg", "Bumbu ayam rica"),
            ("Bumbu Basah", "Tomat Sayur", 1, "kg", "Bumbu segar"),
            ("Bumbu Basah", "Daun Jeruk", 0.1, "kg", "Aromatik"),
            ("Bahan Kering", "Gula Pasir", 3, "kg", "Bumbu kering"),
            ("Bahan Kering", "Gula Merah", 2, "kg", "Bumbu kecap"),
            ("Bahan Kering", "Chicken Powder Knorr", 3, "kg", "Penyedap rasa ayam"),
            ("Saus & Bumbu", "Kecap Manis Indofood 725ml", 5, "pouch", "Bumbu ayam kecap"),
            ("Saus & Bumbu", "Minyak Wijen Pegasus 600ml", 4, "botol", "Aromatik ayam")
        ]
    },
    "Selasa": {
        "date_str": "Selasa, 10 November 2026",
        "menu_str": "Nasi + Ayam Katsu Sambal Geprek + Tahu Goreng + Mixi Vigie + Pisang",
        "porsi_besar": 2550,
        "porsi_kecil": 192,
        "items": [
            ("Protein Hewani", "Ayam Dada Fillet", 173, "kg", "Ayam katsu geprek"),
            ("Buah", "Pisang Segar", 2762, "pcs", "Pisang buffer 20 pcs"),
            ("Protein Nabati", "Tahu Putih Besar", 2772, "pcs", "Tahu goreng buffer 30 pcs"),
            ("Karbohidrat", "Beras Putih", 150, "kg", "Nasi putih"),
            ("Sayuran", "Mix Vegetable (Jagung, Polong, Wortel)", 70, "kg", "Mixi vigie tumis"),
            ("Bahan Kering", "Tepung Terigu Segitiga Biru", 30, "kg", "Adonan katsu"),
            ("Bahan Kering", "Tepung Panir Jfood", 20, "kg", "Panir katsu krispi"),
            ("Minyak", "Minyak Goreng Sawit", 104, "liter", "Menggoreng katsu & tahu"),
            ("Bahan Kering", "Bawang Putih Bubuk Desaku", 5, "pouch", "Marinate katsu"),
            ("Bahan Kering", "Chicken Powder Knorr", 5, "kg", "Penyedap rasa"),
            ("Bumbu Basah", "Bawang Putih", 11, "kg", "Sambal geprek"),
            ("Bumbu Basah", "Cabai Rawit Hijau", 7, "kg", "Sambal geprek"),
            ("Bumbu Basah", "Cabai Hijau Besar", 7, "kg", "Sambal geprek"),
            ("Bumbu Basah", "Bawang Merah Kupas", 2, "kg", "Bumbu dapur"),
            ("Bumbu Basah", "Daun Salam", 5, "ikat", "Aromatik"),
            ("Bahan Kering", "Garam Daun 250g", 6, "pcs", "Bumbu asin"),
            ("Bahan Kering", "Gula Pasir", 1, "kg", "Penyeimbang rasa")
        ]
    },
    "Rabu": {
        "date_str": "Rabu, 11 November 2026",
        "menu_str": "Nasi + Telur Fuyunghai + Saus Fuyunghai + Tempe Goreng + Polong Wortel + Anggur Muscat",
        "porsi_besar": 2550,
        "porsi_kecil": 192,
        "items": [
            ("Protein Hewani", "Telur Ayam Negeri", 130, "kg", "Fuyunghai telur (~15 butir/kg)"),
            ("Protein Nabati", "Tempe Kedelai (9 ons)", 112, "papan", "Tempe goreng gurih"),
            ("Buah", "Anggur Muscat", 171, "kg", "11.115 butir (isi 63-65/kg)"),
            ("Karbohidrat", "Beras Putih", 150, "kg", "Nasi putih"),
            ("Sayuran", "Wortel Segar", 85, "kg", "Sayur polong wortel & fuyunghai"),
            ("Sayuran", "Kacang Polong Frozen", 32, "kg", "Sayur polong wortel"),
            ("Sayuran", "Kol / Kubis Segar", 20, "kg", "Campuran telur fuyunghai"),
            ("Minyak", "Minyak Goreng Sawit", 134, "liter", "Menggoreng fuyunghai & tempe"),
            ("Saus & Bumbu", "Saos Tomat Delmonte 5L", 5, "jerigen", "Saus asam manis fuyunghai"),
            ("Saus & Bumbu", "Saos Sambal Delmonte 5L", 3, "jerigen", "Saus fuyunghai pedas manis"),
            ("Saus & Bumbu", "Saus Tiram Saori 1L", 6, "botol", "Bumbu saus fuyunghai"),
            ("Saus & Bumbu", "Kecap Inggris 600ml", 2, "botol", "Aromatik saus"),
            ("Saus & Bumbu", "Cuka Belibis 150ml", 5, "botol", "Keasaman saus fuyunghai"),
            ("Bahan Kering", "Tepung Jagung Maizenaku", 5, "kg", "Pengental saus fuyunghai"),
            ("Bumbu Basah", "Daun Bawang", 10, "ikat", "Campuran adonan fuyunghai"),
            ("Bumbu Basah", "Bawang Putih Kupas", 5, "kg", "Bumbu tumis saus"),
            ("Bumbu Basah", "Jahe", 0.5, "kg", "Penghilang amis saus"),
            ("Bumbu Basah", "Bawang Merah Kupas", 1, "kg", "Bumbu dapur"),
            ("Bahan Kering", "Garam Daun", 20, "pcs", "Bumbu garam"),
            ("Bahan Kering", "Chicken Powder Knorr", 2, "kg", "Penyedap rasa"),
            ("Bahan Kering", "Ketumbar Bubuk Yutakachi", 2, "pouch", "Bumbu marinasi tempe")
        ]
    },
    "Kamis": {
        "date_str": "Kamis, 12 November 2026",
        "menu_str": "Nasi + Lele Crispy + Sambal Bawang + Edamame + Kakiage + Kelengkeng",
        "porsi_besar": 2550,
        "porsi_kecil": 192,
        "items": [
            ("Protein Hewani", "Ikan Lele Utuh (isi 10/kg)", 278, "kg", "2.780 ekor lele crispy"),
            ("Protein Hewani", "Telur Ayam (Lapisan Tepung)", 30, "kg", "Adonan pelapis tepung lele"),
            ("Buah", "Kelengkeng Manis", 120, "kg", "9.600 butir (4-5 pcs per porsi)"),
            ("Protein Nabati", "Edamame Frozen", 60, "kg", "Edamame rebus segar"),
            ("Karbohidrat", "Beras Putih", 150, "kg", "Nasi putih"),
            ("Sayuran", "Wortel Segar", 45, "kg", "Bahan bakwan kakiage"),
            ("Sayuran", "Kol / Kubis", 40, "kg", "Bahan bakwan kakiage"),
            ("Bahan Kering", "Tepung Terigu Segitiga Biru", 75, "kg", "Tepung lele crispy & kakiage"),
            ("Bahan Kering", "Tepung Beras Rose Brand", 25, "kg", "Perenyah lele crispy"),
            ("Minyak", "Minyak Goreng Sawit", 71, "liter", "Menggoreng lele & kakiage"),
            ("Bumbu Basah", "Bawang Putih", 9, "kg", "Sambal bawang & bumbu lele"),
            ("Bumbu Basah", "Cabai Rawit Setan", 6, "kg", "Sambal bawang pedas"),
            ("Bumbu Basah", "Bawang Merah Kupas", 7, "kg", "Sambal bawang"),
            ("Bumbu Basah", "Jeruk Nipis", 8, "kg", "Penghilang amis lele"),
            ("Bumbu Basah", "Daun Jeruk", 0.5, "kg", "Aromatik sambal"),
            ("Bahan Kering", "Kunyit Bubuk Desaku", 2, "pouch", "Bumbu marinasi kuning lele"),
            ("Bahan Kering", "Ketumbar Bubuk Yutakachi", 4, "pouch", "Bumbu marinasi lele"),
            ("Bahan Kering", "Garam Daun", 29.1, "pcs", "Bumbu dapur"),
            ("Bahan Kering", "Gula Merah", 2, "kg", "Sambal bawang"),
            ("Bahan Kering", "Tepung Jagung Maizenaku", 2.1, "kg", "Pengering adonan")
        ]
    },
    "Jumat": {
        "date_str": "Jumat, 13 November 2026",
        "menu_str": "Nasi + Ayam Crispy Sambal Bajak + Tempe Goreng + Mixi Vigie + Anggur Merah",
        "porsi_besar": 1902,
        "porsi_kecil": 192,
        "items": [
            ("Protein Hewani", "Ayam Dada Fillet", 132, "kg", "Ayam fillet crispy"),
            ("Protein Nabati", "Tempe Kedelai (9 ons)", 85, "papan", "Tempe goreng"),
            ("Buah", "Anggur Red Globe / China", 97, "kg", "8.245 butir (4-5 pcs per porsi)"),
            ("Karbohidrat", "Beras Putih", 103, "kg", "Nasi putih porsi jumat"),
            ("Sayuran", "Mix Vegetable", 60, "kg", "Sayur mixi vigie"),
            ("Bahan Kering", "Tepung Jagung Maizenaku", 20, "kg", "Tepung adonan crispy"),
            ("Minyak", "Minyak Goreng Sawit", 30, "liter", "Menggoreng ayam & tempe"),
            ("Bumbu Basah", "Cabai Merah Teropong", 6, "kg", "Sambal bajak matang"),
            ("Bumbu Basah", "Cabai Rawit Setan", 5, "kg", "Sambal bajak matang"),
            ("Bumbu Basah", "Bawang Merah Kupas", 7, "kg", "Sambal bajak matang"),
            ("Bumbu Basah", "Bawang Putih", 3, "kg", "Sambal bajak matang"),
            ("Bumbu Basah", "Tomat Sayur", 7, "kg", "Sambal bajak matang"),
            ("Bahan Kering", "Bawang Putih Bubuk Desaku", 4, "pouch", "Marinasi ayam crispy"),
            ("Bahan Kering", "Kaldu Jamur 80g", 4, "pouch", "Penyedap rasa"),
            ("Bahan Kering", "Gula Merah", 2, "kg", "Sambal bajak"),
            ("Bahan Kering", "Gula Pasir", 2, "kg", "Bumbu dapur"),
            ("Bahan Kering", "Garam Daun", 24, "pcs", "Bumbu dapur")
        ]
    }
}

for day_name, d in menu_data.items():
    if day_name in wb.sheetnames:
        ws = wb[day_name]
        ws['D9'] = d["date_str"]
        ws['D10'] = d["menu_str"]
        ws['K12'] = d["porsi_besar"]
        ws['K13'] = d["porsi_kecil"]
        ws['K14'] = '=K12+K13'
        ws['D14'] = 'Petugas QC / ASLAP Kedungwuni 4'
        ws['K38'] = '( ASLAP / Chef Lutfi )'

        # Unmerge any merged ranges in rows 17-38
        to_unmerge = []
        for r_range in list(ws.merged_cells.ranges):
            if any(17 <= row <= 38 for row in range(r_range.min_row, r_range.max_row + 1)):
                to_unmerge.append(r_range)
        for r_range in to_unmerge:
            ws.unmerge_cells(str(r_range))

        # Kosongkan baris item 17-38
        for r in range(17, 39):
            for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']:
                ws[f'{col}{r}'].value = None

        # Isi item baru
        for idx, (kat, it, jml, sat, ket) in enumerate(d["items"]):
            r = 17 + idx
            ws[f'A{r}'] = idx + 1
            ws[f'B{r}'] = kat
            ws[f'C{r}'] = it
            ws[f'D{r}'] = sat
            ws[f'E{r}'] = jml
            ws[f'G{r}'] = f'=IFERROR(E{r}-F{r},"")'
            ws[f'H{r}'] = f'=IFERROR(G{r}/E{r},"")'
            ws[f'J{r}'] = f'=IFERROR(F{r}-I{r},"")'
            ws[f'K{r}'] = f'=IFERROR(J{r}/F{r},"")'
            ws[f'M{r}'] = f'=IFERROR(I{r}-L{r},"")'
            ws[f'N{r}'] = ket

wb.save('live_monitoring.xlsx')
print("SUCCESS_UPDATE_LOCAL_EXCEL")

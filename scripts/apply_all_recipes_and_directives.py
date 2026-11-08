import re
import os

new_weekly_menu_code = '''let weeklyMenuCycles = {
  cycle1: {
    label: "Menu Resmi: 09 - 13 November 2026",
    days: {
      senin: {
        title: "Nasi + Ayam Rica-Rica (PB) / Ayam Kecap (PK) + Tahu Goreng + Tumis Putren Wortel + Jeruk",
        nutrition: "Energi 685 kkal • Protein 28 gr • Karbohidrat Kompleks & Serat",
        notePersiapan: "PIC: Pak Yudi & Ikbal. ATURAN EMAS: (1) Ayam potong dadu seragam +-2x2 cm (12-14 g), 5 dadu/porsi. (2) Ayam PB = RICA, ayam PK = KECAP (dua baskom, dua label terpisah, jangan tertukar). (3) Tahu ditekan/dikeringkan sebelum digoreng. (4) Putren dan wortel dipotong seragam di wadah terpisah. (5) 3 siswa alergi nasi (SMK 2, MTs 1): siapkan karbo pengganti & label khusus. (6) Uji goreng 20 dadu ayam bersama Bu Ricky/Bu Linda: timbang matang per 5 dadu wajib +-60 g.",
        notePengolahan: "Goreng dadu ayam berbalut adonan celup tipis di minyak panas 160°C (suhu inti wajib >= 75°C). Masak bumbu rica pedas sedang untuk PB (2.550 porsi) dan bumbu kecap manis gurih tanpa cabai untuk PK (192 porsi). Goreng tahu putih hingga berkulit keemasan dan kesat. Tumis putren & wortel cepat dengan bumbu harum agar tetap renyah cerah dan tidak berair menggenang.",
        notePemorsian: "TOTAL 2.742 PORSI (13.710 WADAH): SMK 1 Kedungwuni 1.712 PB (8.560 wadah), MTs Salafiyah 646 PB (3.230 wadah), Posyandu Ambokembang 185 (86 PB, 99 PK = 925 wadah), Posyandu Panjomblangan 188 (95 PB, 93 PK = 940 wadah), Sampel & Uji Organoleptik 11 PB (55 wadah). URUTAN MEMORSI: (1) Jeruk 1 buah, (2) Nasi +-100 g hangat, (3) Tumis Putren Wortel 30 g tiris, (4) Tahu Goreng 30 g kesat, (5) Ayam Rica/Kecap +-5 dadu (60 g) PALING AKHIR. Tunggu uap berkurang baru tutup wadah.",
        items: [
          { name: "Beras Putih (Nasi)", category: "Karbohidrat", portion: "100 gr", targetOrder: "150.00 kg", supplier: "PO-007 / Koperasi Tani", tare: "0.85", persiapan: "Cuci beras 2-3 kali air mengalir sampai jernih, tiriskan. Siapkan karbo non-nasi untuk 3 siswa alergi nasi (SMK 2, MTs 1).", pengolahan: "Takar air rasio 1:1,1-1,2. Masak di rice steamer hingga pulen mekar matang sempurna (1 kg beras = 19 porsi).", pemorsian: "Takar 100 gr nasi hangat di sekat karbohidrat utama." },
          { name: "Ayam Rica-Rica (PB - Porsi Besar)", category: "Protein Hewani", portion: "60 gr (5 dadu)", targetOrder: "162.00 kg", supplier: "PO-007 / Daging Ayam Fillet", tare: "0.85", persiapan: "Potong dadu +-2x2 cm (12-14 g), 5 dadu per porsi (total 12.750 dadu PB). Marinasi bawang putih, lada, garam 20-30 menit di chiller. Celup adonan tipis.", pengolahan: "Goreng dadu ayam hingga keemasan matang (suhu inti >= 75°C). Tumis bumbu rica pedas sedang, aduk rata meresap dan tidak berair.", pemorsian: "Tata 5 dadu (+-60 g) ayam rica di sekat lauk utama PB (SMK 1, MTs, Posyandu PB, Sampel). Masukkan PALING AKHIR." },
          { name: "Ayam Kecap Gurih (PK - Porsi Kecil)", category: "Protein Hewani", portion: "60 gr (5 dadu)", targetOrder: "12.00 kg", supplier: "PO-007 / Daging Ayam Fillet", tare: "0.85", persiapan: "Potong dadu +-2x2 cm (960 dadu PK). Baskom & label terpisah dari PB. Iris bawang merah, cincang bawang putih, sisir gula merah TANPA cabai.", pengolahan: "Goreng ayam dadu matang empuk. Masak bumbu kecap manis gurih tidak pedas, karamelisasi ringan meresap.", pemorsian: "Tata 5 dadu (+-60 g) ayam kecap khusus wadah PK (Posyandu Ambokembang 99 wadah & Panjomblangan 93 wadah). JANGAN TERTUKAR DENGAN RICA!" },
          { name: "Tahu Putih Besar (Goreng)", category: "Protein Nabati", portion: "30 gr (1 potong)", targetOrder: "2.772 pcs", supplier: "PO-007 / Tahu Putih Besar", tare: "0.50", persiapan: "Timbang 10 pcs awal patokan berat. Potong +-3x3 cm, tiriskan dan tekan/keringkan sebelum digoreng agar minyak tidak muncrat.", pengolahan: "Goreng dalam minyak panas hingga berkulit kuning keemasan, tiriskan sampai kesat dan tidak berminyak berlebih.", pemorsian: "Tata 1 potong tahu goreng (30 g) di sekat lauk pendamping nabati." },
          { name: "Tumis Putren Wortel", category: "Sayuran Segar", portion: "30 gr", targetOrder: "96.00 kg", supplier: "PO-007 / Sayuran Segar (48kg Putren + 48kg Wortel)", tare: "0.50", persiapan: "Kupas wortel dan siangi putren, potong seragam. Cuci 3x air mengalir, simpan di wadah terpisah per jenis.", pengolahan: "Tumis cepat dengan bawang putih lada api besar agar sayuran tetap renyah, warna cerah, dan kuah tidak menggenang berair.", pemorsian: "Tiriskan kuah berlebih, takar 30 gr di sekat sayur ompreng." },
          { name: "Jeruk Medan Segar", category: "Buah Segar", portion: "1 buah", targetOrder: "242.00 kg", supplier: "PO-007 / Jeruk Medan (isi 10-12/kg)", tare: "0.00", persiapan: "Sortir buah utuh, singkirkan buah memar atau busuk. Hitung jumlah buah saat datang (kebutuhan 2.742 buah + cadangan 3%).", pengolahan: "Dilarang terkena panas/kompor. Lap bersih dan keringkan kulit buah dengan kain sanitasi steril.", pemorsian: "Paling awal dikerjakan: masukkan 1 buah jeruk segar ke sekat buah tiap wadah." }
        ]
      },
      selasa: {
        title: "Nasi + Ayam Katsu Sambal Geprek + Tahu Goreng + Mix Vegetable + Pisang",
        nutrition: "Energi 710 kkal • Protein 29 gr • Kaya Vitamin A & C",
        notePersiapan: "Fillet dada ayam ditipiskan rata untuk katsu, marinasi bawang putih lada. Cuci bersih mix vegetable (jagung, polong, wortel). Tahu putih dipotong kotak seragam.",
        notePengolahan: "Balur ayam katsu dengan tepung terigu, telur, dan panir. Goreng deep fry minyak 165°C hingga kuning emas krispi (suhu inti >= 75°C). Ulek sambal geprek tanak. Tumis mix vegetable mentega gurih cepat.",
        notePemorsian: "Ompreng diisi nasi hangat 100 gr di sekat utama, ayam katsu krispi digeprek sambal di sekat lauk, tahu goreng, dan mix vegetable 30 gr. Pisang segar di sekat buah.",
        items: [
          { name: "Beras Putih Premium", category: "Karbohidrat", portion: "100 gr", targetOrder: "150.00 kg", supplier: "PO-012 / Koperasi Tani", tare: "0.85", persiapan: "Cuci beras bersih tiris.", pengolahan: "Masak hingga pulen mekar matang.", pemorsian: "Takar 100 gr sekat utama." },
          { name: "Ayam Katsu Sambal Geprek", category: "Protein Hewani", portion: "60 gr", targetOrder: "173.00 kg", supplier: "PO-012 / Daging Ayam Fillet", tare: "0.85", persiapan: "Pipihkan fillet dada ayam, marinasi lada bawang putih.", pengolahan: "Balur tepung panir, goreng keemasan renyah suhu 165°C. Geprek dengan sambal cabai bawang tanak.", pemorsian: "Tata 1 potong katsu geprek di sekat lauk utama." },
          { name: "Tahu Putih Goreng", category: "Protein Nabati", portion: "30 gr", targetOrder: "2.772 pcs", supplier: "PO-012 / Tahu Putih Besar", tare: "0.50", persiapan: "Potong tahu seragam, tiriskan airnya.", pengolahan: "Goreng minyak panas hingga berkulit keemasan kesat.", pemorsian: "Tata 1 potong tahu di sekat nabati." },
          { name: "Mix Vegetable (Jagung, Polong, Wortel)", category: "Sayuran Segar", portion: "30 gr", targetOrder: "70.00 kg", supplier: "PO-012 / Sayuran Segar", tare: "0.50", persiapan: "Cuci bersih jagung pipil, wortel dadu, dan polong.", pengolahan: "Tumis mentega gurih api besar agar warna tetap cerah.", pemorsian: "Takar 30 gr di sekat sayur." },
          { name: "Pisang Segar", category: "Buah Segar", portion: "1 pcs", targetOrder: "2.762 pcs", supplier: "PO-012 / Buah Nusantara", tare: "0.00", persiapan: "Sortir buah pisang matang mulus higienis.", pengolahan: "Dilarang terkena suhu panas.", pemorsian: "Letakkan 1 buah pisang di sekat buah." }
        ]
      },
      rabu: {
        title: "Nasi + Telur Fuyunghai + Saus Asam Manis + Tempe Goreng + Tumis Polong Wortel Kol + Anggur Muscat",
        nutrition: "Energi 695 kkal • Protein 27 gr • Tinggi Antioksidan & Serat",
        notePersiapan: "Kocok telur bersama cincangan sayuran wortel & kol untuk fuyunghai. Potong tempe kedelai seragam, marinasi bumbu ketumbar bawang garam.",
        notePengolahan: "Goreng fuyunghai tebal matang merata hingga keemasan. Masak saus fuyunghai asam manis mengental gurih berkilap. Goreng tempe renyah garing. Tumis sayuran polong wortel cepat.",
        notePemorsian: "Nasi pulen 100 gr sekat utama, 1 porsi fuyunghai disiram saus asam manis di sekat lauk utama, tempe goreng dan tumis sayur. Anggur muscat segar di sekat buah.",
        items: [
          { name: "Beras Putih Premium", category: "Karbohidrat", portion: "100 gr", targetOrder: "150.00 kg", supplier: "PO-017 / Koperasi Tani", tare: "0.85", persiapan: "Cuci beras bersih tiris.", pengolahan: "Kukus pulen standar BGN.", pemorsian: "Takar 100 gr di sekat utama." },
          { name: "Telur Fuyunghai + Saus Asam Manis", category: "Protein Hewani", portion: "1 porsi (60 gr)", targetOrder: "130.00 kg telur", supplier: "PO-017 / Telur Ayam", tare: "0.85", persiapan: "Kocok telur campur wortel kol cincang halus.", pengolahan: "Goreng dadar fuyunghai tebal matang merata. Siram saus asam manis lezat.", pemorsian: "Tata 1 porsi fuyunghai di sekat lauk utama." },
          { name: "Tempe Goreng Gurih", category: "Protein Nabati", portion: "30 gr", targetOrder: "112 papan", supplier: "PO-017 / Tempe Kedelai", tare: "0.50", persiapan: "Potong tempe seragam, rendam air garam bawang.", pengolahan: "Goreng minyak panas hingga kuning renyah tiris.", pemorsian: "Tata 1 potong tempe di samping fuyunghai." },
          { name: "Tumis Polong Wortel Kol", category: "Sayuran Segar", portion: "30 gr", targetOrder: "137.00 kg", supplier: "PO-017 / Sayuran (Wortel 85kg, Polong 32kg, Kol 20kg)", tare: "0.50", persiapan: "Iris wortel koin, kol tipis, cuci tiris bersih.", pengolahan: "Tumis bawang putih lada wangi gurih renyah.", pemorsian: "Takar 30 gr di sekat sayur." },
          { name: "Anggur Muscat Segar", category: "Buah Segar", portion: "50 gr", targetOrder: "171.00 kg", supplier: "PO-017 / Buah Nusantara", tare: "0.50", persiapan: "Sortir buah anggur segar utuh manis.", pengolahan: "Cuci dengan air mengalir dingin, tiriskan sempurna.", pemorsian: "Timbang porsi anggur di sekat buah tertutup." }
        ]
      },
      kamis: {
        title: "Nasi + Ikan Lele Crispy + Sambal Bawang + Edamame Rebus + Kakiage Sayur + Kelengkeng",
        nutrition: "Energi 715 kkal • Protein 30 gr • Tinggi Omega-3 & Kalsium",
        notePersiapan: "Bersihkan ikan lele utuh, kerat badan, marinasi kunyit bawang putih garam. Iris wortel dan kol halus untuk kakiage. Sortir edamame segar.",
        notePengolahan: "Balur lele dengan adonan tepung renyah, goreng minyak banyak hingga garing keemasan. Goreng kakiage krispi tidak berminyak. Rebus edamame air garam 5 menit.",
        notePemorsian: "Nasi putih 100 gr sekat utama, 1 ekor lele crispy + sambal bawang di sekat lauk, kakiage dan edamame di sekat pendamping. Kelengkeng manis di sekat buah.",
        items: [
          { name: "Beras Putih Premium", category: "Karbohidrat", portion: "100 gr", targetOrder: "150.00 kg", supplier: "PO-022 / Koperasi Tani", tare: "0.85", persiapan: "Cuci beras bersih tiris.", pengolahan: "Masak hingga pulen mekar.", pemorsian: "Takar 100 gr sekat utama." },
          { name: "Ikan Lele Crispy + Sambal Bawang", category: "Protein Hewani", portion: "1 ekor", targetOrder: "278.00 kg (isi 10/kg)", supplier: "PO-022 / Ikan Segar", tare: "0.85", persiapan: "Bersihkan isi perut lele, cuci bersih, kerat badan.", pengolahan: "Balur tepung krispi, goreng deep fry hingga kering garing renyah merata.", pemorsian: "Tata 1 ekor lele krispi + sesendok sambal bawang di sekat lauk." },
          { name: "Edamame Rebus Garam", category: "Protein Nabati", portion: "30 gr", targetOrder: "60.00 kg", supplier: "PO-022 / Edamame Frozen", tare: "0.50", persiapan: "Sortir polong edamame segar.", pengolahan: "Rebus dalam air garam ringan 5-6 menit, tiriskan.", pemorsian: "Tata 30 gr di sekat pendamping." },
          { name: "Kakiage (Bakwan Sayur Jepang)", category: "Sayuran Segar", portion: "1 pcs (30 gr)", targetOrder: "85.00 kg (Wortel 45kg + Kol 40kg)", supplier: "PO-022 / Sayuran", tare: "0.50", persiapan: "Iris wortel & kol korek api halus.", pengolahan: "Campur adonan tepung dingin, goreng krispi keemasan tiris minyak.", pemorsian: "Tata 1 pcs kakiage krispi di sekat sayur." },
          { name: "Kelengkeng Manis Segar", category: "Buah Segar", portion: "40 gr", targetOrder: "120.00 kg", supplier: "PO-022 / Buah Nusantara", tare: "0.50", persiapan: "Sortir kelengkeng manis segar utuh.", pengolahan: "Dilarang terkena panas kompor.", pemorsian: "Tata di sekat buah ompreng." }
        ]
      },
      jumat: {
        title: "Nasi + Ayam Crispy Sambal Bajak + Tempe Goreng + Mix Vegetable + Anggur Red Globe",
        nutrition: "Energi 690 kkal • Protein 28 gr • Kaya Vitamin & Mineral",
        notePersiapan: "Potong fillet dada ayam untuk crispy (2.094 porsi). Potong tempe seragam. Siapkan mix vegetable.",
        notePengolahan: "Goreng ayam berbalut tepung keriting renyah suhu 165°C hingga matang sempurna suhu inti >= 75°C. Masak sambal bajak tanak harum gurih. Goreng tempe keemasan. Tumis mix vegetable mentega gurih.",
        notePemorsian: "Nasi hangat 100 gr sekat utama, ayam crispy disiram sambal bajak di sekat lauk, tempe goreng dan mix vegetable. Anggur red globe di sekat buah.",
        items: [
          { name: "Beras Putih Premium", category: "Karbohidrat", portion: "100 gr", targetOrder: "103.00 kg", supplier: "PO-027 / Koperasi Tani", tare: "0.85", persiapan: "Cuci beras hingga bersih tiris.", pengolahan: "Masak hingga pulen mekar matang.", pemorsian: "Takar 100 gr sekat utama." },
          { name: "Ayam Crispy Sambal Bajak", category: "Protein Hewani", portion: "60 gr", targetOrder: "132.00 kg", supplier: "PO-027 / Daging Ayam Fillet", tare: "0.85", persiapan: "Potong fillet dada ayam sesuai porsi 2.094.", pengolahan: "Balur tepung krispi keriting, goreng renyah keemasan. Tumis sambal bajak matang tanak harum.", pemorsian: "Tata 1 potong ayam crispy disiram sambal bajak di sekat lauk." },
          { name: "Tempe Goreng Gurih", category: "Protein Nabati", portion: "30 gr", targetOrder: "85 papan", supplier: "PO-027 / Tempe Kedelai", tare: "0.50", persiapan: "Potong tempe persegi seragam.", pengolahan: "Goreng keemasan gurih tiris minyak.", pemorsian: "Tata 1 potong tempe di sekat nabati." },
          { name: "Mix Vegetable (Jagung, Polong, Wortel)", category: "Sayuran Segar", portion: "30 gr", targetOrder: "60.00 kg", supplier: "PO-027 / Sayuran", tare: "0.50", persiapan: "Siapkan jagung manis, polong, wortel bersih.", pengolahan: "Tumis mentega gurih api besar warna tetap cerah.", pemorsian: "Takar 30 gr di sekat sayur." },
          { name: "Anggur Red Globe Segar", category: "Buah Segar", portion: "45 gr", targetOrder: "97.00 kg", supplier: "PO-027 / Buah Nusantara", tare: "0.50", persiapan: "Sortir buah anggur merah segar bersih.", pengolahan: "Cuci air mengalir dingin, tiriskan.", pemorsian: "Tata di sekat buah tertutup." }
        ]
      }
    }
  }
};'''

target_files = [
    'preview.html',
    'index.html',
    'mbg_chef_monitor/assets/web/index.html'
]

pattern = re.compile(r'let weeklyMenuCycles = \{.*?\n\s*\};\n', re.DOTALL)

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        if pattern.search(content):
            new_content = pattern.sub(new_weekly_menu_code + '\n', content)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated weeklyMenuCycles in {fpath}")
        else:
            print(f"Pattern NOT found in {fpath}")
    else:
        print(f"File not found: {fpath}")


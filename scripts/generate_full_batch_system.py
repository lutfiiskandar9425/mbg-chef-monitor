# -*- coding: utf-8 -*-
import json

school_batches_js = """
// ========================================================
// DATA RESMI BATCH DISTRIBUSI SEKOLAH & LOKASI (SENIN - JUMAT)
// ========================================================
const schoolBatchesData = {
  senin: {
    title: "Senin, 9 November 2026",
    menu: "Nasi + Ayam Rica (PB) / Ayam Kecap (PK) + Tahu Goreng + Tumis Putren Wortel + Jeruk",
    locations: [
      {
        id: "all",
        name: "Total Keseluruhan (5 Titik)",
        badge: "2.742 Porsi • 13.710 Wadah (x5 Item)",
        pb: 2550,
        pk: 192,
        totalPorsi: 2742,
        totalWadah: 13710,
        driver: "Armada SPPG 1, 2, 3 & QC Lab",
        jamBerangkat: "09:00 - 09:45 WIB",
        jamPemorsian: "07:30 - Selesai",
        alergiNotice: "PERHATIAN ALERGI: 3 Siswa Alergi Nasi (SMK 1: 2 siswa, MTs: 1 siswa). Siapkan wadah karbo non-nasi khusus berlabel 'ALERGI NASI'.",
        posyanduNotice: "PEMBAGIAN AYAM: 2.550 Wadah Ayam Rica (PB, pedas sedang) & 192 Wadah Ayam Kecap (PK, balita tidak pedas). Dua baskom berbeda, jangan tertukar!",
        items: [
          { name: "Nasi Putih", perPorsi: "+-100 g", total: "274,20 kg", wadah: "2.742", note: "144,3 kg beras (1 kg = 19 porsi). 3 wadah karbo pengganti non-nasi alergi." },
          { name: "Ayam Rica (PB - Porsi Besar)", perPorsi: "60 g (5 dadu)", total: "153,00 kg", wadah: "2.550", note: "12.750 dadu ayam rica (SMK 1.712, MTs 646, Ambokembang 86, Panjomblangan 95, Sampel 11)." },
          { name: "Ayam Kecap (PK - Balita)", perPorsi: "60 g (5 dadu)", total: "11,52 kg", wadah: "192", note: "960 dadu ayam kecap manis gurih TANPA cabai (Ambokembang 99, Panjomblangan 93)." },
          { name: "Tahu Putih Goreng", perPorsi: "30 g (1 potong)", total: "82,26 kg", wadah: "2.742", note: "2.742 potong +-3x3 cm, ditekan/dikeringkan sebelum digoreng agar minyak tidak muncrat." },
          { name: "Tumis Putren Wortel", perPorsi: "30 g", total: "82,26 kg", wadah: "2.742", note: "Putren 48 kg + Wortel 48 kg (total 96 kg mentah). Tiriskan kuah berlebih." },
          { name: "Jeruk Medan Segar", perPorsi: "1 buah", total: "2.742 buah", wadah: "2.742", note: "Sortir buah utuh, lap kering steril (cadangan +3% = 242 kg PO, isi 10-12/kg)." }
        ]
      },
      {
        id: "smk1",
        name: "SMK 1 Kedungwuni",
        badge: "1.712 Porsi PB • 8.560 Wadah",
        pb: 1712,
        pk: 0,
        totalPorsi: 1712,
        totalWadah: 8560,
        driver: "Driver Armada 1",
        jamBerangkat: "09:30 WIB",
        jamPemorsian: "07:30 - 08:45 WIB",
        alergiNotice: "⚠️ ALERGI NASI (2 SISWA): Wadah Nasi Biasa = 1.710 wadah | Wadah Pengganti Karbo Non-Nasi = 2 wadah berlabel mencolok 'ALERGI NASI' (saran Chef: kentang kukus 150g).",
        posyanduNotice: "Semua porsi di SMK 1 adalah PB, jadi ayam yang diisi HANYA AYAM RICA (pedas sedang).",
        items: [
          { name: "Nasi Putih Biasa", perPorsi: "+-100 g", total: "171,00 kg", wadah: "1.710", note: "Nasi pulen hangat dari rice steamer" },
          { name: "Pengganti Karbo (Alergi Nasi)", perPorsi: "1 porsi (150 g)", total: "2 wadah", wadah: "2", note: "Wadah karbo non-nasi dengan stiker 'ALERGI NASI'" },
          { name: "Ayam Rica (PB)", perPorsi: "60 g (5 dadu)", total: "102,72 kg", wadah: "1.712", note: "8.560 dadu ayam rica pedas sedang" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g (1 potong)", total: "51,36 kg", wadah: "1.712", note: "1.712 potong tahu keemasan kesat" },
          { name: "Tumis Putren Wortel", perPorsi: "30 g", total: "51,36 kg", wadah: "1.712", note: "1.712 wadah sayur cerah renyah tiris" },
          { name: "Jeruk Medan", perPorsi: "1 buah", total: "1.712 buah", wadah: "1.712", note: "Paling awal dimasukkan ke sekat buah" }
        ]
      },
      {
        id: "mts",
        name: "MTs Salafiyah Syafiiyah",
        badge: "646 Porsi PB • 3.230 Wadah",
        pb: 646,
        pk: 0,
        totalPorsi: 646,
        totalWadah: 3230,
        driver: "Driver Armada 2",
        jamBerangkat: "09:45 WIB",
        jamPemorsian: "08:15 - 09:15 WIB",
        alergiNotice: "⚠️ ALERGI NASI (1 SISWA): Wadah Nasi Biasa = 645 wadah | Wadah Pengganti Karbo Non-Nasi = 1 wadah berlabel mencolok 'ALERGI NASI'.",
        posyanduNotice: "Semua porsi di MTs adalah PB, ayam yang diisi HANYA AYAM RICA (pedas sedang).",
        items: [
          { name: "Nasi Putih Biasa", perPorsi: "+-100 g", total: "64,50 kg", wadah: "645", note: "Nasi pulen hangat" },
          { name: "Pengganti Karbo (Alergi Nasi)", perPorsi: "1 porsi (150 g)", total: "1 wadah", wadah: "1", note: "Wadah karbo non-nasi khusus" },
          { name: "Ayam Rica (PB)", perPorsi: "60 g (5 dadu)", total: "38,76 kg", wadah: "646", note: "3.230 dadu ayam rica" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g (1 potong)", total: "19,38 kg", wadah: "646", note: "646 potong tahu keemasan" },
          { name: "Tumis Putren Wortel", perPorsi: "30 g", total: "19,38 kg", wadah: "646", note: "646 wadah sayur tiris" },
          { name: "Jeruk Medan", perPorsi: "1 buah", total: "646 buah", wadah: "646", note: "Lap bersih kulit kering steril" }
        ]
      },
      {
        id: "posyandu_ambo",
        name: "Posyandu Ambokembang",
        badge: "185 Porsi (86 PB + 99 PK) • 925 Wadah",
        pb: 86,
        pk: 99,
        totalPorsi: 185,
        totalWadah: 925,
        driver: "Driver Armada 3",
        jamBerangkat: "09:00 WIB",
        jamPemorsian: "07:30 - 08:30 WIB",
        alergiNotice: "👶 WADAH KHUSUS BALITA (PK): 99 Wadah Ayam Kecap Manis Gurih TANPA CABAI. Jangan sampai tertukar dengan 86 Wadah Ayam Rica (PB). Siapkan 2 baskom berlabel berbeda!",
        posyanduNotice: "86 Wadah Ayam Rica (PB) + 99 Wadah Ayam Kecap (PK). Total 185 porsi.",
        items: [
          { name: "Nasi Putih", perPorsi: "+-100 g", total: "18,50 kg", wadah: "185", note: "185 wadah nasi hangat" },
          { name: "Ayam Rica (PB)", perPorsi: "60 g (5 dadu)", total: "5,16 kg", wadah: "86", note: "86 wadah PB porsi besar (430 dadu rica)" },
          { name: "Ayam Kecap (PK Balita)", perPorsi: "60 g (5 dadu)", total: "5,94 kg", wadah: "99", note: "99 wadah balita (495 dadu kecap manis tanpa cabai)" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g (1 potong)", total: "5,55 kg", wadah: "185", note: "185 potong tahu goreng kesat" },
          { name: "Tumis Putren Wortel", perPorsi: "30 g", total: "5,55 kg", wadah: "185", note: "185 wadah sayur tiris cerah" },
          { name: "Jeruk Medan", perPorsi: "1 buah", total: "185 buah", wadah: "185", note: "185 buah jeruk mulus tidak memar" }
        ]
      },
      {
        id: "posyandu_panjom",
        name: "Posyandu Panjomblangan",
        badge: "188 Porsi (95 PB + 93 PK) • 940 Wadah",
        pb: 95,
        pk: 93,
        totalPorsi: 188,
        totalWadah: 940,
        driver: "Driver Armada 3",
        jamBerangkat: "09:15 WIB",
        jamPemorsian: "07:45 - 08:45 WIB",
        alergiNotice: "👶 WADAH KHUSUS BALITA (PK): 93 Wadah Ayam Kecap Manis Gurih TANPA CABAI. Jangan sampai tertukar dengan 95 Wadah Ayam Rica (PB). Siapkan 2 baskom berlabel berbeda!",
        posyanduNotice: "95 Wadah Ayam Rica (PB) + 93 Wadah Ayam Kecap (PK). Total 188 porsi.",
        items: [
          { name: "Nasi Putih", perPorsi: "+-100 g", total: "18,80 kg", wadah: "188", note: "188 wadah nasi hangat" },
          { name: "Ayam Rica (PB)", perPorsi: "60 g (5 dadu)", total: "5,70 kg", wadah: "95", note: "95 wadah PB porsi besar (475 dadu rica)" },
          { name: "Ayam Kecap (PK Balita)", perPorsi: "60 g (5 dadu)", total: "5,58 kg", wadah: "93", note: "93 wadah balita (465 dadu kecap manis tanpa cabai)" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g (1 potong)", total: "5,64 kg", wadah: "188", note: "188 potong tahu goreng kesat" },
          { name: "Tumis Putren Wortel", perPorsi: "30 g", total: "5,64 kg", wadah: "188", note: "188 wadah sayur tiris cerah" },
          { name: "Jeruk Medan", perPorsi: "1 buah", total: "188 buah", wadah: "188", note: "188 buah jeruk mulus tidak memar" }
        ]
      },
      {
        id: "sampel",
        name: "Sampel & Uji Organoleptik",
        badge: "11 Porsi PB • 55 Wadah",
        pb: 11,
        pk: 0,
        totalPorsi: 11,
        totalWadah: 55,
        driver: "QC Lab Dapur SPPG",
        jamBerangkat: "Sebelum Distribusi",
        jamPemorsian: "07:00 WIB (Paling Awal)",
        alergiNotice: "🔬 WADAH KHUSUS QC LAB: 2 Sampel Arsip Simpan Dapur + 9 Uji Organoleptik Ahli Gizi / Kepala SPPG. Wadah wajib berlabel 'SAMPEL / UJI'.",
        posyanduNotice: "11 Porsi PB (Ayam Rica). Satu set diserahkan ke Ahli Gizi / Kepala SPPG sesuai arahan Chef.",
        items: [
          { name: "Nasi Putih", perPorsi: "+-100 g", total: "1,10 kg", wadah: "11", note: "11 wadah sampel uji" },
          { name: "Ayam Rica (PB)", perPorsi: "60 g (5 dadu)", total: "0,66 kg", wadah: "11", note: "55 dadu ayam rica" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g (1 potong)", total: "0,33 kg", wadah: "11", note: "11 potong tahu" },
          { name: "Tumis Putren Wortel", perPorsi: "30 g", total: "0,33 kg", wadah: "11", note: "11 wadah sayur" },
          { name: "Jeruk Medan", perPorsi: "1 buah", total: "11 buah", wadah: "11", note: "11 buah jeruk" }
        ]
      }
    ],
    posKerja: [
      { pos: "Pos Nasi", picSerah: "Rizal (Pengolahan Umum)", tugas: "Timbang beras 144,3 kg (1:1,1 air), cuci 2-3x, tiriskan. Siapkan karbo pengganti untuk 3 siswa alergi nasi (SMK 2, MTs 1).", target: "274,2 kg matang (1 kg = 19 porsi)" },
      { pos: "Pos Ayam", picSerah: "Bu Ricky & Bu Linda (ProHe)", tugas: "Potong dadu +-2x2 cm (12-14 g), 5 dadu/porsi (PB: 12.750 dadu, PK: 960 dadu). Marinasi chiller 20-30 mnt, celup tepung. Bumbu rica & kecap.", target: "174 kg fillet mentah" },
      { pos: "Pos Tahu", picSerah: "Faiz (ProNa)", tugas: "Timbang 10 pcs awal patokan, tekan perlahan dengan kain bersih sampai kering, potong 3x3x1,5 cm (target 30g matang), rendam air garam bawang.", target: "2.772 pcs mentah (82,26 kg matang)" },
      { pos: "Pos Sayur", picSerah: "Abidin (Sayur)", tugas: "Kupas & potong putren serong 2,5 cm, wortel iris setengah bulan 0,4 cm. Bawang merah/putih iris. Wadah terpisah.", target: "Putren 48 kg + Wortel 48 kg" },
      { pos: "Pos Jeruk", picSerah: "Tim Pemorsian", tugas: "Hitung saat datang (242 kg isi 10-12/kg = 2.742 buah + cadangan 3%), sortir memar, lap kulit bersih kering dengan kain sanitasi.", target: "2.742 buah mulus" },
      { pos: "Pos Pemorsian", picSerah: "Driver Armada & Aslap", tugas: "Takar ompreng 5 sekat per sekolah: (1) Jeruk -> (2) Nasi hangat 100g -> (3) Tumis Putren 30g tiris -> (4) Tahu 30g kesat -> (5) Ayam Rica/Kecap terakhir.", target: "13.710 wadah dalam krat per sekolah" }
    ],
    jadwalMundur: [
      { waktu: "T - 6 Jam", kegiatan: "Hitung & sortir jeruk. Timbang & cuci beras, masuk rice steamer. Potong ayam dadu, marinasi chiller. Uji goreng 20 dadu bersama Bu Ricky/Bu Linda (timbang matang 5 dadu harus +-60 g)." },
      { waktu: "T - 5 Jam", kegiatan: "Kupas dan iris putren, wortel, bawang. Potong tahu, rendam air garam bawang. Haluskan bumbu rica (PB) dan iris bumbu kecap manis (PK)." },
      { waktu: "T - 4 Jam", kegiatan: "Serahkan semua bahan mentah siap-olah ke Tim Pengolahan (Ayam ke Bu Ricky/Linda, Tahu ke Faiz, Sayur ke Abidin, Beras ke Rizal)." },
      { waktu: "T - 1 Jam", kegiatan: "Siapkan meja pemorsian per stasiun sekolah (SMK 1, MTs, Posyandu Ambokembang, Posyandu Panjomblangan, Sampel). Hitung stok wadah dan label alergi." },
      { waktu: "T - 45 Menit", kegiatan: "Mulai pemorsian urutan standar: (1) Jeruk, (2) Nasi hangat 100g, (3) Tumis Putren Wortel 30g tiris, (4) Tahu 30g kesat, (5) Ayam Rica/Kecap 5 dadu (60g) terakhir setelah uap turun." },
      { waktu: "T - 0", kegiatan: "Pemorsian selesai, hitung ulang per krat tiap sekolah, checklist serah terima, muat ke mobil armada masing-masing." }
    ],
    aturanEmas: [
      "Ayam dipotong dadu seragam +-2x2 cm (12-14 gram), tepat 5 dadu per porsi.",
      "Ayam PB = RICA (pedas sedang), ayam PK = KECAP (manis tidak pedas): wajib dua baskom terpisah dan dua label berbeda, JANGAN TERTUKAR.",
      "Tahu ditekan/dikeringkan perlahan dengan kain bersih sebelum digoreng supaya minyak panas tidak muncrat.",
      "Putren dan wortel dipotong seragam, simpan tiap jenis di wadah terpisah.",
      "Perhatian khusus 3 siswa alergi nasi (SMK 2 siswa, MTs 1 siswa): siapkan pengganti karbo non-nasi & label khusus 'ALERGI NASI'.",
      "Telenan dan pisau untuk bahan mentah (ayam) WAJIB dipisah dari sayuran dan makanan matang.",
      "Ragu dengan kesegaran atau mutu bahan: JANGAN DIPAKAI, segera lapor Chef Lutfi."
    ]
  },
  selasa: {
    title: "Selasa, 10 November 2026",
    menu: "Nasi + Ayam Katsu Sambal Geprek + Tahu Goreng + Mix Vegetable + Pisang",
    locations: [
      { id: "all", name: "Total Keseluruhan (5 Titik)", badge: "2.742 Porsi • 13.710 Wadah", pb: 2742, pk: 0, totalPorsi: 2742, totalWadah: 13710, driver: "Armada SPPG 1, 2, 3", jamBerangkat: "09:00 - 09:45 WIB", jamPemorsian: "07:30 - Selesai", alergiNotice: "Alergi nasi tetap diperhatikan untuk 3 siswa.", posyanduNotice: "Ayam katsu untuk balita disajikan TANPA sambal geprek.", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "274,20 kg", wadah: "2.742", note: "150 kg beras PO" },
        { name: "Ayam Katsu Geprek", perPorsi: "60 g", total: "164,52 kg", wadah: "2.742", note: "173 kg dada fillet PO" },
        { name: "Tahu Goreng", perPorsi: "30 g", total: "82,26 kg", wadah: "2.742", note: "2.772 pcs tahu PO" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "82,26 kg", wadah: "2.742", note: "70 kg mix vegetable PO" },
        { name: "Pisang Segar", perPorsi: "1 buah", total: "2.742 buah", wadah: "2.742", note: "2.762 pcs pisang PO" }
      ]},
      { id: "smk1", name: "SMK 1 Kedungwuni", badge: "1.712 Porsi PB • 8.560 Wadah", pb: 1712, pk: 0, totalPorsi: 1712, totalWadah: 8560, driver: "Armada 1", jamBerangkat: "09:30 WIB", jamPemorsian: "07:30 - 08:45 WIB", alergiNotice: "2 siswa alergi nasi: siapkan karbo pengganti berlabel.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "171,20 kg", wadah: "1.710", note: "+ 2 karbo non-nasi" },
        { name: "Ayam Katsu", perPorsi: "60 g", total: "102,72 kg", wadah: "1.712", note: "Katsu krispi geprek" },
        { name: "Tahu Goreng", perPorsi: "30 g", total: "51,36 kg", wadah: "1.712", note: "Tahu gurih" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "51,36 kg", wadah: "1.712", note: "Tumis mentega" },
        { name: "Pisang Segar", perPorsi: "1 buah", total: "1.712 buah", wadah: "1.712", note: "Pisang mulus" }
      ]},
      { id: "mts", name: "MTs Salafiyah Syafiiyah", badge: "646 Porsi PB • 3.230 Wadah", pb: 646, pk: 0, totalPorsi: 646, totalWadah: 3230, driver: "Armada 2", jamBerangkat: "09:45 WIB", jamPemorsian: "08:15 - 09:15 WIB", alergiNotice: "1 siswa alergi nasi: siapkan karbo pengganti berlabel.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "64,60 kg", wadah: "645", note: "+ 1 karbo non-nasi" },
        { name: "Ayam Katsu", perPorsi: "60 g", total: "38,76 kg", wadah: "646", note: "Katsu geprek" },
        { name: "Tahu Goreng", perPorsi: "30 g", total: "19,38 kg", wadah: "646", note: "Tahu gurih" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "19,38 kg", wadah: "646", note: "Tumis mentega" },
        { name: "Pisang Segar", perPorsi: "1 buah", total: "646 buah", wadah: "646", note: "Pisang mulus" }
      ]},
      { id: "posyandu_ambo", name: "Posyandu Ambokembang", badge: "185 Porsi • 925 Wadah", pb: 86, pk: 99, totalPorsi: 185, totalWadah: 925, driver: "Armada 3", jamBerangkat: "09:00 WIB", jamPemorsian: "07:30 - 08:30 WIB", alergiNotice: "99 porsi katsu balita TIDAK DIGEPREK SAMBAL.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "18,50 kg", wadah: "185", note: "Nasi hangat" },
        { name: "Ayam Katsu", perPorsi: "60 g", total: "11,10 kg", wadah: "185", note: "86 geprek + 99 non-pedas" },
        { name: "Tahu Goreng", perPorsi: "30 g", total: "5,55 kg", wadah: "185", note: "Tahu goreng" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "5,55 kg", wadah: "185", note: "Tumis sayur" },
        { name: "Pisang Segar", perPorsi: "1 buah", total: "185 buah", wadah: "185", note: "Pisang manis" }
      ]},
      { id: "posyandu_panjom", name: "Posyandu Panjomblangan", badge: "188 Porsi • 940 Wadah", pb: 95, pk: 93, totalPorsi: 188, totalWadah: 940, driver: "Armada 3", jamBerangkat: "09:15 WIB", jamPemorsian: "07:45 - 08:45 WIB", alergiNotice: "93 porsi katsu balita TIDAK DIGEPREK SAMBAL.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "18,80 kg", wadah: "188", note: "Nasi hangat" },
        { name: "Ayam Katsu", perPorsi: "60 g", total: "11,28 kg", wadah: "188", note: "95 geprek + 93 non-pedas" },
        { name: "Tahu Goreng", perPorsi: "30 g", total: "5,64 kg", wadah: "188", note: "Tahu goreng" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "5,64 kg", wadah: "188", note: "Tumis sayur" },
        { name: "Pisang Segar", perPorsi: "1 buah", total: "188 buah", wadah: "188", note: "Pisang manis" }
      ]},
      { id: "sampel", name: "Sampel & Uji Organoleptik", badge: "11 Porsi • 55 Wadah", pb: 11, pk: 0, totalPorsi: 11, totalWadah: 55, driver: "QC Lab Dapur", jamBerangkat: "Sebelum Distribusi", jamPemorsian: "07:00 WIB", alergiNotice: "2 sampel simpan + 9 uji organoleptik.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "1,10 kg", wadah: "11", note: "Sampel nasi" },
        { name: "Ayam Katsu", perPorsi: "60 g", total: "0,66 kg", wadah: "11", note: "Sampel katsu" },
        { name: "Tahu Goreng", perPorsi: "30 g", total: "0,33 kg", wadah: "11", note: "Sampel tahu" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "0,33 kg", wadah: "11", note: "Sampel sayur" },
        { name: "Pisang Segar", perPorsi: "1 buah", total: "11 buah", wadah: "11", note: "Sampel pisang" }
      ]}
    ],
    posKerja: [
      { pos: "Pos Nasi", picSerah: "Rizal (Pengolahan Umum)", tugas: "Timbang beras 150 kg, cuci bersih, masak pulen.", target: "274,2 kg matang" },
      { pos: "Pos Ayam Katsu", picSerah: "Bu Ricky & Bu Linda (ProHe)", tugas: "Pipihkan dada ayam, marinasi lada bawang putih, balur tepung panir.", target: "173 kg dada fillet" },
      { pos: "Pos Tahu", picSerah: "Faiz (ProNa)", tugas: "Potong tahu kotak, tiriskan, rendam air garam.", target: "2.772 pcs mentah" },
      { pos: "Pos Sayur", picSerah: "Abidin (Sayur)", tugas: "Siapkan mix vegetable jagung polong wortel bersih.", target: "70 kg sayur" },
      { pos: "Pos Buah", picSerah: "Tim Pemorsian", tugas: "Sortir pisang segar matang mulus higienis.", target: "2.762 pcs pisang" },
      { pos: "Pos Pemorsian", picSerah: "Driver & Aslap", tugas: "Takar ompreng: Pisang -> Nasi -> Mix Veggie -> Tahu -> Katsu Geprek.", target: "13.710 wadah" }
    ],
    jadwalMundur: [
      { waktu: "T - 6 Jam", kegiatan: "Sortir pisang. Timbang & cuci beras. Pipihkan fillet ayam katsu, marinasi chiller." },
      { waktu: "T - 5 Jam", kegiatan: "Balur panir ayam katsu. Potong tahu. Cuci mix vegetable." },
      { waktu: "T - 4 Jam", kegiatan: "Serahkan semua bahan ke Tim Pengolahan untuk digoreng & dimasak." },
      { waktu: "T - 1 Jam", kegiatan: "Siapkan meja stasiun pemorsian per sekolah." },
      { waktu: "T - 45 Menit", kegiatan: "Mulai pemorsian ompreng 5 item." },
      { waktu: "T - 0", kegiatan: "Selesai pemorsian, serah terima muat armada." }
    ],
    aturanEmas: [
      "Fillet ayam katsu ditipiskan seragam agar matang merata sampai ke inti.",
      "Suhu inti penggorengan katsu wajib minimal 75°C.",
      "Untuk balita Posyandu (192 porsi), katsu TIDAK DIGEPREK SAMBAL.",
      "Tahu digoreng hingga berkulit keemasan dan kesat.",
      "Mix vegetable ditumis cepat mentega gurih agar warna tetap cerah.",
      "Pisang disortir yang matang sempurna tanpa luka memar.",
      "Gunakan sarung tangan steril baru di setiap stasiun kerja."
    ]
  },
  rabu: {
    title: "Rabu, 11 November 2026",
    menu: "Nasi + Telur Fuyunghai + Saus Asam Manis + Tempe Goreng + Tumis Polong Wortel Kol + Anggur Muscat",
    locations: [
      { id: "all", name: "Total Keseluruhan (5 Titik)", badge: "2.742 Porsi • 13.710 Wadah", pb: 2742, pk: 0, totalPorsi: 2742, totalWadah: 13710, driver: "Armada SPPG 1, 2, 3", jamBerangkat: "09:00 - 09:45 WIB", jamPemorsian: "07:30 - Selesai", alergiNotice: "Alergi nasi 3 siswa disiapkan karbo non-nasi.", posyanduNotice: "Saus fuyunghai balita dipisah / tidak pedas.", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "274,20 kg", wadah: "2.742", note: "150 kg beras PO" },
        { name: "Telur Fuyunghai", perPorsi: "60 g", total: "164,52 kg", wadah: "2.742", note: "130 kg telur PO" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "82,26 kg", wadah: "2.742", note: "112 papan tempe PO" },
        { name: "Tumis Polong Wortel", perPorsi: "30 g", total: "82,26 kg", wadah: "2.742", note: "137 kg sayur PO" },
        { name: "Anggur Muscat", perPorsi: "50 g", total: "137,10 kg", wadah: "2.742", note: "171 kg anggur PO" }
      ]},
      { id: "smk1", name: "SMK 1 Kedungwuni", badge: "1.712 Porsi PB • 8.560 Wadah", pb: 1712, pk: 0, totalPorsi: 1712, totalWadah: 8560, driver: "Armada 1", jamBerangkat: "09:30 WIB", jamPemorsian: "07:30 - 08:45 WIB", alergiNotice: "2 siswa alergi nasi.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "171,20 kg", wadah: "1.710", note: "+ 2 karbo non-nasi" },
        { name: "Telur Fuyunghai", perPorsi: "60 g", total: "102,72 kg", wadah: "1.712", note: "Fuyunghai tebal" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "51,36 kg", wadah: "1.712", note: "Tempe renyah" },
        { name: "Tumis Polong Wortel", perPorsi: "30 g", total: "51,36 kg", wadah: "1.712", note: "Sayuran tiris" },
        { name: "Anggur Muscat", perPorsi: "50 g", total: "85,60 kg", wadah: "1.712", note: "Anggur segar" }
      ]},
      { id: "mts", name: "MTs Salafiyah Syafiiyah", badge: "646 Porsi PB • 3.230 Wadah", pb: 646, pk: 0, totalPorsi: 646, totalWadah: 3230, driver: "Armada 2", jamBerangkat: "09:45 WIB", jamPemorsian: "08:15 - 09:15 WIB", alergiNotice: "1 siswa alergi nasi.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "64,60 kg", wadah: "645", note: "+ 1 karbo non-nasi" },
        { name: "Telur Fuyunghai", perPorsi: "60 g", total: "38,76 kg", wadah: "646", note: "Fuyunghai tebal" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "19,38 kg", wadah: "646", note: "Tempe renyah" },
        { name: "Tumis Polong Wortel", perPorsi: "30 g", total: "19,38 kg", wadah: "646", note: "Sayuran tiris" },
        { name: "Anggur Muscat", perPorsi: "50 g", total: "32,30 kg", wadah: "646", note: "Anggur segar" }
      ]},
      { id: "posyandu_ambo", name: "Posyandu Ambokembang", badge: "185 Porsi • 925 Wadah", pb: 86, pk: 99, totalPorsi: 185, totalWadah: 925, driver: "Armada 3", jamBerangkat: "09:00 WIB", jamPemorsian: "07:30 - 08:30 WIB", alergiNotice: "Saus fuyunghai balita rasa manis gurih ramah anak.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "18,50 kg", wadah: "185", note: "Nasi pulen" },
        { name: "Telur Fuyunghai", perPorsi: "60 g", total: "11,10 kg", wadah: "185", note: "Fuyunghai saus" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "5,55 kg", wadah: "185", note: "Tempe renyah" },
        { name: "Tumis Polong Wortel", perPorsi: "30 g", total: "5,55 kg", wadah: "185", note: "Sayuran empuk" },
        { name: "Anggur Muscat", perPorsi: "50 g", total: "9,25 kg", wadah: "185", note: "Anggur dicuci bersih" }
      ]},
      { id: "posyandu_panjom", name: "Posyandu Panjomblangan", badge: "188 Porsi • 940 Wadah", pb: 95, pk: 93, totalPorsi: 188, totalWadah: 940, driver: "Armada 3", jamBerangkat: "09:15 WIB", jamPemorsian: "07:45 - 08:45 WIB", alergiNotice: "Saus fuyunghai balita rasa manis gurih.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "18,80 kg", wadah: "188", note: "Nasi pulen" },
        { name: "Telur Fuyunghai", perPorsi: "60 g", total: "11,28 kg", wadah: "188", note: "Fuyunghai saus" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "5,64 kg", wadah: "188", note: "Tempe renyah" },
        { name: "Tumis Polong Wortel", perPorsi: "30 g", total: "5,64 kg", wadah: "188", note: "Sayuran empuk" },
        { name: "Anggur Muscat", perPorsi: "50 g", total: "9,40 kg", wadah: "188", note: "Anggur dicuci bersih" }
      ]},
      { id: "sampel", name: "Sampel & Uji Organoleptik", badge: "11 Porsi • 55 Wadah", pb: 11, pk: 0, totalPorsi: 11, totalWadah: 55, driver: "QC Lab Dapur", jamBerangkat: "Sebelum Distribusi", jamPemorsian: "07:00 WIB", alergiNotice: "2 sampel simpan + 9 uji organoleptik.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "1,10 kg", wadah: "11", note: "Sampel nasi" },
        { name: "Telur Fuyunghai", perPorsi: "60 g", total: "0,66 kg", wadah: "11", note: "Sampel fuyunghai" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "0,33 kg", wadah: "11", note: "Sampel tempe" },
        { name: "Tumis Polong Wortel", perPorsi: "30 g", total: "0,33 kg", wadah: "11", note: "Sampel sayur" },
        { name: "Anggur Muscat", perPorsi: "50 g", total: "0,55 kg", wadah: "11", note: "Sampel anggur" }
      ]}
    ],
    posKerja: [
      { pos: "Pos Nasi", picSerah: "Rizal (Pengolahan Umum)", tugas: "Timbang beras 150 kg, cuci bersih, masak pulen.", target: "274,2 kg matang" },
      { pos: "Pos Fuyunghai", picSerah: "Bu Ricky & Bu Linda (ProHe)", tugas: "Kocok telur 130 kg + cincangan sayur wortel kol, racik saus asam manis.", target: "130 kg telur mentah" },
      { pos: "Pos Tempe", picSerah: "Faiz (ProNa)", tugas: "Potong tempe 112 papan, rendam air garam bawang.", target: "112 papan tempe" },
      { pos: "Pos Sayur", picSerah: "Abidin (Sayur)", tugas: "Iris wortel koin, kol tipis, cuci kacang polong frozen.", target: "137 kg sayur" },
      { pos: "Pos Buah", picSerah: "Tim Pemorsian", tugas: "Cuci anggur muscat air mengalir dingin, tiriskan.", target: "171 kg anggur" },
      { pos: "Pos Pemorsian", picSerah: "Driver & Aslap", tugas: "Takar: Anggur -> Nasi -> Tumis -> Tempe -> Fuyunghai + saus.", target: "13.710 wadah" }
    ],
    jadwalMundur: [
      { waktu: "T - 6 Jam", kegiatan: "Cuci anggur muscat tiriskan. Timbang cuci beras. Cincang sayuran adonan fuyunghai." },
      { waktu: "T - 5 Jam", kegiatan: "Kocok telur fuyunghai. Potong tempe marinasi. Racik saus asam manis." },
      { waktu: "T - 4 Jam", kegiatan: "Goreng dadar fuyunghai tebal keemasan, goreng tempe, masak saus." },
      { waktu: "T - 1 Jam", kegiatan: "Siapkan meja stasiun pemorsian per sekolah." },
      { waktu: "T - 45 Menit", kegiatan: "Mulai pemorsian ompreng 5 item." },
      { waktu: "T - 0", kegiatan: "Selesai pemorsian, serah terima muat armada." }
    ],
    aturanEmas: [
      "Adonan telur fuyunghai dikocok merata dengan cincangan halus wortel & kol.",
      "Goreng fuyunghai dengan api sedang agar bagian dalam matang sempurna tidak lembek.",
      "Saus asam manis dimasak hingga mengental berkilap dan tidak encer berair.",
      "Tempe dipotong seragam dan digoreng garing renyah.",
      "Anggur muscat dicuci bersih dengan air mengalir dingin dan ditiriskan sampai kering.",
      "Wadah buah harus benar-benar kering sebelum anggur dimasukkan."
    ]
  },
  kamis: {
    title: "Kamis, 12 November 2026",
    menu: "Nasi + Ikan Lele Crispy + Sambal Bawang + Edamame Rebus + Kakiage Sayur + Kelengkeng",
    locations: [
      { id: "all", name: "Total Keseluruhan (5 Titik)", badge: "2.742 Porsi • 13.710 Wadah", pb: 2742, pk: 0, totalPorsi: 2742, totalWadah: 13710, driver: "Armada SPPG 1, 2, 3", jamBerangkat: "09:00 - 09:45 WIB", jamPemorsian: "07:30 - Selesai", alergiNotice: "Alergi nasi 3 siswa tetap dipantau.", posyanduNotice: "Lele balita dipastikan bebas duri tajam dan sambal dipisah.", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "274,20 kg", wadah: "2.742", note: "150 kg beras PO" },
        { name: "Ikan Lele Crispy", perPorsi: "1 ekor", total: "278,00 kg", wadah: "2.742", note: "Lele isi 10/kg PO" },
        { name: "Edamame Rebus", perPorsi: "30 g", total: "82,26 kg", wadah: "2.742", note: "60 kg edamame PO" },
        { name: "Kakiage Sayur", perPorsi: "1 pcs (30 g)", total: "82,26 kg", wadah: "2.742", note: "85 kg sayur PO" },
        { name: "Kelengkeng Manis", perPorsi: "40 g", total: "109,68 kg", wadah: "2.742", note: "120 kg kelengkeng PO" }
      ]},
      { id: "smk1", name: "SMK 1 Kedungwuni", badge: "1.712 Porsi PB • 8.560 Wadah", pb: 1712, pk: 0, totalPorsi: 1712, totalWadah: 8560, driver: "Armada 1", jamBerangkat: "09:30 WIB", jamPemorsian: "07:30 - 08:45 WIB", alergiNotice: "2 siswa alergi nasi.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "171,20 kg", wadah: "1.710", note: "+ 2 karbo non-nasi" },
        { name: "Ikan Lele Crispy", perPorsi: "1 ekor", total: "171,20 kg", wadah: "1.712", note: "1.712 ekor lele garing" },
        { name: "Edamame Rebus", perPorsi: "30 g", total: "51,36 kg", wadah: "1.712", note: "Edamame rebus" },
        { name: "Kakiage Sayur", perPorsi: "1 pcs", total: "51,36 kg", wadah: "1.712", note: "Kakiage krispi" },
        { name: "Kelengkeng Manis", perPorsi: "40 g", total: "68,48 kg", wadah: "1.712", note: "Kelengkeng manis" }
      ]},
      { id: "mts", name: "MTs Salafiyah Syafiiyah", badge: "646 Porsi PB • 3.230 Wadah", pb: 646, pk: 0, totalPorsi: 646, totalWadah: 3230, driver: "Armada 2", jamBerangkat: "09:45 WIB", jamPemorsian: "08:15 - 09:15 WIB", alergiNotice: "1 siswa alergi nasi.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "64,60 kg", wadah: "645", note: "+ 1 karbo non-nasi" },
        { name: "Ikan Lele Crispy", perPorsi: "1 ekor", total: "64,60 kg", wadah: "646", note: "646 ekor lele garing" },
        { name: "Edamame Rebus", perPorsi: "30 g", total: "19,38 kg", wadah: "646", note: "Edamame rebus" },
        { name: "Kakiage Sayur", perPorsi: "1 pcs", total: "19,38 kg", wadah: "646", note: "Kakiage krispi" },
        { name: "Kelengkeng Manis", perPorsi: "40 g", total: "25,84 kg", wadah: "646", note: "Kelengkeng manis" }
      ]},
      { id: "posyandu_ambo", name: "Posyandu Ambokembang", badge: "185 Porsi • 925 Wadah", pb: 86, pk: 99, totalPorsi: 185, totalWadah: 925, driver: "Armada 3", jamBerangkat: "09:00 WIB", jamPemorsian: "07:30 - 08:30 WIB", alergiNotice: "Lele balita dipisahkan sambal.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "18,50 kg", wadah: "185", note: "Nasi pulen" },
        { name: "Ikan Lele Crispy", perPorsi: "1 ekor", total: "18,50 kg", wadah: "185", note: "185 ekor lele" },
        { name: "Edamame Rebus", perPorsi: "30 g", total: "5,55 kg", wadah: "185", note: "Edamame gurih" },
        { name: "Kakiage Sayur", perPorsi: "1 pcs", total: "5,55 kg", wadah: "185", note: "Kakiage krispi" },
        { name: "Kelengkeng Manis", perPorsi: "40 g", total: "7,40 kg", wadah: "185", note: "Kelengkeng manis" }
      ]},
      { id: "posyandu_panjom", name: "Posyandu Panjomblangan", badge: "188 Porsi • 940 Wadah", pb: 95, pk: 93, totalPorsi: 188, totalWadah: 940, driver: "Armada 3", jamBerangkat: "09:15 WIB", jamPemorsian: "07:45 - 08:45 WIB", alergiNotice: "Lele balita dipisahkan sambal.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "18,80 kg", wadah: "188", note: "Nasi pulen" },
        { name: "Ikan Lele Crispy", perPorsi: "1 ekor", total: "18,80 kg", wadah: "188", note: "188 ekor lele" },
        { name: "Edamame Rebus", perPorsi: "30 g", total: "5,64 kg", wadah: "188", note: "Edamame gurih" },
        { name: "Kakiage Sayur", perPorsi: "1 pcs", total: "5,64 kg", wadah: "188", note: "Kakiage krispi" },
        { name: "Kelengkeng Manis", perPorsi: "40 g", total: "7,52 kg", wadah: "188", note: "Kelengkeng manis" }
      ]},
      { id: "sampel", name: "Sampel & Uji Organoleptik", badge: "11 Porsi • 55 Wadah", pb: 11, pk: 0, totalPorsi: 11, totalWadah: 55, driver: "QC Lab Dapur", jamBerangkat: "Sebelum Distribusi", jamPemorsian: "07:00 WIB", alergiNotice: "2 sampel simpan + 9 uji organoleptik.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "1,10 kg", wadah: "11", note: "Sampel nasi" },
        { name: "Ikan Lele Crispy", perPorsi: "1 ekor", total: "1,10 kg", wadah: "11", note: "11 ekor lele" },
        { name: "Edamame Rebus", perPorsi: "30 g", total: "0,33 kg", wadah: "11", note: "Sampel edamame" },
        { name: "Kakiage Sayur", perPorsi: "1 pcs", total: "0,33 kg", wadah: "11", note: "Sampel kakiage" },
        { name: "Kelengkeng Manis", perPorsi: "40 g", total: "0,44 kg", wadah: "11", note: "Sampel kelengkeng" }
      ]}
    ],
    posKerja: [
      { pos: "Pos Nasi", picSerah: "Rizal (Pengolahan Umum)", tugas: "Timbang beras 150 kg, cuci bersih, masak pulen.", target: "274,2 kg matang" },
      { pos: "Pos Lele", picSerah: "Bu Ricky & Bu Linda (ProHe)", tugas: "Bersihkan perut lele 278 kg, kerat badan, marinasi bumbu kunyit, balur tepung renyah.", target: "278 kg lele utuh" },
      { pos: "Pos Edamame", picSerah: "Faiz (ProNa)", tugas: "Sortir polong edamame 60 kg, rebus air garam 5 menit.", target: "60 kg edamame" },
      { pos: "Pos Kakiage", picSerah: "Abidin (Sayur)", tugas: "Iris wortel & kol korek api halus, campur adonan tepung encer es.", target: "85 kg sayur" },
      { pos: "Pos Buah", picSerah: "Tim Pemorsian", tugas: "Sortir kelengkeng manis segar utuh.", target: "120 kg kelengkeng" },
      { pos: "Pos Pemorsian", picSerah: "Driver & Aslap", tugas: "Takar: Kelengkeng -> Nasi -> Kakiage -> Edamame -> Lele Crispy + Sambal.", target: "13.710 wadah" }
    ],
    jadwalMundur: [
      { waktu: "T - 6 Jam", kegiatan: "Sortir kelengkeng. Timbang & cuci beras. Siangi dan kerat lele, marinasi chiller." },
      { waktu: "T - 5 Jam", kegiatan: "Iris sayuran kakiage. Rebus edamame air garam. Siapkan adonan tepung lele." },
      { waktu: "T - 4 Jam", kegiatan: "Goreng lele crispy deep fry garing keemasan, goreng kakiage krispi." },
      { waktu: "T - 1 Jam", kegiatan: "Siapkan meja stasiun pemorsian per sekolah." },
      { waktu: "T - 45 Menit", kegiatan: "Mulai pemorsian ompreng 5 item." },
      { waktu: "T - 0", kegiatan: "Selesai pemorsian, serah terima muat armada." }
    ],
    aturanEmas: [
      "Ikan lele dibersihkan hingga kesat dari lendir dan isi perut dibuang bersih.",
      "Goreng lele deep fry hingga benar-benar kering dan garing renyah.",
      "Kakiage digoreng dengan minyak panas tiris sempurna agar tidak menyerap minyak berlebih.",
      "Edamame direbus dengan garam ringan tepat 5-6 menit agar polong tetap hijau segar.",
      "Kelengkeng disortir buah utuh manis bebas dari tangkai busuk."
    ]
  },
  jumat: {
    title: "Jumat, 13 November 2026",
    menu: "Nasi + Ayam Crispy Sambal Bajak + Tempe Goreng + Mix Vegetable + Anggur Red Globe",
    locations: [
      { id: "all", name: "Total Keseluruhan (Jumat)", badge: "2.094 Porsi • 10.470 Wadah", pb: 2094, pk: 0, totalPorsi: 2094, totalWadah: 10470, driver: "Armada SPPG 1, 2, 3", jamBerangkat: "09:00 - 09:45 WIB", jamPemorsian: "07:30 - Selesai", alergiNotice: "Alergi nasi tetap dipantau untuk siswa terdaftar.", posyanduNotice: "Ayam crispy balita disajikan TANPA sambal bajak.", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "209,40 kg", wadah: "2.094", note: "103 kg beras PO" },
        { name: "Ayam Crispy Sambal Bajak", perPorsi: "60 g", total: "125,64 kg", wadah: "2.094", note: "132 kg dada fillet PO" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "62,82 kg", wadah: "2.094", note: "85 papan tempe PO" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "62,82 kg", wadah: "2.094", note: "60 kg mix vegetable PO" },
        { name: "Anggur Red Globe", perPorsi: "45 g", total: "94,23 kg", wadah: "2.094", note: "97 kg anggur PO" }
      ]},
      { id: "smk1", name: "SMK 1 Kedungwuni", badge: "1.300 Porsi PB • 6.500 Wadah", pb: 1300, pk: 0, totalPorsi: 1300, totalWadah: 6500, driver: "Armada 1", jamBerangkat: "09:30 WIB", jamPemorsian: "07:30 - 08:45 WIB", alergiNotice: "2 siswa alergi nasi.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "130,00 kg", wadah: "1.298", note: "+ 2 karbo non-nasi" },
        { name: "Ayam Crispy", perPorsi: "60 g", total: "78,00 kg", wadah: "1.300", note: "Ayam sambal bajak" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "39,00 kg", wadah: "1.300", note: "Tempe gurih" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "39,00 kg", wadah: "1.300", note: "Tumis sayur" },
        { name: "Anggur Red Globe", perPorsi: "45 g", total: "58,50 kg", wadah: "1.300", note: "Anggur merah" }
      ]},
      { id: "mts", name: "MTs Salafiyah Syafiiyah", badge: "494 Porsi PB • 2.470 Wadah", pb: 494, pk: 0, totalPorsi: 494, totalWadah: 2470, driver: "Armada 2", jamBerangkat: "09:45 WIB", jamPemorsian: "08:15 - 09:15 WIB", alergiNotice: "1 siswa alergi nasi.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "49,40 kg", wadah: "493", note: "+ 1 karbo non-nasi" },
        { name: "Ayam Crispy", perPorsi: "60 g", total: "29,64 kg", wadah: "494", note: "Ayam sambal bajak" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "14,82 kg", wadah: "494", note: "Tempe gurih" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "14,82 kg", wadah: "494", note: "Tumis sayur" },
        { name: "Anggur Red Globe", perPorsi: "45 g", total: "22,23 kg", wadah: "494", note: "Anggur merah" }
      ]},
      { id: "posyandu_ambo", name: "Posyandu Ambokembang", badge: "145 Porsi • 725 Wadah", pb: 70, pk: 75, totalPorsi: 145, totalWadah: 725, driver: "Armada 3", jamBerangkat: "09:00 WIB", jamPemorsian: "07:30 - 08:30 WIB", alergiNotice: "Ayam crispy balita disajikan tanpa sambal pedas.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "14,50 kg", wadah: "145", note: "Nasi hangat" },
        { name: "Ayam Crispy", perPorsi: "60 g", total: "8,70 kg", wadah: "145", note: "70 bajak + 75 polos" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "4,35 kg", wadah: "145", note: "Tempe gurih" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "4,35 kg", wadah: "145", note: "Tumis sayur" },
        { name: "Anggur Red Globe", perPorsi: "45 g", total: "6,52 kg", wadah: "145", note: "Anggur merah" }
      ]},
      { id: "posyandu_panjom", name: "Posyandu Panjomblangan", badge: "144 Porsi • 720 Wadah", pb: 70, pk: 74, totalPorsi: 144, totalWadah: 720, driver: "Armada 3", jamBerangkat: "09:15 WIB", jamPemorsian: "07:45 - 08:45 WIB", alergiNotice: "Ayam crispy balita disajikan tanpa sambal pedas.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "14,40 kg", wadah: "144", note: "Nasi hangat" },
        { name: "Ayam Crispy", perPorsi: "60 g", total: "8,64 kg", wadah: "144", note: "70 bajak + 74 polos" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "4,32 kg", wadah: "144", note: "Tempe gurih" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "4,32 kg", wadah: "144", note: "Tumis sayur" },
        { name: "Anggur Red Globe", perPorsi: "45 g", total: "6,48 kg", wadah: "144", note: "Anggur merah" }
      ]},
      { id: "sampel", name: "Sampel & Uji Organoleptik", badge: "11 Porsi • 55 Wadah", pb: 11, pk: 0, totalPorsi: 11, totalWadah: 55, driver: "QC Lab Dapur", jamBerangkat: "Sebelum Distribusi", jamPemorsian: "07:00 WIB", alergiNotice: "2 sampel simpan + 9 uji organoleptik.", posyanduNotice: "", items: [
        { name: "Nasi Putih", perPorsi: "100 g", total: "1,10 kg", wadah: "11", note: "Sampel nasi" },
        { name: "Ayam Crispy", perPorsi: "60 g", total: "0,66 kg", wadah: "11", note: "Sampel ayam" },
        { name: "Tempe Goreng", perPorsi: "30 g", total: "0,33 kg", wadah: "11", note: "Sampel tempe" },
        { name: "Mix Vegetable", perPorsi: "30 g", total: "0,33 kg", wadah: "11", note: "Sampel sayur" },
        { name: "Anggur Red Globe", perPorsi: "45 g", total: "0,50 kg", wadah: "11", note: "Sampel anggur" }
      ]}
    ],
    posKerja: [
      { pos: "Pos Nasi", picSerah: "Rizal (Pengolahan Umum)", tugas: "Timbang beras 103 kg, cuci bersih, masak pulen.", target: "209,4 kg matang" },
      { pos: "Pos Ayam Crispy", picSerah: "Bu Ricky & Bu Linda (ProHe)", tugas: "Potong dada fillet 132 kg, marinasi, balur tepung keriting renyah.", target: "132 kg dada fillet" },
      { pos: "Pos Tempe", picSerah: "Faiz (ProNa)", tugas: "Potong tempe 85 papan seragam, rendam air garam bawang.", target: "85 papan tempe" },
      { pos: "Pos Sayur", picSerah: "Abidin (Sayur)", tugas: "Siapkan mix vegetable jagung polong wortel segar.", target: "60 kg sayur" },
      { pos: "Pos Buah", picSerah: "Tim Pemorsian", tugas: "Cuci anggur red globe air mengalir dingin, tiriskan.", target: "97 kg anggur" },
      { pos: "Pos Pemorsian", picSerah: "Driver & Aslap", tugas: "Takar: Anggur -> Nasi -> Tumis -> Tempe -> Ayam Crispy Sambal Bajak.", target: "10.470 wadah" }
    ],
    jadwalMundur: [
      { waktu: "T - 6 Jam", kegiatan: "Cuci anggur red globe. Timbang cuci beras. Potong dada ayam marinasi chiller." },
      { waktu: "T - 5 Jam", kegiatan: "Balur tepung krispi ayam. Potong tempe marinasi. Tumis sambal bajak tanak." },
      { waktu: "T - 4 Jam", kegiatan: "Goreng ayam krispi suhu 165°C, goreng tempe, tumis sayur." },
      { waktu: "T - 1 Jam", kegiatan: "Siapkan stasiun pemorsian per sekolah." },
      { waktu: "T - 45 Menit", kegiatan: "Mulai pemorsian ompreng 5 item." },
      { waktu: "T - 0", kegiatan: "Selesai pemorsian, serah terima muat armada." }
    ],
    aturanEmas: [
      "Ayam digoreng dengan tepung keriting renyah suhu minyak 165°C hingga matang sempurna (suhu inti >= 75°C).",
      "Sambal bajak ditumis hingga tanak berminyak dan matang sempurna.",
      "Untuk balita Posyandu (149 porsi), ayam crispy disajikan TANPA SAMBAL.",
      "Tempe digoreng kuning keemasan dan kesat.",
      "Anggur red globe dicuci air mengalir dingin dan ditiriskan sampai kering."
    ]
  }
};

let currentBatchLocation = 'all';
let currentDirectiveSubtab = 'aturan';

function selectBatchLocation(locId) {
  currentBatchLocation = locId;
  renderSchoolBatchSection();
}

function selectDirectiveSubtab(tabId) {
  currentDirectiveSubtab = tabId;
  updateStickyNoteContent();
}

function renderSchoolBatchSection() {
  const container = document.getElementById('school-batch-section');
  if (!container) return;

  const dayData = schoolBatchesData[currentDay] || schoolBatchesData['senin'];
  if (!dayData || !dayData.locations) {
    container.innerHTML = '<p class="text-xs text-slate-500">Data batch lokasi tidak tersedia.</p>';
    return;
  }

  // Find active location or default to first
  let activeLoc = dayData.locations.find(l => l.id === currentBatchLocation);
  if (!activeLoc) {
    activeLoc = dayData.locations[0];
    currentBatchLocation = activeLoc.id;
  }

  // 1. Build Location Chips
  let tabsHtml = '<div class="flex items-center gap-1.5 overflow-x-auto pb-1 custom-scrollbar no-print">';
  dayData.locations.forEach(loc => {
    const isActive = loc.id === currentBatchLocation;
    const btnCls = isActive
      ? 'bg-slate-900 text-white font-extrabold shadow-sm border border-slate-900'
      : 'bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold border border-slate-200';
    tabsHtml += '<button type="button" onclick="selectBatchLocation(\\'' + loc.id + '\\')" class="whitespace-nowrap px-3 py-1.5 rounded-xl text-xs flex items-center gap-1.5 cursor-pointer transition-all ' + btnCls + '">' +
      '<span>' + loc.name + '</span>' +
      '<span class="text-[10px] opacity-80 font-mono-num font-bold">(' + loc.totalPorsi + ')</span>' +
    '</button>';
  });
  tabsHtml += '</div>';

  // 2. Build Active Location Card
  let activeCardHtml = '<div class="bg-slate-50 border border-slate-200 rounded-xl p-3.5 space-y-3">';
  
  // Header Info
  activeCardHtml += '<div class="flex flex-wrap items-start justify-between gap-2 border-b border-slate-200/80 pb-2.5">' +
    '<div>' +
      '<div class="flex items-center gap-2">' +
        '<h3 class="text-xs font-black text-slate-900 uppercase tracking-wide">' + activeLoc.name + '</h3>' +
        '<span class="text-[10px] font-extrabold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full border border-emerald-200">' + activeLoc.badge + '</span>' +
      '</div>' +
      '<p class="text-[11px] text-slate-600 mt-0.5">Jam Berangkat: <span class="font-bold text-slate-800">' + activeLoc.jamBerangkat + '</span> • Driver: <span class="font-bold text-slate-800">' + activeLoc.driver + '</span></p>' +
    '</div>' +
    '<button type="button" onclick="openSchoolPrintModal(\\'' + activeLoc.id + '\\')" class="px-2.5 py-1.5 bg-slate-900 hover:bg-black text-white text-[11px] font-extrabold rounded-lg shadow-sm flex items-center gap-1.5 cursor-pointer no-print">' +
      '<svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>' +
      '<span>Cetak Lembar Kerja A4</span>' +
    '</button>' +
  '</div>';

  // Notices (Alergi / Posyandu)
  if (activeLoc.alergiNotice) {
    activeCardHtml += '<div class="p-2.5 bg-amber-50 border border-amber-300 rounded-lg text-amber-950 text-xs font-medium flex items-start gap-2">' +
      '<span class="text-sm">⚠️</span>' +
      '<div class="flex-1">' +
        '<span class="font-bold text-[11px] uppercase tracking-wide block text-amber-900">Catatan Khusus Alergi:</span>' +
        '<p class="text-[11px] mt-0.5">' + activeLoc.alergiNotice + '</p>' +
      '</div>' +
    '</div>';
  }

  if (activeLoc.posyanduNotice && activeLoc.posyanduNotice !== activeLoc.alergiNotice) {
    activeCardHtml += '<div class="p-2.5 bg-blue-50 border border-blue-200 rounded-lg text-blue-950 text-xs font-medium flex items-start gap-2">' +
      '<span class="text-sm">ℹ️</span>' +
      '<div class="flex-1">' +
        '<span class="font-bold text-[11px] uppercase tracking-wide block text-blue-900">Alokasi Varian Menu:</span>' +
        '<p class="text-[11px] mt-0.5">' + activeLoc.posyanduNotice + '</p>' +
      '</div>' +
    '</div>';
  }

  // Items Table
  activeCardHtml += '<div class="overflow-x-auto"><table class="w-full text-left text-xs border-collapse">' +
    '<thead>' +
      '<tr class="border-b border-slate-200 text-[10px] text-slate-500 font-extrabold uppercase bg-white">' +
        '<th class="p-2">Item Olahan</th>' +
        '<th class="p-2 text-center">Gramasi/Porsi</th>' +
        '<th class="p-2 text-center">Total Kebutuhan</th>' +
        '<th class="p-2 text-center">Target Wadah</th>' +
        '<th class="p-2">Catatan Khusus</th>' +
      '</tr>' +
    '</thead>' +
    '<tbody class="divide-y divide-slate-100 bg-white">';

  activeLoc.items.forEach(it => {
    activeCardHtml += '<tr class="hover:bg-slate-50 transition-colors">' +
      '<td class="p-2 font-bold text-slate-900">' + it.name + '</td>' +
      '<td class="p-2 text-center font-mono-num font-semibold text-slate-700">' + it.perPorsi + '</td>' +
      '<td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">' + it.total + '</td>' +
      '<td class="p-2 text-center font-mono-num font-bold text-slate-700">' + it.wadah + '</td>' +
      '<td class="p-2 text-[11px] text-slate-600">' + it.note + '</td>' +
    '</tr>';
  });

  activeCardHtml += '</tbody></table></div>';
  activeCardHtml += '</div>';

  container.innerHTML = '<div class="flex items-center justify-between">' +
    '<div>' +
      '<div class="flex items-center gap-1.5">' +
        '<span class="w-2.5 h-2.5 rounded-full bg-emerald-600"></span>' +
        '<h2 class="text-xs font-black text-slate-900 uppercase tracking-wide">DISTRIBUSI BATCH TIAP SEKOLAH & LOKASI</h2>' +
      '</div>' +
      '<p class="text-[10px] text-slate-500 font-medium">Klik lokasi sekolah di bawah untuk melihat rincian gramasi matang, jumlah wadah, dan cetak lembar kerja</p>' +
    '</div>' +
    '<span class="text-[10px] bg-slate-100 text-slate-700 font-mono-num font-bold px-2 py-0.5 rounded-md">' + dayData.locations.length + ' Titik</span>' +
  '</div>' +
  tabsHtml +
  activeCardHtml;
}

function openSchoolPrintModal(locId) {
  const dayData = schoolBatchesData[currentDay] || schoolBatchesData['senin'];
  if (!dayData) return;

  const loc = dayData.locations.find(l => l.id === locId) || dayData.locations[0];
  const modalPreview = document.getElementById('modal-school-preview');
  const printContainer = document.getElementById('printable-school-form');
  if (!modalPreview || !printContainer) return;

  let table1Rows = '';
  loc.items.forEach((it, idx) => {
    table1Rows += '<tr class="border-b border-slate-200">' +
      '<td class="p-2 text-center font-bold">Wadah ' + (idx + 1) + '</td>' +
      '<td class="p-2 font-bold">' + it.name + '</td>' +
      '<td class="p-2 text-slate-700">' + it.perPorsi + ' matang</td>' +
      '<td class="p-2 text-center font-mono-num font-bold">' + it.wadah + '</td>' +
    '</tr>';
  });

  let table2Rows = '';
  loc.items.forEach(it => {
    table2Rows += '<tr class="border-b border-slate-200">' +
      '<td class="p-2 font-bold">' + it.name + '</td>' +
      '<td class="p-2 text-center font-mono-num">' + it.perPorsi + '</td>' +
      '<td class="p-2 text-center font-mono-num font-bold text-emerald-900">' + it.total + '</td>' +
      '<td class="p-2 text-[11px] text-slate-600">' + it.note + '</td>' +
    '</tr>';
  });

  let table3Rows = '';
  loc.items.forEach(it => {
    table3Rows += '<tr class="border-b border-slate-200">' +
      '<td class="p-2 font-bold">' + it.name + '</td>' +
      '<td class="p-2 text-center font-mono-num font-bold">' + it.wadah + '</td>' +
      '<td class="p-2 text-center font-mono-num text-slate-400">................</td>' +
      '<td class="p-2 text-center text-slate-400">[ &nbsp; ] Sesuai</td>' +
    '</tr>';
  });

  const printHtml = '<div class="p-6 bg-white text-slate-900 font-sans text-xs space-y-4 max-w-2xl mx-auto border border-slate-300">' +
    '<div class="border-b-2 border-slate-900 pb-2 flex items-center justify-between">' +
      '<div>' +
        '<p class="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Badan Gizi Nasional Republik Indonesia</p>' +
        '<h2 class="text-sm font-black uppercase text-slate-900">SPPG PEKAJANGAN 04 - Program Makan Bergizi Gratis (MBG)</h2>' +
        '<h3 class="text-xs font-bold text-emerald-800">Lembar Kerja Tim Persiapan - ' + loc.name + '</h3>' +
      '</div>' +
      '<div class="text-right text-[10px] text-slate-500">' +
        '<p class="font-bold text-slate-800">' + dayData.title + '</p>' +
        '<p>Menu: ' + dayData.menu + '</p>' +
      '</div>' +
    '</div>' +

    '<div class="grid grid-cols-2 gap-2 p-2.5 bg-slate-50 border border-slate-200 rounded-lg text-[11px]">' +
      '<div>' +
        '<p><span class="font-bold">Lokasi:</span> ' + loc.name + '</p>' +
        '<p><span class="font-bold">Jumlah Porsi:</span> ' + loc.totalPorsi + ' porsi (' + (loc.pb > 0 ? loc.pb + ' PB' : '') + (loc.pk > 0 ? ' + ' + loc.pk + ' PK' : '') + ')</p>' +
        '<p><span class="font-bold">Jumlah Wadah:</span> 5 wadah per porsi = ' + loc.totalWadah + ' wadah</p>' +
      '</div>' +
      '<div>' +
        '<p><span class="font-bold">Jam Berangkat:</span> ' + loc.jamBerangkat + '</p>' +
        '<p><span class="font-bold">Jam Mulai Pemorsian:</span> ' + loc.jamPemorsian + '</p>' +
        '<p><span class="font-bold">Driver / Armada:</span> ' + loc.driver + '</p>' +
      '</div>' +
    '</div>' +

    (loc.alergiNotice ? '<div class="p-2 bg-amber-50 border border-amber-300 rounded text-amber-950 text-[11px]"><strong>CATATAN KHUSUS ALERGI:</strong> ' + loc.alergiNotice + '</div>' : '') +

    '<div>' +
      '<h4 class="font-extrabold text-slate-900 mb-1">1. Isi Tiap Wadah (Gramasi Matang)</h4>' +
      '<table class="w-full border-collapse border border-slate-300 text-[11px]">' +
        '<thead class="bg-slate-100">' +
          '<tr>' +
            '<th class="border border-slate-300 p-1.5 text-center">Wadah</th>' +
            '<th class="border border-slate-300 p-1.5 text-left">Item Komponen</th>' +
            '<th class="border border-slate-300 p-1.5 text-left">Standar Isi Satu Wadah</th>' +
            '<th class="border border-slate-300 p-1.5 text-center">Jumlah Wadah</th>' +
          '</tr>' +
        '</thead>' +
        '<tbody>' + table1Rows + '</tbody>' +
      '</table>' +
    '</div>' +

    '<div>' +
      '<h4 class="font-extrabold text-slate-900 mb-1">2. Kebutuhan Makanan Matang untuk Lokasi Ini</h4>' +
      '<table class="w-full border-collapse border border-slate-300 text-[11px]">' +
        '<thead class="bg-slate-100">' +
          '<tr>' +
            '<th class="border border-slate-300 p-1.5 text-left">Item</th>' +
            '<th class="border border-slate-300 p-1.5 text-center">Per Porsi</th>' +
            '<th class="border border-slate-300 p-1.5 text-center">Total Kebutuhan</th>' +
            '<th class="border border-slate-300 p-1.5 text-left">Catatan Teknis</th>' +
          '</tr>' +
        '</thead>' +
        '<tbody>' + table2Rows + '</tbody>' +
      '</table>' +
    '</div>' +

    '<div>' +
      '<h4 class="font-extrabold text-slate-900 mb-1">3. Checklist Serah Terima Distribusi</h4>' +
      '<table class="w-full border-collapse border border-slate-300 text-[11px]">' +
        '<thead class="bg-slate-100">' +
          '<tr>' +
            '<th class="border border-slate-300 p-1.5 text-left">Item</th>' +
            '<th class="border border-slate-300 p-1.5 text-center">Target Wadah</th>' +
            '<th class="border border-slate-300 p-1.5 text-center">Aktual Wadah</th>' +
            '<th class="border border-slate-300 p-1.5 text-center">Paraf Driver</th>' +
          '</tr>' +
        '</thead>' +
        '<tbody>' + table3Rows + '</tbody>' +
      '</table>' +
    '</div>' +

    '<div class="grid grid-cols-2 pt-4 text-[11px]">' +
      '<div>' +
        '<p class="font-bold">Kepala Regu Pemorsian:</p>' +
        '<div class="h-10"></div>' +
        '<p>( ................................................. )</p>' +
      '</div>' +
      '<div class="text-right">' +
        '<p class="font-bold">Driver / Aslap Penerima:</p>' +
        '<div class="h-10"></div>' +
        '<p>( ................................................. )</p>' +
      '</div>' +
    '</div>' +
  '</div>';

  modalPreview.innerHTML = printHtml;
  printContainer.innerHTML = printHtml;
  document.getElementById('print-school-modal').classList.remove('hidden');
}

function closeSchoolPrintModal() {
  const modal = document.getElementById('print-school-modal');
  if (modal) modal.classList.add('hidden');
}
"""

print("school_batches_js generated successfully, length:", len(school_batches_js))

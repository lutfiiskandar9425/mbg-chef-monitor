# -*- coding: utf-8 -*-
import os
import re

new_selasa_batches = """  selasa: {
    title: "Selasa, 10 November 2026",
    menu: "Nasi Gurih + Ayam Katsu + Sambal Geprek Hijau (PB) + Tahu Goreng + Mix Vigie + Pisang",
    locations: [
      {
        id: "all",
        name: "Total Keseluruhan (SPPG Pekajangan 04)",
        badge: "2.742 Porsi • 13.710 Wadah (x5 Item)",
        pb: 2550,
        pk: 192,
        totalPorsi: 2742,
        totalWadah: 13710,
        driver: "Armada SPPG 1, 2, 3 (Semua Rute)",
        jamBerangkat: "08:45 - 09:30 WIB",
        jamPemorsian: "07:15 - 08:30 WIB",
        alergiNotice: "ALERGI NASI: 3 siswa (SMK 2 siswa, MTs 1 siswa) disiapkan karbo pengganti terpisah berlabel khusus ALERGI NASI.",
        posyanduNotice: "SAMBAL GEPREK HIJAU HANYA UNTUK PB (2.550 porsi). Menu PK (192 balita) Posyandu MUTLAK TANPA SAMBAL.",
        items: [
          { name: "Nasi Gurih (Bahan Tanak)", perPorsi: "~100 g", total: "144,21 kg Beras (2.739 porsi)", wadah: "2.739", note: "Beras 144,21 kg + santan 11,51 L + air 147,12 L + serai 217 btg + salam 288 lbr (3 siswa alergi nasi)" },
          { name: "Ayam Katsu (Berlapis Panir)", perPorsi: "1 potong (~60 g matang)", total: "159,00 kg Fillet Mentah", wadah: "2.742", note: "Fillet dada 159 kg dipipihkan 1 cm @58g + terigu 21,9 kg + telur 21,9 kg + panir 32,9 kg (chiller)" },
          { name: "Sambal Geprek Hijau (PB Saja)", perPorsi: "~15 g (Khusus PB)", total: "27,02 kg Cabai + 9,22 kg Bawang", wadah: "2.550", note: "Rawit hijau 10,81 kg + hijau besar 16,21 kg + b.putih 5,03 kg + b.merah 4,19 kg (PK TANPA SAMBAL)" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g (1 potong)", total: "90,46 kg Tahu Mentah", wadah: "2.742", note: "Tahu padat dipotong dadu 3x3x1,5 cm (~33 g mentah -> 30 g matang susut 10%), lap kering sebelum goreng" },
          { name: "Mix Vigie (Tumis Sayur Campur)", perPorsi: "30 g matang", total: "96,78 kg Sayur + 2,40 kg Bawang", wadah: "2.742", note: "Wortel dadu 29,05 kg + buncis 29,05 kg + kol 19,34 kg + jagung pipil 19,34 kg (4 wadah terpisah)" },
          { name: "Pisang Standar BGN", perPorsi: "1 buah utuh sedang", total: "2.742 buah (+22 cadangan)", wadah: "2.742", note: "Total 2.764 buah disortir bersih lap kain lembap, simpan tempat sejuk berlabel (BUKAN CHILLER)" }
        ]
      },
      {
        id: "smk1",
        name: "SMK 1 Kedungwuni",
        badge: "1.723 Porsi (1.712 Sekolah + 11 Sampel QC) • 8.615 Wadah",
        pb: 1723,
        pk: 0,
        totalPorsi: 1723,
        totalWadah: 8615,
        driver: "Armada SPPG 1 (Elf Box)",
        jamBerangkat: "09:00 WIB",
        jamPemorsian: "07:15 - 08:15 WIB",
        alergiNotice: "2 SISWA ALERGI NASI (SMK 1): Tidak diberi nasi gurih. Karbo pengganti disiapkan terpisah label ALERGI NASI. Kebutuhan nasi: 1.721 porsi.",
        posyanduNotice: "11 PORSI KHUSUS: 2 porsi sampel dapur + 9 porsi uji organoleptik QC Lab dikemas di wadah terpisah label SAMPEL/QC.",
        drivePdf: "https://drive.google.com/file/d/1yoaNZLeNKvHIRInwBZvT8ZZLwKhzYTuj/view?usp=sharing",
        items: [
          { name: "Nasi Gurih (Bahan Tanak)", perPorsi: "~100 g", total: "90,61 kg Beras (1.721 porsi)", wadah: "1.721", note: "Beras 90,61 kg + santan 7,23 L + air 92,44 L + serai 136 btg + salam 181 lbr + b.putih 1,38 kg + garam 880 g" },
          { name: "Ayam Katsu (Berlapis Panir)", perPorsi: "1 potong (~60 g)", total: "99,91 kg Fillet Mentah (1.723 potong)", wadah: "1.723", note: "Ayam 99,91 kg tebal 1 cm @58g + terigu 13,79 kg + telur 13,79 kg + panir 20,65 kg + marinasi 2,83 kg" },
          { name: "Sambal Geprek Hijau (PB Saja)", perPorsi: "~15 g", total: "18,26 kg Cabai (1.723 porsi)", wadah: "1.723", note: "Rawit hijau 7,30 kg + hijau besar 10,95 kg + b.putih 3,40 kg + b.merah 2,83 kg + minyak 2,27 L" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g", total: "56,85 kg Tahu Mentah (1.723 potong)", wadah: "1.723", note: "Tahu putih padat mentah 56,85 kg, potong dadu 3x3x1,5 cm (~33 g mentah per porsi)" },
          { name: "Mix Vigie (Tumis Sayur Campur)", perPorsi: "30 g", total: "60,82 kg Sayur (1.723 porsi)", wadah: "1.723", note: "Wortel dadu 18,26 kg + buncis serong 18,26 kg + kol 12,15 kg + jagung 12,15 kg + bumbu 1,51 kg (4 wadah)" },
          { name: "Pisang Standar BGN", perPorsi: "1 buah utuh", total: "1.723 buah (+13 cadangan)", wadah: "1.723", note: "1.736 buah disortir mulus, simpan tempat sejuk berlabel SMK 1 Kedungwuni" }
        ]
      },
      {
        id: "mts",
        name: "MTs Salafiyah Syafiiyah",
        badge: "646 Porsi • 3.230 Wadah (x5 Item)",
        pb: 646,
        pk: 0,
        totalPorsi: 646,
        totalWadah: 3230,
        driver: "Armada SPPG 2 (GrandMax Box)",
        jamBerangkat: "09:15 WIB",
        jamPemorsian: "07:30 - 08:30 WIB",
        alergiNotice: "1 SISWA ALERGI NASI (MTs): Tidak diberi nasi gurih. Karbo pengganti disiapkan terpisah label ALERGI NASI. Kebutuhan nasi: 645 porsi.",
        posyanduNotice: "Semua porsi adalah Porsi Besar (PB 646). Semua mendapatkan sambal geprek hijau.",
        drivePdf: "https://drive.google.com/file/d/1f7FKLGYswwkjHmfsqjm2cqVHvUwx23Lj/view?usp=sharing",
        items: [
          { name: "Nasi Gurih (Bahan Tanak)", perPorsi: "~100 g", total: "33,96 kg Beras (645 porsi)", wadah: "645", note: "Beras 33,96 kg + santan 2,71 L + air 34,64 L + serai 51 btg + salam 68 lbr + b.putih 518 g + garam 330 g" },
          { name: "Ayam Katsu (Berlapis Panir)", perPorsi: "1 potong (~60 g)", total: "37,46 kg Fillet Mentah (646 potong)", wadah: "646", note: "Ayam 37,46 kg tebal 1 cm @58g + terigu 5,17 kg + telur 5,17 kg + panir 7,74 kg + marinasi 1,06 kg" },
          { name: "Sambal Geprek Hijau (PB Saja)", perPorsi: "~15 g", total: "6,84 kg Cabai (646 porsi)", wadah: "646", note: "Rawit hijau 2,74 kg + hijau besar 4,11 kg + b.putih 1,27 kg + b.merah 1,06 kg + minyak 850 ml" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g", total: "21,31 kg Tahu Mentah (646 potong)", wadah: "646", note: "Tahu putih padat 21,31 kg potong 3x3x1,5 cm (~33 g mentah -> 30 g matang)" },
          { name: "Mix Vigie (Tumis Sayur Campur)", perPorsi: "30 g", total: "22,80 kg Sayur (646 porsi)", wadah: "646", note: "Wortel dadu 6,84 kg + buncis serong 6,84 kg + kol 4,56 kg + jagung 4,56 kg + bumbu 566 g (4 wadah)" },
          { name: "Pisang Standar BGN", perPorsi: "1 buah utuh", total: "646 buah (+5 cadangan)", wadah: "646", note: "651 buah disortir mulus, simpan tempat sejuk berlabel MTs Salafiyah Syafiiyah" }
        ]
      },
      {
        id: "posyandu_ambokembang",
        name: "Posyandu Ambokembang",
        badge: "185 Porsi (86 PB + 99 PK Balita) • 925 Wadah",
        pb: 86,
        pk: 99,
        totalPorsi: 185,
        totalWadah: 925,
        driver: "Armada SPPG 3 (Carry Pick-up)",
        jamBerangkat: "08:45 WIB",
        jamPemorsian: "07:00 - 08:00 WIB",
        alergiNotice: "Tidak ada catatan alergi nasi untuk lokasi ini.",
        posyanduNotice: "SAMBAL GEPREK HIJAU HANYA UNTUK 86 PB. Menu 99 PK Balita MUTLAK TANPA SAMBAL. Kemas dan beri label terpisah (PB / PK).",
        drivePdf: "https://drive.google.com/file/d/1iWisATp6qEb1YSw3Sj4tiFRs7CBHm4rc/view?usp=sharing",
        items: [
          { name: "Nasi Gurih (Bahan Tanak)", perPorsi: "~100 g", total: "9,74 kg Beras (185 porsi)", wadah: "185", note: "Beras 9,74 kg + santan 777 ml + air 9,94 L + serai 15 btg + salam 19 lbr + b.putih 149 g + garam 95 g" },
          { name: "Ayam Katsu (Berlapis Panir)", perPorsi: "1 potong (~60 g)", total: "10,73 kg Fillet Mentah (185 potong)", wadah: "185", note: "Ayam 10,73 kg @58g + terigu 1,48 kg + telur 1,48 kg + panir 2,22 kg + b.putih 162 g + garam lada 142 g" },
          { name: "Sambal Geprek Hijau (86 PB Saja)", perPorsi: "~15 g (PB Saja)", total: "911 g Cabai (Khusus 86 PB)", wadah: "86", note: "Rawit hijau 364 g + hijau besar 547 g + b.putih 170 g + b.merah 141 g (99 PK BALITA TANPA SAMBAL)" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g", total: "6,10 kg Tahu Mentah (185 potong)", wadah: "185", note: "Tahu padat 6,10 kg lap kering potong 3x3x1,5 cm (~33 g mentah -> 30 g matang)" },
          { name: "Mix Vigie (Tumis Sayur Campur)", perPorsi: "30 g", total: "6,52 kg Sayur (185 porsi)", wadah: "185", note: "Wortel dadu 1,96 kg + buncis serong 1,96 kg + kol 1,30 kg + jagung 1,30 kg + bumbu 162 g (4 wadah)" },
          { name: "Pisang Standar BGN", perPorsi: "1 buah utuh", total: "185 buah (+2 cadangan)", wadah: "185", note: "187 buah disortir mulus, simpan tempat sejuk berlabel Posyandu Ambokembang" }
        ]
      },
      {
        id: "posyandu_panjomblangan",
        name: "Posyandu Panjomblangan",
        badge: "188 Porsi (95 PB + 93 PK Balita) • 940 Wadah",
        pb: 95,
        pk: 93,
        totalPorsi: 188,
        totalWadah: 940,
        driver: "Armada SPPG 3 (Carry Pick-up)",
        jamBerangkat: "09:00 WIB",
        jamPemorsian: "07:15 - 08:15 WIB",
        alergiNotice: "Tidak ada catatan alergi nasi untuk lokasi ini.",
        posyanduNotice: "SAMBAL GEPREK HIJAU HANYA UNTUK 95 PB. Menu 93 PK Balita MUTLAK TANPA SAMBAL. Kemas dan beri label terpisah (PB / PK).",
        drivePdf: "https://drive.google.com/file/d/18SLMbLHNq-6ROzARVFOmoNslsWJy9bjU/view?usp=sharing",
        items: [
          { name: "Nasi Gurih (Bahan Tanak)", perPorsi: "~100 g", total: "9,90 kg Beras (188 porsi)", wadah: "188", note: "Beras 9,90 kg + santan 790 ml + air 10,10 L + serai 15 btg + salam 20 lbr + b.putih 151 g + garam 96 g" },
          { name: "Ayam Katsu (Berlapis Panir)", perPorsi: "1 potong (~60 g)", total: "10,90 kg Fillet Mentah (188 potong)", wadah: "188", note: "Ayam 10,90 kg @58g + terigu 1,50 kg + telur 1,50 kg + panir 2,25 kg + b.putih 165 g + garam lada 144 g" },
          { name: "Sambal Geprek Hijau (95 PB Saja)", perPorsi: "~15 g (PB Saja)", total: "1,01 kg Cabai (Khusus 95 PB)", wadah: "95", note: "Rawit hijau 403 g + hijau besar 604 g + b.putih 187 g + b.merah 156 g (93 PK BALITA TANPA SAMBAL)" },
          { name: "Tahu Goreng Gurih", perPorsi: "30 g", total: "6,20 kg Tahu Mentah (188 potong)", wadah: "188", note: "Tahu padat 6,20 kg lap kering potong 3x3x1,5 cm (~33 g mentah -> 30 g matang)" },
          { name: "Mix Vigie (Tumis Sayur Campur)", perPorsi: "30 g", total: "6,64 kg Sayur (188 porsi)", wadah: "188", note: "Wortel dadu 1,99 kg + buncis serong 1,99 kg + kol 1,33 kg + jagung 1,33 kg + bumbu 165 g (4 wadah)" },
          { name: "Pisang Standar BGN", perPorsi: "1 buah utuh", total: "188 buah (+2 cadangan)", wadah: "188", note: "190 buah disortir mulus, simpan tempat sejuk berlabel Posyandu Panjomblangan" }
        ]
      }
    ],
    aturanEmas: [
      "Cuci tangan pakai sabun sebelum mulai, setelah pegang ayam/telur mentah, setelah dari toilet, dan setiap ganti pekerjaan. Wajib masker, penutup rambut, celemek, sarung tangan steril.",
      "Ayam dan telur mentah WAJIB dipisah dari sayur dan buah. Gunakan talenan, pisau, dan baki khusus ayam mentah. Setelah selesai, cuci dan sanitasi menyeluruh.",
      "Teknik melapis katsu: Satu tangan basah, satu tangan kering saat melapisi tepung supaya tepung tidak menggumpal di tangan dan lapisan panir menempel rata.",
      "Timbang dan hitung, jangan menebak! Bahan kurang atau lebih wajib segera lapor ke Penanggung Jawab atau Kepala Dapur.",
      "SAMBAL GEPREK HIJAU HANYA UNTUK PORSI BESAR (PB 2.550 porsi). Menu Porsi Kecil (PK 192 balita) Posyandu MUTLAK TANPA SAMBAL. Kemas di wadah terpisah dan berlabel jelas.",
      "ALERGI NASI: 3 siswa (2 di SMK 1 Kedungwuni, 1 di MTs) tidak diberi nasi gurih, disiapkan karbo pengganti terpisah berlabel ALERGI NASI. Kebutuhan nasi gurih: 2.739 porsi.",
      "Pisang disimpan di tempat sejuk berlabel (DILARANG masuk chiller agar kulit tidak menghitam). 11 porsi sampel dapur & uji organoleptik QC Lab dikemas di wadah tersendiri."
    ],
    posKerja: [
      { pos: "Pos 1: Seksi Karbohidrat", tugas: "Timbang beras 144,21 kg (1 kg = 19 porsi), cuci 2-3x air mengalir, campur santan 11,51 L, serai 217 btg memar, salam 288 lbr, b.putih 2,2 kg geprek, garam 1,4 kg (rasio cairan 1:1,1).", target: "144,21 kg Beras (2.739 porsi gurih + 3 porsi alergi)", picSerah: "Tim Pengolahan (Seksi Karbohidrat)" },
      { pos: "Pos 2: Seksi Protein Hewani", tugas: "Timbang fillet dada 159 kg buang lemak/urat, pipihkan rata tebal ±1 cm, potong seragam @58g. Marinasi chiller 20-30 mnt. Lapisi 3 baskom (terigu 21,9 kg -> telur 21,9 kg -> panir 32,9 kg). Susun loyang baking paper.", target: "159,00 kg Fillet Mentah (2.742 potong katsu siap goreng)", picSerah: "Tim Pengolahan (Seksi Protein Hewani)" },
      { pos: "Pos 3: Seksi Side & Bumbu", tugas: "Cuci bersih & potong kasar cabai rawit hijau 10,8 kg, cabai hijau besar 16,2 kg, b.putih 5,0 kg, b.merah 4,2 kg. Wajib sarung tangan. Kemas label SAMBAL GEPREK (PB). Jangan siapkan untuk PK balita!", target: "36,24 kg Bahan Sambal (2.550 porsi PB saja)", picSerah: "Tim Pengolahan (Seksi Bumbu & Sambal)" },
      { pos: "Pos 4: Seksi Protein Nabati", tugas: "Tiriskan air rendaman tahu 90,5 kg, tekan perlahan lap kain bersih sampai kesat agar tidak muncrat. Potong dadu 3x3x1,5 cm (@33g mentah -> 30g matang). Rendam 5 mnt air garam + b.putih bubuk, tiriskan lagi.", target: "90,46 kg Tahu Mentah (2.742 potong)", picSerah: "Tim Pengolahan (Seksi Protein Nabati)" },
      { pos: "Pos 5: Seksi Sayuran", tugas: "Cuci tiriskan sayur. Potong 4 wadah terpisah: wortel dadu 0,7 cm (29,1 kg), buncis serong 2 cm (29,1 kg), kol kotak 2 cm (19,3 kg), jagung manis pipil (19,3 kg), duo bawang iris (2,4 kg). Simpan chiller terpisah.", target: "99,18 kg Sayur & Bumbu Siap Tumis (2.742 porsi)", picSerah: "Tim Pengolahan (Seksi Sayuran)" },
      { pos: "Pos 6: Seksi Buah & QC Timbang", tugas: "Sortir 2.742 buah pisang utuh mulus tanpa memar/busuk (+22 cadangan), lap kain lembap bersih. Hitung sesuai kuota sekolah. Simpan tempat sejuk berlabel (bukan chiller). Selesai di Tim Persiapan.", target: "2.764 Buah Pisang (2.742 porsi + 22 cadangan)", picSerah: "Tim Pemorsian" }
    ],
    jadwalMundur: [
      { waktu: "01:00 - 02:30 WIB", kegiatan: "Briefing sanitasi & APD lengkap, penimbangan & cuci beras 144 kg, siapkan santan daun salam serai geprek, penimbangan & penirisan tahu lap kain bersih." },
      { waktu: "02:30 - 04:30 WIB", kegiatan: "Fillet ayam dipipihkan seragam 1 cm, potong ukuran 58 g, marinasi chiller 20-30 menit, pemotongan kasar cabai sambal geprek hijau PB, pemotongan 4 komponen mix vigie di wadah terpisah." },
      { waktu: "04:30 - 06:00 WIB", kegiatan: "Pelapisan katsu 3 baskom (terigu -> telur -> panir), penataan di loyang baking paper chiller, penanakan nasi gurih kapasitas alat, penggorengan tahu suhu 160°C." },
      { waktu: "06:00 - 07:15 WIB", kegiatan: "Penggorengan ayam katsu deep fry 170°C (suhu inti >= 75°C), penumisan cabai sambal geprek layu & ulek kasar limau, penumisan stir-fry mix vigie cepat api besar, penyortiran pisang segar." },
      { waktu: "07:15 - 08:30 WIB", kegiatan: "QC Lab uji organoleptik 11 porsi, pemorsian ompreng PB (nasi 100g, katsu geprek 60g, tahu 30g, mix vigie 30g, pisang), pemorsian PK balita (katsu tanpa sambal), pemorsian 3 porsi alergi nasi." },
      { waktu: "08:45 - 09:30 WIB", kegiatan: "Final sealing kontainer berlabel tiap sekolah (SMK 1: 1.723, MTs: 646, Ambokembang: 185, Panjomblangan: 188), serah terima ke armada driver SPPG." }
    ]
  },
"""

new_selasa_menu_cycle = """      selasa: {
        title: "Nasi Gurih + Ayam Katsu + Sambal Geprek Hijau (PB) + Tahu Goreng + Mix Vigie + Pisang",
        nutrition: "Energi 710 kkal • Protein 29 gr • Karbohidrat Kompleks, Vitamin A & C",
        notePersiapan: "Fillet ayam buang lemak/urat, pipihkan rata tebal ±1 cm, potong seragam @58g, marinasi b.putih halus + garam lada di chiller 20-30 mnt. Lapisi 3 baskom (terigu -> telur -> panir), panir ditekan menempel kuat, satu tangan basah satu tangan kering. Simpan chiller beralas baking paper jangan bertumpuk. Cuci beras rasio 1:1,1 santan daun salam serai geprek. Tahu lap kain bersih kering potong 3x3x1,5 cm. Sayur mix vigie cuci potong 4 wadah terpisah (wortel dadu 0,7 cm, buncis serong 2 cm, kol kotak 2 cm, jagung pipil). Sambal geprek potong kasar rawit & hijau besar KHUSUS PB (PK TANPA SAMBAL). Pisang sortir simpan tempat sejuk (bukan chiller).",
        notePengolahan: "Goreng katsu deep fry minyak 170°C selama 4-5 menit sampai kuning keemasan matang (suhu inti >= 75°C), tiriskan di rak (bukan ditumpuk tertutup). Nasi gurih santan diaduk awal agar tidak menggumpal, rasio cairan 1:1,1. Goreng tahu 160°C sampai kesat keemasan. Tumis bumbu, masukkan wortel + jagung 2-3 mnt, buncis, lalu kol di menit terakhir secara cepat (stir-fry) agar sayur tetap empuk renyah dan warna hijau segar terjaga, tiriskan kuah sebelum diporsi. Tumis bumbu sambal layu matang lalu ulek kasar dengan perasan jeruk limau dan siram minyak panas.",
        notePemorsian: "Ompreng PB diisi nasi gurih 100 g di sekat utama, ayam katsu 60 g digeprek sambal hijau 15 g di sekat lauk, tahu goreng 30 g, mix vigie 30 g, dan pisang segar di sekat buah. Ompreng PK balita (192 porsi): katsu TANPA SAMBAL GEPREK. 3 siswa alergi nasi (SMK 2 siswa, MTs 1 siswa) diberikan karbo pengganti terpisah stiker khusus ALERGI NASI.",
        items: [
          { name: "Daging Ayam Fillet Katsu", category: "Protein Hewani", portion: "60 gr matang (1 potong)", targetOrder: "159.00 kg Fillet", supplier: "PO-013 / PT Unggas Sejahtera", tare: "0.85", persiapan: "Pipihkan tebal seragam ±1 cm, potong 58 g, marinasi chiller 20-30 mnt, balur terigu-telur-panir rapat (chiller).", pengolahan: "Deep fry minyak 170°C selama 4-5 mnt keemasan matang, tiriskan di rak (suhu inti >= 75°C).", pemorsian: "1 potong katsu renyah 60 g di sekat lauk utama (PB digeprek sambal, PK tanpa sambal)." },
          { name: "Beras Putih Nasi Gurih", category: "Karbohidrat", portion: "~100 gr matang", targetOrder: "144.21 kg Beras", supplier: "PO-012 / Koperasi Tani", tare: "0.85", persiapan: "Cuci 2-3x tiriskan, siapkan santan 11,5 L, serai 217 btg memar, salam 288 lbr, b.putih 2,2 kg geprek, garam 1,4 kg.", pengolahan: "Tanak rice steamer rasio cairan 1:1,1, aduk awal agar santan tidak gumpal, diamkan 5-10 mnt setelah matang.", pemorsian: "Takar 100 g nasi gurih pulen. 3 siswa alergi nasi diganti kentang kukus 150 g terpisah ALERGI NASI." },
          { name: "Sambal Geprek Hijau (PB Saja)", category: "Pelengkap (Side)", portion: "~15 gr (Khusus PB)", targetOrder: "27.02 kg Cabai + 9.22 kg Bawang", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Rawit hijau 10,8 kg + hijau besar 16,2 kg + b.putih 5,0 kg + b.merah 4,2 kg cuci potong kasar 1 cm (sarung tangan).", pengolahan: "Tumis 3-4 mnt layu matang, ulek kasar bersama garam gula jeruk limau, siram minyak panas. JANGAN BUAT UNTUK BALITA PK.", pemorsian: "Takar 15 g di atas katsu khusus ompreng PB (2.550 porsi). PK 192 balita TANPA SAMBAL." },
          { name: "Tahu Putih Segar Goreng", category: "Protein Nabati", portion: "30 gr matang (1 potong)", targetOrder: "90.46 kg Tahu Mentah", supplier: "Koperasi Tahu Kedungwuni", tare: "0.85", persiapan: "Tiriskan air pabrik, tekan lap kain kering kesat, potong 3x3x1,5 cm (~33 g mentah), rendam air garam b.putih 5 mnt.", pengolahan: "Goreng minyak 160°C selama 6-8 mnt sampai kuning keemasan kesat dan sedikit renyah, tiriskan di rak.", pemorsian: "1 potong tahu goreng gurih 30 g di sekat kedua ompreng berdampingan dengan katsu." },
          { name: "Mix Vigie (Sayur Campur)", category: "Sayuran Segar", portion: "30 gr matang", targetOrder: "96.78 kg Sayur + 2.40 kg Bawang", supplier: "Kelompok Tani Pekajangan", tare: "0.50", persiapan: "Wortel dadu 0,7 cm (29 kg), buncis serong 2 cm (29 kg), kol kotak 2 cm (19,3 kg), jagung pipil (19,3 kg) - 4 wadah terpisah.", pengolahan: "Tumis bawang harum, wortel+jagung 2-3 mnt, buncis, kol di menit terakhir (stir-fry cepat 8-10 mnt), tiriskan kuah.", pemorsian: "Takar 30 g sayur segar renyah di sekat sayur ompreng (hindari kuah berlebih)." },
          { name: "Pisang Standar BGN", category: "Buah Segar", portion: "1 buah utuh sedang", targetOrder: "2.742 pcs (+22 cadangan)", supplier: "Distributor Buah Nusantara", tare: "0.00", persiapan: "Sortir buah mulus tanpa memar/busuk, lap kain lembap bersih. Simpan tempat sejuk berlabel (BUKAN CHILLER).", pengolahan: "Tidak melalui proses masak. Selesai di Tim Persiapan.", pemorsian: "1 buah pisang segar utuh di sekat buah paling kering." }
        ]
      },
"""

bumbu_sticky_code = """    if (currentDirectiveSubtab === 'bumbu') {
      let bumbuHtml = '';
      if (currentDay === 'selasa') {
        bumbuHtml = '<div class="space-y-2 text-xs text-slate-800">' +
          '<div class="p-2.5 bg-white/90 border border-amber-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-amber-100 pb-1">' +
              '<span class="font-black text-amber-950 text-xs">🍗 1. AYAM KATSU (2.742 POTONG - DADA FILLET 159 KG)</span>' +
              '<span class="text-[9px] font-bold bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full">Seksi Protein Hewani</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Pipihkan Seragam:</strong> Fillet dada 159 kg dibersihkan urat/lemak. Jika tebal > 2 cm, iris tipis horizontal. Pipihkan dengan pemukul sampai tebal seragam +-1 cm (kunci agar cepat & matang merata).</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Potong & Hitung:</strong> Potong seragam +-58 g per potong. Timbang 10 potong pertama sebagai acuan patokan. Total 2.742 potong.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Marinasi Chiller:</strong> Campur bawang putih halus 2,40 kg dan garam + lada bubuk 2,10 kg. Lumuri ayam rata, simpan di chiller 20-30 menit.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Lapisi 3 Baskom:</strong> Siapkan terigu 21,94 kg -> telur kocok 21,94 kg -> tepung panir/panko 32,86 kg. <strong class="text-amber-800">Satu tangan khusus bahan basah, satu tangan khusus bahan kering</strong> agar tangan tidak menggumpal.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Tekan Panir & Simpan:</strong> Balur terigu (kibaskan), celup telur, gulingkan di panir dan <strong class="text-rose-700">tekan rapat</strong> agar tidak rontok saat digoreng. Susun di loyang beralas baking paper tidak bertumpuk, tutup simpan chiller.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Deep fry minyak +-170°C, goreng 5-6 potong per batch +-4-5 menit, balik sekali sampai keemasan matang (suhu inti >= 75°C), tiriskan di rak (bukan ditumpuk tertutup).</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-purple-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-purple-100 pb-1">' +
              '<span class="font-black text-purple-950 text-xs">🍚 2. NASI GURIH (144,21 KG BERAS / 2.739 PORSI + 3 ALERGI)</span>' +
              '<span class="text-[9px] font-bold bg-purple-100 text-purple-800 px-2 py-0.5 rounded-full">Seksi Karbohidrat</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Cuci Beras:</strong> Timbang beras 144,21 kg (1 kg = 19 porsi). Cuci lembut 2-3 kali sampai air bilasan relatif jernih, tiriskan.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Bumbu Aromatik:</strong> Memarkan 217 batang serai dengan ulekan. Geprek 2,20 kg bawang putih.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Campur Cairan Masak:</strong> Santan kental 11,51 liter + air 147,12 liter + daun salam 288 lembar + serai memar + bawang putih geprek + garam 1,40 kg. Aduk rata. Rasio total cairan masak 1 : 1,1 terhadap beras.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Aduk sekali di awal agar santan tidak menggumpal, jangan sering dibuka. Buang serai dan salam setelah matang, diamkan 5-10 menit, aduk bawah ke atas. Target +-100 g nasi matang.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• 3 Siswa Alergi Nasi:</strong> SMK 2 siswa, MTs 1 siswa tidak diberi nasi gurih. Kukus kentang +-150 g, wadah terpisah stiker khusus ALERGI NASI.</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-rose-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-rose-100 pb-1">' +
              '<span class="font-black text-rose-950 text-xs">🌶️ 3. SAMBAL GEPREK HIJAU (PB 2.550 PORSI - BALITA PK TANPA SAMBAL)</span>' +
              '<span class="text-[9px] font-bold bg-rose-100 text-rose-800 px-2 py-0.5 rounded-full">Baskom PB • Label SAMBAL</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Timbang Cabai & Bawang:</strong> Cabai rawit hijau 10,81 kg + cabai hijau besar 16,21 kg (total cabai 27,02 kg), bawang putih 5,03 kg, bawang merah 4,19 kg.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Bersihkan & Potong:</strong> Buang tangkai cabai, cuci bersih tiriskan, kupas bawang. Potong kasar cabai dan bawang +-1 cm. <strong class="text-rose-700">Wajib pakai sarung tangan</strong> dan jangan menyentuh mata.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Kemas & Label:</strong> Masuk wadah berlabel Sambal Geprek Hijau (PB). <strong class="text-rose-700 underline">MUTLAK JANGAN SIAPKAN UNTUK PK BALITA!</strong></p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Tumis 3-4 menit sampai layu matang (tidak boleh mentah). Ulek kasar bersama garam, gula, perasan air jeruk limau, lalu siram minyak panas 3,36 liter.</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-amber-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-amber-100 pb-1">' +
              '<span class="font-black text-amber-950 text-xs">🧈 4. TAHU GORENG GURIH (2.742 POTONG MATANG)</span>' +
              '<span class="text-[9px] font-bold bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full">Seksi Protein Nabati</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Tiris & Tekan Kering:</strong> Buang air rendaman pabrik 90,46 kg tahu. Tekan perlahan dengan kain bersih sampai kering dan kesat agar minyak panas tidak muncrat/meletup.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Potong:</strong> Dadu/persegi seragam +-3x3x1,5 cm (target 33 g mentah -> 30 g matang susut 10%). Timbang 10 potong pertama sebagai acuan.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Rendam & Tiris:</strong> Rendam 5 menit di air garam encer + bawang putih bubuk, tiriskan lagi sampai kering sebelum diserahkan.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Minyak +-170°C, jangan terlalu penuh per batch, goreng +-6-8 menit sampai kuning keemasan dan sedikit renyah, tiriskan di rak.</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-emerald-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-emerald-100 pb-1">' +
              '<span class="font-black text-emerald-950 text-xs">🥕 5. MIX VIGIE (TUMIS SAYUR CAMPUR 4 JENIS TERPISAH)</span>' +
              '<span class="text-[9px] font-bold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full">Seksi Sayuran</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Potong Per Jenis (4 Wadah):</strong> Wortel 29,05 kg kupas potong dadu kecil +-0,7 cm. Buncis 29,05 kg buang ujung iris serong +-2 cm. Kol putih 19,34 kg iris persegi +-2x2 cm. Jagung manis 19,34 kg dipipil dari bonggolnya.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Bumbu & Simpan Chiller:</strong> Iris tipis bawang merah dan bawang putih 2,40 kg. Simpan tiap jenis di wadah terpisah (karena waktu masuk wajan berbeda) di chiller berlabel.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Tumis bawang harum, wortel + jagung 2-3 menit, lalu buncis, dan kol di menit terakhir, bumbui garam kaldu gula. Total masak +-8-10 menit, sayur masih sedikit renyah, tiriskan kuah berlebih sebelum diporsi.</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-blue-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-blue-100 pb-1">' +
              '<span class="font-black text-blue-950 text-xs">🍌 6. PISANG STANDAR BGN (2.742 BUAH + 22 CADANGAN)</span>' +
              '<span class="text-[9px] font-bold bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">Selesai di Persiapan</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Sortir Mulus:</strong> Pisahkan buah busuk, memar parah, kulit pecah, atau terlalu lembek. Pilih kematangan seragam.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Lap & Simpan Sejuk:</strong> Lap bersih dengan kain lembap (tidak perlu dicuci basah). Simpan di wadah berlabel di tempat sejuk (<strong class="text-rose-700">BUKAN CHILLER</strong> agar kulit tidak menghitam).</p>' +
          '</div>' +
        '</div>';
      } else {
        bumbuHtml = '<div class="space-y-2 text-xs text-slate-800">' +
          '<div class="p-2.5 bg-white/90 border border-rose-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-rose-100 pb-1">' +
              '<span class="font-black text-rose-950 text-xs">🍗 1. AYAM RICA-RICA (PB 2.550 PORSI - PEDAS SEDANG)</span>' +
              '<span class="text-[9px] font-bold bg-rose-100 text-rose-800 px-2 py-0.5 rounded-full">Baskom PB • Label RICA</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Potong Dadu:</strong> 12.750 dadu seragam +-2x2 cm (12-14 gram/dadu, tepat 5 dadu per porsi). Timbang 10 dadu pertama sebagai acuan.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Marinasi Chiller:</strong> Balur bawang putih halus + garam + lada bubuk. Diamkan 20-30 menit di dalam chiller pendingin.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Adonan Celup:</strong> Terigu + maizena + air dingin + garam sampai tekstur seperti cat kental (menempel tipis di sendok).</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Bumbu Halus Rica:</strong> Haluskan bawang merah 8,2 kg, cabai merah keriting 9,8 kg, cabai rawit 2,9 kg, tomat 3,9 kg, bawang putih 3,1 kg, jahe & kunyit 2,4 kg.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Bumbu Aromatik:</strong> Memarkan 49 batang serai, siapkan daun jeruk purut (buang tulang daun agar tidak pahit).</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Cara Masak:</strong> Goreng ayam dadu tepung suhu 160°C hingga matang (suhu inti >= 75°C). Tumis bumbu halus bersama serai dan daun jeruk sampai tanak berminyak dan harum gurih. Masukkan ayam, aduk cepat meresap dan tidak berair.</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-blue-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-blue-100 pb-1">' +
              '<span class="font-black text-blue-950 text-xs">🍗 2. AYAM KECAP MANIS (PK BALITA 192 PORSI - TANPA CABAI)</span>' +
              '<span class="text-[9px] font-bold bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">Baskom PK • Label KECAP</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Potong Dadu:</strong> 960 dadu seragam +-2x2 cm (5 dadu per porsi). Simpan di baskom terpisah dari PB!</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Racikan Bumbu:</strong> Iris tipis bawang merah, cincang halus bawang putih, sisir gula merah 0,3 kg, kecap manis 1,2 L, sedikit garam & air. <strong class="text-rose-700 underline">MUTLAK TANPA CABAI!</strong></p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Cara Masak:</strong> Goreng ayam dadu hingga matang empuk. Tumis bawang hingga harum, masukkan kecap, gula merah, garam dan air. Masak hingga mengental karamel gurih meresap.</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-amber-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-amber-100 pb-1">' +
              '<span class="font-black text-amber-950 text-xs">🧈 3. TAHU GORENG GURIH (2.742 POTONG MATANG)</span>' +
              '<span class="text-[9px] font-bold bg-amber-100 text-amber-800 px-2 py-0.5 rounded-full">Seksi Protein Nabati</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Tiris & Tekan Kering:</strong> Buang air rendaman pabrik. Tekan perlahan dengan kain bersih sampai permukaan kering dan kesat agar minyak panas tidak muncrat/meletup.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Potong:</strong> Ukuran seragam +-3x3x1,5 cm (target 33 g mentah -> 30 g matang susut 10%).</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Rendam & Goreng:</strong> Rendam 5 menit di air garam encer + bawang putih bubuk, tiriskan lagi. Goreng suhu 160°C sampai kuning keemasan dan kesat.</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-emerald-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-emerald-100 pb-1">' +
              '<span class="font-black text-emerald-950 text-xs">🥕 4. TUMIS PUTREN WORTEL (PUTREN 48 KG + WORTEL 48 KG)</span>' +
              '<span class="text-[9px] font-bold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full">Seksi Sayuran</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Potong:</strong> Putren kupas kelobot & rambut, belah dua memanjang, potong serong 2,5 cm. Wortel kupas, iris setengah bulan tipis 0,4 cm.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Bumbu Tumis:</strong> Iris tipis bawang merah dan bawang putih. Simpan di wadah terpisah.</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Teknik Masak Cepat (Stir-fry):</strong> Tumis bawang hingga harum. Masukkan wortel dulu, lalu putren. Masak api besar secara cepat agar sayur tetap empuk renyah dan warna cerah. Tiriskan kuah sebelum diporsi.</p>' +
          '</div>' +

          '<div class="p-2.5 bg-white/90 border border-purple-200 rounded-xl space-y-1.5 shadow-2xs">' +
            '<div class="flex items-center justify-between border-b border-purple-100 pb-1">' +
              '<span class="font-black text-purple-950 text-xs">🍚 5. NASI & ALERGI (144,3 KG BERAS / 150 KG PO)</span>' +
              '<span class="text-[9px] font-bold bg-purple-100 text-purple-800 px-2 py-0.5 rounded-full">Seksi Karbohidrat</span>' +
            '</div>' +
            '<p class="text-[11px] leading-relaxed"><strong>• Cuci & Masak:</strong> Cuci beras 2-3 kali air mengalir sampai jernih, jangan digosok keras. Rasio air 1 : 1,1 - 1,2. Masak di rice steamer hingga pulen mekar (1 kg beras = 19 porsi).</p>' +
            '<p class="text-[11px] leading-relaxed"><strong>• 3 Siswa Alergi Nasi:</strong> Kukus kentang +-150 g, wadah terpisah stiker khusus ALERGI NASI (SMK 2 siswa, MTs 1 siswa).</p>' +
          '</div>' +
        '</div>';
      }
      body.innerHTML = bumbuHtml;"""

modal_sec2_3_code = """  // Section 2: Porsi per Lokasi
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">' +
    '<div class="flex items-center gap-2 border-b border-slate-100 pb-2.5">' +
      '<span class="w-6 h-6 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">2</span>' +
      '<h3 class="text-xs md:text-sm font-black text-slate-900 uppercase">Jumlah Porsi & Distribusi Tiap Lokasi Sekolah</h3>' +
    '</div>' +
    '<div class="overflow-x-auto"><table class="w-full text-left text-xs border-collapse">' +
      '<thead class="bg-slate-100 text-slate-700 font-extrabold uppercase text-[10px]"><tr><th class="p-2">Lokasi Sekolah / Titik</th><th class="p-2 text-center">Porsi PB</th><th class="p-2 text-center">Porsi PK</th><th class="p-2 text-center">Total Porsi</th><th class="p-2 text-center">Total Wadah (x5)</th><th class="p-2">Catatan Khusus</th></tr></thead>' +
      '<tbody class="divide-y divide-slate-100 text-[11px]">';
  if (currentDay === 'selasa') {
    html += '<tr><td class="p-2 font-bold text-slate-900">SMK 1 Kedungwuni</td><td class="p-2 text-center font-mono-num font-bold">1.712</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">1.712</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">8.560</td><td class="p-2 text-amber-900 font-semibold">2 Siswa Alergi Nasi (1.721 nasi gurih + 2 karbo pengganti)</td></tr>' +
      '<tr><td class="p-2 font-bold text-slate-900">MTs Salafiyah Syafiiyah</td><td class="p-2 text-center font-mono-num font-bold">646</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">646</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">3.230</td><td class="p-2 text-amber-900 font-semibold">1 Siswa Alergi Nasi (645 nasi gurih + 1 karbo pengganti)</td></tr>' +
      '<tr><td class="p-2 font-bold text-slate-900">Posyandu Ambokembang</td><td class="p-2 text-center font-mono-num font-bold">86</td><td class="p-2 text-center font-mono-num font-bold text-blue-700">99</td><td class="p-2 text-center font-mono-num font-bold">185</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">925</td><td class="p-2 text-rose-900 font-semibold">99 PK Balita MUTLAK TANPA SAMBAL (wadah terpisah)</td></tr>' +
      '<tr><td class="p-2 font-bold text-slate-900">Posyandu Panjomblangan</td><td class="p-2 text-center font-mono-num font-bold">95</td><td class="p-2 text-center font-mono-num font-bold text-blue-700">93</td><td class="p-2 text-center font-mono-num font-bold">188</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">940</td><td class="p-2 text-rose-900 font-semibold">93 PK Balita MUTLAK TANPA SAMBAL (wadah terpisah)</td></tr>' +
      '<tr><td class="p-2 font-bold text-slate-900">Sampel Dapur & QC Lab</td><td class="p-2 text-center font-mono-num font-bold">11</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">11</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">55</td><td class="p-2 text-purple-900 font-semibold">2 Sampel Dapur + 9 Uji Organoleptik QC Lab (wadah khusus)</td></tr>' +
      '<tr class="bg-slate-50 font-black text-slate-900"><td class="p-2">TOTAL PRODUKSI</td><td class="p-2 text-center font-mono-num">2.550</td><td class="p-2 text-center font-mono-num">192</td><td class="p-2 text-center font-mono-num text-emerald-800">2.742</td><td class="p-2 text-center font-mono-num text-emerald-900">13.710</td><td class="p-2">13.710 Wadah (x5 item per porsi)</td></tr>';
  } else {
    html += '<tr><td class="p-2 font-bold text-slate-900">SMK 1 Kedungwuni</td><td class="p-2 text-center font-mono-num font-bold">1.712</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">1.712</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">8.560</td><td class="p-2 text-amber-900 font-semibold">2 Siswa Alergi Nasi (1.710 biasa + 2 karbo pengganti)</td></tr>' +
      '<tr><td class="p-2 font-bold text-slate-900">MTs Salafiyah Syafiiyah</td><td class="p-2 text-center font-mono-num font-bold">646</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">646</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">3.230</td><td class="p-2 text-amber-900 font-semibold">1 Siswa Alergi Nasi (645 biasa + 1 karbo pengganti)</td></tr>' +
      '<tr><td class="p-2 font-bold text-slate-900">Posyandu Ambokembang</td><td class="p-2 text-center font-mono-num font-bold">86</td><td class="p-2 text-center font-mono-num font-bold text-blue-700">99</td><td class="p-2 text-center font-mono-num font-bold">185</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">925</td><td class="p-2 text-blue-900 font-semibold">99 PK Balita Ayam Kecap (tidak pedas)</td></tr>' +
      '<tr><td class="p-2 font-bold text-slate-900">Posyandu Panjomblangan</td><td class="p-2 text-center font-mono-num font-bold">95</td><td class="p-2 text-center font-mono-num font-bold text-blue-700">93</td><td class="p-2 text-center font-mono-num font-bold">188</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">940</td><td class="p-2 text-blue-900 font-semibold">93 PK Balita Ayam Kecap (tidak pedas)</td></tr>' +
      '<tr><td class="p-2 font-bold text-slate-900">Sampel & Uji Organoleptik</td><td class="p-2 text-center font-mono-num font-bold">11</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">11</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">55</td><td class="p-2 text-purple-900 font-semibold">2 Sampel Arsip + 9 Uji Organoleptik QC Lab</td></tr>' +
      '<tr class="bg-slate-50 font-black text-slate-900"><td class="p-2">TOTAL PRODUKSI</td><td class="p-2 text-center font-mono-num">2.550</td><td class="p-2 text-center font-mono-num">192</td><td class="p-2 text-center font-mono-num text-emerald-800">2.742</td><td class="p-2 text-center font-mono-num text-emerald-900">13.710</td><td class="p-2">Semua titik teralokasi lengkap</td></tr>';
  }
  html += '</tbody></table></div></div>';

  // Section 3: Detail Bumbu & Resep Pengolahan
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">' +
    '<div class="flex items-center gap-2 border-b border-slate-100 pb-2.5">' +
      '<span class="w-6 h-6 rounded-lg bg-rose-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">3</span>' +
      '<h3 class="text-xs md:text-sm font-black text-slate-900 uppercase">Panduan Detail Bumbu & Resep Pengolahan (SOP Relawan MBG) - ' + dayBatch.title + '</h3>' +
    '</div>' +
    '<div class="space-y-3 text-xs text-slate-800">';

  if (currentDay === 'selasa') {
    html += '<div class="p-3 bg-amber-50/70 border border-amber-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-amber-200 pb-1">' +
          '<span class="font-black text-amber-950 text-xs">🍗 1. AYAM KATSU (2.742 POTONG - DADA FILLET 159 KG)</span>' +
          '<span class="text-[9px] font-bold bg-amber-200 text-amber-900 px-2 py-0.5 rounded-full">Seksi Protein Hewani</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Pipihkan Seragam:</strong> Fillet dada 159 kg dibersihkan urat/lemak. Jika tebal > 2 cm, iris tipis horizontal. Pipihkan dengan pemukul sampai tebal seragam +-1 cm (kunci agar cepat & matang merata).</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Potong & Hitung:</strong> Potong seragam +-58 g per potong. Timbang 10 potong pertama sebagai acuan patokan. Total 2.742 potong.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Marinasi Chiller:</strong> Campur bawang putih halus 2,40 kg dan garam + lada bubuk 2,10 kg. Lumuri ayam rata, simpan di chiller 20-30 menit.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Lapisi 3 Baskom:</strong> Siapkan terigu 21,94 kg -> telur kocok 21,94 kg -> tepung panir/panko 32,86 kg. <strong class="text-amber-800">Satu tangan khusus bahan basah, satu tangan khusus bahan kering</strong> agar tangan tidak menggumpal.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Tekan Panir & Simpan:</strong> Balur terigu (kibaskan), celup telur, gulingkan di panir dan <strong class="text-rose-700">tekan rapat</strong> agar tidak rontok saat digoreng. Susun di loyang beralas baking paper tidak bertumpuk, tutup simpan chiller.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Deep fry minyak +-170°C, goreng 5-6 potong per batch +-4-5 menit, balik sekali sampai keemasan matang (suhu inti >= 75°C), tiriskan di rak (bukan ditumpuk tertutup).</p>' +
      '</div>' +

      '<div class="p-3 bg-purple-50/70 border border-purple-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-purple-200 pb-1">' +
          '<span class="font-black text-purple-950 text-xs">🍚 2. NASI GURIH (144,21 KG BERAS / 2.739 PORSI + 3 ALERGI)</span>' +
          '<span class="text-[9px] font-bold bg-purple-200 text-purple-900 px-2 py-0.5 rounded-full">Seksi Karbohidrat</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Cuci Beras:</strong> Timbang beras 144,21 kg (1 kg = 19 porsi). Cuci lembut 2-3 kali sampai air bilasan relatif jernih, tiriskan.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Bumbu Aromatik:</strong> Memarkan 217 batang serai dengan ulekan. Geprek 2,20 kg bawang putih.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Campur Cairan Masak:</strong> Santan kental 11,51 liter + air 147,12 liter + daun salam 288 lembar + serai memar + bawang putih geprek + garam 1,40 kg. Aduk rata. Rasio total cairan masak 1 : 1,1 terhadap beras.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Aduk sekali di awal agar santan tidak menggumpal, jangan sering dibuka. Buang serai dan salam setelah matang, diamkan 5-10 menit, aduk bawah ke atas. Target +-100 g nasi matang.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• 3 Siswa Alergi Nasi:</strong> SMK 2 siswa, MTs 1 siswa tidak diberi nasi gurih. Kukus kentang +-150 g, wadah terpisah stiker khusus ALERGI NASI.</p>' +
      '</div>' +

      '<div class="p-3 bg-rose-50/70 border border-rose-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-rose-200 pb-1">' +
          '<span class="font-black text-rose-950 text-xs">🌶️ 3. SAMBAL GEPREK HIJAU (PB 2.550 PORSI - BALITA PK TANPA SAMBAL)</span>' +
          '<span class="text-[9px] font-bold bg-rose-200 text-rose-900 px-2 py-0.5 rounded-full">Baskom PB • Label SAMBAL</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Timbang Cabai & Bawang:</strong> Cabai rawit hijau 10,81 kg + cabai hijau besar 16,21 kg (total cabai 27,02 kg), bawang putih 5,03 kg, bawang merah 4,19 kg.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Bersihkan & Potong:</strong> Buang tangkai cabai, cuci bersih tiriskan, kupas bawang. Potong kasar cabai dan bawang +-1 cm. <strong class="text-rose-700">Wajib pakai sarung tangan</strong> dan jangan menyentuh mata.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Kemas & Label:</strong> Masuk wadah berlabel Sambal Geprek Hijau (PB). <strong class="text-rose-700 underline">MUTLAK JANGAN SIAPKAN UNTUK PK BALITA!</strong></p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Tumis 3-4 menit sampai layu matang (tidak boleh mentah). Ulek kasar bersama garam, gula, perasan air jeruk limau, lalu siram minyak panas 3,36 liter.</p>' +
      '</div>' +

      '<div class="p-3 bg-amber-50/70 border border-amber-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-amber-200 pb-1">' +
          '<span class="font-black text-amber-950 text-xs">🧈 4. TAHU GORENG GURIH (2.742 POTONG MATANG)</span>' +
          '<span class="text-[9px] font-bold bg-amber-200 text-amber-900 px-2 py-0.5 rounded-full">Seksi Protein Nabati</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Tiris & Tekan Kering:</strong> Buang air rendaman pabrik 90,46 kg tahu. Tekan perlahan dengan kain bersih sampai kering dan kesat agar minyak panas tidak muncrat/meletup.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Potong:</strong> Dadu/persegi seragam +-3x3x1,5 cm (target 33 g mentah -> 30 g matang susut 10%). Timbang 10 potong pertama sebagai acuan.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Rendam & Tiris:</strong> Rendam 5 menit di air garam encer + bawang putih bubuk, tiriskan lagi sampai kering sebelum diserahkan.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Minyak +-170°C, jangan terlalu penuh per batch, goreng +-6-8 menit sampai kuning keemasan dan sedikit renyah, tiriskan di rak.</p>' +
      '</div>' +

      '<div class="p-3 bg-emerald-50/70 border border-emerald-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-emerald-200 pb-1">' +
          '<span class="font-black text-emerald-950 text-xs">🥕 5. MIX VIGIE (TUMIS SAYUR CAMPUR 4 JENIS TERPISAH)</span>' +
          '<span class="text-[9px] font-bold bg-emerald-200 text-emerald-900 px-2 py-0.5 rounded-full">Seksi Sayuran</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Potong Per Jenis (4 Wadah):</strong> Wortel 29,05 kg kupas potong dadu kecil +-0,7 cm. Buncis 29,05 kg buang ujung iris serong +-2 cm. Kol putih 19,34 kg iris persegi +-2x2 cm. Jagung manis 19,34 kg dipipil dari bonggolnya.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Bumbu & Simpan Chiller:</strong> Iris tipis bawang merah dan bawang putih 2,40 kg. Simpan tiap jenis di wadah terpisah (karena waktu masuk wajan berbeda) di chiller berlabel.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Panduan Pengolahan:</strong> Tumis bawang harum, wortel + jagung 2-3 menit, lalu buncis, dan kol di menit terakhir, bumbui garam kaldu gula. Total masak +-8-10 menit, sayur masih sedikit renyah, tiriskan kuah berlebih sebelum diporsi.</p>' +
      '</div>' +

      '<div class="p-3 bg-blue-50/70 border border-blue-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-blue-200 pb-1">' +
          '<span class="font-black text-blue-950 text-xs">🍌 6. PISANG STANDAR BGN (2.742 BUAH + 22 CADANGAN)</span>' +
          '<span class="text-[9px] font-bold bg-blue-200 text-blue-900 px-2 py-0.5 rounded-full">Selesai di Persiapan</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Sortir Mulus:</strong> Pisahkan buah busuk, memar parah, kulit pecah, atau terlalu lembek. Pilih kematangan seragam.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Lap & Simpan Sejuk:</strong> Lap bersih dengan kain lembap (tidak perlu dicuci basah). Simpan di wadah berlabel di tempat sejuk (<strong class="text-rose-700">BUKAN CHILLER</strong> agar kulit tidak menghitam).</p>' +
      '</div>';
  } else {
    html += '<div class="p-3 bg-rose-50/70 border border-rose-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-rose-200 pb-1">' +
          '<span class="font-black text-rose-950 text-xs">🍗 1. AYAM RICA-RICA (PB 2.550 PORSI - PEDAS SEDANG)</span>' +
          '<span class="text-[9px] font-bold bg-rose-200 text-rose-900 px-2 py-0.5 rounded-full">Baskom PB • Label RICA</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Potong Dadu:</strong> 12.750 dadu seragam ±2x2 cm (12-14 g/dadu, tepat 5 dadu per porsi). Timbang 10 dadu pertama sebagai acuan.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Marinasi Chiller:</strong> Balur bawang putih halus + garam + lada bubuk. Diamkan 20-30 menit di chiller pendingin.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Adonan Celup:</strong> Terigu + maizena + air dingin + garam sampai tekstur seperti cat kental (menempel tipis di sendok).</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Bumbu Halus Rica:</strong> Haluskan bawang merah 8,2 kg, cabai merah keriting 9,8 kg, cabai rawit 2,9 kg, tomat 3,9 kg, bawang putih 3,1 kg, jahe & kunyit 2,4 kg.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Bumbu Aromatik:</strong> Memarkan 49 batang serai, siapkan daun jeruk purut (buang tulang daun agar tidak pahit).</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Cara Masak:</strong> Goreng ayam dadu tepung suhu 160°C hingga matang (suhu inti >= 75°C). Tumis bumbu halus bersama serai dan daun jeruk sampai tanak berminyak dan harum gurih. Masukkan ayam, aduk cepat meresap dan tidak berair.</p>' +
      '</div>' +
      '<div class="p-3 bg-blue-50/70 border border-blue-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-blue-200 pb-1">' +
          '<span class="font-black text-blue-950 text-xs">🍗 2. AYAM KECAP MANIS (PK BALITA 192 PORSI - TANPA CABAI)</span>' +
          '<span class="text-[9px] font-bold bg-blue-200 text-blue-900 px-2 py-0.5 rounded-full">Baskom PK • Label KECAP</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Potong Dadu:</strong> 960 dadu seragam ±2x2 cm (5 dadu per porsi). Simpan di baskom terpisah dari PB!</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Racikan Bumbu:</strong> Iris tipis bawang merah, cincang halus bawang putih, sisir gula merah 0,3 kg, kecap manis 1,2 L, sedikit garam & air. <strong class="text-rose-700 underline">MUTLAK TANPA CABAI!</strong></p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Cara Masak:</strong> Goreng ayam dadu hingga matang empuk. Tumis bawang hingga harum, masukkan kecap, gula merah, garam dan air. Masak hingga mengental karamel gurih meresap.</p>' +
      '</div>' +
      '<div class="p-3 bg-amber-50/70 border border-amber-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-amber-200 pb-1">' +
          '<span class="font-black text-amber-950 text-xs">🧈 3. TAHU GORENG GURIH (2.742 POTONG MATANG)</span>' +
          '<span class="text-[9px] font-bold bg-amber-200 text-amber-900 px-2 py-0.5 rounded-full">Seksi Protein Nabati</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Tiris & Tekan Kering:</strong> Buang air rendaman pabrik. Tekan perlahan dengan kain bersih sampai permukaan kering dan kesat agar minyak panas tidak muncrat/meletup.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Potong:</strong> Ukuran seragam ±3x3x1,5 cm (target 33 g mentah -> 30 g matang susut 10%).</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Rendam & Goreng:</strong> Rendam 5 menit di air garam encer + bawang putih bubuk, tiriskan lagi. Goreng suhu 160°C sampai kuning keemasan dan kesat.</p>' +
      '</div>' +
      '<div class="p-3 bg-emerald-50/70 border border-emerald-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-emerald-200 pb-1">' +
          '<span class="font-black text-emerald-950 text-xs">🥕 4. TUMIS PUTREN WORTEL (PUTREN 48 KG + WORTEL 48 KG)</span>' +
          '<span class="text-[9px] font-bold bg-emerald-200 text-emerald-900 px-2 py-0.5 rounded-full">Seksi Sayuran</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Potong:</strong> Putren kupas kelobot & rambut, belah dua memanjang, potong serong 2,5 cm. Wortel kupas, iris setengah bulan tipis 0,4 cm.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Bumbu Tumis:</strong> Iris tipis bawang merah dan bawang putih. Simpan di wadah terpisah.</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Teknik Masak Cepat (Stir-fry):</strong> Tumis bawang hingga harum. Masukkan wortel dulu, lalu putren. Masak api besar secara cepat agar sayur tetap empuk renyah dan warna cerah. Tiriskan kuah sebelum diporsi.</p>' +
      '</div>' +
      '<div class="p-3 bg-purple-50/70 border border-purple-200 rounded-xl space-y-1.5">' +
        '<div class="flex items-center justify-between border-b border-purple-200 pb-1">' +
          '<span class="font-black text-purple-950 text-xs">🍚 5. NASI & ALERGI (144,3 KG BERAS / 150 KG PO)</span>' +
          '<span class="text-[9px] font-bold bg-purple-200 text-purple-900 px-2 py-0.5 rounded-full">Seksi Karbohidrat</span>' +
        '</div>' +
        '<p class="text-[11px] leading-relaxed"><strong>• Cuci & Masak:</strong> Cuci beras 2-3 kali air mengalir sampai jernih, jangan digosok keras. Rasio air 1 : 1,1 - 1,2. Masak di rice steamer hingga pulen mekar (1 kg beras = 19 porsi).</p>' +
        '<p class="text-[11px] leading-relaxed"><strong>• 3 Siswa Alergi Nasi:</strong> Kukus kentang ±150 g, wadah terpisah stiker khusus ALERGI NASI (SMK 2 siswa, MTs 1 siswa).</p>' +
      '</div>';
  }
  html += '</div></div>';"""

targets = [
    'preview.html',
    'index.html',
    'mbg_chef_monitor/assets/web/index.html'
]

for filepath in targets:
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace schoolBatchesData.selasa
    idx_sb = content.find('const schoolBatchesData = {')
    idx_selasa_sb = content.find('  selasa: {', idx_sb)
    idx_rabu_sb = content.find('  rabu: {', idx_selasa_sb)
    if idx_selasa_sb != -1 and idx_rabu_sb != -1:
        content = content[:idx_selasa_sb] + new_selasa_batches + content[idx_rabu_sb:]
        print(f"[{filepath}] Replaced schoolBatchesData.selasa")
    else:
        print(f"[{filepath}] ERROR: Could not find schoolBatchesData.selasa")

    # 2. Replace weeklyMenuCycles.siklus1.days.selasa
    idx_wm = content.find('weeklyMenuCycles = {')
    idx_selasa_wm = content.find('      selasa: {', idx_wm)
    idx_rabu_wm = content.find('      rabu: {', idx_selasa_wm)
    if idx_selasa_wm != -1 and idx_rabu_wm != -1:
        content = content[:idx_selasa_wm] + new_selasa_menu_cycle + content[idx_rabu_wm:]
        print(f"[{filepath}] Replaced weeklyMenuCycles.siklus1.days.selasa")
    else:
        print(f"[{filepath}] ERROR: Could not find weeklyMenuCycles.selasa")

    # 3. Replace updateStickyNoteContent bumbu block
    idx_fn = content.find('function updateStickyNoteContent')
    idx_bumbu = content.find("if (currentDirectiveSubtab === 'bumbu') {", idx_fn)
    idx_end_bumbu = content.find("body.innerHTML = bumbuHtml;", idx_bumbu)
    if idx_bumbu != -1 and idx_end_bumbu != -1:
        idx_end_bumbu += len("body.innerHTML = bumbuHtml;")
        content = content[:idx_bumbu] + bumbu_sticky_code + content[idx_end_bumbu:]
        print(f"[{filepath}] Replaced updateStickyNoteContent bumbu block")
    else:
        print(f"[{filepath}] ERROR: Could not find updateStickyNoteContent bumbu block")

    # 4. Replace openFullDirectiveModal Section 2 & 3
    idx_modal = content.find('function openFullDirectiveModal')
    idx_sec2 = content.find("// Section 2: Porsi per Lokasi", idx_modal)
    idx_sec4 = content.find("// Section 4: Pos Kerja", idx_modal)
    if idx_sec2 != -1 and idx_sec4 != -1:
        content = content[:idx_sec2] + modal_sec2_3_code + "\n\n  " + content[idx_sec4:]
        print(f"[{filepath}] Replaced openFullDirectiveModal Section 2 & 3")
    else:
        print(f"[{filepath}] ERROR: Could not find openFullDirectiveModal Section 2 & 3")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{filepath}] Successfully written.")

print("All files updated successfully.")

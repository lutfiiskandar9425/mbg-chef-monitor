"""
Update preview.html, index.html, dan mbg_chef_monitor/assets/web/index.html
dengan Menu Resmi 09 - 13 November 2026 (SPPG Pekajangan 04).
"""
import re

with open('preview.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update header text and hero banner
content = content.replace('Siklus 1 (16-20 Nov)', 'Siklus 1 (09-13 Nov)')
content = content.replace('Siklus 1: 16 - 20 November 2026', 'Siklus 1: 09 - 13 November 2026')
content = content.replace('Siklus 2 (23-27 Nov)', 'Siklus 2 (16-20 Nov)')
content = content.replace('Siklus 2: 23 - 27 November 2026', 'Siklus 2: 16 - 20 November 2026')

# Update default hero title
content = content.replace(
    'Nasi Gurih + Telur Rollade Bulat + Sambal Bawang + Edamame + Kakiage + Jeruk',
    'Nasi + Ayam Rica-Rica + Ayam Kecap + Tumis Putren Wortel + Tahu Goreng + Jeruk'
)
content = content.replace(
    '3.000 Porsi',
    '2.742 Porsi'
)

# New JavaScript definition for cycle1
new_cycle1_js = '''      senin: {
        title: "Nasi + Ayam Rica-Rica + Ayam Kecap + Tumis Putren Wortel + Tahu Goreng + Jeruk",
        nutrition: "Energi 710 kkal • Protein 32 gr • Karbohidrat Kompleks & Kaya Vitamin C",
        notePersiapan: "Potong dadu ayam dada fillet (174 kg) bagi dua: rica-rica dan kecap. Potong wortel (48 kg) & putren jagung muda (48 kg) serong seragam.",
        notePengolahan: "Masak ayam rica-rica bumbu pedas aromatik daun jeruk dan ayam kecap manis gurih wijen. Tumis putren wortel renyah. Goreng tahu putih besar (2.772 pcs) hingga berkulit keemasan.",
        notePemorsian: "Ompreng sekat nasi diisi 150 gr nasi putih hangat, sekat lauk utama ayam rica/kecap berdampingan dengan tahu goreng dan tumis putren wortel. 1 butir jeruk medan (242 kg) di sekat buah steril.",
        items: [
          { name: "Jeruk Medan (isi 10-12)", category: "Buah Segar", portion: "1 butir (85 gr)", targetOrder: "242.00 kg", supplier: "PO-009/XI/2026", tare: "0.85", persiapan: "Khusus Tim Pemorsian. Sortir buah jeruk utuh segar tanpa cacat.", pengolahan: "Dilarang terkena panas/kompor dapur.", pemorsian: "Lap permukaan kulit jeruk dengan kain sanitasi kering, tata di sekat buah (2.783 butir jeruk, isi 11/kg)." },
          { name: "Tahu Putih Besar", category: "Protein Nabati", portion: "1 pcs (40 gr)", targetOrder: "2.772 pcs", supplier: "PO-010/XI/2026", tare: "0.50", persiapan: "Tiriskan tahu putih dari air perendam, potong presisi kotak seragam.", pengolahan: "Rendam air garam bawang putih, goreng minyak panas suhu 160°C hingga berkulit gurih.", pemorsian: "Tata 1 pcs tahu goreng di sekat lauk pendamping (buffer 30 pcs)." },
          { name: "Ayam Dada Fillet", category: "Protein Hewani", portion: "60 gr", targetOrder: "174.00 kg", supplier: "PO-011/XI/2026", tare: "0.85", persiapan: "Bilas ayam fillet air mengalir, potong dadu 2.5 cm, bagi untuk ayam rica-rica dan ayam kecap.", pengolahan: "Tumis ayam dengan bumbu rica cabai tomat daun jeruk dan bumbu kecap manis saus tiram minyak wijen hingga matang sempurna (suhu inti >= 75°C).", pemorsian: "Takar 60 gr ayam rica/kecap di sekat lauk utama ompreng." },
          { name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "150.00 kg", supplier: "PO-007/XI/2026", tare: "0.85", persiapan: "Cuci beras bersih 3x air mengalir, tiriskan sempurna.", pengolahan: "Takar air presisi, masak di rice steamer hingga pulen mekar matang merata.", pemorsian: "Takar 150 gr nasi putih pulen di sekat utama ompreng." },
          { name: "Wortel Segar", category: "Sayuran Segar", portion: "35 gr", targetOrder: "48.00 kg", supplier: "PO-008/XI/2026", tare: "0.50", persiapan: "Kupas kulit wortel, cuci bersih, iris serong 3 mm seragam.", pengolahan: "Tumis bersama putren dengan bawang putih bombay harum gurih, jaga kerenyahan sayur.", pemorsian: "Campur bersama tumisan putren di sekat sayur." },
          { name: "Putren (Jagung Muda)", category: "Sayuran Segar", portion: "35 gr", targetOrder: "48.00 kg", supplier: "PO-008/XI/2026", tare: "0.50", persiapan: "Kupas kulit putren, cuci bersih tiriskan, potong serong 2 bagian.", pengolahan: "Tumis stir-fry cepat bersama wortel api besar agar renyah segar.", pemorsian: "Takar 60 gr tumis putren wortel di sekat sayur ompreng." }
        ]
      },
      selasa: {
        title: "Nasi + Ayam Katsu Sambal Geprek + Tahu Goreng + Mixi Vigie + Pisang",
        nutrition: "Energi 730 kkal • Protein 33 gr • Kaya Kalium & Vitamin A",
        notePersiapan: "Fillet ayam dada (173 kg) pipihkan tebal 1 cm, marinasi bawang putih bubuk desaku (5 pouch) & chicken powder knorr (5 kg). Siapkan adonan tepung terigu segitiga (30 kg) & tepung panir jfood (20 kg).",
        notePengolahan: "Balur ayam dengan tepung panir, goreng deep frying minyak panas (104 liter) suhu 160°C hingga emas krispi. Ulek kasar sambal geprek cabai rawit hijau (7 kg) cabai hijau besar (7 kg) bawang putih (11 kg). Tumis mix vegetable (70 kg) mentega.",
        notePemorsian: "Ayam katsu krispi dipotong 3 strip disiram sambal geprek gurih di sekat lauk. Tahu goreng (2.772 pcs) mendampingi. 1 pcs pisang segar (2.762 pcs) di sekat buah kering.",
        items: [
          { name: "Ayam Dada Fillet (Katsu)", category: "Protein Hewani", portion: "60 gr", targetOrder: "173.00 kg", supplier: "PO-016/XI/2026", tare: "0.85", persiapan: "Pipihkan dada ayam fillet, marinasi bawang putih bubuk & kaldu ayam 30 menit.", pengolahan: "Balur terigu dan panir jfood, goreng deep fry suhu 160°C hingga krispi matang keemasan.", pemorsian: "Potong 3 bagian seragam, tata di sekat lauk utama." },
          { name: "Pisang Segar", category: "Buah Segar", portion: "1 pcs", targetOrder: "2.762 pcs", supplier: "PO-014/XI/2026", tare: "0.00", persiapan: "Khusus Tim Pemorsian. Sortir pisang matang mulus higienis (buffer 20 pcs).", pengolahan: "Dilarang terkena suhu panas dapur.", pemorsian: "SOP BUAH: Letakkan 1 buah pisang di sekat buah ompreng." },
          { name: "Tahu Putih Besar", category: "Protein Nabati", portion: "1 pcs (40 gr)", targetOrder: "2.772 pcs", supplier: "PO-015/XI/2026", tare: "0.50", persiapan: "Potong tahu kotak seragam, tiriskan air perendam.", pengolahan: "Goreng dalam minyak panas hingga berkulit renyah gurih.", pemorsian: "Tata 1 potong tahu goreng mendampingi katsu." },
          { name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "150.00 kg", supplier: "PO-012/XI/2026", tare: "0.85", persiapan: "Cuci beras hingga bersih 3x air mengalir.", pengolahan: "Masak di rice steamer hingga pulen standar BGN.", pemorsian: "Takar 150 gr di sekat nasi utama." },
          { name: "Mix Vegetable (Jagung, Polong, Wortel)", category: "Sayuran Segar", portion: "60 gr", targetOrder: "70.00 kg", supplier: "PO-013/XI/2026", tare: "0.50", persiapan: "Thawing mix vegetable beku higienis, tiriskan air.", pengolahan: "Tumis stir-fry mentega gurih api besar dengan bawang putih cincang.", pemorsian: "Takar 60 gr di sekat sayur ompreng." },
          { name: "Sambal Geprek Cabai Hijau", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "25.00 kg", supplier: "PO-013/XI/2026", tare: "0.50", persiapan: "Petik cabai rawit hijau, cabai hijau besar, kupas bawang putih 11 kg.", pengolahan: "Ulek kasar, siram minyak panas gurih tanak.", pemorsian: "Oleskan di atas ayam katsu krispi." }
        ]
      },
      rabu: {
        title: "Nasi + Telur Fuyunghai + Saus Fuyunghai + Tempe Goreng + Polong Wortel + Anggur Muscat",
        nutrition: "Energi 695 kkal • Protein 29 gr • Tinggi Antioksidan Alami",
        notePersiapan: "Kocok telur ayam negeri (130 kg, ~15 butir/kg), cincang kol kubis (20 kg), serut wortel (85 kg), iris daun bawang (10 ikat). Potong tempe kedelai 9 ons (112 papan) bentuk persegi.",
        notePengolahan: "Goreng adonan telur fuyunghai tebal mengembang keemasan dalam minyak banyak (134 liter). Racik saus tomat delmonte (5 jerigen) & saus sambal (3 jerigen) dengan saus tiram, kecap inggris, cuka belibis, dan maizena (5 kg). Rebus wortel dan kacang polong frozen (32 kg).",
        notePemorsian: "Sajikan fuyunghai tebal disiram saus asam manis gurih fuyunghai, tempe goreng gurih, dan sayur polong wortel. Anggur muscat hijau (171 kg, isi 63-65 butir/kg) disajikan 4-5 butir di sekat buah.",
        items: [
          { name: "Telur Fuyunghai", category: "Protein Hewani", portion: "1 potong tebal (65 gr)", targetOrder: "130.00 kg", supplier: "PO-020/XI/2026", tare: "0.85", persiapan: "Kocok telur ayam negeri, campur irisan kol dan wortel serut.", pengolahan: "Goreng dadar fuyunghai tebal mengembang suhu 165°C hingga matang sempurna.", pemorsian: "Potong porsi rapi di sekat lauk utama." },
          { name: "Tempe Kedelai (9 ons)", category: "Protein Nabati", portion: "45 gr", targetOrder: "112 papan", supplier: "PO-021/XI/2026", tare: "0.50", persiapan: "Potong tempe papan bentuk persegi seragam, marinasi ketumbar bawang.", pengolahan: "Goreng kering renyah keemasan, tiriskan minyak.", pemorsian: "Tata 1 potong tempe goreng di samping fuyunghai." },
          { name: "Anggur Muscat Segar", category: "Buah Segar", portion: "4-5 butir (60 gr)", targetOrder: "171.00 kg", supplier: "PO-019/XI/2026", tare: "0.50", persiapan: "Sortir anggur muscat hijau segar (11.115 butir, isi 63-65/kg).", pengolahan: "Bilas air mengalir steril dingin, tiriskan.", pemorsian: "Tata 4-5 butir anggur muscat di sekat buah ompreng." },
          { name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "150.00 kg", supplier: "PO-017/XI/2026", tare: "0.85", persiapan: "Cuci beras bersih tiris.", pengolahan: "Masak hingga pulen mekar standar BGN.", pemorsian: "Takar 150 gr sekat utama." },
          { name: "Sayur Polong Wortel", category: "Sayuran Segar", portion: "60 gr", targetOrder: "117.00 kg", supplier: "PO-018/XI/2026", tare: "0.50", persiapan: "Iris wortel koin 2 mm, siangi kacang polong frozen 32 kg.", pengolahan: "Tumis dengan margarin dan bawang putih kupas hingga manis renyah.", pemorsian: "Takar 60 gr di sekat sayur ompreng." },
          { name: "Saus Asam Manis Fuyunghai", category: "Bumbu / Pelengkap", portion: "25 gr", targetOrder: "45.00 kg", supplier: "PO-017/XI/2026", tare: "0.50", persiapan: "Racik saos tomat delmonte, saos sambal, saus tiram, kecap inggris, cuka belibis.", pengolahan: "Masak mendidih kentalkan dengan tepung maizena harum mengkilap.", pemorsian: "Siramkan melimpah di atas telur fuyunghai." }
        ]
      },
      kamis: {
        title: "Nasi + Lele Crispy + Sambal Bawang + Edamame + Kakiage + Kelengkeng",
        nutrition: "Energi 725 kkal • Protein 34 gr • Tinggi Kalsium & Fosfor",
        notePersiapan: "Siangi ikan lele utuh isi 10/kg (278 kg = 2.780 ekor), cuci dengan jeruk nipis (8 kg). Siapkan adonan tepung terigu segitiga (75 kg), tepung beras rose brand (25 kg), kunyit bubuk desaku (2 pouch) & ketumbar bubuk (4 pouch). Serut wortel (45 kg) & kol (40 kg) untuk kakiage.",
        notePengolahan: "Celup lele ke adonan telur pelapis (30 kg) dan tepung bumbu krispi, goreng deep fry minyak panas (71 liter) suhu 170°C sampai renyah garing krispi. Goreng kakiage bakwan sayur renyah. Rebus edamame frozen (60 kg) air garam ringan 5 menit. Ulek sambal bawang matang cabai setan (6 kg) bawang putih (9 kg) bawang merah (7 kg).",
        notePemorsian: "1 ekor lele crispy utuh disajikan bersama sambal bawang pedas, kakiage renyah, dan edamame rebus. Buah kelengkeng manis (120 kg = 9.600 butir) disajikan 4-5 butir di sekat buah.",
        items: [
          { name: "Ikan Lele Crispy Utuh", category: "Protein Hewani", portion: "1 ekor (100 gr)", targetOrder: "278.00 kg", supplier: "PO-026/XI/2026", tare: "0.85", persiapan: "Siangi 2.780 ekor lele (isi 10/kg), marinasi jeruk nipis kunyit ketumbar.", pengolahan: "Balur tepung beras & terigu krispi, goreng deep frying hingga renyah garing emas.", pemorsian: "Tata 1 ekor lele crispy utuh di sekat lauk utama." },
          { name: "Kelengkeng Manis", category: "Buah Segar", portion: "4-5 pcs (45 gr)", targetOrder: "120.00 kg", supplier: "PO-024/XI/2026", tare: "0.50", persiapan: "Sortir kelengkeng manis segar utuh (9.600 butir, isi 80/kg).", pengolahan: "Lap higienis bersih dari debu dan ranting.", pemorsian: "Tata 4-5 butir kelengkeng di sekat buah ompreng." },
          { name: "Edamame Rebus Segar", category: "Protein Nabati", portion: "40 gr", targetOrder: "60.00 kg", supplier: "PO-023/XI/2026", tare: "0.50", persiapan: "Sortir polong edamame frozen, cuci bilas air mengalir.", pengolahan: "Rebus dalam air garam ringan mendidih selama 5 menit, tiriskan.", pemorsian: "Tata 40 gr edamame di sekat lauk pendamping." },
          { name: "Kakiage (Bakwan Jepang)", category: "Sayuran Segar", portion: "50 gr", targetOrder: "85.00 kg", supplier: "PO-023/XI/2026", tare: "0.50", persiapan: "Iris wortel (45 kg) dan kol kubis (40 kg) bentuk korek api tipis.", pengolahan: "Campur tepung adonan encer es, goreng terendam minyak hingga krispi renyah.", pemorsian: "Tata 1 pcs kakiage krispi di sekat sayur ompreng." },
          { name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "150.00 kg", supplier: "PO-022/XI/2026", tare: "0.85", persiapan: "Cuci beras bersih tiris.", pengolahan: "Kukus pulen mekar standar BGN.", pemorsian: "Takar 150 gr di sekat nasi utama." },
          { name: "Sambal Bawang Pedas", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "22.00 kg", supplier: "PO-023/XI/2026", tare: "0.50", persiapan: "Kupas cabai rawit setan 6 kg, bawang merah 7 kg, bawang putih 9 kg.", pengolahan: "Ulek kasar, siram minyak panas tanak gurih harum daun jeruk.", pemorsian: "Sendokkan 15 gr mendampingi lele crispy." }
        ]
      },
      jumat: {
        title: "Nasi + Ayam Crispy Sambal Bajak + Tempe Goreng + Mixi Vigie + Anggur Merah",
        nutrition: "Energi 710 kkal • Protein 31 gr • Kaya Serat & Vitamin C",
        notePersiapan: "Potong ayam dada fillet (132 kg) ukuran porsi jumat (1.902 porsi besar + 192 porsi kecil = 2.094 porsi). Potong tempe kedelai 9 ons (85 papan) persegi. Siapkan bumbu marinasi bawang putih bubuk desaku (4 pouch) & kaldu jamur (4 pouch).",
        notePengolahan: "Balur ayam dengan tepung maizenaku (20 kg) bumbu gurih, goreng deep fry minyak panas (30 liter) hingga krispi keemasan. Goreng tempe renyah. Masak sambal bajak matang tanak cabai merah teropong (6 kg) cabai rawit setan (5 kg) bawang merah (7 kg) tomat (7 kg) gula merah (2 kg). Tumis mix vegetable (60 kg) mentega.",
        notePemorsian: "Sajikan nasi putih (103 kg beras), ayam fillet crispy disiram sambal bajak matang legit gurih, tempe goreng, dan mixi vigie sayur. Anggur china red globe (97 kg = 8.245 butir, isi 85/kg) disajikan 4-5 butir di sekat buah.",
        items: [
          { name: "Ayam Dada Fillet Crispy", category: "Protein Hewani", portion: "60 gr", targetOrder: "132.00 kg", supplier: "PO-031/XI/2026", tare: "0.85", persiapan: "Potong ayam fillet seragam porsi Jumat (2.094 porsi total), marinasi kaldu jamur bawang putih.", pengolahan: "Balur tepung maizena gurih krispi, goreng deep frying suhu 165°C hingga renyah.", pemorsian: "Tata di sekat lauk utama ompreng." },
          { name: "Tempe Kedelai (9 ons)", category: "Protein Nabati", portion: "40 gr", targetOrder: "85 papan", supplier: "PO-030/XI/2026", tare: "0.50", persiapan: "Potong tempe papan seragam, rendam air garam bawang.", pengolahan: "Goreng keemasan renyah gurih, tiriskan minyak.", pemorsian: "Tata 1 potong tempe mendampingi ayam." },
          { name: "Anggur Merah (Red Globe)", category: "Buah Segar", portion: "4-5 butir (50 gr)", targetOrder: "97.00 kg", supplier: "PO-029/XI/2026", tare: "0.50", persiapan: "Sortir buah anggur red globe utuh segar (8.245 butir, isi 85/kg).", pengolahan: "Cuci bilas air mengalir steril dingin, tiriskan.", pemorsian: "SOP BUAH: Tata 4-5 butir anggur merah di sekat buah ompreng." },
          { name: "Beras Putih", category: "Karbohidrat", portion: "150 gr", targetOrder: "103.00 kg", supplier: "PO-027/XI/2026", tare: "0.85", persiapan: "Cuci beras bersih tiris.", pengolahan: "Masak hingga pulen standar BGN untuk porsi Jumat (2.094 porsi).", pemorsian: "Takar 150 gr di sekat nasi utama." },
          { name: "Mix Vegetable (Sayur)", category: "Sayuran Segar", portion: "50 gr", targetOrder: "60.00 kg", supplier: "PO-028/XI/2026", tare: "0.50", persiapan: "Thawing mix vegetable wortel polong jagung segar.", pengolahan: "Tumis bumbu bawang putih mentega gurih api besar.", pemorsian: "Takar di sekat sayur ompreng." },
          { name: "Sambal Bajak Matang", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "20.00 kg", supplier: "PO-028/XI/2026", tare: "0.50", persiapan: "Haluskan cabai merah teropong, cabai rawit setan, bawang merah, tomat sayur, gula merah.", pengolahan: "Tumis minyak panas hingga matang tanak harum legit gurih berwarna merah tua.", pemorsian: "Sendokkan 15 gr di atas ayam crispy." }
        ]
      }'''

# Replace cycle1 days in content
pattern = r'(\s+senin:\s*\{\s*title:\s*"Nasi Gurih.*?\n\s+\},\s*jumat:\s*\{.*?\n\s+\}\s*\n\s+\})'
content = re.sub(pattern, lambda m: '\n' + new_cycle1_js + '\n    }', content, flags=re.DOTALL)

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update mbg_chef_monitor/assets/web/index.html with local tailwind reference
content_local_tw = content.replace('https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js', 'tailwindcss.min.js')
with open('mbg_chef_monitor/assets/web/index.html', 'w', encoding='utf-8') as f:
    f.write(content_local_tw)

print("SUCCESS_UPDATE_ALL_HTML_FILES")


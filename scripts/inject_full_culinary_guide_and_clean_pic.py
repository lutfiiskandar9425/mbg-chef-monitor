# -*- coding: utf-8 -*-
import os
import re

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean up personal names in HTML headers & subtitles
    content = content.replace(
        'PIC Tim: Pak Yudi & Ikbal | Total Produksi: 2.742 Porsi (13.710 Wadah)',
        'Tim Kerja: Tim Persiapan Bahan Baku • Target Produksi: 2.742 Porsi (13.710 Wadah)'
    )
    content = content.replace(
        'PIC Tim: Pak Yudi & Ikbal',
        'Tim Pelaksana: Tim Persiapan'
    )
    content = content.replace(
        'PIC Tim: Pak Yudi, Ikbal',
        'Tim Pelaksana: Tim Persiapan'
    )
    content = content.replace(
        'PIC Tim: Bu Ricky, Bu Linda, Faiz, Abidin | Masak & Uji Suhu Inti >= 75°C',
        'Tim Kerja: Tim Pengolahan (Masak) • Standar Suhu Inti >= 75°C'
    )
    content = content.replace(
        'PIC: Pak Yudi & Ikbal. ',
        ''
    )

    # 2. Update subtabs in HTML to include "Detail Bumbu"
    old_subtabs_html = """        <!-- SUB-TABS PANDUAN KERJA CHEF -->
        <div id="directive-subtabs" class="grid grid-cols-4 gap-1.5 pt-2 border-t border-emerald-200/60 text-[10px] font-extrabold">
          <button type="button" onclick="selectDirectiveSubtab('aturan')" id="subtab-btn-aturan" class="py-1.5 px-1 rounded-lg bg-emerald-700 text-white shadow-xs text-center cursor-pointer transition-all">Aturan Emas</button>
          <button type="button" onclick="selectDirectiveSubtab('pos')" id="subtab-btn-pos" class="py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">5 Pos Kerja</button>
          <button type="button" onclick="selectDirectiveSubtab('jadwal')" id="subtab-btn-jadwal" class="py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">Jadwal Mundur</button>
          <button type="button" onclick="selectDirectiveSubtab('higiene')" id="subtab-btn-higiene" class="py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">Higiene & SOP</button>
        </div>"""

    new_subtabs_html = """        <!-- SUB-TABS PANDUAN KERJA CHEF -->
        <div id="directive-subtabs" class="grid grid-cols-5 gap-1 pt-2 border-t border-emerald-200/60 text-[9px] font-extrabold">
          <button type="button" onclick="selectDirectiveSubtab('aturan')" id="subtab-btn-aturan" class="py-1.5 px-0.5 rounded-lg bg-emerald-700 text-white shadow-xs text-center cursor-pointer transition-all">Aturan Emas</button>
          <button type="button" onclick="selectDirectiveSubtab('bumbu')" id="subtab-btn-bumbu" class="py-1.5 px-0.5 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">Bumbu & Resep</button>
          <button type="button" onclick="selectDirectiveSubtab('pos')" id="subtab-btn-pos" class="py-1.5 px-0.5 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">5 Pos Kerja</button>
          <button type="button" onclick="selectDirectiveSubtab('jadwal')" id="subtab-btn-jadwal" class="py-1.5 px-0.5 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">Jadwal Mundur</button>
          <button type="button" onclick="selectDirectiveSubtab('higiene')" id="subtab-btn-higiene" class="py-1.5 px-0.5 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">Higiene & SOP</button>
        </div>"""

    if old_subtabs_html in content:
        content = content.replace(old_subtabs_html, new_subtabs_html)
        print("  -> Updated subtabs grid to 5 buttons (including Bumbu & Resep)")

    # 3. Clean up personal names in schoolBatchesData posKerja
    content = content.replace('picSerah: "Rizal (Pengolahan Umum)"', 'picSerah: "Tim Pengolahan (Seksi Karbohidrat)"')
    content = content.replace('picSerah: "Bu Ricky & Bu Linda (ProHe)"', 'picSerah: "Tim Pengolahan (Seksi Protein Hewani)"')
    content = content.replace('picSerah: "Faiz (ProNa)"', 'picSerah: "Tim Pengolahan (Seksi Protein Nabati)"')
    content = content.replace('picSerah: "Abidin (Sayur)"', 'picSerah: "Tim Pengolahan (Seksi Sayuran)"')
    content = content.replace('bersama Bu Ricky/Bu Linda', 'bersama Tim Pengolahan')
    content = content.replace('bersama Pak Yudi', 'bersama Tim Persiapan')
    content = content.replace('(Ayam ke Bu Ricky/Linda, Tahu ke Faiz, Sayur ke Abidin, Beras ke Rizal)', '(Ayam ke Seksi ProHe, Tahu ke Seksi ProNa, Sayur ke Seksi Sayuran, Beras ke Seksi Karbohidrat)')
    content = content.replace('Pak Yudi, Ikbal', 'Tim Persiapan')

    # 4. Inject Bumbu & Resep rendering inside updateStickyNoteContent and openFullDirectiveModal
    # Update subtabs styling loop to include 'bumbu'
    old_subtabs_loop = "const subtabs = ['aturan', 'pos', 'jadwal', 'higiene'];"
    new_subtabs_loop = "const subtabs = ['aturan', 'bumbu', 'pos', 'jadwal', 'higiene'];"
    if old_subtabs_loop in content:
        content = content.replace(old_subtabs_loop, new_subtabs_loop)
        print("  -> Updated subtabs loop in JS to include 'bumbu'")

    # In updateStickyNoteContent, add the bumbu branch:
    old_aturan_branch = """    if (currentDirectiveSubtab === 'aturan') {"""
    new_bumbu_branch = """    if (currentDirectiveSubtab === 'bumbu') {
      let bumbuHtml = '<div class="space-y-2 text-xs text-slate-800">' +
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
      body.innerHTML = bumbuHtml;
    } else if (currentDirectiveSubtab === 'aturan') {"""

    if old_aturan_branch in content and "currentDirectiveSubtab === 'bumbu'" not in content:
        content = content.replace(old_aturan_branch, new_bumbu_branch)
        print("  -> Injected 'bumbu' subtab rendering branch in updateStickyNoteContent")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Completed {filepath}!\n")

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']
for fp in files:
    if os.path.exists(fp):
        process_file(fp)

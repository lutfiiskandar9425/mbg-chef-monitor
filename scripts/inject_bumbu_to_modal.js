const fs = require('fs');

const bumbuHtml = `  // Section 3: Detail Bumbu & Resep Pengolahan
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">' +
    '<div class="flex items-center gap-2 border-b border-slate-100 pb-2.5">' +
      '<span class="w-6 h-6 rounded-lg bg-rose-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">3</span>' +
      '<h3 class="text-xs md:text-sm font-black text-slate-900 uppercase">Panduan Detail Bumbu & Resep Pengolahan (SOP Relawan MBG)</h3>' +
    '</div>' +
    '<div class="space-y-3 text-xs text-slate-800">' +
      '<div class="p-3 bg-rose-50/70 border border-rose-200 rounded-xl space-y-1.5">' +
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
      '</div>' +
    '</div></div>';\n\n`;

const files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html'];

files.forEach(fp => {
  if (!fs.existsSync(fp)) return;
  let text = fs.readFileSync(fp, 'utf8');
  if (text.includes('Detail Bumbu & Resep Pengolahan')) {
    console.log(fp + ' already has bumbu in modal');
    return;
  }
  const hasCrlf = text.includes('\r\n');
  let textLf = text.replace(/\r\n/g, '\n');
  const targetLf = '  // Section 3: Pos Kerja & Alur Serah Terima';

  if (textLf.includes(targetLf)) {
    const parts = textLf.split(targetLf);
    let part1 = parts[1];
    part1 = part1.replace(
      '<span class="w-6 h-6 rounded-lg bg-amber-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">3</span>',
      '<span class="w-6 h-6 rounded-lg bg-amber-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">4</span>'
    );
    part1 = part1.replace('// Section 4: Jadwal Mundur Timeline', '// Section 5: Jadwal Mundur Timeline');
    part1 = part1.replace(
      '<span class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">4</span>',
      '<span class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">5</span>'
    );
    part1 = part1.replace('// Section 5: SOP & Higiene', '// Section 6: SOP & Higiene');

    const newTextLf = parts[0] + bumbuHtml + '  // Section 4: Pos Kerja & Alur Serah Terima' + part1;
    const finalContent = hasCrlf ? newTextLf.replace(/\n/g, '\r\n') : newTextLf;
    fs.writeFileSync(fp, finalContent, 'utf8');
    console.log('Successfully updated modal in ' + fp);
  } else {
    console.log('Target not found in ' + fp);
  }
});

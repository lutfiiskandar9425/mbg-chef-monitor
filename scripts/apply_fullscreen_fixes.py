# -*- coding: utf-8 -*-
import re
import os

fullscreen_modal_html = """  <!-- MODAL FULLSCREEN BACA ARAHAN LENGKAP CHEF -->
  <div id="full-directive-modal" class="fixed inset-0 z-50 bg-white flex flex-col hidden no-print">
    <!-- Top Sticky Header -->
    <div class="bg-slate-900 text-white px-4 py-3 flex items-center justify-between border-b border-slate-800 shadow-md shrink-0">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
        <div>
          <h2 class="text-xs font-black uppercase text-white tracking-wide">DOKUMEN RESMI ARAHAN CHEF LUTFI</h2>
          <p class="text-[10px] text-slate-400 font-medium">SPPG Pekajangan 04 • Program Makan Bergizi Gratis (MBG)</p>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <a href="https://drive.google.com/file/d/1wIF4ZxNK_YzfMAoPch5MXb9AWEIL6vNX/view?usp=sharing" target="_blank" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-[10px] font-extrabold rounded-lg border border-slate-700 flex items-center gap-1 cursor-pointer">
          <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          <span>Buka PDF Drive</span>
        </a>
        <button onclick="window.print()" class="px-2.5 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white text-[10px] font-extrabold rounded-lg shadow-sm flex items-center gap-1 cursor-pointer">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
          <span>Cetak</span>
        </button>
        <button onclick="closeFullDirectiveModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center font-bold text-base cursor-pointer">✕</button>
      </div>
    </div>

    <!-- Scrollable Document Body -->
    <div id="full-directive-body" class="flex-1 overflow-y-auto p-4 md:p-8 bg-[#F8FAFC] custom-scrollbar">
      <!-- Populated dynamically by openFullDirectiveModal() -->
    </div>
  </div>"""

js_code_addition = """
// ========================================================
// FULLSCREEN DIRECTIVE READER HANDLERS
// ========================================================
function openFullDirectiveModal() {
  const modal = document.getElementById('full-directive-modal');
  const body = document.getElementById('full-directive-body');
  if (!modal || !body) return;

  const dayBatch = schoolBatchesData[currentDay] || schoolBatchesData['senin'];
  
  let html = '<div class="max-w-3xl mx-auto space-y-6 text-slate-900 pb-12">';
  
  // Header Doc
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-2 text-center">' +
    '<p class="text-[10px] font-extrabold uppercase text-slate-500 tracking-widest">Badan Gizi Nasional Republik Indonesia</p>' +
    '<h1 class="text-base md:text-lg font-black uppercase text-slate-900">SPPG PEKAJANGAN 04 - PROGRAM MAKAN BERGIZI GRATIS (MBG)</h1>' +
    '<h2 class="text-xs md:text-sm font-bold text-emerald-800 uppercase">Dokumen Resmi Panduan & Arahan Kerja - ' + dayBatch.title + '</h2>' +
    '<p class="text-xs text-slate-600 font-medium">Menu: <strong class="text-slate-800">' + dayBatch.menu + '</strong></p>' +
    '<p class="text-[11px] text-slate-500 font-medium">PIC Tim Persiapan: <strong class="text-slate-800">Pak Yudi, Ikbal</strong> • Total Produksi: <strong class="text-emerald-800 font-bold">2.742 Porsi (13.710 Wadah)</strong></p>' +
  '</div>';

  // Section 1: Aturan Emas
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">' +
    '<div class="flex items-center gap-2 border-b border-slate-100 pb-2.5">' +
      '<span class="w-6 h-6 rounded-lg bg-emerald-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">1</span>' +
      '<h3 class="text-xs md:text-sm font-black text-slate-900 uppercase">7 Aturan Emas Hari Ini (Wajib Ditaati)</h3>' +
    '</div>' +
    '<div class="space-y-2 text-xs text-slate-800 font-medium">';
  (dayBatch.aturanEmas || []).forEach((at, idx) => {
    html += '<div class="flex items-start gap-2.5 bg-emerald-50/60 p-2.5 rounded-xl border border-emerald-200/60">' +
      '<span class="w-5 h-5 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-[10px] shrink-0 mt-0.5">' + (idx + 1) + '</span>' +
      '<span class="leading-relaxed">' + at + '</span>' +
    '</div>';
  });
  html += '</div></div>';

  // Section 2: Porsi per Lokasi
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">' +
    '<div class="flex items-center gap-2 border-b border-slate-100 pb-2.5">' +
      '<span class="w-6 h-6 rounded-lg bg-blue-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">2</span>' +
      '<h3 class="text-xs md:text-sm font-black text-slate-900 uppercase">Jumlah Porsi & Distribusi Tiap Lokasi Sekolah</h3>' +
    '</div>' +
    '<div class="overflow-x-auto"><table class="w-full text-left text-xs border-collapse">' +
      '<thead class="bg-slate-100 text-slate-700 font-extrabold uppercase text-[10px]"><tr><th class="p-2">Lokasi Sekolah / Titik</th><th class="p-2 text-center">Porsi PB</th><th class="p-2 text-center">Porsi PK</th><th class="p-2 text-center">Total Porsi</th><th class="p-2 text-center">Total Wadah (x5)</th><th class="p-2">Catatan Khusus</th></tr></thead>' +
      '<tbody class="divide-y divide-slate-100 text-[11px]">' +
        '<tr><td class="p-2 font-bold text-slate-900">SMK 1 Kedungwuni</td><td class="p-2 text-center font-mono-num font-bold">1.712</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">1.712</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">8.560</td><td class="p-2 text-amber-900 font-semibold">2 Siswa Alergi Nasi (1.710 biasa + 2 karbo pengganti)</td></tr>' +
        '<tr><td class="p-2 font-bold text-slate-900">MTs Salafiyah Syafiiyah</td><td class="p-2 text-center font-mono-num font-bold">646</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">646</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">3.230</td><td class="p-2 text-amber-900 font-semibold">1 Siswa Alergi Nasi (645 biasa + 1 karbo pengganti)</td></tr>' +
        '<tr><td class="p-2 font-bold text-slate-900">Posyandu Ambokembang</td><td class="p-2 text-center font-mono-num font-bold">86</td><td class="p-2 text-center font-mono-num font-bold text-blue-700">99</td><td class="p-2 text-center font-mono-num font-bold">185</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">925</td><td class="p-2 text-blue-900 font-semibold">99 PK Balita Ayam Kecap (tidak pedas)</td></tr>' +
        '<tr><td class="p-2 font-bold text-slate-900">Posyandu Panjomblangan</td><td class="p-2 text-center font-mono-num font-bold">95</td><td class="p-2 text-center font-mono-num font-bold text-blue-700">93</td><td class="p-2 text-center font-mono-num font-bold">188</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">940</td><td class="p-2 text-blue-900 font-semibold">93 PK Balita Ayam Kecap (tidak pedas)</td></tr>' +
        '<tr><td class="p-2 font-bold text-slate-900">Sampel & Uji Organoleptik</td><td class="p-2 text-center font-mono-num font-bold">11</td><td class="p-2 text-center text-slate-400">-</td><td class="p-2 text-center font-mono-num font-bold">11</td><td class="p-2 text-center font-mono-num font-extrabold text-emerald-800">55</td><td class="p-2 text-purple-900 font-semibold">2 Sampel Arsip + 9 Uji Organoleptik QC Lab</td></tr>' +
        '<tr class="bg-slate-50 font-black text-slate-900"><td class="p-2">TOTAL PRODUKSI</td><td class="p-2 text-center font-mono-num">2.550</td><td class="p-2 text-center font-mono-num">192</td><td class="p-2 text-center font-mono-num text-emerald-800">2.742</td><td class="p-2 text-center font-mono-num text-emerald-900">13.710</td><td class="p-2">Semua titik teralokasi lengkap</td></tr>' +
      '</tbody></table></div></div>';

  // Section 3: Pos Kerja & Alur Serah Terima
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">' +
    '<div class="flex items-center gap-2 border-b border-slate-100 pb-2.5">' +
      '<span class="w-6 h-6 rounded-lg bg-amber-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">3</span>' +
      '<h3 class="text-xs md:text-sm font-black text-slate-900 uppercase">Alur 5 Pos Kerja Persiapan & Serah Terima ke Pengolahan</h3>' +
    '</div>' +
    '<div class="space-y-2">';
  (dayBatch.posKerja || []).forEach(p => {
    html += '<div class="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-1">' +
      '<div class="flex items-center justify-between">' +
        '<span class="font-extrabold text-xs text-slate-900">' + p.pos + '</span>' +
        '<span class="text-[10px] font-bold bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded-full">Serah ke: ' + p.picSerah + '</span>' +
      '</div>' +
      '<p class="text-xs text-slate-700">' + p.tugas + '</p>' +
      '<p class="text-[11px] text-slate-500 font-medium">Target Bahan: <strong class="text-slate-800">' + p.target + '</strong></p>' +
    '</div>';
  });
  html += '</div></div>';

  // Section 4: Jadwal Mundur Timeline
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-3">' +
    '<div class="flex items-center gap-2 border-b border-slate-100 pb-2.5">' +
      '<span class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">4</span>' +
      '<h3 class="text-xs md:text-sm font-black text-slate-900 uppercase">Jadwal Mundur Produksi (Timeline Dapur)</h3>' +
    '</div>' +
    '<div class="space-y-2 text-xs">';
  (dayBatch.jadwalMundur || []).forEach(j => {
    html += '<div class="flex items-start gap-3 p-3 bg-slate-50 border border-slate-200 rounded-xl">' +
      '<span class="font-mono-num font-black text-xs text-purple-900 bg-purple-100 px-2.5 py-1 rounded-lg shrink-0">' + j.waktu + '</span>' +
      '<span class="text-slate-800 leading-relaxed font-medium">' + j.kegiatan + '</span>' +
    '</div>';
  });
  html += '</div></div>';

  // Section 5: SOP & Higiene
  html += '<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-2.5 text-xs text-slate-800 leading-relaxed">' +
    '<h3 class="text-xs md:text-sm font-black text-rose-900 uppercase border-b border-slate-100 pb-2">Standar Higiene & Larangan Mutlak BGN</h3>' +
    '<p>• Cuci tangan pakai sabun minimal 20 detik sebelum mulai, setelah memegang ayam mentah, dan setiap pindah stasiun kerja.</p>' +
    '<p>• Wajib memakai masker, celemek, penutup rambut, dan sarung tangan steril.</p>' +
    '<p>• Telenan dan pisau untuk daging mentah WAJIB dipisah dari sayuran dan makanan matang.</p>' +
    '<p class="font-bold text-rose-700">• DILARANG menyentuh makanan matang dengan tangan kosong, menaruh wadah di lantai, atau menukar jatah ayam rica dan kecap.</p>' +
  '</div>';

  html += '</div>';

  body.innerHTML = html;
  modal.classList.remove('hidden');
}

function closeFullDirectiveModal() {
  const modal = document.getElementById('full-directive-modal');
  if (modal) modal.classList.add('hidden');
}
"""

def update_file(filepath):
    print(f"Upgrading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Full Directive Modal to HTML
    if "id=\"full-directive-modal\"" not in content:
        # Insert before </body> or right after print-school-modal
        target_marker = "<!-- PRINTABLE CONTAINER UNTUK LEMBAR KERJA SEKOLAH -->\n  <div id=\"printable-school-form\" class=\"hidden\">\n  </div>"
        if target_marker in content:
            content = content.replace(target_marker, target_marker + "\n\n" + fullscreen_modal_html)
            print("  -> Inserted #full-directive-modal")
        else:
            print("  -> Warning: target_marker not found for full-directive-modal")

    # 2. Add button "Buka Arahan Lengkap (Layar Penuh)" in sticky note
    old_sticky_header = '<span id="note-team-badge" class="text-[9px] font-bold bg-white text-emerald-800 px-2 py-0.5 rounded-md border border-emerald-200 shadow-2xs">Langsung Aktif</span>\n        </div>'
    new_sticky_header = """<div class="flex items-center gap-1.5">
            <span id="note-team-badge" class="text-[9px] font-bold bg-white text-emerald-800 px-2 py-0.5 rounded-md border border-emerald-200 shadow-2xs">Langsung Aktif</span>
            <button type="button" onclick="openFullDirectiveModal()" class="px-2.5 py-1 bg-emerald-800 hover:bg-emerald-900 text-white rounded-lg text-[10px] font-extrabold shadow-xs flex items-center gap-1 cursor-pointer transition-all active:scale-95" title="Buka Arahan Lengkap Layar Penuh">
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4"/></svg>
              <span>Layar Penuh</span>
            </button>
          </div>
        </div>"""

    if old_sticky_header in content and "onclick=\"openFullDirectiveModal()\"" not in content:
        content = content.replace(old_sticky_header, new_sticky_header)
        print("  -> Added Fullscreen button to Sticky Note header")

    # 3. Add responsive card layout in renderSchoolBatchSection()
    # Replace the table rendering in renderSchoolBatchSection with responsive cards
    old_table_code = """  // Items Table
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

  activeCardHtml += '</tbody></table></div>';"""

    new_table_code = """  // Items List (Responsive Mobile Cards & Table)
  activeCardHtml += '<div class="space-y-2">';
  activeLoc.items.forEach(it => {
    activeCardHtml += '<div class="p-3 bg-white border border-slate-200 rounded-xl space-y-1.5 shadow-2xs hover:border-slate-300 transition-all">' +
      '<div class="flex items-start justify-between gap-2">' +
        '<div>' +
          '<span class="font-extrabold text-xs text-slate-900 block">' + it.name + '</span>' +
          '<span class="text-[10px] text-slate-500 font-medium">Standar Porsi: <strong class="text-slate-700">' + it.perPorsi + '</strong></span>' +
        '</div>' +
        '<div class="text-right shrink-0">' +
          '<span class="font-mono-num font-black text-xs text-emerald-800 block">' + it.total + '</span>' +
          '<span class="text-[10px] font-bold text-slate-700 bg-slate-100 px-2 py-0.5 rounded-full inline-block mt-0.5 border border-slate-200">' + it.wadah + ' Wadah</span>' +
        '</div>' +
      '</div>' +
      '<div class="pt-1.5 border-t border-slate-100 text-[11px] text-slate-600 leading-snug">' +
        '<strong class="text-slate-700 font-semibold">Catatan:</strong> ' + it.note +
      '</div>' +
    '</div>';
  });
  activeCardHtml += '</div>';"""

    if old_table_code in content:
        content = content.replace(old_table_code, new_table_code)
        print("  -> Replaced squished table with responsive card layout")

    # 4. Inject openFullDirectiveModal and closeFullDirectiveModal
    if "function openFullDirectiveModal()" not in content:
        target_fn_anchor = "function closeSchoolPrintModal() {"
        if target_fn_anchor in content:
            idx = content.find(target_fn_anchor)
            end_fn = content.find("}", idx) + 1
            content = content[:end_fn] + "\n" + js_code_addition + "\n" + content[end_fn:]
            print("  -> Injected openFullDirectiveModal & closeFullDirectiveModal")
        else:
            print("  -> Warning: target_fn_anchor not found")

    # 5. Fix modal classes for mobile full screen
    # print-school-modal
    content = content.replace(
        'id="print-school-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center p-3 hidden no-print">',
        'id="print-school-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center md:p-3 hidden no-print">'
    )
    content = content.replace(
        '<div class="bg-white rounded-2xl w-full max-w-2xl max-h-[92vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden">',
        '<div class="bg-white w-full h-full md:h-auto md:max-w-2xl md:max-h-[92vh] md:rounded-2xl flex flex-col shadow-2xl border border-slate-200 overflow-hidden">'
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Completed {filepath}!\n")

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']
for fp in files:
    if os.path.exists(fp):
        update_file(fp)


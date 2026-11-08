# -*- coding: utf-8 -*-
import re
import os

def update_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS @media print
    old_css_print = """    @media print {
      body * {
        visibility: hidden;
      }
      #printable-aslap-form, #printable-aslap-form * {
        visibility: visible;
      }
      #printable-aslap-form {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        margin: 0;
        padding: 20px;
        background: white;
        color: black;
      }
      .no-print {
        display: none !important;
      }
    }"""

    new_css_print = """    @media print {
      body * {
        visibility: hidden;
      }
      #printable-aslap-form, #printable-aslap-form *,
      #printable-school-form, #printable-school-form * {
        visibility: visible;
      }
      #printable-aslap-form, #printable-school-form {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        margin: 0;
        padding: 20px;
        background: white;
        color: black;
      }
      .no-print {
        display: none !important;
      }
    }"""

    if old_css_print in content:
        content = content.replace(old_css_print, new_css_print)
        print("  -> Updated CSS @media print")
    elif "#printable-school-form" in content:
        print("  -> CSS @media print already has #printable-school-form")

    # 2. Update Sticky Note & add school-batch-section
    old_sticky_pattern = re.compile(
        r'<!-- OTOMATIS TERLAMPIR SEPERTI STICKY NOTE DARI CHEF LUTFI -->\s*<div id="sticky-chef-note".*?</div>\s*<!-- Dynamic Menu Items Container',
        re.DOTALL
    )

    new_sticky_and_batch_html = """<!-- OTOMATIS TERLAMPIR SEPERTI STICKY NOTE DARI CHEF LUTFI -->
      <div id="sticky-chef-note" class="note-paper-persiapan p-3.5 rounded-2xl transition-all shadow-xs space-y-2.5">
        <div class="flex items-start justify-between">
          <div class="flex items-center gap-2">
            <span id="note-team-icon" class="w-6 h-6 rounded-full bg-emerald-600 text-white flex items-center justify-center text-xs font-black shadow-xs">📌</span>
            <div>
              <span id="note-team-title" class="font-extrabold text-xs text-emerald-950 uppercase tracking-wide">ARAHAN RESMI CHEF LUTFI • TIM PERSIAPAN</span>
              <p id="note-team-subtitle" class="text-[10px] text-emerald-700 font-semibold">PIC Tim: Pak Yudi & Ikbal | Total Produksi: 2.742 Porsi (13.710 Wadah)</p>
            </div>
          </div>
          <span id="note-team-badge" class="text-[9px] font-bold bg-white text-emerald-800 px-2 py-0.5 rounded-md border border-emerald-200 shadow-2xs">Langsung Aktif</span>
        </div>

        <!-- SUB-TABS PANDUAN KERJA CHEF -->
        <div id="directive-subtabs" class="grid grid-cols-4 gap-1.5 pt-2 border-t border-emerald-200/60 text-[10px] font-extrabold">
          <button type="button" onclick="selectDirectiveSubtab('aturan')" id="subtab-btn-aturan" class="py-1.5 px-1 rounded-lg bg-emerald-700 text-white shadow-xs text-center cursor-pointer transition-all">Aturan Emas</button>
          <button type="button" onclick="selectDirectiveSubtab('pos')" id="subtab-btn-pos" class="py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">5 Pos Kerja</button>
          <button type="button" onclick="selectDirectiveSubtab('jadwal')" id="subtab-btn-jadwal" class="py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">Jadwal Mundur</button>
          <button type="button" onclick="selectDirectiveSubtab('higiene')" id="subtab-btn-higiene" class="py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all">Higiene & SOP</button>
        </div>

        <div id="note-team-body" class="pt-1 text-xs text-slate-800 space-y-1.5 font-medium leading-relaxed">
          <!-- Populated by JavaScript -->
        </div>
      </div>

      <!-- MODUL BATCH DISTRIBUSI SEKOLAH & LOKASI -->
      <div id="school-batch-section" class="bg-white border border-slate-200 rounded-2xl p-4 shadow-xs space-y-3.5">
        <!-- Rendered dynamically by renderSchoolBatchSection() -->
      </div>

      <!-- Dynamic Menu Items Container"""

    if old_sticky_pattern.search(content):
        content = old_sticky_pattern.sub(new_sticky_and_batch_html, content)
        print("  -> Updated Sticky Note and added school-batch-section")
    elif "id=\"school-batch-section\"" in content:
        print("  -> school-batch-section already present in HTML")

    # 3. Add Modal Cetak Lembar Kerja Sekolah
    old_print_modal_marker = "<!-- PRINTABLE CONTAINER (FOR BROWSER PRINT ENGINE) -->\n  <div id=\"printable-aslap-form\" class=\"hidden\">\n  </div>"
    
    new_school_modal_html = """<!-- PRINTABLE CONTAINER (FOR BROWSER PRINT ENGINE) -->
  <div id=\"printable-aslap-form\" class=\"hidden\">
  </div>

  <!-- MODAL CETAK LEMBAR KERJA SEKOLAH (PRINT A4) -->
  <div id=\"print-school-modal\" class=\"fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center p-3 hidden no-print\">
    <div class=\"bg-white rounded-2xl w-full max-w-2xl max-h-[92vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden\">
      <div class=\"bg-slate-900 text-white px-4 py-3 flex items-center justify-between border-b border-slate-800\">
        <div class=\"flex items-center gap-2\">
          <span class=\"text-xs font-extrabold text-white\">Lembar Kerja Tim Persiapan & Distribusi Sekolah (A4)</span>
        </div>
        <div class=\"flex items-center gap-2\">
          <button onclick=\"window.print()\" class=\"px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold flex items-center gap-1 cursor-pointer shadow-sm\">
            <svg class=\"w-3.5 h-3.5\" fill=\"none\" stroke=\"currentColor\" viewBox=\"0 0 24 24\"><path stroke-linecap=\"round\" stroke-linejoin=\"round\" stroke-width=\"2\" d=\"M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z\"/></svg>
            <span>Cetak / Print Langsung</span>
          </button>
          <button onclick=\"closeSchoolPrintModal()\" class=\"text-slate-400 hover:text-white font-bold text-sm px-2 cursor-pointer\">✕</button>
        </div>
      </div>
      
      <div class=\"p-4 overflow-y-auto bg-slate-100 flex-1 flex justify-center\">
        <div id=\"modal-school-preview\" class=\"bg-white p-5 rounded-xl shadow-sm border border-slate-200 w-full text-slate-900 text-xs space-y-3\">
        </div>
      </div>
    </div>
  </div>

  <!-- PRINTABLE CONTAINER UNTUK LEMBAR KERJA SEKOLAH -->
  <div id=\"printable-school-form\" class=\"hidden\">
  </div>"""

    if old_print_modal_marker in content and "id=\"print-school-modal\"" not in content:
        content = content.replace(old_print_modal_marker, new_school_modal_html)
        print("  -> Added print-school-modal and printable-school-form")
    elif "id=\"print-school-modal\"" in content:
        print("  -> print-school-modal already present")

    # 4. Inject JavaScript
    # We need to replace updateStickyNoteContent and add schoolBatchesData and functions
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from generate_full_batch_system import school_batches_js

    # Check if schoolBatchesData is already in content
    if "const schoolBatchesData =" not in content:
        # Find where weeklyMenuCycles ends or right after let formActiveDay
        insertion_target = "let formActiveDay = 'senin';\n"
        if insertion_target in content:
            content = content.replace(insertion_target, insertion_target + "\n" + school_batches_js + "\n")
            print("  -> Injected schoolBatchesData & helper functions")
        else:
            print("  -> Warning: insertion_target not found for schoolBatchesData")

    # Replace updateStickyNoteContent function
    old_update_sticky_pattern = re.compile(
        r'function updateStickyNoteContent\(\)\s*\{.*?function openChefRecipeModal',
        re.DOTALL
    )

    new_update_sticky_fn = """function updateStickyNoteContent() {
  const stickyNote = document.getElementById('sticky-chef-note');
  const title = document.getElementById('note-team-title');
  const subtitle = document.getElementById('note-team-subtitle');
  const body = document.getElementById('note-team-body');
  const badge = document.getElementById('note-team-badge');
  const icon = document.getElementById('note-team-icon');
  const cur = weeklyMenuCycles[currentCycle].days[currentDay];
  const dayBatch = schoolBatchesData[currentDay] || schoolBatchesData['senin'];

  if (!stickyNote || !title || !body || !cur) return;

  // Update Subtabs styling
  const subtabs = ['aturan', 'pos', 'jadwal', 'higiene'];
  subtabs.forEach(st => {
    const btn = document.getElementById('subtab-btn-' + st);
    if (!btn) return;
    const isAct = st === currentDirectiveSubtab;
    if (currentActiveStation === 'persiapan') {
      btn.className = isAct
        ? 'py-1.5 px-1 rounded-lg bg-emerald-700 text-white shadow-xs text-center cursor-pointer transition-all'
        : 'py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-emerald-900 border border-emerald-300 text-center cursor-pointer transition-all';
    } else if (currentActiveStation === 'pengolahan') {
      btn.className = isAct
        ? 'py-1.5 px-1 rounded-lg bg-amber-700 text-white shadow-xs text-center cursor-pointer transition-all'
        : 'py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-amber-900 border border-amber-300 text-center cursor-pointer transition-all';
    } else {
      btn.className = isAct
        ? 'py-1.5 px-1 rounded-lg bg-blue-700 text-white shadow-xs text-center cursor-pointer transition-all'
        : 'py-1.5 px-1 rounded-lg bg-white/80 hover:bg-white text-blue-900 border border-blue-300 text-center cursor-pointer transition-all';
    }
  });

  if (currentActiveStation === 'persiapan') {
    stickyNote.className = 'note-paper-persiapan p-3.5 rounded-2xl transition-all shadow-xs space-y-2.5';
    title.innerText = 'ARAHAN UTAMA TIM PERSIAPAN (' + currentDay.toUpperCase() + ')';
    if (subtitle) subtitle.innerText = 'PIC Tim: Pak Yudi & Ikbal | Total Produksi: 2.742 Porsi (13.710 Wadah)';
    if (badge) {
      badge.innerText = 'Langsung Aktif';
      badge.className = 'text-[9px] font-bold bg-white text-emerald-800 px-2 py-0.5 rounded-md border border-emerald-200 shadow-2xs';
    }
    if (icon) icon.className = 'w-6 h-6 rounded-full bg-emerald-600 text-white flex items-center justify-center text-xs font-black shadow-xs';

    if (currentDirectiveSubtab === 'aturan') {
      let aturanHtml = '<div class="space-y-1.5"><p class="font-extrabold text-emerald-950 text-xs">7 Aturan Emas Tim Persiapan Hari Ini:</p><div class="grid grid-cols-1 gap-1 text-[11px]">';
      (dayBatch.aturanEmas || []).forEach((at, idx) => {
        aturanHtml += '<div class="flex items-start gap-1.5 bg-white/70 p-1.5 rounded-lg border border-emerald-200/60">' +
          '<span class="w-4 h-4 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-[9px] flex-shrink-0 mt-0.5">' + (idx + 1) + '</span>' +
          '<span class="text-slate-800">' + at + '</span>' +
        '</div>';
      });
      aturanHtml += '</div></div>';
      body.innerHTML = aturanHtml;
    } else if (currentDirectiveSubtab === 'pos') {
      let posHtml = '<div class="space-y-1.5"><p class="font-extrabold text-emerald-950 text-xs">Alur 5 Pos Kerja Persiapan & Serah Terima ke Pengolahan:</p><div class="overflow-x-auto"><table class="w-full text-left text-[11px] border-collapse bg-white/80 rounded-lg overflow-hidden border border-emerald-200">';
      posHtml += '<thead class="bg-emerald-100/70 text-emerald-900 font-extrabold"><tr><th class="p-1.5">Pos Kerja</th><th class="p-1.5">Tugas Spesifik</th><th class="p-1.5">Target Bahan</th><th class="p-1.5">Serah Terima Ke</th></tr></thead><tbody class="divide-y divide-emerald-100">';
      (dayBatch.posKerja || []).forEach(p => {
        posHtml += '<tr><td class="p-1.5 font-bold text-emerald-950">' + p.pos + '</td><td class="p-1.5 text-slate-700">' + p.tugas + '</td><td class="p-1.5 font-mono-num font-bold text-emerald-900">' + p.target + '</td><td class="p-1.5 font-bold text-slate-800 bg-emerald-50/50">' + p.picSerah + '</td></tr>';
      });
      posHtml += '</tbody></table></div></div>';
      body.innerHTML = posHtml;
    } else if (currentDirectiveSubtab === 'jadwal') {
      let jadwalHtml = '<div class="space-y-1.5"><p class="font-extrabold text-emerald-950 text-xs">Jadwal Mundur Produksi (T = Jam Berangkat Lokasi Pertama):</p><div class="space-y-1 text-[11px]">';
      (dayBatch.jadwalMundur || []).forEach(j => {
        jadwalHtml += '<div class="flex items-start gap-2 bg-white/70 p-1.5 rounded-lg border border-emerald-200/60">' +
          '<span class="font-mono-num font-extrabold text-emerald-900 bg-emerald-100 px-1.5 py-0.5 rounded text-[10px] whitespace-nowrap">' + j.waktu + '</span>' +
          '<span class="text-slate-800">' + j.kegiatan + '</span>' +
        '</div>';
      });
      jadwalHtml += '</div></div>';
      body.innerHTML = jadwalHtml;
    } else {
      body.innerHTML = '<div class="space-y-1 text-[11px] bg-white/70 p-2.5 rounded-xl border border-emerald-200">' +
        '<p class="font-bold text-emerald-950">Standar Higiene & Keamanan Pangan (BGN SPPG):</p>' +
        '<p>• <strong>Cuci Tangan 20 Detik:</strong> Sebelum mulai, setelah pegang ayam mentah, dan setiap pindah pos kerja.</p>' +
        '<p>• <strong>Kelengkapan Sanitasi:</strong> Wajib masker, penutup kepala, celemek bersih, dan sarung tangan steril.</p>' +
        '<p>• <strong>Pemisahan Alat:</strong> Telenan dan pisau untuk daging mentah WAJIB terpisah dari sayuran dan buah segar.</p>' +
        '<p class="text-rose-700 font-bold">• <strong>DILARANG:</strong> Sentuh makanan matang dengan tangan kosong, menaruh wadah di lantai, atau menukar jatah ayam rica dan kecap.</p>' +
      '</div>';
    }

  } else if (currentActiveStation === 'pengolahan') {
    stickyNote.className = 'note-paper-pengolahan p-3.5 rounded-2xl transition-all shadow-xs space-y-2.5';
    title.innerText = 'ARAHAN RESMI CHEF LUTFI • TIM PENGOLAHAN (' + currentDay.toUpperCase() + ')';
    if (subtitle) subtitle.innerText = 'PIC Tim: Bu Ricky, Bu Linda, Faiz, Abidin | Masak & Uji Suhu Inti >= 75°C';
    if (badge) {
      badge.innerText = 'Suhu Inti 75°C';
      badge.className = 'text-[9px] font-bold bg-white text-amber-800 px-2 py-0.5 rounded-md border border-amber-200 shadow-2xs';
    }
    if (icon) icon.className = 'w-6 h-6 rounded-full bg-amber-600 text-white flex items-center justify-center text-xs font-black shadow-xs';

    body.innerHTML = '<div class="space-y-1 text-xs text-amber-950 font-medium">' +
      '<p class="font-bold text-amber-950">Pedoman Suhu & Standar Bumbu Masak:</p>' +
      '<p>• ' + cur.notePengolahan + '</p>' +
      '<p>• <strong>Uji Goreng 20 Dadu Ayam:</strong> Timbang matang per 5 dadu harus tepat +-60 g bersama Pak Yudi sebelum seluruh ayam digoreng.</p>' +
      '<p>• <strong>Standar Keamanan Pangan:</strong> Suhu inti daging ayam matang WAJIB minimal 75°C (cek berkala dengan termometer tusuk digital).</p>' +
      '<p>• <strong>Pemisahan Rasa:</strong> Ayam Rica (PB 2.550 porsi) pedas sedang, Ayam Kecap (PK 192 porsi balita) manis gurih TANPA cabai.</p>' +
    '</div>';

  } else {
    stickyNote.className = 'note-paper-pemorsian p-3.5 rounded-2xl transition-all shadow-xs space-y-2.5';
    title.innerText = 'ARAHAN RESMI CHEF LUTFI • TIM PEMORSIAN (' + currentDay.toUpperCase() + ')';
    if (subtitle) subtitle.innerText = 'Distribusi Ompreng 5 Sekat • Total 13.710 Wadah dalam Krat';
    if (badge) {
      badge.innerText = '13.710 Wadah';
      badge.className = 'text-[9px] font-bold bg-white text-blue-800 px-2 py-0.5 rounded-md border border-blue-200 shadow-2xs';
    }
    if (icon) icon.className = 'w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center text-xs font-black shadow-xs';

    body.innerHTML = '<div class="space-y-1 text-xs text-blue-950 font-medium">' +
      '<p class="font-bold text-blue-950">Urutan Standar Memorsi (5 Langkah):</p>' +
      '<p>1. <strong>Jeruk Medan:</strong> 1 buah per wadah, buah mulus tidak memar dilap kering (paling awal).</p>' +
      '<p>2. <strong>Nasi Putih:</strong> +-100 g hangat dari rice steamer (SMK: 2 siswa alergi karbo non-nasi, MTs: 1 siswa alergi non-nasi).</p>' +
      '<p>3. <strong>Tumis Putren Wortel:</strong> 30 g tiris kuah, warna sayur cerah renyah.</p>' +
      '<p>4. <strong>Tahu Goreng:</strong> 1 potong (30 g) kesat tidak berminyak.</p>' +
      '<p>5. <strong>Ayam Rica / Kecap (PALING AKHIR):</strong> 5 dadu (60 g). Tunggu uap panas turun sebelum ditutup agar tidak lembek.</p>' +
    '</div>';
  }

  renderSchoolBatchSection();
}

function openChefRecipeModal"""

    if old_update_sticky_pattern.search(content):
        content = old_update_sticky_pattern.sub(new_update_sticky_fn, content)
        print("  -> Replaced updateStickyNoteContent successfully")
    else:
        print("  -> Warning: old_update_sticky_pattern not matched")

    # 5. Ensure selectDay and initApp calls renderSchoolBatchSection
    if "renderSchoolBatchSection();" not in content:
        content = content.replace("renderWeeklyMenu();", "renderWeeklyMenu();\n  renderSchoolBatchSection();")
        print("  -> Added renderSchoolBatchSection() calls")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Done processing {filepath}!\n")

files = [
    'preview.html',
    'index.html',
    'mbg_chef_monitor/assets/web/index.html'
]

for fp in files:
    if os.path.exists(fp):
        update_file(fp)
    else:
        print(f"File not found: {fp}")

# -*- coding: utf-8 -*-
import os
import re

camera_html_inputs_and_buttons = """        <!-- REAL CAMERA CAPTURE INPUTS (COMPATIBLE WITH IPHONE / ANDROID / LAPTOP) -->
        <input type="file" id="scale-camera-input" accept="image/*" capture="environment" class="hidden" onchange="handleScalePhoto(event)">
        <input type="file" id="scale-gallery-input" accept="image/*" class="hidden" onchange="handleScalePhoto(event)">

        <!-- TOMBOL AMBIL FOTO BUKTI TIMBANGAN -->
        <div class="pt-3 border-t border-slate-800/80 space-y-2">
          <div class="grid grid-cols-2 gap-2">
            <button type="button" onclick="openScaleCamera()" class="py-2.5 px-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98">
              <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              <span>Buka Kamera (Foto)</span>
            </button>
            <button type="button" onclick="openScaleGallery()" class="py-2.5 px-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98">
              <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
              <span>Pilih dari Galeri</span>
            </button>
          </div>

          <!-- CONTAINER PREVIEW FOTO BUKTI TIMBANGAN -->
          <div id="scale-photo-preview-container" class="hidden bg-slate-900/90 border border-emerald-500/40 p-2.5 rounded-2xl flex items-center justify-between gap-3 text-left">
            <div class="flex items-center gap-2.5 overflow-hidden">
              <img id="scale-photo-preview-img" src="" alt="Bukti Foto Timbangan" onclick="viewCurrentPhotoModal()" class="w-14 h-14 object-cover rounded-xl border border-emerald-400/50 shadow-sm cursor-pointer hover:opacity-90 shrink-0">
              <div class="min-w-0">
                <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 text-[10px] font-extrabold border border-emerald-500/30">
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                  Foto Timbangan Terlampir
                </span>
                <p id="scale-photo-timestamp" class="text-[10px] text-slate-400 font-mono-num mt-0.5">Waktu: -</p>
                <p class="text-[9px] text-slate-500">Klik gambar untuk memperbesar</p>
              </div>
            </div>
            <div class="flex flex-col gap-1 shrink-0">
              <button type="button" onclick="viewCurrentPhotoModal()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-400 text-[10px] font-bold rounded-lg border border-slate-700 cursor-pointer">Lihat</button>
              <button type="button" onclick="removeScalePhoto()" class="px-2 py-1 bg-rose-950/40 hover:bg-rose-900/60 text-rose-300 text-[10px] font-bold rounded-lg border border-rose-800/50 cursor-pointer">Hapus</button>
            </div>
          </div>
        </div>"""

photo_modal_html = """  <!-- MODAL VIEWER FOTO BUKTI TIMBANGAN (FULL RESOLUSI) -->
  <div id="photo-viewer-modal" class="fixed inset-0 bg-slate-950/90 z-50 flex items-center justify-center p-3 hidden no-print" onclick="closePhotoModal()">
    <div class="bg-slate-900 border border-slate-700 max-w-lg w-full rounded-3xl overflow-hidden shadow-2xl flex flex-col max-h-[92vh]" onclick="event.stopPropagation()">
      <div class="px-4 py-3 bg-slate-950 border-b border-slate-800 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
          <h3 id="photo-viewer-title" class="text-xs font-bold text-white uppercase tracking-wide">Foto Bukti Indikator Timbangan</h3>
        </div>
        <button type="button" onclick="closePhotoModal()" class="w-7 h-7 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center text-xs font-bold cursor-pointer">✕</button>
      </div>
      <div class="p-3 bg-black flex items-center justify-center overflow-auto flex-1 max-h-[70vh]">
        <img id="photo-viewer-img" src="" alt="Detail Foto Bukti Timbangan" class="max-w-full max-h-[65vh] object-contain rounded-xl shadow-lg">
      </div>
      <div class="px-4 py-2.5 bg-slate-950 border-t border-slate-800 flex items-center justify-between text-xs">
        <span id="photo-viewer-subtext" class="text-slate-400 text-[11px]">Dokumentasi Fisik Indikator Timbangan</span>
        <button type="button" onclick="closePhotoModal()" class="px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs cursor-pointer">Tutup</button>
      </div>
    </div>
  </div>
"""

camera_js_code = """let currentScalePhoto = null;
let currentScalePhotoTime = '';

function openScaleCamera() {
  const input = document.getElementById('scale-camera-input');
  if (input) {
    input.value = '';
    input.click();
  }
}

function openScaleGallery() {
  const input = document.getElementById('scale-gallery-input');
  if (input) {
    input.value = '';
    input.click();
  }
}

// Kompatibilitas tombol triggerCameraOCR yang lama
function triggerCameraOCR() {
  openScaleCamera();
}

function handleScalePhoto(event) {
  const file = event.target.files && event.target.files[0];
  if (!file) return;

  showToast('Memproses foto timbangan...');

  const reader = new FileReader();
  reader.onload = function(e) {
    const rawData = e.target.result;
    
    // Kompresi dan optimasi ukuran foto via Canvas (agar aman di memori iPhone/Android)
    const img = new Image();
    img.onload = function() {
      const maxDim = 1200;
      let width = img.width;
      let height = img.height;

      if (width > maxDim || height > maxDim) {
        if (width > height) {
          height = Math.round((height * maxDim) / width);
          width = maxDim;
        } else {
          width = Math.round((width * maxDim) / height);
          height = maxDim;
        }
      }

      const canvas = document.createElement('canvas');
      canvas.width = width;
      canvas.height = height;
      const ctx = canvas.getContext('2d');
      ctx.drawImage(img, 0, 0, width, height);

      currentScalePhoto = canvas.toDataURL('image/jpeg', 0.82);
      const now = new Date();
      currentScalePhotoTime = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' }) + ' WIB';

      renderScalePhotoPreview();
      showToast('Foto timbangan berhasil dilampirkan!');
    };
    img.src = rawData;
  };
  reader.readAsDataURL(file);
}

function renderScalePhotoPreview() {
  const container = document.getElementById('scale-photo-preview-container');
  const imgElem = document.getElementById('scale-photo-preview-img');
  const timeElem = document.getElementById('scale-photo-timestamp');

  if (!container || !imgElem) return;

  if (currentScalePhoto) {
    imgElem.src = currentScalePhoto;
    if (timeElem) timeElem.innerText = 'Waktu Foto: ' + (currentScalePhotoTime || '-');
    container.classList.remove('hidden');
  } else {
    imgElem.src = '';
    container.classList.add('hidden');
  }
}

function removeScalePhoto() {
  currentScalePhoto = null;
  currentScalePhotoTime = '';
  renderScalePhotoPreview();
  showToast('Foto timbangan dihapus');
}

function viewCurrentPhotoModal() {
  if (!currentScalePhoto) return;
  const itemName = document.getElementById('input-item')?.value || 'Bahan Timbangan';
  const nettoVal = document.getElementById('input-netto')?.value || '0.00';
  viewPhotoModal(currentScalePhoto, 'Foto Indikator: ' + itemName, 'Berat Netto: ' + nettoVal + ' kg • ' + (currentScalePhotoTime || ''));
}

function viewPhotoModal(imgSrc, title, subtext) {
  const modal = document.getElementById('photo-viewer-modal');
  const img = document.getElementById('photo-viewer-img');
  const titleElem = document.getElementById('photo-viewer-title');
  const subtextElem = document.getElementById('photo-viewer-subtext');

  if (!modal || !img) return;

  img.src = imgSrc;
  if (titleElem) titleElem.innerText = title || 'Foto Bukti Indikator Timbangan';
  if (subtextElem) subtextElem.innerText = subtext || 'Dokumentasi Fisik Indikator Timbangan';

  modal.classList.remove('hidden');
}

function closePhotoModal() {
  const modal = document.getElementById('photo-viewer-modal');
  if (modal) modal.classList.add('hidden');
}"""

old_camera_button_regex = re.compile(r'<!-- TOMBOL FOTO KAMERA OCR \(PROPRIETARY MBG ENGINE\) -->\s*<div class="pt-3 border-t border-slate-800/80 flex items-center justify-center gap-2">\s*<button onclick="triggerCameraOCR\(\)"[\s\S]*?<\/button>\s*<\/div>', re.IGNORECASE)

old_trigger_ocr_regex = re.compile(r'function triggerCameraOCR\(\) \{[\s\S]*?showToast\(\'Timbangan Terdeteksi: \' \+ detectedNetto \+ \' kg\'\);\s*\}, 700\);\s*\}', re.IGNORECASE)

old_add_to_cart_regex = re.compile(r'const newItem = \{\s*id: "cart_" \+ Date\.now\(\),\s*timestamp: timeStr,\s*team: team,\s*category: category,\s*name: name,\s*bruto: bruto,\s*tara: tara,\s*netto: netto,\s*catatan: catatan,\s*synced: false\s*\};\s*stagingItems\.unshift\(newItem\);\s*renderStagingList\(\);\s*showToast\(\'Item berhasil dimasukkan ke keranjang!\'\);\s*switchScreen\(\'staging\'\);', re.IGNORECASE)

new_add_to_cart = """  const newItem = {
    id: "cart_" + Date.now(),
    timestamp: timeStr,
    team: team,
    category: category,
    name: name,
    bruto: bruto,
    tara: tara,
    netto: netto,
    catatan: catatan,
    foto: currentScalePhoto,
    fotoTime: currentScalePhotoTime,
    synced: false
  };

  stagingItems.unshift(newItem);
  currentScalePhoto = null;
  currentScalePhotoTime = '';
  renderScalePhotoPreview();
  renderStagingList();
  showToast('Item & bukti foto berhasil masuk ke keranjang!');
  switchScreen('staging');"""

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace camera button in screen-home
    if old_camera_button_regex.search(content):
        content = old_camera_button_regex.sub(camera_html_inputs_and_buttons, content, count=1)
        print(f"[{fn}] Replaced camera HTML inputs & preview buttons.")
    else:
        print(f"[{fn}] Warning: Old camera button regex not matched.")

    # 2. Add photo modal if not present
    if 'id="photo-viewer-modal"' not in content:
        idx_edit_modal = content.find('<!-- MODAL EDIT ITEM KERANJANG -->')
        if idx_edit_modal != -1:
            content = content[:idx_edit_modal] + photo_modal_html + "\n  " + content[idx_edit_modal:]
            print(f"[{fn}] Added photo-viewer-modal before edit-cart-modal.")
        else:
            print(f"[{fn}] Warning: Could not find insert position for photo-viewer-modal.")

    # 3. Replace triggerCameraOCR JS
    if old_trigger_ocr_regex.search(content):
        content = old_trigger_ocr_regex.sub(camera_js_code, content, count=1)
        print(f"[{fn}] Replaced triggerCameraOCR with real camera & photo JS functions.")
    else:
        print(f"[{fn}] Warning: Old triggerCameraOCR regex not matched.")

    # 4. Update addToStagingCart
    if old_add_to_cart_regex.search(content):
        content = old_add_to_cart_regex.sub(new_add_to_cart, content, count=1)
        print(f"[{fn}] Updated addToStagingCart to save photo.")
    else:
        print(f"[{fn}] Warning: old_add_to_cart_regex not matched.")

    # 5. Update renderStagingList to show photo thumbnail
    old_card_middle = "(item.catatan ? '<p class=\"text-[10px] text-slate-600 bg-slate-50 p-1.5 rounded-lg border border-slate-100 font-medium\">📝 ' + item.catatan + '</p>' : '') +"
    new_card_middle = """(item.catatan ? '<p class="text-[10px] text-slate-600 bg-slate-50 p-1.5 rounded-lg border border-slate-100 font-medium">📝 ' + item.catatan + '</p>' : '') +
    (item.foto ? '<div class="flex items-center gap-2 py-1.5 px-2 bg-emerald-50/70 border border-emerald-200/80 rounded-xl mt-1.5">' +
      '<img src="' + item.foto + '" onclick="viewPhotoModal(\\'' + item.foto + '\\', \\'Bukti Foto: ' + item.name.replace(/'/g, "\\\\'") + '\\', \\'Netto: ' + item.netto.toFixed(2) + ' kg • ' + (item.fotoTime || '') + '\\')" class="w-11 h-11 object-cover rounded-lg border border-emerald-400 shadow-2xs cursor-pointer hover:opacity-90 shrink-0" title="Klik untuk perbesar foto bukti timbangan">' +
      '<div class="min-w-0 text-[10px]">' +
        '<span class="font-extrabold text-emerald-800 flex items-center gap-1"><svg class="w-3 h-3 text-emerald-600 inline shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> Bukti Foto Timbangan</span>' +
        '<p class="text-slate-500 font-mono-num text-[9px]">' + (item.fotoTime || 'Terekam Kamera') + '</p>' +
      '</div>' +
    '</div>' : '') +"""

    if old_card_middle in content:
        content = content.replace(old_card_middle, new_card_middle, 1)
        print(f"[{fn}] Added photo thumbnail to staging card list.")
    else:
        print(f"[{fn}] Warning: old_card_middle not found in renderStagingList.")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{fn}] Saved successfully.")

print("All files updated with Camera & Photo proof capabilities.")

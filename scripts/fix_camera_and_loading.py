# -*- coding: utf-8 -*-
import os
import re

nested_camera_section_html = """        <!-- REAL CAMERA CAPTURE INPUTS & DIRECT BUTTONS -->
        <div class="pt-3 border-t border-slate-800/80 space-y-2">
          <div class="grid grid-cols-2 gap-2">
            <!-- Tombol Buka Kamera (Nested Input Langsung) -->
            <label class="py-2.5 px-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98 select-none">
              <input type="file" id="scale-camera-input" accept="image/*" capture="environment" class="sr-only" onchange="handleScalePhoto(event)">
              <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              <span>Buka Kamera (Foto)</span>
            </label>

            <!-- Tombol Pilih dari Galeri (Nested Input Langsung) -->
            <label class="py-2.5 px-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98 select-none">
              <input type="file" id="scale-gallery-input" accept="image/*" class="sr-only" onchange="handleScalePhoto(event)">
              <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
              <span>Pilih dari Galeri</span>
            </label>
          </div>

          <!-- Tombol Foto Indikator Digital (Solusi 1-Tap Tanpa Hambatan) & Kamera Live -->
          <div class="grid grid-cols-2 gap-2 pt-0.5">
            <button type="button" onclick="useDigitalScaleSamplePhoto()" class="py-2 px-2 bg-amber-500/10 hover:bg-amber-500/20 text-amber-300 border border-amber-500/30 rounded-xl text-[11px] font-extrabold flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98">
              <svg class="w-3.5 h-3.5 text-amber-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
              <span>Foto Indikator Digital</span>
            </button>

            <button type="button" onclick="openCameraOptionsModal()" class="py-2 px-2 bg-slate-800/80 hover:bg-slate-800 text-teal-300 border border-slate-700 rounded-xl text-[11px] font-bold flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98">
              <svg class="w-3.5 h-3.5 text-teal-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
              <span>Kamera Live (Webcam)</span>
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

modal_nested_camera_options = """  <!-- MODAL PILIHAN SUMBER FOTO TIMBANGAN (ACTION SHEET) -->
  <div id="camera-options-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-end sm:items-center justify-center p-0 sm:p-4 hidden no-print" onclick="closeCameraOptionsModal(event)">
    <div class="bg-white rounded-t-3xl sm:rounded-3xl w-full max-w-sm p-5 shadow-2xl border border-slate-200 space-y-4 text-left" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between border-b border-slate-100 pb-2.5">
        <div>
          <h3 class="text-xs font-black uppercase text-slate-900 tracking-wide">Pilih Metode Bukti Foto Timbangan</h3>
          <p class="text-[10px] text-slate-500">Pilih metode pengambilan dokumentasi fisik</p>
        </div>
        <button type="button" onclick="closeCameraOptionsModal()" class="w-7 h-7 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center text-xs font-bold cursor-pointer">✕</button>
      </div>

      <div class="space-y-2 text-xs">
        <!-- Opsi 1: Kamera HP (Native Nested) -->
        <label class="w-full p-3 bg-emerald-50/70 hover:bg-emerald-100/70 border border-emerald-200 rounded-2xl flex items-center gap-3 cursor-pointer transition-all">
          <input type="file" accept="image/*" capture="environment" class="sr-only" onchange="closeCameraOptionsModal(); handleScalePhoto(event);">
          <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center shrink-0 shadow-sm">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <div class="flex-1 min-w-0">
            <span class="font-extrabold text-slate-900 block text-xs">Kamera HP (Rana Belakang)</span>
            <span class="text-[10px] text-slate-500">Langsung membuka kamera iPhone / Android Anda</span>
          </div>
        </label>

        <!-- Opsi 2: Galeri / File (Nested) -->
        <label class="w-full p-3 bg-slate-50 hover:bg-slate-100 border border-slate-200 rounded-2xl flex items-center gap-3 cursor-pointer transition-all">
          <input type="file" accept="image/*" class="sr-only" onchange="closeCameraOptionsModal(); handleScalePhoto(event);">
          <div class="w-10 h-10 rounded-xl bg-slate-800 text-white flex items-center justify-center shrink-0 shadow-sm">
            <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
          </div>
          <div class="flex-1 min-w-0">
            <span class="font-extrabold text-slate-900 block text-xs">Pilih Foto dari Galeri / Album</span>
            <span class="text-[10px] text-slate-500">Pilih berkas foto timbangan yang sudah tersimpan</span>
          </div>
        </label>

        <!-- Opsi 3: Live In-App Camera Viewfinder -->
        <button type="button" onclick="startInAppLiveCamera()" class="w-full p-3 bg-teal-50/70 hover:bg-teal-100/70 border border-teal-200 rounded-2xl flex items-center gap-3 cursor-pointer transition-all text-left">
          <div class="w-10 h-10 rounded-xl bg-teal-600 text-white flex items-center justify-center shrink-0 shadow-sm">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
          </div>
          <div class="flex-1 min-w-0">
            <span class="font-extrabold text-slate-900 block text-xs">Kamera Live di Peramban (Webcam)</span>
            <span class="text-[10px] text-slate-500">Tampilkan jendela video live langsung di layar</span>
          </div>
        </button>

        <!-- Opsi 4: Simulasi Foto Timbangan Digital -->
        <button type="button" onclick="useDigitalScaleSamplePhoto()" class="w-full p-3 bg-amber-50/70 hover:bg-amber-100/70 border border-amber-200 rounded-2xl flex items-center gap-3 cursor-pointer transition-all text-left">
          <div class="w-10 h-10 rounded-xl bg-amber-600 text-white flex items-center justify-center shrink-0 shadow-sm">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
          </div>
          <div class="flex-1 min-w-0">
            <span class="font-extrabold text-slate-900 block text-xs">Gunakan Foto Indikator Digital (Cepat)</span>
            <span class="text-[10px] text-slate-500">Otomatis buat foto bukti timbangan digital sesuai angka saat ini</span>
          </div>
        </button>
      </div>
    </div>
  </div>"""

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace screen-home camera section
    idx_cam_start = content.find('<!-- REAL CAMERA CAPTURE INPUTS')
    if idx_cam_start != -1:
        idx_cam_end = content.find('<!-- INPUT FORM DETAIL PENIMBANGAN -->', idx_cam_start)
        idx_div_end = content.rfind('</div>', idx_cam_start, idx_cam_end)
        content = content[:idx_cam_start] + nested_camera_section_html + "\n      " + content[idx_div_end:]
        print(f"[{fn}] Replaced camera section with nested input labels.")

    # 2. Replace camera-options-modal
    idx_opt_start = content.find('<!-- MODAL PILIHAN SUMBER FOTO TIMBANGAN (ACTION SHEET) -->')
    if idx_opt_start != -1:
        idx_opt_end = content.find('<!-- MODAL LIVE IN-APP CAMERA VIEWFINDER -->', idx_opt_start)
        if idx_opt_end != -1:
            content = content[:idx_opt_start] + modal_nested_camera_options + "\n\n  " + content[idx_opt_end:]
            print(f"[{fn}] Replaced camera-options-modal with nested inputs.")

    # 3. Cache buster in forceRefreshApp:
    # Ensure forceRefreshApp resets UI and loads fresh URL with timestamp
    old_replace = "window.location.replace(cleanUrl + '?v=' + Date.now());"
    new_replace = "window.location.href = cleanUrl + '?t=' + Date.now();"
    if old_replace in content:
        content = content.replace(old_replace, new_replace)
        print(f"[{fn}] Updated forceRefreshApp reload mechanism.")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{fn}] Successfully updated.")

# Also update mbg_chef_monitor/lib/main.dart for safety timeout
main_dart_path = 'mbg_chef_monitor/lib/main.dart'
if os.path.exists(main_dart_path):
    with open(main_dart_path, 'r', encoding='utf-8') as f:
        dart_code = f.read()
    
    # Add a safety 3-second timeout to turn off _isLoading if onPageFinished takes too long
    old_load = """  Future<void> _loadFreshUrl() async {
    final timestamp = DateTime.now().millisecondsSinceEpoch;
    final freshUrl = '$_baseUrl?v=$timestamp';
    await _controller.loadRequest(Uri.parse(freshUrl));
  }"""

    new_load = """  Future<void> _loadFreshUrl() async {
    final timestamp = DateTime.now().millisecondsSinceEpoch;
    final freshUrl = '$_baseUrl?v=$timestamp';
    // Timeout pengaman agar loading indikator tidak macet di HP
    Future.delayed(const Duration(seconds: 3), () {
      if (mounted && _isLoading) {
        setState(() {
          _isLoading = false;
        });
      }
    });
    await _controller.loadRequest(Uri.parse(freshUrl));
  }"""

    if old_load in dart_code:
        dart_code = dart_code.replace(old_load, new_load)
        with open(main_dart_path, 'w', encoding='utf-8') as f:
            f.write(dart_code)
        print("Updated main.dart with loading safety timeout.")

print("All updates completed successfully.")

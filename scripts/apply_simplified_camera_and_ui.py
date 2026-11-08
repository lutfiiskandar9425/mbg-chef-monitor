# -*- coding: utf-8 -*-
import os
import re

simple_camera_section_html = """        <!-- BUKTI FOTO TIMBANGAN (SIMPEL & ELEGAN) -->
        <div class="pt-3 border-t border-slate-800/80 space-y-2">
          <!-- Input File Tersembunyi (Standar Browser & Seluler) -->
          <input type="file" id="scale-camera-input" accept="image/*" style="display: none;" onchange="handleScalePhoto(event)">

          <!-- Tombol Aksi Foto (Tampil Saat Belum Ada Foto) -->
          <div id="scale-photo-action-buttons" class="grid grid-cols-2 gap-2">
            <!-- Tombol 1: Buka Kamera / Galeri -->
            <button type="button" onclick="triggerDirectCameraUpload()" class="py-2.5 px-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white rounded-xl text-xs font-black shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98">
              <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              <span>Buka Kamera (Foto)</span>
            </button>

            <!-- Tombol 2: Foto Digital Cepat (1-Sentuhan) -->
            <button type="button" onclick="useDigitalScaleSamplePhoto()" class="py-2.5 px-2 bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-500/30 rounded-xl text-xs font-bold shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98">
              <svg class="w-4 h-4 text-amber-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
              <span>Foto Digital Cepat</span>
            </button>
          </div>

          <!-- CONTAINER PREVIEW FOTO BUKTI TIMBANGAN (Tampil Saat Sudah Ada Foto) -->
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
              <button type="button" onclick="viewCurrentPhotoModal()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-emerald-400 text-[10px] font-bold rounded-lg border border-slate-700 cursor-pointer">Lihat</button>
              <button type="button" onclick="removeScalePhoto()" class="px-2.5 py-1 bg-rose-950/40 hover:bg-rose-900/60 text-rose-300 text-[10px] font-bold rounded-lg border border-rose-800/50 cursor-pointer">Hapus</button>
            </div>
          </div>
        </div>"""

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace camera section in screen-home
    # Pattern starts with <!-- REAL CAMERA CAPTURE INPUTS or <!-- BUKTI FOTO TIMBANGAN
    idx_cam_start = content.find('<!-- REAL CAMERA CAPTURE INPUTS')
    if idx_cam_start == -1:
        idx_cam_start = content.find('<!-- BUKTI FOTO TIMBANGAN')
    
    if idx_cam_start != -1:
        idx_cam_end = content.find('<!-- INPUT FORM DETAIL PENIMBANGAN -->', idx_cam_start)
        idx_div_end = content.rfind('</div>', idx_cam_start, idx_cam_end)
        content = content[:idx_cam_start] + simple_camera_section_html + "\n      " + content[idx_div_end:]
        print(f"[{fn}] Replaced camera section with 2 ultra-simple buttons.")

    # 2. Add triggerDirectCameraUpload and update renderScalePhotoPreview in JS
    js_needle = "function renderScalePhotoPreview() {"
    if js_needle in content:
        # Check if triggerDirectCameraUpload is already present
        if "function triggerDirectCameraUpload()" not in content:
            new_fn = """function triggerDirectCameraUpload() {
  const input = document.getElementById('scale-camera-input');
  if (input) {
    input.value = '';
    input.click();
  }
}

function renderScalePhotoPreview() {
  const container = document.getElementById('scale-photo-preview-container');
  const actionButtons = document.getElementById('scale-photo-action-buttons');
  const imgElem = document.getElementById('scale-photo-preview-img');
  const timeElem = document.getElementById('scale-photo-timestamp');

  if (!container || !imgElem) return;

  if (currentScalePhoto) {
    imgElem.src = currentScalePhoto;
    if (timeElem) timeElem.innerText = 'Waktu Foto: ' + (currentScalePhotoTime || '-');
    container.classList.remove('hidden');
    if (actionButtons) actionButtons.classList.add('hidden');
  } else {
    imgElem.src = '';
    container.classList.add('hidden');
    if (actionButtons) actionButtons.classList.remove('hidden');
  }
}"""
            # Replace the old renderScalePhotoPreview block
            end_old = content.find("function removeScalePhoto()", content.find(js_needle))
            if end_old != -1:
                content = content[:content.find(js_needle)] + new_fn + "\n\n" + content[end_old:]
                print(f"[{fn}] Added triggerDirectCameraUpload and updated renderScalePhotoPreview.")

    # 3. Remove camera-options-modal if present
    idx_modal_start = content.find('<!-- MODAL PILIHAN SUMBER FOTO TIMBANGAN (ACTION SHEET) -->')
    if idx_modal_start != -1:
        idx_modal_end = content.find('<!-- MODAL LIVE IN-APP CAMERA VIEWFINDER -->', idx_modal_start)
        if idx_modal_end != -1:
            content = content[:idx_modal_start] + content[idx_modal_end:]
            print(f"[{fn}] Removed confusing camera-options-modal.")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{fn}] Successfully written.")

# 4. Now update mbg_chef_monitor/lib/main.dart
main_dart_path = 'mbg_chef_monitor/lib/main.dart'
if os.path.exists(main_dart_path):
    with open(main_dart_path, 'r', encoding='utf-8') as f:
        dart_code = f.read()

    # Replace the body Stack to remove RefreshIndicator gesture conflict and blocking overlay
    old_body_stack = """              RefreshIndicator(
                color: const Color(0xFF0F172A),
                onRefresh: _refreshData,
                child: WebViewWidget(controller: _controller),
              ),
              if (_isLoading)
                Container(
                  color: Colors.white.withOpacity(0.4),
                  child: const Center(
                    child: CircularProgressIndicator(
                      color: Color(0xFF0F172A),
                    ),
                  ),
                ),"""

    new_body_stack = """              WebViewWidget(controller: _controller),
              if (_isLoading)
                const Positioned(
                  top: 0,
                  left: 0,
                  right: 0,
                  child: LinearProgressIndicator(
                    minHeight: 3,
                    color: Color(0xFF059669),
                    backgroundColor: Colors.transparent,
                  ),
                ),"""

    if old_body_stack in dart_code:
        dart_code = dart_code.replace(old_body_stack, new_body_stack)
        print("Updated main.dart body with smooth non-blocking WebView.")

    # Add onPlatformPermissionRequest to NavigationDelegate
    old_nav = """        NavigationDelegate(
          onPageStarted: (String url) {
            if (mounted) {
              setState(() {
                _isLoading = true;
              });
            }
          },"""

    new_nav = """        NavigationDelegate(
          onPlatformPermissionRequest: (PlatformPermissionRequest request) {
            request.grant();
          },
          onPageStarted: (String url) {
            if (mounted) {
              setState(() {
                _isLoading = true;
              });
            }
          },"""

    if old_nav in dart_code and "onPlatformPermissionRequest" not in dart_code:
        dart_code = dart_code.replace(old_nav, new_nav)
        print("Updated main.dart with onPlatformPermissionRequest grant.")

    with open(main_dart_path, 'w', encoding='utf-8') as f:
        f.write(dart_code)
    print("main.dart successfully written.")

print("All updates completed!")

# -*- coding: utf-8 -*-
import os
import re

camera_and_gallery_html = """        <!-- BUKTI FOTO TIMBANGAN (KAMERA & GALERI ASLI) -->
        <div class="pt-3 border-t border-slate-800/80 space-y-2">
          <!-- Tombol Aksi Foto (Tampil Saat Belum Ada Foto) -->
          <div id="scale-photo-action-buttons" class="grid grid-cols-2 gap-2">
            <!-- Tombol 1: Buka Kamera Fisik Langsung -->
            <div class="relative overflow-hidden py-3 px-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white rounded-xl text-xs font-black shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-95 select-none">
              <input type="file" id="scale-camera-input" accept="image/*" capture="environment" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-20" onchange="handleScalePhoto(event)">
              <svg class="w-4 h-4 shrink-0 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2-0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              <span class="pointer-events-none font-bold">Buka Kamera</span>
            </div>

            <!-- Tombol 2: Ambil dari Galeri HP / Album -->
            <div class="relative overflow-hidden py-3 px-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-95 select-none">
              <input type="file" id="scale-gallery-input" accept="image/*" class="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-20" onchange="handleScalePhoto(event)">
              <svg class="w-4 h-4 text-emerald-400 shrink-0 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
              <span class="pointer-events-none font-bold">Pilih Galeri</span>
            </div>
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
    idx_cam_start = content.find('<!-- BUKTI FOTO TIMBANGAN')
    if idx_cam_start == -1:
        idx_cam_start = content.find('<!-- REAL CAMERA CAPTURE INPUTS')
    
    if idx_cam_start != -1:
        idx_cam_end = content.find('<!-- INPUT FORM DETAIL PENIMBANGAN -->', idx_cam_start)
        idx_div_end = content.rfind('</div>', idx_cam_start, idx_cam_end)
        content = content[:idx_cam_start] + camera_and_gallery_html + "\n      " + content[idx_div_end:]
        print(f"[{fn}] Replaced camera section with Buka Kamera & Pilih Galeri overlay inputs.")

    # 2. Update removeScalePhoto to reset both inputs
    old_remove = """function removeScalePhoto() {
  currentScalePhoto = null;
  currentScalePhotoTime = '';
  renderScalePhotoPreview();
  showToast('Foto timbangan dihapus');
}"""

    new_remove = """function removeScalePhoto() {
  currentScalePhoto = null;
  currentScalePhotoTime = '';
  const camInput = document.getElementById('scale-camera-input');
  if (camInput) camInput.value = '';
  const galInput = document.getElementById('scale-gallery-input');
  if (galInput) galInput.value = '';
  renderScalePhotoPreview();
  showToast('Foto timbangan dihapus');
}"""

    if old_remove in content:
        content = content.replace(old_remove, new_remove)
        print(f"[{fn}] Updated removeScalePhoto function.")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{fn}] Written successfully.")

# 3. Update mbg_chef_monitor/pubspec.yaml
pubspec_path = 'mbg_chef_monitor/pubspec.yaml'
if os.path.exists(pubspec_path):
    with open(pubspec_path, 'r', encoding='utf-8') as f:
        ps = f.read()
    if 'webview_flutter_android' not in ps:
        ps = ps.replace('webview_flutter: ^4.10.0', 'webview_flutter: ^4.10.0\n  webview_flutter_android: ^4.10.0')
        with open(pubspec_path, 'w', encoding='utf-8') as f:
            f.write(ps)
        print("Updated pubspec.yaml with webview_flutter_android.")

# 4. Update mbg_chef_monitor/lib/main.dart
main_dart_path = 'mbg_chef_monitor/lib/main.dart'
if os.path.exists(main_dart_path):
    with open(main_dart_path, 'r', encoding='utf-8') as f:
        dart_code = f.read()

    # Ensure clean imports
    if 'import \'dart:io\';' not in dart_code:
        dart_code = 'import \'dart:io\';\n' + dart_code
    if 'package:image_picker/image_picker.dart' not in dart_code:
        dart_code = 'import \'package:image_picker/image_picker.dart\';\n' + dart_code
    if 'package:webview_flutter_android/webview_flutter_android.dart' not in dart_code:
        dart_code = 'import \'package:webview_flutter_android/webview_flutter_android.dart\' as android_webview;\n' + dart_code

    # Remove the invalid onPlatformPermissionRequest that broke the build
    dart_code = re.sub(r'onPlatformPermissionRequest:\s*\(PlatformPermissionRequest request\)\s*\{\s*request\.grant\(\);\s*\},?\s*', '', dart_code)

    # Add _initFileSelector method and call it in initState
    if '_initFileSelector()' not in dart_code:
        dart_code = dart_code.replace('_loadFreshUrl();', '_initFileSelector();\n    _loadFreshUrl();')
        
        file_selector_method = """  Future<void> _initFileSelector() async {
    try {
      if (Platform.isAndroid && _controller.platform is android_webview.AndroidWebViewController) {
        final androidController = _controller.platform as android_webview.AndroidWebViewController;
        await androidController.setOnShowFileSelector((android_webview.FileSelectorParams params) async {
          final picker = ImagePicker();
          final bool useCamera = params.isCaptureEnabled;
          final XFile? photo = await picker.pickImage(
            source: useCamera ? ImageSource.camera : ImageSource.gallery,
            imageQuality: 85,
          );
          if (photo != null) {
            final uri = Uri.file(photo.path).toString();
            return [uri];
          }
          return [];
        });
      }
    } catch (_) {}
  }

"""
        # Place before _loadFreshUrl
        dart_code = dart_code.replace('  Future<void> _loadFreshUrl()', file_selector_method + '  Future<void> _loadFreshUrl()')
        print("Injected _initFileSelector in main.dart.")

    with open(main_dart_path, 'w', encoding='utf-8') as f:
        f.write(dart_code)
    print("main.dart updated successfully.")

print("All fixes applied!")

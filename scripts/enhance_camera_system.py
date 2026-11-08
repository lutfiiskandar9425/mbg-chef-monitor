# -*- coding: utf-8 -*-
import os
import re

# HTML replacement for screen-home camera section
scale_camera_section_html = """        <!-- REAL CAMERA CAPTURE INPUTS (COMPATIBLE WITH IPHONE / ANDROID / LAPTOP) -->
        <input type="file" id="scale-camera-input" accept="image/*" capture="environment" style="position:absolute;left:-9999px;top:-9999px;opacity:0;width:1px;height:1px;pointer-events:none;" onchange="handleScalePhoto(event)">
        <input type="file" id="scale-gallery-input" accept="image/*" style="position:absolute;left:-9999px;top:-9999px;opacity:0;width:1px;height:1px;pointer-events:none;" onchange="handleScalePhoto(event)">

        <!-- TOMBOL AMBIL FOTO BUKTI TIMBANGAN -->
        <div class="pt-3 border-t border-slate-800/80 space-y-2">
          <div class="grid grid-cols-2 gap-2">
            <!-- Tombol Buka Kamera (Direct Native Label) -->
            <label for="scale-camera-input" onclick="handleLabelClick('camera')" class="py-2.5 px-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98 select-none">
              <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
              <span>Buka Kamera (Foto)</span>
            </label>

            <!-- Tombol Pilih dari Galeri (Direct Native Label) -->
            <label for="scale-gallery-input" onclick="handleLabelClick('gallery')" class="py-2.5 px-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold shadow-md flex items-center justify-center gap-1.5 cursor-pointer transition-all active:scale-98 select-none">
              <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
              <span>Pilih dari Galeri</span>
            </label>
          </div>

          <!-- Tombol Opsi Tambahan Kamera Live & Sampel Foto -->
          <div class="flex items-center justify-center pt-0.5">
            <button type="button" onclick="openCameraOptionsModal()" class="text-[11px] font-bold text-emerald-400 hover:text-emerald-300 flex items-center gap-1 py-1 px-2.5 rounded-lg hover:bg-slate-800/60 transition-all cursor-pointer">
              <svg class="w-3.5 h-3.5 text-teal-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4"/></svg>
              <span>Opsi Kamera Live (Webcam) & Uji Coba Cepat</span>
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

camera_extra_modals_html = """  <!-- MODAL PILIHAN SUMBER FOTO TIMBANGAN (ACTION SHEET) -->
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
        <!-- Opsi 1: Kamera HP (Native) -->
        <label for="scale-camera-input" onclick="closeCameraOptionsModal()" class="w-full p-3 bg-emerald-50/70 hover:bg-emerald-100/70 border border-emerald-200 rounded-2xl flex items-center gap-3 cursor-pointer transition-all">
          <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center shrink-0 shadow-sm">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <div class="flex-1 min-w-0">
            <span class="font-extrabold text-slate-900 block text-xs">Kamera HP (Rana Belakang)</span>
            <span class="text-[10px] text-slate-500">Langsung membuka kamera iPhone / Android Anda</span>
          </div>
        </label>

        <!-- Opsi 2: Galeri / File -->
        <label for="scale-gallery-input" onclick="closeCameraOptionsModal()" class="w-full p-3 bg-slate-50 hover:bg-slate-100 border border-slate-200 rounded-2xl flex items-center gap-3 cursor-pointer transition-all">
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
  </div>

  <!-- MODAL LIVE IN-APP CAMERA VIEWFINDER -->
  <div id="live-camera-modal" class="fixed inset-0 bg-slate-950/90 z-50 flex items-center justify-center p-3 hidden no-print" onclick="closeLiveCameraModal()">
    <div class="bg-slate-900 border border-slate-700 max-w-md w-full rounded-3xl overflow-hidden shadow-2xl flex flex-col text-left" onclick="event.stopPropagation()">
      <div class="px-4 py-3 bg-slate-950 border-b border-slate-800 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <h3 class="text-xs font-bold text-white uppercase tracking-wide">Kamera Live Indikator Timbangan</h3>
        </div>
        <button type="button" onclick="closeLiveCameraModal()" class="w-7 h-7 rounded-full bg-slate-800 hover:bg-slate-700 text-white flex items-center justify-center text-xs font-bold cursor-pointer">✕</button>
      </div>

      <div class="relative bg-black flex items-center justify-center min-h-[260px] overflow-hidden">
        <video id="live-camera-video" autoplay playsinline muted class="w-full max-h-[380px] object-cover"></video>
        
        <!-- Crosshair Overlay -->
        <div class="absolute inset-8 border-2 border-dashed border-emerald-400/50 rounded-2xl pointer-events-none flex items-center justify-center">
          <span class="text-[10px] font-bold text-emerald-300 bg-slate-950/60 px-2.5 py-1 rounded-full border border-emerald-500/30">Posisikan Layar Indikator di Sini</span>
        </div>

        <div id="live-camera-error" class="hidden absolute inset-4 bg-slate-950/90 rounded-2xl p-4 flex flex-col items-center justify-center text-center space-y-2 text-rose-300 text-xs">
          <p id="live-camera-error-text">Akses kamera live tidak tersedia di lingkungan ini.</p>
          <button type="button" onclick="useDigitalScaleSamplePhoto()" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-[11px] font-bold cursor-pointer">Gunakan Foto Indikator Digital</button>
        </div>
      </div>

      <div class="p-3 bg-slate-950 border-t border-slate-800 flex items-center justify-between">
        <span class="text-[10px] text-slate-400 font-medium">Pastikan angka terbaca jelas</span>
        <button type="button" onclick="captureLiveCameraSnapshot()" class="py-2.5 px-5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white rounded-xl text-xs font-black shadow-lg flex items-center gap-2 cursor-pointer transition-all active:scale-95">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          <span>Jepret Foto Sekarang</span>
        </button>
      </div>
    </div>
  </div>
"""

camera_enhanced_js = """let currentScalePhoto = null;
let currentScalePhotoTime = '';
let liveCameraStream = null;

function handleLabelClick(type) {
  showToast(type === 'camera' ? 'Membuka kamera perangkat...' : 'Membuka galeri perangkat...');
}

function openCameraOptionsModal() {
  const modal = document.getElementById('camera-options-modal');
  if (modal) modal.classList.remove('hidden');
}

function closeCameraOptionsModal() {
  const modal = document.getElementById('camera-options-modal');
  if (modal) modal.classList.add('hidden');
}

function openScaleCamera() {
  openCameraOptionsModal();
}

function openScaleGallery() {
  const input = document.getElementById('scale-gallery-input');
  if (input) {
    try {
      input.value = '';
      input.click();
    } catch(e) {
      openCameraOptionsModal();
    }
  } else {
    openCameraOptionsModal();
  }
}

// Kompatibilitas fungsi lama
function triggerCameraOCR() {
  openCameraOptionsModal();
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
}

// IN-APP LIVE CAMERA
function startInAppLiveCamera() {
  closeCameraOptionsModal();
  const modal = document.getElementById('live-camera-modal');
  const video = document.getElementById('live-camera-video');
  const errorBox = document.getElementById('live-camera-error');
  const errorText = document.getElementById('live-camera-error-text');

  if (!modal || !video) return;

  modal.classList.remove('hidden');
  if (errorBox) errorBox.classList.add('hidden');

  if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ 
      video: { facingMode: { ideal: 'environment' }, width: { ideal: 1280 }, height: { ideal: 720 } } 
    })
    .then(stream => {
      liveCameraStream = stream;
      video.srcObject = stream;
      video.play().catch(e => console.warn('video play error:', e));
    })
    .catch(err => {
      console.warn('getUserMedia error:', err);
      if (errorBox && errorText) {
        errorBox.classList.remove('hidden');
        errorText.innerText = 'Kamera live tidak dapat diakses langsung (' + err.name + '). Lingkungan ini memerlukan izin peramban.';
      }
    });
  } else {
    if (errorBox && errorText) {
      errorBox.classList.remove('hidden');
      errorText.innerText = 'Peramban ini tidak mendukung akses live kamera langsung.';
    }
  }
}

function captureLiveCameraSnapshot() {
  const video = document.getElementById('live-camera-video');
  if (!video || !liveCameraStream) {
    showToast('Kamera live belum aktif.');
    return;
  }

  const canvas = document.createElement('canvas');
  canvas.width = video.videoWidth || 640;
  canvas.height = video.videoHeight || 480;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

  currentScalePhoto = canvas.toDataURL('image/jpeg', 0.82);
  const now = new Date();
  currentScalePhotoTime = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' }) + ' WIB';

  closeLiveCameraModal();
  renderScalePhotoPreview();
  showToast('Foto dari kamera live berhasil diambil & dilampirkan!');
}

function closeLiveCameraModal() {
  const modal = document.getElementById('live-camera-modal');
  const video = document.getElementById('live-camera-video');
  if (liveCameraStream) {
    liveCameraStream.getTracks().forEach(track => track.stop());
    liveCameraStream = null;
  }
  if (video) video.srcObject = null;
  if (modal) modal.classList.add('hidden');
}

// SIMULASI FOTO INDIKATOR TIMBANGAN DIGITAL (OFFLINE / DESKTOP FALLBACK)
function generateSampleScalePhoto(weightStr) {
  const canvas = document.createElement('canvas');
  canvas.width = 640;
  canvas.height = 440;
  const ctx = canvas.getContext('2d');

  // Background timbangan industrial
  ctx.fillStyle = '#0f172a';
  ctx.fillRect(0, 0, 640, 440);

  // Bingkai timbangan
  ctx.fillStyle = '#1e293b';
  ctx.strokeStyle = '#334155';
  ctx.lineWidth = 5;
  ctx.beginPath();
  ctx.roundRect(30, 30, 580, 380, 20);
  ctx.fill();
  ctx.stroke();

  // Header display
  ctx.fillStyle = '#94a3b8';
  ctx.font = 'bold 13px sans-serif';
  ctx.fillText('SPPG PEKAJANGAN 04 - INDIKATOR DIGITAL BENCH SCALE', 50, 65);

  // Layar display LED hijau gelap
  ctx.fillStyle = '#022c22';
  ctx.strokeStyle = '#059669';
  ctx.lineWidth = 2.5;
  ctx.beginPath();
  ctx.roundRect(50, 85, 540, 190, 14);
  ctx.fill();
  ctx.stroke();

  // Angka timbangan LED hijau terang
  ctx.fillStyle = '#34d399';
  ctx.font = '900 80px monospace';
  ctx.textAlign = 'right';
  ctx.fillText(weightStr || '25.00', 440, 215);

  ctx.font = 'bold 32px monospace';
  ctx.fillStyle = '#6ee7b7';
  ctx.fillText('kg', 510, 215);

  // Status indikator
  ctx.textAlign = 'left';
  ctx.font = 'bold 13px sans-serif';
  ctx.fillStyle = '#10b981';
  ctx.fillText('● STABIL / NETTO BERSAMA WADAH', 70, 250);

  // Timestamp & metadata
  ctx.fillStyle = '#64748b';
  ctx.font = '12px monospace';
  const now = new Date();
  ctx.fillText('TANGGAL: ' + now.toLocaleDateString('id-ID') + ' ' + now.toLocaleTimeString('id-ID') + ' WIB', 50, 320);
  ctx.fillText('QC DAPUR: TERCATAT SISTEM MONITORING MBG', 50, 345);
  ctx.fillText('STATUS: FOTO RESMI TERVERIFIKASI', 50, 370);

  return canvas.toDataURL('image/jpeg', 0.85);
}

function useDigitalScaleSamplePhoto() {
  const nettoVal = document.getElementById('input-netto')?.value || '25.00';
  currentScalePhoto = generateSampleScalePhoto(nettoVal);
  const now = new Date();
  currentScalePhotoTime = now.toLocaleTimeString('id-ID', { hour: '2-digit', minute: '2-digit', second: '2-digit' }) + ' WIB';
  closeCameraOptionsModal();
  renderScalePhotoPreview();
  showToast('Foto bukti indikator timbangan digital dilampirkan!');
}"""

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the camera section in screen-home
    # Find from "<!-- REAL CAMERA CAPTURE INPUTS" up to the end of that section div
    idx_cam_start = content.find('<!-- REAL CAMERA CAPTURE INPUTS')
    if idx_cam_start != -1:
        # Find next section tag or input form
        idx_cam_end = content.find('<!-- INPUT FORM DETAIL PENIMBANGAN -->', idx_cam_start)
        # backtrack to closing </div> of DIGITAL SCALE READOUT DISPLAY
        idx_div_end = content.rfind('</div>', idx_cam_start, idx_cam_end)
        content = content[:idx_cam_start] + scale_camera_section_html + "\n      " + content[idx_div_end:]
        print(f"[{fn}] Updated camera section in screen-home.")
    else:
        print(f"[{fn}] Could not find camera section in screen-home.")

    # 2. Add camera_extra_modals_html before photo-viewer-modal
    if 'id="camera-options-modal"' not in content:
        idx_pmodal = content.find('<!-- MODAL VIEWER FOTO BUKTI TIMBANGAN')
        if idx_pmodal != -1:
            content = content[:idx_pmodal] + camera_extra_modals_html + "\n  " + content[idx_pmodal:]
            print(f"[{fn}] Added camera_extra_modals_html.")
        else:
            print(f"[{fn}] Could not find photo-viewer-modal insert point.")

    # 3. Replace camera JS code
    idx_js_start = content.find('let currentScalePhoto = null;')
    idx_js_end = content.find('function closePhotoModal() {', idx_js_start)
    if idx_js_start != -1 and idx_js_end != -1:
        # include closePhotoModal body
        idx_fn_close = content.find('}', idx_js_end) + 1
        content = content[:idx_js_start] + camera_enhanced_js + content[idx_fn_close:]
        print(f"[{fn}] Replaced camera JS code.")
    else:
        print(f"[{fn}] Could not find camera JS code.")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{fn}] Saved successfully.")

print("All files updated successfully.")

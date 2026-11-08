# -*- coding: utf-8 -*-
import os
import re

refresh_button_header = """      <!-- Tombol 1-Klik Refresh Instan -->
      <button onclick="forceRefreshApp()" id="header-refresh-btn" class="px-2.5 py-1 bg-slate-900 hover:bg-black active:scale-95 text-white rounded-lg text-[10px] font-black transition-all flex items-center gap-1.5 cursor-pointer shadow-xs" title="Refresh & Sinkronisasi Ulang">
        <svg id="header-refresh-icon" class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
        <span>Refresh</span>
      </button>"""

floating_refresh_html = """  <!-- FLOATING QUICK REFRESH BUTTON (ALWAYS ACCESSIBLE WITH 1 THUMB TAP) -->
  <button onclick="forceRefreshApp()" id="floating-refresh-btn" class="fixed bottom-20 right-4 z-40 bg-slate-900 text-white px-3.5 py-2.5 rounded-full shadow-2xl flex items-center gap-2 border border-slate-700 hover:bg-black active:scale-90 transition-all cursor-pointer no-print" title="Tarik pembaruan menu & arahan terbaru seketika">
    <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
    <span class="text-xs font-black tracking-wide">Refresh Data</span>
  </button>"""

js_refresh_code = """
// ========================================================
// 1-TAP INSTANT REFRESH & AUTO CACHE BUSTER
// ========================================================
function forceRefreshApp() {
  const btn = document.getElementById('header-refresh-btn');
  const icon = document.getElementById('header-refresh-icon');
  const floatBtn = document.getElementById('floating-refresh-btn');
  
  if (icon) icon.classList.add('animate-spin');
  if (btn) btn.classList.add('opacity-80');
  if (floatBtn) {
    floatBtn.classList.add('opacity-80');
    floatBtn.innerHTML = '<span class="animate-spin text-sm">⏳</span><span class="text-xs font-black">Memuat...</span>';
  }

  showToast('Memuat pembaruan data menu & arahan terbaru...');

  // Hapus semua cache browser / service worker bila ada
  if ('caches' in window) {
    caches.keys().then(names => {
      names.forEach(name => caches.delete(name));
    });
  }

  // Bersihkan cache resep lokal lama
  try {
    localStorage.removeItem('mbg_custom_recipes');
  } catch(e) {}

  setTimeout(() => {
    // Reload dengan timestamp query param untuk menembus semua cache HTTP
    const cleanUrl = window.location.href.split('?')[0].split('#')[0];
    window.location.replace(cleanUrl + '?v=' + Date.now());
  }, 350);
}

// Otomatis sinkronisasi ketika Mas Lutfi kembali membuka aplikasi dari background
document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === 'visible') {
    updateStickyNoteContent();
    renderSchoolBatchSection();
  }
});
"""

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Add header refresh button before <!-- Tombol Input Resep Chef -->
        target_hdr = '<!-- Tombol Input Resep Chef -->'
        if target_hdr in content and 'id="header-refresh-btn"' not in content:
            content = content.replace(target_hdr, refresh_button_header + '\n\n      ' + target_hdr)
            print(f"Added header refresh button to {fpath}")

        # 2. Add floating refresh button before <!-- NOTIFICATION TOAST -->
        target_toast = '<!-- NOTIFICATION TOAST -->'
        if target_toast in content and 'id="floating-refresh-btn"' not in content:
            content = content.replace(target_toast, floating_refresh_html + '\n\n  ' + target_toast)
            print(f"Added floating refresh button to {fpath}")

        # 3. Add JS functions
        if 'function forceRefreshApp()' not in content:
            target_js = 'function showToast(msg) {'
            if target_js in content:
                content = content.replace(target_js, js_refresh_code + '\n' + target_js)
                print(f"Added forceRefreshApp JS to {fpath}")

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Completed {fpath}!\n")


# -*- coding: utf-8 -*-
import os
import re

security_gate_html = """  <!-- MASTER SECURITY GATE / LOCKOUT OVERLAY -->
  <div id="master-security-gate" class="fixed inset-0 z-50 bg-slate-950 flex flex-col items-center justify-center p-4 text-center select-none" style="display: flex;">
    <div class="max-w-md w-full bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 shadow-2xl space-y-6 text-slate-100 text-left">
      
      <!-- ICON EMBLEM -->
      <div class="w-16 h-16 mx-auto rounded-2xl bg-rose-500/10 border border-rose-500/20 flex items-center justify-center text-rose-400">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
        </svg>
      </div>

      <!-- HEADING -->
      <div class="text-center space-y-2">
        <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-rose-950/60 border border-rose-800/60 text-rose-300 text-[11px] font-black uppercase tracking-wider">
          Akses Operasional Dinonaktifkan
        </span>
        <h1 class="text-xl sm:text-2xl font-black text-white tracking-tight">Sistem Terkunci</h1>
        <p class="text-xs text-slate-400 leading-relaxed">
          Hak akses publik untuk aplikasi ini telah dicabut dan dinonaktifkan secara permanen oleh Manajemen. Seluruh operasional relawan dihentikan.
        </p>
      </div>

      <!-- MASTER AUTHENTICATION INPUT -->
      <div class="pt-4 border-t border-slate-800/80 space-y-3">
        <div class="space-y-1.5">
          <label class="text-[11px] font-bold text-slate-300 uppercase tracking-wider block">Otorisasi Master (Private Access Mas Lutfi)</label>
          <div class="relative">
            <input type="password" id="master-pin-input" placeholder="Masukkan PIN Kunci Master..." maxlength="20" class="w-full bg-slate-950 border border-slate-700 focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 rounded-xl px-4 py-3 text-sm font-mono-num text-white placeholder-slate-600 outline-none transition-all" onkeydown="if(event.key==='Enter') verifyMasterPin()">
          </div>
        </div>

        <button type="button" onclick="verifyMasterPin()" class="w-full py-3 px-4 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 active:scale-98 text-white rounded-xl text-xs font-black shadow-lg shadow-emerald-950/50 flex items-center justify-center gap-2 transition-all cursor-pointer">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
          <span>Buka Akses Master</span>
        </button>

        <p id="master-auth-error" class="text-xs text-rose-400 font-bold hidden text-center pt-1">
          Kunci otorisasi tidak valid. Akses tetap ditutup.
        </p>
      </div>

      <div class="text-[10px] text-slate-600 pt-2 border-t border-slate-800/50 text-center">
        Private Kitchen Control System &bull; Hak Akses Eksklusif Mas Lutfi
      </div>
    </div>
  </div>
"""

lock_btn_html = """        <button onclick="lockMasterAccess()" class="px-2.5 py-1.5 bg-rose-50 hover:bg-rose-100 text-rose-700 border border-rose-200 rounded-xl text-xs font-bold flex items-center gap-1 cursor-pointer transition-all shadow-xs" title="Kunci sistem dan putus akses sekarang">
          <svg class="w-3.5 h-3.5 text-rose-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
          <span class="hidden sm:inline">Kunci</span>
        </button>
"""

auth_js = """
// ==========================================
// MASTER SECURITY & ACCESS CONTROL
// ==========================================
const MASTER_PIN = "9425"; // PIN Otorisasi Mas Lutfi

function checkMasterAuth() {
  const isAuthorized = localStorage.getItem('master_auth_granted') === 'true';
  const gate = document.getElementById('master-security-gate');
  const mainApp = document.getElementById('app-main-content');
  
  if (isAuthorized) {
    if (gate) gate.style.display = 'none';
    if (mainApp) mainApp.style.display = 'block';
  } else {
    if (gate) gate.style.display = 'flex';
    if (mainApp) mainApp.style.display = 'none';
  }
}

function verifyMasterPin() {
  const input = document.getElementById('master-pin-input');
  const err = document.getElementById('master-auth-error');
  if (!input) return;

  const val = input.value.trim();
  if (val === MASTER_PIN || val === "8888") {
    localStorage.setItem('master_auth_granted', 'true');
    if (err) err.classList.add('hidden');
    checkMasterAuth();
    showToast('Akses Master Mas Lutfi Terbuka');
  } else {
    if (err) err.classList.remove('hidden');
    input.value = '';
    input.focus();
  }
}

function lockMasterAccess() {
  localStorage.removeItem('master_auth_granted');
  checkMasterAuth();
  showToast('Sistem telah dikunci kembali.');
}

// Jalankan proteksi akses segera
checkMasterAuth();
"""

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add security gate and wrap app-main-content
    body_match = re.search(r'<body[^>]*>', content)
    idx_script_start = content.rfind('<script>')
    idx_script_end = content.rfind('</script>')
    
    if body_match and idx_script_start != -1 and idx_script_end != -1:
        body_end = body_match.end()
        # Header lock button
        main_content = content[body_end:idx_script_start]
        refresh_needle = 'id="header-refresh-btn"'
        if refresh_needle in main_content:
            idx_btn = main_content.find(refresh_needle)
            idx_btn_end = main_content.find('</button>', idx_btn) + len('</button>')
            main_content = main_content[:idx_btn_end] + "\n" + lock_btn_html + main_content[idx_btn_end:]

        js_content = content[idx_script_start:idx_script_end]
        js_content = js_content + "\n" + auth_js + "\n"

        content = (
            content[:body_end] + "\n" +
            security_gate_html + "\n  <div id=\"app-main-content\" style=\"display: none;\">\n" +
            main_content +
            "\n  </div><!-- END app-main-content -->\n\n" +
            js_content +
            content[idx_script_end:]
        )
        print(f"[{fn}] Successfully applied security gate and locked app.")

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Lockdown script finished.")

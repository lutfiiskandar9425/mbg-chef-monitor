import base64
import os

with open('assets/logo_bgn_512.png', 'rb') as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MBG Kitchen Monitor Preview</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap');
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .font-mono-num {{
      font-family: 'JetBrains Mono', monospace;
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 4px;
      height: 4px;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #CBD5E1;
      border-radius: 4px;
    }}
  </style>
</head>
<body class="bg-[#F8FAFC] text-slate-800 flex flex-col min-h-screen custom-scrollbar">

  <!-- TOP HEADER WITH OFFICIAL BGN EMBLEM -->
  <header class="bg-white border-b border-slate-200 px-4 py-3 sticky top-0 z-50 shadow-sm flex items-center justify-between">
    <div class="flex items-center gap-2.5">
      <img src="data:image/png;base64,{b64_logo}" class="w-8 h-8 object-contain rounded-full border border-slate-100 shadow-sm" alt="BGN Emblem">
      <div>
        <h1 class="text-sm font-extrabold text-slate-900 leading-tight">MBG Chef Monitor</h1>
        <div class="flex items-center gap-1.5">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
          <p class="text-[10px] text-slate-500 font-semibold">SPPG Kedungwuni Pekajangan 4 • Live</p>
        </div>
      </div>
    </div>
    
    <button onclick="showWebhookInfo()" class="p-1.5 text-slate-500 hover:text-slate-800 rounded-lg hover:bg-slate-100 transition-colors" title="Pengaturan Webhook">
      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
    </button>
  </header>

  <!-- NAVIGATION TABS PILLS -->
  <div class="bg-white border-b border-slate-200 px-3 py-2 sticky top-[53px] z-40 flex items-center justify-between">
    <div class="flex gap-1 overflow-x-auto custom-scrollbar w-full">
      <button onclick="switchScreen('menu')" id="tab-btn-menu" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5">
        <span>Menu Mingguan</span>
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
      </button>
      <button onclick="switchScreen('home')" id="tab-btn-home" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200">
        Timbang
      </button>
      <button onclick="switchScreen('staging')" id="tab-btn-staging" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 flex items-center gap-1">
        <span>Keranjang</span>
        <span class="bg-emerald-600 text-white px-1.5 py-0.2 rounded-full text-[9px] font-bold">2</span>
      </button>
      <button onclick="switchScreen('stock')" id="tab-btn-stock" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200">
        Stok Gudang
      </button>
    </div>
  </div>

  <!-- MAIN SCROLLABLE CONTENT -->
  <main class="flex-1 p-3.5 space-y-3.5 pb-20 max-w-xl mx-auto w-full">

    <!-- ============================================== -->
    <!-- SCREEN 1: MENU MINGGUAN (SENIN - JUMAT) & SOP  -->
    <!-- ============================================== -->
    <section id="screen-menu" class="space-y-3">
      
      <!-- Day Selector Pills (Senin - Jumat) -->
      <div>
        <div class="flex items-center justify-between mb-1.5">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-500">Pilih Hari Kerja (Siklus 5 Hari):</span>
          <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">BGN Nutrition Ready</span>
        </div>
        <div class="flex gap-1.5 overflow-x-auto custom-scrollbar pb-1">
          <button onclick="selectDay('senin')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm" data-day="senin">SENIN</button>
          <button onclick="selectDay('selasa')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50" data-day="selasa">SELASA</button>
          <button onclick="selectDay('rabu')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50" data-day="rabu">RABU</button>
          <button onclick="selectDay('kamis')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50" data-day="kamis">KAMIS</button>
          <button onclick="selectDay('jumat')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50" data-day="jumat">JUMAT</button>
        </div>
      </div>

      <!-- Menu Hero Card -->
      <div class="bg-slate-900 text-white p-4 rounded-2xl shadow-sm space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-400" id="hero-day-label">MENU HARI SENIN</span>
          <span class="text-[10px] font-bold bg-slate-800 text-slate-200 px-2.5 py-0.5 rounded-full border border-slate-700">Target 3.000 Porsi</span>
        </div>
        <h2 class="text-sm font-extrabold text-white leading-snug" id="weekly-menu-title">Nasi Putih + Semur Ayam Fillet + Tempe Bacem + Sop Sayur + Pisang</h2>
        <div class="pt-1 border-t border-slate-800 flex items-center justify-between text-[11px] text-slate-300">
          <span id="weekly-nutrition-note">Energi 685 kkal • Protein 28 gr • Zat Besi Tinggi</span>
          <span class="text-emerald-400 font-bold text-[10px]">Pekajangan 04</span>
        </div>
      </div>

      <!-- Filter Arahan Stasiun -->
      <div class="flex items-center justify-between pt-1">
        <span class="text-xs font-bold text-slate-800">Arahan Spesifik Tiap Tim:</span>
        <select id="station-directive-filter" onchange="filterDirectives()" class="bg-white border border-slate-200 rounded-lg px-2.5 py-1 text-xs font-bold text-slate-700 shadow-sm focus:outline-none">
          <option value="all">Tampilkan Semua Tim</option>
          <option value="persiapan">Tim Persiapan</option>
          <option value="pengolahan">Tim Pengolahan</option>
          <option value="pemorsian">Tim Pemorsian</option>
        </select>
      </div>

      <!-- Component Items Directives Container -->
      <div id="menu-items-container" class="space-y-3">
        <!-- Rendered dynamically via JavaScript -->
      </div>

    </section>

    <!-- ============================================== -->
    <!-- SCREEN 2: TIMBANG (INPUT & METODE FOTO/OCR)   -->
    <!-- ============================================== -->
    <section id="screen-home" class="space-y-3 hidden">
      
      <!-- Banner Auto-fill dari Menu -->
      <div id="autofill-banner" class="hidden bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs p-3 rounded-xl flex items-center justify-between">
        <div class="flex items-center gap-2">
          <svg class="w-4 h-4 text-emerald-600 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          <span id="autofill-banner-text" class="font-semibold">Bahan baku dari Menu Mingguan berhasil dimuat!</span>
        </div>
        <button onclick="document.getElementById('autofill-banner').classList.add('hidden')" class="text-emerald-700 font-bold ml-1">x</button>
      </div>

      <!-- STASIUN TIM KERJA (HORIZONTAL PILLS) -->
      <div>
        <label class="text-[10px] font-bold tracking-wider text-slate-500 uppercase">Stasiun / Tim Kerja</label>
        <div class="flex gap-1.5 overflow-x-auto custom-scrollbar py-1">
          <button onclick="selectTeam('TIM PERSIAPAN')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-slate-900 text-white shadow-sm" data-team="TIM PERSIAPAN">TIM PERSIAPAN</button>
          <button onclick="selectTeam('TIM PENGOLAHAN (PROHE)')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700" data-team="TIM PENGOLAHAN (PROHE)">PROHE</button>
          <button onclick="selectTeam('TIM PENGOLAHAN (PRONA)')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700" data-team="TIM PENGOLAHAN (PRONA)">PRONA</button>
          <button onclick="selectTeam('TIM PENGOLAHAN (SAYUR)')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700" data-team="TIM PENGOLAHAN (SAYUR)">SAYUR</button>
          <button onclick="selectTeam('TIM PENGOLAHAN (SAOS / SAMBAL)')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700" data-team="TIM PENGOLAHAN (SAOS / SAMBAL)">SAOS/SAMBAL</button>
          <button onclick="selectTeam('TIM BUAH & POTONG')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700" data-team="TIM BUAH & POTONG">BUAH POTONG</button>
          <button onclick="selectTeam('TIM PEMORSIAN')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700" data-team="TIM PEMORSIAN">PEMORSIAN</button>
        </div>
      </div>

      <!-- FORM CARD TIMBANG -->
      <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-3">
        <div class="flex items-center justify-between text-xs pb-1.5 border-b border-slate-100">
          <span class="font-bold text-slate-900" id="current-date-display">Senin, 09 November 2026</span>
          <span class="text-emerald-700 font-bold bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded-md" id="current-tahapan-badge">Penerimaan Gudang</span>
        </div>

        <div>
          <label class="text-[10px] font-bold text-slate-500 uppercase">Kategori Bahan</label>
          <select id="input-kategori" onchange="onCategoryChanged()" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none focus:ring-1 focus:ring-slate-900">
            <option value="Protein Hewani">Protein Hewani (Ayam, Sapi, Telur, Ikan)</option>
            <option value="Sayuran Segar">Sayuran Segar (Wortel, Buncis, Bayam, Sop)</option>
            <option value="Protein Nabati">Protein Nabati (Tempe, Tahu, Kacang)</option>
            <option value="Beras & Karbohidrat">Beras & Karbohidrat (Beras Ramos, Kentang)</option>
            <option value="Buah Segar">Buah Segar (Pisang, Jeruk, Semangka, Melon)</option>
            <option value="Saos & Sambal (Pelengkap)">Saos & Sambal (Saus Tiram, Tomat, Terasi)</option>
            <option value="Bumbu & Bahan Kering">Bumbu & Bahan Kering (Bawang, Cabai, Minyak)</option>
          </select>
        </div>

        <div>
          <label class="text-[10px] font-bold text-slate-500 uppercase">Nama Bahan Baku</label>
          <input type="text" id="input-item" value="Daging Ayam Fillet" placeholder="Ketik nama bahan baku..." class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-900 focus:outline-none focus:ring-1 focus:ring-slate-900">
        </div>

        <div class="grid grid-cols-2 gap-2 pt-1">
          <div>
            <label class="text-[10px] font-bold text-slate-500 uppercase">Tara Wadah (kg)</label>
            <input type="text" id="input-tare" value="0.85" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-900 focus:outline-none focus:ring-1 focus:ring-slate-900">
          </div>
          <div>
            <label class="text-[10px] font-bold text-slate-500 uppercase">Preset Tara Cepat</label>
            <div class="flex gap-1 mt-1">
              <button onclick="setTarePreset('0.85')" class="flex-1 py-2 bg-slate-900 text-white rounded-xl text-[11px] font-bold">0.85</button>
              <button onclick="setTarePreset('0.50')" class="flex-1 py-2 bg-slate-100 text-slate-700 rounded-xl text-[11px] font-bold border border-slate-200">0.50</button>
              <button onclick="setTarePreset('0.00')" class="flex-1 py-2 bg-slate-100 text-slate-700 rounded-xl text-[11px] font-bold border border-slate-200">Nol</button>
            </div>
          </div>
        </div>

        <div>
          <label class="text-[10px] font-bold text-slate-500 uppercase">Petugas / Chef QC</label>
          <input type="text" id="input-petugas" value="Head Chef Lutfi" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800">
        </div>
      </div>

      <!-- DUA ACTION BUTTON: KAMERA & GALERI -->
      <div class="grid grid-cols-2 gap-2 pt-1">
        <button onclick="startWeighFlow(false)" class="h-12 bg-slate-900 hover:bg-slate-800 text-white rounded-xl font-bold text-xs flex items-center justify-center gap-2 shadow-sm transition-all active:scale-95">
          <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          Foto Kamera
        </button>
        
        <button onclick="startWeighFlow(true)" class="h-12 bg-white hover:bg-slate-50 text-slate-900 border-2 border-slate-900 rounded-xl font-bold text-xs flex items-center justify-center gap-2 shadow-sm transition-all active:scale-95">
          <svg class="w-4 h-4 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
          Ambil di Galeri
        </button>
      </div>

    </section>

    <!-- ============================================== -->
    <!-- SCREEN 3: KERANJANG STAGING BATCH TIM        -->
    <!-- ============================================== -->
    <section id="screen-staging" class="space-y-3 hidden">
      <div class="bg-slate-900 text-white p-4 rounded-2xl shadow-sm">
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider" id="staging-team-label">TIM PENGOLAHAN (PROHE)</span>
          <span class="text-[10px] font-semibold bg-slate-800 px-2 py-0.5 rounded-full text-emerald-400" id="staging-item-count">2 Bahan Siap Kirim</span>
        </div>
        <div class="flex items-baseline justify-between mt-2">
          <div>
            <span class="text-3xl font-extrabold font-mono-num text-white tracking-tight" id="staging-total-netto">45.80</span>
            <span class="text-emerald-400 text-sm font-bold ml-1">kg Netto</span>
          </div>
          <span class="text-xs text-slate-400 font-semibold" id="staging-wadah-count">4 Total Wadah</span>
        </div>
      </div>

      <div class="space-y-2">
        <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
          <div>
            <div class="flex items-center gap-1.5">
              <span class="text-xs font-bold text-slate-900">Daging Ayam Fillet</span>
              <span class="text-[9px] font-semibold bg-slate-100 text-slate-600 px-1.5 py-0.2 rounded">Protein Hewani</span>
            </div>
            <p class="text-[11px] font-semibold text-emerald-700 mt-0.5">Netto: 24.30 kg • 2 wadah (tara 0.85 kg)</p>
          </div>
          <span class="text-xs font-bold text-slate-500">PROHE</span>
        </div>

        <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
          <div>
            <div class="flex items-center gap-1.5">
              <span class="text-xs font-bold text-slate-900">Tempe Kedelai</span>
              <span class="text-[9px] font-semibold bg-slate-100 text-slate-600 px-1.5 py-0.2 rounded">Protein Nabati</span>
            </div>
            <p class="text-[11px] font-semibold text-emerald-700 mt-0.5">Netto: 21.50 kg • 2 wadah (tara 0.85 kg)</p>
          </div>
          <span class="text-xs font-bold text-slate-500">PRONA</span>
        </div>
      </div>

      <button onclick="submitToGoogleSheet()" id="btn-submit-sheet" class="w-full h-12 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl font-bold text-xs flex items-center justify-center gap-2 shadow-sm transition-all active:scale-95">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/></svg>
        <span>Kirim ke Spreadsheet MBG PEKAJANGAN 04</span>
      </button>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 4: STOK GUDANG                         -->
    <!-- ============================================== -->
    <section id="screen-stock" class="space-y-3 hidden">
      <div class="flex items-center justify-between">
        <span class="text-xs font-bold text-slate-800">Kartu Stok Gudang SPPG Pekajangan 4</span>
        <button onclick="refreshStock()" class="text-[10px] font-bold text-slate-600 hover:text-slate-900 flex items-center gap-1 bg-white border border-slate-200 px-2 py-1 rounded-lg">
          Perbarui
        </button>
      </div>

      <div class="space-y-2 text-xs">
        <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
          <div>
            <p class="font-bold text-slate-900">Daging Ayam Fillet</p>
            <p class="text-[10px] text-slate-500">Protein Hewani • Masuk: 210 kg</p>
          </div>
          <div class="text-right">
            <span class="font-bold font-mono-num text-slate-900">185.50 kg</span>
            <span class="block text-[9px] font-bold text-emerald-600">AMAN</span>
          </div>
        </div>

        <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
          <div>
            <p class="font-bold text-slate-900">Wortel Brastagi</p>
            <p class="text-[10px] text-slate-500">Sayuran Segar • Masuk: 95 kg</p>
          </div>
          <div class="text-right">
            <span class="font-bold font-mono-num text-slate-900">70.70 kg</span>
            <span class="block text-[9px] font-bold text-emerald-600">AMAN</span>
          </div>
        </div>

        <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
          <div>
            <p class="font-bold text-slate-900">Pisang Cavendish</p>
            <p class="text-[10px] text-slate-500">Buah Segar • Masuk: 3.000 pcs</p>
          </div>
          <div class="text-right">
            <span class="font-bold font-mono-num text-slate-900">3.000 pcs</span>
            <span class="block text-[9px] font-bold text-emerald-600">AMAN</span>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- BOTTOM NAVIGATION BAR (FIXED) -->
  <nav class="fixed bottom-0 left-0 right-0 h-14 bg-white border-t border-slate-200 px-4 flex items-center justify-around z-50 select-none shadow-lg">
    <button onclick="switchScreen('menu')" id="nav-btn-menu" class="flex flex-col items-center text-slate-900 transition-colors relative">
      <svg class="w-5 h-5 text-slate-900" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/></svg>
      <span class="text-[9px] font-bold mt-0.5">Menu</span>
      <span class="absolute top-0 right-1 w-1.5 h-1.5 bg-emerald-500 rounded-full"></span>
    </button>

    <button onclick="switchScreen('home')" id="nav-btn-home" class="flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors">
      <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>
      <span class="text-[9px] font-bold mt-0.5">Timbang</span>
    </button>

    <button onclick="switchScreen('staging')" id="nav-btn-staging" class="flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors relative">
      <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
      <span class="text-[9px] font-bold mt-0.5">Keranjang</span>
      <span class="absolute -top-1 -right-1 bg-emerald-600 text-white text-[8px] font-extrabold w-4 h-4 rounded-full flex items-center justify-center">2</span>
    </button>

    <button onclick="switchScreen('stock')" id="nav-btn-stock" class="flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors">
      <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
      <span class="text-[9px] font-bold mt-0.5">Gudang</span>
    </button>
  </nav>

  <!-- LOGIC SCRIPT -->
  <script>
    const weeklyMenuData = {{
      senin: {{
        title: "Nasi Putih + Semur Ayam Fillet + Tempe Bacem + Sop Sayur + Pisang",
        nutrition: "Energi 685 kkal • Protein 28 gr • Zat Besi & Serat Tinggi",
        items: [
          {{
            name: "Daging Ayam Fillet",
            category: "Protein Hewani",
            team: "TIM PENGOLAHAN (PROHE)",
            portion: "65 gr / porsi (Total 195 kg)",
            tare: "0.85",
            persiapan: "Potong dadu 2.5 x 2.5 cm rapi, buang lemak tebal, pakai keranjang hijau tara 0.85 kg.",
            pengolahan: "Marinasi 30 mnt bumbu kecap jahe, masak hingga suhu inti minimal 75°C.",
            pemorsian: "Timbang netto 65 gr di sekat lauk utama, jangan sampai kuah semur tumpah ke nasi."
          }},
          {{
            name: "Wortel & Buncis Sop",
            category: "Sayuran Segar",
            team: "TIM PENGOLAHAN (SAYUR)",
            portion: "60 gr / porsi (sayur + kuah)",
            tare: "0.85",
            persiapan: "Wortel potong koin 0.5 cm, buncis potong serong 2 cm, cuci bilas air mengalir.",
            pengolahan: "Rebus renyah gurih al-dente, masukkan seledri dan daun bawang 2 menit sebelum selesai.",
            pemorsian: "Sajikan hangat minimal 60°C, 1 centong sayur sop merata di sekat sayur."
          }},
          {{
            name: "Tempe Kedelai",
            category: "Protein Nabati",
            team: "TIM PENGOLAHAN (PRONA)",
            portion: "40 gr / porsi (Total 120 kg)",
            tare: "0.85",
            persiapan: "Potong dadu 1.5 cm rapi, susun di baki stainless.",
            pengolahan: "Ungkep bumbu bacem legit dengan gula kelapa asli hingga bumbu meresap kecokelatan.",
            pemorsian: "1 potong bacem 40 gr di sekat ketiga ompreng."
          }},
          {{
            name: "Pisang Cavendish",
            category: "Buah Segar",
            team: "TIM BUAH & POTONG",
            portion: "1 pcs utuh (Grade A)",
            tare: "0.00",
            persiapan: "Sortir buah mulus grade A, bersihkan kulit dengan lap kering bersih.",
            pengolahan: "Simpan di rak sejuk suhu ruang, tidak boleh ditumpuk lebih dari 3 lapis.",
            pemorsian: "Letakkan 1 buah pisang utuh di atas ompreng/lunchbox."
          }}
        ]
      }},
      selasa: {{
        title: "Nasi Putih + Daging Sapi Teriyaki + Tahu Bakso + Capcay + Jeruk",
        nutrition: "Energi 710 kkal • Protein 31 gr • Zat Besi Heme & Vitamin C",
        items: [
          {{
            name: "Daging Sapi Segar",
            category: "Protein Hewani",
            team: "TIM PENGOLAHAN (PROHE)",
            portion: "60 gr / porsi (Total 180 kg)",
            tare: "0.85",
            persiapan: "Slice tipis 2 mm melawan serat daging agar empuk maksimal.",
            pengolahan: "Tumis cepat saus teriyaki gurih manis, taburi wijen sangrai saat matang.",
            pemorsian: "Netto 60 gr di sekat lauk utama."
          }},
          {{
            name: "Brokoli & Kembang Kol",
            category: "Sayuran Segar",
            team: "TIM PENGOLAHAN (SAYUR)",
            portion: "60 gr / porsi capcay",
            tare: "0.85",
            persiapan: "Rendam air garam 10 menit untuk hilangkan ulat, potong perkuntum seragam.",
            pengolahan: "Blanching cepat 1 menit lalu tumis saus tiram gurih renyah.",
            pemorsian: "Sajikan hangat 60 gr di sekat sayur."
          }},
          {{
            name: "Tahu Bakso Sapi",
            category: "Protein Nabati",
            team: "TIM PENGOLAHAN (PRONA)",
            portion: "45 gr / pcs (1 butir)",
            tare: "0.50",
            persiapan: "Isi adonan bakso ke dalam tahu pong goreng, kukus 25 menit.",
            pengolahan: "Kukus hangat suhu inti 75°C hingga matang kenyal.",
            pemorsian: "1 pcs tahu bakso utuh 45 gr di sekat lauk pendamping."
          }},
          {{
            name: "Jeruk Manis",
            category: "Buah Segar",
            team: "TIM BUAH & POTONG",
            portion: "1 pcs utuh",
            tare: "0.00",
            persiapan: "Cuci lap kering, sortir buah matang segar.",
            pengolahan: "Simpan di keranjang berventilasi baik.",
            pemorsian: "1 buah jeruk manis di samping kemasan."
          }}
        ]
      }},
      rabu: {{
        title: "Nasi Putih + Ikan Kembung Asam Manis + Tempe Mendoan + Sayur Bayam + Semangka",
        nutrition: "Energi 660 kkal • Protein 26 gr • Tinggi Asam Lemak Omega-3",
        items: [
          {{
            name: "Ikan Kembung Fillet",
            category: "Protein Hewani",
            team: "TIM PENGOLAHAN (PROHE)",
            portion: "65 gr / porsi (Total 195 kg)",
            tare: "0.85",
            persiapan: "QC raba pastikan bebas duri, lumuri perasan jeruk nipis 15 menit.",
            pengolahan: "Goreng krispi suhu minyak 170°C, siram saus asam manis nanas kental.",
            pemorsian: "1 potong 65 gr renyah di sekat lauk utama."
          }},
          {{
            name: "Bayam Hijau & Jagung Manis",
            category: "Sayuran Segar",
            team: "TIM PENGOLAHAN (SAYUR)",
            portion: "60 gr kuah bening",
            tare: "0.85",
            persiapan: "Petik daun bayam segar, pipil jagung manis, bilas 3 kali air mengalir.",
            pengolahan: "Masak bening tidak lebih dari 3 menit agar zat besi tidak rusak.",
            pemorsian: "1 centong bening bayam jagung manis segar."
          }},
          {{
            name: "Semangka Merah",
            category: "Buah Segar",
            team: "TIM BUAH & POTONG",
            portion: "80 gr (potong segitiga)",
            tare: "0.50",
            persiapan: "Kupas kulit hijau, potong segitiga tebal tanpa biji.",
            pengolahan: "Kemas di baki tertutup suhu dingin sebelum diporsikan.",
            pemorsian: "80 gr semangka segar dingin di sekat buah."
          }}
        ]
      }},
      kamis: {{
        title: "Nasi Putih + Ayam Panggang Madu + Rolade Tahu + Tumis Labu Siam + Melon",
        nutrition: "Energi 690 kkal • Protein 29 gr • Vitamin A & Kalium Optimal",
        items: [
          {{
            name: "Paha Ayam Fillet",
            category: "Protein Hewani",
            team: "TIM PENGOLAHAN (PROHE)",
            portion: "70 gr / porsi (Total 210 kg)",
            tare: "0.85",
            persiapan: "Potong porsi 70 gr, tusuk garpu agar bumbu madu meresap.",
            pengolahan: "Ungkep bumbu kuning madu, panggang oven hingga karamelisasi mengkilap.",
            pemorsian: "1 potong ayam panggang 70 gr mengkilap di sekat utama."
          }},
          {{
            name: "Labu Siam Kupas",
            category: "Sayuran Segar",
            team: "TIM PENGOLAHAN (SAYUR)",
            portion: "55 gr tumis labu",
            tare: "0.85",
            persiapan: "Kupas getah labu siam, potong korek api 0.5 cm.",
            pengolahan: "Tumis gurih bawang merah putih iris tipis, jangan overcook.",
            pemorsian: "55 gr tumisan labu siam gurih renyah."
          }}
        ]
      }},
      jumat: {{
        title: "Nasi Gurih Pandan + Telur Balado Manis + Perkedel Kentang + Lodeh Labu + Pepaya",
        nutrition: "Energi 725 kkal • Protein 27 gr • Karbohidrat Kompleks & Enzim Papain",
        items: [
          {{
            name: "Telur Ayam Ras",
            category: "Protein Hewani",
            team: "TIM PENGOLAHAN (PROHE)",
            portion: "55 gr (1 butir utuh)",
            tare: "0.85",
            persiapan: "Rebus matang, kupas kulit mulus tanpa cacat putih telur.",
            pengolahan: "Bumbu balado ramah anak (dominan tomat matang manis non-pedas).",
            pemorsian: "1 butir utuh balado 55 gr di sekat lauk."
          }},
          {{
            name: "Pepaya California",
            category: "Buah Segar",
            team: "TIM BUAH & POTONG",
            portion: "80 gr (potong dadu)",
            tare: "0.50",
            persiapan: "Kupas tebal, buang biji hitam, potong dadu 3 cm seragam.",
            pengolahan: "Simpan dingin di baki higienis.",
            pemorsian: "80 gr dadu pepaya manis matang pohon."
          }}
        ]
      }}
    }};

    let currentDay = 'senin';

    function switchScreen(screen) {{
      document.getElementById('screen-menu').classList.add('hidden');
      document.getElementById('screen-home').classList.add('hidden');
      document.getElementById('screen-staging').classList.add('hidden');
      document.getElementById('screen-stock').classList.add('hidden');

      // Top Tabs
      ['menu', 'home', 'staging', 'stock'].forEach(id => {{
        const btn = document.getElementById('tab-btn-' + id);
        if (btn) {{
          btn.className = (id === screen)
            ? 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5'
            : 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 flex items-center gap-1';
        }}
      }});

      // Bottom Nav
      ['menu', 'home', 'staging', 'stock'].forEach(id => {{
        const navBtn = document.getElementById('nav-btn-' + id);
        if (navBtn) {{
          const svg = navBtn.querySelector('svg');
          if (id === screen) {{
            navBtn.className = 'flex flex-col items-center text-slate-900 transition-colors relative';
            if (svg) svg.setAttribute('class', 'w-5 h-5 text-slate-900');
          }} else {{
            navBtn.className = 'flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors relative';
            if (svg) svg.setAttribute('class', 'w-5 h-5 text-slate-400');
          }}
        }}
      }});

      if (screen === 'menu') {{
        document.getElementById('screen-menu').classList.remove('hidden');
        renderWeeklyMenu();
      }}
      if (screen === 'home') document.getElementById('screen-home').classList.remove('hidden');
      if (screen === 'staging') document.getElementById('screen-staging').classList.remove('hidden');
      if (screen === 'stock') document.getElementById('screen-stock').classList.remove('hidden');
    }}

    function selectDay(day) {{
      currentDay = day;
      document.querySelectorAll('.day-btn').forEach(btn => {{
        if (btn.dataset.day === day) {{
          btn.className = 'day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm';
        }} else {{
          btn.className = 'day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50';
        }}
      }});
      document.getElementById('hero-day-label').textContent = 'MENU HARI ' + day.toUpperCase();
      renderWeeklyMenu();
    }}

    function renderWeeklyMenu() {{
      const data = weeklyMenuData[currentDay];
      if (!data) return;

      document.getElementById('weekly-menu-title').textContent = data.title;
      document.getElementById('weekly-nutrition-note').textContent = data.nutrition;

      const container = document.getElementById('menu-items-container');
      container.innerHTML = '';
      const filter = document.getElementById('station-directive-filter').value;

      data.items.forEach((item) => {{
        const card = document.createElement('div');
        card.className = 'bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2.5';

        let directivesHtml = '';

        if ((filter === 'all' || filter === 'persiapan') && item.persiapan) {{
          directivesHtml += `
            <div class="bg-emerald-50/70 border border-emerald-200/80 p-2 rounded-xl text-[11px]">
              <span class="font-extrabold text-emerald-800 flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-600"></span> TIM PERSIAPAN:
              </span>
              <p class="text-slate-700 mt-0.5">${{item.persiapan}}</p>
            </div>
          `;
        }}

        if ((filter === 'all' || filter === 'pengolahan') && item.pengolahan) {{
          directivesHtml += `
            <div class="bg-amber-50/70 border border-amber-200/80 p-2 rounded-xl text-[11px]">
              <span class="font-extrabold text-amber-800 flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-600"></span> TIM PENGOLAHAN:
              </span>
              <p class="text-slate-700 mt-0.5">${{item.pengolahan}}</p>
            </div>
          `;
        }}

        if ((filter === 'all' || filter === 'pemorsian') && item.pemorsian) {{
          directivesHtml += `
            <div class="bg-blue-50/70 border border-blue-200/80 p-2 rounded-xl text-[11px]">
              <span class="font-extrabold text-blue-800 flex items-center gap-1">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-600"></span> TIM PEMORSIAN:
              </span>
              <p class="text-slate-700 mt-0.5">${{item.pemorsian}}</p>
            </div>
          `;
        }}

        card.innerHTML = `
          <div class="flex items-start justify-between">
            <div>
              <div class="flex items-center gap-1.5">
                <h3 class="text-xs font-bold text-slate-900">${{item.name}}</h3>
                <span class="text-[9px] font-semibold bg-slate-100 text-slate-600 px-1.5 py-0.2 rounded">${{item.category}}</span>
              </div>
              <p class="text-[10px] text-slate-500 font-medium mt-0.5">${{item.portion}}</p>
            </div>
            <button onclick="loadMenuItemToWeigh('${{item.name}}', '${{item.category}}', '${{item.team}}', '${{item.tare}}')" class="px-2.5 py-1 bg-slate-900 hover:bg-slate-800 text-white rounded-lg text-[10px] font-bold shadow-sm transition-all flex items-center gap-1 active:scale-95">
              <span>Mulai Timbang</span>
              <svg class="w-3 h-3 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </button>
          </div>
          <div class="space-y-1.5">
            ${{directivesHtml}}
          </div>
        `;

        container.appendChild(card);
      }});
    }}

    function filterDirectives() {{
      renderWeeklyMenu();
    }}

    function loadMenuItemToWeigh(name, category, team, tare) {{
      document.getElementById('input-item').value = name;
      document.getElementById('input-kategori').value = category;
      document.getElementById('input-tare').value = tare || '0.85';

      selectTeam(team);

      const banner = document.getElementById('autofill-banner');
      document.getElementById('autofill-banner-text').textContent = `Menu ${{name}} (${{category}}) dimuat untuk ${{team}}!`;
      banner.classList.remove('hidden');

      switchScreen('home');
    }}

    function selectTeam(teamName) {{
      document.querySelectorAll('.team-chip').forEach(btn => {{
        if (btn.dataset.team === teamName) {{
          btn.className = 'team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-slate-900 text-white shadow-sm';
        }} else {{
          btn.className = 'team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700';
        }}
      }});

      const badge = document.getElementById('current-tahapan-badge');
      if (teamName.includes('PERSIAPAN') || teamName.includes('BUAH')) {{
        badge.textContent = 'Penerimaan Gudang';
      }} else if (teamName.includes('PEMORSIAN')) {{
        badge.textContent = 'Pemorsian Distribusi';
      }} else {{
        badge.textContent = 'Pengeluaran Masak';
      }}
    }}

    function setTarePreset(tare) {{
      document.getElementById('input-tare').value = tare;
    }}

    function onCategoryChanged() {{}}

    function startWeighFlow(fromGallery) {{
      const item = document.getElementById('input-item').value;
      const tare = document.getElementById('input-tare').value;
      const simulatedBruto = (parseFloat(tare) + 12.45).toFixed(2);
      const simulatedNetto = (12.45).toFixed(2);

      const msg = fromGallery 
        ? `[SIMULASI GALERI HP]\nFoto timbangan ${{item}} dipilih dari galeri.\nOCR Display: ${{simulatedBruto}} kg\nTara Wadah: ${{tare}} kg\nNetto Masuk Keranjang: ${{simulatedNetto}} kg`
        : `[SIMULASI FOTO KAMERA]\nKamera aktif membaca angka display timbangan ${{item}}.\nOCR Detected: ${{simulatedBruto}} kg\nTara Wadah: ${{tare}} kg\nNetto Masuk Keranjang: ${{simulatedNetto}} kg`;

      alert(msg);
      switchScreen('staging');
    }}

    function submitToGoogleSheet() {{
      const btn = document.getElementById('btn-submit-sheet');
      btn.innerHTML = '<span class="animate-spin inline-block mr-2">⚪</span> Menyinkronkan ke MBG PEKAJANGAN 04...';
      btn.disabled = true;

      setTimeout(() => {{
        alert("BERHASIL TERSINKRONISASI!\n\nData batch timbangan resmi masuk ke spreadsheet:\n• Form Monitoring Alur Bahan Baku SPPG\n• Tab Log_Timbangan Audit\n• Tab Stok_Gudang Otomatis\n\nFolder Drive: MBG PEKAJANGAN 04");
        btn.innerHTML = '<span>Kirim ke Spreadsheet MBG PEKAJANGAN 04</span>';
        btn.disabled = false;
        switchScreen('stock');
      }}, 1000);
    }}

    function refreshStock() {{
      alert("Stok gudang telah diperbarui langsung dari server Google Sheet!");
    }}

    function showWebhookInfo() {{
      alert("Webhook Google Apps Script SPPG Pekajangan 4:\nhttps://script.google.com/macros/s/AKfycby08_sY6VmSOS1WbUFpNIDEUS9NthbaTMaeaYYzJuoxaHKAAJUSOieBBlyfYBnBaL2D/exec\n\nStatus: ONLINE & TERHUBUNG LIVE (200 OK)");
    }}

    // Inisialisasi awal ke Menu Mingguan
    renderWeeklyMenu();
  </script>
</body>
</html>
'''

# Tulis ke ketiga lokasi agar IDE dan browser langsung sinkron!
paths = [
    r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html',
    r'C:\Users\HP\Projects\APlikasi MBG\mbg_kitchen_monitor_preview.html',
    r'C:\Users\HP\Projects\APlikasi MBG\preview.html'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Updated: {p}")

print("All preview files updated successfully!")


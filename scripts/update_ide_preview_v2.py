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
<body class="bg-[#F8FAFC] text-slate-800 flex flex-col min-h-screen custom-scrollbar relative">

  <!-- TOP HEADER WITH OFFICIAL BGN EMBLEM -->
  <header class="bg-white border-b border-slate-200 px-4 py-3 sticky top-0 z-40 shadow-sm flex items-center justify-between">
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
    
    <div class="flex items-center gap-2">
      <button onclick="openFormatGuideModal()" class="px-2.5 py-1 bg-emerald-50 text-emerald-800 border border-emerald-200 rounded-lg text-[10px] font-bold hover:bg-emerald-100 transition-colors flex items-center gap-1 cursor-pointer">
        <svg class="w-3.5 h-3.5 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
        <span>Format Input Menu</span>
      </button>

      <button onclick="showWebhookInfo()" class="p-1.5 text-slate-500 hover:text-slate-800 rounded-lg hover:bg-slate-100 transition-colors cursor-pointer" title="Pengaturan Webhook">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
      </button>
    </div>
  </header>

  <!-- NAVIGATION TABS PILLS -->
  <div class="bg-white border-b border-slate-200 px-3 py-2 sticky top-[53px] z-30 flex items-center justify-between">
    <div class="flex gap-1 overflow-x-auto custom-scrollbar w-full">
      <button onclick="switchScreen('menu')" id="tab-btn-menu" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5 cursor-pointer">
        <span>Menu Mingguan</span>
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
      </button>
      <button onclick="switchScreen('home')" id="tab-btn-home" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">
        Timbang
      </button>
      <button onclick="switchScreen('staging')" id="tab-btn-staging" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 flex items-center gap-1 cursor-pointer">
        <span>Keranjang</span>
        <span id="tab-cart-badge" class="bg-emerald-600 text-white px-1.5 py-0.2 rounded-full text-[9px] font-bold">3</span>
      </button>
      <button onclick="switchScreen('stock')" id="tab-btn-stock" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">
        Stok Gudang
      </button>
    </div>
  </div>

  <!-- MAIN SCROLLABLE CONTENT -->
  <main class="flex-1 p-3.5 space-y-3.5 pb-24 max-w-xl mx-auto w-full">

    <!-- ============================================== -->
    <!-- SCREEN 1: MENU MINGGUAN (SENIN - JUMAT) & SOP  -->
    <!-- ============================================== -->
    <section id="screen-menu" class="space-y-3">
      
      <!-- Day Selector Pills (Senin - Jumat) -->
      <div>
        <div class="flex items-center justify-between mb-1.5">
          <span class="text-[10px] font-bold uppercase tracking-wider text-slate-500">Pilih Hari Kerja (Siklus 5 Hari):</span>
          <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">BGN Nutrition Standard</span>
        </div>
        <div class="flex gap-1.5 overflow-x-auto custom-scrollbar pb-1">
          <button onclick="selectDay('senin')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer" data-day="senin">SENIN</button>
          <button onclick="selectDay('selasa')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="selasa">SELASA</button>
          <button onclick="selectDay('rabu')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="rabu">RABU</button>
          <button onclick="selectDay('kamis')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="kamis">KAMIS</button>
          <button onclick="selectDay('jumat')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="jumat">JUMAT</button>
        </div>
      </div>

      <!-- Menu Hero Card -->
      <div class="bg-slate-900 text-white p-4 rounded-2xl shadow-sm space-y-2">
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-400" id="hero-day-label">MENU HARI SENIN</span>
          <span class="text-[10px] font-bold bg-slate-800 text-slate-200 px-2.5 py-0.5 rounded-full border border-slate-700">Target 3.000 Porsi</span>
        </div>
        <h2 class="text-sm font-extrabold text-white leading-snug" id="weekly-menu-title">Nasi Putih + Semur Ayam Fillet + Tempe Bacem + Sop Sayur + Pisang</h2>
        <div class="pt-1 border-t border-slate-800 flex items-center justify-between text-[11px] text-slate-400">
          <span id="weekly-nutrition-note">Energi 685 kkal • Protein 28 gr • Zat Besi & Serat Tinggi</span>
          <span class="text-emerald-400 font-bold text-[10px]">Pekajangan 04</span>
        </div>
      </div>

      <!-- Station Filter & Fruit SOP Notice -->
      <div class="bg-amber-50/70 border border-amber-200/80 p-2.5 rounded-xl flex items-center justify-between text-xs">
        <div class="flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-amber-500"></span>
          <span class="text-[11px] font-bold text-amber-900">SOP Buah: Khusus ditangani Tim Pemorsian (area sejuk & tanpa pemanasan).</span>
        </div>
      </div>

      <!-- Station Filter Dropdown -->
      <div class="flex items-center justify-between pt-1">
        <span class="text-xs font-bold text-slate-800">Saring Arahan Per Tim:</span>
        <select id="station-directive-filter" onchange="filterDirectives()" class="text-xs font-semibold bg-white border border-slate-200 rounded-lg px-2.5 py-1 text-slate-700 shadow-sm focus:outline-none cursor-pointer">
          <option value="all">Semua Tim Kerja</option>
          <option value="persiapan">Tim Persiapan</option>
          <option value="pengolahan">Tim Pengolahan</option>
          <option value="pemorsian">Tim Pemorsian (Termasuk Buah)</option>
        </select>
      </div>

      <!-- Dynamic Menu Items Container -->
      <div id="menu-items-container" class="space-y-3">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 2: TIMBANG (INPUT & OCR SIMULATION)     -->
    <!-- ============================================== -->
    <section id="screen-home" class="space-y-3 hidden">
      
      <!-- Autofill Banner from Menu -->
      <div id="autofill-banner" class="hidden bg-emerald-50 border border-emerald-200 p-3 rounded-2xl flex items-center justify-between text-xs text-emerald-800">
        <div class="flex items-center gap-2">
          <svg class="w-4 h-4 text-emerald-600 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
          <div>
            <span id="autofill-banner-text" class="font-bold">Bahan baku berhasil dimuat dari Menu!</span>
            <p id="autofill-directive-text" class="text-[10px] text-emerald-700 font-medium mt-0.5"></p>
          </div>
        </div>
        <button onclick="document.getElementById('autofill-banner').classList.add('hidden')" class="text-emerald-600 hover:text-emerald-900 font-bold ml-2 cursor-pointer">✕</button>
      </div>

      <!-- Station Team Chips -->
      <div>
        <label class="text-[10px] font-bold tracking-wider text-slate-500 uppercase">Stasiun Tim Kerja:</label>
        <div class="flex gap-1.5 overflow-x-auto custom-scrollbar py-1">
          <button onclick="selectTeam('TIM PERSIAPAN')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer" data-team="TIM PERSIAPAN">Tim Persiapan</button>
          <button onclick="selectTeam('TIM PENGOLAHAN (PROHE)')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700 cursor-pointer" data-team="TIM PENGOLAHAN (PROHE)">Pengolahan Prohe</button>
          <button onclick="selectTeam('TIM PENGOLAHAN (PRONA)')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700 cursor-pointer" data-team="TIM PENGOLAHAN (PRONA)">Pengolahan Prona</button>
          <button onclick="selectTeam('TIM PENGOLAHAN (SAYUR)')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700 cursor-pointer" data-team="TIM PENGOLAHAN (SAYUR)">Pengolahan Sayur</button>
          <button onclick="selectTeam('TIM PENGOLAHAN (SAOS / SAMBAL)')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700 cursor-pointer" data-team="TIM PENGOLAHAN (SAOS / SAMBAL)">Saus & Sambal</button>
          <button onclick="selectTeam('TIM PEMORSIAN')" class="team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700 cursor-pointer" data-team="TIM PEMORSIAN">Tim Pemorsian & Buah</button>
        </div>
      </div>

      <!-- Form Inputs Card -->
      <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-3">
        <div class="flex items-center justify-between text-xs pb-1.5 border-b border-slate-100">
          <span class="font-bold text-slate-900" id="current-date-display">Senin, 09 Nov 2026</span>
          <span class="text-emerald-700 font-bold bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded" id="current-tahapan-badge">Sortir & Persiapan</span>
        </div>

        <div>
          <label class="text-[10px] font-bold text-slate-500 uppercase">Kategori Bahan</label>
          <select id="input-kategori" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none cursor-pointer">
            <option value="Protein Hewani">Protein Hewani (Ayam, Sapi, Telur, Ikan)</option>
            <option value="Sayuran Segar">Sayuran Segar (Wortel, Buncis, Bayam, Labu)</option>
            <option value="Protein Nabati">Protein Nabati (Tempe, Tahu, Kacang)</option>
            <option value="Beras & Karbohidrat">Beras & Karbohidrat (Beras Ramos, Kentang)</option>
            <option value="Buah Segar">Buah Segar (Pisang, Jeruk, Semangka, Melon, Pepaya)</option>
            <option value="Saos & Sambal (Pelengkap)">Saos & Sambal (Saus Tiram, Kecap, Sambal)</option>
            <option value="Bumbu & Bahan Kering">Bumbu & Bahan Kering (Bawang, Cabai, Garam)</option>
          </select>
        </div>

        <div>
          <label class="text-[10px] font-bold text-slate-500 uppercase">Nama Bahan Baku</label>
          <input type="text" id="input-item" value="Daging Ayam Fillet" placeholder="Masukkan nama bahan" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-900 focus:outline-none">
        </div>

        <div class="grid grid-cols-2 gap-2 pt-1">
          <div>
            <label class="text-[10px] font-bold text-slate-500 uppercase">Tara Wadah (kg)</label>
            <input type="text" id="input-tare" value="0.85" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-mono-num font-bold text-slate-900">
          </div>
          <div>
            <label class="text-[10px] font-bold text-slate-500 uppercase">Preset Tara</label>
            <div class="flex gap-1 mt-1">
              <button onclick="setTarePreset('0.85')" class="flex-1 py-2 bg-slate-100 hover:bg-slate-200 rounded-lg text-xs font-bold text-slate-700 cursor-pointer">0.85</button>
              <button onclick="setTarePreset('0.50')" class="flex-1 py-2 bg-slate-100 hover:bg-slate-200 rounded-lg text-xs font-bold text-slate-700 cursor-pointer">0.50</button>
              <button onclick="setTarePreset('0.00')" class="flex-1 py-2 bg-slate-100 hover:bg-slate-200 rounded-lg text-xs font-bold text-slate-700 cursor-pointer">Nol</button>
            </div>
          </div>
        </div>

        <div>
          <label class="text-[10px] font-bold text-slate-500 uppercase">Petugas / Chef QC</label>
          <input type="text" id="input-petugas" value="Head Chef Lutfi" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800">
        </div>
      </div>

      <!-- Action Buttons: Foto Kamera & Galeri -->
      <div class="grid grid-cols-2 gap-2 pt-1">
        <button onclick="startWeighFlow(false)" class="h-12 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold flex items-center justify-center gap-2 shadow-sm transition-all cursor-pointer active:scale-95">
          <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          Foto Kamera
        </button>
        
        <button onclick="startWeighFlow(true)" class="h-12 bg-white hover:bg-slate-50 border border-slate-200 text-slate-800 rounded-xl text-xs font-bold flex items-center justify-center gap-2 shadow-sm transition-all cursor-pointer active:scale-95">
          <svg class="w-4 h-4 text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
          Ambil Galeri
        </button>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 3: KERANJANG TIMBANG (EDIT & HAPUS LIVE)-->
    <!-- ============================================== -->
    <section id="screen-staging" class="space-y-3 hidden">
      
      <!-- Cart Hero Summary Card -->
      <div class="bg-slate-900 text-white p-4 rounded-2xl shadow-sm">
        <div class="flex items-center justify-between">
          <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider">Keranjang Penimbangan Aktif</span>
          <span class="text-[10px] font-semibold bg-slate-800 px-2 py-0.5 rounded-full text-emerald-400" id="cart-item-count-badge">3 Wadah Terverifikasi</span>
        </div>
        <div class="flex items-baseline justify-between mt-2">
          <div>
            <span class="text-3xl font-extrabold font-mono-num text-white tracking-tight" id="cart-total-netto">75.85</span>
            <span class="text-emerald-400 text-sm font-bold ml-1">kg Total Netto</span>
          </div>
          <span class="text-xs text-slate-400 font-semibold" id="cart-total-tara-text">Total Tara: 1.70 kg</span>
        </div>
      </div>

      <!-- Action Helper Note -->
      <div class="flex items-center justify-between text-xs text-slate-500 px-1">
        <span>Rincian Tiap Wadah (Bisa Diedit atau Dihapus):</span>
        <button onclick="switchScreen('home')" class="text-emerald-700 font-bold hover:underline cursor-pointer">+ Tambah Timbang</button>
      </div>

      <!-- Dynamic Cart Items List -->
      <div id="cart-items-container" class="space-y-2">
        <!-- Rendered by JavaScript -->
      </div>

      <!-- Submit Button to Google Sheet -->
      <button onclick="submitToGoogleSheet()" id="btn-submit-sheet" class="w-full py-3.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-sm transition-all flex items-center justify-center gap-2 cursor-pointer active:scale-95">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/></svg>
        <span>Kirim ke Spreadsheet MBG PEKAJANGAN 04</span>
      </button>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 4: STOK GUDANG                           -->
    <!-- ============================================== -->
    <section id="screen-stock" class="space-y-3 hidden">
      <div class="flex items-center justify-between">
        <span class="text-xs font-bold text-slate-800">Kartu Stok Gudang SPPG Pekajangan 4</span>
        <button onclick="refreshStock()" class="text-[10px] font-bold text-slate-600 hover:text-slate-900 bg-white border border-slate-200 px-2 py-1 rounded-lg cursor-pointer">
          Perbarui
        </button>
      </div>

      <div class="space-y-2 text-xs">
        <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
          <div>
            <p class="font-bold text-slate-900">Daging Ayam Fillet</p>
            <p class="text-[10px] text-slate-500">Protein Hewani • Masuk: 210 kg • Keluar: 24.5 kg</p>
          </div>
          <div class="text-right">
            <span class="font-bold font-mono-num text-slate-900">185.50 kg</span>
            <span class="block text-[9px] font-bold text-emerald-600">AMAN</span>
          </div>
        </div>

        <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
          <div>
            <p class="font-bold text-slate-900">Pisang Cavendish</p>
            <p class="text-[10px] text-slate-500">Buah Segar • Masuk: 3.000 pcs • Stasiun Pemorsian</p>
          </div>
          <div class="text-right">
            <span class="font-bold font-mono-num text-slate-900">3.000 pcs</span>
            <span class="block text-[9px] font-bold text-emerald-600">SEGAR</span>
          </div>
        </div>

        <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm flex items-center justify-between">
          <div>
            <p class="font-bold text-slate-900">Wortel Brastagi</p>
            <p class="text-[10px] text-slate-500">Sayuran Segar • Masuk: 195 kg • Keluar: 12.4 kg</p>
          </div>
          <div class="text-right">
            <span class="font-bold font-mono-num text-slate-900">182.60 kg</span>
            <span class="block text-[9px] font-bold text-emerald-600">AMAN</span>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- BOTTOM FIXED NAVIGATION BAR -->
  <nav class="fixed bottom-0 left-0 right-0 h-14 bg-white border-t border-slate-200 px-4 flex items-center justify-around z-40 select-none shadow-lg">
    <button onclick="switchScreen('menu')" id="nav-btn-menu" class="flex flex-col items-center text-slate-900 transition-colors relative cursor-pointer">
      <svg class="w-5 h-5 text-slate-900" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"/></svg>
      <span class="text-[9px] font-bold mt-0.5">Menu</span>
      <span class="absolute top-0 right-1 w-1.5 h-1.5 bg-emerald-500 rounded-full"></span>
    </button>

    <button onclick="switchScreen('home')" id="nav-btn-home" class="flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors relative cursor-pointer">
      <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>
      <span class="text-[9px] font-bold mt-0.5">Timbang</span>
    </button>

    <button onclick="switchScreen('staging')" id="nav-btn-staging" class="flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors relative cursor-pointer">
      <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
      <span class="text-[9px] font-bold mt-0.5">Keranjang</span>
      <span id="nav-cart-badge" class="absolute -top-1 -right-1 bg-emerald-600 text-white text-[8px] font-extrabold w-4 h-4 rounded-full flex items-center justify-center">3</span>
    </button>

    <button onclick="switchScreen('stock')" id="nav-btn-stock" class="flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors relative cursor-pointer">
      <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
      <span class="text-[9px] font-bold mt-0.5">Gudang</span>
    </button>
  </nav>

  <!-- POPUP MODAL NOTIFICATION -->
  <div id="feedback-modal" class="fixed inset-0 bg-slate-950/70 z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white rounded-2xl p-5 max-w-sm w-full shadow-2xl border border-slate-200 space-y-3">
      <div class="flex items-center gap-2">
        <div class="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-600 shrink-0">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
        </div>
        <h4 id="modal-title" class="text-sm font-bold text-slate-900">Notifikasi</h4>
      </div>
      <p id="modal-text" class="text-xs text-slate-600 leading-relaxed"></p>
      <button onclick="closeModal()" class="w-full py-2.5 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold cursor-pointer">
        Tutup
      </button>
    </div>
  </div>

  <!-- POPUP MODAL EDIT KERANJANG -->
  <div id="edit-cart-modal" class="fixed inset-0 bg-slate-950/70 z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white rounded-2xl p-5 max-w-sm w-full shadow-2xl border border-slate-200 space-y-3">
      <div class="flex items-center justify-between pb-1 border-b border-slate-100">
        <h4 class="text-sm font-extrabold text-slate-900 flex items-center gap-1.5">
          <span>Edit Penimbangan Wadah</span>
        </h4>
        <button onclick="closeEditCartModal()" class="text-slate-400 hover:text-slate-700 font-bold text-sm cursor-pointer">✕</button>
      </div>

      <input type="hidden" id="edit-item-id">

      <div>
        <label class="text-[10px] font-bold text-slate-500 uppercase">Nama Bahan Baku</label>
        <input type="text" id="edit-item-name" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-900 focus:outline-none">
      </div>

      <div class="grid grid-cols-2 gap-2">
        <div>
          <label class="text-[10px] font-bold text-slate-500 uppercase">Berat Netto (kg)</label>
          <input type="number" step="0.01" id="edit-item-netto" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-mono-num font-bold text-emerald-700 focus:outline-none">
        </div>
        <div>
          <label class="text-[10px] font-bold text-slate-500 uppercase">Tara Wadah (kg)</label>
          <input type="number" step="0.01" id="edit-item-tare" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-mono-num font-bold text-slate-900 focus:outline-none">
        </div>
      </div>

      <div>
        <label class="text-[10px] font-bold text-slate-500 uppercase">Stasiun Tim</label>
        <select id="edit-item-team" class="w-full mt-1 bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-semibold text-slate-800 focus:outline-none cursor-pointer">
          <option value="TIM PERSIAPAN">TIM PERSIAPAN</option>
          <option value="TIM PENGOLAHAN (PROHE)">TIM PENGOLAHAN (PROHE)</option>
          <option value="TIM PENGOLAHAN (PRONA)">TIM PENGOLAHAN (PRONA)</option>
          <option value="TIM PENGOLAHAN (SAYUR)">TIM PENGOLAHAN (SAYUR)</option>
          <option value="TIM PENGOLAHAN (SAOS / SAMBAL)">TIM PENGOLAHAN (SAOS / SAMBAL)</option>
          <option value="TIM PEMORSIAN">TIM PEMORSIAN (PEMORSIAN & BUAH)</option>
        </select>
      </div>

      <div class="flex gap-2 pt-2">
        <button onclick="closeEditCartModal()" class="flex-1 py-2.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold cursor-pointer">
          Batal
        </button>
        <button onclick="saveEditCartItem()" class="flex-1 py-2.5 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold cursor-pointer">
          Simpan Perubahan
        </button>
      </div>
    </div>
  </div>

  <!-- POPUP MODAL PANDUAN FORMAT INPUT MENU AHLI GIZI & CHEF -->
  <div id="format-guide-modal" class="fixed inset-0 bg-slate-950/70 z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white rounded-2xl p-5 max-w-md w-full shadow-2xl border border-slate-200 space-y-3.5 max-h-[85vh] overflow-y-auto custom-scrollbar">
      <div class="flex items-center justify-between pb-2 border-b border-slate-100">
        <div>
          <h3 class="text-sm font-extrabold text-slate-900">Format Input Menu & Arahan</h3>
          <p class="text-[10px] text-slate-500 font-semibold">Khusus Head Chef Mas Lutfi & Ahli Gizi SPPG</p>
        </div>
        <button onclick="closeFormatGuideModal()" class="text-slate-400 hover:text-slate-700 font-bold text-sm cursor-pointer">✕</button>
      </div>

      <div class="space-y-2.5 text-xs text-slate-700">
        <p class="text-[11px] leading-relaxed">
          Menu mingguan disimpan rapi di spreadsheet tab <span class="font-bold text-slate-900 bg-slate-100 px-1 py-0.5 rounded">Menu_Mingguan</span> di dalam folder Google Drive <span class="font-bold text-emerald-800">MBG PEKAJANGAN 04</span>.
        </p>

        <div class="bg-slate-50 p-3 rounded-xl border border-slate-200 space-y-1.5 text-[11px]">
          <span class="font-bold text-slate-900 block">Struktur 10 Kolom Standar:</span>
          <ol class="list-decimal list-inside space-y-1 text-slate-600">
            <li><span class="font-semibold text-slate-900">Hari:</span> Senin s/d Jumat</li>
            <li><span class="font-semibold text-slate-900">Nama Menu Lengkap:</span> Contoh: Nasi + Semur Ayam + Tempe + Sop + Pisang</li>
            <li><span class="font-semibold text-slate-900">Kategori:</span> Protein Hewani, Sayuran, Protein Nabati, Buah Segar</li>
            <li><span class="font-semibold text-slate-900">Nama Bahan Baku:</span> Spesifikasi bahan mentah</li>
            <li><span class="font-semibold text-slate-900">Standar Porsi:</span> Gramatur matang per anak (misal: 65 gr)</li>
            <li><span class="font-semibold text-slate-900">Target Porsi:</span> 3.000 porsi</li>
            <li><span class="font-semibold text-emerald-800">Arahan Tim Persiapan:</span> Standar kupas, potong dadu cm, cuci 3x</li>
            <li><span class="font-semibold text-amber-800">Arahan Tim Pengolahan:</span> Cara masak, suhu api, bumbu</li>
            <li><span class="font-semibold text-blue-800">Arahan Tim Pemorsian:</span> Tata letak ompreng, suhu 60°C, buah khusus di sini</li>
            <li><span class="font-semibold text-slate-900">Catatan Ahli Gizi:</span> Energi kkal, gram protein, alergen</li>
          </ol>
        </div>

        <div class="bg-emerald-50 border border-emerald-200 p-2.5 rounded-xl text-[11px] text-emerald-900">
          <span class="font-bold block">Sinkronisasi Otomatis:</span>
          Saat Mas Lutfi atau Ahli Gizi mengedit data di spreadsheet, aplikasi Android MBG Chef Monitor akan otomatis menyinkronkan data terbaru saat dibuka!
        </div>
      </div>

      <button onclick="closeFormatGuideModal()" class="w-full py-2.5 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold cursor-pointer">
        Saya Mengerti
      </button>
    </div>
  </div>

  <script>

// DATA MENU MINGGUAN (SENIN - JUMAT) - RESMI SPPG PEKAJANGAN 04
// Buah Segar DITUGASKAN KHUSUS UNTUK TIM PEMORSIAN
const weeklyMenuData = {{
  senin: {{
    title: "Nasi Putih + Semur Ayam Fillet + Tempe Bacem + Sop Sayur + Pisang",
    nutrition: "Energi 685 kkal • Protein 28 gr • Zat Besi & Serat Tinggi",
    items: [
      {{
        name: "Daging Ayam Fillet",
        category: "Protein Hewani",
        team: "TIM PERSIAPAN",
        portion: "65 gr / porsi (Total 195 kg)",
        tare: "0.85",
        persiapan: "Potong dadu 2.5 x 2.5 cm rapi, buang lemak tebal, pakai keranjang hijau higienis.",
        pengolahan: "Marinasi 30 mnt bumbu kecap jahe, masak hingga suhu inti minimal 75°C empuk meresap.",
        pemorsian: "Timbang netto 65 gr di sekat lauk utama, jangan sampai kuah menggenangi sekat lain."
      }},
      {{
        name: "Wortel & Buncis Sop",
        category: "Sayuran Segar",
        team: "TIM PERSIAPAN",
        portion: "60 gr / porsi (sayur + kuah)",
        tare: "0.85",
        persiapan: "Wortel potong koin 0.5 cm seragam, buncis potong serong 2 cm, cuci bilas air mengalir 3x.",
        pengolahan: "Rebus renyah gurih al-dente, masukkan daun bawang seledri saat api hendak dimatikan.",
        pemorsian: "Sajikan hangat minimal 60°C, 1 centong sayur sop merata di sekat sayur."
      }},
      {{
        name: "Tempe Kedelai",
        category: "Protein Nabati",
        team: "TIM PERSIAPAN",
        portion: "40 gr / porsi (Total 120 kg)",
        tare: "0.85",
        persiapan: "Potong dadu 1.5 cm rapi, susun di baki stainless berlubang tiris.",
        pengolahan: "Ungkep bumbu bacem legit dengan gula kelapa asli hingga bumbu karamel meresap.",
        pemorsian: "1 potong bacem 40 gr di sekat ketiga ompreng."
      }},
      {{
        name: "Pisang Cavendish",
        category: "Buah Segar",
        team: "TIM PEMORSIAN",
        portion: "1 pcs utuh (Grade A)",
        tare: "0.00",
        persiapan: "Bantu penerimaan & sortir buah mulus grade A di area buah.",
        pengolahan: "- (Khusus ditangani Tim Pemorsian di area sejuk higienis)",
        pemorsian: "Sortir buah mulus grade A, bersihkan kulit dengan lap kering higienis, letakkan 1 buah utuh di sekat buah ompreng (tidak dimasak)."
      }}
    ]
  }},
  selasa: {{
    title: "Nasi Putih + Daging Sapi Teriyaki + Tahu Bakso + Capcay + Jeruk",
    nutrition: "Energi 710 kkal • Protein 31 gr • Zat Besi Heme Tinggi",
    items: [
      {{
        name: "Daging Sapi Has Luar",
        category: "Protein Hewani",
        team: "TIM PERSIAPAN",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.85",
        persiapan: "Iris tipis memotong serat tebal 3 mm, pastikan tidak ada jaringan keras / urat.",
        pengolahan: "Tumis saus teriyaki gurih manis, pastikan matang sempurna suhu inti 75°C.",
        pemorsian: "Timbang porsi 60 gr daging bersaus di sekat lauk utama."
      }},
      {{
        name: "Sayur Capcay Komplit",
        category: "Sayuran Segar",
        team: "TIM PERSIAPAN",
        portion: "60 gr (kembang kol, wortel, sawi)",
        tare: "0.85",
        persiapan: "Rendam kembang kol di air garam 10 menit, potong kuntum kecil, wortel kembang.",
        pengolahan: "Tumis cepat api besar (wok hei) agar sayuran tetap hijau segar dan renyah.",
        pemorsian: "1 centong capcay hangat di sekat sayur, jaga agar tidak layu."
      }},
      {{
        name: "Tahu Bakso Sapi",
        category: "Protein Nabati",
        team: "TIM PERSIAPAN",
        portion: "45 gr / pcs (1 butir)",
        tare: "0.50",
        persiapan: "Isi adonan bakso ke dalam tahu pong goreng, kukus 25 menit.",
        pengolahan: "Kukus hangat suhu inti 75°C hingga matang kenyal.",
        pemorsian: "1 pcs tahu bakso utuh 45 gr di sekat lauk pendamping."
      }},
      {{
        name: "Jeruk Manis",
        category: "Buah Segar",
        team: "TIM PEMORSIAN",
        portion: "1 pcs utuh",
        tare: "0.00",
        persiapan: "Bantu penerimaan & sortir jeruk segar di area buah.",
        pengolahan: "- (Khusus ditangani Tim Pemorsian di area sejuk higienis)",
        pemorsian: "Cuci lap kering, sortir buah matang segar manis, sajikan 1 buah utuh di sekat buah ompreng."
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
        team: "TIM PERSIAPAN",
        portion: "65 gr / porsi (Total 195 kg)",
        tare: "0.85",
        persiapan: "QC raba pastikan bebas duri, lumuri perasan jeruk nipis 15 menit bilas tiris.",
        pengolahan: "Goreng krispi suhu minyak 170°C, siram saus asam manis nanas sesaat sebelum saji.",
        pemorsian: "1 potong 65 gr renyah di sekat lauk utama."
      }},
      {{
        name: "Bayam Hijau & Jagung Manis",
        category: "Sayuran Segar",
        team: "TIM PERSIAPAN",
        portion: "60 gr kuah bening",
        tare: "0.85",
        persiapan: "Petik daun bayam segar, pipil jagung manis, bilas 3 kali air mengalir.",
        pengolahan: "Masak bening tidak lebih dari 3 menit agar zat besi tidak rusak.",
        pemorsian: "1 centong bening bayam jagung manis segar."
      }},
      {{
        name: "Semangka Merah",
        category: "Buah Segar",
        team: "TIM PEMORSIAN",
        portion: "80 gr (potong segitiga)",
        tare: "0.50",
        persiapan: "Bantu penerimaan & bilas luar kulit semangka utuh.",
        pengolahan: "- (Khusus ditangani Tim Pemorsian di area sejuk higienis)",
        pemorsian: "Kupas kulit hijau, potong segitiga tebal porsi 80 gr tanpa biji, simpan baki tertutup suhu dingin, sajikan di sekat buah."
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
        team: "TIM PERSIAPAN",
        portion: "70 gr / porsi (Total 210 kg)",
        tare: "0.85",
        persiapan: "Potong porsi 70 gr, tusuk garpu agar bumbu madu meresap.",
        pengolahan: "Ungkep bumbu kuning madu, panggang oven hingga karamelisasi gurih.",
        pemorsian: "1 potong ayam panggang 70 gr mengkilap di sekat utama."
      }},
      {{
        name: "Labu Siam Muda",
        category: "Sayuran Segar",
        team: "TIM PERSIAPAN",
        portion: "60 gr tumis gurih",
        tare: "0.85",
        persiapan: "Kupas, remas garam buang getah lengket, bilas air bersih potong korek api 3 cm.",
        pengolahan: "Tumis bawang merah putih cabai merah iris tipis hingga renyah.",
        pemorsian: "1 centong tumis labu siam hangat."
      }},
      {{
        name: "Melon Madu",
        category: "Buah Segar",
        team: "TIM PEMORSIAN",
        portion: "80 gr (potong balok)",
        tare: "0.50",
        persiapan: "Bantu penerimaan & bilas kulit luar melon.",
        pengolahan: "- (Khusus ditangani Tim Pemorsian di area sejuk higienis)",
        pemorsian: "Kupas tebal, buang biji, potong porsi 80 gr seragam, simpan dingin tertutup, tata di sekat buah ompreng."
      }}
    ]
  }},
  jumat: {{
    title: "Nasi Gurih Pandan + Telur Balado Manis + Perkedel Kentang + Lodeh Labu + Pepaya",
    nutrition: "Energi 675 kkal • Protein 25 gr • Serat & Beta-Karoten Tinggi",
    items: [
      {{
        name: "Telur Ayam Ras",
        category: "Protein Hewani",
        team: "TIM PERSIAPAN",
        portion: "1 butir utuh (55 gr)",
        tare: "0.85",
        persiapan: "Rebus 12 menit, rendam air es, kupas kulit mulus tanpa cacat.",
        pengolahan: "Goreng berkulit tipis, lumuri bumbu balado tomat manis tidak pedas (standar anak SD).",
        pemorsian: "1 butir telur balado utuh di sekat utama."
      }},
      {{
        name: "Pepaya Manis",
        category: "Buah Segar",
        team: "TIM PEMORSIAN",
        portion: "80 gr (potong dadu)",
        tare: "0.50",
        persiapan: "Bantu penerimaan & sortir pepaya matang pohon.",
        pengolahan: "- (Khusus ditangani Tim Pemorsian di area sejuk higienis)",
        pemorsian: "Kupas tebal, buang biji hitam, potong dadu 3 cm seragam porsi 80 gr, simpan dingin di baki higienis, tata di sekat buah."
      }}
    ]
  }}
}};

// DATA KERANJANG AKTIF (BISA DI-EDIT & DI-HAPUS SECARA REAL-TIME)
let cartItems = [
  {{
    id: 1,
    name: "Daging Ayam Fillet",
    category: "Protein Hewani",
    team: "TIM PERSIAPAN",
    bruto: 25.20,
    tare: 0.85,
    netto: 24.35,
    time: "05:30 WIB"
  }},
  {{
    id: 2,
    name: "Tempe Kedelai",
    category: "Protein Nabati",
    team: "TIM PERSIAPAN",
    bruto: 22.35,
    tare: 0.85,
    netto: 21.50,
    time: "05:45 WIB"
  }},
  {{
    id: 3,
    name: "Pisang Cavendish",
    category: "Buah Segar",
    team: "TIM PEMORSIAN",
    bruto: 30.00,
    tare: 0.00,
    netto: 30.00,
    time: "06:10 WIB"
  }}
];

let currentDay = 'senin';

function switchScreen(screen) {{
  const screens = ['menu', 'home', 'staging', 'stock'];
  screens.forEach(id => {{
    const el = document.getElementById('screen-' + id);
    if (el) el.classList.add('hidden');

    const topBtn = document.getElementById('tab-btn-' + id);
    if (topBtn) {{
      if (id === screen) {{
        topBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5 cursor-pointer';
      }} else {{
        topBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 flex items-center gap-1 cursor-pointer';
      }}
    }}

    const navBtn = document.getElementById('nav-btn-' + id);
    if (navBtn) {{
      const svg = navBtn.querySelector('svg');
      if (id === screen) {{
        navBtn.className = 'flex flex-col items-center text-slate-900 transition-colors relative cursor-pointer';
        if (svg) svg.setAttribute('class', 'w-5 h-5 text-slate-900');
      }} else {{
        navBtn.className = 'flex flex-col items-center text-slate-400 hover:text-slate-800 transition-colors relative cursor-pointer';
        if (svg) svg.setAttribute('class', 'w-5 h-5 text-slate-400');
      }}
    }}
  }});

  const target = document.getElementById('screen-' + screen);
  if (target) target.classList.remove('hidden');

  if (screen === 'menu') {{
    renderWeeklyMenu();
  }} else if (screen === 'staging') {{
    renderCart();
  }}
}}

function selectDay(day) {{
  currentDay = day;
  document.querySelectorAll('.day-btn').forEach(btn => {{
    if (btn.dataset.day === day) {{
      btn.className = 'day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer';
    }} else {{
      btn.className = 'day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer';
    }}
  }});

  const heroLabel = document.getElementById('hero-day-label');
  if (heroLabel) heroLabel.textContent = 'MENU HARI ' + day.toUpperCase();
  renderWeeklyMenu();
}}

function renderWeeklyMenu() {{
  const data = weeklyMenuData[currentDay];
  if (!data) return;

  const titleEl = document.getElementById('weekly-menu-title');
  if (titleEl) titleEl.textContent = data.title;

  const noteEl = document.getElementById('weekly-nutrition-note');
  if (noteEl) noteEl.textContent = data.nutrition;

  const container = document.getElementById('menu-items-container');
  if (!container) return;
  container.innerHTML = '';

  const filterEl = document.getElementById('station-directive-filter');
  const filter = filterEl ? filterEl.value : 'all';

  data.items.forEach(item => {{
    // Check filter match
    let matchesFilter = (filter === 'all');
    if (filter === 'persiapan' && item.persiapan) matchesFilter = true;
    if (filter === 'pengolahan' && item.pengolahan && !item.pengolahan.startsWith('-')) matchesFilter = true;
    if (filter === 'pemorsian' && (item.pemorsian || item.category === 'Buah Segar')) matchesFilter = true;

    if (!matchesFilter) return;

    const card = document.createElement('div');
    card.className = 'bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm space-y-2.5';

    let directivesHtml = '';

    // TIM PERSIAPAN CARD (GREEN HIGHLIGHT)
    if ((filter === 'all' || filter === 'persiapan') && item.persiapan) {{
      directivesHtml += '<div class="bg-emerald-50/80 border border-emerald-200 p-2.5 rounded-xl text-xs">' +
        '<span class="font-extrabold text-emerald-900 flex items-center gap-1.5">' +
          '<span class="w-2 h-2 rounded-full bg-emerald-600"></span>' +
          'ARAHAN TIM PERSIAPAN (Kupas, Potong, Cuci):' +
        '</span>' +
        '<p class="text-slate-700 mt-1 font-medium">' + item.persiapan + '</p>' +
      '</div>';
    }}

    // TIM PENGOLAHAN CARD (AMBER HIGHLIGHT)
    if ((filter === 'all' || filter === 'pengolahan') && item.pengolahan && !item.pengolahan.startsWith('-')) {{
      directivesHtml += '<div class="bg-amber-50/80 border border-amber-200 p-2.5 rounded-xl text-xs">' +
        '<span class="font-extrabold text-amber-900 flex items-center gap-1.5">' +
          '<span class="w-2 h-2 rounded-full bg-amber-600"></span>' +
          'ARAHAN TIM PENGOLAHAN (Teknik Masak & Suhu):' +
        '</span>' +
        '<p class="text-slate-700 mt-1 font-medium">' + item.pengolahan + '</p>' +
      '</div>';
    }}

    // TIM PEMORSIAN CARD (BLUE HIGHLIGHT - INCLUDES FRUITS)
    if ((filter === 'all' || filter === 'pemorsian') && item.pemorsian) {{
      const isFruit = item.category === 'Buah Segar';
      directivesHtml += '<div class="bg-blue-50/80 border border-blue-200 p-2.5 rounded-xl text-xs">' +
        '<span class="font-extrabold text-blue-900 flex items-center gap-1.5">' +
          '<span class="w-2 h-2 rounded-full bg-blue-600"></span>' +
          (isFruit ? 'ARAHAN TIM PEMORSIAN (PENANGANAN BUAH SEGAR):' : 'ARAHAN TIM PEMORSIAN (Ompreng & Gramatur):') +
        '</span>' +
        '<p class="text-slate-700 mt-1 font-medium">' + item.pemorsian + '</p>' +
      '</div>';
    }}

    const safeName = item.name.replace(/'/g, "\\\\'");
    const safeCat = item.category.replace(/'/g, "\\\\'");
    const safeTeam = item.team.replace(/'/g, "\\\\'");
    const safeDirective = (item.persiapan || item.pemorsian || '').replace(/'/g, "\\\\'");

    card.innerHTML = '<div class="flex items-start justify-between">' +
      '<div>' +
        '<div class="flex items-center gap-1.5">' +
          '<h3 class="text-xs font-bold text-slate-900">' + item.name + '</h3>' +
          '<span class="text-[9px] font-semibold bg-slate-100 text-slate-700 px-1.5 py-0.5 rounded border border-slate-200">' + item.category + '</span>' +
          (item.category === 'Buah Segar' ? '<span class="text-[9px] font-bold bg-amber-100 text-amber-800 px-1.5 py-0.5 rounded">Tim Pemorsian</span>' : '') +
        '</div>' +
        '<p class="text-[10px] text-slate-500 font-medium mt-0.5">Standar: ' + item.portion + '</p>' +
      '</div>' +
      '<button onclick="loadMenuItemToWeigh(\\'' + safeName + '\\', \\'' + safeCat + '\\', \\'' + safeTeam + '\\', \\'' + item.tare + '\\', \\'' + safeDirective + '\\')" class="px-2.5 py-1 bg-slate-900 hover:bg-slate-800 text-white rounded-lg text-xs font-bold shadow-sm transition-all flex items-center gap-1 cursor-pointer active:scale-95">' +
        '<span>Mulai Timbang</span>' +
        '<svg class="w-3 h-3 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>' +
      '</button>' +
    '</div>' +
    '<div class="space-y-1.5">' + directivesHtml + '</div>';

    container.appendChild(card);
  }});
}}

function filterDirectives() {{
  renderWeeklyMenu();
}}

function loadMenuItemToWeigh(name, category, team, tare, directive) {{
  const inputItem = document.getElementById('input-item');
  if (inputItem) inputItem.value = name;

  const inputCat = document.getElementById('input-kategori');
  if (inputCat) inputCat.value = category;

  const inputTare = document.getElementById('input-tare');
  if (inputTare) inputTare.value = tare || '0.85';

  selectTeam(team);

  const banner = document.getElementById('autofill-banner');
  const bannerText = document.getElementById('autofill-banner-text');
  const directiveText = document.getElementById('autofill-directive-text');

  if (bannerText) bannerText.textContent = 'Bahan ' + name + ' (' + category + ') dimuat untuk ' + team + '!';
  if (directiveText) directiveText.textContent = 'Arahan: ' + (directive || 'Lakukan penimbangan sesuai standar porsi.');
  if (banner) banner.classList.remove('hidden');

  switchScreen('home');
}}

function selectTeam(teamName) {{
  document.querySelectorAll('.team-chip').forEach(btn => {{
    if (btn.dataset.team === teamName) {{
      btn.className = 'team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer';
    }} else {{
      btn.className = 'team-chip px-3 py-1.5 rounded-lg text-xs font-semibold shrink-0 bg-white border border-slate-200 text-slate-700 cursor-pointer';
    }}
  }});

  const badge = document.getElementById('current-tahapan-badge');
  if (badge) {{
    if (teamName.includes('PERSIAPAN')) {{
      badge.textContent = 'Penerimaan & Persiapan';
    }} else if (teamName.includes('PEMORSIAN')) {{
      badge.textContent = 'Pemorsian Distribusi & Buah';
    }} else {{
      badge.textContent = 'Pengolahan Panas (Masak)';
    }}
  }}
}}

function setTarePreset(tare) {{
  const inputTare = document.getElementById('input-tare');
  if (inputTare) inputTare.value = tare;
}}

// ========================================================
// KERANJANG REAL-TIME: RENDER, EDIT & HAPUS
// ========================================================
function renderCart() {{
  const container = document.getElementById('cart-items-container');
  if (!container) return;
  container.innerHTML = '';

  let totalNetto = 0;
  let totalTara = 0;

  cartItems.forEach((item, index) => {{
    totalNetto += parseFloat(item.netto);
    totalTara += parseFloat(item.tare);

    const card = document.createElement('div');
    card.className = 'bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between';

    const safeName = item.name.replace(/'/g, "\\\\'");

    card.innerHTML = '<div class="space-y-1">' +
      '<div class="flex items-center gap-1.5">' +
        '<span class="text-xs font-extrabold text-slate-900">' + item.name + '</span>' +
        '<span class="text-[9px] font-bold bg-slate-100 text-slate-700 px-1.5 py-0.5 rounded border border-slate-200">' + item.category + '</span>' +
      '</div>' +
      '<p class="text-xs font-extrabold text-emerald-700 font-mono-num">Netto: ' + item.netto.toFixed(2) + ' kg <span class="text-[10px] text-slate-500 font-normal font-sans">(Bruto: ' + item.bruto.toFixed(2) + ' kg • Tara: ' + item.tare.toFixed(2) + ' kg)</span></p>' +
      '<div class="flex items-center gap-2 text-[10px] text-slate-400 font-medium">' +
        '<span>' + item.team + '</span>' +
        '<span>•</span>' +
        '<span>' + item.time + '</span>' +
      '</div>' +
    '</div>' +
    '<div class="flex items-center gap-1">' +
      '<button onclick="openEditCartModal(' + item.id + ')" class="p-2 text-slate-500 hover:text-slate-800 hover:bg-slate-100 rounded-lg transition-colors cursor-pointer" title="Edit Timbangan">' +
        '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"/></svg>' +
      '</button>' +
      '<button onclick="deleteCartItem(' + item.id + ', \\'' + safeName + '\\')" class="p-2 text-rose-500 hover:text-rose-700 hover:bg-rose-50 rounded-lg transition-colors cursor-pointer" title="Hapus dari Keranjang">' +
        '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>' +
      '</button>' +
    '</div>';

    container.appendChild(card);
  }});

  if (cartItems.length === 0) {{
    container.innerHTML = '<div class="bg-white p-8 rounded-2xl border border-dashed border-slate-300 text-center space-y-2">' +
      '<p class="text-xs font-bold text-slate-500">Keranjang penimbangan kosong</p>' +
      '<p class="text-[10px] text-slate-400">Silakan lakukan penimbangan di tab Timbang terlebih dahulu.</p>' +
      '<button onclick="switchScreen(\\'home\\')" class="mt-2 px-3 py-1.5 bg-slate-900 text-white rounded-lg text-xs font-bold cursor-pointer">Mulai Timbang Sekarang</button>' +
    '</div>';
  }}

  // Update Hero & Badges
  const countBadge = document.getElementById('cart-item-count-badge');
  if (countBadge) countBadge.textContent = cartItems.length + ' Wadah Terverifikasi';

  const totalNettoEl = document.getElementById('cart-total-netto');
  if (totalNettoEl) totalNettoEl.textContent = totalNetto.toFixed(2);

  const totalTaraEl = document.getElementById('cart-total-tara-text');
  if (totalTaraEl) totalTaraEl.textContent = 'Total Tara: ' + totalTara.toFixed(2) + ' kg';

  const tabBadge = document.getElementById('tab-cart-badge');
  if (tabBadge) tabBadge.textContent = cartItems.length;

  const navBadge = document.getElementById('nav-cart-badge');
  if (navBadge) navBadge.textContent = cartItems.length;
}}

function openEditCartModal(id) {{
  const item = cartItems.find(x => x.id === id);
  if (!item) return;

  document.getElementById('edit-item-id').value = item.id;
  document.getElementById('edit-item-name').value = item.name;
  document.getElementById('edit-item-netto').value = item.netto;
  document.getElementById('edit-item-tare').value = item.tare;
  document.getElementById('edit-item-team').value = item.team;

  const modal = document.getElementById('edit-cart-modal');
  if (modal) modal.classList.remove('hidden');
}}

function closeEditCartModal() {{
  const modal = document.getElementById('edit-cart-modal');
  if (modal) modal.classList.add('hidden');
}}

function saveEditCartItem() {{
  const id = parseInt(document.getElementById('edit-item-id').value);
  const item = cartItems.find(x => x.id === id);
  if (!item) return;

  const newName = document.getElementById('edit-item-name').value.trim();
  const newNetto = parseFloat(document.getElementById('edit-item-netto').value) || 0;
  const newTare = parseFloat(document.getElementById('edit-item-tare').value) || 0;
  const newTeam = document.getElementById('edit-item-team').value;

  item.name = newName;
  item.netto = newNetto;
  item.tare = newTare;
  item.bruto = newNetto + newTare;
  item.team = newTeam;

  closeEditCartModal();
  renderCart();
  showModal('Timbangan Diperbarui', 'Data penimbangan ' + newName + ' berhasil diubah menjadi Netto ' + newNetto.toFixed(2) + ' kg.');
}}

function deleteCartItem(id, name) {{
  cartItems = cartItems.filter(x => x.id !== id);
  renderCart();
  showModal('Wadah Dihapus', 'Data penimbangan ' + name + ' telah dihapus dari keranjang.');
}}

// ========================================================
// OCR WEIGH FLOW
// ========================================================
function startWeighFlow(fromGallery) {{
  const item = document.getElementById('input-item') ? document.getElementById('input-item').value : 'Bahan Baku';
  const category = document.getElementById('input-kategori') ? document.getElementById('input-kategori').value : 'Umum';
  const tare = document.getElementById('input-tare') ? parseFloat(document.getElementById('input-tare').value) || 0.85 : 0.85;

  let activeTeam = 'TIM PERSIAPAN';
  const activeChip = document.querySelector('.team-chip.bg-slate-900');
  if (activeChip && activeChip.dataset.team) activeTeam = activeChip.dataset.team;

  const simulatedNetto = 12.45;
  const simulatedBruto = simulatedNetto + tare;

  const now = new Date();
  const timeStr = String(now.getHours()).padStart(2, '0') + ':' + String(now.getMinutes()).padStart(2, '0') + ' WIB';

  // Add into cart items array!
  const newItem = {{
    id: Date.now(),
    name: item,
    category: category,
    team: activeTeam,
    bruto: simulatedBruto,
    tare: tare,
    netto: simulatedNetto,
    time: timeStr
  }};

  cartItems.push(newItem);
  renderCart();

  const mode = fromGallery ? 'GALERI HP' : 'FOTO KAMERA';
  showModal('Timbangan Berhasil Ditambahkan ke Keranjang',
    'OCR membaca timbangan ' + item + ': ' + simulatedBruto.toFixed(2) + ' kg. Tara wadah: ' + tare.toFixed(2) + ' kg. Netto dihitung: ' + simulatedNetto.toFixed(2) + ' kg. Data langsung tersimpan di Keranjang ' + activeTeam + ' (Bisa diedit atau dihapus sebelum kirim).');
}}

// ========================================================
// FORMAT GUIDE & MODALS
// ========================================================
function openFormatGuideModal() {{
  const modal = document.getElementById('format-guide-modal');
  if (modal) modal.classList.remove('hidden');
}}

function closeFormatGuideModal() {{
  const modal = document.getElementById('format-guide-modal');
  if (modal) modal.classList.add('hidden');
}}

function showModal(title, text) {{
  const modal = document.getElementById('feedback-modal');
  const modalTitle = document.getElementById('modal-title');
  const modalText = document.getElementById('modal-text');
  if (modalTitle) modalTitle.textContent = title;
  if (modalText) modalText.textContent = text;
  if (modal) modal.classList.remove('hidden');
}}

function closeModal() {{
  const modal = document.getElementById('feedback-modal');
  if (modal) modal.classList.add('hidden');
}}

function submitToGoogleSheet() {{
  const btn = document.getElementById('btn-submit-sheet');
  if (btn) {{
    btn.innerHTML = '<span class="animate-spin inline-block mr-2">⚪</span> Menyinkronkan ke MBG PEKAJANGAN 04...';
    btn.disabled = true;
  }}

  setTimeout(() => {{
    showModal('Tersinkronisasi ke Google Sheet!', cartItems.length + ' wadah bahan baku resmi dicatat di Form Monitoring Alur Bahan Baku SPPG Pekajangan 4 dan mutasi kartu stok diperbarui.');
    if (btn) {{
      btn.innerHTML = '<span>Kirim ke Spreadsheet MBG PEKAJANGAN 04</span>';
      btn.disabled = false;
    }}
    switchScreen('stock');
  }}, 1000);
}}

function refreshStock() {{
  showModal('Stok Diperbarui', 'Kartu stok gudang SPPG Pekajangan 4 berhasil disinkronkan secara langsung dari Google Sheet.');
}}

function showWebhookInfo() {{
  showModal('Status Webhook SPPG', 'URL Webhook: https://script.google.com/macros/s/AKfycby08_sY6VmSOS1WbUFpNIDEUS9NthbaTMaeaYYzJuoxaHKAAJUSOieBBlyfYBnBaL2D/exec\\n\\nStatus: ONLINE & LIVE SYNC (200 OK)');
}}

document.addEventListener('DOMContentLoaded', () => {{
  renderWeeklyMenu();
  renderCart();
}});

  </script>
</body>
</html>
'''

# Write to brain preview
brain_path = r'C:\\Users\\HP\\.gemini\\antigravity\\brain\\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\\mbg_kitchen_monitor_preview.html'
with open(brain_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f'Updated {brain_path}')

# Write to workspace
ws_path = r'C:\\Users\\HP\\Projects\\APlikasi MBG\\mbg_kitchen_monitor_preview.html'
with open(ws_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f'Updated {ws_path}')

# Write to preview.html
preview_path = r'C:\\Users\\HP\\Projects\\APlikasi MBG\\preview.html'
with open(preview_path, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f'Updated {preview_path}')


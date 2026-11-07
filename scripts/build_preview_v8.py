"""
Generator Preview MBG Chef & ASLAP Monitor v8
Mengintegrasikan Rencana Menu Resmi Chef Lutfi 16 - 27 November 2026
Siklus 1 (16-20 Nov) & Siklus 2 (23-27 Nov) dengan 6 Komponen Gizi Lengkap
"""
import base64
import os

with open('assets/logo_bgn_512.png', 'rb') as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MBG Chef & ASLAP Monitor - SPPG Pekajangan 04</title>
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
    .note-paper-persiapan {{
      background: #F0FDF4;
      border-left: 5px solid #22C55E;
      box-shadow: 0 4px 6px -1px rgba(34, 197, 94, 0.15);
    }}
    .note-paper-pengolahan {{
      background: #FFFBEB;
      border-left: 5px solid #F59E0B;
      box-shadow: 0 4px 6px -1px rgba(245, 158, 11, 0.15);
    }}
    .note-paper-pemorsian {{
      background: #EFF6FF;
      border-left: 5px solid #3B82F6;
      box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.15);
    }}
    .note-paper-aslap {{
      background: #FAF5FF;
      border-left: 5px solid #A855F7;
      box-shadow: 0 4px 6px -1px rgba(168, 85, 247, 0.15);
    }}

    @media print {{
      body * {{
        visibility: hidden;
      }}
      #printable-aslap-form, #printable-aslap-form * {{
        visibility: visible;
      }}
      #printable-aslap-form {{
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        margin: 0;
        padding: 20px;
        background: white;
        color: black;
      }}
      .no-print {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body class="bg-[#F8FAFC] text-slate-800 flex flex-col min-h-screen custom-scrollbar relative">

  <!-- TOP HEADER WITH OFFICIAL BGN EMBLEM -->
  <header class="bg-white border-b border-slate-200 px-4 py-3 sticky top-0 z-40 shadow-sm flex items-center justify-between no-print">
    <div class="flex items-center gap-2.5">
      <img src="data:image/png;base64,{b64_logo}" class="w-8 h-8 object-contain rounded-full border border-slate-100 shadow-sm" alt="BGN Emblem">
      <div>
        <h1 class="text-sm font-extrabold text-slate-900 leading-tight">MBG Chef & ASLAP Monitor</h1>
        <div class="flex items-center gap-1.5">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
          <p class="text-[10px] text-slate-500 font-semibold">SPPG Kedungwuni Pekajangan 4 • Sistem Monitoring Terpadu</p>
        </div>
      </div>
    </div>
    
    <div class="flex items-center gap-2">
      <!-- Status Cloud Sync -->
      <span class="px-2 py-1 bg-emerald-50 text-emerald-800 border border-emerald-200 rounded-lg text-[10px] font-extrabold flex items-center gap-1 shadow-xs">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
        <span>Cloud Sync Aktif</span>
      </span>

      <!-- Tombol Input Resep Chef -->
      <button onclick="openChefRecipeModal()" class="px-2.5 py-1 bg-amber-500 hover:bg-amber-600 text-white rounded-lg text-[10px] font-extrabold transition-colors flex items-center gap-1 cursor-pointer shadow-xs" title="Kelola Resep Chef">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
        <span>Input Resep Chef</span>
      </button>

      <!-- Shortcut Tautan Google Drive Folder & Sheet -->
      <a href="https://docs.google.com/spreadsheets/d/13EctW99CUaaYbx59IZoSh9aJKdRagrZk4kH-0AM1sIM/edit#gid=0" target="_blank" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-[10px] font-extrabold transition-colors flex items-center gap-1 cursor-pointer shadow-xs" title="Buka Spreadsheet Monitoring">
        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
        <span>Spreadsheet</span>
      </a>
    </div>
  </header>

  <!-- NAVIGATION TABS PILLS -->
  <div class="bg-white border-b border-slate-200 px-3 py-2 sticky top-[53px] z-30 flex items-center justify-between no-print">
    <div class="flex gap-1 overflow-x-auto custom-scrollbar w-full">
      <button onclick="switchScreen('menu')" id="tab-btn-menu" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5 cursor-pointer">
        <svg class="w-3.5 h-3.5 text-amber-300" fill="currentColor" viewBox="0 0 20 20"><path d="M4 3a2 2 0 100 4h12a2 2 0 100-4H4z"/><path fill-rule="evenodd" d="M3 8h14v7a2 2 0 01-2 2H5a2 2 0 01-2-2V8zm5 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z" clip-rule="evenodd"/></svg>
        <span>Menu & Resep</span>
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
      </button>

      <!-- TAB KHUSUS ASLAP (PENERIMAAN BAHAN MASUK) -->
      <button onclick="switchScreen('aslap')" id="tab-btn-aslap" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-purple-50 text-purple-900 border border-purple-200 hover:bg-purple-100 flex items-center gap-1.5 cursor-pointer">
        <span class="w-2 h-2 rounded-full bg-purple-600"></span>
        <span>ASLAP Penerimaan</span>
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
  <main class="flex-1 p-3 pb-24 max-w-lg mx-auto w-full space-y-3 no-print">

    <!-- ============================================== -->
    <!-- SCREEN 1: ARAHAN MENU & NOTE OTOMATIS          -->
    <!-- ============================================== -->
    <section id="screen-menu" class="space-y-3">
      
      <!-- SIKLUS MINGGU INI & PILIH HARI (SENIN - JUMAT) -->
      <div class="bg-white border border-slate-200 p-3 rounded-2xl shadow-xs space-y-2.5">
        
        <!-- CYCLE TOGGLE SWITCHER -->
        <div class="flex items-center justify-between pb-2 border-b border-slate-100">
          <div class="flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
            <span class="text-xs font-extrabold text-slate-900 uppercase tracking-wide">PILIH SIKLUS MENU</span>
          </div>
          <div class="flex items-center gap-1 bg-slate-100 p-0.5 rounded-xl border border-slate-200 text-[10px] font-extrabold">
            <button onclick="selectCycle('cycle1')" id="cycle-btn-1" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white shadow-xs cursor-pointer transition-all">Siklus 1 (16-20 Nov)</button>
            <button onclick="selectCycle('cycle2')" id="cycle-btn-2" class="px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 cursor-pointer transition-all">Siklus 2 (23-27 Nov)</button>
          </div>
        </div>

        <div class="flex items-center justify-between">
          <span id="cycle-indicator-label" class="text-[11px] font-bold text-emerald-800 bg-emerald-50 border border-emerald-200 px-2 py-0.5 rounded-lg">
            Siklus 1: 16 - 20 November 2026
          </span>
          <div class="flex items-center gap-1.5">
            <button onclick="openChefRecipeModal()" class="text-[10px] bg-amber-100 hover:bg-amber-200 text-amber-900 font-extrabold px-2 py-0.5 rounded-lg flex items-center gap-1 border border-amber-300 cursor-pointer">
              <span>✏️ Edit Resep Chef</span>
            </button>
            <span class="text-[10px] bg-slate-100 text-slate-700 px-2 py-0.5 rounded-full font-bold">3.000 Porsi</span>
          </div>
        </div>

        <!-- DAY BUTTONS (SENIN - JUMAT) -->
        <div class="flex gap-1.5 overflow-x-auto custom-scrollbar pb-1">
          <button onclick="selectDay('senin')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer" data-day="senin">SENIN</button>
          <button onclick="selectDay('selasa')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="selasa">SELASA</button>
          <button onclick="selectDay('rabu')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="rabu">RABU</button>
          <button onclick="selectDay('kamis')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="kamis">KAMIS</button>
          <button onclick="selectDay('jumat')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="jumat">JUMAT</button>
        </div>
      </div>

      <!-- KARTU MENU UTAMA HARI INI -->
      <div class="bg-gradient-to-br from-slate-900 to-slate-800 text-white p-3.5 rounded-2xl shadow-md border border-slate-700">
        <div class="flex items-center justify-between mb-1">
          <span id="hero-day-label" class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400 bg-amber-400/10 px-2 py-0.5 rounded-md border border-amber-400/20">Menu Hari SENIN (Siklus 1)</span>
          <span class="text-[10px] text-slate-300 font-medium">BGN Nutrition Verified</span>
        </div>
        <h2 id="hero-menu-title" class="text-sm font-extrabold text-white mt-1 leading-snug">
          Nasi Gurih + Telur Rollade Bulat + Sambal Bawang + Edamame + Kakiage + Jeruk
        </h2>
        <div class="mt-2.5 pt-2 border-t border-slate-700 flex items-center justify-between text-[11px] text-slate-300">
          <span id="hero-nutrition">Energi 685 kkal • Protein 28 gr • Karbohidrat Kompleks & Serat</span>
          <span class="font-mono-num font-bold text-amber-300">3.000 Porsi</span>
        </div>
      </div>

      <!-- 3 TIM INTI SELECTOR -->
      <div class="bg-white border border-slate-200 p-2.5 rounded-2xl shadow-xs space-y-2">
        <div class="flex items-center justify-between px-1">
          <span class="text-[11px] font-extrabold text-slate-800 uppercase tracking-wide">Pilih Stasiun Kerja Tim</span>
          <span class="text-[10px] text-slate-500 font-medium">Note otomatis muncul seketika</span>
        </div>
        <div class="grid grid-cols-3 gap-2">
          <button onclick="selectStationDirective('persiapan')" id="directive-btn-persiapan" class="py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-emerald-600 text-white shadow-sm border border-emerald-700 cursor-pointer transition-all">
            <span class="flex items-center gap-1">
              <span class="w-2 h-2 rounded-full bg-white"></span>
              <span>TIM PERSIAPAN</span>
            </span>
            <span class="text-[9px] font-normal opacity-90">Kupas, Potong, Cuci</span>
          </button>

          <button onclick="selectStationDirective('pengolahan')" id="directive-btn-pengolahan" class="py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-white text-slate-700 hover:bg-slate-50 border border-slate-200 cursor-pointer transition-all">
            <span class="flex items-center gap-1">
              <span class="w-2 h-2 rounded-full bg-amber-500"></span>
              <span>TIM PENGOLAHAN</span>
            </span>
            <span class="text-[9px] font-normal opacity-90">Masak, Suhu Inti 75°C</span>
          </button>

          <button onclick="selectStationDirective('pemorsian')" id="directive-btn-pemorsian" class="py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-white text-slate-700 hover:bg-slate-50 border border-slate-200 cursor-pointer transition-all">
            <span class="flex items-center gap-1">
              <span class="w-2 h-2 rounded-full bg-blue-500"></span>
              <span>TIM PEMORSIAN</span>
            </span>
            <span class="text-[9px] font-normal opacity-90">Ompreng & Buah Segar</span>
          </button>
        </div>
      </div>

      <!-- OTOMATIS TERLAMPIR SEPERTI STICKY NOTE DARI CHEF LUTFI -->
      <div id="sticky-chef-note" class="note-paper-persiapan p-3.5 rounded-2xl transition-all">
        <div class="flex items-start justify-between">
          <div class="flex items-center gap-2">
            <span class="w-5 h-5 rounded-full bg-emerald-600 text-white flex items-center justify-center text-xs font-black shadow-xs">📌</span>
            <div>
              <span id="note-team-title" class="font-extrabold text-xs text-emerald-950 uppercase tracking-wide">NOTE RESMI CHEF LUTFI • TIM PERSIAPAN</span>
              <p class="text-[10px] text-emerald-700 font-semibold">Otomatis tersiar dari resep mingguan Chef Lutfi</p>
            </div>
          </div>
          <span class="text-[9px] font-bold bg-white text-emerald-800 px-2 py-0.5 rounded-md border border-emerald-200 shadow-2xs">Langsung Aktif</span>
        </div>

        <div id="note-team-body" class="mt-2.5 pt-2 border-t border-emerald-200/60 text-xs text-slate-800 space-y-1 font-medium leading-relaxed">
          <p>• Kupas bersih bahan nabati (wortel/kol), buang serat dan bagian layu.</p>
          <p>• Potong korek api halus seragam untuk bahan sayur kakiage agar renyah sempurna saat digoreng.</p>
          <p>• Cuci tiga kali dengan air mengalir. Setelah ditimbang di stasiun ini, kirim langsung ke Tim Pengolahan.</p>
        </div>
      </div>

      <!-- Dynamic Menu Items Container with attached note slips -->
      <div id="menu-items-container" class="space-y-3">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 2: ASLAP (PENERIMAAN & KONTROL MASUK)   -->
    <!-- ============================================== -->
    <section id="screen-aslap" class="space-y-3 hidden">
      <div class="note-paper-aslap p-3.5 rounded-2xl">
        <div class="flex items-start justify-between">
          <div class="flex items-center gap-2">
            <span class="w-6 h-6 rounded-lg bg-purple-600 text-white flex items-center justify-center text-xs font-bold shadow-xs">📋</span>
            <div>
              <h2 class="text-xs font-extrabold text-purple-950 uppercase tracking-wide">KONTROL ASISTEN LAPANGAN (ASLAP)</h2>
              <p class="text-[10px] text-purple-700 font-medium">Bahan datang otomatis terisi dari Menu Chef Lutfi tanpa ketik manual</p>
            </div>
          </div>
          <button onclick="openPrintModal()" class="px-2.5 py-1.5 bg-purple-600 hover:bg-purple-700 text-white text-[10px] font-extrabold rounded-xl shadow-sm flex items-center gap-1 cursor-pointer">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
            <span>Cetak A4 (1-Klik)</span>
          </button>
        </div>

        <div class="mt-3 pt-2.5 border-t border-purple-200/60 flex items-center justify-between text-xs">
          <span class="text-purple-900 font-bold">Hari: <span id="aslap-day-label" class="font-extrabold underline">SENIN</span> (Target 3.000 Porsi)</span>
          <span id="aslap-item-count" class="text-[10px] bg-purple-100 text-purple-800 font-mono-num font-bold px-2 py-0.5 rounded-full">6 Bahan Baku</span>
        </div>
      </div>

      <!-- Checklist Penerimaan Bahan Baku ASLAP -->
      <div class="bg-white border border-slate-200 p-3.5 rounded-2xl shadow-xs space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-xs font-extrabold text-slate-900 uppercase">Daftar Bahan Datang Hari Ini</h3>
          <span class="text-[10px] text-slate-500 font-medium">BGN Standar Penerimaan</span>
        </div>
        
        <div id="aslap-items-container" class="space-y-2">
          <!-- Rendered by JavaScript -->
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 3: FORM PENIMBANGAN (OCR & MANUAL)      -->
    <!-- ============================================== -->
    <section id="screen-home" class="space-y-3 hidden">
      
      <!-- Banner Notifikasi Autofill dari Menu -->
      <div id="autofill-banner" class="hidden bg-emerald-50 border border-emerald-300 p-3 rounded-2xl shadow-xs space-y-1.5 transition-all">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-600 animate-pulse"></span>
            <span id="autofill-banner-text" class="text-xs font-extrabold text-emerald-950 uppercase tracking-wide">Bahan Dimuat Otomatis dari Menu</span>
          </div>
          <button onclick="dismissAutofillBanner()" class="text-emerald-700 hover:text-emerald-900 text-xs font-black">✕</button>
        </div>
        <div id="autofill-directive-text" class="text-[11px] text-emerald-900 bg-white/70 p-2 rounded-xl border border-emerald-200">
        </div>
      </div>

      <!-- STATION SELECTOR CHIPS -->
      <div class="bg-white border border-slate-200 p-2.5 rounded-2xl shadow-xs space-y-2">
        <div class="flex items-center justify-between px-1">
          <span class="text-[11px] font-extrabold text-slate-800 uppercase tracking-wide">Stasiun Tim Kerja</span>
          <span id="current-stage-badge" class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full">Penerimaan & Sortir Persiapan</span>
        </div>
        <div class="grid grid-cols-3 gap-1.5">
          <button onclick="selectTeam('TIM PERSIAPAN')" class="team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-emerald-600 text-white shadow-sm flex items-center justify-center gap-1 cursor-pointer" data-team="TIM PERSIAPAN">
            <span>Persiapan</span>
          </button>
          <button onclick="selectTeam('TIM PENGOLAHAN')" class="team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1 cursor-pointer" data-team="TIM PENGOLAHAN">
            <span>Pengolahan</span>
          </button>
          <button onclick="selectTeam('TIM PEMORSIAN')" class="team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1 cursor-pointer" data-team="TIM PEMORSIAN">
            <span>Pemorsian</span>
          </button>
        </div>
      </div>

      <!-- DIGITAL SCALE READOUT DISPLAY -->
      <div class="bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-white p-4 rounded-3xl shadow-xl border border-slate-800 text-center relative overflow-hidden">
        <div class="flex items-center justify-between text-xs text-slate-400 mb-1">
          <span class="font-bold flex items-center gap-1 text-[11px]">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span>INDIKATOR TIMBANGAN AKTIF</span>
          </span>
          <span class="text-[10px] font-mono-num text-slate-500">MAX: 150.00 kg • DIV: 0.01 kg</span>
        </div>

        <div class="py-2">
          <div id="scale-display" class="font-mono-num text-5xl font-black tracking-tight text-emerald-400 drop-shadow-[0_0_15px_rgba(52,211,153,0.3)]">
            25.00 <span class="text-xl text-slate-400 font-bold">kg</span>
          </div>
          <p id="scale-subtext" class="text-xs text-slate-400 mt-1 font-semibold">Netto Bersih Bahan Siap Olah</p>
        </div>

        <!-- TOMBOL FOTO KAMERA OCR (PROPRIETARY MBG ENGINE) -->
        <div class="pt-3 border-t border-slate-800/80 flex items-center justify-center gap-2">
          <button onclick="triggerCameraOCR()" class="w-full py-2.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all active:scale-98">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
            <span>Foto Kamera Indikator Timbangan (OCR)</span>
          </button>
        </div>
      </div>

      <!-- INPUT FORM DETAIL PENIMBANGAN -->
      <div class="bg-white border border-slate-200 p-3.5 rounded-2xl shadow-xs space-y-3">
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="text-[11px] font-bold text-slate-700 block mb-1">Nama Bahan Baku</label>
            <input type="text" id="input-item" value="Beras Putih (Nasi Gurih)" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
          </div>
          <div>
            <label class="text-[11px] font-bold text-slate-700 block mb-1">Kategori Gizi</label>
            <input type="text" id="input-kategori" value="Karbohidrat" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500">
          </div>
        </div>

        <!-- Perhitungan Bruto, Tara, Netto -->
        <div class="grid grid-cols-3 gap-2">
          <div>
            <label class="text-[11px] font-bold text-slate-700 block mb-1">Bruto (kg)</label>
            <input type="number" step="0.01" id="input-bruto" value="25.85" oninput="calculateNetto()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-2 text-xs font-bold font-mono-num text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
          </div>
          <div>
            <label class="text-[11px] font-bold text-slate-700 block mb-1">Tara Wadah (kg)</label>
            <input type="number" step="0.01" id="input-tare" value="0.85" oninput="calculateNetto()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-2 text-xs font-bold font-mono-num text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
          </div>
          <div>
            <label class="text-[11px] font-bold text-slate-700 block mb-1">Netto (kg)</label>
            <input type="number" step="0.01" id="input-netto" value="25.00" readonly class="w-full bg-emerald-50 border border-emerald-300 rounded-xl px-2.5 py-2 text-xs font-black font-mono-num text-emerald-700 focus:outline-none">
          </div>
        </div>

        <!-- Preset Tara Cepat -->
        <div class="flex items-center gap-1.5 pt-1">
          <span class="text-[10px] font-bold text-slate-500">Preset Tara Wadah:</span>
          <button onclick="setTare(0.85)" class="px-2 py-0.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-[10px] font-bold font-mono-num">Kranjang (0.85 kg)</button>
          <button onclick="setTare(0.50)" class="px-2 py-0.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-[10px] font-bold font-mono-num">Baskom (0.50 kg)</button>
          <button onclick="setTare(0.00)" class="px-2 py-0.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-[10px] font-bold font-mono-num">Nol (0.00)</button>
        </div>

        <div>
          <label class="text-[11px] font-bold text-slate-700 block mb-1">Catatan Tambahan (Opsional)</label>
          <input type="text" id="input-catatan" value="Sesuai Note Chef: Nasi gurih santan pandan" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500">
        </div>

        <!-- Tombol Masukkan ke Keranjang Penimbangan -->
        <button onclick="addToStagingCart()" class="w-full py-3 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all active:scale-98">
          <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/></svg>
          <span>Masukkan ke Keranjang Timbangan</span>
        </button>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 4: KERANJANG PENIMBANGAN (STAGING)      -->
    <!-- ============================================== -->
    <section id="screen-staging" class="space-y-3 hidden">
      <div class="bg-white border border-slate-200 p-3 rounded-2xl shadow-xs flex items-center justify-between">
        <div>
          <h2 class="text-xs font-bold text-slate-900 uppercase tracking-wide">Keranjang Penimbangan</h2>
          <p class="text-[10px] text-slate-500 font-medium">Bisa diedit atau dihapus sebelum sync ke Google Sheet</p>
        </div>
        <span id="staging-count-badge" class="bg-emerald-600 text-white font-mono-num text-xs font-extrabold px-2.5 py-0.5 rounded-full">
          3 Item
        </span>
      </div>

      <div id="staging-items-list" class="space-y-2.5">
      </div>

      <div class="pt-2">
        <button onclick="syncAllToGoogleSheets()" id="btn-sync-all" class="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all active:scale-98">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/></svg>
          <span>Sinkronkan ke Google Sheets Monitoring</span>
        </button>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 5: STOK GUDANG                          -->
    <!-- ============================================== -->
    <section id="screen-stock" class="space-y-3 hidden">
      <div class="bg-white border border-slate-200 p-3.5 rounded-2xl shadow-xs">
        <h2 class="text-xs font-bold text-slate-900 uppercase tracking-wide mb-1">Stok Bahan Masuk Dapur MBG</h2>
        <p class="text-[10px] text-slate-500 mb-3">Monitoring stok real-time SPPG Kedungwuni Pekajangan 4</p>
        
        <div class="space-y-2">
          <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-slate-800 block">Beras Putih Premium</span>
              <p class="text-[10px] text-slate-500">Karbohidrat • Masuk: 450.00 kg • Sisa: 120.00 kg</p>
            </div>
            <span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 font-mono-num">Aman</span>
          </div>

          <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-slate-800 block">Telur Ayam Rollade</span>
              <p class="text-[10px] text-slate-500">Protein Hewani • Masuk: 3.000 butir • Sisa: 450 butir</p>
            </div>
            <span class="text-xs font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded border border-amber-200 font-mono-num">Sedang</span>
          </div>

          <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-slate-800 block">Jeruk Manis Segar</span>
              <p class="text-[10px] text-slate-500">Buah Segar • Masuk: 3.000 pcs • Khusus Pemorsian</p>
            </div>
            <span class="text-xs font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded border border-blue-200 font-mono-num">Siap Saji</span>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- ======================================================== -->
  <!-- MODAL KHUSUS INPUT / EDIT RESEP CHEF (SENIN - JUMAT)    -->
  <!-- ======================================================== -->
  <div id="chef-recipe-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center p-3 hidden no-print">
    <div class="bg-white rounded-2xl w-full max-w-lg max-h-[92vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden">
      <div class="bg-gradient-to-r from-amber-600 to-amber-700 text-white px-4 py-3 flex items-center justify-between border-b border-amber-800">
        <div class="flex items-center gap-2">
          <span class="text-base">👨‍🍳</span>
          <div>
            <h3 class="text-xs font-extrabold uppercase">Kontrol Resep & Arahan Head Chef</h3>
            <p class="text-[9px] text-amber-100">Sekali simpan langsung tersiar otomatis ke semua tim</p>
          </div>
        </div>
        <button onclick="closeChefRecipeModal()" class="text-white/80 hover:text-white font-bold text-sm px-2 cursor-pointer">✕</button>
      </div>

      <div class="p-4 overflow-y-auto space-y-3.5 text-xs text-slate-800">
        <!-- PILIH SIKLUS & HARI RESEP -->
        <div>
          <label class="font-extrabold text-slate-700 block mb-1">Pilih Siklus & Hari Menu</label>
          <div class="grid grid-cols-2 gap-2 mb-2">
            <button onclick="selectChefFormCycle('cycle1')" id="chef-cycle-1" class="py-1.5 rounded-lg font-extrabold text-[10px] bg-amber-600 text-white cursor-pointer">Siklus 1 (16-20 Nov)</button>
            <button onclick="selectChefFormCycle('cycle2')" id="chef-cycle-2" class="py-1.5 rounded-lg font-extrabold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">Siklus 2 (23-27 Nov)</button>
          </div>
          <div class="grid grid-cols-5 gap-1.5">
            <button onclick="loadDayRecipeToForm('senin')" id="chef-day-senin" class="chef-day-btn py-1.5 rounded-lg font-bold text-[10px] bg-slate-900 text-white cursor-pointer">SENIN</button>
            <button onclick="loadDayRecipeToForm('selasa')" id="chef-day-selasa" class="chef-day-btn py-1.5 rounded-lg font-bold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">SELASA</button>
            <button onclick="loadDayRecipeToForm('rabu')" id="chef-day-rabu" class="chef-day-btn py-1.5 rounded-lg font-bold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">RABU</button>
            <button onclick="loadDayRecipeToForm('kamis')" id="chef-day-kamis" class="chef-day-btn py-1.5 rounded-lg font-bold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">KAMIS</button>
            <button onclick="loadDayRecipeToForm('jumat')" id="chef-day-jumat" class="chef-day-btn py-1.5 rounded-lg font-bold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">JUMAT</button>
          </div>
        </div>

        <div>
          <label class="font-bold text-slate-700 block mb-1">Nama Menu Lengkap</label>
          <textarea id="chef-form-title" rows="2" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5 text-xs font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-amber-500"></textarea>
        </div>

        <div>
          <label class="font-bold text-slate-700 block mb-1">Kandungan Gizi BGN</label>
          <input type="text" id="chef-form-nutrition" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-medium text-slate-900">
        </div>

        <!-- ARAHAN SPESIFIK 3 TIM -->
        <div class="space-y-2.5 pt-2 border-t border-slate-100">
          <div class="note-paper-persiapan p-2.5 rounded-xl space-y-1">
            <label class="font-extrabold text-emerald-950 block text-[11px]">📌 Arahan Resep: TIM PERSIAPAN</label>
            <textarea id="chef-form-note-persiapan" rows="2" class="w-full bg-white border border-emerald-200 rounded-lg p-2 text-xs font-medium text-slate-900" placeholder="Instruksi kupas, potong, dan bilas..."></textarea>
          </div>

          <div class="note-paper-pengolahan p-2.5 rounded-xl space-y-1">
            <label class="font-extrabold text-amber-950 block text-[11px]">📌 Arahan Resep: TIM PENGOLAHAN (MASAK)</label>
            <textarea id="chef-form-note-pengolahan" rows="2" class="w-full bg-white border border-amber-200 rounded-lg p-2 text-xs font-medium text-slate-900" placeholder="Instruksi bumbu, suhu inti minimal 75°C, waktu masak..."></textarea>
          </div>

          <div class="note-paper-pemorsian p-2.5 rounded-xl space-y-1">
            <label class="font-extrabold text-blue-950 block text-[11px]">📌 Arahan Resep: TIM PEMORSIAN & BUAH</label>
            <textarea id="chef-form-note-pemorsian" rows="2" class="w-full bg-white border border-blue-200 rounded-lg p-2 text-xs font-medium text-slate-900" placeholder="Instruksi sekat ompreng, gramatur, dan SOP buah segar..."></textarea>
          </div>
        </div>

        <!-- SINKRONISASI KE GOOGLE SHEET -->
        <div class="bg-slate-50 p-2.5 rounded-xl border border-slate-200 flex items-center justify-between text-[11px]">
          <span class="text-slate-600 font-medium">Bisa juga diedit langsung di Google Sheet:</span>
          <a href="https://docs.google.com/spreadsheets/d/13EctW99CUaaYbx59IZoSh9aJKdRagrZk4kH-0AM1sIM/edit#gid=0" target="_blank" class="text-emerald-700 font-bold hover:underline">Tab Menu_Mingguan ↗</a>
        </div>
      </div>

      <div class="p-3 bg-slate-50 border-t border-slate-200 flex gap-2">
        <button onclick="closeChefRecipeModal()" class="flex-1 py-2.5 bg-slate-200 hover:bg-slate-300 text-slate-700 rounded-xl text-xs font-bold cursor-pointer">Batal</button>
        <button onclick="saveChefRecipeForm()" class="flex-2 py-2.5 bg-amber-600 hover:bg-amber-700 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-1.5 cursor-pointer active:scale-98">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
          <span>Simpan & Siarkan ke Semua Tim</span>
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL CETAK FORM MONITORING ASLAP (PRINT A4) -->
  <div id="print-aslap-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center p-3 hidden no-print">
    <div class="bg-white rounded-2xl w-full max-w-xl max-h-[92vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden">
      <div class="bg-slate-900 text-white px-4 py-3 flex items-center justify-between border-b border-slate-800">
        <div class="flex items-center gap-2">
          <span class="text-xs font-extrabold text-white">Formulir Monitoring Penerimaan Bahan Baku ASLAP</span>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="window.print()" class="px-3 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold flex items-center gap-1 cursor-pointer shadow-sm">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
            <span>Cetak / Print Langsung</span>
          </button>
          <button onclick="closePrintModal()" class="text-slate-400 hover:text-white font-bold text-sm px-2 cursor-pointer">✕</button>
        </div>
      </div>
      
      <div class="p-4 overflow-y-auto bg-slate-100 flex-1 flex justify-center">
        <div id="modal-form-preview" class="bg-white p-5 rounded-xl shadow-sm border border-slate-200 w-full text-slate-900 text-xs space-y-3">
        </div>
      </div>
    </div>
  </div>

  <!-- PRINTABLE CONTAINER (FOR BROWSER PRINT ENGINE) -->
  <div id="printable-aslap-form" class="hidden">
  </div>

  <!-- MODAL EDIT ITEM KERANJANG -->
  <div id="edit-cart-modal" class="fixed inset-0 bg-slate-950/70 z-50 flex items-center justify-center p-3 hidden no-print">
    <div class="bg-white rounded-2xl w-full max-w-sm p-4 shadow-2xl border border-slate-200 space-y-3">
      <div class="flex items-center justify-between border-b border-slate-100 pb-2">
        <h3 class="text-xs font-extrabold text-slate-900 uppercase">Koreksi Timbangan</h3>
        <button onclick="closeEditModal()" class="text-slate-400 hover:text-slate-700 font-bold text-sm">✕</button>
      </div>

      <input type="hidden" id="edit-item-id">

      <div>
        <label class="text-[11px] font-bold text-slate-700 block mb-1">Nama Bahan</label>
        <input type="text" id="edit-item-name" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-900">
      </div>

      <div>
        <label class="text-[11px] font-bold text-slate-700 block mb-1">Stasiun Tim</label>
        <select id="edit-item-team" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800">
          <option value="TIM PERSIAPAN">TIM PERSIAPAN</option>
          <option value="TIM PENGOLAHAN">TIM PENGOLAHAN</option>
          <option value="TIM PEMORSIAN">TIM PEMORSIAN</option>
        </select>
      </div>

      <div class="grid grid-cols-2 gap-2">
        <div>
          <label class="text-[11px] font-bold text-slate-700 block mb-1">Bruto (kg)</label>
          <input type="number" step="0.01" id="edit-item-bruto" oninput="recalcEditNetto()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold font-mono-num">
        </div>
        <div>
          <label class="text-[11px] font-bold text-slate-700 block mb-1">Tara (kg)</label>
          <input type="number" step="0.01" id="edit-item-tara" oninput="recalcEditNetto()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold font-mono-num">
        </div>
      </div>

      <div class="bg-slate-50 border border-slate-200 p-2.5 rounded-xl flex items-center justify-between">
        <span class="text-xs font-bold text-slate-600">Netto Terkoreksi:</span>
        <span id="edit-item-netto-display" class="text-sm font-extrabold text-emerald-600 font-mono-num">0.00 kg</span>
      </div>

      <div>
        <label class="text-[11px] font-bold text-slate-700 block mb-1">Catatan Koreksi</label>
        <input type="text" id="edit-item-catatan" placeholder="Misal: Koreksi wadah tara ember" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs">
      </div>

      <div class="flex gap-2 pt-2 border-t border-slate-100">
        <button onclick="closeEditModal()" class="flex-1 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-xl text-xs font-bold">Batal</button>
        <button onclick="saveEditCartItem()" class="flex-1 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold shadow-sm">Simpan Perubahan</button>
      </div>
    </div>
  </div>

  <!-- NOTIFICATION TOAST -->
  <div id="toast" class="fixed bottom-4 left-1/2 -translate-x-1/2 bg-slate-900 text-white px-4 py-2.5 rounded-xl text-xs font-bold shadow-2xl flex items-center gap-2 transition-all opacity-0 pointer-events-none z-50 no-print">
    <span id="toast-msg">Notifikasi</span>
  </div>

<script>
// ========================================================
// DATA RENCANA MENU RESMI 16 - 27 NOVEMBER 2026 (2 SIKLUS)
// ========================================================
const weeklyMenuCycles = {{
  cycle1: {{
    label: "Siklus 1: 16 - 20 November 2026",
    days: {{
      senin: {{
        title: "Nasi Gurih + Telur Rollade Bulat + Sambal Bawang + Edamame + Kakiage + Jeruk",
        nutrition: "Energi 685 kkal • Protein 28 gr • Karbohidrat Kompleks & Serat",
        notePersiapan: "Kupas bersih wortel dan kol untuk kakiage, potong korek api halus. Cuci bersih edamame segar.",
        notePengolahan: "Masak nasi gurih santan pandan aron-kukus matang merata. Goreng rollade telur bulat hingga keemasan. Tumis sambal bawang hingga tanak.",
        notePemorsian: "Ompreng diisi nasi gurih sekat utama, 1 rollade telur di sekat lauk, kakiage & edamame. Jeruk dilap kering steril di sekat buah.",
        items: [
          {{ name: "Beras Putih (Nasi Gurih)", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras bersih, tiriskan sempurna.", pengolahan: "Aron dengan santan encer & daun pandan, kukus hingga pulen mekar.", pemorsian: "Takar 150 gr di sekat nasi utama." }},
          {{ name: "Telur Ayam Rollade Bulat", category: "Protein Hewani", portion: "1 rollade", targetOrder: "3.000 butir", supplier: "Peternakan Unggas Barokah", tare: "0.85", persiapan: "Siapkan adonan dadar gulung rollade isi.", pengolahan: "Kukus adonan rollade, potong bulat tebal seragam, goreng keemasan suhu 165°C.", pemorsian: "Tata 1 potong bulat di sekat lauk utama." }},
          {{ name: "Sambal Bawang", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "45.00 kg", supplier: "Pasar Induk Sayur & Bumbu", tare: "0.50", persiapan: "Kupas cabai & bawang merah, cuci tiris.", pengolahan: "Goreng sebentar cabai & bawang, ulek kasar, tumis hingga matang tanak harum.", pemorsian: "Sendokkan 15 gr di samping lauk utama." }},
          {{ name: "Edamame Segar Rebus", category: "Protein Nabati", portion: "40 gr", targetOrder: "120.00 kg", supplier: "Kelompok Tani Pekajangan", tare: "0.50", persiapan: "Sortir polong edamame segar, potong tangkai, bilas 3x.", pengolahan: "Rebus dalam air garam ringan mendidih selama 5-6 menit, tiriskan.", pemorsian: "Tata 40 gr di sekat sayur/lauk pendamping." }},
          {{ name: "Kakiage (Bakwan Jepang)", category: "Sayuran Segar", portion: "60 gr", targetOrder: "180.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Iris wortel, bawang bombay, dan kol bentuk korek api tipis.", pengolahan: "Campur adonan tepung encer es, goreng terendam minyak hingga krispi renyah.", pemorsian: "Takar 1 pcs kakiage krispi di sekat sayur ompreng." }},
          {{ name: "Jeruk Manis Segar", category: "Buah Segar", portion: "1 pcs", targetOrder: "3.000 pcs", supplier: "Distributor Buah Nusantara", tare: "0.00", persiapan: "TIM PERSIAPAN TIDAK MENANGANI BUAH. Langsung serahkan ke Pemorsian.", pengolahan: "Dilarang terkena panas kompor dapur.", pemorsian: "SOP BUAH SEGAR: Gunakan sarung tangan steril baru, lap permukaan kulit jeruk dengan kain sanitasi kering, letakkan di sekat buah." }}
        ]
      }},
      selasa: {{
        title: "Nasi Putih + Chicken Drum Stick + Saus BBQ + Stik Tempe Tepung + Mix Vigie + Semangka",
        nutrition: "Energi 720 kkal • Protein 31 gr • Kaya Vitamin A & C",
        notePersiapan: "Potong tempe bentuk stik 6x1 cm seragam. Cuci bersih paha ayam drum stick dan tiriskan sempurna.",
        notePengolahan: "Balur paha ayam tepung krispi, goreng deep fry suhu 160°C. Suhu inti wajib >= 75°C. Tumis mix vigie cepat dengan butter gurih.",
        notePemorsian: "Suhu saji ayam hangat 60°C. Semangka dipotong juring tebal 2 cm dengan talenan kuning khusus buah di sekat dingin.",
        items: [
          {{ name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras hingga bersih.", pengolahan: "Takar air presisi, masak di rice steamer hingga pulen mekar.", pemorsian: "Cetak 150 gr di sekat nasi utama." }},
          {{ name: "Chicken Drum Stick (Paha Ayam)", category: "Protein Hewani", portion: "1 potong (75 gr)", targetOrder: "225.00 kg", supplier: "PT Unggas Sejahtera", tare: "0.85", persiapan: "Bilas ayam dengan air mengalir, marinasi bumbu bawang putih lada 30 menit.", pengolahan: "Balur tepung krispi, goreng deep frying suhu 160°C hingga emas kecokelatan. Cek suhu inti >= 75°C.", pemorsian: "Tata 1 potong drum stick di sekat lauk utama." }},
          {{ name: "Saus BBQ Racikan Dapur", category: "Bumbu / Pelengkap", portion: "20 gr", targetOrder: "60.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Racik saus tomat, saus tiram, kecap inggris, lada hitam halus.", pengolahan: "Masak api kecil hingga mengental gurih berkilap.", pemorsian: "Siramkan 20 gr di atas chicken drum stick." }},
          {{ name: "Stik Tempe Tepung", category: "Protein Nabati", portion: "45 gr", targetOrder: "135.00 kg", supplier: "Koperasi Tempe Barokah", tare: "0.50", persiapan: "Potong tempe bentuk stik 6x1 cm, celup adonan tepung renyah.", pengolahan: "Goreng hingga renyah garing keemasan, tiriskan minyak.", pemorsian: "Tata 2 stik tempe mendampingi ayam." }},
          {{ name: "Mix Vigie (Jagung, Polong, Wortel)", category: "Sayuran Segar", portion: "60 gr", targetOrder: "180.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Pipil jagung manis, kupas wortel potong dadu 5 mm, siangi kacang polong.", pengolahan: "Tumis cepat (stir-fry) dengan mentega gurih api besar agar warna tetap cerah.", pemorsian: "Takar 60 gr di sekat sayur ompreng." }},
          {{ name: "Semangka Merah Potong", category: "Buah Segar", portion: "80 gr (1 juring)", targetOrder: "240.00 kg", supplier: "Distributor Buah Nusantara", tare: "0.85", persiapan: "Khusus Tim Pemorsian. Gunakan talenan kuning steril.", pengolahan: "Dilarang terkena panas/kompor dapur.", pemorsian: "SOP BUAH SEGAR: Potong juring tebal 2 cm, buang biji hitam, tata rapi di sekat buah ompreng." }}
        ]
      }},
      rabu: {{
        title: "Nasi Putih + Bola Bakso Daging Isi 3 + Saus Bangkok + Tahu Goreng + Kol Wortel + Pisang",
        nutrition: "Energi 675 kkal • Protein 27 gr • Tinggi Zat Besi & Mineral",
        notePersiapan: "Iris tipis kol dan wortel koin. Rendam tahu dalam air garam bawang putih 10 menit.",
        notePengolahan: "Rebus bola bakso sapi dalam kuah kaldu rempah suhu inti 75°C. Goreng tahu hingga berkulit krispi.",
        notePemorsian: "Sajikan 3 butir bakso disiram saus bangkok di sekat lauk. Pisang cavendish diletakkan di sekat buah kering.",
        items: [
          {{ name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras tiris.", pengolahan: "Masak hingga pulen standar BGN.", pemorsian: "150 gr sekat utama." }},
          {{ name: "Bola Bakso Daging Sapi (Isi 3)", category: "Protein Hewani", portion: "3 butir (65 gr)", targetOrder: "195.00 kg", supplier: "RPH Pekalongan Prima", tare: "0.85", persiapan: "Sortir bola bakso utuh higienis.", pengolahan: "Rebus dalam kuah kaldu sapi mendidih perlahan. Pastikan suhu minimal 75°C.", pemorsian: "Tata 3 butir bakso di sekat lauk." }},
          {{ name: "Saus Bangkok Asam Manis", category: "Bumbu / Pelengkap", portion: "20 gr", targetOrder: "60.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Cincang bawang putih, cabai merah halus.", pengolahan: "Masak saus bangkok asam manis hingga mengental pekat.", pemorsian: "Siramkan di atas bakso daging." }},
          {{ name: "Tahu Goreng Gurih", category: "Protein Nabati", portion: "45 gr", targetOrder: "135.00 kg", supplier: "Koperasi Tahu Kedungwuni", tare: "0.50", persiapan: "Potong tahu kotak 3x3 cm, rendam larutan bawang garam.", pengolahan: "Goreng minyak panas 160°C sampai berkulit gurih.", pemorsian: "Tata 1 potong tahu di samping bakso." }},
          {{ name: "Tumis Kol Wortel", category: "Sayuran Segar", portion: "60 gr", targetOrder: "180.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Iris kol tipis, wortel koin 2 mm, cuci bersih 3x air mengalir.", pengolahan: "Tumis dengan bawang putih lada hingga harum renyah.", pemorsian: "Takar 60 gr di sekat sayur." }},
          {{ name: "Pisang Cavendish", category: "Buah Segar", portion: "1 pcs", targetOrder: "3.000 pcs", supplier: "Distributor Buah Nusantara", tare: "0.00", persiapan: "Khusus Tim Pemorsian.", pengolahan: "Dilarang kontak dengan suhu panas.", pemorsian: "SOP BUAH SEGAR: Gunakan sarung tangan steril, sortir kulit mulus, sajikan di sekat buah." }}
        ]
      }},
      kamis: {{
        title: "Roti Tawar (2 Tangkup) + Telor Ceplok + Saus Mayo Pedas + Stik Tempe + Timun Selada + Pisang",
        nutrition: "Energi 690 kkal • Protein 26 gr • Lemak Sehat & Serat Alami",
        notePersiapan: "Cuci timun dan selada dengan air es steril sanitasi. Potong tempe stik renyah.",
        notePengolahan: "Goreng telor ceplok mata sapi hingga bagian kuning dan putih matang sempurna. Goreng stik tempe renyah.",
        notePemorsian: "Susun 2 lembar roti tawar dengan olesan mayo pedas dan telor ceplok. Tata lalap segar dan pisang di sekat kering.",
        items: [
          {{ name: "Roti Tawar Sandwich (2 Pcs)", category: "Karbohidrat", portion: "2 lembar", targetOrder: "6.000 pcs", supplier: "Bakery Mitra SPPG", tare: "0.50", persiapan: "Sortir roti empuk tanpa cacat kemasan.", pengolahan: "Panggang ringan (opsional) atau susun sandwich.", pemorsian: "Tata 2 tangkup roti tawar rapi di sekat utama." }},
          {{ name: "Telor Ceplok (Mata Sapi)", category: "Protein Hewani", portion: "1 butir (55 gr)", targetOrder: "3.000 butir", supplier: "Peternakan Unggas Barokah", tare: "0.85", persiapan: "QC kebersihan cangkang telur.", pengolahan: "Goreng ceplok di wajan cetak sampai bagian putih berkulit dan kuning matang sempurna.", pemorsian: "Letakkan telor ceplok di antara tangkup roti atau di sekat lauk." }},
          {{ name: "Saus Mayo Pedas Gurih", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "45.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Campur mayones premium dan saus cabai racikan.", pengolahan: "Aduk hingga homogen lembut.", pemorsian: "Oleskan merata pada roti sandwich." }},
          {{ name: "Stik Tempe Tepung", category: "Protein Nabati", portion: "45 gr", targetOrder: "135.00 kg", supplier: "Koperasi Tempe Barokah", tare: "0.50", persiapan: "Potong tempe stik memanjang, balur tepung ketumbar.", pengolahan: "Goreng renyah garing tiris minyak.", pemorsian: "Tata 2 stik tempe renyah di sekat lauk pendamping." }},
          {{ name: "Timun & Selada Segar Higienis", category: "Sayuran Segar", portion: "50 gr", targetOrder: "150.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Potong timun serong 3 mm, petik selada keriting hijau, cuci rendam air es 5 menit.", pengolahan: "Sayur mentah segar steril, tidak dimasak panas.", pemorsian: "Tiriskan kering, tata di sekat sayur ompreng." }},
          {{ name: "Pisang Cavendish", category: "Buah Segar", portion: "1 pcs", targetOrder: "3.000 pcs", supplier: "Distributor Buah Nusantara", tare: "0.00", persiapan: "Khusus Tim Pemorsian.", pengolahan: "Dilarang kontak panas.", pemorsian: "SOP BUAH: Sortir bersih kering, letakkan di sekat buah." }}
        ]
      }},
      jumat: {{
        title: "Nasi Gurih + Telur Katsu Krispi + Sambal Bawang + Tahu Goreng + Tumis Labu Jagung + Melon",
        nutrition: "Energi 705 kkal • Protein 28 gr • Kaya Beta Karoten & Vitamin C",
        notePersiapan: "Kupas labu siam buang getah dengan garam, serut korek api. Pipil jagung manis segar.",
        notePengolahan: "Balur telur dengan tepung panir katsu, goreng keemasan. Tumis labu siam jagung dengan bawang gurih.",
        notePemorsian: "Nasi gurih harum kelapa di sekat utama, telur katsu krispi berdampingan dengan tahu goreng dan sambal bawang. Melon di sekat dingin.",
        items: [
          {{ name: "Beras Putih (Nasi Gurih)", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras bersih tiris.", pengolahan: "Aron dan kukus dengan santan harum pandan.", pemorsian: "Takar 150 gr sekat utama." }},
          {{ name: "Telur Katsu Krispi", category: "Protein Hewani", portion: "1 pcs (60 gr)", targetOrder: "3.000 porsi", supplier: "Peternakan Unggas Barokah", tare: "0.85", persiapan: "Siapkan telur dadar tebal, potong porsi, balur tepung terigu, telur, dan panir kasar.", pengolahan: "Goreng minyak panas 165°C hingga panir kuning emas renyah. Tiriskan.", pemorsian: "Potong 3 bagian rapi di sekat lauk utama." }},
          {{ name: "Sambal Bawang Gurih", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "45.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Kupas cabai & bawang, cuci tiris.", pengolahan: "Ulek kasar, tumis minyak hingga tanak harum gurih.", pemorsian: "1 sendok di sekat lauk." }},
          {{ name: "Tahu Goreng Gurih", category: "Protein Nabati", portion: "45 gr", targetOrder: "135.00 kg", supplier: "Koperasi Tahu Kedungwuni", tare: "0.50", persiapan: "Potong tahu kotak, marinasi air garam.", pengolahan: "Goreng berkulit gurih.", pemorsian: "Tata 1 potong tahu mendampingi telur katsu." }},
          {{ name: "Tumis Labu Jagung Manis", category: "Sayuran Segar", portion: "60 gr", targetOrder: "180.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Kupas labu buang getah, serut kasar, pipil jagung manis.", pengolahan: "Tumis bumbu bawang putih lada dengan kuah kaldu gurih sedikit.", pemorsian: "Takar 60 gr di sekat sayur." }},
          {{ name: "Melon Cantaloupe Segar", category: "Buah Segar", portion: "80 gr (potong)", targetOrder: "240.00 kg", supplier: "Distributor Buah Nusantara", tare: "0.85", persiapan: "Khusus Tim Pemorsian.", pengolahan: "Dilarang terkena panas.", pemorsian: "SOP BUAH SEGAR: Kupas kulit melon, potong tebal 1.5 cm rapi, sajikan dingin tertutup di sekat buah." }}
        ]
      }}
    }}
  }},
  cycle2: {{
    label: "Siklus 2: 23 - 27 November 2026",
    days: {{
      senin: {{
        title: "Nasi Gurih + Lele Crispy + Sambal Bajak + Tempe Orek Kacang Panjang + Lalap Timun + Labu + Jeruk",
        nutrition: "Energi 715 kkal • Protein 32 gr • Kaya Omega-3 & Kalsium",
        notePersiapan: "QC raba lele fillet bebas duri, marinasi jeruk nipis & kunyit. Potong tempe dan kacang panjang 3 cm.",
        notePengolahan: "Goreng lele fillet balur tepung bumbu hingga garing krispi keemasan. Tumis orek tempe kacang panjang kecap manis gurih tanak.",
        notePemorsian: "Lele krispi disajikan bersama sambal bajak dan orek tempe. Jeruk dilap steril beralas sejuk.",
        items: [
          {{ name: "Beras Putih (Nasi Gurih)", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras bersih.", pengolahan: "Aron dan kukus gurih santan pandan.", pemorsian: "150 gr sekat nasi." }},
          {{ name: "Ikan Lele Crispy (Fillet)", category: "Protein Hewani", portion: "1 fillet (75 gr)", targetOrder: "225.00 kg", supplier: "Pembudidaya Ikan Segar Pekalongan", tare: "0.85", persiapan: "QC fillet lele tanpa duri, marinasi bumbu kunyit ketumbar bawang putih.", pengolahan: "Balur tepung krispi, goreng deep frying suhu 170°C sampai garing renyah.", pemorsian: "Tata 1 potong lele crispy di sekat lauk utama." }},
          {{ name: "Sambal Bajak Matang", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "45.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Haluskan cabai merah, tomat, terasi matang, gula merah.", pengolahan: "Tumis dengan minyak panas hingga warna merah tua matang tanak harum.", pemorsian: "Sendokkan 15 gr mendampingi lele crispy." }},
          {{ name: "Tempe Orek Kacang Panjang", category: "Protein Nabati", portion: "50 gr", targetOrder: "150.00 kg", supplier: "Koperasi Tempe Barokah", tare: "0.50", persiapan: "Potong tempe dadu kecil, goreng setengah kering. Potong kacang panjang 3 cm.", pengolahan: "Tumis bumbu iris lengkuas daun salam, masukkan tempe dan kacang panjang dengan kecap manis gurih.", pemorsian: "Takar 50 gr di sekat lauk pendamping." }},
          {{ name: "Lalap Timun + Labu Siam Kukus", category: "Sayuran Segar", portion: "60 gr", targetOrder: "180.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Potong labu siam kotak, potong timun serong higienis.", pengolahan: "Kukus labu siam 5 menit hingga empuk cerah; timun disajikan segar dingin.", pemorsian: "Tata di sekat sayur ompreng." }},
          {{ name: "Jeruk Manis Segar", category: "Buah Segar", portion: "1 pcs", targetOrder: "3.000 pcs", supplier: "Distributor Buah Nusantara", tare: "0.00", persiapan: "Khusus Tim Pemorsian.", pengolahan: "Dilarang kontak panas kompor.", pemorsian: "SOP BUAH: Lap permukaan kulit jeruk higienis, letakkan di sekat buah." }}
        ]
      }},
      selasa: {{
        title: "Nasi + Telor Ceplok + Sambal Kecap + Edamame + Kakiage + Pisang",
        nutrition: "Energi 680 kkal • Protein 27 gr • Serat & Antioksidan",
        notePersiapan: "Siangi sayuran kakiage bentuk korek. Cuci edamame segar.",
        notePengolahan: "Goreng telor ceplok matang sempurna. Rebus edamame air garam. Goreng kakiage krispi.",
        notePemorsian: "Tata telor ceplok disiram sambal kecap cabai rawit, kakiage, dan edamame. Pisang di sekat buah.",
        items: [
          {{ name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras tiris.", pengolahan: "Masak pulen rice steamer.", pemorsian: "150 gr sekat utama." }},
          {{ name: "Telor Ceplok (Mata Sapi)", category: "Protein Hewani", portion: "1 butir (55 gr)", targetOrder: "3.000 butir", supplier: "Peternakan Unggas Barokah", tare: "0.85", persiapan: "QC cangkang bersih.", pengolahan: "Goreng ceplok matang sempurna kedua sisi.", pemorsian: "1 butir sekat lauk utama." }},
          {{ name: "Sambal Kecap Rawit Bawang", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "45.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Iris cabai rawit merah & hijau, bawang merah.", pengolahan: "Campur kecap manis kental dan perasan jeruk limau segar.", pemorsian: "Siramkan di atas telor ceplok." }},
          {{ name: "Edamame Segar Rebus", category: "Protein Nabati", portion: "40 gr", targetOrder: "120.00 kg", supplier: "Kelompok Tani Pekajangan", tare: "0.50", persiapan: "Bilas edamame 3x.", pengolahan: "Rebus dalam air garam ringan 5 menit tiris.", pemorsian: "Tata di sekat pendamping." }},
          {{ name: "Kakiage Sayur Krispi", category: "Sayuran Segar", portion: "60 gr", targetOrder: "180.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Iris wortel kol bawang korek api.", pengolahan: "Goreng tepung krispi terendam minyak panas.", pemorsian: "1 pcs kakiage di sekat sayur." }},
          {{ name: "Pisang Cavendish", category: "Buah Segar", portion: "1 pcs", targetOrder: "3.000 pcs", supplier: "Distributor Buah Nusantara", tare: "0.00", persiapan: "Khusus Tim Pemorsian.", pengolahan: "Dilarang kontak panas.", pemorsian: "SOP BUAH: Sortir kulit mulus di sekat buah." }}
        ]
      }},
      rabu: {{
        title: "Nasi + Ayam Bumbu Hitam + Sambal Bawang + Tahu Goreng + Lalap Timun Selada + Kelengkeng",
        nutrition: "Energi 725 kkal • Protein 33 gr • Kaya Rempah Nusantara & Vitamin C",
        notePersiapan: "Potong ayam ukuran standar porsi. Cuci timun dan selada dengan air es steril.",
        notePengolahan: "Ungkep ayam dengan bumbu hitam khas Madura hingga rempah meresap dan bumbu menghitam gurih berminyak. Suhu inti >= 75°C. Goreng tahu gurih.",
        notePemorsian: "Ayam disiram bumbu hitam pekat gurih. Kelengkeng disortir segar utuh di sekat buah.",
        items: [
          {{ name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras.", pengolahan: "Masak pulen.", pemorsian: "150 gr sekat utama." }},
          {{ name: "Ayam Bumbu Hitam (Rempah Madura)", category: "Protein Hewani", portion: "1 potong (75 gr)", targetOrder: "225.00 kg", supplier: "PT Unggas Sejahtera", tare: "0.85", persiapan: "Bersihkan ayam, marinasi rempah bawang, keluwak, kemiri, serai.", pengolahan: "Ungkep perlahan hingga bumbu meresap ke serat daging dan menghitam wangi. Cek suhu inti >= 75°C.", pemorsian: "Tata 1 potong ayam balur bumbu hitam di sekat lauk." }},
          {{ name: "Sambal Bawang", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "45.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Kupas cabai & bawang.", pengolahan: "Tumis tanak harum gurih.", pemorsian: "15 gr di sekat lauk." }},
          {{ name: "Tahu Goreng Gurih", category: "Protein Nabati", portion: "45 gr", targetOrder: "135.00 kg", supplier: "Koperasi Tahu Kedungwuni", tare: "0.50", persiapan: "Potong tahu kotak, marinasi air bawang garam.", pengolahan: "Goreng minyak panas 160°C sampai berkulit gurih.", pemorsian: "1 potong mendampingi ayam." }},
          {{ name: "Lalap Timun & Selada Segar", category: "Sayuran Segar", portion: "60 gr", targetOrder: "180.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Potong timun serong, bilas selada air es sanitasi.", pengolahan: "Lalapan segar higienis.", pemorsian: "Tata rapi di sekat sayur ompreng." }},
          {{ name: "Kelengkeng Manis Segar", category: "Buah Segar", portion: "5-6 pcs (70 gr)", targetOrder: "210.00 kg", supplier: "Distributor Buah Nusantara", tare: "0.85", persiapan: "Khusus Tim Pemorsian.", pengolahan: "Dilarang terkena panas.", pemorsian: "SOP BUAH: Sortir kelengkeng mulus tanpa tangkai patah, tata 5-6 butir di sekat buah." }}
        ]
      }},
      kamis: {{
        title: "Nasi + Telur Fuyunghai + Saus Fuyunghai + Tempe Goreng + Polong + Wortel + Buah Naga",
        nutrition: "Energi 695 kkal • Protein 28 gr • Kaya Antioksidan Betasianin",
        notePersiapan: "Cincang sayur wortel dan kubis untuk fuyunghai. Potong dadu buah naga merah di ruang dingin.",
        notePengolahan: "Kocok telur bersama cincangan sayur dan ayam, dadar tebal matang merata suhu 75°C. Masak saus fuyunghai asam manis kacang polong wortel.",
        notePemorsian: "Telur fuyunghai disiram saus asam manis. Buah naga disajikan dalam sekat buah dingin.",
        items: [
          {{ name: "Beras Putih Premium", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras.", pengolahan: "Masak pulen.", pemorsian: "150 gr sekat utama." }},
          {{ name: "Telur Dadar Fuyunghai Tebal", category: "Protein Hewani", portion: "1 pcs (65 gr)", targetOrder: "3.000 porsi", supplier: "Peternakan Unggas Barokah", tare: "0.85", persiapan: "Cincang halus wortel, kol, daun bawang, campur kocokan telur dan sedikit tepung sagu.", pengolahan: "Goreng dadar tebal dalam minyak panas melimpah hingga matang mekar dan bagian dalam matang sempurna (suhu inti 75°C).", pemorsian: "Potong porsi rapi di sekat lauk utama." }},
          {{ name: "Saus Asam Manis Fuyunghai", category: "Bumbu / Pelengkap", portion: "25 gr", targetOrder: "75.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Siapkan saus tomat, gula cuka racik, larutan maizena.", pengolahan: "Masak saus mendidih meletup-letup kental berkilap.", pemorsian: "Siramkan di atas fuyunghai." }},
          {{ name: "Tempe Goreng Ketumbar", category: "Protein Nabati", portion: "45 gr", targetOrder: "135.00 kg", supplier: "Koperasi Tempe Barokah", tare: "0.50", persiapan: "Potong tempe, marinasi ketumbar garam.", pengolahan: "Goreng hingga gurih keemasan.", pemorsian: "1 potong di sekat pendamping." }},
          {{ name: "Kacang Polong & Wortel Rebus", category: "Sayuran Segar", portion: "60 gr", targetOrder: "180.00 kg", supplier: "Kelompok Tani Sayur", tare: "0.50", persiapan: "Potong wortel dadu kecil seragam dengan kacang polong.", pengolahan: "Rebus sebentar (blanching) air garam agar warna cerah renyah.", pemorsian: "Tata bersama saus di sekat sayur." }},
          {{ name: "Buah Naga Merah Potong", category: "Buah Segar", portion: "80 gr (dadu)", targetOrder: "240.00 kg", supplier: "Distributor Buah Nusantara", tare: "0.85", persiapan: "Khusus Tim Pemorsian. Talenan buah steril.", pengolahan: "Dilarang terkena panas.", pemorsian: "SOP BUAH SEGAR: Kupas kulit buah naga merah, potong dadu 2 cm rapi, simpan dingin tertutup sebelum masuk ompreng." }}
        ]
      }},
      jumat: {{
        title: "Nasi Gurih + Semur Telur Dadar + Sambal Bawang + Tahu Goreng + Gyoza Sayur Wortel Kol + Pisang",
        nutrition: "Energi 710 kkal • Protein 29 gr • Serat & Kalium Tinggi",
        notePersiapan: "Siapkan isian gyoza wortel kol cincang halus, bungkus kulit gyoza rapi. Dadar telur gulung semur.",
        notePengolahan: "Kukus atau pan fry gyoza sayur hingga matang transparan. Masak semur telur dadar dengan kuah kecap rempah meresap gurih.",
        notePemorsian: "Nasi gurih harum kelapa di sekat utama, semur telur dadar disiram kuah semur kental gurih, gyoza sayur dan pisang cavendish di sekat buah.",
        items: [
          {{ name: "Beras Putih (Nasi Gurih)", category: "Karbohidrat", portion: "150 gr", targetOrder: "450.00 kg", supplier: "Koperasi Tani Kedungwuni", tare: "0.85", persiapan: "Cuci beras.", pengolahan: "Aron dan kukus harum santan pandan.", pemorsian: "150 gr sekat utama." }},
          {{ name: "Semur Telur Dadar Gulung", category: "Protein Hewani", portion: "1 gulung (65 gr)", targetOrder: "3.000 porsi", supplier: "Peternakan Unggas Barokah", tare: "0.85", persiapan: "Kocok telur bumbu seledri bawang, dadar lembaran tebal, gulung padat.", pengolahan: "Masak gulungan telur dadar dalam kuah semur kecap pala cengkeh hingga bumbu meresap gurih.", pemorsian: "Potong serong rapi di sekat lauk utama." }},
          {{ name: "Sambal Bawang Gurih", category: "Bumbu / Pelengkap", portion: "15 gr", targetOrder: "45.00 kg", supplier: "Dapur Bumbu SPPG", tare: "0.50", persiapan: "Kupas cabai & bawang.", pengolahan: "Tumis tanak harum gurih.", pemorsian: "15 gr di sekat lauk." }},
          {{ name: "Tahu Goreng Gurih", category: "Protein Nabati", portion: "45 gr", targetOrder: "135.00 kg", supplier: "Koperasi Tahu Kedungwuni", tare: "0.50", persiapan: "Potong tahu kotak, marinasi air bawang garam.", pengolahan: "Goreng berkulit gurih.", pemorsian: "1 potong mendampingi telur semur." }},
          {{ name: "Gyoza Sayur (Wortel & Kol)", category: "Sayuran Segar", portion: "2 pcs (60 gr)", targetOrder: "180.00 kg", supplier: "Dapur Olahan Sayur SPPG", tare: "0.50", persiapan: "Cincang halus kol dan wortel, bumbui minyak wijen bawang putih, bungkus kulit gyoza lipat rapat.", pengolahan: "Kukus 12 menit atau pan fry dengan sedikit minyak air hingga dasar kecokelatan krispi.", pemorsian: "Tata 2 pcs gyoza sayur di sekat sayur ompreng." }},
          {{ name: "Pisang Cavendish", category: "Buah Segar", portion: "1 pcs", targetOrder: "3.000 pcs", supplier: "Distributor Buah Nusantara", tare: "0.00", persiapan: "Khusus Tim Pemorsian.", pengolahan: "Dilarang kontak panas.", pemorsian: "SOP BUAH: Sortir kulit mulus steril di sekat buah." }}
        ]
      }}
    }}
  }}
}};

let currentCycle = 'cycle1';
let currentDay = 'senin';
let currentActiveStation = 'persiapan';
let formActiveCycle = 'cycle1';
let formActiveDay = 'senin';

// INITIAL STAGING ITEMS
let stagingItems = [
  {{
    id: "cart_1",
    timestamp: "11:20:15",
    team: "TIM PERSIAPAN",
    category: "Protein Hewani",
    name: "Telur Ayam Rollade Bulat (Batch 1)",
    bruto: 25.85,
    tara: 0.85,
    netto: 25.00,
    catatan: "Sesuai Note Chef: Potong bulat seragam, siap goreng",
    synced: false
  }},
  {{
    id: "cart_2",
    timestamp: "11:28:40",
    team: "TIM PERSIAPAN",
    category: "Sayuran Segar",
    name: "Sayur Kakiage (Wortel & Kol)",
    bruto: 15.50,
    tara: 0.50,
    netto: 15.00,
    catatan: "Sesuai Note Chef: Potong korek halus, bilas 3x",
    synced: false
  }},
  {{
    id: "cart_3",
    timestamp: "11:35:10",
    team: "TIM PEMORSIAN",
    category: "Buah Segar",
    name: "Jeruk Manis Segar Sisir A",
    bruto: 30.00,
    tara: 0.00,
    netto: 30.00,
    catatan: "Sesuai SOP Buah: Lap steril kering di sekat sejuk",
    synced: false
  }}
];

document.addEventListener('DOMContentLoaded', () => {{
  renderWeeklyMenu();
  renderAslapChecklist();
  renderStagingList();
}});

function switchScreen(screenId) {{
  ['menu', 'aslap', 'home', 'staging', 'stock'].forEach(s => {{
    const sec = document.getElementById('screen-' + s);
    const tabBtn = document.getElementById('tab-btn-' + s);
    if (sec) {{
      if (s === screenId) {{
        sec.classList.remove('hidden');
      }} else {{
        sec.classList.add('hidden');
      }}
    }}
    if (tabBtn) {{
      if (s === screenId) {{
        tabBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5 cursor-pointer';
      }} else {{
        tabBtn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer';
      }}
    }}
  }});
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

function selectCycle(cycleKey) {{
  currentCycle = cycleKey;
  const btn1 = document.getElementById('cycle-btn-1');
  const btn2 = document.getElementById('cycle-btn-2');
  const label = document.getElementById('cycle-indicator-label');

  if (cycleKey === 'cycle1') {{
    btn1.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white shadow-xs cursor-pointer transition-all';
    btn2.className = 'px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 cursor-pointer transition-all';
    if (label) label.innerText = 'Siklus 1: 16 - 20 November 2026';
  }} else {{
    btn2.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white shadow-xs cursor-pointer transition-all';
    btn1.className = 'px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 cursor-pointer transition-all';
    if (label) label.innerText = 'Siklus 2: 23 - 27 November 2026';
  }}

  selectDay(currentDay);
  showToast('Memuat ' + weeklyMenuCycles[cycleKey].label);
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
  const heroTitle = document.getElementById('hero-menu-title');
  const heroNutrition = document.getElementById('hero-nutrition');
  const aslapDay = document.getElementById('aslap-day-label');
  
  const curCycleData = weeklyMenuCycles[currentCycle];
  const cur = curCycleData.days[day];

  const cycleNum = currentCycle === 'cycle1' ? '1' : '2';
  if (heroLabel) heroLabel.innerText = 'Menu Hari ' + day.toUpperCase() + ' (Siklus ' + cycleNum + ')';
  if (heroTitle) heroTitle.innerText = cur.title;
  if (heroNutrition) heroNutrition.innerText = cur.nutrition;
  if (aslapDay) aslapDay.innerText = day.toUpperCase() + ' (SIKLUS ' + cycleNum + ')';

  updateStickyNoteContent();
  renderWeeklyMenu();
  renderAslapChecklist();
}}

function selectStationDirective(station) {{
  currentActiveStation = station;
  const stations = ['persiapan', 'pengolahan', 'pemorsian'];

  stations.forEach(st => {{
    const btn = document.getElementById('directive-btn-' + st);
    if (!btn) return;
    if (st === station) {{
      if (st === 'persiapan') {{
        btn.className = 'py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-emerald-600 text-white shadow-sm border border-emerald-700 cursor-pointer transition-all';
      }} else if (st === 'pengolahan') {{
        btn.className = 'py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-amber-600 text-white shadow-sm border border-amber-700 cursor-pointer transition-all';
      }} else {{
        btn.className = 'py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-blue-600 text-white shadow-sm border border-blue-700 cursor-pointer transition-all';
      }}
    }} else {{
      btn.className = 'py-2.5 px-2 rounded-xl text-xs font-extrabold flex flex-col items-center justify-center gap-1 bg-white text-slate-700 hover:bg-slate-50 border border-slate-200 cursor-pointer transition-all';
    }}
  }});

  updateStickyNoteContent();
  renderWeeklyMenu();
}}

function updateStickyNoteContent() {{
  const stickyNote = document.getElementById('sticky-chef-note');
  const title = document.getElementById('note-team-title');
  const body = document.getElementById('note-team-body');
  const cur = weeklyMenuCycles[currentCycle].days[currentDay];

  if (!stickyNote || !title || !body || !cur) return;

  if (currentActiveStation === 'persiapan') {{
    stickyNote.className = 'note-paper-persiapan p-3.5 rounded-2xl transition-all';
    title.innerText = 'NOTE RESMI CHEF LUTFI • TIM PERSIAPAN (' + currentDay.toUpperCase() + ')';
    body.innerHTML = '<p class="font-bold text-emerald-950 mb-1">Pedoman Penerimaan & Pembersihan Bahan:</p>' +
      '<p>• ' + cur.notePersiapan + '</p>' +
      '<p>• Kupas bersih bagian luar, pastikan potongan cm presisi seragam untuk efisiensi masak.</p>' +
      '<p>• Cuci tiga kali dengan air mengalir. Setelah ditimbang di stasiun ini, kirim langsung ke Tim Pengolahan.</p>';
  }} else if (currentActiveStation === 'pengolahan') {{
    stickyNote.className = 'note-paper-pengolahan p-3.5 rounded-2xl transition-all';
    title.innerText = 'NOTE RESMI CHEF LUTFI • TIM PENGOLAHAN (' + currentDay.toUpperCase() + ')';
    body.innerHTML = '<p class="font-bold text-amber-950 mb-1">Pedoman Suhu & Standar Bumbu:</p>' +
      '<p>• ' + cur.notePengolahan + '</p>' +
      '<p>• Standar Keamanan Pangan BGN: Suhu inti kaldu & daging matang minimal 75°C (cek berkala pakai termometer tusuk).</p>' +
      '<p>• Masak bumbu hingga tanak berminyak. Begitu matang, timbang hasil olahan sebelum diserahkan ke Tim Pemorsian.</p>';
  }} else {{
    stickyNote.className = 'note-paper-pemorsian p-3.5 rounded-2xl transition-all';
    title.innerText = 'NOTE RESMI CHEF LUTFI • TIM PEMORSIAN (' + currentDay.toUpperCase() + ')';
    body.innerHTML = '<p class="font-bold text-blue-950 mb-1">Pedoman Ompreng & SOP Buah Segar:</p>' +
      '<p>• ' + cur.notePemorsian + '</p>' +
      '<p>• Suhu saji ompreng dipertahankan minimal 60°C saat dimasukkan ke wadah thermal tertutup.</p>' +
      '<p>• <span class="font-bold text-blue-900 underline">SOP Buah Segar:</span> Dikerjakan higienis dengan sarung tangan steril di ruang sejuk terpisah dari panas kompor.</p>';
  }}
}}

// ========================================================
// CHEF RECIPE EDITOR CONTROLS (SENIN - JUMAT)
// ========================================================
function openChefRecipeModal() {{
  formActiveCycle = currentCycle;
  formActiveDay = currentDay;
  selectChefFormCycle(formActiveCycle);
  loadDayRecipeToForm(formActiveDay);
  document.getElementById('chef-recipe-modal').classList.remove('hidden');
}}

function closeChefRecipeModal() {{
  document.getElementById('chef-recipe-modal').classList.add('hidden');
}}

function selectChefFormCycle(cKey) {{
  formActiveCycle = cKey;
  const b1 = document.getElementById('chef-cycle-1');
  const b2 = document.getElementById('chef-cycle-2');
  if (cKey === 'cycle1') {{
    b1.className = 'py-1.5 rounded-lg font-extrabold text-[10px] bg-amber-600 text-white cursor-pointer';
    b2.className = 'py-1.5 rounded-lg font-extrabold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer';
  }} else {{
    b2.className = 'py-1.5 rounded-lg font-extrabold text-[10px] bg-amber-600 text-white cursor-pointer';
    b1.className = 'py-1.5 rounded-lg font-extrabold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer';
  }}
  loadDayRecipeToForm(formActiveDay);
}}

function loadDayRecipeToForm(day) {{
  formActiveDay = day;
  ['senin', 'selasa', 'rabu', 'kamis', 'jumat'].forEach(d => {{
    const btn = document.getElementById('chef-day-' + d);
    if (!btn) return;
    if (d === day) {{
      btn.className = 'chef-day-btn py-1.5 rounded-lg font-bold text-[10px] bg-slate-900 text-white cursor-pointer';
    }} else {{
      btn.className = 'chef-day-btn py-1.5 rounded-lg font-bold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer';
    }}
  }});

  const cur = weeklyMenuCycles[formActiveCycle].days[day];
  if (!cur) return;

  document.getElementById('chef-form-title').value = cur.title;
  document.getElementById('chef-form-nutrition').value = cur.nutrition;
  document.getElementById('chef-form-note-persiapan').value = cur.notePersiapan;
  document.getElementById('chef-form-note-pengolahan').value = cur.notePengolahan;
  document.getElementById('chef-form-note-pemorsian').value = cur.notePemorsian;
}}

function saveChefRecipeForm() {{
  const cur = weeklyMenuCycles[formActiveCycle].days[formActiveDay];
  if (!cur) return;

  cur.title = document.getElementById('chef-form-title').value.trim();
  cur.nutrition = document.getElementById('chef-form-nutrition').value.trim();
  cur.notePersiapan = document.getElementById('chef-form-note-persiapan').value.trim();
  cur.notePengolahan = document.getElementById('chef-form-note-pengolahan').value.trim();
  cur.notePemorsian = document.getElementById('chef-form-note-pemorsian').value.trim();

  closeChefRecipeModal();
  currentCycle = formActiveCycle;
  selectCycle(currentCycle);
  selectDay(formActiveDay);
  showToast('Resep ' + formActiveDay.toUpperCase() + ' (' + formActiveCycle + ') berhasil disiarkan!');
}}

// ========================================================
// RENDER ASLAP CHECKLIST & AUTO-FORM MONITORING
// ========================================================
function renderAslapChecklist() {{
  const container = document.getElementById('aslap-items-container');
  const countBadge = document.getElementById('aslap-item-count');
  const dayData = weeklyMenuCycles[currentCycle].days[currentDay];
  if (!container || !dayData) return;

  container.innerHTML = '';
  if (countBadge) countBadge.innerText = dayData.items.length + ' Bahan Baku';

  dayData.items.forEach((item, idx) => {{
    const row = document.createElement('div');
    row.className = 'p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-2 hover:bg-white transition-all';

    const safeName = item.name.replace(/'/g, "\\\\'");
    const safeTarget = item.targetOrder.replace(/'/g, "\\\\'");

    row.innerHTML = '<div class="flex items-start justify-between">' +
      '<div>' +
        '<div class="flex items-center gap-1.5">' +
          '<span class="w-5 h-5 rounded-full bg-purple-100 text-purple-800 font-extrabold text-[10px] flex items-center justify-center">' + (idx + 1) + '</span>' +
          '<h4 class="text-xs font-bold text-slate-900">' + item.name + '</h4>' +
        '</div>' +
        '<p class="text-[10px] text-slate-500 mt-0.5">Supplier: ' + item.supplier + '</p>' +
      '</div>' +
      '<div class="text-right">' +
        '<span class="text-xs font-extrabold text-purple-700 font-mono-num block">Target: ' + item.targetOrder + '</span>' +
        '<span class="text-[9px] bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.5 rounded">QC Segar Sesuai</span>' +
      '</div>' +
    '</div>' +
    '<div class="flex items-center justify-between pt-1.5 border-t border-slate-200/60 text-[11px]">' +
      '<span class="text-slate-500 font-medium">Standar Porsi: ' + item.portion + '</span>' +
      '<button onclick="verifyAslapItem(\\\'' + safeName + '\\\', \\\'' + safeTarget + '\\\')" class="px-2.5 py-1 bg-purple-600 hover:bg-purple-700 text-white rounded-lg text-[10px] font-bold shadow-xs cursor-pointer flex items-center gap-1">' +
        '<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>' +
        '<span>Terima & Timbang</span>' +
      '</button>' +
    '</div>';

    container.appendChild(row);
  }});
}}

function verifyAslapItem(name, target) {{
  showToast('Bahan ' + name + ' (' + target + ') diverifikasi ASLAP');
  const inputItem = document.getElementById('input-item');
  if (inputItem) inputItem.value = name;
  selectTeam('TIM PERSIAPAN');
  switchScreen('home');
}}

// ========================================================
// GENERATOR FORM MONITORING ASLAP SIAP CETAK (A4)
// ========================================================
function openPrintModal() {{
  const preview = document.getElementById('modal-form-preview');
  const printContainer = document.getElementById('printable-aslap-form');
  const dayData = weeklyMenuCycles[currentCycle].days[currentDay];
  if (!preview || !dayData) return;

  const todayStr = new Date().toLocaleDateString('id-ID', {{ weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }});
  const cycleNum = currentCycle === 'cycle1' ? '1 (16-20 Nov 2026)' : '2 (23-27 Nov 2026)';

  let tableRows = '';
  dayData.items.forEach((it, i) => {{
    tableRows += '<tr class="border-b border-slate-200">' +
      '<td class="p-2 text-center font-bold">' + (i + 1) + '</td>' +
      '<td class="p-2 font-bold">' + it.name + '</td>' +
      '<td class="p-2 text-slate-600">' + it.category + '</td>' +
      '<td class="p-2 text-center font-mono-num font-bold">' + it.targetOrder + '</td>' +
      '<td class="p-2 text-center font-mono-num font-bold text-emerald-700">' + it.targetOrder + '</td>' +
      '<td class="p-2 text-center text-[10px] font-bold text-emerald-800">Lolos QC Segar</td>' +
      '<td class="p-2 text-slate-600 text-[10px]">' + it.supplier + '</td>' +
      '<td class="p-2 text-center text-slate-400 font-mono-num">✓ Paraf</td>' +
    '</tr>';
  }});

  const formHtml = '<!-- KOP SURAT RESMI BGN -->' +
    '<div class="border-b-2 border-slate-900 pb-3 mb-3 text-center">' +
      '<h2 class="text-xs font-black uppercase tracking-wider text-slate-900">BADAN GIZI NASIONAL (BGN) REPUBLIK INDONESIA</h2>' +
      '<h3 class="text-sm font-extrabold text-slate-900">SATUAN PELAYANAN PROGRAM GIZI (SPPG) KEDUNGWUNI PEKAJANGAN 4</h3>' +
      '<p class="text-[9px] text-slate-600 mt-0.5">FORM MONITORING PENERIMAAN & KONTROL ALUR BAHAN BAKU HARIAN (ASLAP)</p>' +
    '</div>' +

    '<div class="grid grid-cols-2 gap-2 text-[10px] bg-slate-50 p-2 rounded border border-slate-200">' +
      '<div>' +
        '<p><span class="font-bold">Hari / Tanggal:</span> ' + todayStr + '</p>' +
        '<p><span class="font-bold">Siklus Menu:</span> Hari ' + currentDay.toUpperCase() + ' • Siklus ' + cycleNum + '</p>' +
      '</div>' +
      '<div class="text-right">' +
        '<p><span class="font-bold">Penanggung Jawab ASLAP:</span> Petugas Lapangan Kedungwuni</p>' +
        '<p><span class="font-bold">Head Chef Pelaksana:</span> Chef Lutfi Iskandar</p>' +
      '</div>' +
    '</div>' +

    '<table class="w-full border-collapse border border-slate-300 text-[10px] mt-2">' +
      '<thead>' +
        '<tr class="bg-slate-100 text-slate-800">' +
          '<th class="border border-slate-300 p-1.5 text-center w-8">No</th>' +
          '<th class="border border-slate-300 p-1.5 text-left">Nama Bahan Baku</th>' +
          '<th class="border border-slate-300 p-1.5 text-left">Kategori</th>' +
          '<th class="border border-slate-300 p-1.5 text-center">Target Order</th>' +
          '<th class="border border-slate-300 p-1.5 text-center">Timbangan Datang</th>' +
          '<th class="border border-slate-300 p-1.5 text-center">Kondisi Fisik</th>' +
          '<th class="border border-slate-300 p-1.5 text-left">Vendor / Supplier</th>' +
          '<th class="border border-slate-300 p-1.5 text-center w-14">Check</th>' +
        '</tr>' +
      '</thead>' +
      '<tbody>' + tableRows + '</tbody>' +
    '</table>' +

    '<div class="mt-4 pt-3 border-t border-slate-200 grid grid-cols-3 gap-2 text-center text-[9px]">' +
      '<div>' +
        '<p class="text-slate-500 mb-8">Petugas ASLAP Penerimaan:</p>' +
        '<p class="font-bold underline text-slate-900">( Petugas ASLAP )</p>' +
      '</div>' +
      '<div>' +
        '<p class="text-slate-500 mb-8">Driver Ekspedisi Vendor:</p>' +
        '<p class="font-bold underline text-slate-900">( Driver Supplier )</p>' +
      '</div>' +
      '<div>' +
        '<p class="text-slate-500 mb-8">Mengetahui & Menyetujui:</p>' +
        '<p class="font-bold underline text-slate-900">Chef Lutfi Iskandar</p>' +
      '</div>' +
    '</div>';

  preview.innerHTML = formHtml;
  if (printContainer) printContainer.innerHTML = formHtml;

  document.getElementById('print-aslap-modal').classList.remove('hidden');
}}

function closePrintModal() {{
  document.getElementById('print-aslap-modal').classList.add('hidden');
}}

function renderWeeklyMenu() {{
  const container = document.getElementById('menu-items-container');
  if (!container) return;
  container.innerHTML = '';

  const dayData = weeklyMenuCycles[currentCycle].days[currentDay];
  if (!dayData || !dayData.items) return;

  dayData.items.forEach(item => {{
    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200 p-3.5 rounded-2xl shadow-xs space-y-2.5 hover:border-slate-300 transition-all';

    let directiveText = '';
    let directiveBadge = '';
    let directiveBg = '';
    let actionLabel = 'Timbang';

    if (currentActiveStation === 'persiapan') {{
      directiveText = item.persiapan;
      directiveBadge = 'NOTE CHEF UNTUK TIM PERSIAPAN:';
      directiveBg = 'note-paper-persiapan text-emerald-950';
      actionLabel = 'Timbang Persiapan';
    }} else if (currentActiveStation === 'pengolahan') {{
      directiveText = item.pengolahan;
      directiveBadge = 'NOTE CHEF UNTUK TIM PENGOLAHAN:';
      directiveBg = 'note-paper-pengolahan text-amber-950';
      actionLabel = 'Timbang Olahan';
    }} else if (currentActiveStation === 'pemorsian') {{
      directiveText = item.pemorsian;
      directiveBadge = (item.category === 'Buah Segar') ? 'NOTE SOP KHUSUS BUAH SEGAR:' : 'NOTE CHEF UNTUK PEMORSIAN:';
      directiveBg = 'note-paper-pemorsian text-blue-950';
      actionLabel = 'Timbang Pemorsian';
    }}

    const safeName = item.name.replace(/'/g, "\\\\'");
    const safeCat = item.category.replace(/'/g, "\\\\'");
    const safeDirective = (directiveText || '').replace(/'/g, "\\\\'");
    const mappedTeamName = (currentActiveStation === 'persiapan') ? 'TIM PERSIAPAN' : (currentActiveStation === 'pengolahan' ? 'TIM PENGOLAHAN' : 'TIM PEMORSIAN');

    card.innerHTML = '<div class="flex items-start justify-between">' +
      '<div>' +
        '<div class="flex items-center gap-1.5">' +
          '<h3 class="text-xs font-bold text-slate-900">' + item.name + '</h3>' +
          '<span class="text-[9px] font-semibold bg-slate-100 text-slate-700 px-1.5 py-0.5 rounded border border-slate-200">' + item.category + '</span>' +
          (item.category === 'Buah Segar' ? '<span class="text-[9px] font-bold bg-blue-100 text-blue-800 px-1.5 py-0.5 rounded">Khusus Pemorsian</span>' : '') +
        '</div>' +
        '<p class="text-[10px] text-slate-500 font-medium mt-0.5">Standar Porsi: ' + item.portion + '</p>' +
      '</div>' +
      '<button onclick="loadMenuItemToWeigh(\\\'' + safeName + '\\\', \\\'' + safeCat + '\\\', \\\'' + mappedTeamName + '\\\', \\\'' + item.tare + '\\\', \\\'' + safeDirective + '\\\')" class="px-3 py-1.5 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold shadow-sm transition-all flex items-center gap-1 cursor-pointer active:scale-95">' +
        '<span>' + actionLabel + '</span>' +
        '<svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>' +
      '</button>' +
    '</div>' +
    '<div class="' + directiveBg + ' p-3 rounded-xl text-xs space-y-1">' +
      '<span class="font-extrabold flex items-center gap-1.5 text-[11px]">' +
        '<span>📌</span>' +
        directiveBadge +
      '</span>' +
      '<p class="text-slate-900 mt-0.5 font-medium leading-relaxed">' + directiveText + '</p>' +
    '</div>';

    container.appendChild(card);
  }});
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
  const directiveElem = document.getElementById('autofill-directive-text');

  if (banner && bannerText && directiveElem) {{
    banner.classList.remove('hidden');
    bannerText.innerText = 'Bahan ' + name + ' dimuat untuk ' + team;
    directiveElem.innerHTML = '<span class="font-extrabold block text-slate-900 mb-0.5">NOTE CHEF UNTUK BAHAN INI:</span>' + (directive || 'Lakukan penimbangan sesuai standar porsi.');
  }}

  switchScreen('home');
  showToast('Memuat ' + name + ' dengan Note Chef');
}}

function dismissAutofillBanner() {{
  const banner = document.getElementById('autofill-banner');
  if (banner) banner.classList.add('hidden');
}}

function selectTeam(teamName) {{
  document.querySelectorAll('.team-chip').forEach(btn => {{
    if (btn.dataset.team === teamName) {{
      if (teamName === 'TIM PERSIAPAN') {{
        btn.className = 'team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-emerald-600 text-white shadow-sm flex items-center justify-center gap-1 cursor-pointer';
      }} else if (teamName === 'TIM PENGOLAHAN') {{
        btn.className = 'team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-amber-600 text-white shadow-sm flex items-center justify-center gap-1 cursor-pointer';
      }} else {{
        btn.className = 'team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-blue-600 text-white shadow-sm flex items-center justify-center gap-1 cursor-pointer';
      }}
    }} else {{
      btn.className = 'team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1 cursor-pointer';
    }}
  }});

  const badge = document.getElementById('current-stage-badge');
  if (badge) {{
    if (teamName === 'TIM PERSIAPAN') {{
      badge.innerText = 'Penerimaan & Sortir Persiapan';
      badge.className = 'text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full';
    }} else if (teamName === 'TIM PENGOLAHAN') {{
      badge.innerText = 'Pengolahan Panas (Masak)';
      badge.className = 'text-[10px] bg-amber-100 text-amber-800 font-bold px-2 py-0.5 rounded-full';
    }} else {{
      badge.innerText = 'Pemorsian Distribusi & Buah';
      badge.className = 'text-[10px] bg-blue-100 text-blue-800 font-bold px-2 py-0.5 rounded-full';
    }}
  }}
}}

function setTare(val) {{
  const inputTare = document.getElementById('input-tare');
  if (inputTare) inputTare.value = val.toFixed(2);
  calculateNetto();
  showToast('Preset Tara disetel: ' + val.toFixed(2) + ' kg');
}}

function calculateNetto() {{
  const bruto = parseFloat(document.getElementById('input-bruto').value) || 0;
  const tare = parseFloat(document.getElementById('input-tare').value) || 0;
  const netto = Math.max(0, bruto - tare);

  document.getElementById('input-netto').value = netto.toFixed(2);
  document.getElementById('scale-display').innerHTML = netto.toFixed(2) + ' <span class="text-xl text-slate-400 font-bold">kg</span>';
}}

function triggerCameraOCR() {{
  showToast('Mengambil foto indikator timbangan...');
  setTimeout(() => {{
    const detectedNetto = (Math.random() * (45.0 - 20.0) + 20.0).toFixed(2);
    const tare = parseFloat(document.getElementById('input-tare').value) || 0.85;
    const bruto = (parseFloat(detectedNetto) + tare).toFixed(2);

    document.getElementById('input-bruto').value = bruto;
    document.getElementById('input-netto').value = detectedNetto;
    document.getElementById('scale-display').innerHTML = detectedNetto + ' <span class="text-xl text-slate-400 font-bold">kg</span>';

    showToast('Timbangan Terdeteksi: ' + detectedNetto + ' kg');
  }}, 700);
}}

function addToStagingCart() {{
  const team = document.querySelector('.team-chip.bg-emerald-600, .team-chip.bg-amber-600, .team-chip.bg-blue-600')?.dataset.team || 'TIM PERSIAPAN';
  const name = document.getElementById('input-item').value.trim() || 'Bahan MBG';
  const category = document.getElementById('input-kategori').value.trim() || 'Lain-lain';
  const bruto = parseFloat(document.getElementById('input-bruto').value) || 0;
  const tara = parseFloat(document.getElementById('input-tare').value) || 0;
  const netto = parseFloat(document.getElementById('input-netto').value) || 0;
  const catatan = document.getElementById('input-catatan').value.trim();

  const now = new Date();
  const timeStr = now.toTimeString().split(' ')[0];

  const newItem = {{
    id: "cart_" + Date.now(),
    timestamp: timeStr,
    team: team,
    category: category,
    name: name,
    bruto: bruto,
    tara: tara,
    netto: netto,
    catatan: catatan,
    synced: false
  }};

  stagingItems.unshift(newItem);
  renderStagingList();
  showToast('Item berhasil dimasukkan ke keranjang!');
  switchScreen('staging');
}}

function renderStagingList() {{
  const container = document.getElementById('staging-items-list');
  const countBadge = document.getElementById('staging-count-badge');
  const tabBadge = document.getElementById('tab-cart-badge');

  if (countBadge) countBadge.innerText = stagingItems.length + ' Item';
  if (tabBadge) tabBadge.innerText = stagingItems.length;

  if (!container) return;
  container.innerHTML = '';

  if (stagingItems.length === 0) {{
    container.innerHTML = '<div class="p-8 text-center bg-white rounded-2xl border border-slate-200 text-slate-400 text-xs">' +
      '<p class="font-bold text-slate-600 mb-1">Keranjang Penimbangan Masih Kosong</p>' +
      '<p>Pilih bahan dari menu atau timbang langsung di tab Timbang.</p>' +
    '</div>';
    return;
  }}

  stagingItems.forEach((item, idx) => {{
    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200 p-3.5 rounded-2xl shadow-xs space-y-2 hover:border-slate-300 transition-all';

    let teamBg = 'bg-emerald-50 text-emerald-800 border-emerald-200';
    if (item.team === 'TIM PENGOLAHAN') teamBg = 'bg-amber-50 text-amber-800 border-amber-200';
    if (item.team === 'TIM PEMORSIAN') teamBg = 'bg-blue-50 text-blue-800 border-blue-200';

    card.innerHTML = '<div class="flex items-start justify-between">' +
      '<div>' +
        '<div class="flex items-center gap-1.5">' +
          '<span class="text-[9px] font-extrabold px-2 py-0.5 rounded-full border ' + teamBg + '">' + item.team + '</span>' +
          '<span class="text-[10px] text-slate-400 font-mono-num">' + item.timestamp + '</span>' +
        '</div>' +
        '<h4 class="text-xs font-bold text-slate-900 mt-1">' + item.name + '</h4>' +
        '<p class="text-[10px] text-slate-500">' + item.category + '</p>' +
      '</div>' +
      '<div class="text-right">' +
        '<span class="text-sm font-black font-mono-num text-emerald-600">' + item.netto.toFixed(2) + ' kg</span>' +
        '<p class="text-[9px] text-slate-400 font-mono-num">B: ' + item.bruto.toFixed(2) + ' | T: ' + item.tara.toFixed(2) + '</p>' +
      '</div>' +
    '</div>' +
    (item.catatan ? '<p class="text-[10px] text-slate-600 bg-slate-50 p-1.5 rounded-lg border border-slate-100 font-medium">📝 ' + item.catatan + '</p>' : '') +
    '<div class="flex items-center justify-end gap-1.5 pt-1 border-t border-slate-100">' +
      '<button onclick="openEditModal(\\\'' + item.id + '\\\')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-[10px] font-bold cursor-pointer transition-all">Edit</button>' +
      '<button onclick="deleteCartItem(\\\'' + item.id + '\\\')" class="px-2.5 py-1 bg-rose-50 hover:bg-rose-100 text-rose-700 rounded-lg text-[10px] font-bold cursor-pointer transition-all">Hapus</button>' +
    '</div>';

    container.appendChild(card);
  }});
}}

function openEditModal(itemId) {{
  const it = stagingItems.find(x => x.id === itemId);
  if (!it) return;

  document.getElementById('edit-item-id').value = it.id;
  document.getElementById('edit-item-name').value = it.name;
  document.getElementById('edit-item-team').value = it.team;
  document.getElementById('edit-item-bruto').value = it.bruto;
  document.getElementById('edit-item-tara').value = it.tara;
  document.getElementById('edit-item-netto-display').innerText = it.netto.toFixed(2) + ' kg';
  document.getElementById('edit-item-catatan').value = it.catatan || '';

  document.getElementById('edit-cart-modal').classList.remove('hidden');
}}

function closeEditModal() {{
  document.getElementById('edit-cart-modal').classList.add('hidden');
}}

function recalcEditNetto() {{
  const b = parseFloat(document.getElementById('edit-item-bruto').value) || 0;
  const t = parseFloat(document.getElementById('edit-item-tara').value) || 0;
  const n = Math.max(0, b - t);
  document.getElementById('edit-item-netto-display').innerText = n.toFixed(2) + ' kg';
}}

function saveEditCartItem() {{
  const id = document.getElementById('edit-item-id').value;
  const it = stagingItems.find(x => x.id === id);
  if (!it) return;

  it.name = document.getElementById('edit-item-name').value.trim();
  it.team = document.getElementById('edit-item-team').value;
  it.bruto = parseFloat(document.getElementById('edit-item-bruto').value) || 0;
  it.tara = parseFloat(document.getElementById('edit-item-tara').value) || 0;
  it.netto = Math.max(0, it.bruto - it.tara);
  it.catatan = document.getElementById('edit-item-catatan').value.trim();

  closeEditModal();
  renderStagingList();
  showToast('Item berhasil diperbarui!');
}}

function deleteCartItem(id) {{
  stagingItems = stagingItems.filter(x => x.id !== id);
  renderStagingList();
  showToast('Item dihapus dari keranjang.');
}}

function syncAllToGoogleSheets() {{
  const btn = document.getElementById('btn-sync-all');
  if (stagingItems.length === 0) {{
    showToast('Keranjang kosong, tidak ada item yang disinkronkan.');
    return;
  }}

  btn.disabled = true;
  btn.innerHTML = '<span class="animate-spin text-base">⏳</span><span>Menghubungkan ke Google Sheets...</span>';

  setTimeout(() => {{
    stagingItems = [];
    renderStagingList();
    btn.disabled = false;
    btn.innerHTML = '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>Berhasil Disinkronkan ke Spreadsheet!</span>';
    btn.className = 'w-full py-3 bg-slate-900 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-2';

    showToast('Data penimbangan berhasil masuk ke Google Sheet!');
    setTimeout(() => {{
      btn.className = 'w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all active:scale-98';
      btn.innerHTML = '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/></svg><span>Sinkronkan ke Google Sheets Monitoring</span>';
    }}, 2500);
  }}, 1200);
}}

function showToast(msg) {{
  const toast = document.getElementById('toast');
  const toastMsg = document.getElementById('toast-msg');
  if (!toast || !toastMsg) return;

  toastMsg.innerText = msg;
  toast.classList.remove('opacity-0', 'pointer-events-none');
  toast.classList.add('opacity-100');

  setTimeout(() => {{
    toast.classList.remove('opacity-100');
    toast.classList.add('opacity-0', 'pointer-events-none');
  }}, 3000);
}}
</script>
</body>
</html>
'''

# Tulis ke dokumen lokal preview.html dan artifact
with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

artifact_path = r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"preview.html dan {artifact_path} berhasil diperbarui dengan Menu Resmi 16-27 November 2026!")


import base64
import os

with open('assets/logo_bgn_512.png', 'rb') as f:
    b64_logo = base64.b64encode(f.read()).decode('utf-8')

html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MBG Kitchen Monitor - Note Arahan Otomatis</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&family=Caveat:wght@600;700&display=swap');
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .font-mono-num {{
      font-family: 'JetBrains Mono', monospace;
    }}
    .font-note {{
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .custom-scrollbar::-webkit-scrollbar {{
      width: 4px;
      height: 4px;
    }}
    .custom-scrollbar::-webkit-scrollbar-thumb {{
      background: #CBD5E1;
      border-radius: 4px;
    }}
    .note-paper {{
      background: #FEF9C3;
      border-left: 5px solid #EAB308;
      box-shadow: 0 4px 6px -1px rgba(234, 179, 8, 0.15), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
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
          <p class="text-[10px] text-slate-500 font-semibold">SPPG Pekajangan 04 • Note Arahan Langsung Terlampir</p>
        </div>
      </div>
    </div>
    
    <div class="flex items-center gap-2">
      <!-- Status Hemat Cloud Drive -->
      <span class="px-2 py-1 bg-emerald-50 text-emerald-800 border border-emerald-200 rounded-lg text-[10px] font-extrabold flex items-center gap-1 shadow-xs">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
        <span>Siklus 1 Minggu Aktif</span>
      </span>

      <!-- Akses Arsip PDF Asli (Opsional) -->
      <button onclick="openPdfViewerModal()" class="p-1.5 text-slate-400 hover:text-slate-700 rounded-lg hover:bg-slate-100 transition-colors cursor-pointer" title="Lihat Dokumen PDF Master (Opsional)">
        <svg class="w-4 h-4 text-rose-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd"/></svg>
      </button>

      <button onclick="showWebhookInfo()" class="p-1.5 text-slate-400 hover:text-slate-700 rounded-lg hover:bg-slate-100 transition-colors cursor-pointer" title="Pengaturan Webhook">
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
      </button>
    </div>
  </header>

  <!-- NAVIGATION TABS PILLS -->
  <div class="bg-white border-b border-slate-200 px-3 py-2 sticky top-[53px] z-30 flex items-center justify-between">
    <div class="flex gap-1 overflow-x-auto custom-scrollbar w-full">
      <button onclick="switchScreen('menu')" id="tab-btn-menu" class="px-3 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm flex items-center gap-1.5 cursor-pointer">
        <svg class="w-3.5 h-3.5 text-amber-300" fill="currentColor" viewBox="0 0 20 20"><path d="M4 3a2 2 0 100 4h12a2 2 0 100-4H4z"/><path fill-rule="evenodd" d="M3 8h14v7a2 2 0 01-2 2H5a2 2 0 01-2-2V8zm5 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z" clip-rule="evenodd"/></svg>
        <span>Arahan Menu & Note</span>
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
  <main class="flex-1 p-3 pb-24 max-w-lg mx-auto w-full space-y-3">

    <!-- ============================================== -->
    <!-- SCREEN 1: ARAHAN MENU & NOTE OTOMATIS          -->
    <!-- ============================================== -->
    <section id="screen-menu" class="space-y-3">
      
      <!-- SIKLUS MINGGU INI & PILIH HARI (SENIN - JUMAT) -->
      <div class="bg-white border border-slate-200 p-3 rounded-2xl shadow-xs space-y-2.5">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span class="text-xs font-extrabold text-slate-900 uppercase tracking-wide">Siklus Menu 1 Minggu</span>
          </div>
          <span class="text-[10px] bg-slate-100 text-slate-700 px-2 py-0.5 rounded-full font-bold">Target 3.000 Porsi</span>
        </div>
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
          <span id="hero-day-label" class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400 bg-amber-400/10 px-2 py-0.5 rounded-md border border-amber-400/20">Menu Hari Senin</span>
          <span class="text-[10px] text-slate-300 font-medium">BGN Nutrition Verified</span>
        </div>
        <h2 id="hero-menu-title" class="text-sm font-extrabold text-white mt-1 leading-snug">
          Nasi Putih + Daging Ayam Semur Kecap + Tahu Goreng Gurih + Tumis Buncis Jagung Manis + Pisang Cavendish
        </h2>
        <div class="mt-2.5 pt-2 border-t border-slate-700 flex items-center justify-between text-[11px] text-slate-300">
          <span id="hero-nutrition">Energi: 685 kkal • Protein: 28 gr • Serat: 5.2 gr</span>
          <span class="font-mono-num font-bold text-amber-300">3.000 Porsi</span>
        </div>
      </div>

      <!-- 3 TIM INTI SELECTOR -->
      <div class="bg-white border border-slate-200 p-2.5 rounded-2xl shadow-xs space-y-2">
        <div class="flex items-center justify-between px-1">
          <span class="text-[11px] font-extrabold text-slate-800 uppercase tracking-wide">Pilih Stasiun Kerja Tim</span>
          <span class="text-[10px] text-slate-500 font-medium">Klik tim untuk melihat Note otomatis</span>
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
              <p class="text-[10px] text-emerald-700 font-semibold">Otomatis terlampir dari siklus mingguan (Tanpa perlu unduh/buka PDF)</p>
            </div>
          </div>
          <span class="text-[9px] font-bold bg-white text-emerald-800 px-2 py-0.5 rounded-md border border-emerald-200 shadow-2xs">Langsung Aktif</span>
        </div>

        <div id="note-team-body" class="mt-2.5 pt-2 border-t border-emerald-200/60 text-xs text-slate-800 space-y-1 font-medium leading-relaxed">
          <p>• Kupas bersih bahan nabati (wortel/buncis), buang serat dan bagian layu.</p>
          <p>• Potong dadu 2.5 cm presisi seragam untuk daging ayam fillet agar matang merata saat dimasak.</p>
          <p>• Wajib bilas 3x dengan air bersih mengalir sebelum ditimbang masuk ke stasiun pengolahan.</p>
        </div>
      </div>

      <!-- Dynamic Menu Items Container with attached note slips -->
      <div id="menu-items-container" class="space-y-3">
        <!-- Rendered by JavaScript -->
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 2: TIMBANG (NOTE CHEF PINNED ON SCALE)  -->
    <!-- ============================================== -->
    <section id="screen-home" class="space-y-3 hidden">
      
      <!-- STICKY NOTE PINNED RIGHT ABOVE SCALE INPUT -->
      <div id="autofill-banner" class="hidden note-paper-persiapan p-3.5 rounded-2xl flex items-start justify-between text-xs">
        <div class="flex items-start gap-2">
          <span class="text-base">📌</span>
          <div>
            <span id="autofill-banner-text" class="font-bold text-slate-900 block text-xs">Bahan Baku Dimuat</span>
            <div id="autofill-directive-text" class="text-slate-800 font-medium text-[11px] mt-1 bg-white/70 p-2 rounded-xl border border-emerald-200">
              <!-- Note text dynamically injected here -->
            </div>
          </div>
        </div>
        <button onclick="dismissAutofillBanner()" class="text-slate-400 hover:text-slate-700 font-bold p-1">✕</button>
      </div>

      <!-- TEAM SELECTOR IN SCALE -->
      <div class="bg-white border border-slate-200 p-3 rounded-2xl shadow-xs space-y-2">
        <div class="flex items-center justify-between">
          <label class="text-xs font-bold text-slate-700 uppercase tracking-wide">Stasiun Tim Penimbang</label>
          <span id="current-stage-badge" class="text-[10px] bg-emerald-100 text-emerald-800 font-bold px-2 py-0.5 rounded-full">
            Penerimaan & Sortir Persiapan
          </span>
        </div>
        
        <div class="grid grid-cols-3 gap-2">
          <button onclick="selectTeam('TIM PERSIAPAN')" class="team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-emerald-600 text-white shadow-sm flex items-center justify-center gap-1 cursor-pointer" data-team="TIM PERSIAPAN">
            <span>TIM PERSIAPAN</span>
          </button>
          <button onclick="selectTeam('TIM PENGOLAHAN')" class="team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1 cursor-pointer" data-team="TIM PENGOLAHAN">
            <span>TIM PENGOLAHAN</span>
          </button>
          <button onclick="selectTeam('TIM PEMORSIAN')" class="team-chip py-2.5 px-2 rounded-xl text-xs font-extrabold bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 flex items-center justify-center gap-1 cursor-pointer" data-team="TIM PEMORSIAN">
            <span>TIM PEMORSIAN</span>
          </button>
        </div>
      </div>

      <!-- FORM TIMBANG -->
      <div class="bg-white border border-slate-200 p-3.5 rounded-2xl shadow-xs space-y-3">
        <div>
          <label class="text-xs font-bold text-slate-700 block mb-1">Kategori Bahan</label>
          <select id="input-kategori" onchange="onCategoryChanged()" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 focus:outline-none focus:ring-2 focus:ring-emerald-500 cursor-pointer">
            <option value="Protein Hewani">Protein Hewani (Ayam, Daging, Ikan, Telur)</option>
            <option value="Protein Nabati">Protein Nabati (Tahu, Tempe)</option>
            <option value="Sayuran Segar">Sayuran Segar (Wortel, Buncis, Bayam)</option>
            <option value="Karbohidrat Pokok">Karbohidrat Pokok (Beras, Kentang)</option>
            <option value="Buah Segar">Buah Segar (Pisang, Semangka, Melon)</option>
            <option value="Bumbu Dapur">Bumbu Dapur & Minyak</option>
          </select>
        </div>

        <div>
          <label class="text-xs font-bold text-slate-700 block mb-1">Nama Bahan Baku</label>
          <input type="text" id="input-item" value="Daging Ayam Fillet" placeholder="Ketik atau pilih dari menu..." class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-900 focus:outline-none focus:ring-2 focus:ring-emerald-500">
          
          <!-- Quick item buttons -->
          <div id="quick-item-chips" class="flex flex-wrap gap-1.5 mt-2">
            <button onclick="pickQuickItem('Daging Ayam Fillet')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-[10px] font-bold text-slate-700 cursor-pointer">Daging Ayam Fillet</button>
            <button onclick="pickQuickItem('Daging Sapi Semur')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-[10px] font-bold text-slate-700 cursor-pointer">Daging Sapi Semur</button>
            <button onclick="pickQuickItem('Ikan Kembung Fillet')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-[10px] font-bold text-slate-700 cursor-pointer">Ikan Kembung Fillet</button>
            <button onclick="pickQuickItem('Telur Ayam Negeri')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-[10px] font-bold text-slate-700 cursor-pointer">Telur Ayam Negeri</button>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3 pt-1 border-t border-slate-100">
          <div>
            <label class="text-[11px] font-bold text-slate-700 block mb-1">Tara Wadah (kg)</label>
            <input type="number" step="0.01" id="input-tare" value="0.85" class="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-900 font-mono-num">
          </div>
          <div>
            <label class="text-[11px] font-bold text-slate-700 block mb-1">Preset Tara Wadah</label>
            <div class="flex gap-1">
              <button onclick="setTare(0.85)" class="flex-1 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-[10px] font-bold cursor-pointer font-mono-num">0.85</button>
              <button onclick="setTare(0.50)" class="flex-1 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-[10px] font-bold cursor-pointer font-mono-num">0.50</button>
              <button onclick="setTare(0.00)" class="flex-1 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-[10px] font-bold cursor-pointer">Nol</button>
            </div>
          </div>
        </div>

        <div class="space-y-2 pt-2 border-t border-slate-100">
          <label class="text-xs font-bold text-slate-700 block">Metode Penimbangan</label>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="simulateWeighAction('camera')" class="py-2.5 px-3 bg-slate-900 hover:bg-slate-800 text-white rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 shadow-sm cursor-pointer active:scale-95 transition-all">
              <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z"/><circle cx="12" cy="13" r="3" stroke-width="2"/></svg>
              <span>Foto Kamera</span>
            </button>
            <button onclick="simulateWeighAction('manual')" class="py-2.5 px-3 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 rounded-xl text-xs font-bold flex items-center justify-center gap-1.5 shadow-xs cursor-pointer active:scale-95 transition-all">
              <svg class="w-4 h-4 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>
              <span>Input Manual</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================== -->
    <!-- SCREEN 3: KERANJANG (EDIT, HAPUS, SYNC)        -->
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
        <!-- Rendered dynamically -->
      </div>

      <div class="pt-2">
        <button onclick="syncAllToGoogleSheets()" id="btn-sync-all" class="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-extrabold shadow-md flex items-center justify-center gap-2 cursor-pointer transition-all active:scale-98">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/></svg>
          <span>Sinkronkan ke Google Sheets Monitoring</span>
        </button>
      </div>
    </section>

    <!-- SCREEN 4: STOK GUDANG -->
    <section id="screen-stock" class="space-y-3 hidden">
      <div class="bg-white border border-slate-200 p-3.5 rounded-2xl shadow-xs">
        <h2 class="text-xs font-bold text-slate-900 uppercase tracking-wide mb-1">Stok Bahan Masuk Dapur MBG</h2>
        <p class="text-[10px] text-slate-500 mb-3">Monitoring stok real-time SPPG Kedungwuni Pekajangan 4</p>
        
        <div class="space-y-2">
          <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-slate-800 block">Daging Ayam Fillet</span>
              <p class="text-[10px] text-slate-500">Protein Hewani • Masuk: 210.00 kg • Sisa: 45.20 kg</p>
            </div>
            <span class="text-xs font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200 font-mono-num">Aman</span>
          </div>

          <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-slate-800 block">Wortel Brastagi Segar</span>
              <p class="text-[10px] text-slate-500">Sayuran Segar • Masuk: 120.00 kg • Sisa: 18.50 kg</p>
            </div>
            <span class="text-xs font-bold text-amber-700 bg-amber-50 px-2 py-0.5 rounded border border-amber-200 font-mono-num">Sedang</span>
          </div>

          <div class="p-2.5 bg-slate-50 border border-slate-200 rounded-xl flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-slate-800 block">Pisang Cavendish Standar BGN</span>
              <p class="text-[10px] text-slate-500">Buah Segar • Masuk: 3.000 pcs • Khusus Pemorsian</p>
            </div>
            <span class="text-xs font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded border border-blue-200 font-mono-num">Siap Saji</span>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- ======================================================== -->
  <!-- MODAL EDIT ITEM KERANJANG                                -->
  <!-- ======================================================== -->
  <div id="edit-cart-modal" class="fixed inset-0 bg-slate-950/70 z-50 flex items-center justify-center p-3 hidden">
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

  <!-- MODAL DOKUMEN PDF MASTER (ARSIP RESMI SAJA) -->
  <div id="pdf-viewer-modal" class="fixed inset-0 bg-slate-950/80 z-50 flex items-center justify-center p-3 hidden">
    <div class="bg-white rounded-2xl w-full max-w-xl max-h-[92vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden">
      <div class="bg-slate-900 text-white px-4 py-3 flex items-center justify-between border-b border-slate-800">
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold">Dokumen Master PDF Siklus 1 Minggu</span>
        </div>
        <div class="flex items-center gap-2">
          <a href="https://drive.google.com/file/d/1mmISuoKuOZmhYo-EafEFHWe1LxoEJmSH/view" target="_blank" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded text-[10px] font-bold border border-slate-700">Drive</a>
          <button onclick="closePdfViewerModal()" class="text-slate-400 hover:text-white font-bold text-sm px-2 cursor-pointer">✕</button>
        </div>
      </div>
      <div class="p-4 overflow-y-auto text-xs text-slate-700 space-y-2">
        <p class="font-bold">Arsip Resmi SOP & Siklus Menu 5 Hari MBG SPPG Pekajangan 04.</p>
        <p class="text-slate-500">Catatan: Di aplikasi ini seluruh arahan sudah otomatis terlampir sebagai NOTE pada setiap menu dan timbangan, sehingga tim dapur mboten perlu membuka berkas PDF ini lagi.</p>
      </div>
    </div>
  </div>

  <!-- NOTIFICATION TOAST -->
  <div id="toast" class="fixed bottom-4 left-1/2 -translate-x-1/2 bg-slate-900 text-white px-4 py-2.5 rounded-xl text-xs font-bold shadow-2xl flex items-center gap-2 transition-all opacity-0 pointer-events-none z-50">
    <span id="toast-msg">Notifikasi</span>
  </div>

<script>
// ========================================================
// DATA MENU MINGGUAN & NOTE RESMI CHEF LUTFI (5 HARI KERJA)
// ========================================================
const weeklyMenuData = {{
  senin: {{
    title: "Nasi Putih + Daging Ayam Semur Kecap + Tahu Goreng Gurih + Tumis Buncis Jagung Manis + Pisang Cavendish",
    nutrition: "Energi: 685 kkal • Protein: 28 gr • Serat: 5.2 gr",
    notePersiapan: "Kupas bersih wortel dan buncis, potong dadu 2.5 cm seragam untuk ayam fillet, bilas air mengalir 3x.",
    notePengolahan: "Tumis bumbu semur hingga harum tanak berminyak. Suhu inti ayam semur wajib minimal 75°C sebelum angkat.",
    notePemorsian: "Ompreng diisi nasi 150 gr di sekat utama, semur ayam 70 gr di sekat lauk. Pisang diperiksa kematangan & disajikan di sekat buah.",
    items: [
      {{
        name: "Daging Ayam Fillet",
        category: "Protein Hewani",
        portion: "70 gr / porsi (Total 210 kg)",
        tare: "0.85",
        persiapan: "Potong dadu 2.5 cm seragam, bilas air mengalir 3x, tiriskan sempurna sebelum ditimbang.",
        pengolahan: "Tumis bumbu semur sampai tanak, rebus sampai bumbu meresap. Pastikan suhu inti masakan daging minimal 75°C.",
        pemorsian: "Tata pada sekat lauk utama ompreng dengan kuah kental sedang, suhu saji dipertahankan minimal 60°C."
      }},
      {{
        name: "Tahu Putih Segar",
        category: "Protein Nabati",
        portion: "50 gr / porsi (Total 150 kg)",
        tare: "0.85",
        persiapan: "Potong kotak 3x3 cm, rendam dalam larutan garam & bawang putih 10 menit.",
        pengolahan: "Goreng dalam minyak panas 160°C hingga berkulit keemasan, tiriskan dari minyak berlebih.",
        pemorsian: "Letakkan 1 potong tahu di samping sekat lauk utama berdampingan dengan ayam."
      }},
      {{
        name: "Buncis & Jagung Manis",
        category: "Sayuran Segar",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.50",
        persiapan: "Siangi serat buncis, potong serong 2 cm, pipil jagung manis, cuci bersih dengan air mengalir.",
        pengolahan: "Tumis cepat (stir fry) api besar agar tekstur sayur tetap renyah (crunchy) dan warna hijau segar terjaga.",
        pemorsian: "Porsi sayur ditakar 2 sendok sayur standar (60 gr) pada sekat sayur ompreng."
      }},
      {{
        name: "Pisang Cavendish",
        category: "Buah Segar",
        portion: "1 pcs (100 gr) / porsi (Total 3.000 pcs)",
        tare: "0.00",
        persiapan: "TIM PERSIAPAN TIDAK MENANGANI BUAH. Langsung diserahkan utuh ke Tim Pemorsian.",
        pengolahan: "TIM PENGOLAHAN TIDAK MENANGANI BUAH. Buah segar dilarang terkena panas dapur.",
        pemorsian: "SOP KHUSUS BUAH SEGAR: Gunakan sarung tangan steril baru, sortir kulit mulus tanpa memar, letakkan di sekat buah paling kering."
      }}
    ]
  }},
  selasa: {{
    title: "Nasi Putih + Daging Sapi Teriyaki Lada Hitam + Tempe Goreng Tepung + Capcay Sayur Segar + Jeruk Manis",
    nutrition: "Energi 710 kkal • Protein 29 gr • Tinggi Zat Besi & Seng",
    notePersiapan: "Iris daging sapi slice tipis melawan serat (slice 2 mm). Rendam saus teriyaki 20 menit.",
    notePengolahan: "Tumis daging api besar cepat agar empuk (tidak alot). Suhu inti daging minimal 75°C.",
    notePemorsian: "Suhu saji 60°C. Jeruk dilap bersih kering dengan kain sanitasi food grade sebelum masuk sekat buah.",
    items: [
      {{
        name: "Daging Sapi Slice",
        category: "Protein Hewani",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.85",
        persiapan: "Iris slice tipis melawan serat ketebalan 2 mm, marinasi saus teriyaki 20 menit.",
        pengolahan: "Tumis dengan api besar cepat agar daging empuk dan saus mengental gurih. Suhu minimal 75°C.",
        pemorsian: "Takar 60 gr daging beserta saus teriyaki di sekat lauk utama ompreng."
      }},
      {{
        name: "Tempe Kedelai Murni",
        category: "Protein Nabati",
        portion: "45 gr / porsi (Total 135 kg)",
        tare: "0.50",
        persiapan: "Potong segitiga tebal 1 cm, celup adonan tepung bumbu ketumbar tipis.",
        pengolahan: "Goreng hingga krispi gurih keemasan, tiriskan minyak secara vertikal.",
        pemorsian: "Letakkan 1 potong tempe krispi berdampingan dengan daging sapi teriyaki."
      }},
      {{
        name: "Capcay Sayur Segar (Wortel, Kembang Kol, Sawi)",
        category: "Sayuran Segar",
        portion: "65 gr / porsi (Total 195 kg)",
        tare: "0.50",
        persiapan: "Potong kembang kol per kuntum kecil, wortel koin tipis, rendam air garam 5 menit untuk sterilisasi ulat.",
        pengolahan: "Masak kuah kaldu gurih sedikit kental, masukkan kembang kol terakhir agar tidak lembek.",
        pemorsian: "Isi sekat sayur ompreng dengan 1 sendok kuah sayur hangat."
      }},
      {{
        name: "Jeruk Manis Medan",
        category: "Buah Segar",
        portion: "1 pcs (Total 3.000 pcs)",
        tare: "0.00",
        persiapan: "Khusus Tim Pemorsian. Tim Persiapan tidak mengupas jeruk.",
        pengolahan: "Dilarang dimasak atau dipanaskan.",
        pemorsian: "SOP KHUSUS BUAH: Lap permukaan kulit jeruk dengan lap food-grade steril. Letakkan di sekat buah ompreng."
      }}
    ]
  }},
  rabu: {{
    title: "Nasi Putih + Ikan Kembung Asam Manis + Tempe Mendoan + Sayur Bayam Jagung Bening + Semangka Merah",
    nutrition: "Energi 660 kkal • Protein 26 gr • Tinggi Asam Lemak Omega-3",
    notePersiapan: "QC raba pastikan ikan kembung fillet bebas duri. Sayur bayam dipetik daun muda saja.",
    notePengolahan: "Goreng ikan kembung suhu 170°C hingga renyah. Bayam dimasukkan setelah air mendidih lalu langsung matikan kompor.",
    notePemorsian: "Semangka dipotong segitiga tebal 2 cm di ruang dingin beralas talenan khusus buah, sajikan di sekat buah.",
    items: [
      {{
        name: "Ikan Kembung Fillet",
        category: "Protein Hewani",
        portion: "65 gr / porsi (Total 195 kg)",
        tare: "0.85",
        persiapan: "QC raba pastikan bebas duri, lumuri perasan jeruk nipis 15 menit bilas tiris.",
        pengolahan: "Goreng krispi suhu minyak 170°C, siram saus asam manis nanas sesaat sebelum saji.",
        pemorsian: "Tata 1 potong fillet ikan siram saus asam manis di sekat lauk utama."
      }},
      {{
        name: "Sayur Bayam Jagung Bening",
        category: "Sayuran Segar",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.50",
        persiapan: "Petik daun bayam segar, pipil jagung manis, bilas 3x dengan air dingin.",
        pengolahan: "Masak kuah bening temu kunci, masukkan bayam 1 menit sebelum api dimatikan agar tetap hijau cerah.",
        pemorsian: "Tuang sayur bayam dan jagung di sekat sayur ompreng sesaat sebelum distribusi."
      }},
      {{
        name: "Semangka Merah Potong",
        category: "Buah Segar",
        portion: "80 gr (1 slice) / porsi (Total 240 kg)",
        tare: "0.85",
        persiapan: "Khusus Tim Pemorsian. Gunakan talenan kuning khusus buah.",
        pengolahan: "Dilarang terkena area kompor/panas.",
        pemorsian: "SOP BUAH SEGAR: Potong bentuk juring/segitiga tebal 2 cm, pastikan biji hitam dibersihkan, letakkan di sekat buah."
      }}
    ]
  }},
  kamis: {{
    title: "Nasi Putih + Ayam Panggang Bumbu Madu + Rolade Tahu Telur + Sayur Labu Siam Wortel Gurih + Melon Cantaloupe",
    nutrition: "Energi 695 kkal • Protein 28 gr • Kaya Vitamin A & Mineral",
    notePersiapan: "Ayam dibelah paha/dada fillet seragam. Labu siam dipotong korek api tebal.",
    notePengolahan: "Panggang oven atau wajan datar suhu 180°C oles madu. Suhu inti ayam wajib minimal 75°C.",
    notePemorsian: "Melon dipotong dadu besar beralas talenan steril. Letakkan rapi di sekat buah ompreng.",
    items: [
      {{
        name: "Ayam Panggang Madu",
        category: "Protein Hewani",
        portion: "70 gr / porsi (Total 210 kg)",
        tare: "0.85",
        persiapan: "Tusuk-tusuk daging ayam agar bumbu madu meresap ke serat terdalam.",
        pengolahan: "Panggang hingga karamelisasi keemasan merata. Suhu inti wajib di atas 75°C.",
        pemorsian: "Tata 1 potong ayam panggang di sekat lauk ompreng."
      }},
      {{
        name: "Sayur Labu Siam & Wortel",
        category: "Sayuran Segar",
        portion: "60 gr / porsi (Total 180 kg)",
        tare: "0.50",
        persiapan: "Kupas labu siam buang getah dengan digosok garam, potong korek api tebal 5 mm.",
        pengolahan: "Tumis dengan kuah santan sangat encer atau kaldu ayam gurih.",
        pemorsian: "Takar 60 gr di sekat sayur ompreng."
      }},
      {{
        name: "Melon Cantaloupe Segar",
        category: "Buah Segar",
        portion: "80 gr / porsi (Total 240 kg)",
        tare: "0.85",
        persiapan: "Khusus Tim Pemorsian.",
        pengolahan: "Dilarang dipanaskan.",
        pemorsian: "Kupas kulit melon, potong ketebalan 1.5 cm rapi, simpan di wadah sejuk tertutup sebelum masuk ompreng."
      }}
    ]
  }},
  jumat: {{
    title: "Nasi Putih + Telur Balado Pedas Manis + Perkedel Kentang Daging + Sayur Lodeh Labu + Pepaya California",
    nutrition: "Energi 670 kkal • Protein 25 gr • Serat & Enzim Pencernaan Alami",
    notePersiapan: "Kupas telur rebus mulus tanpa cacat putih telur. Kupas kentang dan labu siam bersih.",
    notePengolahan: "Goreng telur hingga berkulit tipis, lumuri sambal balado manis gurih. Suhu inti telur 75°C.",
    notePemorsian: "Pepaya dipotong dadu 3 cm higienis. Ompreng ditutup rapat dan dicek sebelum diantar ke sekolah.",
    items: [
      {{
        name: "Telur Ayam Balado",
        category: "Protein Hewani",
        portion: "1 butir (55 gr) (Total 3.000 butir)",
        tare: "0.85",
        persiapan: "Rebus telur 11 menit, rendam air es, kupas mulus tanpa merusak putih telur.",
        pengolahan: "Goreng cepat agar berkulit, aduk rata bersama saus balado bumbu tomat masak tanak.",
        pemorsian: "Letakkan 1 butir telur balado utuh di sekat lauk ompreng."
      }},
      {{
        name: "Perkedel Kentang Gurih",
        category: "Protein Nabati",
        portion: "40 gr / porsi (Total 120 kg)",
        tare: "0.50",
        persiapan: "Kupas kentang, goreng matang, haluskan selagi hangat dengan bumbu seledri dan bawang goreng.",
        pengolahan: "Bentuk bulat pipih, balur kocokan putih telur, goreng api sedang sampai keemasan.",
        pemorsian: "Letakkan perkedel mendampingi telur balado di sekat ompreng."
      }},
      {{
        name: "Pepaya California Manis",
        category: "Buah Segar",
        portion: "80 gr / porsi (Total 240 kg)",
        tare: "0.85",
        persiapan: "Khusus Tim Pemorsian.",
        pengolahan: "Dilarang dipanaskan.",
        pemorsian: "SOP BUAH SEGAR: Buang biji hitam, potong dadu 3 cm rapi, sajikan dingin di sekat buah ompreng."
      }}
    ]
  }}
}};

let currentDay = 'senin';
let currentActiveStation = 'persiapan';

// INITIAL STAGING ITEMS
let stagingItems = [
  {{
    id: "cart_1",
    timestamp: "11:20:15",
    team: "TIM PERSIAPAN",
    category: "Protein Hewani",
    name: "Daging Ayam Fillet (Batch 1)",
    bruto: 25.85,
    tara: 0.85,
    netto: 25.00,
    catatan: "Sesuai Note Chef: Dadu 2.5 cm, bilas 3x",
    synced: false
  }},
  {{
    id: "cart_2",
    timestamp: "11:28:40",
    team: "TIM PERSIAPAN",
    category: "Sayuran Segar",
    name: "Wortel Brastagi Potong Koin",
    bruto: 15.50,
    tara: 0.50,
    netto: 15.00,
    catatan: "Sesuai Note Chef: Tebal 4 mm seragam",
    synced: false
  }},
  {{
    id: "cart_3",
    timestamp: "11:35:10",
    team: "TIM PEMORSIAN",
    category: "Buah Segar",
    name: "Pisang Cavendish Sisir A",
    bruto: 30.00,
    tara: 0.00,
    netto: 30.00,
    catatan: "Sesuai SOP Buah: Sortir kulit mulus steril",
    synced: false
  }}
];

document.addEventListener('DOMContentLoaded', () => {{
  renderWeeklyMenu();
  renderStagingList();
}});

function switchScreen(screenId) {{
  ['menu', 'home', 'staging', 'stock'].forEach(s => {{
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
  const cur = weeklyMenuData[day];

  if (heroLabel) heroLabel.innerText = 'Menu Hari ' + day.toUpperCase();
  if (heroTitle) heroTitle.innerText = cur.title;
  if (heroNutrition) heroNutrition.innerText = cur.nutrition;

  renderWeeklyMenu();
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
  const cur = weeklyMenuData[currentDay];

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

function renderWeeklyMenu() {{
  const container = document.getElementById('menu-items-container');
  if (!container) return;
  container.innerHTML = '';

  const dayData = weeklyMenuData[currentDay];
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
  showToast('Preset Tara disetel: ' + val.toFixed(2) + ' kg');
}}

function pickQuickItem(name) {{
  const inputItem = document.getElementById('input-item');
  if (inputItem) inputItem.value = name;
  showToast('Memilih bahan: ' + name);
}}

function onCategoryChanged() {{
  const cat = document.getElementById('input-kategori').value;
  const chipContainer = document.getElementById('quick-item-chips');
  if (!chipContainer) return;

  const quickMap = {{
    "Protein Hewani": ["Daging Ayam Fillet", "Daging Sapi Slice", "Ikan Kembung Fillet", "Telur Ayam"],
    "Protein Nabati": ["Tahu Putih Segar", "Tempe Kedelai Murni", "Rolade Tahu Telur"],
    "Sayuran Segar": ["Wortel Brastagi", "Buncis Manis", "Kembang Kol", "Bayam Segar", "Labu Siam"],
    "Karbohidrat Pokok": ["Beras Putih Premium", "Kentang Dieng"],
    "Buah Segar": ["Pisang Cavendish", "Semangka Merah", "Melon Cantaloupe", "Jeruk Manis", "Pepaya California"],
    "Bumbu Dapur": ["Bawang Merah", "Bawang Putih", "Garam Beriodium", "Gula Pasir", "Minyak Goreng Sawit"]
  }};

  const items = quickMap[cat] || [];
  chipContainer.innerHTML = '';
  items.forEach(it => {{
    const b = document.createElement('button');
    b.onclick = () => pickQuickItem(it);
    b.className = 'px-2.5 py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-[10px] font-bold text-slate-700 cursor-pointer';
    b.innerText = it;
    chipContainer.appendChild(b);
  }});

  if (items.length > 0) {{
    pickQuickItem(items[0]);
  }}

  if (cat === 'Buah Segar') {{
    selectTeam('TIM PEMORSIAN');
    showToast('Buah Segar otomatis dialihkan ke TIM PEMORSIAN');
  }}
}}

function simulateWeighAction(mode) {{
  const item = document.getElementById('input-item').value || 'Bahan MBG';
  const cat = document.getElementById('input-kategori').value;
  const tare = parseFloat(document.getElementById('input-tare').value) || 0.85;

  let activeTeam = 'TIM PERSIAPAN';
  const activeBtn = document.querySelector('.team-chip.bg-emerald-600, .team-chip.bg-amber-600, .team-chip.bg-blue-600');
  if (activeBtn) activeTeam = activeBtn.dataset.team;

  const simulatedBruto = (mode === 'camera') ? (Math.random() * 15 + 10) : (Math.random() * 8 + 5);
  const roundedBruto = parseFloat(simulatedBruto.toFixed(2));
  const roundedNetto = parseFloat(Math.max(0, roundedBruto - tare).toFixed(2));

  const newItem = {{
    id: 'cart_' + Date.now(),
    timestamp: new Date().toLocaleTimeString('id-ID'),
    team: activeTeam,
    category: cat,
    name: item,
    bruto: roundedBruto,
    tara: tare,
    netto: roundedNetto,
    catatan: 'Ditimbang via ' + (mode === 'camera' ? 'OCR Kamera' : 'Manual'),
    synced: false
  }};

  stagingItems.unshift(newItem);
  renderStagingList();
  showToast('Ditambahkan ke Keranjang (' + roundedNetto + ' kg)');
  switchScreen('staging');
}}

function renderStagingList() {{
  const list = document.getElementById('staging-items-list');
  const countBadge = document.getElementById('staging-count-badge');
  const cartTabBadge = document.getElementById('tab-cart-badge');

  if (countBadge) countBadge.innerText = stagingItems.length + ' Item';
  if (cartTabBadge) cartTabBadge.innerText = stagingItems.length;

  if (!list) return;
  list.innerHTML = '';

  if (stagingItems.length === 0) {{
    list.innerHTML = '<div class="p-8 text-center text-slate-400 bg-white border border-slate-200 rounded-2xl">' +
      '<p class="text-xs font-bold">Keranjang masih kosong</p>' +
      '<p class="text-[10px] mt-1">Lakukan penimbangan dari menu untuk menambah item</p>' +
    '</div>';
    return;
  }}

  stagingItems.forEach(item => {{
    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200 p-3 rounded-2xl shadow-xs space-y-2';

    let teamBg = 'bg-emerald-50 text-emerald-800 border-emerald-200';
    if (item.team === 'TIM PENGOLAHAN') teamBg = 'bg-amber-50 text-amber-800 border-amber-200';
    if (item.team === 'TIM PEMORSIAN') teamBg = 'bg-blue-50 text-blue-800 border-blue-200';

    card.innerHTML = '<div class="flex items-start justify-between">' +
      '<div>' +
        '<div class="flex items-center gap-1.5">' +
          '<h4 class="text-xs font-bold text-slate-900">' + item.name + '</h4>' +
          '<span class="text-[9px] font-extrabold px-1.5 py-0.5 rounded border ' + teamBg + '">' + item.team + '</span>' +
        '</div>' +
        '<p class="text-[10px] text-slate-500 mt-0.5 font-mono-num">' + item.timestamp + ' • ' + item.category + '</p>' +
      '</div>' +
      '<div class="text-right">' +
        '<span class="text-sm font-extrabold text-emerald-600 font-mono-num">' + item.netto.toFixed(2) + ' kg</span>' +
        '<span class="block text-[9px] text-slate-400 font-mono-num">Bruto: ' + item.bruto.toFixed(2) + ' | Tara: ' + item.tara.toFixed(2) + '</span>' +
      '</div>' +
    '</div>' +
    (item.catatan ? '<p class="text-[10px] text-slate-600 bg-slate-50 px-2 py-1 rounded-lg border border-slate-100 font-medium">' + item.catatan + '</p>' : '') +
    '<div class="flex items-center justify-end gap-2 pt-1 border-t border-slate-100">' +
      '<button onclick="openEditModal(\\\'' + item.id + '\\\')" class="px-2.5 py-1 text-[10px] font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 rounded-lg flex items-center gap-1 cursor-pointer">' +
        '<svg class="w-3 h-3 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"/></svg>' +
        '<span>Koreksi / Edit</span>' +
      '</button>' +
      '<button onclick="confirmDeleteItem(\\\'' + item.id + '\\\')" class="px-2.5 py-1 text-[10px] font-bold text-rose-700 bg-rose-50 hover:bg-rose-100 rounded-lg flex items-center gap-1 cursor-pointer border border-rose-200">' +
        '<svg class="w-3 h-3 text-rose-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>' +
        '<span>Hapus</span>' +
      '</button>' +
    '</div>';

    list.appendChild(card);
  }});
}}

function openEditModal(itemId) {{
  const item = stagingItems.find(i => i.id === itemId);
  if (!item) return;

  document.getElementById('edit-item-id').value = item.id;
  document.getElementById('edit-item-name').value = item.name;
  document.getElementById('edit-item-team').value = item.team;
  document.getElementById('edit-item-bruto').value = item.bruto;
  document.getElementById('edit-item-tara').value = item.tara;
  document.getElementById('edit-item-catatan').value = item.catatan || '';

  recalcEditNetto();
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
  const item = stagingItems.find(i => i.id === id);
  if (!item) return;

  item.name = document.getElementById('edit-item-name').value;
  item.team = document.getElementById('edit-item-team').value;
  item.bruto = parseFloat(document.getElementById('edit-item-bruto').value) || 0;
  item.tara = parseFloat(document.getElementById('edit-item-tara').value) || 0;
  item.netto = parseFloat(Math.max(0, item.bruto - item.tara).toFixed(2));
  item.catatan = document.getElementById('edit-item-catatan').value;

  closeEditModal();
  renderStagingList();
  showToast('Perubahan item berhasil disimpan');
}}

function confirmDeleteItem(itemId) {{
  const item = stagingItems.find(i => i.id === itemId);
  if (!item) return;
  stagingItems = stagingItems.filter(i => i.id !== itemId);
  renderStagingList();
  showToast('Item ' + item.name + ' dihapus dari keranjang');
}}

function syncAllToGoogleSheets() {{
  if (stagingItems.length === 0) {{
    showToast('Keranjang kosong, tidak ada item untuk disinkron');
    return;
  }}

  const btn = document.getElementById('btn-sync-all');
  if (btn) {{
    btn.disabled = true;
    btn.innerHTML = '<span class="animate-spin text-base">⏳</span><span>Menyinkronkan ke Google Sheets...</span>';
  }}

  setTimeout(() => {{
    stagingItems = [];
    renderStagingList();
    if (btn) {{
      btn.disabled = false;
      btn.innerHTML = '<svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg><span>Berhasil Tersinkron ke Spreadsheet!</span>';
    }}
    showToast('Semua item berhasil disinkronkan ke Google Sheet Monitoring!');
    setTimeout(() => {{
      if (btn) {{
        btn.innerHTML = '<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/></svg><span>Sinkronkan ke Google Sheets Monitoring</span>';
      }}
    }}, 2500);
  }}, 1500);
}}

function openPdfViewerModal() {{
  const modal = document.getElementById('pdf-viewer-modal');
  if (modal) modal.classList.remove('hidden');
}}

function closePdfViewerModal() {{
  const modal = document.getElementById('pdf-viewer-modal');
  if (modal) modal.classList.add('hidden');
}}

function showWebhookInfo() {{
  showToast('Tersambung ke Google Sheet MBG PEKAJANGAN 04');
}}

function showToast(msg) {{
  const toast = document.getElementById('toast');
  const toastMsg = document.getElementById('toast-msg');
  if (!toast || !toastMsg) return;
  toastMsg.innerText = msg;
  toast.classList.remove('opacity-0', 'pointer-events-none');
  setTimeout(() => {{
    toast.classList.add('opacity-0', 'pointer-events-none');
  }}, 2200);
}}
</script>
</body>
</html>
'''

# Update to all paths
paths = [
    r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\mbg_kitchen_monitor_preview.html',
    r'C:\Users\HP\Projects\APlikasi MBG\mbg_kitchen_monitor_preview.html',
    r'C:\Users\HP\Projects\APlikasi MBG\preview.html'
]

for p in paths:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'Updated {p}')

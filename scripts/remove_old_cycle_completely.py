"""
Hapus seluruh menu 16-27 dan Siklus 2 dari preview.html dan index.html.
Jadikan aplikasi hanya menampilkan Menu Resmi 09 - 13 November 2026.
"""
import re

with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Hapus tombol Siklus 2 dari UI Cycle Toggle Switcher
old_cycle_switcher = '''          <div class="flex items-center gap-1 bg-slate-100 p-0.5 rounded-xl border border-slate-200 text-[10px] font-extrabold">
            <button onclick="selectCycle('cycle1')" id="cycle-btn-1" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white shadow-xs cursor-pointer transition-all">Siklus 1 (09-13 Nov)</button>
            <button onclick="selectCycle('cycle2')" id="cycle-btn-2" class="px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 cursor-pointer transition-all">Siklus 2 (16-20 Nov)</button>
          </div>'''

new_cycle_switcher = '''          <div class="flex items-center gap-1.5 bg-emerald-50 px-2.5 py-1 rounded-xl border border-emerald-200 text-[11px] font-extrabold text-emerald-800">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>Menu Aktif: 09 - 13 November 2026</span>
          </div>'''

c = c.replace(old_cycle_switcher, new_cycle_switcher)

# 2. Update Cycle indicator label
c = c.replace('Siklus 1: 09 - 13 November 2026', 'Menu Resmi: 09 - 13 November 2026')
c = c.replace('Siklus 1: 16 - 20 November 2026', 'Menu Resmi: 09 - 13 November 2026')

# 3. Update tombol hari dengan tanggal eksplisit
old_days = '''          <button onclick="selectDay('senin')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer" data-day="senin">SENIN</button>
          <button onclick="selectDay('selasa')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="selasa">SELASA</button>
          <button onclick="selectDay('rabu')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="rabu">RABU</button>
          <button onclick="selectDay('kamis')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="kamis">KAMIS</button>
          <button onclick="selectDay('jumat')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="jumat">JUMAT</button>'''

new_days = '''          <button onclick="selectDay('senin')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-slate-900 text-white shadow-sm cursor-pointer" data-day="senin">SENIN (09 Nov)</button>
          <button onclick="selectDay('selasa')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="selasa">SELASA (10 Nov)</button>
          <button onclick="selectDay('rabu')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="rabu">RABU (11 Nov)</button>
          <button onclick="selectDay('kamis')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="kamis">KAMIS (12 Nov)</button>
          <button onclick="selectDay('jumat')" class="day-btn px-3.5 py-1.5 rounded-xl text-xs font-bold shrink-0 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 cursor-pointer" data-day="jumat">JUMAT (13 Nov)</button>'''

c = c.replace(old_days, new_days)

# 4. Hapus tombol Siklus 2 dari modal Input Resep Chef
old_modal_switcher = '''          <div class="grid grid-cols-2 gap-1.5">
            <button onclick="selectChefFormCycle('cycle1')" id="chef-cycle-1" class="py-1.5 rounded-lg font-extrabold text-[10px] bg-slate-900 text-white shadow-xs cursor-pointer">Siklus 1 (09-13 Nov)</button>
            <button onclick="selectChefFormCycle('cycle2')" id="chef-cycle-2" class="py-1.5 rounded-lg font-extrabold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">Siklus 2 (16-20 Nov)</button>
          </div>'''

new_modal_switcher = '''          <div class="bg-emerald-50 border border-emerald-200 text-emerald-800 text-[11px] font-bold px-3 py-1.5 rounded-xl text-center">
            Menu Aktif: 09 - 13 November 2026 (SPPG Pekajangan 04)
          </div>'''

c = c.replace(old_modal_switcher, new_modal_switcher)

# 5. Hapus blok cycle2 dari JavaScript weeklyMenuCycles
cycle2_block_pattern = r',\s*cycle2:\s*\{.*?\}\s*\}\s*;'
c = re.sub(cycle2_block_pattern, '\n  }\n};', c, flags=re.DOTALL)

# 6. Reset localStorage yang menyimpan cache lama
cache_cleaner = '''// Bersihkan cache menu lama agar tidak ada residu 16-27
try {
  localStorage.removeItem('mbg_custom_recipes');
} catch(e) {}
'''
c = c.replace('// Restore custom recipes from localStorage if available', cache_cleaner + '\n// Restore custom recipes from localStorage if available')

# 7. Update initial stagingItems dengan data real Senin 9 Nov
old_staging = '''let stagingItems = [
  {
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
  },
  {
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
  },
  {
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
  }
];'''

new_staging = '''let stagingItems = [
  {
    id: "cart_1",
    timestamp: "06:30:15",
    team: "TIM PERSIAPAN",
    category: "Protein Hewani",
    name: "Ayam Dada Fillet (Potong Dadu Rica & Kecap)",
    bruto: 58.85,
    tara: 0.85,
    netto: 58.00,
    catatan: "Sesuai Note Chef: Potong dadu 2.5 cm, siap masak rica & kecap",
    synced: false
  },
  {
    id: "cart_2",
    timestamp: "06:45:20",
    team: "TIM PERSIAPAN",
    category: "Sayuran Segar",
    name: "Putren & Wortel (Iris Serong Seragam)",
    bruto: 24.50,
    tara: 0.50,
    netto: 24.00,
    catatan: "Sesuai Note Chef: Cuci bersih, tiriskan, siap stir-fry",
    synced: false
  },
  {
    id: "cart_3",
    timestamp: "07:10:00",
    team: "TIM PEMORSIAN",
    category: "Buah Segar",
    name: "Jeruk Medan (isi 10-12 per kg)",
    bruto: 45.00,
    tara: 0.00,
    netto: 45.00,
    catatan: "Sesuai SOP Buah: Lap sanitasi kering, letakkan di sekat buah",
    synced: false
  }
];'''

c = c.replace(old_staging, new_staging)

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

c_local = c.replace('https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js', 'tailwindcss.min.js')
with open('mbg_chef_monitor/assets/web/index.html', 'w', encoding='utf-8') as f:
    f.write(c_local)

print('PURGED_16_27_COMPLETELY_SUCCESS')


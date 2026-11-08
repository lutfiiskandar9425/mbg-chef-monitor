with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace chef form cycle buttons
old_c_btn = """          <div class="grid grid-cols-2 gap-2 mb-2">
            <button onclick="selectChefFormCycle('cycle1')" id="chef-cycle-1" class="py-1.5 rounded-lg font-extrabold text-[10px] bg-amber-600 text-white cursor-pointer">Siklus 1 (09-13 Nov)</button>
            <button onclick="selectChefFormCycle('cycle2')" id="chef-cycle-2" class="py-1.5 rounded-lg font-extrabold text-[10px] bg-slate-100 text-slate-700 hover:bg-slate-200 cursor-pointer">Siklus 2 (16-20 Nov)</button>
          </div>"""

new_c_btn = """          <div class="mb-2 py-1.5 px-3 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800 text-[11px] font-extrabold text-center">
            Menu Mingguan Resmi: 09 - 13 November 2026
          </div>"""
c = c.replace(old_c_btn, new_c_btn)

# Replace cycleNum
c = c.replace("const cycleNum = currentCycle === 'cycle1' ? '1 (16-20 Nov 2026)' : '2 (23-27 Nov 2026)';", "const cycleNum = '09 - 13 November 2026';")

# Clean selectCycle function
old_select_cycle = """function selectCycle(cycleKey) {
  currentCycle = cycleKey;
  const btn1 = document.getElementById('cycle-btn-1');
  const btn2 = document.getElementById('cycle-btn-2');
  const label = document.getElementById('cycle-indicator-label');

  if (cycleKey === 'cycle1') {
    btn1.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white shadow-xs cursor-pointer transition-all';
    btn2.className = 'px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 cursor-pointer transition-all';
    if (label) label.innerText = 'Siklus 1: 09 - 13 November 2026';
  } else {
    btn2.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white shadow-xs cursor-pointer transition-all';
    btn1.className = 'px-2.5 py-1 rounded-lg text-slate-600 hover:text-slate-900 cursor-pointer transition-all';
    if (label) label.innerText = 'Siklus 2: 16 - 20 November 2026';
  }

  selectDay(currentDay);
  showToast('Memuat ' + weeklyMenuCycles[cycleKey].label);
}"""

new_select_cycle = """function selectCycle(cycleKey) {
  currentCycle = 'cycle1';
  selectDay(currentDay);
}"""
c = c.replace(old_select_cycle, new_select_cycle)

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

c_local = c.replace('https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js', 'tailwindcss.min.js')
with open('mbg_chef_monitor/assets/web/index.html', 'w', encoding='utf-8') as f:
    f.write(c_local)

print('CLEANUP_FINAL_SUCCESS')


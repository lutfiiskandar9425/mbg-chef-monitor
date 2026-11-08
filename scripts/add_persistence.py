with open('preview.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('const weeklyMenuCycles = {', 'let weeklyMenuCycles = {')

save_target = "showToast('Resep ' + formActiveDay.toUpperCase() + ' (' + formActiveCycle + ') berhasil disiarkan!');"
save_logic = """  try {
    localStorage.setItem('mbg_custom_recipes', JSON.stringify(weeklyMenuCycles));
  } catch(e) {}
  showToast('Resep ' + formActiveDay.toUpperCase() + ' (' + formActiveCycle + ') berhasil disiarkan!');"""

c = c.replace(save_target, save_logic)

load_logic = """// Restore custom recipes from localStorage if available
try {
  const savedMenu = localStorage.getItem('mbg_custom_recipes');
  if (savedMenu) {
    const parsed = JSON.parse(savedMenu);
    for (let cyc in parsed) {
      if (weeklyMenuCycles[cyc]) {
        for (let d in parsed[cyc].days) {
          if (weeklyMenuCycles[cyc].days[d]) {
            Object.assign(weeklyMenuCycles[cyc].days[d], parsed[cyc].days[d]);
          }
        }
      }
    }
  }
} catch(e) {}
"""

c = c.replace('let currentCycle = "cycle1";', load_logic + '\nlet currentCycle = "cycle1";')

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

c_local = c.replace('https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js', 'tailwindcss.min.js')
with open('mbg_chef_monitor/assets/web/index.html', 'w', encoding='utf-8') as f:
    f.write(c_local)

print('PERSISTENCE_ENABLED_SUCCESS')


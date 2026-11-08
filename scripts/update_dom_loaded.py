import os

files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']
target = """document.addEventListener('DOMContentLoaded', () => {
  renderWeeklyMenu();
  renderAslapChecklist();
  renderStagingList();
});"""

replacement = """document.addEventListener('DOMContentLoaded', () => {
  updateStickyNoteContent();
  renderSchoolBatchSection();
  renderWeeklyMenu();
  renderAslapChecklist();
  renderStagingList();
});"""

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if target in content:
            content = content.replace(target, replacement)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Updated DOMContentLoaded in", fpath)
        else:
            print("Target not found in", fpath)


const fs = require('fs');

const files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html'];

files.forEach(fp => {
  if (!fs.existsSync(fp)) return;
  let content = fs.readFileSync(fp, 'utf8');
  
  // 1. Remove "Input Resep Chef" button from header
  const headerBtnRegex = /<!--\s*Tombol Input Resep Chef\s*-->[\s\S]*?<\/button>\s*/i;
  if (headerBtnRegex.test(content)) {
    content = content.replace(headerBtnRegex, '');
    console.log(`Removed header "Input Resep Chef" button in ${fp}`);
  }
  
  // 2. Remove "Spreadsheet" link from header
  const headerSheetRegex = /<!--\s*Shortcut Tautan Google Drive Folder & Sheet\s*-->[\s\S]*?<\/a>\s*/i;
  if (headerSheetRegex.test(content)) {
    content = content.replace(headerSheetRegex, '');
    console.log(`Removed header "Spreadsheet" link in ${fp}`);
  }
  
  // 3. Remove "Edit Resep Chef" button above day selector
  const editBtnRegex = /<button onclick="openChefRecipeModal\(\)"[^>]*>[\s\S]*?<span>✏️ Edit Resep Chef<\/span>[\s\S]*?<\/button>\s*/i;
  if (editBtnRegex.test(content)) {
    content = content.replace(editBtnRegex, '');
    console.log(`Removed "Edit Resep Chef" button in ${fp}`);
  }

  fs.writeFileSync(fp, content, 'utf8');
});

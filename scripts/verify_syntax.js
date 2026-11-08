const fs = require('fs');

const files = [
  'preview.html',
  'index.html',
  'mbg_chef_monitor/assets/web/index.html'
];

files.forEach(file => {
  const html = fs.readFileSync(file, 'utf8');
  const scriptRegex = /<script(?![^>]*src=)[^>]*>([\s\S]*?)<\/script>/gi;
  let match;
  let scriptIdx = 0;
  let hasError = false;

  while ((match = scriptRegex.exec(html)) !== null) {
    scriptIdx++;
    const code = match[1];
    try {
      new Function(code);
    } catch (err) {
      console.error(`Syntax error in ${file} (script #${scriptIdx}):`, err.message);
      hasError = true;
    }
  }

  if (!hasError) {
    console.log(`[PASS] ${file}: All ${scriptIdx} inline scripts parsed successfully without syntax errors.`);
  }
});

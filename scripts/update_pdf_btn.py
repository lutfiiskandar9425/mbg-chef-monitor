# -*- coding: utf-8 -*-
files = ['preview.html', 'index.html', 'mbg_chef_monitor/assets/web/index.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Add id to the link
    target_link = '<a href="https://drive.google.com/file/d/1wIF4ZxNK_YzfMAoPch5MXb9AWEIL6vNX/view?usp=sharing" target="_blank"'
    repl_link = '<a id="modal-drive-pdf-btn" href="https://drive.google.com/file/d/1wIF4ZxNK_YzfMAoPch5MXb9AWEIL6vNX/view?usp=sharing" target="_blank"'
    if target_link in c:
        c = c.replace(target_link, repl_link)

    # In openFullDirectiveModal, update href
    target_fn = 'const dayBatch = schoolBatchesData[currentDay] || schoolBatchesData[\'senin\'];\n  \n  let html ='
    repl_fn = '''const dayBatch = schoolBatchesData[currentDay] || schoolBatchesData['senin'];
  
  const pdfBtn = document.getElementById('modal-drive-pdf-btn');
  if (pdfBtn) {
    if (currentDay === 'selasa') {
      pdfBtn.href = 'https://drive.google.com/drive/folders/1unodAt2RR0z8zoSBmzUMUjlQ_OZues06';
    } else {
      pdfBtn.href = 'https://drive.google.com/file/d/1wIF4ZxNK_YzfMAoPch5MXb9AWEIL6vNX/view?usp=sharing';
    }
  }

  let html ='''

    if target_fn in c:
        c = c.replace(target_fn, repl_fn)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Updated {fn}")

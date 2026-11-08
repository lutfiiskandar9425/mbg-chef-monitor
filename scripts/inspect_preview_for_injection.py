# -*- coding: utf-8 -*-
import re
import os

with open('preview.html', 'r', encoding='utf-8') as f:
    preview_content = f.read()

# Check what we need to replace in preview.html, index.html, mbg_chef_monitor/assets/web/index.html
print("preview_content size:", len(preview_content))


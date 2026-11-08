# -*- coding: utf-8 -*-
import urllib.request

req = urllib.request.Request(
    'https://lutfiiskandar9425.github.io/mbg-chef-monitor/',
    headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'}
)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

print("Live online length:", len(html))
print("Has camera-options-modal:", 'id="camera-options-modal"' in html)
print("Has scale-camera-input:", 'id="scale-camera-input"' in html)
print("Has openCameraOptionsModal:", 'openCameraOptionsModal' in html)
print("Has generateSampleScalePhoto:", 'generateSampleScalePhoto' in html)

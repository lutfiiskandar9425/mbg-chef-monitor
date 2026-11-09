# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 420, 'height': 850})

        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # 1. Switch to screen-home
        page.evaluate("switchScreen('home')")
        page.wait_for_timeout(500)

        # Screenshot mobile view with Buka Kamera and Pilih Galeri
        page.screenshot(path='mobile_camera_and_gallery_buttons.png', full_page=False)
        print("Captured mobile_camera_and_gallery_buttons.png")

        # Check input elements
        cam_input = page.locator('#scale-camera-input')
        gal_input = page.locator('#scale-gallery-input')
        print("Camera input attached:", cam_input.count() > 0)
        print("Gallery input attached:", gal_input.count() > 0)

        # 2. Test attaching a photo via canvas/data URL into currentScalePhoto
        page.evaluate("""
          const canvas = document.createElement('canvas');
          canvas.width = 400; canvas.height = 300;
          const ctx = canvas.getContext('2d');
          ctx.fillStyle = '#0f172a'; ctx.fillRect(0, 0, 400, 300);
          ctx.fillStyle = '#10b981'; ctx.font = '24px sans-serif';
          ctx.fillText('BUKTI FOTO TIMBANGAN', 50, 150);
          currentScalePhoto = canvas.toDataURL('image/jpeg', 0.85);
          currentScalePhotoTime = '08.55 WIB';
          renderScalePhotoPreview();
        """)
        page.wait_for_timeout(500)

        page.screenshot(path='mobile_photo_attached_state.png', full_page=False)
        print("Captured mobile_photo_attached_state.png")

        # 3. Test removing photo
        page.evaluate("removeScalePhoto()")
        page.wait_for_timeout(400)
        page.screenshot(path='mobile_photo_removed_back_to_buttons.png', full_page=False)
        print("Captured mobile_photo_removed_back_to_buttons.png")

        browser.close()

if __name__ == '__main__':
    run()

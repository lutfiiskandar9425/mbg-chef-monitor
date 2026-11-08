# -*- coding: utf-8 -*-
import os
import base64
from playwright.sync_api import sync_playwright

def run():
    # Buat dummy photo file
    sample_png = os.path.abspath('sample_scale_indicator.png')
    # 1x1 transparent png or write small image
    png_data = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9QzwAEjDAGg4EAAO+/Bf80YIidAAAAAElFTkSuQmCC')
    with open(sample_png, 'wb') as f:
        f.write(png_data)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})

        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # 1. Switch to screen-home (Timbang)
        page.evaluate("switchScreen('home')")
        page.wait_for_timeout(500)

        # 2. Upload file via #scale-camera-input
        input_file = page.locator('#scale-camera-input')
        input_file.set_input_files(sample_png)
        page.wait_for_timeout(800)

        # Screenshot Timbang Screen with Photo Attached
        page.screenshot(path='test_timbang_photo_attached.png', full_page=False)
        print("Captured test_timbang_photo_attached.png")

        # 3. View Photo in Modal
        page.evaluate("viewCurrentPhotoModal()")
        page.wait_for_timeout(500)
        page.screenshot(path='test_photo_viewer_modal.png', full_page=False)
        print("Captured test_photo_viewer_modal.png")
        page.evaluate("closePhotoModal()")
        page.wait_for_timeout(300)

        # 4. Add to Staging Cart
        page.evaluate("addToStagingCart()")
        page.wait_for_timeout(800)

        # Screenshot Keranjang with Photo Thumbnail
        page.screenshot(path='test_keranjang_with_photo.png', full_page=False)
        print("Captured test_keranjang_with_photo.png")

        browser.close()

if __name__ == '__main__':
    run()

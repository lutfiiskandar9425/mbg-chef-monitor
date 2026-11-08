# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})

        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # 1. Switch to Timbang (screen-home)
        page.evaluate("switchScreen('home')")
        page.wait_for_timeout(500)

        # Screenshot Timbang Screen with Native Labels & Options
        page.screenshot(path='screen_home_camera_buttons.png', full_page=False)
        print("Captured screen_home_camera_buttons.png")

        # 2. Click Opsi Kamera Live & Uji Coba
        page.evaluate("openCameraOptionsModal()")
        page.wait_for_timeout(400)
        page.screenshot(path='screen_camera_options_modal.png', full_page=False)
        print("Captured screen_camera_options_modal.png")

        # 3. Click "Gunakan Foto Indikator Digital (Cepat)"
        page.evaluate("useDigitalScaleSamplePhoto()")
        page.wait_for_timeout(500)
        page.screenshot(path='screen_scale_photo_preview_active.png', full_page=False)
        print("Captured screen_scale_photo_preview_active.png")

        # 4. View Photo Modal
        page.evaluate("viewCurrentPhotoModal()")
        page.wait_for_timeout(400)
        page.screenshot(path='screen_digital_scale_photo_viewer.png', full_page=False)
        print("Captured screen_digital_scale_photo_viewer.png")
        page.evaluate("closePhotoModal()")
        page.wait_for_timeout(300)

        # 5. Add to Cart
        page.evaluate("addToStagingCart()")
        page.wait_for_timeout(600)
        page.screenshot(path='screen_staging_with_digital_photo.png', full_page=False)
        print("Captured screen_staging_with_digital_photo.png")

        browser.close()

if __name__ == '__main__':
    run()

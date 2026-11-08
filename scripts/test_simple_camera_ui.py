# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 420, 'height': 850}) # Emulate Mobile Phone

        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # 1. Switch to Timbang (screen-home)
        page.evaluate("switchScreen('home')")
        page.wait_for_timeout(500)

        # Capture mobile home with the 2 simple buttons
        page.screenshot(path='mobile_simple_camera_buttons.png', full_page=False)
        print("Captured mobile_simple_camera_buttons.png")

        # 2. Click Foto Digital Cepat
        page.evaluate("useDigitalScaleSamplePhoto()")
        page.wait_for_timeout(500)

        # Capture photo preview state (buttons hidden, preview card active)
        page.screenshot(path='mobile_photo_attached_preview.png', full_page=False)
        print("Captured mobile_photo_attached_preview.png")

        # 3. View Photo Modal
        page.evaluate("viewCurrentPhotoModal()")
        page.wait_for_timeout(400)
        page.screenshot(path='mobile_photo_viewer.png', full_page=False)
        print("Captured mobile_photo_viewer.png")
        page.evaluate("closePhotoModal()")
        page.wait_for_timeout(300)

        # 4. Remove photo to test reverting to 2 buttons
        page.evaluate("removeScalePhoto()")
        page.wait_for_timeout(400)
        page.screenshot(path='mobile_photo_reverted_buttons.png', full_page=False)
        print("Captured mobile_photo_reverted_buttons.png")

        browser.close()

if __name__ == '__main__':
    run()

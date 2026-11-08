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

        page.evaluate("switchScreen('home')")
        page.wait_for_timeout(500)

        # Check if button is clickable
        cam_btn = page.locator('button:has-text("Buka Kamera")')
        print("Camera button visible:", cam_btn.is_visible())
        print("Camera button enabled:", cam_btn.is_enabled())

        gallery_btn = page.locator('button:has-text("Pilih dari Galeri")')
        print("Gallery button visible:", gallery_btn.is_visible())
        print("Gallery button enabled:", gallery_btn.is_enabled())

        # Click camera button
        cam_btn.click()
        page.wait_for_timeout(500)

        browser.close()

if __name__ == '__main__':
    run()

# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 420, 'height': 850}) # Mobile view
        page = context.new_page()

        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # 1. Outsider View (Default state: Locked Out)
        gate = page.locator('#master-security-gate')
        main_app = page.locator('#app-main-content')

        print("Gate visible by default:", gate.is_visible())
        print("Main app visible by default:", main_app.is_visible())
        page.screenshot(path='screen_locked_out.png', full_page=False)
        print("Captured screen_locked_out.png")

        # 2. Try wrong PIN
        page.fill('#master-pin-input', '1234')
        page.click('button:has-text("Buka Akses Master")')
        page.wait_for_timeout(400)
        err = page.locator('#master-auth-error')
        print("Error shown on wrong PIN:", err.is_visible())

        # 3. Enter correct Master PIN (9425)
        page.fill('#master-pin-input', '9425')
        page.click('button:has-text("Buka Akses Master")')
        page.wait_for_timeout(600)

        print("Gate visible after correct PIN:", gate.is_visible())
        print("Main app visible after correct PIN:", main_app.is_visible())
        page.screenshot(path='screen_unlocked.png', full_page=False)
        print("Captured screen_unlocked.png")

        # 4. Click Lock button in header
        page.click('button[title="Kunci sistem dan putus akses sekarang"]')
        page.wait_for_timeout(400)
        print("Gate visible after clicking Lock:", gate.is_visible())
        print("Main app visible after clicking Lock:", main_app.is_visible())

        browser.close()

if __name__ == '__main__':
    run()

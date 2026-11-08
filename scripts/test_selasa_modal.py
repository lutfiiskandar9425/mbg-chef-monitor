# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        
        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(800)

        page.evaluate("selectDay('selasa')")
        page.wait_for_timeout(500)

        page.evaluate("openFullDirectiveModal()")
        page.wait_for_timeout(500)

        # Scroll full-directive-body to 600
        page.evaluate("document.getElementById('full-directive-body').scrollTo(0, 600)")
        page.wait_for_timeout(400)
        page.screenshot(path='selasa_modal_table.png', full_page=False)

        # Scroll full-directive-body to 1200
        page.evaluate("document.getElementById('full-directive-body').scrollTo(0, 1200)")
        page.wait_for_timeout(400)
        page.screenshot(path='selasa_modal_bumbu_deep.png', full_page=False)

        browser.close()

if __name__ == '__main__':
    run()

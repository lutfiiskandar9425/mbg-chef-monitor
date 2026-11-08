# -*- coding: utf-8 -*-
import os
import time
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        
        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # Switch to Tuesday (selasa)
        page.evaluate("selectDay('selasa')")
        page.wait_for_timeout(800)

        # Screenshot Tuesday Main
        page.screenshot(path='selasa_main_view.png', full_page=False)
        print("Captured selasa_main_view.png")

        # Click bumbu subtab
        page.evaluate("selectDirectiveSubtab('bumbu')")
        page.wait_for_timeout(500)
        page.screenshot(path='selasa_bumbu_subtab.png', full_page=False)
        print("Captured selasa_bumbu_subtab.png")

        # Open Full Directive Modal
        page.evaluate("openFullDirectiveModal()")
        page.wait_for_timeout(600)
        page.screenshot(path='selasa_modal_top.png', full_page=False)
        print("Captured selasa_modal_top.png")

        # Scroll modal to table & bumbu section
        page.evaluate("document.getElementById('full-directive-modal').scrollTo(0, 750)")
        page.wait_for_timeout(500)
        page.screenshot(path='selasa_modal_table_bumbu.png', full_page=False)
        print("Captured selasa_modal_table_bumbu.png")

        browser.close()

if __name__ == '__main__':
    run()

# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

def run():
    errors = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 900})
        
        # Listen for console errors
        page.on('console', lambda msg: errors.append(f"CONSOLE {msg.type}: {msg.text}") if msg.type == 'error' else None)
        page.on('pageerror', lambda err: errors.append(f"PAGEERROR: {str(err)}"))

        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # 1. Test Day Switchers
        for d in ['senin', 'selasa', 'rabu', 'kamis', 'jumat']:
            page.evaluate(f"selectDay('{d}')")
            page.wait_for_timeout(200)

        # 2. Test Station Switchers
        for st in ['persiapan', 'pengolahan', 'pemorsian']:
            page.evaluate(f"selectStationDirective('{st}')")
            page.wait_for_timeout(200)

        # 3. Test Subtabs
        for s in ['aturan', 'bumbu', 'pos', 'jadwal', 'higiene']:
            page.evaluate(f"selectDirectiveSubtab('{s}')")
            page.wait_for_timeout(200)

        # 4. Test Screens
        for scr in ['aslap', 'home', 'staging', 'stock', 'menu']:
            page.evaluate(f"switchScreen('{scr}')")
            page.wait_for_timeout(300)

        # 5. Test ASLAP Print Modal
        page.evaluate("openPrintModal()")
        page.wait_for_timeout(300)
        page.evaluate("closePrintModal()")

        # 6. Test Full Directive Modal
        page.evaluate("openFullDirectiveModal()")
        page.wait_for_timeout(300)
        page.evaluate("closeFullDirectiveModal()")

        # 7. Test Tare Presets
        page.evaluate("switchScreen('home')")
        for tare in [0.85, 0.50, 0.00]:
            page.evaluate(f"setTare({tare})")
            page.wait_for_timeout(100)

        # 8. Test triggerCameraOCR
        page.evaluate("triggerCameraOCR()")
        page.wait_for_timeout(800)

        # 9. Test addToStagingCart
        page.evaluate("addToStagingCart()")
        page.wait_for_timeout(500)

        # 10. Test Staging Edit Modal
        page.evaluate("switchScreen('staging')")
        page.wait_for_timeout(300)
        page.evaluate("openEditModal(stagingItems[0].id)")
        page.wait_for_timeout(300)
        page.evaluate("closeEditModal()")

        # 11. Test Sync
        page.evaluate("syncAllToGoogleSheets()")
        page.wait_for_timeout(1500)

        # 12. Test Refresh
        page.evaluate("forceRefreshApp()")
        page.wait_for_timeout(800)

        browser.close()

    print(f"Total Errors Captured: {len(errors)}")
    for e in errors:
        print(e)

if __name__ == '__main__':
    run()

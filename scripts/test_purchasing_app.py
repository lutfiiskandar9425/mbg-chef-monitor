# -*- coding: utf-8 -*-
import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Desktop view
        page = browser.new_page(viewport={'width': 1280, 'height': 900})

        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # 1. Screenshot Stage 1: PR
        page.screenshot(path='purchasing_stage1_pr.png', full_page=False)
        print("Captured purchasing_stage1_pr.png")

        # 2. Screenshot Stage 2: RFQ Matrix
        page.evaluate("switchStage('rfq')")
        page.wait_for_timeout(500)
        page.screenshot(path='purchasing_stage2_rfq.png', full_page=False)
        print("Captured purchasing_stage2_rfq.png")

        # 3. Screenshot Stage 3: Negosiasi & Terms
        page.evaluate("switchStage('nego')")
        page.wait_for_timeout(500)
        page.screenshot(path='purchasing_stage3_nego.png', full_page=False)
        print("Captured purchasing_stage3_nego.png")

        # 4. Screenshot Stage 4: PO Table & Official Print Modal
        page.evaluate("switchStage('po')")
        page.wait_for_timeout(500)
        page.screenshot(path='purchasing_stage4_po_table.png', full_page=False)
        print("Captured purchasing_stage4_po_table.png")

        # Open PO Modal
        page.evaluate("previewOfficialPO('PO/WSI/2026/11/008')")
        page.wait_for_timeout(500)
        page.screenshot(path='purchasing_stage4_po_official_doc.png', full_page=False)
        print("Captured purchasing_stage4_po_official_doc.png")
        page.evaluate("closePOModal()")
        page.wait_for_timeout(300)

        # 5. Screenshot Stage 5: Tracking
        page.evaluate("switchStage('tracking')")
        page.wait_for_timeout(500)
        page.screenshot(path='purchasing_stage5_tracking.png', full_page=False)
        print("Captured purchasing_stage5_tracking.png")

        # 6. Screenshot Stage 6: Goods Receipt (GR)
        page.evaluate("switchStage('gr')")
        page.wait_for_timeout(500)
        page.screenshot(path='purchasing_stage6_gr.png', full_page=False)
        print("Captured purchasing_stage6_gr.png")

        # 7. Screenshot Stage 7: 3-Way Matching
        page.evaluate("switchStage('matching')")
        page.wait_for_timeout(500)
        page.screenshot(path='purchasing_stage7_matching.png', full_page=False)
        print("Captured purchasing_stage7_matching.png")

        # 8. Mobile View Test
        page.set_viewport_size({'width': 420, 'height': 850})
        page.evaluate("switchStage('pr')")
        page.wait_for_timeout(500)
        page.screenshot(path='purchasing_mobile_view.png', full_page=False)
        print("Captured purchasing_mobile_view.png")

        browser.close()

if __name__ == '__main__':
    run()

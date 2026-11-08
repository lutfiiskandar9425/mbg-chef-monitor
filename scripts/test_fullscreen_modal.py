import asyncio
import os
from playwright.async_api import async_playwright

async def test_fullscreen_modal():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 412, "height": 915})
        file_url = "file:///" + os.path.abspath("preview.html").replace("\\", "/")
        print(f"Loading {file_url}...")
        await page.goto(file_url, wait_until="networkidle")

        # 1. Check Fullscreen button
        btn = await page.query_selector("button:has-text('Layar Penuh')")
        print("Layar Penuh button found:", btn is not None)
        if btn:
            await btn.click()
            await page.wait_for_timeout(400)
            
            modal = await page.query_selector("#full-directive-modal")
            is_visible = await modal.is_visible()
            print("Full directive modal visible:", is_visible)
            
            # Screenshot of the fullscreen reader
            shot1 = "C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/fullscreen_reader_top.png"
            await page.screenshot(path=shot1)
            print("Saved top screenshot to", shot1)

            # Scroll inside the modal body
            body = await page.query_selector("#full-directive-body")
            if body:
                await body.evaluate("el => el.scrollBy(0, 600)")
                await page.wait_for_timeout(300)
                shot2 = "C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/fullscreen_reader_middle.png"
                await page.screenshot(path=shot2)
                print("Saved middle screenshot to", shot2)

            # Close modal
            close_btn = await page.query_selector("button:has-text('✕')")
            if close_btn:
                await close_btn.click()
                await page.wait_for_timeout(300)
                is_closed = not await modal.is_visible()
                print("Modal closed successfully:", is_closed)

        # 2. Check the new responsive batch card layout
        batch_elem = await page.query_selector("#school-batch-section")
        if batch_elem:
            await batch_elem.scroll_into_view_if_needed()
            await page.wait_for_timeout(300)
            shot3 = "C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/responsive_batch_cards.png"
            await page.screenshot(path=shot3)
            print("Saved batch cards screenshot to", shot3)

        await browser.close()
        print("Test completed successfully!")

asyncio.run(test_fullscreen_modal())


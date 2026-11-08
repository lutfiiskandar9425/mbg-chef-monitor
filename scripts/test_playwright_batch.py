import asyncio
import os
from playwright.async_api import async_playwright

async def test_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 412, "height": 915}) # Mobile viewport
        
        errors = []
        page.on("pageerror", lambda err: errors.append(err.message))
        page.on("console", lambda msg: print(f"[CONSOLE {msg.type}] {msg.text}") if msg.type in ['error', 'warn'] else None)

        file_url = "file:///" + os.path.abspath("preview.html").replace("\\", "/")
        print(f"Loading {file_url}...")
        await page.goto(file_url, wait_until="networkidle")
        
        # Verify elements
        sticky = await page.query_selector("#sticky-chef-note")
        print("Sticky note found:", sticky is not None)
        
        school_batch = await page.query_selector("#school-batch-section")
        print("School batch section found:", school_batch is not None)
        
        batch_text = await school_batch.inner_text()
        print("Batch text preview:\n", batch_text[:300])
        
        # Take screenshot of home screen
        screenshot_path = os.path.abspath("preview_batch_home.png")
        await page.screenshot(path=screenshot_path)
        print("Saved screenshot to", screenshot_path)

        # Test clicking SMK 1
        smk_btn = await page.query_selector("button:has-text('SMK 1 Kedungwuni')")
        if smk_btn:
            await smk_btn.click()
            await page.wait_for_timeout(300)
            smk_text = await school_batch.inner_text()
            print("\nSMK 1 Text Preview:\n", smk_text[:300])
            
            # Click print button
            print_btn = await page.query_selector("button:has-text('Cetak Lembar Kerja A4')")
            if print_btn:
                await print_btn.click()
                await page.wait_for_timeout(500)
                modal = await page.query_selector("#print-school-modal")
                is_visible = await modal.is_visible()
                print("School print modal visible:", is_visible)
                
                modal_screenshot = os.path.abspath("preview_batch_print_modal.png")
                await page.screenshot(path=modal_screenshot)
                print("Saved print modal screenshot to", modal_screenshot)

        print("\nTotal errors:", len(errors))
        if errors:
            print("Errors found:", errors)
        else:
            print("Zero errors detected! UI works flawlessly!")

        await browser.close()

asyncio.run(test_page())


import asyncio
import os
from playwright.async_api import async_playwright

async def take_scrolled_screenshot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 412, "height": 915})
        file_url = "file:///" + os.path.abspath("preview.html").replace("\\", "/")
        await page.goto(file_url, wait_until="networkidle")
        
        # Scroll down to school batch section
        element = await page.query_selector("#school-batch-section")
        if element:
            await element.scroll_into_view_if_needed()
            await page.wait_for_timeout(300)
            path = "C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/preview_scrolled_batch.png"
            await page.screenshot(path=path)
            print("Saved scrolled screenshot to", path)
            
        await browser.close()

asyncio.run(take_scrolled_screenshot())


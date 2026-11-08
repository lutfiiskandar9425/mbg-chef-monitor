import asyncio
import os
from playwright.async_api import async_playwright

async def snap_refresh_ui():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 412, 'height': 915})
        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        await page.goto(file_url, wait_until='networkidle')

        # Check buttons
        hdr_btn = await page.query_selector("#header-refresh-btn")
        float_btn = await page.query_selector("#floating-refresh-btn")
        print("Header refresh button found:", hdr_btn is not None)
        print("Floating refresh button found:", float_btn is not None)

        shot_path = "C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/refresh_buttons_ui.png"
        await page.screenshot(path=shot_path)
        print("Saved refresh UI screenshot to", shot_path)
        await browser.close()

asyncio.run(snap_refresh_ui())


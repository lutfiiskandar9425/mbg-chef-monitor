import asyncio
import os
from playwright.async_api import async_playwright

async def snap_cards():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 412, 'height': 915})
        file_url = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        await page.goto(file_url, wait_until='networkidle')
        elem = await page.query_selector('#school-batch-section')
        if elem:
            await elem.scroll_into_view_if_needed()
            await page.wait_for_timeout(300)
            await page.screenshot(path='C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/responsive_batch_cards.png')
            print('Snapped cards screenshot!')
        await browser.close()

asyncio.run(snap_cards())


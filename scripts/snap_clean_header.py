# -*- coding: utf-8 -*-
import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 390, 'height': 844},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True
        )
        page = await context.new_page()
        file_path = 'file:///' + os.path.abspath('preview.html').replace('\\', '/')
        await page.goto(file_path)
        await page.wait_for_timeout(1000)
        
        await page.screenshot(path='clean_header_ui.png')
        print("Captured clean_header_ui.png")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

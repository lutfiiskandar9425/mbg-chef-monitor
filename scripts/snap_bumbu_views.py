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
        
        # 1. Click Bumbu & Resep subtab and scroll down to the sticky note content
        await page.click('#subtab-btn-bumbu')
        await page.wait_for_timeout(300)
        await page.evaluate("window.scrollTo(0, 550)")
        await page.wait_for_timeout(500)
        await page.screenshot(path='culinary_sticky_bumbu_visible.png')
        print("Captured culinary_sticky_bumbu_visible.png")
        
        # 2. Scroll a bit more to see the rest of bumbu items in sticky note
        await page.evaluate("window.scrollTo(0, 950)")
        await page.wait_for_timeout(500)
        await page.screenshot(path='culinary_sticky_bumbu_part2.png')
        print("Captured culinary_sticky_bumbu_part2.png")
        
        # 3. Open Fullscreen modal and scroll directly to Section 3 (Bumbu)
        await page.click('button[onclick="openFullDirectiveModal()"]')
        await page.wait_for_timeout(500)
        await page.evaluate("document.getElementById('full-directive-body').scrollTop = 1100")
        await page.wait_for_timeout(500)
        await page.screenshot(path='culinary_fullscreen_bumbu_section.png')
        print("Captured culinary_fullscreen_bumbu_section.png")
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())

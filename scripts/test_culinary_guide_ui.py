# -*- coding: utf-8 -*-
import os
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Mobile viewport iPhone 14 / modern smartphone
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
        
        # 1. Take screenshot of home page with subtabs
        await page.screenshot(path='culinary_home_subtabs.png')
        print("Captured culinary_home_subtabs.png")
        
        # 2. Click "Bumbu & Resep" subtab button
        bumbu_btn = page.locator('#subtab-btn-bumbu')
        await bumbu_btn.click()
        await page.wait_for_timeout(500)
        await page.screenshot(path='culinary_bumbu_subtab_active.png')
        print("Captured culinary_bumbu_subtab_active.png")
        
        # 3. Click "Layar Penuh" button to open fullscreen directive modal
        fullscreen_btn = page.locator('button[onclick="openFullDirectiveModal()"]')
        await fullscreen_btn.click()
        await page.wait_for_timeout(500)
        
        # Modal is open, scroll down to Section 3: Bumbu
        modal_body = page.locator('#full-directive-body')
        await page.screenshot(path='culinary_fullscreen_top.png')
        print("Captured culinary_fullscreen_top.png")
        
        # Scroll modal to Section 3 (Bumbu & Resep)
        await page.evaluate("document.getElementById('full-directive-body').scrollTop = 700")
        await page.wait_for_timeout(500)
        await page.screenshot(path='culinary_fullscreen_bumbu.png')
        print("Captured culinary_fullscreen_bumbu.png")
        
        await browser.close()
        print("All screenshots taken successfully!")

if __name__ == '__main__':
    asyncio.run(main())


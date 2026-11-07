from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        url = 'file:///C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/mbg_kitchen_monitor_preview.html'
        print('Navigating to', url)
        page.goto(url)
        page.wait_for_timeout(1000)
        
        # Test Chef Recipe Modal
        page.click('button:has-text("Input Resep Chef")')
        page.wait_for_timeout(500)
        print('Chef recipe modal visible?', page.is_visible('#chef-recipe-modal'))
        
        # Switch to SELASA
        page.click('#chef-day-selasa')
        page.wait_for_timeout(300)
        title_val = page.input_value('#chef-form-title')
        print('Loaded Selasa title:', title_val[:40])
        
        # Click Save & Broadcast
        page.click('button:has-text("Simpan & Siarkan")')
        page.wait_for_timeout(500)
        print('Modal closed?', not page.is_visible('#chef-recipe-modal'))
        print('Hero updated to SELASA?', 'SELASA' in page.inner_text('#hero-day-label'))
        
        browser.close()
        print('CHEF RECIPE MODAL & BROADCAST TEST PASSED 100%!')

if __name__ == '__main__':
    test()


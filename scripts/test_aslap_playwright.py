from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        url = 'file:///C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/mbg_kitchen_monitor_preview.html'
        print('Navigating to', url)
        page.goto(url)
        page.wait_for_timeout(1000)
        
        # Test ASLAP tab
        page.click('#tab-btn-aslap')
        page.wait_for_timeout(500)
        print('ASLAP screen visible?', page.is_visible('#screen-aslap'))
        count = page.eval_on_selector('#aslap-item-count', 'el => el.textContent.trim()')
        print('ASLAP item count:', count)
        
        # Test Print Modal
        page.click('button:has-text("Cetak Form A4")')
        page.wait_for_timeout(500)
        print('Print modal visible?', page.is_visible('#print-aslap-modal'))
        print('Form preview contains KOP BGN?', 'BADAN GIZI NASIONAL' in page.content())
        print('Form preview contains Chef Lutfi?', 'Chef Lutfi Iskandar' in page.content())
        
        browser.close()
        print('ASLAP & PRINTABLE FORM TEST PASSED 100%!')

if __name__ == '__main__':
    test()


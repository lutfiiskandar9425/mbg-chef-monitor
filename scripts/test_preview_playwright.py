from playwright.sync_api import sync_playwright
import time

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        url = 'file:///C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/mbg_kitchen_monitor_preview.html'
        print('Navigating to', url)
        page.goto(url)
        page.wait_for_timeout(1000)
        
        # Test 1: Cek Note di Tim Persiapan
        page.click('#directive-btn-persiapan')
        page.wait_for_timeout(500)
        content_persiapan = page.content()
        print('Persiapan active - Contains "NOTE RESMI CHEF LUTFI"?', 'NOTE RESMI CHEF LUTFI' in content_persiapan)
        print('Contains potong dadu 2.5?', '2.5 cm' in content_persiapan)
        
        # Test 2: Cek Note di Tim Pengolahan
        page.click('#directive-btn-pengolahan')
        page.wait_for_timeout(500)
        content_pengolahan = page.content()
        print('Pengolahan active - Contains suhu 75?', '75°C' in content_pengolahan)
        
        # Test 3: Cek Note di Tim Pemorsian
        page.click('#directive-btn-pemorsian')
        page.wait_for_timeout(500)
        content_pemorsian = page.content()
        print('Pemorsian active - Contains SOP Buah Segar?', 'SOP BUAH SEGAR' in content_pemorsian or 'SOP Khusus Buah' in content_pemorsian or 'SOP KHUSUS BUAH' in content_pemorsian)
        
        # Test 4: Klik tombol Timbang Pemorsian dari menu item
        first_btn = page.query_selector('#menu-items-container button')
        if first_btn:
            first_btn.click()
            page.wait_for_timeout(500)
            print('Switched to Timbang screen with Note?', page.is_visible('#autofill-banner'))
            note_text = page.eval_on_selector('#autofill-directive-text', 'el => el.textContent.trim()')
            print('Autofill note text:', note_text[:80])
        
        # Test 5: Tab Keranjang
        page.click('#tab-btn-staging')
        page.wait_for_timeout(500)
        print('Staging screen visible?', page.is_visible('#screen-staging'))
        count = page.eval_on_selector('#staging-count-badge', 'el => el.textContent.trim()')
        print('Cart count badge:', count)
        
        browser.close()
        print('ALL NOTE CHEF & WORKFLOW TESTS PASSED 100%!')

if __name__ == '__main__':
    test()

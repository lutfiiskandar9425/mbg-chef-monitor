from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        url = 'file:///C:/Users/HP/.gemini/antigravity/brain/9c1ce148-7426-4dba-b2a3-bd7207cd3b11/mbg_kitchen_monitor_preview.html'
        print('Navigating to', url)
        page.goto(url)
        page.wait_for_timeout(1000)
        
        # 1. Verify Cycle 1 Senin Menu
        hero_title = page.inner_text('#hero-menu-title')
        print('Senin Siklus 1 title:', hero_title)
        assert 'Telur Rollade' in hero_title, 'Expected Telur Rollade in Senin Siklus 1'

        # 2. Switch to Siklus 2
        page.click('#cycle-btn-2')
        page.wait_for_timeout(500)
        hero_title_c2 = page.inner_text('#hero-menu-title')
        print('Senin Siklus 2 title:', hero_title_c2)
        assert 'Lele Crispy' in hero_title_c2, 'Expected Lele Crispy in Senin Siklus 2'

        # 3. Switch to Rabu Siklus 2
        page.click('button[data-day="rabu"]')
        page.wait_for_timeout(300)
        rabu_title = page.inner_text('#hero-menu-title')
        print('Rabu Siklus 2 title:', rabu_title)
        assert 'Ayam Bumbu Hitam' in rabu_title, 'Expected Ayam Bumbu Hitam in Rabu Siklus 2'

        # 4. Test Team Switcher
        page.click('#directive-btn-pengolahan')
        page.wait_for_timeout(300)
        note_title = page.inner_text('#note-team-title')
        print('Active Note Title:', note_title)
        assert 'TIM PENGOLAHAN' in note_title, 'Expected TIM PENGOLAHAN in note'

        # 5. Test ASLAP tab
        page.click('#tab-btn-aslap')
        page.wait_for_timeout(300)
        assert page.is_visible('#screen-aslap'), 'ASLAP screen should be visible'
        print('ASLAP screen active!')

        # 6. Test Print Modal
        page.click('button:has-text("Cetak A4")')
        page.wait_for_timeout(400)
        assert page.is_visible('#print-aslap-modal'), 'Print modal should be visible'
        page.click('#print-aslap-modal button[onclick="closePrintModal()"]')
        page.wait_for_timeout(300)

        # 7. Test Chef Recipe Modal
        page.click('button:has-text("Input Resep Chef")')
        page.wait_for_timeout(400)
        assert page.is_visible('#chef-recipe-modal'), 'Chef recipe modal should be visible'
        page.click('button:has-text("Batal")')
        page.wait_for_timeout(300)

        browser.close()
        print('SEMUA FITUR SIKLUS 1 & 2 SERTA ASLAP TERVERIFIKASI 100% SUKSES!')

if __name__ == '__main__':
    test()

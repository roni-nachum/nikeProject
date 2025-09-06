


class TestEbayEnhanced():

    def test_ebay_navigation(self,setup_playwright):
        print('into navigation test')
        page = setup_playwright
        page.goto('https://www.ebay.com/')
        assert page.url == 'https://www.ebay.com/' , 'Page URL is not as expected'


    def test_ebay_adv(self, setup_playwright):
        page = setup_playwright
        page.goto('https://www.ebay.com/')
        adv_button = page.get_by_role("link", name="Advanced")
        adv_button.click()
        assert page.url == "https://www.ebay.com/sch/ebayadvsearch", "page URL is not as expected after clik on Adv. button"

    # def test_demo(self,setup_playwright):
    #     print('into test')
    #     page = setup_playwright
    #     setup_playwright('http://www.ebay.com/')
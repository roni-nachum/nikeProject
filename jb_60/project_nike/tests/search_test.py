
from jb_60.project_nike.pages.product_page import productPage

class TestSearch():
    def test_first_product(self, setup_nike):
        print('dunk test')
        page = setup_nike
        product_page = productPage(page)
        search = page.locator("[id= 'gn-search-input']")
        search.click()
        search.clear()
        search.fill("dunk")
        search.press("Enter")
        value = product_page.get_product_amount()
        assert value > 1, 'the value is less than 1'
        print(f'found {value} Dunks')



    def test_second_product(self, setup_nike):
        print('socks test')
        page = setup_nike
        product_page = productPage(page)
        search = page.locator("[id= 'gn-search-input']")
        search.click()
        search.clear()
        search.fill("socks")
        search.press("Enter")
        value = product_page.get_product_amount()
        assert value > 1, 'the value is less than 1'
        print(f'found {value} socks')

    def test_third_product(self, setup_nike):
        print('bag test')
        page = setup_nike
        product_page = productPage(page)
        search = page.locator("[id= 'gn-search-input']")
        search.click()
        search.clear()
        search.fill("bag")
        search.press("Enter")
        value = product_page.get_product_amount()
        assert value > 1, 'the value is less than 1'
        print(f'found {value} bags')






from jb_60.project_nike.pages.search_page import searchPage


class TestCategory():

    def test_women_category(self,setup_nike):
        print('Women category')
        page = setup_nike
        search_page = searchPage(page)
        search = page.locator("[href='https://www.nike.com/il/women']")
        search.click()
        sale_page = page.locator("[href='https://www.nike.com/il/w/womens-sale-3yaepz5e1x6']")
        sale_page.click()
        value = search_page.get_amount()
        assert value > 1, 'the value is less than 1'
        print(f'found {value} items on sale')


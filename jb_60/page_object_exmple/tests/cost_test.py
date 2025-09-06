from jb_60.page_object_exmple.pages.home_page import homePage
from jb_60.page_object_exmple.pages.product_page import productPage


class TestCost():
    def test_first_product(self,setup_swaglabs):
        print('Test Start')
        page = setup_swaglabs
        home_page = homePage(page)
        product_page = productPage(page)

        home_page.set_user_and_password("standard_user", "secret_sauce")
        home_page.click_on_login_button()
        price = product_page.get_first_price()
        assert  price<50.0, 'Price of first Prod. is more than 50$'

    def test_dropdown_example(self, setup_swaglabs):
        print("Test Start")
        page = setup_swaglabs
        home_page = homePage(page)
        product_page = productPage(page)
        home_page.set_user_and_password("standard_user", "secret_sauce")
        home_page.click_on_login_button()
        product_page.sort_by_drop_down()

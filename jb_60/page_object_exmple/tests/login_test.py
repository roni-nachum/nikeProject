
from jb_60.page_object_exmple.pages.home_page import homePage
from jb_60.page_object_exmple.pages.product_page import productPage

class TestSwagLab():

    def test_correct_login(self,setup_swaglabs):
        print('Test Start')
        page = setup_swaglabs
        home_page = homePage(page)
        product_page = productPage(page)

        home_page.set_user_and_password("standard_user", "secret_sauce")
        home_page.click_on_login_button()
        product_page.get_first_price()
        assert page.url == 'https://www.saucedemo.com/inventory.html', "Page URL is not as expected after login "

    def test_invalid_user(self,setup_swaglabs):
        print('Test Start')
        page = setup_swaglabs
        home_page = homePage(page)
        product_page = productPage(page)

        home_page.set_user_and_password("fake_user", "fake_password")
        home_page.click_on_login_button()
        product_page.get_first_price()
        assert page.url == 'https://www.saucedemo.com/inventory.html', "Page URL is not as expected after login "




class cartPage():
    def __init__(self, page):
        print("Into ProductPage init")
        self.page = page

    def get_cart(self):
        cart_page = self.page.query_selector_all("[class='css-79q9fn']")

    def get_bag_button(self):
        bag_bottun = self.page.query_selector_all("[class='nds-btn mb3-sm css-dnr0el btn-primary-dark  btn-lg']")

    def get_size(self, size):
        size_button = self.page.query_selector(f"test='size'")
        if size_button:
            size_button.click()
        else:
            raise Exception(f"Size {size} not available")




class searchPage():

    def __init__(self, page):
        print("Into SearchPage init")
        self.page = page

    def get_first_product(self):
        print('getting the first price of product')
        search = self.page.locator("[id='gn-search-input']")

    def get_amount(self):
        result_element = self.page.locator("[class='wall-header__item_count']")
        result_text = result_element.text_content()
        result_text = result_text.replace("(", "")
        result_text = result_text.replace(")", "")
        value = int(result_text)
        return value





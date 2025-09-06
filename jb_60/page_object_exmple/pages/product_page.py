from jb_60.playwrite_example.find_elements_example import text_as_float


class productPage():

    def __init__(self,page):
      print('into init')
      self.page = page


    def get_first_price(self):
        print('getting the first price of product')
        products = self.page.query_selector_all("[class='inventory_item_price']")
        product_1 = products[0]
        text = product_1.text_content()
        print(f"text found {text}")
        text = text.replace("$", '')
        text_as_float = float(text)
        return text_as_float

    def sort_by_drop_down(self):
        sort_menu = self.page.locator("[class='product_sort_container']")
        # sort_menu.select_option("Harry Potter")
        sort_menu.select_option(index=1)
        sort_menu.select_option("Name (Z to A)")







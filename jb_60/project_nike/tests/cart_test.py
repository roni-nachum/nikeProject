from jb_60.project_nike.pages import cart_page
from jb_60.project_nike.pages.cart_page import cartPage
from jb_60.project_nike.pages.product_page import productPage


class TestProduct():
    def test_add_dunk(self, setup_nike):
        print('Dunk added to the cart')
        page = setup_nike

        # --- Your search logic (looks good) ---
        search = page.locator("#gn-search-input")
        search.click()
        search.clear()
        search.fill("dunk")
        search.press("Enter")

        dunk = page.wait_for_selector("a[aria-label='Nike Dunk Low Next Nature']")
        dunk.click()


        available_size = page.locator('div[data-testid="pdp-grid-selector-item"]:not(.disabled)').first

        available_size.locator('label').click()

        add_to_bag_button = page.locator('button[data-testid="add-to-cart-button"]')
        add_to_bag_button.click()

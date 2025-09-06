from playwright.sync_api import sync_playwright, Page

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    user = page.locator("[id='user-name']")
    password = page.locator("[name='password']")
    password_by_id = page.locator("[id='password']")
    login_button = page.locator("[id='login-button']")
    user.click()
    user.click()
    user.clear()
    # user.fill("standard_user")

    user.type("standard_user")
    password.click()
    password.clear()
    password.fill("secret_sauce")
    password.fill("secret_sauce")

    login_button.click()
  # example how to get elements from the same locator
    products = page.query_selector_all("[class='inventory_item_price']")
    product_3 = products[2]
    product_4 = products[3]
    product_4.text_content()
    assert len(products) >5, 'lass than 5 product found'
    for product in products:
    #example how to read the text of element
        text = product.text_content()
        print(f"text found {text}")
        text = text.replace("$",'')

        text_as_float=float(text)
        assert text_as_float <50.00, 'The price is more than 50$ not as expected'



    page.close()
    print("Test End")




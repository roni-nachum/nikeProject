from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/loginmak")
    button =page.get_by_text("Customer Login")

    button.click()
    user_menu = page.locator('[id="userSelect"]')
    user_menu.select_option(index=2)
    user_menu.select_option(value="Harry Potter")

    page.close()
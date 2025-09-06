from datetime import time


class StorePage:

    @staticmethod
    def count_store_in_location(page, country):
        find_button = page.locator("[href ='https://www.nike.com/il/retail']")
        find_button.click()
        find = page.locator("[id='ta-Location_input']")
        find.click()
        find.clear()
        find.type(country, delay=1500)  # mimics human typing
        page.keyboard.press("Enter")
        result_element = page.wait_for_selector("[class= 'd-sm-flx flx-ai-sm-c text-color-secondary body-3 flex-child mr2-sm']")
        result_text = result_element.text_content().strip()
        result_text = result_text.replace(" Stores Near You","")
        value = int(result_text)
        return value

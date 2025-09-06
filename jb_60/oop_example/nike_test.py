import time


class TestNike():

    def test_navagation(self,setup_playwright):
        page = setup_playwright
        page.goto('https://www.nike.com/il')
        url = page.url
        assert url=='https://www.nike.com/il' , 'Test URL is not expected'


    def test_find_store(self,setup_playwright):
        page = setup_playwright
        page.goto('https://www.nike.com/il')
        find_button = page.locator("[href = 'https://www.nike.com/il/retail']")
        find_button.click()
        find = page.locator("[id='ta-Location_input']")
        find.click()
        find.clear()
        find.fill('Jerusalem')
        time.sleep(3) #adding delay due a slow response of searching
        page.keyboard.press('ENTER')
        time.sleep(5)
        result_element = page.locator("[class= 'd-sm-flx flx-ai-sm-c text-color-secondary body-3 flex-child mr2-sm-w']")
        result_text = result_element.text_content()
        index = result_text.index(' ')
        result_text = result_text[0:index]
        value = int(result_text)
        assert value>1, 'the value is less than 1'
        print(f'{result_text}')
        print('test end')
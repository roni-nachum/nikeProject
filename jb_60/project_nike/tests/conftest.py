import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture

def setup_nike():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.nike.com/il/")

        yield page
        page.close()
        browser.close()
        print('test end')

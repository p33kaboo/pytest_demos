import time
from selenium.webdriver.common.by import By


class TestLang:
    def test_star_check(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        browser.implicitly_wait(5)
        check_btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
        assert check_btn, 'not found button!'

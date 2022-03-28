from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestLang:
    # def test_star_check(self, browser):
    #     browser.get('http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer ')
    #     browser.implicitly_wait(5)
    #     check_btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    #     assert check_btn, 'not found button!'

    def test_guest_can_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_should_see_login_form(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()

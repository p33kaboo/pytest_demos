import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators


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

    @pytest.mark.new
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.open_card()
        # ниже лютый костыль
        basket_page = BasketPage(page.browser)
        assert basket_page.is_basket_empty(*BasketPageLocators.BASKET_FORMSET)
        basket_page.is_basket_empty_message()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
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
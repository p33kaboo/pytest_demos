import time
from itertools import product

import pytest

from pages.locators import ProductPageLocators

from pages.product_page import ProductPage


class TestProductPage:
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo"
                                           "=offer7", marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def st_test_guest_can_add_product_to_basket(self, browser, link):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
        page = ProductPage(browser=browser, url=link)

        page.go_to_product_page()
        page.add_product_to_card()
        page.solve_quiz_and_get_code()
        product_name = page.get_product_name()

        assert page.is_element_present(*ProductPageLocators.ITEM_ADDED_ALERT)
        product_name_in_alert = page.get_item_name_in_alert()

        assert page.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_CARD)
        item_price_in_card = page.get_item_price_in_card()
        price_in_page = page.get_price_in_page()

        page.open_card()
        card_item = page.get_card_items()

        assert product_name in card_item, 'product not in card'
        assert product_name == product_name_in_alert, 'no alert about added item in card'
        assert price_in_page == item_price_in_card, f'price in page {price_in_page} and in card {item_price_in_card} is different'


    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser=browser, url=link)
        page.open()

        page.add_product_to_card()
        page.solve_quiz_and_get_code()

        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def test_guest_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser=browser, url=link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
        page = ProductPage(browser=browser, url=link)
        page.open()

        page.add_product_to_card()
        page.solve_quiz_and_get_code()

        assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
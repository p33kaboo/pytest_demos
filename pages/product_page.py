from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def go_to_product_page(self):
        self.browser.get(self.url)

    def add_product_to_card(self):
        add_to_card_btn = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_CARD_BTN)
        add_to_card_btn.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_card_items(self):
        all_card_items = self.browser.find_elements(*ProductPageLocators.CARD_ITEMS)
        assert all_card_items, 'Error not elements found'
        card_items = []
        for item in all_card_items:
            card_items.append(item.text)
        return card_items

    def get_item_price_in_card(self):
        price_in_card = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CARD)
        assert price_in_card
        return price_in_card.text

    def get_price_in_page(self):
        price_in_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_PAGE)
        assert price_in_page
        return price_in_page.text

    def get_item_name_in_alert(self):
        item_name_in_alert = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_ALERT)
        assert item_name_in_alert, f'error, not found! {item_name_in_alert}'
        return item_name_in_alert.text

    def should_not_be_success_message(self):
        """
        Проверка наличии элемента
        :return:
        """
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_delete_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


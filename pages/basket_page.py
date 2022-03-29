from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasketPageLocators

class BasketPage:
    def __init__(self, browser):
        self.browser = browser

    def is_basket_empty(self, how, what, timeout=4):
        """
        Проверяет не появился ли элемент в течении заданного времени timeout
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_basket_empty_message(self):
        empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT)
        assert 'Ваша корзина пуста' in empty_text.text, 'Is not empty'

    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяет исчезает ли элемент за заданный период timeout
        :param how:
        :param what:
        :param timeout:
        :return:
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
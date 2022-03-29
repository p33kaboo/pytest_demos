from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


class ProductPageLocators:
    ITEM_ADDED_ALERT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRODUCT_PRICE_IN_PAGE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > '
                                              'p.price_color')
    PRODUCT_PRICE_IN_CARD = (By.CSS_SELECTOR, '#messages > .alert.alert-safe.alert-noicon.alert-info.fade.in > '
                                              'div.alertinner > p > strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_ADD_TO_CARD_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CARD_BTN = (By.CSS_SELECTOR, '.btn-group > .btn.btn-default')
    CARD_ITEMS = (By.CSS_SELECTOR, '#basket_formset > div > div > div.col-sm-4 > h3 > a')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-success.fade.in > '
                                        '.alertinner')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
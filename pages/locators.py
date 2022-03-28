from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
from .base_page import BasePage
from .locators import LoginPageLocators, RegistrationFormLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_page = self.browser.get(LoginPageLocators.LOGIN_URL)
        assert 'login' in self.browser.current_url, f'Current url {self.browser.current_url} does not have "login"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Error! Login form not found'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Error! Register form not found'

    def open_login_page(self):
        self.browser.get(self.url)

    def register_new_user(self, email, password):
        login_form = self.browser.find_element(*RegistrationFormLocators.REGISTERATION_FORM)
        assert login_form
        pswd_form1 = self.browser.find_element(*RegistrationFormLocators.REGISTRATION_PASSWORD1)
        pswd_form2 = self.browser.find_element(*RegistrationFormLocators.REGISTRATION_PASSWORD2)
        registration_btn = self.browser.find_element(*RegistrationFormLocators.REGISTRATION_BTN)

        login_form.send_keys(email)
        pswd_form1.send_keys(password)
        pswd_form2.send_keys(password)
        registration_btn.click()

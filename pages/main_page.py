from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators, LoginPageLocators
from login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # для перехода по страницам, можно использовать вариант
        # инициализации объекта страницы путем его подключения в импорте и вызове
        # тут с использованием current_url() так мы передали текущий линкс и текущий
        # экземпляр браузера новому экземпляру логин пейдж
        # return  LoginPage(browser=self.browser, url=self.browser.current_url())
        # способ можно использовать, но с осторожностью, так как чем больше таких
        # подключаемых страниц, тем больше перекрестных импортов и риск зацикливания
        # импортов, ну и логика становится зависимой, что не есть хорошо

    # теперь мы получаем проинициализированный объект
    # def test_guest_can_go_to_login_page(self, browser):
    #     link = "http://selenium1py.pythonanywhere.com"
    #     page = MainPage(browser, link)
    #     page.open()
    #     login_page = page.go_to_login_page() # вот он
    #     login_page.should_be_login_page()

    # второй вариант - это использование
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    # в таком случае, у нас появляется дублирование кода, необходимость
    # просчитывания каждого перехода и попявляется лишний шаг в тесте.

    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login is not presented"


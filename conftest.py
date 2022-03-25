import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', default='ru', help='ru or en')
    parser.addoption('--browser_name', action='store', default="chrome", help='chrome or firefox')

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if browser_name == 'chrome':
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise f'not find browser {language}'
    yield browser
    print("\nquit browser..")
    browser.quit()
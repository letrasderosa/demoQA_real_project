from selenium import webdriver
import pytest
import time
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile



def pytest_addoption(parser):
    """Определяем возможность выбора браузера"""
    parser.addoption('--browser', action='store', default='chrome')


@pytest.fixture(scope='session')
def browser(request):
    """Определяем настройки драйвера в зависимости от опции командной строки"""
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        options = chrome_options()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        options = firefox_options()
        # options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError('Unsupported browser')

    # driver.maximize_window()
    yield driver
    driver.quit()




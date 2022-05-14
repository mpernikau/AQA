from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
        parser.addoption('--language', action='store', default='en')

@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)


    yield browser

    print("\nquit browser...")
    browser.quit()

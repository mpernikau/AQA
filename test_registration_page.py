from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.registration_page import RegisterPage
import time
import pytest



class TestRegistrUser:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser, "https://staging.vr-smart-guide.de/registration")
        page.open()
        page.personal_data_button_click()
        first_name = 'George'
        last_name = 'Snow'
        email = str(time.time()) + "@examplemail.org"
        password = '80808011aDf13'
        page.register_new_user(email, first_name, last_name, password)




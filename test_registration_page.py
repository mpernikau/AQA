from pages.registration_page import RegisterPage

import time
import pytest



class TestRegistrUser:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser, "https://staging.vr-smart-guide.de/registration")
        page.open()
        page.personal_data_button_click()
        page.register_new_user()

    def test_user_can_test(self, browser):
        assert True




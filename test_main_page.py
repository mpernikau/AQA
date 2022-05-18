from pages.base_page import BasePage
from pages.main_page import MainPage
import pytest
import time

class TestLoggedUser:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = BasePage(browser, "https://staging.vr-smart-guide.de/login")
        page.open()
        page.personal_data_button_click()
        page.fill_email_password_fields()
        time.sleep(1)

    def test_user_can_enter_proposals_page(self, browser, timeout=15):
        page = MainPage(browser, "https://staging.vr-smart-guide.de")
        page.open()
        page.hover_menu()
        page.enter_outgoing_invoice_page()
        page.enter_proposal_page()
        page.create_new_proposal()
        page.filling_proposal_inputs_1()
        page.scroll_page()
        page.filling_proposal_inputs_2()
        time.sleep(3)
from pages.base_page import BasePage
from pages.proposal_page import ProposalPage
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
        page.check_url_after_loggin()

    def test_user_can_create_proposal(self, browser, timeout=15):
        page = ProposalPage(browser, "https://staging.vr-smart-guide.de")
        page.open()
        page.hover_menu()
        page.enter_outgoing_invoice_page()
        page.enter_proposal_page()
        page.create_new_proposal()
        page.fill_name_input_proposal()
        page.fill_client_input_proposal()
        page.click_client_input_proposal()
        page.fill_until_input_proposal()
        page.scroll_page()
        page.fill_line_input_name_proposal()
        page.fill_line_input_quantity_proposal()
        page.fill_line_input_unit_proposal()
        page.click_line_input_unit_proposal()
        page.fill_line_input_net_gross_proposal()
        page.click_line_item_creation_button_proposal()
        page.line_item_creation_button_pressed()
        page.click_download_or_save_button_proposal()
        page.click_download_pdf_button_proposal()
        time.sleep(3)
        page.check_url_after_creating_proposal()
        time.sleep(3)
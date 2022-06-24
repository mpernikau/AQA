from pages.base_page import BasePage
from pages.proposal_page import ProposalPage
from pages.proposal_page import ProposalPageList
from pages.order_conformation_page import OrderConformationPage
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
        page = OrderConformationPage(browser, "https://staging.vr-smart-guide.de")
        page.hover_menu()
        page.enter_outgoing_invoice_page()
        page.enter_order_conformation_page()

    #@pytest.mark.smoke
    def test_user_can_create_pdf_order_conformation(self, browser):
        page = OrderConformationPage(browser, "https://staging.vr-smart-guide.de")
        page.create_new_order_conformation()
        page.fill_name_input_order_conformation()
        page.fill_client_input_order_conformation()
        page.click_client_input_order_conformation()
        page.fill_until_input_order_conformation()
        page.scroll_page()
        page.fill_line_input_name_order_conformation()
        page.fill_line_input_quantity_order_conformation()
        page.fill_line_input_unit_order_conformation()
        page.click_line_input_unit_order_conformation()
        page.fill_line_input_net_gross_order_conformation()
        page.click_line_item_creation_button_order_conformation()
        page.line_item_creation_button_pressed()
        page.click_download_or_save_button_order_conformation()
        page.click_download_pdf_button_order_conformation()
        page.check_url_after_creating_order_conformation()

    #@pytest.mark.smoke
    def test_user_can_send_order_conformation_by_email(self, browser):
        page = OrderConformationPage(browser, "https://staging.vr-smart-guide.de")
        page.create_new_order_conformation()
        page.fill_name_input_order_conformation()
        page.fill_client_input_order_conformation()
        page.click_client_input_order_conformation()
        page.fill_until_input_order_conformation()
        page.scroll_page()
        page.fill_line_input_name_order_conformation()
        page.fill_line_input_quantity_order_conformation()
        page.fill_line_input_unit_order_conformation()
        page.click_line_input_unit_order_conformation()
        page.fill_line_input_net_gross_order_conformation()
        page.click_line_item_creation_button_order_conformation()
        page.line_item_creation_button_pressed()
        page.click_download_or_save_button_order_conformation()
        page.click_order_conformation_send_by_email()
        page.check_url_after_creating_order_conformation()

    #@pytest.mark.smoke
    def test_user_can_create_invoice_from_order_conformation_document(self, browser):
        page = OrderConformationPage(browser, "https://staging.vr-smart-guide.de")
        page.create_new_order_conformation()
        page.fill_name_input_order_conformation()
        page.fill_client_input_order_conformation()
        page.click_client_input_order_conformation()
        page.fill_until_input_order_conformation()
        page.scroll_page()
        page.fill_line_input_name_order_conformation()
        page.fill_line_input_quantity_order_conformation()
        page.fill_line_input_unit_order_conformation()
        page.click_line_input_unit_order_conformation()
        page.fill_line_input_net_gross_order_conformation()
        page.click_line_item_creation_button_order_conformation()
        page.line_item_creation_button_pressed()
        page.create_invoice_from_order_confirmation()
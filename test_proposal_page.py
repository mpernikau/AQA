from pages.base_page import BasePage
from pages.proposal_page import ProposalPage
from pages.proposal_page import ProposalPageList
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
        page = ProposalPage(browser, "https://staging.vr-smart-guide.de")
        page.hover_menu()
        page.enter_outgoing_invoice_page()
        page.enter_proposal_page()


    def test_user_can_create_proposal(self, browser, timeout=15):
        page = ProposalPage(browser, "https://staging.vr-smart-guide.de")
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
        time.sleep(1)
        page.check_url_after_creating_proposal()


    def test_user_can_navigate_through_proposal_page(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_page_navigation_arrows()


    @pytest.mark.smoke
    def test_user_can_enter_proposal_view_mode(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_view_mode()

    @pytest.mark.smoke
    def test_user_can_enter_proposal_edit_mode(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_edit_mode()


    def test_user_can_use_search_on_proposal_page(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_search_input()
        time.sleep(2)
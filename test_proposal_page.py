from pages.base_page import BasePage
from pages.proposal_page import ProposalPage
from pages.proposal_page import ProposalPageList
import pytest
import time

class TestCreationDocumentsLoggedUser:
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


    #@pytest.mark.smoke
    def test_user_can_create_pdf_proposal(self, browser):
        page = ProposalPage(browser, "https://staging.vr-smart-guide.de")
        page.click_download_or_save_button_proposal()
        page.click_download_pdf_button_proposal()
        page.check_url_after_creating_proposal()

    #@pytest.mark.smoke
    def test_user_can_send_proposal_by_email(self, browser):
        page = ProposalPage(browser, "https://staging.vr-smart-guide.de")
        page.click_download_or_save_button_proposal()
        page.click_proposal_send_by_email()
        page.check_url_after_sending_email()


    #@pytest.mark.smoke
    def test_user_can_create_invoice_from_proposal_document(self, browser):
        page = ProposalPage(browser, "https://staging.vr-smart-guide.de")
        page.create_invoice_from_proposal()

    #@pytest.mark.smoke
    def test_user_can_create_order_conformation_from_proposal(self, browser):
        page = ProposalPage(browser, "https://staging.vr-smart-guide.de")
        page.create_order_conformation_from_proposal()

    # @pytest.mark.smoke
    def test_user_can_create_proposal_draft(self, browser):
        page = ProposalPage(browser, "https://staging.vr-smart-guide.de")
        page.create_proposal_draft()


class TestPageFunctionalityLoggedUser:
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

    #@pytest.mark.smoke
    def test_user_can_navigate_through_proposal_page(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_page_navigation_arrows()


    #@pytest.mark.smoke
    def test_user_can_enter_proposal_view_mode(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_view_mode()


    #@pytest.mark.smoke
    def test_user_can_edit_proposal(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.user_can_edit_proposal()


    #@pytest.mark.smoke
    def test_user_can_duplicate_proposals(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_duplicate_button()


    #@pytest.mark.smoke
    def test_user_can_create_invoice_from_proposal_page(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_to_invoice_button()


    #@pytest.mark.smoke
    def test_user_can_use_search_on_proposal_page(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_search_input()


    #@pytest.mark.smoke
    def test_user_can_not_delete_sent_proposal(self, browser):
        page_proposal = ProposalPage(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.create_new_proposal()
        page_proposal.fill_name_input_proposal()
        page_proposal.fill_client_input_proposal()
        page_proposal.click_client_input_proposal()
        page_proposal.fill_until_input_proposal()
        page_proposal.scroll_page()
        page_proposal.fill_line_input_name_proposal()
        page_proposal.fill_line_input_quantity_proposal()
        page_proposal.fill_line_input_unit_proposal()
        page_proposal.click_line_input_unit_proposal()
        page_proposal.fill_line_input_net_gross_proposal()
        page_proposal.click_line_item_creation_button_proposal()
        page_proposal.line_item_creation_button_pressed()
        page_proposal.click_download_or_save_button_proposal()
        page_proposal.click_download_pdf_button_proposal()
        time.sleep(2)
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_delete_button()


    #@pytest.mark.smoke
    def test_user_can_export_csv_proposals(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.check_proposal_export_csv_feature()


    #@pytest.mark.smoke
    def test_filters_on_proposal_page_work_properly(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.proposal_page_filters_work_properly()

    @pytest.mark.smoke
    def test_proposal_page_number_on_the_page_works_properly(self, browser):
        page_proposal = ProposalPageList(browser, 'https://staging.vr-smart-guide.de/proposals')
        page_proposal.proposal_page_number_on_the_page_works_properly()
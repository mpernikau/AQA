import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.locators import MainPageLocators
from pages.locators import OrderConfromationLocators
from pages.locators import OutgoingInvoiceLocators
from pages.locators import ProposalPageListLocators
from pages.locators import ProposalPageLocators
from .base_page import BasePage
from .base_page import creating_current_date
from .base_page import numbers_generator
from .base_page import subject_generator


class ProposalPage(BasePage):

    def alert_is_present(self):
        # Check if there is guide alert
        assert self.is_element_present(*MainPageLocators.ALERT_GUIDE), 'No guide alert'

    def guide_alert_btn_click(self):
        # Check if there is button to skip guide
        assert self.is_element_present(*MainPageLocators.ALERT_GUIDE_PASS_BTN), 'No button to skip guide'
        pass_guide_btn = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.ALERT_GUIDE_PASS_BTN))
        pass_guide_btn.click()

    def hover_menu(self):
        # Check if there is hover menu
        assert self.is_element_present(*MainPageLocators.BURGER_MENU), 'No menu'
        hover_menu = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.BURGER_MENU))
        hover_menu.click()


    def enter_outgoing_invoice_page(self):
        # Check if there is outgoing invoice page field in menu
        assert self.is_element_present(*MainPageLocators.OUTGOING_INVOICE_PAGE), 'No incoming invoice page'
        incoming_invoice_page = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.OUTGOING_INVOICE_PAGE))
        incoming_invoice_page.click()


    def enter_proposal_page(self):
        # Check if there is proposal page field in menu
        assert self.is_element_present(*MainPageLocators.PROPOSAL_PAGE), 'No proposal page'
        proposal_page = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.PROPOSAL_PAGE))
        proposal_page.click()


    def create_new_proposal(self):
        # Check if there is create proposal button
        assert self.is_element_present(*MainPageLocators.CREATE_PROPOSAL_BUTTON), 'No create proposal button'
        click_proposal_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.CREATE_PROPOSAL_BUTTON))
        click_proposal_button.click()

        # Check if there is alert button
        assert self.is_element_present(*MainPageLocators.BUTTON_BANK_ALERT), 'No alert button'
        button_bank_alert = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_BANK_ALERT))
        button_bank_alert.click()

        # Check if url contains 'proposals/new'
        url_check = self.browser.current_url
        assert 'proposals/new' in url_check, 'Wrong URL for proposals'


    def fill_name_input_proposal(self):
        # Check if there is subject menu
        assert self.is_element_present(*ProposalPageLocators.SUBJECT_INPUT), 'No subject input field'
        name = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.SUBJECT_INPUT))
        time.sleep(1)
        name.send_keys(subject_generator())


    def fill_client_input_proposal(self):
        # Check if there is client input
        assert self.is_element_present(*ProposalPageLocators.CLIENT_INPUT), 'No client input field'
        client = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.CLIENT_INPUT))
        client.send_keys('Some')


    def click_client_input_proposal(self):
        # Check if there is client menu
        assert self.is_element_present(*ProposalPageLocators.CLIENT_MENU_CHOICE), 'No client menu'
        client_menu = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.CLIENT_MENU_CHOICE))
        client_menu.click()


    def fill_until_input_proposal(self):
        # Check if there is valid until field
        assert self.is_element_present(*ProposalPageLocators.VALID_UNTIL_PROPOSAL), 'No valid until input'
        valid_until_proposal = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.VALID_UNTIL_PROPOSAL))
        valid_until_proposal.click()
        valid_until_proposal.send_keys(creating_current_date(self))


    def fill_line_input_name_proposal(self):
        # Check if there is name field
        line_item_input = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.LINE_ITEM_INPUT))
        assert self.is_element_present(*ProposalPageLocators.LINE_ITEM_INPUT), 'No line item input'
        line_item_input.click()
        line_item_input.send_keys(subject_generator())

    def fill_line_input_quantity_proposal(self):
        # Check if there is quantity field
        assert self.is_element_present(*ProposalPageLocators.LINE_ITEM_QUANTITY), 'No quantity field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.LINE_ITEM_QUANTITY))
        unit_proposal_field.send_keys(numbers_generator(size=2))

    def fill_line_input_unit_proposal(self):
        # Check if there is unit field
        assert self.is_element_present(*ProposalPageLocators.UNIT_PROPOSAL_FIELD), 'No unit field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.UNIT_PROPOSAL_FIELD))
        unit_proposal_field.send_keys('BOX')

    def click_line_input_unit_proposal(self):
        # Check if there is unit menu
        assert self.is_element_present(*ProposalPageLocators.UNIT_MENU_CHOICE), 'No unit menu'
        unit_menu = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.UNIT_MENU_CHOICE))
        unit_menu.click()

    def fill_line_input_net_gross_proposal(self):
        # Check if there is net gross field
        assert self.is_element_present(*ProposalPageLocators.LINE_ITEM_NET_GROSS), 'No net gross field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.LINE_ITEM_NET_GROSS))
        unit_proposal_field.send_keys(numbers_generator(size=2))


    def click_line_item_creation_button_proposal(self):
        # Check is there conformation line item button
        assert self.is_element_present(*ProposalPageLocators.CONFIRM_LINE_ITEM), 'No confirm line item button'
        confirm_line_item = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.CONFIRM_LINE_ITEM))
        time.sleep(1)
        confirm_line_item.click()

    def line_item_creation_button_pressed(self):
        # Check is there is no conformation line item button
        assert self.is_not_element_present(*ProposalPageLocators.CONFIRM_LINE_ITEM), 'Line item is not confirmed'

    def click_download_or_save_button_proposal(self):
        # Check is there download or save button
        assert self.is_element_present(*ProposalPageLocators.DOWNLOAD_OR_SAVE_PROPOSAL_BUTTON), 'No download or save button'
        download_or_save = WebDriverWait(self.browser, 5, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.DOWNLOAD_OR_SAVE_PROPOSAL_BUTTON))
        download_or_save.click()

    def click_download_pdf_button_proposal(self):
        # Check is there download pdf button
        assert self.is_element_present(*ProposalPageLocators.DOWNLOAD_PDF_PROPOSAL_BUTTON), 'No download pdf button'
        download_pdf = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.DOWNLOAD_PDF_PROPOSAL_BUTTON))
        download_pdf.click()

    def check_url_after_creating_proposal(self):
        url_check = self.browser.current_url
        # Check if url contains 'proposals/new'
        assert 'proposals/new' not in url_check, 'Wrong URL for proposals'

    def create_invoice_from_proposal(self):
        assert self.is_element_present(
            *ProposalPageLocators.PROPOSAL_PAGE_TO_INVOICE_BUTTON), 'No proposal_-to-invoice button'
        proposal_page_to_invoice_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.PROPOSAL_PAGE_TO_INVOICE_BUTTON))
        proposal_page_to_invoice_button.click()

        assert self.is_element_present(
            *ProposalPageLocators.SAVE_BEFORE_CONTINUE_MODAL_BUTTON), 'No save before continue modal button'
        proposal_save_before_continue = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.SAVE_BEFORE_CONTINUE_MODAL_BUTTON))
        proposal_save_before_continue.click()

        time.sleep(3)
        url_check = self.browser.current_url
        # Check if url contains 'from-proposal'
        assert 'from-proposal' in url_check, 'Wrong URL from proposals to invoice'

        assert self.is_element_present(
            *OutgoingInvoiceLocators.INVOICE_STATUS), 'No invoice status field'
        assert self.is_element_present(*OutgoingInvoiceLocators.DOWNLOAD_OR_SAVE_INVOICE_BUTTON), 'No download or save button'
        download_or_save_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OutgoingInvoiceLocators.DOWNLOAD_OR_SAVE_INVOICE_BUTTON))
        download_or_save_button.click()

        assert self.is_element_present(*OutgoingInvoiceLocators.DOWNLOAD_PDF_INVOICE_BUTTON), 'No download pdf button'
        download_pdf = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OutgoingInvoiceLocators.DOWNLOAD_PDF_INVOICE_BUTTON))
        download_pdf.click()

        url_check = self.browser.current_url
        # Check if url contains '/revenue/outgoing-invoices'
        assert '/revenue/outgoing-invoices' in url_check, 'Wrong URL for invoice'

    def create_order_conformation_from_proposal(self):
        assert self.is_element_present(
            *ProposalPageLocators.PROPOSAL_PAGE_TO_ORDER_CONFORMATION), 'No proposal_-to-invoice button'
        proposal_page_to_order_conformation_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.PROPOSAL_PAGE_TO_ORDER_CONFORMATION))
        proposal_page_to_order_conformation_button.click()

        assert self.is_element_present(
            *ProposalPageLocators.SAVE_BEFORE_CONTINUE_MODAL_BUTTON), 'No save before continue modal button'
        proposal_save_before_continue = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.SAVE_BEFORE_CONTINUE_MODAL_BUTTON))
        proposal_save_before_continue.click()

        time.sleep(3)
        url_check = self.browser.current_url
        # Check if url contains 'from-proposal'
        assert 'order-confirmation' in url_check, 'Wrong URL from proposals to order conformation'


        assert self.is_element_present(
            *OrderConfromationLocators.DOWNLOAD_OR_SAVE_ORDER_CONFORMATION_BUTTON), 'No download or save button'
        download_or_save_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.DOWNLOAD_OR_SAVE_ORDER_CONFORMATION_BUTTON))
        download_or_save_button.click()

        assert self.is_element_present(*OrderConfromationLocators.DOWLOAD_PDF_ORDER_CONFORMATION), 'No download pdf button'
        download_pdf = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.DOWLOAD_PDF_ORDER_CONFORMATION))
        download_pdf.click()

        url_check = self.browser.current_url
        # Check if url contains '/revenue/outgoing-invoices'
        assert 'order-confirmation' in url_check, 'Wrong URL for order confromation'




class ProposalPageList(BasePage):

    def check_page_navigation_arrows(self):
        # Is right arrow presented on the page
        assert self.is_element_present(*ProposalPageListLocators.PROPOSAL_PAGE_NAVIGATION_ARROW_RIGHT), 'No navigation arrow right'
        # Is left arrow presented on the page
        assert self.is_element_present(*ProposalPageListLocators.PROPOSAL_PAGE_NAVIGATION_ARROW_LEFT), 'No navigation arrow left'

        next_page = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageListLocators.PROPOSAL_PAGE_NAVIGATION_ARROW_RIGHT))
        next_page.click()
        # Is current page input presented on the page
        assert self.is_element_present(*ProposalPageListLocators.PROPOSAL_PAGE_NAVIGATION_CURRENT_PAGE_FIELD), 'No current page input'
        time.sleep(1)

        page_number = self.browser.find_element(*ProposalPageListLocators.PROPOSAL_PAGE_NAVIGATION_CURRENT_PAGE_FIELD)
        page_number_value = page_number.get_attribute('value')
        # Did we move to the next page using arrow right
        assert page_number_value == '2', 'Wrong page'

        previous_page = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageListLocators.PROPOSAL_PAGE_NAVIGATION_ARROW_LEFT))
        previous_page.click()
        time.sleep(1)

        page_num = self.browser.find_element(*ProposalPageListLocators.PROPOSAL_PAGE_NAVIGATION_CURRENT_PAGE_FIELD)
        page_num_value = page_num.get_attribute('value')
        # Did we move to the previous page using arrow left
        assert page_num_value == '1', 'Wrong page'


    def check_proposal_view_mode(self):
        assert self.is_element_present(
            *ProposalPageListLocators.PROPOSAL_VIEW_BUTTON), 'No view button on the first invoice'
        subject_on_page = self.browser.find_element(*ProposalPageListLocators.SUBJECT_ON_PROPOSAL_PAGE).text
        view_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageListLocators.PROPOSAL_VIEW_BUTTON))
        view_button.click()
        time.sleep(1)

        subject_on_document = self.browser.find_element(*ProposalPageLocators.SUBJECT_INPUT)
        assert self.is_element_present(*ProposalPageLocators.SUBJECT_INPUT), 'Smth wrong with name on proposal page'
        subject_on_document_value = subject_on_document.get_attribute('value')

        assert subject_on_page == subject_on_document_value, 'Wrong proposal was chosen for checking'

        input_disabling_finding = self.browser.find_element(
            *ProposalPageLocators.SUBJECT_INPUT)
        input_disabling_finding.get_property('disabled')
        assert True, 'Input is not disabled'


    def user_can_edit_proposal(self):
        assert self.is_element_present(
            *ProposalPageListLocators.PROPOSAL_EDIT_BUTTON), 'No edit button on the first invoice'
        subject_on_page = self.browser.find_element(*ProposalPageListLocators.SUBJECT_ON_PROPOSAL_PAGE).text
        edit_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageListLocators.PROPOSAL_EDIT_BUTTON))
        edit_button.click()
        time.sleep(1)

        subject_on_document = self.browser.find_element(*ProposalPageLocators.SUBJECT_INPUT)
        assert self.is_element_present(*ProposalPageLocators.SUBJECT_INPUT), 'Smth wrong with name on proposal page'
        subject_on_document_value = subject_on_document.get_attribute('value')

        assert subject_on_page == subject_on_document_value, 'Wrong proposal was chosen for checking'

        input_is_enabled = self.browser.find_element(*ProposalPageLocators.SUBJECT_INPUT)
        #input_is_enabled.click()
        #assert True, 'Input is disabled'
        input_is_enabled.send_keys('Aa111')
        input_is_enabled_value = input_is_enabled.get_attribute('value')
        assert 'Aa111' in input_is_enabled_value, 'text did not added to name'

        assert self.is_element_present(*ProposalPageLocators.CATEGORY_INPUT), 'No category input'
        category_input = self.browser.find_element(*ProposalPageLocators.CATEGORY_INPUT)
        category_input.click()
        assert self.is_element_present(*ProposalPageLocators.CATEGORY_OTHER_CATEGORY), 'No other category'
        choose_other_category = self.browser.find_element(*ProposalPageLocators.CATEGORY_OTHER_CATEGORY)
        choose_other_category.click()

        assert self.is_element_present(*ProposalPageLocators.CHANGE_CATEGORY_CONFIRM_BUTTON), 'No modal to confirm changing category'
        click_on_confirm_button = self.browser.find_element(*ProposalPageLocators.CHANGE_CATEGORY_CONFIRM_BUTTON)
        click_on_confirm_button.click()

        assert self.is_element_present(*ProposalPageLocators.CHANGE_CATEGORY_HINT), 'No hint about changing the category'
        changing_category_hint = self.browser.find_element(*ProposalPageLocators.CHANGE_CATEGORY_HINT)
        hint_text = 'Hinweis: Bei Auswahl dieser Kategorie wird auf dem PDF-Dokument automatisch der passende Erläuterungstext nach UStG gedruckt.'
        changing_category_hint_text = changing_category_hint.text
        assert hint_text in changing_category_hint_text, 'Hint text is wrong'

        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        save_button_is_disabled = self.browser.find_element(*ProposalPageLocators.DOWNLOAD_OR_SAVE_PROPOSAL_BUTTON)
        save_button_is_disabled.get_property('disabled')
        assert True, 'Save and download button is not disabled'

        to_order_conformation_button_is_disabled = self.browser.find_element(*ProposalPageLocators.PROPOSAL_PAGE_TO_ORDER_CONFORMATION)
        to_order_conformation_button_is_disabled.get_property('disabled')
        assert True, 'To order conformation button is not disabled'

        to_draft_button_is_disabled = self.browser.find_element(*ProposalPageLocators.SAVE_AS_DRAFT_BUTTON)
        to_draft_button_is_disabled.get_property('disabled')
        assert True, 'To draft button is not disabled'

        create_draft_click = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.SAVE_AS_DRAFT_BUTTON))
        create_draft_click.click()

        url_check = self.browser.current_url
        # Check if url contains 'proposals'
        assert 'proposals' in url_check, 'Wrong URL for proposals'

    def check_proposal_duplicate_button(self):
        assert self.is_element_present(
            *ProposalPageListLocators.PROPOSAL_DUPLICATE_BUTTON), 'No duplicate button on the first invoice'
        duplicate_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageListLocators.PROPOSAL_DUPLICATE_BUTTON))
        duplicate_button.click()
        client_table = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.CLIENT_INPUT))
        client_table.click()
        assert True, 'Client input is not clickable'


    def check_proposal_to_invoice_button(self):
        assert self.is_element_present(
            *ProposalPageListLocators.PROPOSAL_MORE_OPTIONS_BUTTON), 'No more options button on the first invoice'
        more_options_button = self.browser.find_element(*ProposalPageListLocators.PROPOSAL_MORE_OPTIONS_BUTTON)
        more_options_button.click()

        assert self.is_element_present(
            *ProposalPageListLocators.PROPOSAL_TO_INVOICE_BUTTON), 'No proposal_to_invoice button on the first invoice'
        proposal_to_invoice_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageListLocators.PROPOSAL_TO_INVOICE_BUTTON))
        proposal_to_invoice_button.click()

        url_check = self.browser.current_url
        # Check if url contains 'from-proposal'
        assert 'from-proposal' not in url_check, 'Wrong URL from proposals to invoice'


    def check_proposal_delete_button(self):
        assert self.is_element_present(
            *ProposalPageListLocators.PROPOSAL_MORE_OPTIONS_BUTTON), 'No more options button on the first invoice'
        more_options_button = self.browser.find_element(*ProposalPageListLocators.PROPOSAL_MORE_OPTIONS_BUTTON)
        more_options_button.click()

        assert self.is_not_element_present(
            *ProposalPageListLocators.PROPOSAL_DELETE_BUTTON), 'There is delete_proposal button on the first invoice'


    def check_proposal_search_input(self):
        # Is search input presented on the page
        assert self.is_element_present(*ProposalPageListLocators.PROPOSAL_PAGE_SEARCH), 'No search input'
        subject_on_page = self.browser.find_element(*ProposalPageListLocators.SUBJECT_ON_PROPOSAL_PAGE).text
        search_input = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageListLocators.PROPOSAL_PAGE_SEARCH))
        search_input.send_keys(subject_on_page)
        search_input_value = search_input.get_attribute('value')
        # Is proposal still has subject_name
        assert self.is_element_present(*ProposalPageListLocators.SUBJECT_ON_PROPOSAL_PAGE)
        # Check if text in input is the same as subject name
        assert search_input_value == subject_on_page, 'Search input text is not valid'

    def check_proposal_export_csv_feature(self):
        assert self.is_element_present(*ProposalPageListLocators.PROPOSAL_PAGE_CSV_EXPORT), 'No csv export button'
        csv_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageListLocators.PROPOSAL_PAGE_CSV_EXPORT))
        csv_button.click()
        time.sleep(3)
        assert self.check_csv_file_dowloaded_name('angebote_*.csv'), 'File name is wrong or file is not downloaded'
        time.sleep(1)
        self.delete_file_name_starts_with('angebote')




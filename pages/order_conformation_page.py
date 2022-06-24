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

class OrderConformationPage(BasePage):

    def enter_order_conformation_page(self):
        # Check if there is proposal page field in menu
        assert self.is_element_present(*MainPageLocators.ORDER_CONFORMATION_PAGE), 'No order conformation page'
        order_conformation_page = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_CONFORMATION_PAGE))
        order_conformation_page.click()


    def create_new_order_conformation(self):
        # Check if there is create order_conformation button
        assert self.is_element_present(*MainPageLocators.CREATE_ORDER_CONFORMATION_BUTTON), 'No create order conformation button'
        click_order_conformation_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.CREATE_ORDER_CONFORMATION_BUTTON))
        click_order_conformation_button.click()

        # Check if there is alert button
        assert self.is_element_present(*MainPageLocators.BUTTON_BANK_ALERT), 'No alert button'
        button_bank_alert = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_BANK_ALERT))
        button_bank_alert.click()

        # Check if url contains 'order-confirmation/new'
        url_check = self.browser.current_url
        assert 'order-confirmation/new' in url_check, 'Wrong URL for order conformation'


    def fill_name_input_order_conformation(self):
        # Check if there is subject menu
        assert self.is_element_present(*OrderConfromationLocators.SUBJECT_ON_ORDER_CONFORMATION_DOCUMENT), 'No subject input field'
        name = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.SUBJECT_ON_ORDER_CONFORMATION_DOCUMENT))
        time.sleep(1)
        name.send_keys(subject_generator())

    def fill_client_input_order_conformation(self):
        # Check if there is client input
        assert self.is_element_present(*ProposalPageLocators.CLIENT_INPUT), 'No client input field'
        client = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.CLIENT_INPUT))
        client.send_keys('Some')

    def click_client_input_order_conformation(self):
        # Check if there is client menu
        assert self.is_element_present(*ProposalPageLocators.CLIENT_MENU_CHOICE), 'No client menu'
        client_menu = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.CLIENT_MENU_CHOICE))
        client_menu.click()

    def fill_until_input_order_conformation(self):
        # Check if there is valid until field
        assert self.is_element_present(*OrderConfromationLocators.VALID_UNTIL_ORDER_CONFORMATION), 'No valid until input'
        valid_until_order_conformation = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.VALID_UNTIL_ORDER_CONFORMATION))
        valid_until_order_conformation.click()
        valid_until_order_conformation.send_keys(creating_current_date(self))

    def fill_line_input_name_order_conformation(self):
        # Check if there is name field
        line_item_input = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.LINE_ITEM_NAME_INPUT_ORDER_CONFORMATION))
        assert self.is_element_present(*OrderConfromationLocators.LINE_ITEM_NAME_INPUT_ORDER_CONFORMATION), 'No line item input'
        line_item_input.click()
        line_item_input.send_keys(subject_generator())

    def fill_line_input_quantity_order_conformation(self):
        # Check if there is quantity field
        assert self.is_element_present(*OrderConfromationLocators.LINE_ITEM_QUANTITY_ORDER_CONFORMATION), 'No quantity field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.LINE_ITEM_QUANTITY_ORDER_CONFORMATION))
        unit_proposal_field.send_keys(numbers_generator(size=2))

    def fill_line_input_unit_order_conformation(self):
        # Check if there is unit field
        assert self.is_element_present(*OrderConfromationLocators.LINE_ITEM_UNITS_ORDER_CONFORMATION), 'No unit field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.LINE_ITEM_UNITS_ORDER_CONFORMATION))
        unit_proposal_field.send_keys('KILOMETER')

    def click_line_input_unit_order_conformation(self):
        # Check if there is unit menu
        assert self.is_element_present(*ProposalPageLocators.UNIT_MENU_CHOICE), 'No unit menu'
        unit_menu = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.UNIT_MENU_CHOICE))
        unit_menu.click()

    def fill_line_input_net_gross_order_conformation(self):
        # Check if there is net gross field
        assert self.is_element_present(*ProposalPageLocators.LINE_ITEM_NET_GROSS), 'No net gross field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.LINE_ITEM_NET_GROSS))
        unit_proposal_field.send_keys(numbers_generator(size=2))

    def click_line_item_creation_button_order_conformation(self):

        # Check is there conformation line item button
        assert self.is_element_present(*ProposalPageLocators.CONFIRM_LINE_ITEM), 'No confirm line item button'
        confirm_line_item = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.CONFIRM_LINE_ITEM))
        time.sleep(1)
        confirm_line_item.click()

    def line_item_creation_button_pressed(self):
        # Check is there is no conformation line item button
        assert self.is_not_element_present(*ProposalPageLocators.CONFIRM_LINE_ITEM), 'Line item is not confirmed'

    def click_download_or_save_button_order_conformation(self):
        # Check is there download or save button
        assert self.is_element_present(*OrderConfromationLocators.DOWNLOAD_OR_SAVE_ORDER_CONFORMATION_BUTTON), 'No download or save button'
        download_or_save = self.browser.find_element(*OrderConfromationLocators.DOWNLOAD_OR_SAVE_ORDER_CONFORMATION_BUTTON)
        download_or_save.click()

    def click_download_pdf_button_order_conformation(self):
        # Check is there download pdf button
        assert self.is_element_present(*OrderConfromationLocators.DOWNLOAD_PDF_ORDER_CONFORMATION), 'No download pdf button'
        download_pdf = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.DOWNLOAD_PDF_ORDER_CONFORMATION))
        download_pdf.click()
        time.sleep(1)

    def check_url_after_creating_order_conformation(self):
        url_check = self.browser.current_url
        # Check if url contains 'order-confirmation'
        assert 'order-confirmation' in url_check, 'Wrong URL for order-confirmations'

    def click_order_conformation_send_by_email(self):
        assert self.is_element_present(*OrderConfromationLocators.SEND_BY_EMAIL_BUTTON_ORDER_CONFORMATION), 'No send by email button'
        send_by_email = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.SEND_BY_EMAIL_BUTTON_ORDER_CONFORMATION))
        send_by_email.click()

        assert self.is_element_present(*ProposalPageLocators.EMAIL_INPUT_ON_EMAIL_SENDING_MODAL), 'No email input field'
        email_input_fill = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.EMAIL_INPUT_ON_EMAIL_SENDING_MODAL))
        email_input_fill.send_keys('fleshstorm@mail.ru')

        assert self.is_element_present(*ProposalPageLocators.EMAIL_SEND_BUTTON), 'No email send button'
        email_send_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(ProposalPageLocators.EMAIL_SEND_BUTTON))
        email_send_button.click()

    def create_invoice_from_order_confirmation(self):
        assert self.is_element_present(
            *OrderConfromationLocators.ORDER_CONFORMATION_TO_INVOICE_BUTTON), 'No OC-to-invoice button'
        proposal_page_to_invoice_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.ORDER_CONFORMATION_TO_INVOICE_BUTTON))
        proposal_page_to_invoice_button.click()

        assert self.is_element_present(
            *OrderConfromationLocators.ORDER_CONFORMATION_TO_INVOICE_SAVE_BEFORE_CONTINUE_BUTTON), 'No save before continue modal button'
        proposal_save_before_continue = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(OrderConfromationLocators.ORDER_CONFORMATION_TO_INVOICE_SAVE_BEFORE_CONTINUE_BUTTON))
        proposal_save_before_continue.click()

        time.sleep(3)
        url_check = self.browser.current_url
        # Check if url contains 'from-order-confirmation'
        assert 'from-order-confirmation' in url_check, 'Wrong URL from-order-confirmation to invoice'

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
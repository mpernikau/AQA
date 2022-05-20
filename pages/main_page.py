from .base_page import BasePage
from pages.locators import MainPageLocators
import time
from .base_page import subject_generator
from .base_page import creating_current_date
from .base_page import numbers_generator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class MainPage(BasePage):

    def alert_is_present(self):
        assert self.is_element_present(*MainPageLocators.ALERT_GUIDE), 'No guide alert'

    def guide_alert_btn_click(self):
        assert self.is_element_present(*MainPageLocators.ALERT_GUIDE_PASS_BTN), 'No button to skip guide'
        pass_guide_btn = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.ALERT_GUIDE_PASS_BTN))
        pass_guide_btn.click()

    def hover_menu(self):
        assert self.is_element_present(*MainPageLocators.BURGER_MENU), 'No menu'
        hover_menu = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.BURGER_MENU))
        hover_menu.click()


    def enter_outgoing_invoice_page(self):
        assert self.is_element_present(*MainPageLocators.OUTGOING_INVOICE_PAGE), 'No incoming invoice page'
        incoming_invoice_page = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.OUTGOING_INVOICE_PAGE))
        incoming_invoice_page.click()


    def enter_proposal_page(self):
        assert self.is_element_present(*MainPageLocators.PROPOSAL_PAGE), 'No proposal page'
        proposal_page = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.PROPOSAL_PAGE))
        proposal_page.click()


    def create_new_proposal(self):
        assert self.is_element_present(*MainPageLocators.CREATE_PROPOSAL_BUTTON), 'No create proposal button'
        click_proposal_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.CREATE_PROPOSAL_BUTTON))
        click_proposal_button.click()

        assert self.is_element_present(*MainPageLocators.BUTTON_BANK_ALERT), 'No alert button'
        button_bank_alert = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.BUTTON_BANK_ALERT))
        button_bank_alert.click()

        url_check = self.browser.current_url
        assert 'proposals/new' in url_check, 'Wrong URL for proposals'


    def fill_name_input_proposal(self):
        assert self.is_element_present(*MainPageLocators.SUBJECT_INPUT), 'No subject input field'
        name = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.SUBJECT_INPUT))
        time.sleep(1)
        name.send_keys(subject_generator())


    def fill_client_input_proposal(self):
        assert self.is_element_present(*MainPageLocators.CLIENT_INPUT), 'No client input field'
        client = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.CLIENT_INPUT))
        client.send_keys('Some')


    def click_client_input_proposal(self):
        assert self.is_element_present(*MainPageLocators.CLIENT_MENU_CHOICE), 'No client menu'
        client_menu = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.CLIENT_MENU_CHOICE))
        client_menu.click()


    def fill_until_input_proposal(self):
        assert self.is_element_present(*MainPageLocators.VALID_UNTIL_PROPOSAL), 'No valid until input'
        valid_until_proposal = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.VALID_UNTIL_PROPOSAL))
        valid_until_proposal.click()
        valid_until_proposal.send_keys(creating_current_date(self))


    def fill_line_input_name_proposal(self):
        assert self.is_element_present(*MainPageLocators.LINE_ITEM_INPUT), 'No line item input'
        line_item_input = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.LINE_ITEM_INPUT))
        line_item_input.click()
        line_item_input.send_keys(subject_generator())

    def fill_line_input_quantity_proposal(self):
        assert self.is_element_present(*MainPageLocators.LINE_ITEM_QUANTITY), 'No quantity field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.LINE_ITEM_QUANTITY))
        unit_proposal_field.send_keys(numbers_generator(size=2))

    def fill_line_input_unit_proposal(self):
        assert self.is_element_present(*MainPageLocators.UNIT_PROPOSAL_FIELD), 'No unit field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.UNIT_PROPOSAL_FIELD))
        unit_proposal_field.send_keys('BOX')

    def click_line_input_unit_proposal(self):
        assert self.is_element_present(*MainPageLocators.UNIT_MENU_CHOICE), 'No unit menu'
        unit_menu = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.UNIT_MENU_CHOICE))
        unit_menu.click()

    def fill_line_input_net_gross_proposal(self):
        assert self.is_element_present(*MainPageLocators.LINE_ITEM_NET_GROSS), 'No net gross field'
        unit_proposal_field = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.LINE_ITEM_NET_GROSS))
        unit_proposal_field.send_keys(numbers_generator(size=2))


    def click_line_item_creation_button_proposal(self):
        assert self.is_element_present(*MainPageLocators.CONFIRM_LINE_ITEM), 'No confirm line item button'
        confirm_line_item = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.CONFIRM_LINE_ITEM))
        time.sleep(1)
        confirm_line_item.click()

    def line_item_creation_button_pressed(self):
        assert self.is_not_element_present(*MainPageLocators.CONFIRM_LINE_ITEM), 'Line item is not confirmed'

    def click_download_or_save_button_proposal(self):
        assert self.is_element_present(*MainPageLocators.DOWNLOAD_OR_SAVE_PROPOSAL_BUTTON), 'No download or save button'
        download_or_save = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.DOWNLOAD_OR_SAVE_PROPOSAL_BUTTON))
        download_or_save.click()

    def click_download_pdf_button_proposal(self):
        assert self.is_element_present(*MainPageLocators.DOWNLOAD_PDF_PROPOSAL_BUTTON), 'No download pdf button'
        download_pdf = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(MainPageLocators.DOWNLOAD_PDF_PROPOSAL_BUTTON))
        download_pdf.click()

    def check_url_after_creating_proposal(self):
        url_check = self.browser.current_url
        assert 'proposals/new' not in url_check, 'Wrong URL for proposals'

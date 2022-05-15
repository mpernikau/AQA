from .base_page import BasePage
from pages.locators import MainPageLocators
import time



class MainPage(BasePage):

    def alert_is_present(self):
        assert self.is_element_present(*MainPageLocators.ALERT_GUIDE), 'No guide alert'

    def guide_alert_btn_click(self):
        assert self.is_element_present(*MainPageLocators.ALLERT_GUIDE_PASS_BTN), 'No button to skip guide'
        pass_guide_btn = self.browser.find_element(*MainPageLocators.ALLERT_GUIDE_PASS_BTN)
        pass_guide_btn.click()

    def hover_menu(self):
        assert self.is_element_present(*MainPageLocators.BURGER_MENU), 'No menu'
        hover_menu = self.browser.find_element(*MainPageLocators.BURGER_MENU)
        hover_menu.click()

    def enter_outgoing_invoice_page(self):
        assert self.is_element_present(*MainPageLocators.OUTGOING_INVOICE_PAGE), 'No incoming invoice page'
        incoming_invoice_page = self.browser.find_element(*MainPageLocators.OUTGOING_INVOICE_PAGE)
        incoming_invoice_page.click()

    def enter_proposal_page(self):
        assert self.is_element_present(*MainPageLocators.PROPOSAL_PAGE), 'No proposal page'
        proposal_page = self.browser.find_element(*MainPageLocators.PROPOSAL_PAGE)
        proposal_page.click()

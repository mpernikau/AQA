from .base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def personal_data_button_click(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_PERSONAL_DATA), "Personal data button isn't found"
        button_personal = self.browser.find_element(*LoginPageLocators.BUTTON_PERSONAL_DATA)
        button_personal.click()

    def fill_email_password_fields(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), "No email field"
        email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email.send_keys('fleshstorm@mail.ru')
        assert self.is_element_present(*LoginPageLocators.PASS_FIELD), "No pass field"
        passw = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        passw.send_keys("Bugaga707")
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), "No submit button"
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()

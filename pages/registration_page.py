from .base_page import BasePage
from pages.locators import RegisterPageLocators
import random
import string




class RegisterPage(BasePage):


    def register_new_user(self, email, first_name, last_name, password):
        inp_first_name = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_FIELD)
        inp_first_name.send_keys(first_name)

        inp_last_name = self.browser.find_element(*RegisterPageLocators.LAST_NAME_FIELD)
        inp_last_name.send_keys(last_name)

        inp_email = self.browser.find_element(*RegisterPageLocators.REGISTRATION_EMAIL_FIELD)
        inp_email.send_keys(email)

        btn_reg = self.browser.find_element(*RegisterPageLocators.REGISTRATION_BUTTON)
        btn_reg.click()

        inp_pass = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        inp_pass.send_keys(password)

        checkbox = self.browser.find_element(*RegisterPageLocators.REQ_CHECKBOX)
        checkbox.click()

        recaptcha = self.browser.find_element(*RegisterPageLocators.RECAPTCHA)
        recaptcha.click()



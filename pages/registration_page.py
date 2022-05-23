from .base_page import BasePage
from pages.locators import RegisterPageLocators
from pages.base_page import subject_generator
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from pages.locators import MainPageLocators
import time
from .base_page import subject_generator
from .base_page import creating_current_date
from .base_page import numbers_generator

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class RegisterPage(BasePage):


    def register_new_user(self):

        first_name = 'George'
        inp_first_name = self.browser.find_element(*RegisterPageLocators.FIRST_NAME_FIELD)
        inp_first_name.send_keys(first_name)

        last_name = 'Snow'
        inp_last_name = self.browser.find_element(*RegisterPageLocators.LAST_NAME_FIELD)
        inp_last_name.send_keys(last_name)

        email = subject_generator() + "@examplemail.org"
        inp_email = self.browser.find_element(*RegisterPageLocators.REGISTRATION_EMAIL_FIELD)
        inp_email.send_keys(email)

        btn_reg = self.browser.find_element(*RegisterPageLocators.REGISTRATION_BUTTON)
        btn_reg.click()

        password = '80808011aDf13'
        inp_pass = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        inp_pass.send_keys(password)

        checkbox = self.browser.find_element(*RegisterPageLocators.REQ_CHECKBOX)
        checkbox.click()

        time.sleep(3)

        find_recaptcha_frame = self.browser.find_element(*RegisterPageLocators.RECAPTCHA_FRAME) #move to recaptcha frame
        switch_to_recaptcha_frame = self.browser.switch_to.frame(find_recaptcha_frame)

        time.sleep(3)
        recaptcha = self.browser.find_element(*RegisterPageLocators.RECAPTCHA_SOLVE)
        recaptcha.click()
        time.sleep(3)
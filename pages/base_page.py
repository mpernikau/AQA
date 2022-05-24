from selenium.common.exceptions import NoSuchElementException
from pages.locators import LoginPageLocators
from pages.locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import string
import random
from datetime import date
import time

def subject_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def creating_current_date(self):
    today = date.today()
    current_date = str(today.strftime("%d.%m.%Y"))
    return current_date

def numbers_generator(size=1, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class BasePage():
    def __init__(self, browser, url, timeout=15):  #Конструктор — метод, который вызывается, когда мы создаем объект. Конструктор объявляется ключевым словом __init__
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def personal_data_button_click(self):
        assert self.is_element_present(*LoginPageLocators.BUTTON_PERSONAL_DATA), "Personal data button isn't found"
        button_personal = self.browser.find_element(*LoginPageLocators.BUTTON_PERSONAL_DATA)
        button_personal.click()

    def fill_email_password_fields(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FIELD), "No email field"
        email = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        email.send_keys('fleshstorm@mail.ru')
        assert self.is_element_present(*LoginPageLocators.PASS_FIELD), "No pass field"
        passw = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.presence_of_element_located(LoginPageLocators.PASS_FIELD))
        passw.send_keys("Bugaga707")
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), "No submit button"
        submit_button = WebDriverWait(self.browser, 15, TimeoutException).until(
            EC.element_to_be_clickable(LoginPageLocators.SUBMIT_BUTTON))
        submit_button.click()

    def check_url_after_loggin(self):
        url_check = self.browser.current_url
        assert 'login' not in url_check, 'User is not logged in'


    def close_notification(self):
        assert self.is_element_present(*MainPageLocators.NOTIF_CLOSE)

    def scroll_page(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

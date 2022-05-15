from selenium.common.exceptions import NoSuchElementException
from pages.locators import LoginPageLocators
from pages.locators import MainPageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


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
        email = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email.send_keys('fleshstorm@mail.ru')
        assert self.is_element_present(*LoginPageLocators.PASS_FIELD), "No pass field"
        passw = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        passw.send_keys("Bugaga707")
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON), "No submit button"
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def close_notification(self):
        assert self.is_element_present(*MainPageLocators.NOTIF_CLOSE)

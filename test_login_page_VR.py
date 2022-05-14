from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from .pages.base_page import BasePage
from .pages.login_page import LoginPage

link = "https://staging.vr-smart-guide.de/login"

class LoginPageTests():

     def userCanLogin(browser, link):

         page = BasePage(browser, link)
         page.open()
         login_page = LoginPage(browser, link)
         login_page.personal_data_button_click()
         login_page.fill_email_password_fields()




# не забываем оставить пустую строку в конце файла


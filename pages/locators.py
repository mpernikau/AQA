from selenium.webdriver.common.by import By


class LoginPageLocators():
    BUTTON_PERSONAL_DATA = (By.CSS_SELECTOR, "[data-id='accept-all']")
    EMAIL_FIELD = (By.NAME, 'email')
    PASS_FIELD = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-id='button-submit']")
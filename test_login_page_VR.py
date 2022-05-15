from pages.base_page import BasePage


def test_User_Can_Login(browser):
    page = BasePage(browser, "https://staging.vr-smart-guide.de/login")
    page.open()
    page.personal_data_button_click()
    page.fill_email_password_fields()







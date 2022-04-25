import pytest
from selenium.webdriver.common.by import By



def test_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(15)

    button_exists = browser.find_elements(By.ID, 'add_to_basket_form')
    assert button_exists, 'no button'


if __name__ == "__main__":
        pytest.main()

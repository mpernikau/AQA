from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "https://staging.vr-smart-guide.de/login"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_personal_data = browser.find_element(By.CSS_SELECTOR, "[data-id='accept-all']")
    button_personal_data.click()

    input1 = browser.find_element(By.NAME, 'email').send_keys('fleshstorm@mail.ru')

    input2 = browser.find_element(By.NAME, 'password').send_keys("Bugaga707")

    button = browser.find_element(By.CSS_SELECTOR, "[data-id='button-submit']")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


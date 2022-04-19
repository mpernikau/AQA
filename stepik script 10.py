from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"



try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element(By.ID, 'input_value')
    get_x = x_element.text
    y = calc(get_x)

    input1 = browser.find_element(By.ID, 'answer').send_keys(y)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
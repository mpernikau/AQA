from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    get_x = x_element.text
    y = calc(get_x)

    input1 = browser.find_element(By.ID, 'answer').send_keys(y)

    input2 = browser.find_element(By.ID, 'robotCheckbox').click()

    input3 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input3) #скрол в видимость
    input3.click()

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


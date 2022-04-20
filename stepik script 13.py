from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button = browser.find_element(By.ID, 'book')
    button.click()

    x_element = browser.find_element(By.ID, 'input_value')
    get_x = x_element.text
    x_count = calc(get_x)

    input1 = browser.find_element(By.ID, 'answer').send_keys(x_count)

    button2 = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()

finally:

    time.sleep(10)

    browser.quit()

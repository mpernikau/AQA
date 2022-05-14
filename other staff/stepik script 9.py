from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname').send_keys('Ivan')

    input2 = browser.find_element(By.NAME, 'lastname').send_keys('Ivanov')

    input3 = browser.find_element(By.NAME, 'email').send_keys('IvanIvanov@mail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__)) #путь к .py файлу
    file_path = os.path.join(current_dir, 'NameFile.txt') #название файла в директории с .py файлом
    file_send = browser.find_element(By.ID, 'file')
    file_send.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

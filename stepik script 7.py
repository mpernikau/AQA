from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)


    first_element = browser.find_element(By.ID, 'num1')
    first_element_num = int(first_element.text)
    second_element = browser.find_element(By.ID, 'num2')
    second_element_num = int(second_element.text)
    summa = str(first_element_num+second_element_num)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(summa)
    #get_x = x_element.text('valuex')



    #input1 = browser.find_element(By.ID, 'answer').send_keys(y)
    #input2 = browser.find_element(By.ID, 'robotCheckbox').click()
    #input3 = browser.find_element(By.ID, 'robotsRule').click()
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default').click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


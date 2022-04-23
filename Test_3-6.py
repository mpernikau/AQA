import time
import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture(scope="function") #фикстура открытия\закрытия браузера после теста
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]) #параметризация с частями урла
class TestLogin:
    def test_entering_link(self, browser, link):
        answer = str(math.log(int(time.time()))) #фигня, которую нужно решить для получения данных для инпута

        link = f"https://stepik.org/lesson/{link}/step/1/"
        browser.get(link)
        browser.implicitly_wait(10)

        input = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
        input.send_keys(answer)

        waiting1 = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))) #ждем пока кнопка станет кликабл

        button = browser.find_element(By.CLASS_NAME, "submit-submission")
        button.click()

        waiting2 = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))) #ждем когда появится текст

        success_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text #ищем текст + меняем формат на текст
        text = success_text
        assert("Correct!" == text) #проверяем, подходит ли ответ
        if text != "Correct":
            return(text)

        if __name__ == "__main__":
            pytest.main()
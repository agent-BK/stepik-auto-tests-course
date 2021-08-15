import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


class TestSucceed:
    @pytest.mark.parametrize('lesson_num', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
    def test_succeed(self, browser, lesson_num):
        url = f"https://stepik.org/lesson/{lesson_num}/step/1"
        answer = math.log(int(time.time()))

        browser.get(url)

        # форма ввода текста
        textarea = browser.find_element_by_xpath("//textarea")
        textarea.send_keys(f'{answer}')

        # кнопка "Отправить"
        button = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
        button.click()
        # получение и проверка ответа
        feedback = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//pre")))
        assert feedback.text == "Correct!"
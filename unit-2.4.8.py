# import time
# import random

import math
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# генерация произвольного набора букв определенной длины т.е по сути тестоового слова
# def rand_word(start_count, end_count):
#    list_letters = random.sample(letters, random.randint(start_count, end_count))
#    return "".join(map(chr, list_letters))


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def scroll(element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)


# генерация списка символов для формирования случаных наборов букв произвольной длины
# letters = list(range(97, 123)) + list(range(65, 91))

url = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(5)

try:
    if WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "100")):
        browser.find_element_by_id("book").click()

        text_input = browser.find_element_by_id("input_value").text

        answer = browser.find_element_by_id("answer")
        scroll(answer)
        answer.send_keys(calc(text_input))

        button = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.ID, "solve")))
        scroll(button)
        button.click()

        alert = browser.switch_to.alert
        print(alert.text)
        alert.accept()
    else:
        print("Нет подходящей цены")
finally:
    browser.quit()

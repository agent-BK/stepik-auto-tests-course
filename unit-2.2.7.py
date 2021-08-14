from selenium import webdriver
import time
import random
import os

def random_words(letters):
  word = "".join(map(chr, random.sample(letters, random.randint(3, 15))))
  return word

def path_file(file_name):
  current_dir = os.path.abspath(os.path.dirname(__file__))
  return os.path.join(current_dir, file_name)


# генерация списка символов для формирования случаных наборов букв произвольной длины
letters = list(range(97, 123)) + list(range(65, 91))

browser = webdriver.Chrome()
link = " http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
  for element in browser.find_elements_by_css_selector("input[type=text]"):
    element.send_keys(random_words(letters))

  browser.find_element_by_css_selector("#file").send_keys(path_file("test.txt"))
  time.sleep(1)

  btn_submit = browser.find_element_by_css_selector("form button[type=submit]")
  btn_submit.click()

finally:
  time.sleep(10)
  browser.quit()
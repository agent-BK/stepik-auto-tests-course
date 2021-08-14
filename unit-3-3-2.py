import unittest
import random
from selenium import webdriver


class TestFormRegistration(unittest.TestCase):

    # генерация произвольного набора букв определенной длины т.е по сути тестового слова
    @staticmethod
    def rand_word(start_count=3, end_count=10):
        # генерация списка символов для формирования случаных наборов букв произвольной длины
        letters = list(range(97, 123)) + list(range(65, 91))
        list_letters = random.sample(letters, random.randint(start_count, end_count))
        return "".join(map(chr, list_letters))

    def form_registration(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element_by_css_selector("input.first[required]").send_keys(self.rand_word(3, 15))
        browser.find_element_by_css_selector("input.second[required]").send_keys(self.rand_word(3, 15))
        browser.find_element_by_css_selector("input.third[required]").send_keys(self.rand_word(3, 15))
        browser.find_element_by_css_selector("form[method=get] button[type=submit]").click()

        text = browser.find_element_by_tag_name("h1").text
        browser.quit()
        self.assertEqual(text, "Congratulations! You have successfully registered!", "registration is failed")

    def test_form_registrarion_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.form_registration(link)

    def test_form_registrarion_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.form_registration(link)


if __name__ == "__main__":
    unittest.main()

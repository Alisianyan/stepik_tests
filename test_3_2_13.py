from selenium import webdriver
import unittest, time

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        print("nyan1")
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_name_field=browser.find_element_by_css_selector(".first_block .first_class input")
        first_name_field.send_keys("example")
        time.sleep(1)
        last_name_field=browser.find_element_by_css_selector(".first_block .second_class input")
        last_name_field.send_keys("example")
        time.sleep(1)
        email_field=browser.find_element_by_css_selector(".first_block .third_class input")
        email_field.send_keys("example")
        time.sleep(1)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        string = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual (string, welcome_text, "failed!")
        time.sleep(10)
        browser.quit()

    def test_registration2(self):
        print("nyan1")
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        first_name_field=browser.find_element_by_css_selector(".first_block .first_class input")
        first_name_field.send_keys("example")
        time.sleep(1)
        last_name_field=browser.find_element_by_css_selector(".first_block .second_class input")
        last_name_field.send_keys("example")
        time.sleep(1)
        email_field=browser.find_element_by_css_selector(".first_block .third_class input")
        email_field.send_keys("example")
        time.sleep(1)
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        string = "Congratulations! You have successfully registered!"
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual (string, welcome_text, "failed!")
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    unittest.main()

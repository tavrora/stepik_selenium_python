import unittest
from selenium import webdriver
import time

class TestRegistration(unittest.TestCase):
	def test_reg_1(self):
		# test_pass
	    link = "http://suninjuly.github.io/registration1.html" 
	    browser = webdriver.Chrome()
	    browser.get(link)

	    # Код, который заполняет обязательные поля
	    ...
	    input1 = browser.find_element_by_css_selector(".first_block .first")
	    input1.send_keys("Ivan")
	    input2 = browser.find_element_by_css_selector(".first_block .second")
	    input2.send_keys("Petrov")
	    input3 = browser.find_element_by_css_selector(".first_block .third")
	    input3.send_keys("ivan@ivan.ku")

	    input4 = browser.find_element_by_css_selector(".second_block .first")
	    input4.send_keys("89622255888")
	    input4 = browser.find_element_by_css_selector(".second_block .second")
	    input4.send_keys("Russia")

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

	    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	    self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 
	    	"Welcome text does not match")

	    # ожидание чтобы визуально оценить результаты прохождения скрипта
	    time.sleep(10)
	    # закрываем браузер после всех манипуляций
	    browser.quit()


	def test_reg_2(self):
	    # test_fail
	    link = "http://suninjuly.github.io/registration2.html"
	    browser = webdriver.Chrome()
	    browser.get(link)

	    # Код, который заполняет обязательные поля
	    ...
	    input1 = browser.find_element_by_css_selector(".first_block .first")
	    input1.send_keys("Ivan")
	    input2 = browser.find_element_by_css_selector(".first_block .second")
	    input2.send_keys("Petrov")
	    input3 = browser.find_element_by_css_selector(".first_block .third")
	    input3.send_keys("ivan@ivan.ku")

	    input4 = browser.find_element_by_css_selector(".second_block .first")
	    input4.send_keys("89622255888")
	    input4 = browser.find_element_by_css_selector(".second_block .second")
	    input4.send_keys("Russia")

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

	    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	    self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 
	    	"Welcome text does not match")

	    # ожидание чтобы визуально оценить результаты прохождения скрипта
	    time.sleep(10)
	    # закрываем браузер после всех манипуляций
	    browser.quit()


if __name__ == "__main__":
    unittest.main()
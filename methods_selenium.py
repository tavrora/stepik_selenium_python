# перенести используемые зависимости в файл
pip freeze > requirements.txt
# установить зависимоисти
pip install -r requirements.txt


Чтобы указать количество перезапусков для каждого из упавших тестов, 
нужно добавить в командную строку параметр:
"--reruns n", где n - это количество перезапусков.

--tb=line, чтобы сократить лог с результатами теста

pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py

# проверка пристуствия кнопки
button = browser.find_element_by_css_selector('.btn.btn-add-to-basket')
assert button.get_attribute('type') == 'submit'
assert button.is_displayed() is True, "Должна быть кнопка добавления в корзину" 
assert browser.find_element_by_css_selector('.btn-add-to-basket'), 'Кнопка не найдена'

1.6

from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    button = browser.find_element_by_css_selector("button.btn")
    #or
    button = browser.find_element_by_xpath("//div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


1.6

link = browser.find_element_by_partial_link_text(result)

# заполнение полей в цикле
elements = browser.find_elements_by_tag_name("input")
	for element in elements:
	   element.send_keys("Мой ответ")

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text
# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text


2.1

# проставляем чекбоксы и радиобаттоны
robotCheckbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
robotCheckbox.click()
robotsRule = browser.find_element_by_css_selector("[for='robotsRule']")
robotsRule.click()

# берем значение атрибута элемента
x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex") 


2.2 

# выпадающий список
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"

# скролл
input_element = browser.find_element_by_tag_name("input")
browser.execute_script("return arguments[0].scrollIntoView(true);", input_element)

import os 
# получаем путь к директории текущего исполняемого файла 
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')            
element.send_keys(file_path


2.3

# модальные окна
alert = browser.switch_to.alert
alert.accept()
# Чтобы получить текст из alert, используйте свойство text объекта alert:
alert = browser.switch_to.alert
alert_text = alert.text

# подтверждение или отказ в модальном окне
confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

# модальное окно с полем для ввода текста
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

# получение имени вкладки
first_window = browser.window_handles[0]
new_window = browser.window_handles[1]
# переключение на вкладку браузера
browser.switch_to.window(window_name)


2.4

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд (вместо sleep)
browser.implicitly_wait(5)

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

# говорим Selenium проверять в течение 12 секунд пока цена не будет $100
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )



3

# Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод add_experimental_option, как указано в примере ниже:

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

# Для Firefox объявление нужного языка будет выглядеть немного иначе:

fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
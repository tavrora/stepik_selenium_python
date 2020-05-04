from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element_by_id("num1")
    num1 = num1_element.text
    num2_element = browser.find_element_by_id("num2")
    num2 = num2_element.text
    result = int(num1) + int(num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result)) # ищем элемент с результатом

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
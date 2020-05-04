from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # скролл
    input_element = browser.find_element_by_tag_name("input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_element)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    robotCheckbox = browser.find_element_by_id("robotCheckbox")
    robotCheckbox.click()
    robotsRule = browser.find_element_by_id("robotsRule")
    robotsRule.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
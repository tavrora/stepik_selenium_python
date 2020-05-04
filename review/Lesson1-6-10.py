from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('input[placeholder~=first]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    input2.send_keys("Smolensk@ssr.ru")
    input3 = browser.find_element_by_class_name('form-control.second')
    input3.send_keys("Petrov")
    # input4 = browser.find_element_by_id("country")
    # input4.send_keys("Russia")

    # Ваш код, который заполняет обязательные поля
    ...

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
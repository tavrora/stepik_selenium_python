from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# "Правильная" страница, которую тест проходит
page = "http://suninjuly.github.io/registration1.html"
# "Неправильная" страница, где тест выбрасывает исключение NoSuchElementException из-за отсутствия второго поля
# page = "http://suninjuly.github.io/registration2.html"

# Используем менеджер контекста вместо конструкции try...except...finally
# browser.quit() он выполнит сам, благодаря объявленному в классе WebDriver методу __exit__
with webdriver.Chrome() as browser:
    # Открываем в Chrome страницу, ищем нужные поля ввода по уникальным селекторам классов и заполняем их
    browser.get(page)
    input_first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input_last_name.send_keys("Danko")
    input_email = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input_email.send_keys("red@heat.su")

    # Ищем кнопку подтверждения, нажимаем
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Ждём 1 сек для загрузки следующей страницы. Если она на вашем канале не успевает открыться, увеличьте аргумент
    time.sleep(1)

    # Находим на открывшейся странице текст в заголовке, присваиваем переменной
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    # Сравниваем с референсным значением
    assert "Congratulations! You have successfully registered!" == welcome_text
    # Ждём 10 сек для визуальной оценки, по истечении времени браузер закроется сам
    time.sleep(10)

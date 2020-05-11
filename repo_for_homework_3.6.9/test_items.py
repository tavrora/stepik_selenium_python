import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_exists_button_add_basket(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button.get_attribute('type') == 'submit'

    # или так
    # assert button.is_displayed() is True
    # assert browser.find_element_by_css_selector('.btn-add-to-basket'), 'Кнопка не найдена'

    # запасной вариант
    # try:
	# 	browser.find_element_by_css_selector(".btn-add-to-basket")
	# except NoSuchElementException:
	# 	return False
	# return True

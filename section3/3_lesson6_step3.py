import time
import math
import pytest
from selenium import webdriver

text_result = ''

@pytest.fixture(scope="function")
# @pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(18)
    yield browser
    print("\nquit browser..")
    browser.quit()
    # print(f"Sentence: {text_result}")


@pytest.mark.parametrize('step', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_the_answer_must_be_correct(browser, step):
	global text_result
	link = f"https://stepik.org/lesson/{step}/step/1"
	browser.get(link)

	answer = math.log(int(time.time()))
	answer_element = browser.find_element_by_css_selector("textarea")
	answer_element.send_keys(str(answer))
	button = browser.find_element_by_css_selector(".submit-submission")
	button.click()
	result_element = browser.find_element_by_tag_name("pre")
	result = result_element.text

	# конкатенируем результаты опциональных фидбеков из каждого упавшего теста	
	if result != "Correct!":
		text_result = text_result + result
		print(f"Sentence: {text_result}")

	assert result == "Correct!", f"{result}"


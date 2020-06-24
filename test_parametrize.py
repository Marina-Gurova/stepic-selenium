import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Answer for this task is message: The owls are not what they seem! OvO

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def calc():
    return str(math.log(int(time.time())))

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_answer(browser, link):
    browser.implicitly_wait(5)
    browser.get(link)
    field = browser.find_element_by_css_selector(".textarea")
    answer = calc()
    field.send_keys(answer)
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
    button.click()
    message = browser.find_element_by_css_selector("pre.smart-hints__hint")
    assert message.text == "Correct!", f"{message.text}"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
from math import log, sin

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn.btn-primary[id = 'book']")
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button.click()

    def calc(x):
        return str(log(abs(12*sin(x))))

    x_elem = browser.find_element_by_css_selector("span.nowrap[id = 'input_value']")
    x = int(x_elem.text)
    y = calc(x)
    field = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn.btn-primary[id = 'solve']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

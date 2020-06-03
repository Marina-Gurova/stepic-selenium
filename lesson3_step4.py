from selenium import webdriver
import time
import math
from math import log, sin
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(log(abs(12*sin(x))))

    x_elem = browser.find_element_by_css_selector("span.nowrap[id = 'input_value']")
    x = int(x_elem.text)
    y = calc(x)
    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    submit = browser.find_element_by_css_selector("button.btn.btn-primary")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

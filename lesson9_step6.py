import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    img_element = browser.find_element(By.ID, "input_value")
    x = int(img_element.text)
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    submit_button = browser.find_element(By.XPATH,
                                         "/html/body/form/div/div/button")
    submit_button.click()



finally:
    time.sleep(5)
    browser.quit()

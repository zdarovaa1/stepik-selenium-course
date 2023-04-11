import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element(By.ID, 'book')
    _ = button.location_once_scrolled_into_view
    button.click()

    img_element = browser.find_element(By.ID, "input_value")
    x = int(img_element.text)
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    submit_button = browser.find_element(By.XPATH,
                                         "/html/body/form/div/div/button")
    submit_button.click()




finally:
    time.sleep(60)
    browser.quit()

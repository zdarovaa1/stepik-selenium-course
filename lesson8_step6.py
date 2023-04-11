from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num = int(browser.find_element(By.ID, "input_value").text)
    answer = calc(num)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(answer)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    _ = radio_button.location_once_scrolled_into_view
    radio_button.click()

    button = browser.find_element(By.TAG_NAME, "button")
    _ = button.location_once_scrolled_into_view
    button.click()

finally:
    time.sleep(5)
    browser.quit()

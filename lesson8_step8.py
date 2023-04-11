import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("Petrov@gmail.com")

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.html')
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()



finally:
    time.sleep(5)
    browser.quit()

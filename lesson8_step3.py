from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    sum_of_nums = str(num1 + num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum_of_nums)

    submit_button = browser.find_element(By.TAG_NAME, "button")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()

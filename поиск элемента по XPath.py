from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")

    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

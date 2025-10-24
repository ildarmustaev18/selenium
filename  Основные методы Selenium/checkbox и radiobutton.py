from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/find_xpath_form"

try:
    option1 = browser.find_element(By.CSS_SELECTOR, "[value='python']")
    option1.click()
finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

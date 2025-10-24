from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")

    print(treasure.get_attribute("valuex"))

    x = math.log(math.fabs((12*math.sin(int(treasure.get_attribute("valuex"))))),10)
    print(x)


finally:
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

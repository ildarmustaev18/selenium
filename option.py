from sys import executable

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()

## chrome_options.add_argument("--headless") ##запуск в фоне
## chrome_options.add_argument("--incognito") ## инкогнито
##chrome_options.add_argument("--ignore-certificate-errors") ##игнор ошибок
## chrome_options.add_argument("--disable_cashe") ##  отключить кеш

service = Service(executable_path="")
driver = webdriver.Chrome(service=service, options = chrome_options)

# driver.set_window_size(700, 700)  # размер окна


driver.get("https://google.com")
##driver.get("https://expired.badssl.com")





time.sleep(10)



#driver.quit()

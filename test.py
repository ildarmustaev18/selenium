from sys import executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)

driver.get('https://www.saucedemo.com/v1')





time.sleep(10)

#driver.quit()

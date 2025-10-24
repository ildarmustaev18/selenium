from sys import executable

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/ru/ru/login")

time.sleep(3)
driver.find_element("id", "loginformsubmit").click()



time.sleep(10)



#driver.quit()

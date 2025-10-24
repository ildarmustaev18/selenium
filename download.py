import os
from sys import executable

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from strategy_to_load import chrome_options

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)

prefs = {
    "download.defaults_directory": f"{os.getcwd()}/downloads"
}
chrome_options.add_experimental_option("prefs", prefs)
driver.get("https://the-internet.herokuapp.com/download")

time.sleep(3)

driver.find_elements("xpath", "//a")[3].click()

#//input[@type="email"]

time.sleep(3)
#driver.quit()

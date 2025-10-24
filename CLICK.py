from sys import executable

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/pl")
login_button = driver.find_element("xpath", "//a[@id='login-desktop']")
login_button.click()


email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("HELLO")

print(email_field.get_attribute("value"))
print(email_field.get_attribute("maxlength"))





time.sleep(50)



#driver.quit()

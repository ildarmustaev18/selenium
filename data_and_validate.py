from sys import executable

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="")
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikipedia.org/")

url = driver.current_url
print("URL страницы: ", url)

assert url == "https://www.wikipedia.org/", "Ошибка в URL"
current_title = driver.title
print("Текущий заголовок:", current_title)

assert current_title == "Wikipedia", "Некорректный заголовок страницы"

print(driver.page_source)

email_field = driver.find_element("xpath", "//input[@id='searchInput']")
email_field.send_keys("ARMY")

time.sleep(5)



#driver.quit()

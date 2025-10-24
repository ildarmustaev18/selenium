from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
#value = browser.find_element(By.Class_Name, "input_value")
print(driver.find_element(By.Class_name, "input_value"))
#print(value)
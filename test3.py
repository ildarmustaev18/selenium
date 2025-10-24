from selenium import webdriver
from selenium.webdriver.common.by import BY [1](https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/)

browser = webdriver.Chrome()
browser.get("https://example.com/register")

# Найти элементы формы
first_name = browser.find_element(By.ID, "input-firstname")
first_name.send_keys("FirstName")

from re import X
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

x = browser.find_element(By.ID, "num1")
y = browser.find_element(By.ID, "num2")

x1= x.text
x2= y.text

sum = str(int(x1)+int(x2))


select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(value=sum)



button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)
browser.quit()

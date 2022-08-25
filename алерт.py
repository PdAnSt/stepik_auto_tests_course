from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

btn = browser.find_element(By.TAG_NAME, "button")
btn.click()

browser.switch_to.alert.accept()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x) 

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

browser.find_element(By.TAG_NAME, "button").click()

time.sleep(5)
browser.quit()
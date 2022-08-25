from tkinter import SW
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

btn = browser.find_element(By.TAG_NAME, "button")
btn.click()

new_window = browser.window_handles[1] 
browser.switch_to.window(new_window)

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x) 

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

browser.find_element(By.TAG_NAME, "button").click()

alert = browser.switch_to.alert()
alertt = alert.text
print(alert.text)
time.sleep(30)
browser.quit()
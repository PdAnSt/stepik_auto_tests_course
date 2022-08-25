from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

baza = browser.find_element(By.CSS_SELECTOR, "#treasure")
x = baza.get_attribute("checked")
y = calc(x)

inp = browser.find_element(By.CSS_SELECTOR, "#answer")
inp.send_keys(y)

browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
browser.find_element(By.CSS_SELECTOR, "button").click()

time.sleep(5)
browser.quit()
print(x)
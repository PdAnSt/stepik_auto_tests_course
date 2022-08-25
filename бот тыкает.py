from tkinter import BROWSE
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get(" https://suninjuly.github.io/math.html")

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

inp = browser.find_element(By.CSS_SELECTOR, "#answer")
inp.send_keys(y)

browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
browser.find_element(By.CSS_SELECTOR, "button").click()

time.sleep(5)
browser.quit()
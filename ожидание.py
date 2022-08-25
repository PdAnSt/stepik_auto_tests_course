from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

browser.find_element(By.ID, "book").click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x) 

input = browser.find_element(By.ID, "answer")
input.send_keys(y)

browser.find_element(By.ID, "solve").click()

time.sleep(5)
browser.quit()

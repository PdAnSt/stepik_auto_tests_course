from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.TAG_NAME, "input")
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')    
input3.send_keys("123@23.c")


current_dir = os.path.abspath(os.path.dirname(__file__))    
file_path = os.path.join(current_dir, 'file.txt')           

input11 = browser.find_element(By.ID, "file")

input11.send_keys(file_path)
   
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
browser.quit()

# не забываем оставить пустую строку в конце файла
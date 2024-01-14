
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# print(os.environ['login'])

browser = webdriver.Firefox()
browser.get('https://fedsfm.ru')
try:
   browser.find_element(By.CLASS_NAME, 'btn.btn-danger').click()
except:
   print("Can't find element")

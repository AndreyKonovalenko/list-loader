
import os
import time
from dotenv import load_dotenv 
from selenium import webdriver
from selenium.webdriver.common.by import By
load_dotenv()

login = os.environ['login']
password = os.environ['password']


browser = webdriver.Firefox()
browser.get('https://portal.fedsfm.ru/account/login')
try:
   # browser.find_element(By.CLASS_NAME, 'btn.btn-danger').click()
   loginInput = browser.find_element(By.ID, 'loginEditor')
   passwordInput = browser.find_element(By.ID, 'passwordEditor')
   loginInput.send_keys(login)
   passwordInput.send_keys(password)
   time.sleep(2)
   print(browser.current_url)
   browser.find_element(By.ID, 'loginButton').click()
   time.sleep(5)
   print(browser.current_url)
   browser.find_element(By.ID, 'e91ae743-b77c-45a7-b5d6-3444e8c60f86').click()
   time.sleep(2) 
   print(browser.current_url)  
   browser.find_element(By.ID, '8d0a3196-062d-4987-8ea0-90efddba53fc_anchor').click()
   print(browser.current_url)
   time.sleep(2)
   browser.find_element(By.XPATH, '//a[text()="Скачать"]').click()
except:
   print("Can't find element")

# time.sleep(5)
# browser.close()

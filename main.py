
import os
import time
from dotenv import load_dotenv 
from selenium import webdriver
from selenium.webdriver.common.by import By
load_dotenv()

elementIdList = ["e91ae743-b77c-45a7-b5d6-3444e8c60f86", "e91ae743-b77c-45a7-b5d6-3444e8c60f86", "8d0a3196-062d-4987-8ea0-90efddba53fc_anchor"]

login = os.environ['login']
password = os.environ['password']

maxDelay = 30
base_location = 'https://portal.fedsfm.ru/account/login'
browser = webdriver.Firefox()
browser.get(base_location)
current_location = browser.current_url

def clickByID(id):
      browser.find_element(By.ID, id).click()

def delay(current_location): 
     count = 0
     while(base_location == current_location):
         print(current_location)
         time.sleep(1)
         print('waiting')
         count += 1
         current_location = browser.current_url
         if count == maxDelay:
              break
         if base_location != current_location:
              base_location = current_location
              break              
def login():
   try:
      loginInput = browser.find_element(By.ID, 'loginEditor')
      passwordInput = browser.find_element(By.ID, 'passwordEditor')
      loginInput.send_keys(login)
      passwordInput.send_keys(password) 
      browser.find_element(By.ID, 'loginButton').click()
   except: 
        print("login failed!")
        browser.close()
        

login()
delay(base_location)

for id in elementIdList: 
      delay(base_location)
      clickByID(id)
      

# browser.find_element(By.XPATH, '//a[text()="Скачать"]').click()

# try:
#    # browser.find_element(By.CLASS_NAME, 'btn.btn-danger').click()
#    loginInput = browser.find_element(By.ID, 'loginEditor')
#    passwordInput = browser.find_element(By.ID, 'passwordEditor')
#    loginInput.send_keys(login)
#    passwordInput.send_keys(password) 
#    while (current_location == browser.current_url):
#       time.sleep(1)
#    else:
#       current_location = browser.current_location   
#    browser.find_element(By.ID, 'loginButton').click()
#    time.sleep(5)
#    print(browser.current_url)
#    browser.find_element(By.ID, 'e91ae743-b77c-45a7-b5d6-3444e8c60f86').click()
#    time.sleep(2) 
#    print(browser.current_url)  
#    browser.find_element(By.ID, '8d0a3196-062d-4987-8ea0-90efddba53fc_anchor').click()
#    print(browser.current_url)
#    time.sleep(2)
#    browser.find_element(By.XPATH, '//a[text()="Скачать"]').click()
# except:
#    print("Can't find element")

# time.sleep(5)
# browser.close()


import os
import sys
import time
from dotenv import load_dotenv 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

list_types = ('ter', "oon", "mvk")

if len(sys.argv) < 2:
    print('provide argrument with list type')
    exit()

if (sys.argv[1] in list_types) == False:
     print('Incorrect list type')
     exit()
    
load_dotenv()

elementIdList = ["e91ae743-b77c-45a7-b5d6-3444e8c60f86", "e91ae743-b77c-45a7-b5d6-3444e8c60f86"]

# "8d0a3196-062d-4987-8ea0-90efddba53fc_anchor"

login = os.environ['login']
password = os.environ['password']

maxDelay = 30
base_location = 'https://portal.fedsfm.ru/account/login'
browser = webdriver.Firefox()
browser.get(base_location)

current_location = browser.current_url

def delay_click(element: any) -> None:
      wait = WebDriverWait(browser, timeout=3)
      wait.until(lambda d : element.is_displayed())
      element.click()
     

def clickByID(id: str) -> None:
   try:
      element =  browser.find_element(By.ID, id)
      delay_click(element)   
   except:
      print(f'Element with id: {id} not found/')


def delay(base_location: str, current_location: str) -> None : 
     count = 0
     while(base_location == current_location):
         time.sleep(1)
         current_location = browser.current_url
         count += 1
         if count == maxDelay:
              print("maximum number of attempts reached")
              break
         if base_location != current_location:
              base_location = current_location
              break         


def loginHandler() -> None:
   try:
      loginInput = browser.find_element(By.ID, 'loginEditor')
      passwordInput = browser.find_element(By.ID, 'passwordEditor')
      loginInput.send_keys(login)
      passwordInput.send_keys(password) 
      loginButton = browser.find_element(By.ID, 'loginButton')
      delay_click(loginButton)
   except: 
      print("login failed!")
      browser.close()

def download() -> None:
      downloadLink = browser.find_element(By.XPATH, '//a[@href="/SkedDownload/GetActiveSked?type=xml21"]')
      delay_click(downloadLink)      

loginHandler()

delay(base_location, current_location)

for id in elementIdList: 
   delay(base_location, current_location)
   clickByID(id)

download()

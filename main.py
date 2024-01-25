
import os
import sys
import time
from dotenv import load_dotenv 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from browser_module import browser

url = 'https://portal.fedsfm.ru/account/login'


list_types = ('ter', "oon", "mvk")

load_dotenv()

login = os.environ['login']
password = os.environ['password']
formIdList = ['loginEditor', 'passwordEditor']
formInputs = [login, password]
elementIdList = ["e91ae743-b77c-45a7-b5d6-3444e8c60f86"]
browser.get(url)

current_location = browser.current_url

def wait_to_be_displayed(element: any) -> None:
      wait = WebDriverWait(browser, timeout=3)
      wait.until(lambda d : element.is_displayed())    

def clickByID(id: str) -> None:
   try:
      element =  browser.find_element(By.ID, id)
      wait_to_be_displayed(element)
      element.click()   
   except:
      print(f'Element with id: {id} not found/')

def loginHandler() -> None:
   try:
      for id in formIdList:
          element = browser.find_element(By.ID, id)
          wait_to_be_displayed(element)
          element.send_keys(formInputs[formIdList.index(id)])
      clickByID("loginButton")
   except: 
      print("login failed!")
      browser.close()

def download(listType) -> None:
      listHref = ''
      print(listType)
      if(listType == 'ter'):
          listHref = "/SkedDownload/GetActiveSked?type=xml21"
      if(listType == 'oon'):
         listHref = "/XmlCatalogDownload/GetActiveOONRus"
      if(listType == 'mvk'):
         listHref = "/XmlCatalogDownload/GetActiveMvk"
      downloadLink = browser.find_element(By.XPATH, f'//a[@href="{listHref}"]')
      wait_to_be_displayed(downloadLink) 
      downloadLink.click()   


if len(sys.argv) < 2:
    print('provide argrument with list type')
    loginHandler()
    exit()

if (sys.argv[1] in list_types) == False:
     print('Incorrect list type')
     exit()
    


loginHandler()
time.sleep(5)
clickByID(elementIdList[0])
time.sleep(5)
download(sys.argv[1])
time.sleep(10)
browser.close()



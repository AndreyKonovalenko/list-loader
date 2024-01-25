import os 
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from dotenv import load_dotenv
load_dotenv()
directory = os.environ['directory']
print(directory)

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", directory)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

browser = webdriver.Firefox(options=options)
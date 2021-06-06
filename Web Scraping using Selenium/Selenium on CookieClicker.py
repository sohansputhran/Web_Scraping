from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'D:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://orteil.dashnet.org/cookieclicker/')
print(driver.title)
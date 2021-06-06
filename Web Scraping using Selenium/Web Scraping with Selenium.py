# Selenium Tutorial
# Learning from YouTube video: https://www.youtube.com/watch?v=Xjv1sY630Uc

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = 'D:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
print(driver.title)

search = driver.find_element_by_name('s')
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()
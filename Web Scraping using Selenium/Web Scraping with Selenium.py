# Selenium Tutorial
# Learning from YouTube video: https://www.youtube.com/watch?v=Xjv1sY630Uc

from selenium import webdriver

PATH = 'D:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
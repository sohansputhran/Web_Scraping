# Selenium Tutorial
# Learning from YouTube video: https://www.youtube.com/watch?v=Xjv1sY630Uc

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# For waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'D:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
print(driver.title)

search = driver.find_element_by_name('s')
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    print(main.text)
except:
    driver.quit()

driver.quit()
# Selenium Tutorial
# Learning from YouTube video: https://www.youtube.com/watch?v=Xjv1sY630Uc

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# For explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'D:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
print(driver.title)

# Read some contents from the website using tag-names and class names
# search = driver.find_element_

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )
#     # print(main.text)
#     articles = main.find_elements_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry-summary")
#         print(header.text)
# except:
#     driver.quit()

# Click a link
link = driver.find_element_by_link_text('Python Programming')
link.click()

# Wait for 10 sec for the link to be loaded
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-1931003"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
except:
    driver.quit()

driver.quit()
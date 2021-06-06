from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'D:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://orteil.dashnet.org/cookieclicker/')

# Implicit wait
driver.implicitly_wait(5)

cookie = driver.find_element_by_id('bigCookie')
big_cookie = driver.find_element_by_id('cookies')
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
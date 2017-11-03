from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

fp = webdriver.FirefoxProfile('/home/pandey/.mozilla/firefox/mwad0hks.default')
driver = webdriver.Firefox(firefox_profile=fp)

driver.get("https://tinder.com/")

time.sleep(10)

for i in range(1,80):
    driver.find_element_by_class_name('recsGamepad__button--like').click()
    time.sleep(5)

driver.close()





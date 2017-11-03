from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

fp = webdriver.FirefoxProfile('/home/pandey/.mozilla/firefox/mwad0hks.default')
driver = webdriver.Firefox(firefox_profile=fp)

driver.get("https://satendrapandeymp.wordpress.com/")

time.sleep(10)

videos = driver.find_elements_by_class_name('youtube-player')

for video in videos:
    video.click()
    time.sleep(100)
    video.click()

driver.close()





from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

fp = webdriver.FirefoxProfile('/home/pandey/.mozilla/firefox/mwad0hks.default')
driver = webdriver.Firefox(firefox_profile=fp)

driver.get("https://www.youtube.com")

time.sleep(10)

elem = driver.find_element_by_name('search_query')
elem.clear()
elem.send_keys("How to make PDF reader in Python using GTTS or pyttsx")
elem.send_keys(Keys.RETURN)

time.sleep(10)

for i in range(1,5):
    driver.find_elements_by_id('video-title')[i].click()
    for j in range(1,14):
        time.sleep(20)
        player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
        if player_status == 0:
            break

time.sleep(100)

driver.close()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, sys, socket

socket.setdefaulttimeout(60)
reload(sys)
sys.setdefaultencoding("utf-8")

fp = webdriver.FirefoxProfile('/home/pandey/.mozilla/firefox/mwad0hks.default')
driver = webdriver.Firefox(firefox_profile=fp)

contact = open('test.txt', 'wb')

for i in range(400):
    driver.get("https://www.facebook.com/satendrapandeymp/friends")
    time.sleep(1)

    for j in range((i+1)/20):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    frd = driver.find_elements_by_class_name('_5q6s._8o._8t.lfloat._ohe')
    if len(frd) <= i :
        continue

    friend = frd[i]
    friend.click()
    time.sleep(2)

    check = driver.find_elements_by_class_name('_5q6s._8o._8t.lfloat._ohe')
    if len(check) > 0:
        continue

    driver.find_elements_by_class_name('_6-6')[1].click()
    time.sleep(2)

    details = driver.find_elements_by_class_name('_c24._50f3')
    if len(details) < 1:
        continue

    number = details[0].text

    if 'Phone' in number:
        number = number.replace('\n',' , ')
        number = number.split('hones , ')[1]
        name = driver.find_element_by_id('fb-timeline-cover-name').text
        name = name.replace('\n',' ')
        print name, number
        contact.write(name + ' -- ' + number + '\n')
    time.sleep(1)

contact.close()

driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('./chromedriver', options=options)
driver.set_window_size(1920, 1080)
driver.implicitly_wait(10)
driver.get('https://ktis.kookmin.ac.kr/')

login_id = driver.find_element_by_id("txt_user_id").send_keys("20150084")
time.sleep(1)



login_pw = driver.find_element_by_id("txt_passwd").send_keys("rnralseo15^^")
time.sleep(1)
login_pw.send_keys(Keys.RETURN)

time.sleep(10)

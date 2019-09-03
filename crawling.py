import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

# 브라우저 사이즈를 조절합니다.
driver.set_window_size(1920, 1080)

driver.implicitly_wait(10)

# driver.get('주소') : 해당 주소로 이동
driver.get('https://www.naver.com/')

searchbar = driver.find_element_by_css_selector("#account > div > a > i")
searchbar.click()

login_id = driver.find_element_by_id("id")
login_id.send_keys("gus2dnjf3dlf")
login_id.send_keys(Keys.RETURN)

login_pw = driver.find_element_by_id("pw")
login_pw.send_keys("Rnralseo15^^")
login_pw.send_keys(Keys.RETURN)

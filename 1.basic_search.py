# Selenium 의 자세한 사용 방법은 아래 주소를 참조
# https://selenium-python.readthedocs.io

# Python의 selenium 모듈을 별도로 설치해야 합니다.
# Windows: pip install selenium
# Mac: pip3 install selenium

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 크롬 자동화를 가능하게 해주는 크롬드라이버의 경로
# OS에 맞게 크롬 드라이버 설치: http://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('./chromedriver')

# 브라우저 사이즈를 조절합니다.
driver.set_window_size(1920, 1080)

# 웹 페이지 로딩이 길어질 경우, 최대 기다리는 시간
# 10초가 지나면 에러가 발생하며 종료
driver.implicitly_wait(10)


# driver.get('주소') : 해당 주소로 이동
driver.get('https://www.naver.com')

# 실행이 너무 빨라서 우리가 볼 수 있게끔 단계별로 3초씩 쉽니다.
# 실제 프로젝트에서는 사용하지 않으셔도 됩니다 :)
time.sleep(3)

# 자세한 내용은 링크 참조
# https://selenium-python.readthedocs.io/locating-elements.html
# 
# find_element_by_id *
# find_element_by_name
# find_element_by_link_text *
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector *
searchbar = driver.find_element_by_id("query")
print(searchbar.get_attribute('title'))

# 실행이 너무 빨라서 우리가 볼 수 있게끔 단계별로 3초씩 쉽니다.
# 실제 프로젝트에서는 사용하지 않으셔도 됩니다 :)
time.sleep(3)

# 검색창에 미세먼지라 입력합니다.
searchbar.send_keys("미세먼지")

# 실행이 너무 빨라서 우리가 볼 수 있게끔 단계별로 3초씩 쉽니다.
# 실제 프로젝트에서는 사용하지 않으셔도 됩니다 :)
time.sleep(3)

# 자세한 내용은 링크 참조
# https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html?highlight=keys#selenium.webdriver.common.keys
# 검색창에서 엔터를 칩니다.
searchbar.send_keys(Keys.RETURN)

# 실행이 너무 빨라서 우리가 볼 수 있게끔 단계별로 3초씩 쉽니다.
# 실제 프로젝트에서는 사용하지 않으셔도 됩니다 :)
time.sleep(3)

# 스크린샷을 찍습니다.
driver.save_screenshot('./screenshot.png')

# 브라우저 종료
driver.quit()
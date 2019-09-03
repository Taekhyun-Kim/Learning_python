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
searchbar = driver.find_element_by_id("query")

# 실행이 너무 빨라서 우리가 볼 수 있게끔 단계별로 3초씩 쉽니다.
# 실제 프로젝트에서는 사용하지 않으셔도 됩니다 :)
time.sleep(3)

# 검색창에 미세먼지라 입력합니다.
searchbar.send_keys("미세먼지")

time.sleep(3)

# 자세한 내용은 링크 참조
# https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html?highlight=keys#selenium.webdriver.common.keys
# 검색창에서 엔터를 칩니다.
searchbar.send_keys(Keys.RETURN)

time.sleep(3)

# 링크 중에서 "실시간검색" 이라는 텍스트를 가진 링크를 찾습니다.
realtime_search_link = driver.find_element_by_link_text("실시간검색")
# 찾은 그 링크를 마우스로 클릭합니다.
realtime_search_link.click()

time.sleep(3)


# 화면 제일 아래로 스크롤합니다.
# https://selenium-python.readthedocs.io/faq.html#how-to-scroll-down-to-the-bottom-of-a-page
# JavaScript 코드를 실행시켜주는 함수인데, JS를 모르기 때문에 이건 그냥 이렇게 쓰는 거구나 합니다.
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

# 클래스 이름을 활용해서 더보기 버튼을 찾습니다.
more_button = driver.find_element_by_class_name("_moreBtn")
# 더보기 버튼을 클릭합니다.
more_button.click()
# 로딩 될 때까지 기다립니다.
time.sleep(3)

# 아래로 스크롤, 더보기 버튼 클릭, 로딩 대기 를 반복합니다.

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
more_button = driver.find_element_by_class_name("_moreBtn")
more_button.click()
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
more_button = driver.find_element_by_class_name("_moreBtn")
more_button.click()
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
more_button = driver.find_element_by_class_name("_moreBtn")
more_button.click()
time.sleep(3)


# driver.find_element"s" 입니다.
# 클래스 이름을 활용해 해당 클래스를 가진 모든 요소를 수집합니다.
text_links = driver.find_elements_by_class_name("txt_link")
print(text_links)


# 브라우저 종료
driver.quit()
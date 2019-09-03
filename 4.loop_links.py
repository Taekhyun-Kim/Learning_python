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

# 자세한 내용은 링크 참조
# https://selenium-python.readthedocs.io/locating-elements.html
searchbar = driver.find_element_by_id("query")

# 검색창에 미세먼지라 입력합니다.
searchbar.send_keys("미세먼지")

# 자세한 내용은 링크 참조
# https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html?highlight=keys#selenium.webdriver.common.keys
# 검색창에서 엔터를 칩니다.
searchbar.send_keys(Keys.RETURN)

# 링크 중에서 "실시간검색" 이라는 텍스트를 가진 링크를 찾습니다.
realtime_search_link = driver.find_element_by_link_text("실시간검색")
# 찾은 그 링크를 마우스로 클릭합니다.
realtime_search_link.click()

time.sleep(3)

# 화면 제일 아래로 스크롤합니다.
# 반복문으로 중복되는 스크롤 코드를 깔끔하게 해결합니다.
for index in range(3):
    print(f"{index + 1} 번 째 시도입니다.")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    more_button = driver.find_element_by_class_name("_moreBtn")
    more_button.click()
    time.sleep(3)


# driver.find_element"s" 입니다.
# 클래스 이름을 활용해 해당 클래스를 가진 모든 요소를 수집합니다.
text_links = driver.find_elements_by_class_name("txt_link")

analyzed_text_list = []
url_text_dict = {}

for link in text_links:
    url = link.get_attribute('href')
    text = link.text

    # 텍스트를 가지고 일련의 처리를 한 다음에 리스트에 넣어서 수집할 수 있습니다.
    #   DO_SOMETHING
    analyzed_text_list.append(text)

    # {"URL": "텍스트"} 이렇게 정리해서 저장하고 싶다면 Dictionary를 활용!
    url_text_dict[url] = text


print(analyzed_text_list)
print(url_text_dict)

# 브라우저 종료
driver.quit()

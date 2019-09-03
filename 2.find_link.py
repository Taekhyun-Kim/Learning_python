# Selenium 의 자세한 사용 방법은 아래 주소를 참조
# https://selenium-python.readthedocs.io

# Python의 selenium 모듈을 별도로 설치해야 합니다.
# Windows: pip install selenium
# Mac: pip3 install selenium

import time
import requests  # facebook에 전달해줄 requests 모듈 사용 (get / post)

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
# time.sleep(3)

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
# time.sleep(3)

# 검색창에 미세먼지라 입력합니다.
searchbar.send_keys("미세먼지")

# 실행이 너무 빨라서 우리가 볼 수 있게끔 단계별로 3초씩 쉽니다.
# 실제 프로젝트에서는 사용하지 않으셔도 됩니다 :)
# time.sleep(3)

# 자세한 내용은 링크 참조
# https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html?highlight=keys#selenium.webdriver.common.keys
# 검색창에서 엔터를 칩니다.
searchbar.send_keys(Keys.RETURN)

# 실행이 너무 빨라서 우리가 볼 수 있게끔 단계별로 3초씩 쉽니다.
# 실제 프로젝트에서는 사용하지 않으셔도 됩니다 :)
# time.sleep(3)

# 링크 중에서 "실시간검색" 이라는 텍스트를 가진 링크를 찾습니다.
realtime_search_link = driver.find_element_by_link_text("실시간검색")
# 찾은 그 링크를 마우스로 클릭합니다.
# realtime_search_link.click()
# print(realtime_search_link.text)


ACCESS_TOKEN = "EAAV7iZB1SMcEBAC5wxpkrTzR7KPFKIeHOgyNPBaMyWQwsYTiMjydP0vCggZChNAaq0r6r6hXJemOqKW1hQaRGjxS2B7llighrwy7R01bxKdsGOizZC7RFjeXTjJBOxTtgcRZAm4ALslrImEP7s9WbuyE8lNbKdUN9Ks2M98FawZDZD"
sender_id = 2561858357221446  # 이건 여러분하고 저랑 달라요
message = realtime_search_link.text

request_body = {
    "messaging_type": "RESPONSE",
    "recipient": {
        "id": sender_id
    },
    "message": {
        "text": f"크롤링 결과: {message}",
        "attachment": {
            "type": "image",
            "payload": {
                "url": "./0.jpg",
                "is_reusable": True,
            }
        }
    }
}

res = requests.post(
    url=f"https://graph.facebook.com/v3.2/me/messages?access_token={ACCESS_TOKEN}",
    json=request_body
)


# 실행이 너무 빨라서 우리가 볼 수 있게끔 단계별로 3초씩 쉽니다.
# 실제 프로젝트에서는 사용하지 않으셔도 됩니다 :)
# time.sleep(3)


# 브라우저 종료
driver.quit()

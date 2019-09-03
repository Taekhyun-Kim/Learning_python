import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

driver = webdriver.Chrome('./chromedriver')
driver.set_window_size(1920, 1080)

driver.implicitly_wait(10)

driver.get('https://www.naver.com')

searchbar = driver.find_element_by_id("query")
searchbar.send_keys("나라")
searchbar.send_keys(Keys.RETURN)

realtime_search_link = driver.find_element_by_link_text("이미지")
realtime_search_link.click()

images = driver.find_elements_by_css_selector('a.thumb._thumb > img')

# 기본 링크 출력
# for image in images:
#     print(image.get_attribute('src'))

# enumerate 는 순서가 존재하는 콜렉션 데이터를,
# 순서를 나타내는 인덱스와 함께 사용할 수 있게 해줍니다.
for index, image in enumerate(images):
    image_url = image.get_attribute('src')

    raw_image_url = image_url.split('&')[0]

    image_format = raw_image_url.split('.')[-1]

    if image_format != "jpg" and image_format != "png":
        image_format = 'jpg'

    # requests 모듈을 활용해 이미지를 GET 방식으로 요청하기
    response = requests.get(raw_image_url)
    # "wb" 모드는 이미지나 영상과 같은 바이너리 파일을 저장할 때 사용
    # 아래 코드에서는 images 폴더에 저장하기 때문에 사전에 images 폴더가 존재해야 함
    open(f"./images/{index}.{image_format}", "wb").write(response.content)

time.sleep(3)

driver.quit()

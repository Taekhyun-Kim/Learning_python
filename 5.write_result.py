import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

driver.set_window_size(1920, 1080)
driver.implicitly_wait(10)

driver.get('https://www.naver.com')
searchbar = driver.find_element_by_id("query")

searchbar.send_keys("미세먼지")
searchbar.send_keys(Keys.RETURN)

realtime_search_link = driver.find_element_by_link_text("실시간검색")
realtime_search_link.click()

time.sleep(3)

for index in range(3):
    print(f"{index + 1} 번 째 시도입니다.")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    more_button = driver.find_element_by_class_name("_moreBtn")
    more_button.click()
    time.sleep(3)

text_links = driver.find_elements_by_class_name("txt_link")


# 새롭게 만든 파일을 엽니다.
my_file = open("./result.txt", 'w', encoding='UTF8')

for link in text_links:
    url = link.get_attribute('href')
    text = link.text

    # 텍스트를 가지고 일련의 처리를 한 다음에 리스트에 넣어서 수집할 수 있습니다.
    #   DO_SOMETHING

    # 파일에 한 줄씩 입력
    my_file.write(text + "\n")

# 파일을 닫아줘야 합니다.
my_file.close()


# 브라우저 종료
driver.quit()
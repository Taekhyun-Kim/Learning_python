import time

# 해시태그를 분석하기 위한 Twitter 모듈
from konlpy.tag import Twitter

# 크롬 브라우저 조작을 위한 모듈
from selenium import webdriver

# 페이지 스크롤링을 위한 모듈
from selenium.webdriver.common.keys import Keys

from konlpy.tag import Kkma
kkma = Kkma()

# 맛집 장소를 입력받습니다
keyword = input(" 검색하고 싶은 해시태그를 적어주세요! ")

# 크롬 자동화를 가능하게 해주는 크롬드라이버의 경로
driver = webdriver.Chrome('./chromedriver')

# 브라우저 사이즈를 조절합니다.
driver.set_window_size(1920, 1080)

# 웹 페이지 로딩이 길어질 경우, 최대 기다리는 시간
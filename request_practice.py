import requests

data = requests.get("https://www.naver.com")
print(data.text)

# index.html을 받아올거야. 웹 크롤링의 전통적인 방법
# beautifulsoup 추가적인 데이터를 가져올 수 없을 뿐더러 1차원적인 데이터만 가져올 수 있다. 
# 모던화된 사이트는 html 소스코드에는 한글이 없다. 처음에는 안 담겨지다가 나중에 담겨진다.
# 셀레니움을 이용하면 추가적인 데이터도 크롤링을 할 수 있다.
# selenium documentation python
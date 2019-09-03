# 로또 추첨기
from random import choice, randint
for i in range(7):
    print(f"로또 추첨 중! {i+1}번째 번호 : {randint(1, 45)}")

# 어떻게 하면 중복을 막을 수 있을까? 
secret_number = 9
# else는 아무것도 해당되지 않을 때 이걸 실행해
if secret_number == 7 or secret_number == 9 :
    print('딩 동 댕 !')
elif secret_number == 8 :
    print('딩 동 댕 동 !')
else:
    print('땡 !')

hungry = True
cold = True
tired = True

if hungry and cold and tired:
    print("배고픈 소크라테스가 돼지보다 나을까?")
else:
    print("아닝!")

# 반복문 - while문
number = 1
# 강제로 서버를 끄고 싶을 떄 ctrl + C
while number < 5:
    print("5보다 작다!")
    number = number + 1

number = 1

while number < 5:
    if number == 3:
        break
    print("5보다 작다!")
    number = number + 1
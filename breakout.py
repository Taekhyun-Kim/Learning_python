while True:
    secret_number = int(input("비밀번호를 입력해주세요: "))
    if secret_number == 712 :
        print("탈출 성공!")
        break
    else :
        print("택현의 생일을 입력해주세요.")

# 복습
# while문과 if문은 제어문 input함수 사용자로부터 내용을 받아서 변수로 사용할 수 있다.
# parameter를 설정할 수 있으나 갯수를 맞춰야한다.
# input은 문자열이기 때문에 숫자를 입력하려면 int로 바꿔줘야한다!
# 함수 잘 쓰면 30줄 짜리가 된다! 순환문 잘 쓰면 3~4줄에 끝난다!
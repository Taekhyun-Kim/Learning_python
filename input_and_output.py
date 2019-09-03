#사용자와 대화할 수 있는 프로그램. 
GPA = input("성적을 입력해주세요: ")
GPA_to_integer = int(GPA)

# 점수를 비교하는 if 문쓰기

if GPA_to_integer >= 90 :
    print("A 입니다.")
elif GPA_to_integer < 90 and GPA_to_integer >= 80 :
    print("B 입니다.")
elif GPA_to_integer < 80 and GPA_to_integer >= 70 :
    print("C 입니다.")
elif GPA_to_integer < 70 and GPA_to_integer >= 60 :
    print("D 입니다.")
else :
    print("1등이 아니면 기억하지 않는 더러운 세상")

# 특정 숫자를 정해놓는 for 반복문 함수
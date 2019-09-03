# 변수가 들어가는 부분입니다.
name = "택현"
age = "24"

print("=" * 50)
# formatted string이라는 뜻입니다. (python 3.6 이상부터 가능)
print(f"안녕! 나는 {name} {age}세")
print("=" * 50)

def Taekhyun_Hello():
    name = "택현"
    age = 24

    print("=" * 50)
    print(f"안녕! 나는 {name} {age}세야")
    print("=" * 50)

Taekhyun_Hello()
Taekhyun_Hello()

# parameter를 설정해서 함수만들기(name, age)
def greeting(name, age):
    print("=" * 50)
    print(f"안녕! 나는 {name} {age}세야")
    print("=" * 50)

greeting("택현", 24)
greeting(name = "철수", age = 28)

# 몇년생인지 구하는 함수 
def born_year (age) :
    current_year = 2019
    answer = current_year - age +1
    print(answer)
born_year(26)

# return문
def born_year (age) :
    current_year = 2019
    answer = current_year - age +1
    return answer

Taekhyun = born_year(27)
Dahyun = born_year(20)

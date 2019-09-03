people = ["희재", "상우", "채영", "택현"]

#   이건맘대로  리스트
for person in people :
    print(f"{person}님 안녕하세요!")  #f스트링으로 따옴표 없이!

# range(10)은 [0,1,2...9] 같은 리스트 아닌 리스트를 줍니다. 
for i in range(10):
    print(f"{i}번째 야호!") #변수를 따로 설정 안해도 된다. for _ in range(10) : 처럼

profile = {
    'name' : '운장',
    'age' : 26,
    'hobby' : 'sleep'}

for key in profile.keys():
    # ['name', 'age', 'hobby'] 같은 겁니다.
    print(key * 5)

for key in profile.keys():
    print(profile[key])

for key, value in profile.items():
    print(f"{key}가 {value}를 가리킵니다") 

# 점프투파이썬이 친절합니다. (추천추천) #공홈은 어려워요
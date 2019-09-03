# key-value 쌍을 담는 Dictionary
# 딕셔너리는 리스트와 비슷하지만, key-value 쌍을 씁니다.

profile = {
    'name' : '운장',
    'age' : 26,
    'hobby' : 'sleep'
}
print('딕셔너리', profile)

#접근은 key값으로 합니다. 
print('name 키에 접근', profile['name'])
# 수정도 가능합니다.
profile['age'] = 28
print('수정 후', profile)

#key 값이 없다면 접근에는 실패하지만, 값을 넣어주면 새로운 쌍을 만들어줍니다.
profile['occu'] = 'LikeLion'
print("추가 후", profile)

# 이건 에러가 나겠죠?
# print(profile['asdasdasd'])

# 에러가 나지 않게 접근하는 방법이 있습니다.
print(profile.get('asdasdasd')) # 없으면 None을 반환
print(profile.get('name'))
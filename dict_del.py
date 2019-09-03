profile = {
    'name' : '운장',
    'age' : 26,
    'hobby' : 'sleep'}

print("삭제 전", profile)
#약간 모양새가 다른데, 어쩔수 없다
del profile['age']

print('삭제 후', profile)
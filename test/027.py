# 문제 027 : 딕셔너리 만들기

name = input().split(' ')
score = list(input().split(' '))

result = dict(zip(name, score))
print(result)

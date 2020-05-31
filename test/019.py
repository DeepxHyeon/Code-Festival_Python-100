# 문제 019 : 제곱을 구하자

num = input().split(' ')
l = []
for i in num:
    l.append(int(i))
result = (l[0] ** l[1])
print(result)
# 문제 020 : 몫과 나머지

num = input().split(' ')
l = []
for i in num:
    l.append(int(i))
print(l[0] // l[1], l[0] % l[1])
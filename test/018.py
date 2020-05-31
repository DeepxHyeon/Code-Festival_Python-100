# 문제 018 : 평균 점수

score = input().split(' ')
l = []
for i in score:
    l.append(int(i))
avg = sum(l) // len(l)
print(avg)
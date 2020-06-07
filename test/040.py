# 문제 040 : 놀이동산에 가자

total = 0
count = 0
limit = int(input())
n = int(input())

for i in range(n):
    friend = int(input())
    if total <= limit:
        total += friend
        count = i
print(count)
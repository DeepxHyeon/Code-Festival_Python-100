# 문제 034 : sort 구현하기

input = input()
data = list(input.split())
result = []
for i in data:
    result.append(i)

if result != sorted(result):
    print("NO")
else:
    print("YES")
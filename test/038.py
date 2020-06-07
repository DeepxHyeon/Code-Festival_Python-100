# 문제 038 : 호준이의 아르바이트

input = input().split()
result = []
for i in input:
    result.append(int(i))
count = 0
for i in range(3):
    top = max(result)
    count += result.count(top)
    for j in range(result.count(top)):
        result.remove(top)
print(count)

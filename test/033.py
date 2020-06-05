# 문제 033 : 거꾸로 출력하기

input = input()
data = list(input.split())
result = []
for i in data:
    result.append(int(i))
for x in range(len(result)-1, -1, -1):
    print(result[x], end = ' ')
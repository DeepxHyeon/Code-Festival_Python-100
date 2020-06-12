# 문제 043 : 10진수를 2진수로

input = int(input())
result = []
while input:
    result.append(str(input % 2))
    input = int(input / 2)
result.reverse()
print(int(''.join(result)))
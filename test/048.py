# 문제 048 : 대소문자 바꿔서 출력하기

input = input()
result = []
for i in input:
    if i.islower():
        result.append(i.upper())
    elif i.isupper():
        result.append(i.lower())
print(''.join(result))
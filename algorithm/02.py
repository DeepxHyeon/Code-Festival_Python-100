'''
문제 접근 방법
1. 반복문의 경우는 Bottom-up (작은 문제에서 출발)
2. 재귀의 경우는 Top-down (큰 문제에서 출발)
'''

x = 0
for i in range(1, 11):
    x += i
print(x)

def f(n):
    if n <= 1:
        return 1
    else:
        return n + f(n-1)
print(f(10))

# while True:
#     if input('##') == 'exit':
#         break
#     if input('##') == 'hi':
#         print('hello world')
#     else:
#         continue

# def console():
#     if input('##') == 'exit':
#         break
#     if input('##') == 'hi':
#         print('hello world')
#     console()
# console()

# 2진수 구하기 - 반복문
x = int(input('2진수로 바꿀 숫자를 입력하세요:'))
result = ''
while True:
    if x % 2 == 0:
        result += '0'
    else:
        result += '1'
    x = x // 2
    if x == 1:
        result += str(x)
        print(result[::-1])
        break

def 이진수구하기(입력값):
    if 입력값 < 2:
        return str(입력값)
    else:
        return str(이진수구하기(입력값//2)) + str(입력값%2)

print(이진수구하기(11))

'''
이진수구하기(11) > str(이진수구하기(5) + str(1) > 1011 
이진수구하기(5) > str(이진수구하기(2) + str(1) > 101
이진수구하기(2) > str(이진수구하기(1) + str(0) > 10
이진수구하기(1) > 1
'''

def 문자열뒤집기(문자열):
    if 문자열 == '':
        return None
    else:
        문자열뒤집기(문자열[1:])
        print(문자열[0])
print(문자열뒤집기('loopy'))

result = ''
for i in 'loopy':
    result = i + result
print(result)

x = 0
for i in '2231':
    x += int(i)
print(x)

def 문자열뒤집기(문자열):
    if 문자열 == '':
        return 0
    else:
        return int(문자열[0]) + int(문자열뒤집기(문자열[1:]))
print(문자열뒤집기('2211'))
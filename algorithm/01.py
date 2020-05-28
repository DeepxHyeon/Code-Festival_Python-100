'''
재귀함수
내가 나를 호출하는 방법
반복문 <-> 재귀함수
'''

x = 0
n = 100
for i in range(1, n+1):
    x += i
print(x)

# 시그마 공식 : n*(n+1)//2
x = 0
n = 100
x = n*(n+1)//2
print(x)

print('-----')

def f(n):
    if n <= 1:
        return 1
    else:
        return n + f(n-1)
n = 100
print(f(n))

print('-----')

'''
팩토리얼
5! = 5 * 4 * 3 * 2 * 1 = 120
4! = 4 * 3 * 2 * 1 = 24
'''

x = 1
n = 5
for i in range(1, n+1):
    x *= i
print (x)


def 숫자세기(숫자):
    if 숫자 <= 0:
        print('끝!')
    else:
        print(숫자)
        return 숫자세기(숫자-1)
숫자세기(10)

print('-----')

# 피보나치
# 0 1 1 2 3 5 8 13 21
a = 0
b = 1
print(a)
for i in range(10):
    print(b)
    a, b = b, a+b

print('-----')

#f(n) = f(n-1) + f(n-2)
def 피보나치(숫자):
    if 숫자 == 0 or 숫자 == 1:
        return 1
    return 피보나치(숫자-1)+피보나치(숫자-2)
print(피보나치(5))
print(피보나치(6))
print(피보나치(7))
print(피보나치(8))

print('-----')

def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)
print(f(5))

print('-----')

s = 0
for i in [100, 200, 300, 400]:
    s += i
print(s)

def s(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + s(l[1:])
print(s([100, 200, 300, 400]))

print('-----')

print(2**6)

result = 1
for i in range(6):
    result *= 2
print(result)

def f(n, e):
    result = 1
    for i in range(e):
        result *= n
    return result
print(f(2, 6))

def f(n, e):
    if e == 1:
        return n
    else:
        return n * f(n, e-1)
print(f(2, 6))

print('-----')

def comma(s):
    if len(s) < 3:
        return s
    else:
        return comma(s[:len(s)-3]) + ',' + s[len(s)-3:]
print(comma('10000000'))

n = 99999999999
n = format(n, ',')
print(n)
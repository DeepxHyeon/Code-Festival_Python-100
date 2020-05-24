# 재귀함수

def f(n):
    if n > 1:
        return n * f(n-1)
    else:
        return 1

print(f(5))

'''
f(5) 4*24
f(4) 4*6
f(3) 3*2
f(2) 2*1
f(1) 1
'''
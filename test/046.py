# 문제 046 : str 자료형의 응용

n = 0
for i in list(range(21)):
    for j in str(i):
        n += int(j)
print(n)
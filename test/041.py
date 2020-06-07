# 문제 041 : 소수판별

input = int(input())
ch = True
for i in range(2, input):
    if input % i == 0:
        ch = False
if ch == True:
    print("YES")
else:
    print("NO")
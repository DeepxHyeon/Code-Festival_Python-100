# 문제 010 : 별 찍기

input = int(input())
for i in range(1, input+1):
    print(' ' *(input-i) + '*'*(2*i-1))
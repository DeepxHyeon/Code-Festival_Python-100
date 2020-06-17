# 문제 054 : 연속되는 수

input = input()
input = list(map(int, input.split(' ')))

def result(l):
    l = sorted(l)
    for i in range(len(l) - 1):
        if l[i]+1 != l[i+1]:
            return 'NO'
    return 'YES'

print(result(input))
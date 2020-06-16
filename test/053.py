# 문제 053 : 괄호 문자열

def 괄호체크(s):
    if s.count('(') != s.count(')'):
        return 'NO'
    괄호 = []
    for i in s:
        if i == '(':
            괄호.append('(')
        if i == ')':
            if len(괄호) == 0:
                return 'NO'
            괄호.pop()
    return 'YES'

input = input()
print(괄호체크(input))
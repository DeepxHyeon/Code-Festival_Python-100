# 문제 029 : 대문자만 지나가세요

input = input()
if ord(input) >= 65 and ord(input) <= 90:
    print("YES")
else:
    print("NO")
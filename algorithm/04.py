# 선택정렬
입력값 = [5, 10, 66, 77, 54, 32, 11, 15]
정렬된리스트 = []

while 입력값:
    정렬된리스트.append(min(입력값))
    입력값.pop(입력값.index(min(입력값)))
    print(정렬된리스트)
    print(입력값)
    print('-----')
print('최종값')
print(정렬된리스트)
print(입력값)

print('-----')

입력값 = [5, 10, 66, 77, 1, 54, 32, 11, 15, 2]
def 최소값(l):
    최소 = l[0]
    count = 0
    for i in l:
        if 최소 > i:
            최소 = i
            index = count
        count += 1
    return index
print(최소값(입력값))

print('-----')

입력값 = [5, 10, 66, 77, 1, 54, 32, 11, 15, 2]
def 최소값_인덱스(l):
    비교값 = l[0]
    for i in range(len(l)):
        if l[i] > 비교값:
            인덱스 = i
    return 인덱스
print(최소값(입력값))
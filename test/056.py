# 문제 056 : 리스트의 함수 응용

nationWidth = {
    'Korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England': 242900 }

koreaWidth = nationWidth['Korea']
nationWidth.pop('Korea')
l = list(nationWidth.items())
gap = max(nationWidth.values())
for i in l:
    if gap > abs(i[1] - koreaWidth):
        gap = abs(i[1] - koreaWidth)
        item = i
print(item[0], gap)

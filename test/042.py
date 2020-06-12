# 문제 042 : 2020년(datetime 모듈 사용)

import datetime

m = int(input())
d = int(input())
def findDay(a, b):
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return day[datetime.date(2020, a, b).weekday()]
print(findDay(m, d))
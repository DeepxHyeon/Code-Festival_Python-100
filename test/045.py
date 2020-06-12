# 문제 045 : time함수 사용하기

import time

t = time.time()
print(int(t//(365*24*3600)+1970))
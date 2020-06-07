# 문제 037 : count 사용하기 

input = input().split()
for i in range(1, len(input)):
    if input.count(input[i-1]) < input.count(input[i]):
        count = i
print(f"{input[count]}(이)가 총 {input.count(input[count])}표로 반장이 되었습니다.")
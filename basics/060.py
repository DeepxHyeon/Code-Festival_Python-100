# max, min, sum

x = [100, 200, 300, 400]

print(max(x))
print(min(x))
print(sum(x))
print('-----')
a = 'ABC'
b = 'DEF'
c = 'GHI'
d = [1, 2, 3]
print(list(zip(a, b, c)))
print('-----')
print(zip(a, d))
for i in zip(a, d):
    print(i)

def loopy(x):
    return x * 2

print(list(map(loopy, [1, 2, 3])))
print(list(map(loopy, 'ABC')))
print(list(map(lambda x : x ** 2, [1, 2, 3])))


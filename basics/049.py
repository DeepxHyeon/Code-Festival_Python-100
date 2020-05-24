# list, tuple, set, dict

a = 'loopy'
print(list(a))
print(tuple(a))
print(list(tuple(a)))
print(set(a))
# print(dict(a))

# 0008
# 0080
# 0800
# 8000
print(str(list(range(10000))).count('8'))
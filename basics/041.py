s = 'asdfqfzxcvdfuqerhfsadofjsadfnqoefqo'
print(set(s))
print(len(set(s)))

count = 0
for i in set(s):
    count += 1
print(count)
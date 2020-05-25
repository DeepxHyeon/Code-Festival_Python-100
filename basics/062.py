file = open('sample.txt', 'r')

'''
file.write('hello world')
file.write('\n')
file.write('hello world')
file.close()
'''

# print(dir(file))
# print(file.readline())
# print(file.readline())
# print(file.readline())
print(file.read())
file.close()
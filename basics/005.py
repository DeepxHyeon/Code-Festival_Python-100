name = 'dohyeon'
age = 20
n = 88888888.888888
s = '제 이름은 %s입니다. 제 나이는 %d입니다.'

print(s % (name, age))
print('제 이름은 {}입니다. 제 나이는 {}입니다.'.format(name, age))

s = '제 이름은 {name}입니다. 제 나이는 {age}입니다.'

print(s.format(name = 'dohyeon', age = 20))
print('{0:4} X {1:4} = {2:4}'.format(2, 3, 6))
print('{0:<4} X {1:<4} = {2:<4}'.format(2, 3, 6))
print('{0:.3f}'.format(1/4.0))
print('{0:.4f}'.format(1/4.0))
print('{0:,.3f}'.format(n))
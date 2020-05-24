l = [100, 200, 300]
t = (100, 200, 300)
print(id(l))

def change(i):
    print(id(i))
    i[0] = 10000
    
change(l)
print(l)
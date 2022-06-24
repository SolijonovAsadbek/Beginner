a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

if a < b < c :
    a, b, c = 2*a, 2*b, 2*c
else:
    a, b, c = -a, -b, -c

print('a: ', a)
print('b: ', b)
print('c: ', c)
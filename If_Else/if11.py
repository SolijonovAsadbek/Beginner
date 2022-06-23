a = int(input('a: '))
b = int(input('b: '))

if a != b and a > b:
    b = a
elif a != b and b > a:
    a = b
else:
    a, b = 0, 0
print('a:', a)
print('b:', b)




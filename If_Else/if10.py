a = int(input('a: '))
b = int(input('b: '))

if a != b:
    summ = a + b
    a, b = summ, summ
else:
    a = 0
    b = 0

print('a:', a)
print('b:', b)

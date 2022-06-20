a = int(input('a son: '))
b = int(input('b son: '))
c = int(input('c son: '))

cond1 = a == b != c
cond2 = c == a != b
cond3 = b == c != a
cond4 = a == b == c

cond = cond1 or cond2 or cond3 or cond4
print(f'{a}, {b} va {c} sonlaridan hech bo`ganda ikkitasi tengmi? :{cond}')

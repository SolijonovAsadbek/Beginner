a = int(input('a son: '))
b = int(input('b son: '))
c = int(input('c son: '))

shart1 = a == -b
shart2 = a == -c
shart3 = b == -c

naatija = shart1 or shart2 or shart3
print(f'{a}, {b} va {c} sonlardan hech bo`lmaganda bir o`zaro qarama qarshimi? : {naatija}')

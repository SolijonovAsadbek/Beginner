a = int(input('A kesma: '))
b = int(input('B kesma: '))
A = a
count = 0
while a >= b:
    count += 1
    a -= b
print(f'{A} kesmada {b} kesma {count} marta joylasha oladi.')

n = int(input('n: '))

summa = 0

for i in range(n, 2 * n + 1):
    summa += i ** 2
print(f'{n} dan {2 * n} gacha sonlar yig`indisi: {summa} ga teng.')


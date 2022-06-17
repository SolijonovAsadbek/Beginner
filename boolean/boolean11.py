a = int(input('a son: '))
b = int(input('b son: '))
natija = (a % 2 == 0 and b % 2 == 0) or (a % 2 == 1 and b % 2 == 1)
print(f'{a} va {b} son ikkilasi ham juft yoki toq: {natija}.')

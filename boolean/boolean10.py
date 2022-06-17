a = int(input('a son: '))
b = int(input('b son: '))
natija = (a % 2 == 1 and b % 2 != 1) or (a % 2 != 1 and b % 2 == 1)
print(f'Natija: {a} va {b} sonlar faqat bitasi toq : {natija}')

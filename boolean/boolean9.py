a = int(input('a son: '))
b = int(input('b son: '))
toq_a = a % 2 == 1
toq_b = b % 2 == 1
natija = toq_a or toq_b
print(f'{a} va {b} sonlar ichida hech bo`lmaganda faqat bittasi toq : {natija}.')

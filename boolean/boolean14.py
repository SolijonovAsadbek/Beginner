a = int(input('a son: '))
b = int(input('b son: '))
c = int(input('b son: '))
shart1 = (a > 0) and (b < 0) and (c < 0)
shart2 = (b > 0) and (a < 0) and (c < 0)
shart3 = (c > 0) and (a < 0) and (b < 0)
natija = shart1 or shart2 or shart3
print(f'Natija {a},{b}, va {c} sonlar  faqat bittasi  musbat: {natija}')

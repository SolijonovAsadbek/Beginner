a = int(input('a son: '))
b = int(input('b son: '))
c = int(input('b son: '))
natija = ((a > 0) and (b > 0) and (c < 0)) or ((b > 0) and (a < 0) and (c > 0)) or ((c > 0) and (a > 0) and (b < 0))

print(f'Natija {a},{b}, va {c} sonlar  hech bo`lmaganda iktasi  musbat: {natija}')

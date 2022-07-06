a = int(input('a son: '))
rooms = 1
while a > 0:
    end = a % 10
    print(f'{rooms} lar xonasi: ', end, ' ga teng.')
    rooms *= 10
    a //= 10

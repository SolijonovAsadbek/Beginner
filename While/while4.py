n = int(input('n son: '))
dg_3 = 3
count = 1
while n >= dg_3:
    if dg_3 == n:
        print(f'3 ning darajasida {count}')
        break
    if dg_3 > n:
        print('3 ning darajasi emas')
        break
    dg_3 *= 3
    count += 1
else:
    if n == 1:
        print('3 ning drajasida 0')
    else:
        print('3 ning darajasi emas')
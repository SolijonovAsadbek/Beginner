n = int(input('n son: '))
mult = 1
while n >= 1:
    mult *= n
    n -= 2
    if n == 0:
        break
print('Sonlar ko`paytasi:', mult)

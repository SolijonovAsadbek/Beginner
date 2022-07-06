n = int(input('n son: '))
count = 0
summa = 0
while summa <= n:
    if summa == n:
        break
    count += 1
    summa += count
print('k:', count)
print('yig`indi:', summa)
# print(*list(range(1, count + 1)), sep='+', end='')
# print('=', summa, sep='', end='')

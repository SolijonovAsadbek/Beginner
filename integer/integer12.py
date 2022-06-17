x = int(input('Uch xonali son: '))
bir = x % 10
on = (x // 10) % 10
yuz = x // 100
y = bir * 100 + on * 10 + yuz
print(f'{x} son teskarisi: {y}')

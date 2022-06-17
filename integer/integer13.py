x = int(input('Uch xonali son: '))
bir = x % 10
on = (x // 10) % 10
yuz = x // 100
uch = on * 100 + bir * 10 + yuz
print(f'{x} son almashtirildi: {uch}')

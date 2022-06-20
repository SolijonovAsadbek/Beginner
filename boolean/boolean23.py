a = int(input('uch xonali son: '))
yuz = a // 100
on = (a // 10) % 10
bir = a % 10
b = bir * 100 + on * 10 + yuz
natija = a == b
print(f'{a} soni teskari o`qiganda ham bir xil chiqadimi? : {natija}')

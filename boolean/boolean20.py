a = int(input('uch xonali son: '))
yuz = a // 100
on = (a // 10) % 10
bir = a % 10

natija = yuz != on != bir and yuz != bir
print(f'Berilgan soning raqamlari har xil raqamlarimi? : {natija}')

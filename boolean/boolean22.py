a = int(input('uch xonali son: '))
yuz = a // 100
on = (a // 10) % 10
bir = a % 10

natija = yuz < on < bir or yuz > on > bir
print(f'{a} soni raqamlari o`sish tartibidami? : {natija}')

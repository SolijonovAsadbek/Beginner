a = int(input('A: '))
b = int(input('B: '))
count = 0
while a >= b:
    a -= b
    count += 1
print('Qoldiq: ', a)
print('Butun qismi: ', count)

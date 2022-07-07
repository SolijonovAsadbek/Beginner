# begin1
# a = float(input('Kvadrat tomonini a: '))
# P = 4 * a
# print("Kvadratning perimetri: ", P)

# begin2
# a = float(input('Kvadratning tomoni a: '))
# S = a * a
# print('Kvadratning yuzasi: ', S)

# begin4
# import math
# d = float(input('Aylananing diametri d: '))
# L = math.pi * d
# print("pi: ", math.pi)
# print('Aylananing uzunligi: ', L)


# begin5
# a = float(input('Kub tomoni a: '))
# V = a ** 3
# S = 6 * a ** 2
# print('Kubning hajmi: ', V)
# print('Kubning to\'la sirti: ', S)


# begin6
# a = float(input('a: '))
# b = float(input('b: '))
# c = float(input('c: '))
#
# V = a * b * c
# S = 2 * (a * b + a * c + b * c)
# print('Paralelopipedning hajmi: ', V)
# print('Paralelopipedning to\'la sirti: ', S)


# begin7
# import math
#
# r = float(input('Doiraning radiusi r: '))
# L = 2 * math.pi * r
# S = math.pi * r ** 2
# print('Doiraning yuzi: ', S)
# print('Doiraning uzunligi: ', L)


# begin8
# a = float(input('a: '))
# b = float(input('b: '))
#
# avg = (a + b) / 2
# print('Ikki sonning o\'rta arifmetigi avg: ', avg)


# begin9
# import math
#
# a = float(input('a: '))
# b = float(input('b: '))
# geo = math.sqrt(a * b)
# print('Ikki sonnining o\'rta geometrigi geo: ', geo)


# begin10
# x = float(input('x: '))
# y = float(input('y: '))
#
# add = x + y
# multiple = x * y
# square_x = x ** 2
# square_y = y ** 2
# print('Natija: ')
# print(f'{x} + {y} = {add}')
# print(f'{x} * {y} = {multiple}')
# print(f'|{x}| = {square_x}')
# print(f'|{y}| = {square_y}')


# begin11
# x = float(input('x: '))
# y = float(input('y: '))
#
# add = x + y
# multiple = x * y
# modul_x = abs(x)
# modul_y = abs(y)
# print('Natija: ')
# print(f'{x} + {y} = {add}')
# print(f'{x} * {y} = {multiple}')
# print(f'|{x}| = {modul_x}')
# print(f'|{y}| = {modul_y}')


# begin12
# import math
# a = float(input('katet a: '))
# b = float(input('katet b: '))
#
# c = math.sqrt(a*a + b*b)
# P = a + b + c
#
# print('To`g`ri uchburchakning gipotenuzasi c: ', c)
# print('To`g`ri uchburchakning perimetiri P: ', P)


# begin13
# begin14
# begin15

# begin16
# x1 = float(input('nuqta x1: '))
# x2 = float(input('nuqta x2: '))
# M = abs(x2-x1)
# print('Ikki nuqta orasidagi masofa: abs(): ', M)


# abs() - funksiyaning vazifasi doim ikki nuqta
# orasidagi masofa uchun ishlatiladi.

# Sababi: Nuqtalar orasidagi masofa hech qachon
# manfiy son bo'lmasligi kerak


# begin20
import math

x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f'({x1}, {y1}) dan ({x2}, {y2}) koordinatagacha bo`lgan masofa d: ', distance)

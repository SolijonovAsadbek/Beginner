# range - funksiyasini ishlashi
rang = range(1, 12)
print(rang)
print(list(rang))

# dinamik sikl hosil qilish
a = int(input('Sanab ber: '))
for i in range(1, a + 1):
    print(i)


# qadam qo`shish
for item in range(40, 91, 12):
    print(item, end=',')

# Tekari tartibda sanash
for item in range(10, 0, -1):
    print(item, end=', ')

# Tekari tartibda sakrab sanash
for item in range(10, 0, -4):
    print(item, end=', ')
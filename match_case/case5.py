a = int(input('a: '))
b = int(input('b: '))
amal_son = int(input('amal son: '))
match amal_son:
    case 1:
        result = a + b
    case 2:
        result = a - b
    case 3:
        result = a * b
    case 4:
        result = a / b
    case _:
        result = 'Xato'
print(result)

kg = float(input('kilogramm: '))
command = int(input('Kamanda: '))

match command:
    case 1:
        result = f'{kg} kilogramm.'
    case 2:
        result = f'{kg * 1000000} milligramm.'
    case 3:
        result = f'{kg * 1000} gramm.'
    case 4:
        result = f'{kg / 1000} tonna .'
    case 5:
        result = f'{kg / 100} sentner.'
    case _:
        result = 'Xato'
print(result)

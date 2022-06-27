m = float(input('Metr: '))
command = int(input('Kamanda: '))

match command:
    case 1:
        result = f'{m * 10} detsimetr.'
    case 2:
        result = f'{m / 1000} kilometr.'
    case 3:
        result = f'{m} metr.'
    case 4:
        result = f'{m * 1000} millimetr.'
    case 5:
        result = f'{m * 100} santimetr.'
    case _:
        result = 'Xato'
print(result)

oy = int(input('Oy tartib raqami? : '))
fasl = ''
match oy:
    case 1:
        fasl = 'Qish'
    case 2:
        fasl = 'Qish'
    case 3:
        fasl = 'Bahor'
    case 4:
        fasl = 'Bahor'
    case 5:
        fasl = 'Bahor'
    case 6:
        fasl = 'Yoz'
    case 7:
        fasl = 'Yoz'
    case 8:
        fasl = 'Yoz'
    case 9:
        fasl = 'Kuz'
    case 10:
        fasl = 'Kuz'
    case 11:
        fasl = 'Kuz'
    case 12:
        fasl = 'Qish'
    case _:
        fasl = 'Xato'
print('Fasl:', fasl)

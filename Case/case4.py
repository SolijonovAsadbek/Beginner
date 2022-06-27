moonth_num = int(input('oy raqami: '))

match moonth_num:
    case 1:
        days = 31
    case 2:
        days = 28
    case 3:
        days = 31
    case 4:
        days = 30
    case 5:
        days = 31
    case 6:
        days = 30
    case 7:
        days = 31
    case 8:
        days = 31
    case 9:
        days = 30
    case 10:
        days = 31
    case 11:
        days = 30
    case 12:
        days = 31
    case _:
        days = 'Error'
print(days)

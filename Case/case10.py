y = input('Yo`nalish: ')
k = int(input('Kamanada: '))

direction = str()
match y:
    case 's':
        direction += 'Shim12ol '
    case 'j':
        direction += 'Janub '
    case 'q':
        direction += 'Sharq '
    case 'g':
        direction += 'G`arb '
    case _:
        direction += 'Xato '

match k:
    case 0:
        direction += 'Harakatni davom ettir.'
    case 1:
        direction += 'Chapga buril'
    case 2:
        direction += 'O`nga buril'
    case _:
        direction += 'Xato'

print('Yo`nalish: ', direction)

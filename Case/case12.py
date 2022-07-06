import math

num = int(input('son: '))

match num:
    case 1:
        r = float(input('Doira radiusini kiriting: '))
        D = 2 * r
        L = 2 * math.pi * r
        S = math.pi * r ** 2
        print('Doirani diametri:', D)
        print('Doirani uzunligi:', L)
        print('Doirani yuzasi:', S)
    case 2:
        D = float(input('Doira diamerini kiriting: '))
        r = D / 2
        L = 2 * math.pi * r
        S = math.pi * r ** 2
        print('Doirani radiusi:', r)
        print('Doirani uzunligi:', L)
        print('Doirani yuzasi:', S)
    case 3:
        L = float(input('Doira uzunligini kiriting: '))
        D = L / math.pi
        r = D / 2
        L = 2 * math.pi * r
        S = math.pi * r ** 2
        print('Doirani diametri:', D)
        print('Doirani radiusi:', r)
        print('Doirani yuzasi:', S)
    case 4:
        S = float(input('Doira yuzasini kiriting: '))
        r = math.sqrt(S / math.pi)
        D = 2 * r
        L = 2 * math.pi * r
        S = math.pi * r ** 2
        print('Doirani diametri:', D)
        print('Doirani uzunligi:', L)
        print('Doirani radiusi:', r)

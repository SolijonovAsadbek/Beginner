a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

if a > b > c or b > a > c:
    print('eng kichigi c: ', c)
elif a > c > b or c > a > b:
    print('eng kichigi b: ', b)
elif b > c > a or c > b > a:
    print('eng kichigi a: ', a)

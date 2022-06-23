a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

if a > b > c or c > b > a:
    print('o`rachasi b: ', b)
elif a > c > b or b > c > a:
    print('o`rachasi c: ', c)
elif b > a > c or c > a > b:
    print('o`rachasi a: ', a)

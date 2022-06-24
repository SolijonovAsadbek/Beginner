a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

if a == b and a != c:
    print(f'c: {c} 3-tartib')
elif a == c and a != b:
    print(f'b: {b} 2-tartib')
elif b == c and b != a:
    print(f'a: {a} 1-tartib')


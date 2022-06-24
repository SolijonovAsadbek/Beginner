a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

ac = a + c
bc = b + c
ab = a + b
if ac > bc > ab or ac > ab > bc:
    print(f'{a} + {c} = {ac}')
elif bc > ac > ab or bc > ab > ac:
    print(f'{b} + {c} = {bc}')
else:
    print(f'{a} + {b} = {ab}')

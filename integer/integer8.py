son = int(input('Ikki xonali son: '))
on = son // 10    # // - butun bo'lish uchun ishlatiladi.
bir = son % 10    # % - qoldiqli bo`lish uchun ishlatiladi.
add = on + bir*10
print(f'O`nlar xonasi: {on}')
print(f'Birlar xonasi: {bir}')
print(f'{bir}*{10} + {on} = {add}')

n = int(input('n kesma: '))
k = int(input('k kesma: '))
N = n
count = 0
while n >= k:
    n -= k
    count += 1
print(f'{N} kesmada {k} kesmani {count} marta joylashtira olamiz.\nQoldiq: {n}')

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))

katta = int()
kichik = int()
if a > b > c:
    katta = a
    kichik = c
elif a > c > b:
    katta = a
    kichik = b
elif b > a > c:
    katta = b
    kichik = c
elif b > c > a:
    katta = b
    kichik = a
elif c > a > b:
    katta = c
    kichik = b
elif c > b > a:
    katta = c
    kichik = a

print('kattasi : ', katta)
print('kichigi :', kichik)

pul = int(input('summa: '))
import random

kun = 0
clock = 0
while pul >= -17900:
    soat = random.randint(1, 6)
    clock += soat
    pul -= soat * 420
    kun += 1

print('kun: ', kun)
print('qarz: ', pul)
print('soat: ', clock)
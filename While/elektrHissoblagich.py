pul = 12000
import random

kun = 0
clock = 0
while pul >= -20000:
    soat = random.randint(1, 6)
    clock += soat
    pul -= soat * 420
    kun += 1

print('kun: ', kun)
print('pul: ', pul)
print('soat: ', clock)
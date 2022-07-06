n = int(input('n: '))

mult = 1
for i in range(1, n + 1):
    for j in range(1, 10):
        mult *= (i + j / 10)
print(mult)

n = int(input('n son: '))
count = 0

while 3 ** count <= n:
    count += 1
    if 3 ** count > n:
        count -= 1
        break
print(count)
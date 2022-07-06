n = int(input('n son: '))
count = 0

while count ** 2 < n:
    count += 1
    if count ** 2 > n:
        count -= 1
        break

print(count)

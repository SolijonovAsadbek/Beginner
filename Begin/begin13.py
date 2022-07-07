import math

R1 = float(input('R1: '))
R2 = float(input('R2: '))
S1 = math.pi * R1 ** 2
S2 = math.pi * R2 ** 2
S3 = math.pi * (R1 ** 2 - R2 ** 2)

print(f'S1 doira yuzi: {S1}')
print(f'S2 doira yuzi: {S2}')
print(f'S3 doira yuzi => {S1} - {S2} = {S3}')

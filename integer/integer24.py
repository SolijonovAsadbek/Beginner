# 0 - yakshanba
# 1 - dushanba
# 2 - Seshanba
# 3 - Chorshanba
# 4 - Payshanba
# 5 - Juma
# 6 - Shanba
K = int(input("K butun son: "))

hafta_kunlari = ['Yakshanba', 'Dushanba',
                 'Seshanba', 'Chorshanba',
                 'Payshanba', 'Juma',
                 'Shanba']
kun = hafta_kunlari[K % 7]
print(f'{K}-kun {kun}')

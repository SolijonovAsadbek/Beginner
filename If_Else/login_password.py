from login import login
from password import password

log = input('login: ')
pas = int(input('password: '))

if log == login and pas == password:
    print('Welcome!')
else:
    print('I don`t know!' )
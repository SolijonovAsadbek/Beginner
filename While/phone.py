import datetime

money = int(input('Pul : '))
times = 0
formula = (money / 100) * 60
import time

start = datetime.datetime.now()
while times < formula:
    time.sleep(1)
    times += 1
    print('\rSiz aloqadasiz: ', times, ' sekund', end='', sep='')
else:
    print('\rQo`ng`roq yakunlandi.Mablag` tugadi.', end='\n')
end = datetime.datetime.now()
print('Pul miqdori: ', money, 'so`m.')
print('Gaplashilgan vaqt: ', formula, 'sekund.')
print('Boshlangan vaqti: ', start)
print('Tugagan vaqti: ', end)


count = 0
import datetime

begin_time = datetime.datetime.now()
# While - cheksiz sikl hosil qilishda ishlatiladi.
while count < 10:
    count += 1
    print(count)
end_time = datetime.datetime.now()
print('Oraliq vaqt: ', end_time - begin_time)
